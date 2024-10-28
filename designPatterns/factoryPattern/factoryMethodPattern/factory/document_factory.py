from abc import ABC, abstractmethod


class DocumentFactory(ABC):

    @abstractmethod
    def create_document(self):
        pass

    def open_document(self):
        document = self.create_document()
        return document.open()
