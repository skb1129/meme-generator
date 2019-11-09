import os
import random
import shutil

import requests
from flask import Flask, render_template, request

from meme import MemeEngine
from ingestors import Ingestor

app = Flask(__name__)

static_dir = "./static"
if os.path.exists(static_dir):
    shutil.rmtree(static_dir)
meme = MemeEngine(static_dir)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


def setup():
    """ Load all resources """
    quote_files = ["./_data/DogQuotes/DogQuotesTXT.txt",
                   "./_data/DogQuotes/DogQuotesDOCX.docx",
                   "./_data/DogQuotes/DogQuotesPDF.pdf",
                   "./_data/DogQuotes/DogQuotesCSV.csv"]
    all_quotes = []
    for f in quote_files:
        try:
            all_quotes.extend(Ingestor.parse(f))
        except ValueError as error:
            print(f"ValueError: {error}")

    images_path = "./_data/Photos/Dog/"
    all_images = []
    for root, dirs, files in os.walk(images_path):
        all_images = [os.path.join(root, name) for name in files]
    return all_quotes, all_images


quotes, images = setup()


@app.route("/")
def meme_rand():
    """ Generate a random meme """
    img = random.choice(images)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme """
    img = "./temp_image.jpg"
    image_url = request.form.get("image_url")
    img_data = requests.get(image_url, stream=True).content
    with open(img, "wb") as f:
        f.write(img_data)

    body = request.form.get("body", "")
    author = request.form.get("author", "")
    path = meme.make_meme(img, body, author)
    print(path)
    os.remove(img)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
