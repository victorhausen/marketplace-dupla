import json
class Controller:

    def __init__(self, path):
        self.path = path
    
    def create(self, data):
        self.arquivo = open(self.path, 'a')

        self.arquivo.write(str(data)+"\n")

        self.arquivo.close()
