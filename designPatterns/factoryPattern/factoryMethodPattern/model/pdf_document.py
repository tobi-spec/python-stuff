from designPatterns.factoryPattern.factoryMethodPattern.model.document import Document


class PDFDocument(Document):

    def open(self):
        print("Open PDF document")
