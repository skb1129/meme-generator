import os

from ingestors.ingestor_interface import IngestorInterface, extensions
from ingestors.text_ingestor import TextIngestor
from ingestors.docx_ingestor import DocxIngestor
from ingestors.pdf_ingestor import PDFIngestor
from ingestors.csv_ingestor import CSVIngestor


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
