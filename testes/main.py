from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
# from pops import PopEspecial

# class PopEspecial(PopEspecial):
#     size_hint = (.5, .3)
#     def __init__(self, **kwargs):
#         super(PopEspecial, self).__init__(**kwargs)
#         self.size_hint = (.5, .3)

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tela1(Screen):
    def salvar(self):
        print('Funcionou!')

class Teste(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    Teste().run()


#todo OBS: estou tentando fazer com que meu programa tenha o mínimo possível de
# código no main.py, separando assim em módulos e objetos separados em pastas.
# O problema mais recente que encontrei foi no Objeto PopEspecial, o qual busco
# criar um widget alterado, a dificuldade maior está em fazer com que os eventos
# on_left_button e on_right_button sejam replaceable(substituíveis).