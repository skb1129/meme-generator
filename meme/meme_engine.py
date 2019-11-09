import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, "temp.jpg")
        real_height, real_width = img.size
        height = int(real_height * width / real_width)
        img.thumbnail((height, width))

        # Select font-family, font-size, color and position to draw text
        font1 = ImageFont.truetype("./_data/Fonts/Roboto-Bold.ttf", 22)
        font2 = ImageFont.truetype("./_data/Fonts/Roboto-Medium.ttf", 18)
        text_position = random.choice(range(30, height - 50))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        # Draw the text on image
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, fill, font1,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_position + 25), f"- {author}", fill, font2,
                  stroke_width=1, stroke_fill=stroke_fill)

        img.save(outfile, "JPEG")
        return outfile
