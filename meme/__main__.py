from argparse import ArgumentParser

from meme import generate_meme

parser = ArgumentParser(description="Generates meme and prints their path")
parser.add_argument("--path", type=str, required=False, nargs="?",
                    default=None,
                    help="path to an image file")
parser.add_argument("--body", type=str, required=False, nargs="?",
                    default=None,
                    help="quote body to add to the image")
parser.add_argument("--author", type=str, required=False, nargs="?",
                    default=None,
                    help="quote author to add to the image")
args = parser.parse_args()
print(generate_meme(args.path, args.body, args.author))
