from gtts import gTTS
from playsound import playsound
from tkinter import *

def text_to_speech():
    text=entry.get()
    language='en'
    output=gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    playsound('output.mp3')

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text='Start', command=text_to_speech)
canvas.create_window(200, 230, window=button)


root.mainloop()