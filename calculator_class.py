from tkinter import * 

class Calcualator():
    def click(self, num):
        self.expression = self.expression + str(num) 

        self.equation.set(self.expression)


    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set("error")
            self.expression = ""

    def clear(self):
        self.equation.set("")

    def main(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Calculator in python")
        root.configure(background="black")
        self.expression = ""
        self.equation = StringVar()
        expression_field = Entry(root, textvariable=self.equation)

        b_1 = Button(root, text="1", fg = "black", bg = "white", command=lambda: self.click("1"))
        b_2 = Button(root, text="2", fg = "black", bg = "white", command=lambda: self.click("2"))
        b_3 = Button(root, text="3", fg = "black", bg = "white", command=lambda: self.click("3"))
        b_4 = Button(root, text="4", fg = "black", bg = "white", command=lambda: self.click("4"))
        b_5 = Button(root, text="5", fg = "black", bg = "white", command=lambda: self.click("5"))
        b_6 = Button(root, text="6", fg = "black", bg = "white", command=lambda: self.click("6"))
        b_7 = Button(root, text="7", fg = "black", bg = "white", command=lambda: self.click("7"))
        b_8 = Button(root, text="8", fg = "black", bg = "white", command=lambda: self.click("8"))
        b_9 = Button(root, text="9", fg = "black", bg = "white", command=lambda: self.click("9"))
        b_0 = Button(root, text="0", fg = "black", bg = "white", command=lambda: self.click("0"))
        plus = Button(root, text="+", fg = "black", bg = "white", command=lambda: self.click("+"))
        minus = Button(root, text="-", fg = "black", bg = "white", command=lambda: self.click("-"))
        multiply = Button(root, text="*", fg = "black", bg = "white", command=lambda: self.click("*"))
        devide = Button(root, text="/", fg = "black", bg = "white", command=lambda: self.click("/"))
        b_clear = Button(root, text="clear", fg = "black", bg = "white", command=self.clear)
        decimal = Button(root, text=".", fg="black", bg="white", command=lambda: self.click("."))
        equal = Button(root, text="=", fg="black", bg="white", command=self.equalpress)

        b_1.place(x=30, y = 100)
        b_2.place(x=60, y = 100)
        b_3.place(x=90, y = 100)
        b_4.place(x=30, y = 70)
        b_5.place(x=60, y = 70)
        b_6.place(x=90, y = 70)
        b_7.place(x=30, y = 40)
        b_8.place(x=60, y = 40)
        b_9.place(x=90, y = 40)
        b_0.place(x=120, y=40)
        plus.place(x=150, y=40)
        minus.place(x=150, y=70)
        multiply.place(x=150, y=100)
        devide.place(x=150, y=130)
        b_clear.place(x=180, y=40)
        decimal.place(x=120, y=70)
        expression_field.place(x=30, y=10)
        equal.place(x=180, y=70)

        root.mainloop()

root = Calcualator()
root.main()
