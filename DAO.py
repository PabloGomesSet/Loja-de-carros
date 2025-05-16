import json


from carro import Car

class Dao:

    def read_json_content(self): #Esta função somente é usada aqui dentro desta classe
        with open("file_car.json", 'r', encoding="utf-8") as content:
            list_content = json.load(content)
        return list_content

    def add_car(self):
        """16/05/2025: Na função add_car(), foi feita uma melhoria no print final, aquele
        que dá a mensagem de que o carro foi salvo"""

        with open('file_car.json', 'r', encoding="utf-8") as json_content:
            car_list =  json.load(json_content)

        model = input("modelo: ".upper())
        chassi = input("chassi: ".upper())
        mark = input("marca: ".upper())
        year_manufacture = input("ano : ".upper())
        price = input("preco: ".upper())

        new_vehicle = Car(model, chassi, mark, year_manufacture, price)

        validator = False
        for dict_vehicle in car_list:
            for car_attribute in dict_vehicle.values():
                if new_vehicle.chassi == car_attribute:
                    validator = True

        if validator == False:
            car_list.append(new_vehicle.criar_dicionario())

            with open("file_car.json", "w", encoding="utf-8" ) as list_updater:
                list_updater.write(json.dumps(car_list))
            print(f"o {new_vehicle.model}/ {new_vehicle.chassi}/"
                  f"{new_vehicle.mark}/ {new_vehicle.year} foi salvo.".upper())
        else:
            print("\nImpossível adicionar este veículo,\npois este número de chassi já "
                  "aparece nos registros.".upper() .center(100))


    def see_cars(self, search_criteria):
        car_list = self.read_json_content()

        for index, dict_vehicle in enumerate(car_list):
            if search_criteria in dict_vehicle.values():
                print(f"{index}º - "f"MODELO: {dict_vehicle["model"]} |".rjust(30),
                      f"CHASSI: {dict_vehicle["chassi"]}  |",
                      f"MARCA: {dict_vehicle["mark"]}  |",
                      f"ANO DE LANÇAMENTO: {dict_vehicle["year"]}  |",
                    f"R$ {dict_vehicle["price"]}")

    def excluir_carro(self, chassi):

        """16/05/2025: foi criada a função, que vai excluir um carro lá do json."""
        lista_de_carros = self.read_json_content()

        validator = False
        for dicionario_carro in lista_de_carros:
            if chassi in dicionario_carro.values():
                print(f"excluido o {dicionario_carro["model"]}/{dicionario_carro["chassi"]}/"
                      f"{dicionario_carro["mark"]}/{dicionario_carro["year"]}")
                lista_de_carros.remove(dicionario_carro)
                validator = True

        if validator == False:
            print(f"Nenhum veículo com este chassi {chassi} foi encontrado.")
        else:
            with open("file_car.json", "w", encoding="utf-8") as gravador:
                gravador.write(json.dumps(lista_de_carros))
            print("Veículo excluido com sucesso ...")