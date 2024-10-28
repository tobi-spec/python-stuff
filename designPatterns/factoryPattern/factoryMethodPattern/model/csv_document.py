from designPatterns.factoryPattern.factoryMethodPattern.model.document import Document


class CSVDocument(Document):

    def open(self):
        print("Open CSV document")
