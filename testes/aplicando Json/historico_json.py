from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
import random
import datetime

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Historico(Screen):
    def on_pre_enter(self, *args):
        pass

class Tela(Screen):
    def save_json(self):
        lista1 = []
        lista2 = []
        lista_final = []
        for i in range(0, 10):
            lista1.append(random.randint(0, 100))
            lista2.append(random.randint(-100, 0))

        for i in range(len(lista1)):
            lista_final.append([lista1[i], lista2[i]])
        print(lista_final)
        print(datetime.date.today())

class JsonTeste(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    JsonTeste().run()
