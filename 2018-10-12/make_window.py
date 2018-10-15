from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidegets()

    def createWidegets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='Hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        if name =='Mic':
            messagebox.showinfo('Message','Hello,%s'%name)
            self.quitButton1 =Button(self,text='secret',command=self.mimi)
            self.quitButton1.pack()
        else:
            messagebox.showinfo('Wrong', 'Please enter right name...')

    def mimi(self):
        what_say = self.nameInput.get() or 'Love'
        messagebox.showinfo('secret','I want to say I love you...%s'%what_say)

app = Application()
app.master.title('Hello,World!')
app.mainloop()