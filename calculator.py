import tkinter
import math
from tkinter import ttk
from tkinter.tix import Tk






class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)


    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, tkinter.END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "raise":
            self.total = self.total ** self.current
        if self.op == "rootof":
            self.total = self.total ** (1/self.current)
        if self.op == "fact":
            self.total=int(text_box.get())
            self.total=math.factorial(self.total)
        if self.op == "ln":
            self.total = math.loge(self.current)
        if self.op == "log":
            self.total=math.log10(self.current)
        if self.op == "sine":
            self.total=math.sin(math.radians(self.current))
        if self.op == "cosine":
            self.total = math.cos(math.radians(self.current))
        if self.op == "tangent":
            self.total = math.tan(math.radians(self.current))
        if self.op == "sinh":
            self.total = math.sinh(math.radians(self.current))
        if self.op == "cosh":
            self.total = math.cosh(math.radians(self.current))
        if self.op == "tanh":
            self.total = math.tanh(math.radians(self.current))
        if self.op == "asin":
            self.total = math.asin(math.radians(self.current))
        if self.op == "acos":
            self.total = math.acos(math.radians(self.current))
        if self.op == "atan":
            self.total = math.atan(math.radians(self.current))
        if self.op=="pi":
            self.total=math.pi(self.current)


        if self.op == "exp":
            self.total = math.exp(self.current)
        if self.op == "inv":
            self.total = 1/self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = int(self.current)
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def clear(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_clear(self):
        self.clear()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

sum1 = Calc()
root = Tk()
calc = tkinter.Frame (root)
calc.grid()

root.title("Calculator")
text_box = tkinter.Entry (calc, justify=tkinter.RIGHT, width=30, font="Times 16 bold")
text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
text_box.insert(0, "0")
#text_box.focus()


#operator=""
#text_Input=StringVar()

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(
            tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, font="times 18 bold", text = numbers[i]))
        bttn[i]["bg"]= "powder blue"
        bttn[i].grid(row = j, column = k,padx=1,pady=1)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

bttn_0 = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="0", bg="powder blue", font="times 18 bold")
bttn_0["command"] = lambda: sum1.num_press(0)
bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

div = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="/", bg="powder blue", font="times 18 bold")
div["command"] = lambda: sum1.operation("divide")
div.grid(row = 1, column = 3, padx=1, pady = 1)

mult = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="*", bg="powder blue", font="times 18 bold")
mult["command"] = lambda: sum1.operation("times")
mult.grid(row = 2, column = 3,  padx=1, pady = 1)

minus = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="-", bg="powder blue", font="times 18 bold")
minus["command"] = lambda: sum1.operation("minus")
minus.grid(row = 3, column = 3, padx=1, pady = 1)

add = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="+", bg="powder blue", font="times 18 bold")
add["command"] = lambda: sum1.operation("add")
add.grid(row = 4, column = 2,  padx=1, pady = 1)

power = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text="x^y", bg="powder blue", font="times 18 bold")
power["command"] = lambda: sum1.operation("raise")
power.grid(row=2,column = 4,padx=1,pady=1)

#rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "green")
#rootof["command"] = lambda: sum1.operation("rootof")
#rootof.grid(row=4, column=3, padx=1, pady=1)

fact = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text="!", bg="powder blue", font="times 18 bold")
fact["command"] = lambda: sum1.operation("fact")
fact.grid(row=3,column=4, padx=1, pady=1)

loge = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text="ln", bg="powder blue", font="times 18 bold")
loge["command"] = lambda: sum1.operation("ln")
loge.grid(row=4, column=3, padx=1, pady=1)

log10 = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text="log", bg="powder blue", font="times 18 bold")
log10["command"]= lambda: sum1.operation("log")
log10.grid(row=4, column=4, padx=1 , pady=1)

sine = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="sin", bg="powder blue", font="times 18 bold")
sine["command"]=lambda: sum1.operation("sine")
sine.grid(row=5,column=0,padx=1,pady=1)

cosine = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="cos", bg="powder blue", font="times 18 bold")
cosine["command"]=lambda: sum1.operation("cosine")
cosine.grid(row=5,column=1,padx=1,pady=1)

tangent = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="tan", bg="powder blue", font="times 18 bold")
tangent["command"]=lambda: sum1.operation("tangent")
tangent.grid(row=5,column=2,padx=1,pady=1)

sinh = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="sinh", bg="powder blue", font="times 18 bold")
sinh["command"]=lambda: sum1.operation("sinh")
sinh.grid(row=2,column=5,padx=1,pady=1)

cosh = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="cosh", bg="powder blue", font="times 18 bold")
cosh["command"]=lambda: sum1.operation("cosh")
cosh.grid(row=3,column=5,padx=1,pady=1)

tanh= tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="tanh", bg="powder blue", font="times 18 bold")
tanh["command"]=lambda: sum1.operation("tanh")
tanh.grid(row=4,column=5,padx=1,pady=1)

asin = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="asin", bg="powder blue", font="times 18 bold")
asin["command"]=lambda: sum1.operation("asin")
asin.grid(row=5,column=3,padx=1,pady=1)

acos = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="acos", bg="powder blue", font="times 18 bold")
acos["command"]=lambda: sum1.operation("acos")
acos.grid(row=5,column=4,padx=1,pady=1)

atan = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text ="atan", bg="powder blue", font="times 18 bold")
atan["command"]=lambda: sum1.operation("atan")
atan.grid(row=5,column=5,padx=1,pady=1)


exponent = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text='e^x', bg="powder blue", font="times 18 bold")
exponent["command"]=lambda: sum1.operation("exp")
exponent.grid(row=1,column=4,padx=1,pady=1)

inv = tkinter.Button (calc, height=1, width=2, padx=10, pady=10, text="1/x", bg="powder blue", font="times 18 bold")
inv["command"] = lambda: sum1.operation("inv")
inv.grid(row=2,column=6,padx=1,pady=1)

point = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text =".", bg="powder blue", font="times 18 bold")
point["command"] = lambda: sum1.num_press(".")
point.grid(row = 3, column = 6, padx=1, pady = 1)

neg= tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="+/-", bg="powder blue", font="times 18 bold")
neg["command"] = sum1.sign
neg.grid(row = 4, column = 1,  padx=1, pady = 1)


clear = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="C", bg="white", font="times 18 bold")
clear["command"] = sum1.clear
clear.grid(row = 1, column = 5,  padx=1, pady = 1)

all_clear = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="AC", bg="white", font="times 18 bold")
all_clear["command"] = sum1.all_clear
all_clear.grid(row = 1, column = 6, padx=1, pady = 1)

equals = tkinter.Button (calc, height =1, width=2, padx=10, pady =45, text ="=", bg="powder blue", font="times 18 bold")
equals["command"] = sum1.calc_total
equals.grid(row =4, column = 6,columnspan=1,rowspan=2,padx=1, pady = 1)

#pi = tkinter.Button (calc, height =1, width=2, padx=10, pady = 10, text ="pi", bg="powder blue", font="times 18 bold")
#pi["command"] = sum1.calc_total
#pi.grid(row = 4, column = 6,columnspan=1,rowspan=2,padx=1, pady = 1)


root.mainloop()
