import nltk
from nltk.chat.util import Chat, reflections
from pairs import pairs
from contractions import contractions
import re


def preprocess_text(text, contractions):
    # Convert to lowercase
    text = text.lower()

    for contraction, full_form in contractions.items():
        text = text.replace(contraction, full_form)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    
    return text


def chatbot():
    print("Hi, I'm Atenas, a bot created by Lucas Torres. Let's chat!")
    chat = Chat(pairs, reflections)
    def custom_converse():
        user_input = ""
        while user_input != "quit":
            user_input = input("> ")
            user_input = preprocess_text(user_input, contractions)
            response = chat.respond(user_input)
            print(response)
    
    custom_converse()

if __name__ == "__main__":
    chatbot()