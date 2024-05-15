from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.graphics import Color, Rectangle
from kivy.uix.filechooser import FileChooserIconView

class CustomFileChooser(FileChooserIconView):
    def is_hidden(self, fn):
        
        if fn.startswith('C:\\Windows\\'):
            return True
        return super(CustomFileChooser, self).is_hidden(fn)

         
Window.size = (400, 620)

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.name = 'settings'
        
        # Layout principal
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(None, None), size=(400, 620))
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Cor branca
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        
        # Título
        title_label = Label(text="Configurações", font_size=30, size_hint=(1, None), height=50, color=(0, 0, 0, 1), font_name="times")
        layout.add_widget(title_label)
        
        # Foto de perfil e botão para editar
        profile_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.profile_image = Image(source="C:\\Users\\lulusinha\\Downloads\\18765757-icone-de-perfil-de-usuario-em-estilo-simples-ilustracao-em-avatar-membro-no-fundo-isolado-conceito-de-negocio-de-sinal-de-permissao-humana-vetor.jpg", size_hint=(None, None), size=(100, 100), allow_stretch=True)
        self.edit_profile_button = Button(text="Editar Foto", size_hint=(1, None), height=50, background_color=(1, 0.8, 0.8, 1), font_size=15, font_name="times")
        self.edit_profile_button.bind(on_press=self.open_filechooser)  # Associa a função open_filechooser ao pressionar o botão
        profile_layout.add_widget(self.profile_image)
        profile_layout.add_widget(self.edit_profile_button)
        layout.add_widget(profile_layout)
        
        # Botão de idioma e menu suspenso
        language_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        language_label = Label(text="Idioma:", font_size=16, size_hint=(0.2, None), height=50, color=(0, 0, 0, 1))
        self.language_spinner = Spinner(text='Português', values=('Português', 'Inglês', 'Espanhol'), size_hint=(0.3, None), height=50, background_color=(1, 0.8, 0.8, 1), font_size=16, font_name="times")
        language_layout.add_widget(language_label)
        language_layout.add_widget(self.language_spinner)
        layout.add_widget(language_layout)
        
        # Botões de configurações
        buttons_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, 0.4))
        for text in ["Notificações", "Privacidade", "Conta"]:
            button = Button(text=text, size_hint=(1, None), height=50, background_color=(1, 0.8, 0.8, 1), font_size=16, font_name="times")
            buttons_layout.add_widget(button)
        layout.add_widget(buttons_layout)
        
        # Botão Voltar
        back_button = Button(text="Voltar", size_hint=(1, 0.1), background_color=(1, 0.8, 0.8, 1), font_size=16, font_name="times")
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'main'
    
    def open_filechooser(self, instance):
        filechooser = FileChooserIconView()
        filechooser.bind(on_submit=self.select_image)
        filechooser.bind(on_cancel=self.dismiss_popup)
        self._popup = Popup(title="Escolha uma imagem", content=filechooser, size_hint=(0.9, 0.9))
        self._popup.open()
    
    def select_image(self, instance, path):
        self.profile_image.source = path[0]
        self.dismiss_popup()
    
    def dismiss_popup(self, instance):
        self._popup.dismiss()

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = 'main'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(None, None), size=(400, 620))
        with layout.canvas.before:
            Color(1, 1, 1, 1)  # Cor branca
            self.rect = Rectangle(size=layout.size, pos=layout.pos)
        layout.add_widget(Label(text="Reencontre.me", font_size=40, size_hint=(1, 0.5), color=(0, 0, 0, 1), font_name="times"))
        
        # Adicionando o ícone da foto de perfil acima do título
        profile_icon = Image(source="C:\\Users\\lulusinha\\Downloads\\18765757-icone-de-perfil-de-usuario-em-estilo-simples-ilustracao-em-avatar-membro-no-fundo-isolado-conceito-de-negocio-de-sinal-de-permissao-humana-vetor.jpg", size_hint=(1, None), height=200, allow_stretch=True)
        layout.add_widget(profile_icon)
        
        settings_button = Button(text="Configurações", size_hint=(1, 0.05), background_color=(1, 0.8, 0.8, 1), font_size=20, font_name="times")
        settings_button.bind(on_press=self.go_to_settings)
        layout.add_widget(settings_button)
        
        self.add_widget(layout)
    
    def go_to_settings(self, instance):
        self.manager.current = 'settings'

class MyApp(App):
    def build(self):
        self.settings_screen = SettingsScreen()
        self.main_screen = MainScreen()
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.settings_screen)
        return self.screen_manager
    
if __name__ == "__main__":
    MyApp().run()
