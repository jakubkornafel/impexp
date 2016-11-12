#     Guidelines:
#     - Data - klasa która ma się składać z następujących metod:
#     - __init__ - przyjmuje argumenty data_source, importer, exporter
#     - my_import - wywołuje self.importer.process() i rezultat zapisuje w self.data
#     - export - wywołuje self.exporter.process()


class Data:
    def __init__(self, data_source, importer, exporter):
        self.data_source = data_source
        self.importer = importer
        self.exporter = exporter

    def my_import(self):
        self.data = self.importer.process()

    def export(self):
        self.exporter.process()
