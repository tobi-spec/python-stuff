from designPatterns.factoryPattern.factoryMethodPattern.factory.csv_document_factory import CSVDocumentFactory
from designPatterns.factoryPattern.factoryMethodPattern.factory.pdf_document_factory import PDFDocumentFactory
from designPatterns.factoryPattern.factoryMethodPattern.factory.word_document_factory import WordDocumentFactory

pdf_factory = PDFDocumentFactory()
pdf_factory.open_document()

word_factory = WordDocumentFactory()
word_factory.open_document()

csv_factory = CSVDocumentFactory()
csv_factory.create_document().open()