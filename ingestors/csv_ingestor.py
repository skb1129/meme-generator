import pandas as pd

from models import QuoteModel
from ingestors.ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path):
        csv = pd.read_csv(path)
        return [QuoteModel(**row) for index, row in csv.iterrows()]
