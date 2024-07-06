from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class ChatBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.input = TextInput(size_hint_y=None, height=40)
        self.add_widget(self.input)
        
        self.button = Button(text='Send', size_hint_y=None, height=40)
        self.button.bind(on_press=self.send_message)
        self.add_widget(self.button)
        
        self.response = Label()
        self.add_widget(self.response)
    
    def send_message(self, instance):
        user_message = self.input.text
        response = requests.post('http://127.0.0.1:5000/chat', json={'message': user_message})
        self.response.text = 'Bot: ' + response.json().get('reply', '')

class ChatApp(App):
    def build(self):
        return ChatBox()

if __name__ == '__main__':
    ChatApp().run()