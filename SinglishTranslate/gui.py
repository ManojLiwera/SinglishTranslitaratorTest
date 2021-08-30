from tkinter import *
import singlishTag

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Singlish')
        self.lbl3=Label(win, text='Sinhala')
        self.t1=Entry(bd=3,width=45)
        self.t3=Entry(width=45)
        self.lbl1.place(x=50, y=50)
        self.t1.place(x=150, y=50)
        self.b1=Button(win, text='Transliterate', command=self.trans)
        self.b1.place(x=350, y=110)
        self.b2=Button(win, text='Clear', command=self.clear)
        self.b2.place(x=300, y=110)
        self.lbl3.place(x=50, y=190)
        self.t3.place(x=150, y=190)
    def trans(self):
        result = singlishTag.triGramTranslate(self.t1.get())
        self.t3.delete(0, 'end')
        self.t3.insert(END, str(result))
    def clear(self):
        self.t1.delete(0, 'end')

window=Tk()
MyWindow(window)
window.title('Singlish Transliterater')
window.geometry("500x300+10+10")
window.configure(background='honeydew3')
window.mainloop()