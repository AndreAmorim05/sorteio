from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import StringProperty

class ButtonStyle(ButtonBehavior, Label):
    source_image = StringProperty('')
    def __init__(self, **kwargs):
        super(ButtonStyle, self).__init__(**kwargs)
        self.atualizar()
        # self.background_down = ''

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=(get_color_from_hex('2BD62B')))
            Ellipse(size=(self.height, self.height),
                    pos=self.pos)
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + self.height/2.0, self.y))
            Image(pos=(self.x + self.height/4, self.y + self.height * 0.3),
                  source=self.source_image,
                  size=(self.height * 0.4, self.height * 0.4))

    def load_image(self):
        pass
# cor do ícone do botão F5F6F2
