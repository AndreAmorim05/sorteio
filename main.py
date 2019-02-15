from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from layouts.pops import PopSortear
from modulos.celula import *
from layouts.retorno_unico import *
import json

Config.set('graphics', 'height', 700)
Config.set('graphics', 'width', 500)

class PopSair(Popup):
    def salvar(self):
        pass

    def sem_salvar(self):
# IMPORTANTE!!!!!
# Abaixo temos uma forma de trocar de tela mesmo estando fora do escopo da tela atual
        App.get_running_app().root.current = 'telaincial'

class Manager(ScreenManager):
    pass

class TelaInicial(Screen):

    def on_pre_enter(self, *args):
        Window.bind(on_request_close=self.confirmacao)

    def confirmacao(self, *args, **kwargs):
        box = BoxLayout(orientation='vertical')
        botoes = BoxLayout()
        pop = Popup(title='Deseja sair?', content=box, size_hint=(None, None),
                    height=dp(150), width=dp(300))

        botao1 = Button(text='Sim', on_release=App.get_running_app().stop)
        botao2 = Button(text='Não', on_release=pop.dismiss)

        botoes.add_widget(botao1)
        botoes.add_widget(botao2)

        box.add_widget(botoes)

        pop.open()

        return True

class Tipos(Screen):
    def get_tipo(self, *args):
        tela = ''
        for widget in self.ids.box.walk():
            try:
                if widget.active:
                    print(widget.name)
                    tela = widget.name
                    widget.active = False
            except:
                pass
        if tela == 'Basico':
            App.get_running_app().root.current = 'basico'
        elif tela == 'Retorno Unico':
            App.get_running_app().root.current = 'Retorno Unico'
        # elif tela == 'Retorno Duplo':
        #     App.get_running_app().root.current = 'Retorno Duplo'
        # elif tela == 'Inteiro Positivo':
        #     App.get_running_app().root.current = 'Inteiro Positivo'

class Historico(Screen):

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27: # 27 corresponde ao código da tecla Esc
            App.get_running_app().root.current = 'telaincial'
            return True
        # print(key)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

class Basico(Screen):
    lista1 = ListProperty([])
    lista2 = ListProperty([])

    def __init__(self, **kwargs):
        super(Basico, self).__init__(**kwargs)


    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27: # 27 corresponde ao código da tecla Esc
            PopSair().open()
# importante, pois sem este return abrem-se os dois popups, de encerrar e de voltar
            return True

    def sem_salvar(self):
        App.get_running_app().root.current = 'telaincial'
        return True

    def sortear(self):
        pop = PopSortear(self)
        pop.open()


    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    def adicionar(self, texto):
        try:
            if texto != '':
                self.lista1.append(texto)
                self.ids.box1.add_widget(Celula(self, text_button=texto))
        except:
            print('Não foi possível adicionar uma nova célula')

    def adicionar2(self, texto):
        try:
            if texto != '':
                self.lista2.append(texto)
                self.ids.box2.add_widget(Celula(self, text_button=texto))
        except:
            print('Não foi possível adicionar uma nova célula')

class RetornoUnico(Screen):
    lista1 = ListProperty([])
    lista2 = ListProperty([])
    def adicionar(self, texto):
        try:
            if texto != '':
                # self.lista1.append(texto)
                self.ids.scroll_unico.add_widget(Celula(self, text_button=texto))
        except:
            print('Não foi possível adicionar uma nova célula')



class RetornoDuplo(Screen):
    pass

class IntPositivo(Screen):
    pass

class Principal(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    Principal().run()


# nomes = ['andré', 'gernam','jardielson', 'gislânio' ]
# temas = ['Exemplos','Exemplos','Avaliação Financeira','Avaliação Financeira']
# sorteio1 = [choice(nomes), choice(temas)]
# nomes.remove(sorteio1[0])
# temas.remove(sorteio1[1])
#
# sorteio2 = [choice(nomes), choice(temas)]
# nomes.remove(sorteio2[0])
# temas.remove(sorteio2[1])
#
# sorteio3 = [choice(nomes), choice(temas)]
# nomes.remove(sorteio3[0])
# temas.remove(sorteio3[1])
#
# sorteio4 = [choice(nomes), choice(temas)]
# nomes.remove(sorteio4[0])
# temas.remove(sorteio4[1])

# print(f'{sorteio1}\n{sorteio2}\n{sorteio3}\n{sorteio4}')
