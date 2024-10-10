from tkinter import *
from tkinter import messagebox
class Calcualator():
    def click(self, num):
        self.expression += str(num) 
        self.equation.set(self.expression)
    def equalpress(self):
        try:
            self.total = str(round(eval(self.expression), 2))
            self.equation.set(self.total)
            self.allTotal = self.expression + "=" + self.total
            self.listMemory.insert(END, self.allTotal)
            self.expression = ""
        except:
            self.equation.set("error")
            self.expression = ""
    def addPrev(self): 
        self.expression += self.total
        self.equation.set(self.expression)
    def clearMemory(self): 
        self.listMemory.delete(0, END)
    def clear(self):
        self.expression = "" 
        self.equation.set("")
    def clear_prev(self): 
        self.expression = self.expression[:-1]
        self.equation.set(self.equation.get()[:-1])
    def add_win(self):  
        if self.counter < 1: 
            win = Toplevel(self.root) 
            win.title("Інформація про роботу")
            win.minsize(width=200, height=200)
            info = Label(win, text="Група: ПЗ-22-1/9\nГальчевський Кирил")
            info.pack() 
            self.counter+=1 
        else: 
            messagebox.showinfo(title="Помилка", message="Вікно вже відкрите!")
    def help(self): 
        help_win = Toplevel(self.root)
        help_win.title("Інформація про комбінаціяї клавіш")
        help_win.geometry("670x250")
        main = Label(help_win, text="Комбінації клавіш для програми:")
        comb1 = Label(help_win, text="Перша комбінація: Натисніть Enter, для того щоб відкрити вікно інформації про програму.")
        comb2 = Label(help_win, text="Друга комбінація: Натисніть клавіши Control+Q, для того щоб закрити програму.")
        comb3 = Label(help_win, text="Третя комбінація: Натисніть клавішу C(англ)+Ліву кнопку миші, для того щоб видалити останній знак в вікні вводу.")
        comb4 = Label(help_win, text="Четверта комбінація: Натисніть клавішу Control+Рух миші, для того щоб змінити тему програму.")
        comb1.place(x=20, y=40)
        comb2.place(x=20, y=70)
        comb3.place(x=20, y=100)
        comb4.place(x=20, y=130)
        main.place(x=10, y=10)
    def theme(self, s): 
        if s == "Dark Theme":
            self.root.configure(bg="black")
            self.expression_field.configure(bg="black", fg="white")
        elif s == "Grey Theme": 
            self.root.configure(bg="grey")
            self.expression_field.configure(bg="grey")
        elif s == "White Theme": 
            self.root.configure(bg="white")
            self.expression_field.configure(bg="white", fg="black")
    def max_min_size(self, s):
        if s == "Maximize" and self.temp == 1: 
            self.root.attributes('-fullscreen', False)
            self.temp = 0 
        elif s == "Maximize":
            self.root.attributes('-fullscreen', True)
            self.temp = 1
        elif s == "Minimize":
            self.root.state(newstate='iconic') 
    def quit(self): 
        self.root.destroy()
    def motion(self): 
        self.root.configure(background="blue")
    def main(self):
        self.root = Tk()
        self.root.geometry("500x210")
        self.root.title("Calculator in python")
        self.root.configure(background="white")
        self.root.bind('<Control-q>', lambda quit: self.quit())#Комбінація клавіш на закриття вікна
        self.root.bind('<Return>', lambda info: self.add_win())#Подія відкривання вікна за допомогою клавіши Enter
        self.root.bind('<Control-Motion>', lambda motion: self.motion())#Подія для опрацювання руху миші
        self.expression = ""
        self.counter = 0
        self.temp = 0
        self.equation = StringVar()
        self.frameMemory = Frame()
        self.listMemory = Listbox(self.frameMemory, height=6)
        self.button_clear = Button(self.root, text="Clear Memory", command=lambda: self.clearMemory()) 
        self.button_add = Button(self.root, text="Add Previous Result", command=lambda: self.addPrev())
        self.scroll = Scrollbar(self.frameMemory, orient="vertical")
        self.scroll.place(x=320, y=10)
        self.listMemory.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listMemory.yview) 
        self.expression_field = Entry(self.root, textvariable=self.equation)
        mainmenu = Menu(self.root)
        self.root.config(menu=mainmenu)
        file = Menu(mainmenu, tearoff=0)
        file.add_command(label="Maximize", command=lambda:self.max_min_size("Maximize"))
        file.add_command(label="Minimize", command=lambda:self.max_min_size("Minimize"))
        file.add_separator()
        file.add_command(label="Exit", command=lambda: self.quit())
        theme = Menu(mainmenu, tearoff=0)
        theme.add_command(label="Dark Theme", command=lambda:self.theme("Dark Theme"))
        theme.add_command(label="Grey Theme", command=lambda:self.theme("Grey Theme"))
        theme.add_command(label="White Theme", command=lambda:self.theme("White Theme"))
        help = Menu(mainmenu, tearoff=0)
        help.add_command(label="About Program", command=lambda:self.add_win())
        help.add_command(label="Short Keys", command=lambda: self.help())
        mainmenu.add_cascade(label="File", menu=file)
        mainmenu.add_cascade(label="Theme", menu=theme)
        mainmenu.add_cascade(label="Help", menu=help)
        f_num1 = Frame()
        f_num2 = Frame()
        f_num3 = Frame()
        f_num4 = Frame()
        f_func1 = Frame()
        f_func2 = Frame()
        f_func3 = Frame()
        b_1 = Button(f_num1, text="1", width=2, height=2, fg = "white", bg = "black")
        b_1.bind('<Button-1>',lambda number: self.click('1'))
        b_2 = Button(f_num1, text="2", width=2, height=2, fg = "white", bg = "black")
        b_2.bind('<Button-1>', lambda number: self.click('2'))
        b_3 = Button(f_num1, text="3", width=2, height=2, fg = "white", bg = "black")
        b_3.bind('<Button-1>', lambda number: self.click('3'))
        b_4 = Button(f_num2, text="4", width=2, height=2, fg = "white", bg = "black")
        b_4.bind('<Button-1>', lambda number: self.click('4'))
        b_5 = Button(f_num2, text="5", width=2, height=2, fg = "white", bg = "black")
        b_5.bind('<Button-1>', lambda number: self.click('5'))
        b_6 = Button(f_num2, text="6", width=2, height=2, fg = "white", bg = "black")
        b_6.bind('<Button-1>', lambda number: self.click('6'))
        b_7 = Button(f_num3, text="7", width=2, height=2, fg = "white", bg = "black")
        b_7.bind('<Button-1>', lambda number: self.click('7'))
        b_8 = Button(f_num3, text="8", width=2, height=2, fg = "white", bg = "black")
        b_8.bind('<Button-1>', lambda number: self.click('8'))
        b_9 = Button(f_num3, text="9", width=2, height=2, fg = "white", bg = "black")
        b_9.bind('<Button-1>', lambda number: self.click('9'))
        b_0 = Button(f_num4, text="0", width=2, height=2, fg = "white", bg = "black")
        b_0.bind('<Button-1>', lambda number: self.click('0'))
        plus = Button(f_func1, text="+", width=2, height=2, fg = "white", bg = "black")
        plus.bind('<Button-1>', lambda op: self.click('+'))
        minus = Button(f_func1, text="-", width=2, height=2, fg = "white", bg = "black")
        minus.bind('<Button-1>', lambda op: self.click('-'))
        multiply = Button(f_func1, text="*", width=2, height=2, fg = "white", bg = "black")
        multiply.bind('<Button-1>', lambda op: self.click('*'))
        devide = Button(f_func1, text="/", width=2, height=2, fg = "white", bg = "black")
        devide.bind('<Button-1>', lambda op: self.click('/'))
        b_clear = Button(f_func2, text="clear", width=4, height=2, fg = "white", bg = "black")
        b_clear.bind('<Button-1>', lambda clear: self.clear())
        decimal = Button(f_func2, text=".", width=2, height=2, fg="white", bg="black")
        decimal.bind('<Button-1>', lambda number: self.click('.'))
        equal = Button(f_func3, text="=", width=2, height=2, fg="white", bg="black")
        equal.bind('<Button-1>', lambda result: self.equalpress())
        b_clearPrev = Button(f_func3, text="<--", width=2, height=2, fg = "white", bg = "black")
        b_clearPrev.bind('<Button-1>', lambda clear: self.clear_prev())
        self.root.bind('<c><Button-1>', lambda clear: self.clear_prev())#Комбінація клавіш миші та клавіатури на видалення останього символу
        l_credits = Label(self.root, text="Для відкривання інформація натисніть клавішу Enter", fg = "white", bg = "black")
        self.expression_field.place(x=30, y=10)
        f_num1.place(x=30, y=40)
        b_1.pack(side=LEFT)
        b_2.pack(side=LEFT)
        b_3.pack(side=LEFT)
        f_num2.place(x=30, y=80)
        b_4.pack(side=LEFT)
        b_5.pack(side=LEFT)
        b_6.pack(side=LEFT)
        f_num3.place(x=30, y=120)
        b_7.pack(side=LEFT)
        b_8.pack(side=LEFT) 
        b_9.pack(side=LEFT)
        f_num4.place(x=30, y=160)
        b_0.pack(side=LEFT) 
        f_func1.place(x=100, y=40)
        plus.pack(side=LEFT)
        minus.pack(side=LEFT)
        multiply.pack(side=LEFT)
        devide.pack(side=LEFT)
        f_func2.place(x=100, y=80)
        b_clear.pack(side=LEFT)
        decimal.pack(side=LEFT)
        f_func3.place(x=100, y=120)
        equal.pack(side=LEFT)
        b_clearPrev.pack(side=LEFT) 
        l_credits.pack(side=BOTTOM, anchor=E) 
        self.frameMemory.place(x=200, y=10)
        self.listMemory.pack(side=LEFT)
        self.scroll.pack(side=LEFT)
        self.button_clear.place(x=350, y=10)
        self.button_add.place(x=350, y=50)
        self.root.mainloop()
root = Calcualator()
root.main()