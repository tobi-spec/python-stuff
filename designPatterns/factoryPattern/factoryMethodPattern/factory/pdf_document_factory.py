from designPatterns.factoryPattern.factoryMethodPattern.factory.document_factory import DocumentFactory
from designPatterns.factoryPattern.factoryMethodPattern.model.pdf_document import PDFDocument


class PDFDocumentFactory(DocumentFactory):

    def create_document(self):
        return PDFDocument()
