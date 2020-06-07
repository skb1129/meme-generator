import os
import subprocess

from ingestors.ingestor_interface import IngestorInterface
from ingestors.text_ingestor import TextIngestor


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text_file = './pdf_to_text.txt'
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)
        return quotes
