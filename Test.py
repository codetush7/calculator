
from tkinter import *
import ast
root = Tk()
root.geometry("400x400")
i = 0
def get_number(num):
    global i
    display.insert(i,num)
    i += 1

def get_operations(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i += length

def clearAll():
    display.delete(0,END)

def calculate():
    entireString = display.get()
    try:
        node = ast.parse(entireString,mode="eval")
        result = eval(compile(node,'<string>','eval'))
        clearAll()
        display.insert(0,result)
    except Exception:
        clearAll()
        display.insert(0,"Error")
#   import Abstract syntax tree(AST) module
def backspace():
    entire_string = display.get()
    if len(entire_string):
        newString = entire_string[:-1]
        clearAll()
        display.insert(0,newString)
# Configure the grid layout to expand
for i in range(6):  # 6 columns (for Entry columnspan)
    root.columnconfigure(i, weight=1)
for i in range(5):  # total 5 rows (1 for Entry + 3 for buttons + 1 margin)
    root.rowconfigure(i, weight=1)

# Entry widget (spans all 6 columns)
display = Entry(root, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=5, pady=5)


numbers = [1,2,3,4,5,6,7,8,9]
# Buttons (3x3 grid)
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(root, text=button_text,command=lambda text=button_text:get_number(text))
        button.grid(row=x+1, column=y,sticky="nsew", padx=5, pady=5)
        counter += 1
button_zero = Button(root, text="0",command=lambda :get_number(0))
button_zero.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

count = 0
operations = ['+','-',"*","/","3.14","%","(","**",")","**2"]
for x in range(4):
    for y in range(3):
        if count<len(operations):
            button = Button(root,text=operations[count],command=lambda text=operations[count]:get_operations(text))
            count+=1
            button.grid(row= x+1,column=y+3,sticky="nsew", padx=5, pady=5)
all_clearButton = Button(root,text="AC",font=("Arial", 16, "bold"), fg="black",command=clearAll)
all_clearButton.grid(row=4,column=0,sticky="nsew", padx=5, pady=5)


equal_button = Button(
    root,
    text="=",
    font=("Arial", 16, "bold"),
    bg="lightblue",
    fg="black",
    command=calculate
)
equal_button.grid(row=4, column=4, columnspan=2, sticky="nsew", padx=5, pady=5)

backspaceButton = Button(root,text="←",fg="black",font=("Arial", 18, "bold"),activebackground="#ff1c1c", borderwidth=2,command=backspace)
backspaceButton.grid(row=4,column=2,sticky="nsew", padx=5, pady=5)
root.mainloop()
