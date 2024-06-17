import tkinter as tk
from tkinter import Text, Entry, Button, END
import model

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

    # Clear the input field
    input_field.delete(0, END)

    # Generate a response from the chatbot
    response = chatbot_response(user_input)

    # Display the response in the chatbot's text area
    text_area.insert(END, f"User: {user_input}\n")
    text_area.insert(END, f"Chatbot: {response}\n")


def chatbot_response(text):
    return model.chat(text)

root.mainloop()
