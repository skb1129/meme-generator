# Meme Module

This module has all the models and functions required for generating memes.

## Dependencies

[pillow](https://pillow.readthedocs.io/en/stable/) => This package is used to
draw text over images.

## Usage

Import and use `MemeEngine` class if you want to provide the image path, meme
body and author yourself.

Import and use `generate_meme` method if you to generate random memes.
This can also be to generate custom memes.

You can run this module in command line using the following command:
```
python -m meme --path <path_of_the_file> --body <quote_body> --author <quote_author>
```

## Models

### MemeEngine
This class takes an output directory path as an argument. Each instance keeps
count of the image generated. The `make_meme` method creates the meme image and
saves it in the provided output directory and returns a path to the created
meme. It uses the `pillow` library to resize image and draw text on it.
