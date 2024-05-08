from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image 


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.orientation = "vertical"
        self.spacing = 10
        self.padding = [50, 20]

       
        self.logo = Image(source='C:\\Users\\aluno.sesipaulista\\Downloads\\tabaio.png')
        self.add_widget(self.logo)

        self.username_input = TextInput(hint_text="Username", multiline=False)
        self.add_widget(self.username_input)

        self.password_input = TextInput(hint_text="Password", password=True, multiline=False)
        self.add_widget(self.password_input)

        self.login_button = Button(text="Login")
        self.login_button.bind(on_press=self.check_login)
        self.add_widget(self.login_button)

        self.error_label = Label(text="", color=(1, 0, 0, 1))
        self.add_widget(self.error_label)

    def check_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if username == "usuario" and password == "senha":
            self.error_label.text = "Login successful!"
        else:
            self.error_label.text = "Invalid username or password"


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
