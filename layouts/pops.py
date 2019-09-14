from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from modulos.sorteio import basico, retorno_unico, retorno_duplo


class PopEspecial(Popup):
    main_screen = StringProperty('')
    size_hint = ListProperty([0.5,0.3])
    title = StringProperty('Sair')
    label_content = StringProperty('')
    # __events__ = ('left_button', 'right_button')


    def __init__(self, **kwargs):
        super(PopEspecial, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.botoes = BoxLayout()
        self.lab = Label(text=self.label_content)

        self.botao1 = Button(text='Sim', on_release=self.on_left_button)
        self.botao2 = Button(text='Não', on_release=self.on_right_button)

        self.botoes.add_widget(self.botao1)
        self.botoes.add_widget(self.botao2)

        self.box.add_widget(self.lab)
        self.box.add_widget(self.botoes)
        self.add_widget(self.box)


    def on_left_button(self, *args):
        pass

    def on_right_button(self, *args):
        # IMPORTANTE!!!!!
        # Abaixo temos uma forma de trocar de tela mesmo estando
        # fora do escopo da tela atual
        self.dismiss()
        App.get_running_app().root.current = self.main_screen

class PopSortear(Popup):
    '''
        Utilizado para apresentar na tela os resultados obtidos
        dos sorteios realizados.
    '''

    lab_content = StringProperty('Deseja realizar o sorteio?')
    size_hint = ListProperty([0.5,0.3])
    title = StringProperty('Sair')
    ''' incluir aqui um sistema de recepção de Tipos de sorteio, para que a tela
    e a operação corretas sejam apresentadas ao usuário'''
    def __init__(self, instancia, tela, **kwargs):
        super(PopSortear, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.botoes = BoxLayout()
        self.lab = Label(text=self.lab_content)
        self.tela = tela

        self.botao1 = Button(text='Sim')
        if tela == 'basico':
            self.botao1.bind(on_release=self.preparando)
        elif tela == 'Retorno Unico':
            self.botao1.bind(on_release=self.sorteio_unico)
        elif tela == 'Retorno Duplo':
             self.botao1.bind(on_release=self.preparando)
        self.botao2 = Button(text='Não')
        self.botao2.bind(on_release=self.sem_salvar)

        self.botoes.add_widget(self.botao1)
        self.botoes.add_widget(self.botao2)

        self.box.add_widget(self.lab)
        self.box.add_widget(self.botoes)
        self.add_widget(self.box)

        self.instancia = instancia

    def preparando(self, *args):
        # print((self.instancia.lista_completa, '', self.instancia.lista2))
        # print('salvou')
        lista_completa = []
        lista2 = []
        lista1 = []
        if self.tela == 'basico':
            for widget in self.instancia.ids.box1.walk():
                # if type(widget) != type():
                try:
                    if widget.text != 'X' and widget.text != 'Sortear':
                        lista_completa.append(widget.text)
                except:
                    pass
            for widget in self.instancia.ids.box2.walk():
                try:
                    if widget.text != 'X' and widget.text != 'Sortear':
                        lista2.append(widget.text)
                except:
                    pass
        else:
            for widget in self.instancia.ids.sroll_duplo1.walk():
                # if type(widget) != type():
                try:
                    if widget.text != 'X' and widget.text != 'Sortear':
                        lista_completa.append(widget.text)
                except:
                    pass
            for widget in self.instancia.ids.scroll_duplo2.walk():
                try:
                    if widget.text != 'X' and widget.text != 'Sortear':
                        lista2.append(widget.text)
                except:
                    pass


        for i in lista_completa:
            if i not in lista2:
                lista1.append(i)

        while len(lista1) != len(lista2):
            if len(lista1) > len(lista2):
                lista2.append('---')
            else:
                lista1.append('---')

        # print(lista1, '\n', lista2)
        if self.tela == 'basico':
            result = basico(lista1, lista2)
            pop_result = PopResult(result, 'basico')
            pop_result.open()

            self.dismiss()
        else:
            result = retorno_duplo(lista1, lista2)
        # print(result)
            pop_result = PopResult(result, 'Retorno Duplo')
            pop_result.open()

            self.dismiss()

    def sorteio_unico(self, *args):
        lista = []
        for widget in self.instancia.ids.scroll_unico.walk():
            try:
                if widget.text != 'X' and widget.text != 'Sortear':
                    lista.append(widget.text)
            except:
                pass
        result = retorno_unico(lista)
        pop_result = PopResult(result, 'Retorno Unico')
        pop_result.open()

    def sem_salvar(self, *args):
        self.dismiss()

class PopResult(Popup):
    ''' Apresenta os resultados em forma de tabela ou de Label
    simples, no caso de sorteios que apresentam grande quantidade
    de valores, um sistema de scroll é adicionado, exemplo é o
    sorteio simples'''
    def __init__(self, resultado, tipo, **kwargs):
        super(PopResult, self).__init__(**kwargs)
        self.size_hint = (.7, .5)
        self.resultado = resultado
        self.tipo = tipo
        self.title = "Resultado"
        self.box = ScrollView(do_scroll_x=False,do_scroll_y=True)
        self.add_widget(self.box)

        self.dados(self.resultado)

    def dados(self, dados):
        resultado = ''
        gdl = GridLayout(cols = 3)
        if self.tipo == 'basico':
            gdl.size_hint_y = None
            gdl.bind(minimum_height=gdl.setter('height'))
            for i in range(len(dados)):
                gdl.add_widget(Label(text=str(dados[i][0]), size_hint_y=None, height=40))
                gdl.add_widget(Label(text='|',size_hint_y=None, height=40))
                gdl.add_widget(Label(text=str(dados[i][1]),size_hint_y=None, height=40))

            self.box.add_widget(gdl)

        elif self.tipo == 'Retorno Unico':
            self.box.add_widget(Label(text=str(dados)))

        elif self.tipo == 'Retorno Duplo':
            gdl.add_widget(Label(text=str(dados[0])))
            gdl.add_widget(Label(text='|'))
            gdl.add_widget(Label(text=str(dados[1])))

            self.box.add_widget(gdl)
