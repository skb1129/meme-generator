from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        file = open(path, "r", encoding="utf-8-sig")
        lines = file.readlines()
        file.close()
        return [QuoteModel(*quote.rstrip("\n").split(" - ")) for quote in lines]
