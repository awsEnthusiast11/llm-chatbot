from flask import Flask, request, render_template
import tkinter as tk
import threading
from tkinter import Text, Entry, Button, END
import model
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

def run_flask():
  app.run(port=5000)


def run_tkinter():
  root = tk.Tk()
  root.title("Chatbot")

  # Create the chatbot's text area
  text_area = Text(root, bg="white", width=50, height=20)
  text_area.pack()

  # Create the user's input field
  input_field = Entry(root, width=50)
  input_field.pack()

  # Create the send button
  send_button = Button(root, text="Send", command=lambda: send_message())
  send_button.pack()

  def send_message():
    # Get the user's input
    user_input = input_field.get()
    print(user_input)

    # Clear the input field
    input_field.delete(0, END)

    # Generate a response from the chatbot
    response = chatbot_response(user_input)

    # Display the response in the chatbot's text area
    text_area.insert(END, f"User: {user_input}\n")
    text_area.insert(END, f"Chatbot: {response}\n")

  def chatbot_response(user_input):
    return model.chat(user_input)

  root.mainloop()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    tkinter_thread = threading.Thread(target=run_tkinter)

    flask_thread.start()
    tkinter_thread.start()

    flask_thread.join()
    tkinter_thread.join()