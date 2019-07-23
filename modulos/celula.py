from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from modulos.change_popup import ChPopup


class Celula(BoxLayout):
    size_hint_y = NumericProperty(None)
    height = NumericProperty(dp(70))
    text_button = StringProperty('')
    
    # id = 'box'
    def __init__(self, instancia, **kwargs):
        super(Celula, self).__init__(**kwargs)
        self.botoes = BoxLayout()  # size_hint_y=None, height=dp(100)

        self.botao1 = Button(text=self.text_button, on_release=self.chPop)
        self.botao2 = Button(size_hint_x=None, width=dp(30), text='X', on_release=self.delete_wid)

        self.botoes.add_widget(self.botao1)
        self.botoes.add_widget(self.botao2)
        self.add_widget(self.botoes)

        self.instancia = instancia
        self.change_popup = ChPopup(self) # text_button=self.text_button

    def chPop(self, *args):
        self.change_popup.open()


    def delete_wid(self, *args):
        self.parent.remove_widget(self)
