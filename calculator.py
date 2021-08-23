from tkinter import * 

expression = ""

def click(num):
        global expression
        expression = expression + str(num) 

        equation.set(expression)


def equalpress():
    try:
        global expression
        #What is eval in python?
        #Answer: eval is a built-in- function used in python, eval function parses the expression argument and evaluates it as a python expression. In simple words, the eval function evaluates the “String” like a python expression and returns the result as an integer.
        total = str(eval(expression))
        #set is a function that will give variable equation the same meaning that total has
        equation.set(total)
        expression = ""
    except:
        #Create excaption, that won't let ZeroDivisionError appear in the terminal.
        equation.set("error")
        expression = ""

# We create function clear, that will delete all text from the input, in our example, it's expression_field. 
def clear():
    #Create variable named expression
    global expression

    expression = ""
    #Add empty string to the equation, so then everything will be empty
    equation.set("")

if __name__ == "__main__":

    calc = Tk()
    calc.geometry("300x200")
    calc.title("Calculator in python")
    calc.configure(background="black")

    equation = StringVar()

    expression_field = Entry(calc, textvariable=equation)

    # We create buttons for calculator
    b_1 = Button(calc, text="1", fg = "black", bg = "red", command=lambda: click("1"))
    b_2 = Button(calc, text="2", fg = "black", bg = "red", command=lambda: click("2"))
    b_3 = Button(calc, text="3", fg = "black", bg = "red", command=lambda: click("3"))
    b_4 = Button(calc, text="4", fg = "black", bg = "red", command=lambda: click("4"))
    b_5 = Button(calc, text="5", fg = "black", bg = "red", command=lambda: click("5"))
    b_6 = Button(calc, text="6", fg = "black", bg = "red", command=lambda: click("6"))
    b_7 = Button(calc, text="7", fg = "black", bg = "red", command=lambda: click("7"))
    b_8 = Button(calc, text="8", fg = "black", bg = "red", command=lambda: click("8"))
    b_9 = Button(calc, text="9", fg = "black", bg = "red", command=lambda: click("9"))
    b_0 = Button(calc, text="0", fg = "black", bg = "red", command=lambda: click("0"))
    # We create buttons for calculator
    # in Button(command = lambda: click("some text")), we create a button and add the function to it, so then it will be able to follow rules of function named click.
    plus = Button(calc, text="+", fg = "black", bg = "red", command=lambda: click("+"))
    minus = Button(calc, text="-", fg = "black", bg = "red", command=lambda: click("-"))
    multiply = Button(calc, text="*", fg = "black", bg = "red", command=lambda: click("*"))
    devide = Button(calc, text="/", fg = "black", bg = "red", command=lambda: click("/"))

    b_clear = Button(calc, text="clear", fg = "black", bg = "red", command=clear)

    decimal = Button(calc, text=".", fg="black", bg="red", command=lambda: click("."))


    equal = Button(calc, text="=", fg="black", bg="red",command=equalpress)


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

    expression_field.place(x=10, y=10)

    equal.place(x=180, y=70)

    calc.mainloop()
