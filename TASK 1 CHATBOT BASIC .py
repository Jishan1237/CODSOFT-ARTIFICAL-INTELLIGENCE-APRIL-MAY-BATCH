import nltk
import random
from nltk.chat.util import Chat, reflections
import PySimpleGUI as sg

patterns = [
    (r'How are you?', ['I am fine, thank you.', 'I am doing well.', 'I am great, thanks for asking!']),
    (r'What is your name?', ['You can call me Chatbot.', 'I go by the name Chatbot.', 'My name is Chatbot.']),
    (r'What is the capital of France?', ['Paris.']),
    # Add 100 different questions and answers without skipping any
    (r'What is the largest country in the world?', ['Russia.']),
    (r'How many continents are there?', ['There are seven continents.']),
    (r'What is the freezing point of water?', ['0 degrees Celsius.']),
    (r'What is the boiling point of water?', ['100 degrees Celsius.']),
    (r'What is the capital of Japan?', ['Tokyo.']),
    (r'What is the currency of the United Kingdom?', ['Pound sterling.']),
    # Add more questions and answers here...
    (r'What is the chemical symbol for oxygen?', ['O.']),
    (r'How many planets are there in our solar system?', ['There are eight planets in our solar system.']),
    (r'Who discovered penicillin?', ['Alexander Fleming.']),
    (r'What is the chemical symbol for gold?', ['Au.']),
    (r'What is the square root of 25?', ['5.']),
    (r'Who is known as the father of modern physics?', ['Albert Einstein.']),
    (r'What is the tallest mountain in the world?', ['Mount Everest.']),
    (r'What is the chemical symbol for sodium?', ['Na.']),
    (r'What is the chemical symbol for iron?', ['Fe.']),
    (r'What is the national flower of India?', ['Lotus.']),
    (r'Who painted the Mona Lisa?', ['Leonardo da Vinci.']),
    (r'What is the chemical symbol for carbon?', ['C.']),
    (r'Who wrote "To Kill a Mockingbird"?', ['Harper Lee.']),
    (r'What is the chemical symbol for water?', ['H2O.']),
    (r'What is the speed of light?', ['299,792 kilometers per second.']),
    (r'Who is the author of "Pride and Prejudice"?', ['Jane Austen.']),
    (r'What is the chemical symbol for potassium?', ['K.']),
    (r'What is the national bird of the United States?', ['Bald eagle.']),
    (r'Who composed the "Moonlight Sonata"?', ['Ludwig van Beethoven.']),
    (r'What is the chemical symbol for helium?', ['He.']),
    (r'What is the largest ocean in the world?', ['Pacific Ocean.']),
    (r'Who is the author of "1984"?', ['George Orwell.']),
    (r'What is the chemical symbol for nitrogen?', ['N.']),
    (r'Who discovered the theory of relativity?', ['Albert Einstein.']),
    (r'What is the national animal of China?', ['Giant panda.']),
    (r'Who painted the ceiling of the Sistine Chapel?', ['Michelangelo.']),
    (r'What is the chemical symbol for silver?', ['Ag.']),
    (r'What is the tallest building in the world?', ['Burj Khalifa.']),
    (r'Who is the author of "The Catcher in the Rye"?', ['J.D. Salinger.']),
    (r'What is the chemical symbol for lead?', ['Pb.']),
    (r'What is the national sport of Canada?', ['Ice hockey.']),
    (r'Who is the author of "Hamlet"?', ['William Shakespeare.']),
    (r'What is the chemical symbol for copper?', ['Cu.']),
    (r'What is the national animal of India?', ['Bengal tiger.']),
    (r'Who painted "Starry Night"?', ['Vincent van Gogh.']),
    (r'What is the chemical symbol for calcium?', ['Ca.']),
    (r'Who is the author of "The Great Gatsby"?', ['F. Scott Fitzgerald.']),
    (r'What is the chemical symbol for mercury?', ['Hg.']),
    (r'Who wrote the "Harry Potter" series?', ['J.K. Rowling.']),
    (r'What is the chemical symbol for uranium?', ['U.']),
    (r'Who is the author of "War and Peace"?', ['Leo Tolstoy.']),
    (r'What is the chemical symbol for tin?', ['Sn.']),
    (r'What is the national flower of Japan?', ['Cherry blossom.']),
    (r'Who is the author of "Moby-Dick"?', ['Herman Melville.']),
    (r'What is the chemical symbol for silicon?', ['Si.']),
    (r'What is the national animal of Australia?', ['Red kangaroo.']),
    (r'Who is the author of "The Odyssey"?', ['Homer.']),
    (r'What is the chemical symbol for phosphorus?', ['P.']),
    (r'What is the national sport of Japan?', ['Sumo wrestling.']),
    (r'Who is the author of "Crime and Punishment"?', ['Fyodor Dostoevsky.']),
    (r'What is the chemical symbol for magnesium?', ['Mg.']),
    (r'What is the national animal of Canada?', ['Beaver.']),
    (r'Who wrote "Romeo and Juliet"?', ['William Shakespeare.']),
    (r'What is the chemical symbol for potassium?', ['K.']),
    (r'What is the national flower of China?', ['Peony.']),
    (r'Who is the author of "Don Quixote"?', ['Miguel de Cervantes.']),
    (r'What is the chemical symbol for zinc?', ['Zn.']),
    (r'What is the national bird of India?', ['Indian peacock.']),
    (r'Who is the author of "The Picture of Dorian Gray"?', ['Oscar Wilde.']),
    (r'What is the chemical symbol for fluoride?', ['F.']),
    (r'What is the national sport of Brazil?', ['Football.']),
    (r'Who is the author of "Alice\'s Adventures in Wonderland"?', ['Lewis Carroll.']),
    (r'What is the chemical symbol for sodium?', ['Na.']),
    (r'What is the national flower of France?', ['Lily.']),
    (r'Who wrote "The Lord of the Rings"?', ['J.R.R. Tolkien.']),
    (r'What is the chemical symbol for neon?', ['Ne.']),
    (r'What is the national bird of Australia?', ['Emu.']),
    (r'Who is the author of "The Iliad"?', ['Homer.']),
    (r'What is the chemical symbol for sulfur?', ['S.']),
    (r'What is the national sport of China?', ['Table tennis.']),
    (r'Who wrote "The Chronicles of Narnia"?', ['C.S. Lewis.']),
    (r'What is the chemical symbol for chlorine?', ['Cl.']),
    (r'What is the national flower of Canada?', ['Maple leaf.']),
    (r'Who is the author of "The Canterbury Tales"?', ['Geoffrey Chaucer.']),
    (r'What is the chemical symbol for titanium?', ['Ti.']),
    (r'What is the national bird of Japan?', ['Green pheasant.']),
    (r'Who wrote "The Hobbit"?', ['J.R.R. Tolkien.']),
    (r'What is the chemical symbol for argon?', ['Ar.']),
    (r'What is the national sport of Russia?', ['Bandy.']),
    (r'Who is the author of "Les Misérables"?', ['Victor Hugo.']),
    (r'What is the chemical symbol for chromium?', ['Cr.']),
    (r'What is the national flower of Australia?', ['Golden wattle.']),
    (r'Who is the author of "The Divine Comedy"?', ['Dante Alighieri.']),
    (r'What is the chemical symbol for manganese?', ['Mn.']),
    (r'What is the national sport of France?', ['Football.']),
]
# Create a chatbot with the defined patterns
chatbot = Chat(patterns, reflections)

# Define the layout of the GUI
layout = [
    [sg.Text('Chatbot', size=(20, 1), justification='center', font=('Helvetica', 25), relief=sg.RELIEF_RIDGE)],
    [sg.Multiline(size=(60, 20), key='-OUTPUT-', font=('Helvetica', 12), background_color='#f0f0f0', text_color='#333')],
    [sg.Text('You:', font=('Helvetica', 12)), sg.InputText(key='-INPUT-', size=(50, 1)), sg.Button('Send'), sg.Button('Exit')],
]

# Create the GUI window
window = sg.Window('Chatbot', layout, resizable=True, finalize=True)

# Main loop to handle events and interact with the chatbot
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    user_input = values['-INPUT-']
    response = chatbot.respond(user_input)
    window['-OUTPUT-'].print(f'You: {user_input}', text_color='#007bff')
    window['-OUTPUT-'].print(f'Chatbot: {response}\n\n', text_color='#28a745')

window.close()
