from tkinter import *

pycrypto = Tk()
pycrypto.title("My Portfolio")

name = Label(pycrypto, text="Bitcoin",bg="red",fg="blue")
name.grid(row=0,column=0, sticky=E+W+N+S)

pycrypto.mainloop()
