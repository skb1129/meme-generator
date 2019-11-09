from ingestors import Ingestor

quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
               './_data/DogQuotes/DogQuotesDOCX.docx',
               './_data/DogQuotes/DogQuotesPDF.pdf',
               './_data/DogQuotes/DogQuotesCSV.csv']

for f in quote_files:
    print(Ingestor.parse(f))
