from flask import Flask, request, jsonify
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import threading

# Flask part
app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    return jsonify({'reply': user_message})

def run_flask():
    app.run(debug=True, use_reloader=False)

# Kivy part
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
    threading.Thread(target=run_flask).start()
    ChatApp().run()
