import json
from carro import Car

class Dao:

    def read_json_content(self):
        with open("file_car.json", 'r', encoding="utf-8") as content:
            list_content = json.load(content)
        return list_content

    def add_car(self):

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
            print(f"o {new_vehicle.model} foi salvo")
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
