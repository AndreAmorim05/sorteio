from kivy.app import App
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from sorteio import basico, retorno_unico


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

        self.botao1 = Button(text='Sim')
        if tela == 'basico':
            self.botao1.bind(on_release=self.preparando)
        elif tela == 'Retorno Unico':
            self.botao1.bind(on_release=self.sorteio_unico)
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

        for i in lista_completa:
            if i not in lista2:
                lista1.append(i)

        while len(lista1) != len(lista2):
            if len(lista1) > len(lista2):
                lista2.append('---')
            else:
                lista1.append('---')

        # print(lista1, '\n', lista2)

        result = basico(lista1, lista2)
        # print(result)
        pop_result = PopResult(result, 'basico')
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
    def __init__(self, resultado, tipo, **kwargs):
        super(PopResult, self).__init__(**kwargs)
        self.size_hint = (.7, .5)
        self.resultado = resultado
        self.tipo = tipo
        self.title = "Resultado"
        self.box = BoxLayout(orientation='vertical')
        self.lab = Label()

        self.box.add_widget(self.lab)
        self.add_widget(self.box)

        self.dados(self.resultado)

    def dados(self, dados):
        resultado = ''
        if self.tipo == 'basico':
            for i in range(len(dados)):
                if i == 0:
                    '''aqui eu desejo fazer com que a distancia dos valores sorteados sejam a
                    mesma, imitando uma tabela'''
                    resultado = f'{dados[i][0]:<7}' + '   <--->   '.format(end='') + f'{dados[i][1]:<7}'
                else:
                    resultado = resultado + '\n'.format(end='') + f'{dados[i][0]:<7}' + '   <--->   '.format(end='') + f'{dados[i][1]:<7}'
            self.lab.text = resultado

        elif self.tipo == 'Retorno Unico':
            self.lab.text = dados