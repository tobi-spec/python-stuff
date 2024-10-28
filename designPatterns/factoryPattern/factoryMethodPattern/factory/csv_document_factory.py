from designPatterns.factoryPattern.factoryMethodPattern.factory.document_factory import DocumentFactory
from designPatterns.factoryPattern.factoryMethodPattern.model.csv_document import CSVDocument


class CSVDocumentFactory(DocumentFactory):

    def create_document(self):
        return CSVDocument()