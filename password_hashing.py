from tkinter import *
import bcrypt

def validate(password):
    #this hash value was created from the original password which is 'thisismypassword'
    hash=b'$2b$12$820H4C3hNkt2KKuz17nFzeu0qgBVQj5.aq6ilrDOJVdEftybDyjOa'
    entered_password=bytes(password, encoding='utf-8')

    if bcrypt.checkpw(entered_password, hash):
        print('Login successful!')
    else:
        print('Invalid password!')

root = Tk()
root.geometry('300x300')

password_entry=Entry(root)
password_entry.pack()
button=Button(text='validate',command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()