from tkinter import *
import tkfilebrowser


class Form:

    def __init__(self, master):
        self.name = Label(text="First Name:").grid(row=0,column=0)
        self.ename = Entry(master).grid(row=0,column=1)
        # Last name
        self.surname = Label(text="Last Name:").grid(row=1, column=0)
        self.esurname = Entry(master).grid(row=1, column=1)
        # email
        self.email = Label(text="Email:").grid(row=2, column=0)
        self.eemail = Entry(master).grid(row=2, column=1)
        # password
        self.password = Label(text="Password:").grid(row=3, column=0)
        self.epassword = Entry(master,show='*').grid(row=3, column=1)
        # Desired Pos
        self.position = Label(text="Key Word:");
        self.position.grid(row=4, column=0)
        self.epos = Entry(master).grid(row=4, column=1)
        # Location
        self.Loc = Label(text="Location:")
        self.Loc.grid(row=5, column=0)
        self.Location = Entry(master).grid(row=5, column=1)
        self.res = Label(text="Resume:")
        self.res.grid(row=7, column=0)
        self.Resume = Entry(master, font=40)
        self.Resume.grid(row=7, column=1)
        self.b1 = Button(master, text="Choose File", font=40, command=self.browsefunc)
        self.b1.grid(row=7, column=2)
        self.res = Label(text="Driver:")
        self.res.grid(row=8, column=0)
        self.Driver = Entry(master, font=40)
        self.Driver.grid(row=8, column=1)
        self.b2 = Button(master, text="Choose File", font=40, command=self.browsefunc)
        self.b2.grid(row=8, column=2)

    def browsefunc(self):
        filename = tkfilebrowser.askopenfilename(filetypes=(("All files", "*.*"), ("PDF files", "*.pdf")))
        self.Resume.insert(END, filename)  # add this
        return filename






