from designPatterns.factoryPattern.factoryMethodPattern.model.document import Document


class WordDocument(Document):

    def open(self):
        print("Open word document")
