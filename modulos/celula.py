from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button, ButtonBehavior
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty
from modulos.change_popup import ChPopup
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase

import sys, os
# data_path = sys.path.append(os.path.abspath(os.path.join('..', 'data')))
data_path = os.path.abspath('data')

LabelBase.register(name='Lobster', fn_regular=os.path.join(data_path, 'Lobster-Regular.ttf'))


class Celula(BoxLayout):
    size_hint_y = NumericProperty(None)
    height = NumericProperty(dp(70))
    text_button = StringProperty('')
    
    # id = 'box'
    def __init__(self, instancia, **kwargs):
        super(Celula, self).__init__(**kwargs)
        self.botoes = BoxLayout(spacing=dp(1.5))

        self.botao1 = ButtonCollored(text=self.text_button, on_release=self.chPop, font_name='Lobster')

        self.botao2 = ButtonCollored(size_hint_x=0.16, text='X', on_release=self.delete_wid) #width=dp(30),

        self.botoes.add_widget(self.botao1)
        self.botoes.add_widget(self.botao2)
        self.add_widget(self.botoes)

        self.instancia = instancia
        self.change_popup = ChPopup(self)

    def chPop(self, *args):
        self.change_popup.open()


    def delete_wid(self, *args):
        self.parent.remove_widget(self)


class ButtonCollored(ButtonBehavior,Label):
    def __init__(self, **kwargs):
        super(ButtonCollored,self).__init__(**kwargs)
        self.atualizar()
        # self.font_name = 'Lobster'
        self.font_size = dp(20)

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()
    
    def on_state(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Color(rbga=get_color_from_hex('2abdb7')) 229072
            Color(rgba=((get_color_from_hex('2abdb7') if self.state == 'normal' else get_color_from_hex('0eeaca'))))
            RoundedRectangle(pos=self.pos, size=self.size, border=(50,50,50,50))
            Color(rgba=(get_color_from_hex('229072')))
            RoundedRectangle(size=(self.width - self.height*0.1, self.height - self.height*0.1),
            pos=(self.x + self.height*0.05 , self.y + self.height*0.05))