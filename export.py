# - AbstractExporter - klasa która mi składać się z następujących metod:
#     - __init__ - przyjmuje argument storage oraz data
#     - process - tutaj również chcemy podnieć wyjątek, który mówi że metoda nie została zaimplementowana - jak wyżej wybierz właściwy wyjątek.

class AbstractExporter:

    def __init__(self, storage, data):
        self.storage = storage
        self.data = data

    def process(self):
        raise NotImplementedError
