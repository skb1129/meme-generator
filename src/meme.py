import os
import random
from argparse import ArgumentParser

from .ingestors import Ingestor
from .meme_engine import MemeEngine
from .models import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    if path is None:
        images_dir = "./_data/Photos/Dog/"
        images = []
        for root, dirs, files in os.walk(images_dir):
            images = [os.path.join(root, name) for name in files]

        img_path = random.choice(images)
    else:
        img_path = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img_path, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = ArgumentParser(description="Generates meme and prints their path")
    parser.add_argument("path", type=str, required=False, nargs="?",
                        default=None,
                        help="path to an image file")
    parser.add_argument("body", type=str, required=False, nargs="?",
                        default=None,
                        help="quote body to add to the image")
    parser.add_argument("author", type=str, required=False, nargs="?",
                        default=None,
                        help="quote author to add to the image")
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
