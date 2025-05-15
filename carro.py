class Car:
    """classe modelo para os carro a serem cadastrados no sistema"""

    def __init__(self, model, chassi, mark, year, price):
        self.model = model
        self.chassi = chassi
        self.mark = mark
        self.year = year
        self.price = price

    def criar_dicionario(self):
       dict_car = {
           "model": self.model,
            "chassi": self.chassi,
           "mark": self.mark,
           "year": self.year,
           "price": self.price
       }
       return dict_car