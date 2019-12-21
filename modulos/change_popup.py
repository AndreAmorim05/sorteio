from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button


class ChPopup(Popup):
    text_button = StringProperty('')
    size_hint = ListProperty([0.5,0.3])
    pop_return = StringProperty('')
    title = text_button

    def __init__(self, celula_editar, **kwargs):
        ''' celula_editar captura o self da classe Celula do arquivo celula.py'''
        super(ChPopup, self).__init__(**kwargs)
        self.box = BoxLayout(orientation='vertical')
        self.botoes = BoxLayout()
        self.celula_root = celula_editar # atribuindo o self do Celula a uma variável
        self.text_button = self.celula_root.text_button

        self.left_bt = Button(text='Fechar')
        self.left_bt.bind(on_release=self.fechar)
        self.right_bt = Button(text='Salvar')
        self.right_bt.bind(on_release=self.salvar)
        self.celula = TextInput(text=self.text_button)

        self.botoes.add_widget(self.left_bt)
        self.botoes.add_widget(self.right_bt)

        self.box.add_widget(self.celula)
        self.box.add_widget(self.botoes)
        self.add_widget(self.box)


    def fechar(self, *args):
        # print('Deletou')
        self.dismiss()

    def salvar(self, *args):
        # import gb_variables
        ''' elemento de troca de valores na lista, neste trecho de código
        o erro occorrente é que sempre que tivermos o mesmo texto em mais de uma célula
        todos serão trocados.
        todo Objetivo: descobrir uma forma de encontrar exatamente o indíce e alterar apenas
        a célula desejada.
        '''
        if self.celula.text != '':
            for i in range(len(self.celula_root.instancia.lista1) - 1):
                if self.celula_root.instancia.lista1[i] == self.celula_root.botao1.text:
                    self.celula_root.instancia.lista1[i] = self.celula.text
            # self.celula_root.instancia.lista1 = self.celula.text #[self.celula_root.botao1.text]

            '''no próximo trecho de código utilizaremos os atributos da classe Celula 
            do arquivo celula.py, isto pelo fato de ter passado o argumento self ao 
            se inicializar este arquivo lá, fazendo assim com que todos os atributos
            que pertencem a ele seja acessados por self.celula_root.'''
            self.celula_root.botao1.text = self.celula.text
            self.title = self.celula.text
            self.dismiss()
            # gb_variables.alterar = self.celula.text
            # gb_variables.boolean = True
        else:
            print('celula vazia')
            self.celula.hint_text = 'Digite algum texto'
