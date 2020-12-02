from tkinter import *
import random
import string
import pyperclip

root = Tk()
#root.iconbitmap(r'C:\Users\Saksham\Desktop\images\key-5.png')
root.geometry("350x350")
#root.resizable(0,0)
Label(root, text ='PASSWORD GENERATOR', font ='arial 15 bold').pack()
frame=LabelFrame(root,text="",padx=20,pady=20)
frame.pack(padx=50,pady=50)
root.title("PASSWORD GENERATOR")

Label(root, text ='DataFlair', font ='arial 15 bold').pack(side = BOTTOM)

pass_label = Label(frame, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(frame, from_ = 8, to_ = 32 , textvariable = pass_len , width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(Password+password)

Button(frame, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(frame , textvariable = pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(frame, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5) 

root.mainloop()   
