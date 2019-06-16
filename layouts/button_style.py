from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.widget import Widget
from kivy.core.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import StringProperty
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage


class ButtonStyle(ButtonBehavior, Label):
    source_image = StringProperty('')
    def __init__(self, **kwargs):
        super(ButtonStyle, self).__init__(**kwargs)
        self.tex = Texture.create(size=(137, 80), colorfmt='rgba')
        self.atualizar()
        # self.background_down = ''

    def on_source_image(self, *args):
        self.tex = Image(self.source_image, color=(1,.5,.6,1)).texture
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()
    
    def on_state(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # trocar cor não funcionou
            Color(rgba=((get_color_from_hex('2BD62B') if self.state == 'normal' else get_color_from_hex('219321'))))
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height/2.0, self.y))
            Rectangle(pos=(self.x + self.height/4, self.y + self.height * 0.3),
                  size=(self.height * 0.4, self.height * 0.4),
                  texture=self.tex)            

# cor do ícone do botão F5F6F2
