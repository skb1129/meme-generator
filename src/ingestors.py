import os
import subprocess

import pandas as pd
from docx import Document

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx",
}


class IngestorInterface:
    @classmethod
    def verify(cls, file_extension):
        return file_extension in extensions.values()

    @classmethod
    def parse(cls, path):
        pass


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        file = open(path, "r", encoding="utf-8-sig")
        quotes = [quote.rstrip("\n") for quote in file.readlines()]
        file.close()
        return quotes


class DocxIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        document = Document(path)
        quotes = []
        for paragraph in document.paragraphs:
            quotes.append(paragraph.text)
        return quotes


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        text_file = '.pdf_to_text_temp.txt'
        cmd = f"pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        return TextIngestor.parse(text_file)


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        csv = pd.read_csv(path)
        quotes = [f"""{row.get("body", "")} - {row.get("author", "")}"""
                  for index, row in csv.iterrows()]
        return quotes


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        filename, file_extension = os.path.splitext(path)
        if not cls.verify(file_extension):
            raise ValueError("Unsupported file extension:", file_extension)
        if file_extension == extensions.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == extensions.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get("PDF"):
            return PDFIngestor.parse(path)
        if file_extension == extensions.get("CSV"):
            return CSVIngestor.parse(path)
