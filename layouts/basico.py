from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy.core.window import Window
from pops import PopSortear
from main import PopSair
from celula import Celula

'''
Neste arquivo desejo transferir o código do Layout do sorteio
Basico, porém o codigo do PopSair implementado no arquivo main 
está sendo acessado diretamente por lá e parte dele está sendo
escrito no arquivo principal.kv, o que está dificultando o acesso
por este arquivo.
'''

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