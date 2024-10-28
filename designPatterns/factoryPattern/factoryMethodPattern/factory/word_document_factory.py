from designPatterns.factoryPattern.factoryMethodPattern.factory.document_factory import DocumentFactory
from designPatterns.factoryPattern.factoryMethodPattern.model.word_document import WordDocument


class WordDocumentFactory(DocumentFactory):

    def create_document(self):
        return WordDocument()
