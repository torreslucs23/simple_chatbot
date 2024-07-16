import nltk
from nltk.chat.util import Chat, reflections
from pairs import pairs



def chatbot():
    print("Hi, I'm Atenas, a bot created by Lucas Torres. Let's chat!")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()