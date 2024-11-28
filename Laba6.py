from tkinter import * 
from tkinter import filedialog, messagebox, ttk
from random import*


f = open('laba4.txt','w+') 
what = [(randint(1, 1000)) for i in range(10)]
for i in what:
    f.write(str(i) + ' ')
f = open('laba4.txt','r')

f1 = open('laba4,1.txt','w+')
what = [(randint(1, 1000)) for i in range(10)]
for i in what:
    f1.write(str(i) + ' ')
f1 = open('laba4.txt','r')

f2 = open('laba4,2.txt','w+')
what = [(randint(1, 1000)) for i in range(10)]
for i in what:
    f2.write(str(i) + ' ')
f2 = open('laba4.txt','r')

f.close()
f1.close()
f2.close()


window = Tk() 


window.title("Собрание всех лабораторных")

window.geometry("900x500")


def click(): 
    NamePrint = Name.get()
    Kak['text'] = f'Здравствуйте, {NamePrint}!'

Laba1=Label(window, text="Лабораторная №1")
Laba1.pack()
NameTitle=Label(window, text="Введите Ваше имя")
NameTitle.pack()
Name=Entry(window)
Name.pack()
btn = ttk.Button(window, text="Нажми на меня", command=click)
btn.pack()
Kak = Label(window, font = 200)
Kak.pack()


def perem():
    a=numone.get()
    b=numtwo.get()
    a=int(a)
    b=int(b)
    numsum['text']= f'{a+b}, {a-b}, {a*b}, {a**b}, дальнейшие действия невозможны'
    if a!=0 and b!=0:
        numsum['text']= f' {a}+{b}={a+b}, {a}-{b}={a-b}, {a}*{b}={a*b}, {a}^{b}={a**b}, {a}/{b}={a/b}, {a}//{b}={a//b}, {a}%{b}={a%b}'

Laba2=Label(window, text="Лабораторная №2")
Laba2.pack()
Text1=Label(window, text="Введите первое число")
Text1.pack()
numone=Entry(window)
numone.pack()
Text2=Label(window, text="Введите второе число")
Text2.pack()
numtwo=Entry(window)
numtwo.pack()
numbtn= ttk.Button(window, text="Нажми на меня", command=perem)
numbtn.pack()
numsum=Label(window)
numsum.pack()



def popop():
    c=randone.get()
    d=randtwo.get()
    c=int(c)
    d=int(d)
    i=0
    e=[]
    for i in range (10):
        e.append(randint(c, d))
    RandStrok['text']=f'{e}'
    e.sort()
    SortStrok['text']=f'Сортировка от меньшего к большему - {e}'
    e.sort(reverse=True)
    ReversStrok['text']=f'Сортировка от большего к меньшему - {e}'
    Min['text']=f'Минимальное число - {min(e)}'
    Max['text']=f'Максимальное число - {max(e)}'
    sum=0
    for i in e:
        sum+=i
    Sum['text']=f'Сумма всех чисел - {sum}'


Laba3=Label(window, text="Лабораторная №3")
Laba3.pack()
Text3=Label(window, text="Введите минимальное число")
Text3.pack()
randone=Entry(window)
randone.pack()
Text4=Label(window, text="Введите максимальное число")
Text4.pack()
randtwo=Entry(window)
randtwo.pack()
numbtn= ttk.Button(window, text="Нажми на меня", command=popop)
numbtn.pack()
RandStrok=Label(window)
RandStrok.pack()
SortStrok=Label(window)
SortStrok.pack()
ReversStrok=Label(window)
ReversStrok.pack()
Min=Label(window)
Min.pack()
Max=Label(window)
Max.pack()
Sum=Label(window)
Sum.pack()


def help():
    fn = filedialog.askopenfilename()
    f3 = open(fn, 'r')
    txt=f3.read()
    FileText['text']=txt
    filecont=list(map(int, txt.split()))
    sred = sum(filecont)/len(filecont)
    Otbr['text']=f'Среднее значение чисел - {sred}'

Laba4=Label(window, text="Лабораторная №4")
Laba4.pack()
numbtn=ttk.Button(window, text="Нажми на меня", command=help)
numbtn.pack()
FileText = Label(window)
FileText.pack()
Otbr=Label(window)
Otbr.pack()


def me():
    class Tarkov:
        def __init__(self, name, age, money):
            self.name=name
            self.age=age
            self.money=money

        def mama(self):
            return f"Название: {self.name}. Возраст игры: {self.age} лет."
        
    class Arena(Tarkov):
        def papa(self):
            return f"Стоимость: {self.money}."
                 
    kakashka = Arena("Таркоу", 7, 1600)
    res = f"{kakashka.mama()}\n{kakashka.papa()}"  
    messagebox.showinfo("Результаты", res) 


Laba5=Label(window, text="Лабораторная №5")
Laba5.pack()
numbtn=ttk.Button(window, text="Нажми на меня", command=me)
numbtn.pack()




window.mainloop()

