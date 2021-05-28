from tkinter import *

root=Tk()
frame=Frame(root)
frame.pack()
#------------CALCULO -----------------_#
result=0
operator=""
def showResult():
    global result
    if(operator=="+"):
        result+=int(dataScreen.get())
        dataScreen.set(str(result))


    if(operator=="*"):
        result*=int(dataScreen.get())
        dataScreen.set(str(result))

    if(operator=="-"):
        result-=int(dataScreen.get())
        dataScreen.set(str(result))
    
    if(operator=="/"):
        result=result/int(dataScreen.get())
        dataScreen.set(str(result))



#---------PANTALLA-------------#
def setOperator(ope):
    global result
    global operator
    result=0
    result+=float(dataScreen.get())
    print(result)
    dataScreen.set("")
    operator=ope

dataScreen=StringVar()
screen=Entry(frame,textvariable=dataScreen)
screen.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
screen.config(background="black",fg="#1eae98",justify="right")

#---- FUNCION REPRESENTACION
def dataPush(key):
    dataScreen.set(dataScreen.get()+key)

def clear():
    global result
    global operator
    dataScreen.set("")
    result=0
    operator=""


#--------FILA 1 ---------------

buton_7=Button(frame,text="7",width=3,command=lambda:dataPush("7"))
buton_8=Button(frame,text="8",width=3,command=lambda:dataPush("8"))
buton_9=Button(frame,text="9",width=3,command=lambda:dataPush("9"))
buton_div=Button(frame,text="/",width=3,command=lambda:setOperator("/"))
buton_7.grid(row=2,column=1)
buton_8.grid(row=2,column=2)
buton_9.grid(row=2,column=3)
buton_div.grid(row=2,column=4)

#--------FILA2---------------
buton_4=Button(frame,text="4",width=3,command=lambda:dataPush("4"))
buton_5=Button(frame,text="5",width=3,command=lambda:dataPush("5"))
buton_6=Button(frame,text="6",width=3,command=lambda:dataPush("6"))
buton_multi=Button(frame,text="*",width=3,command=lambda:setOperator("*"))
buton_4.grid(row=3,column=1)
buton_5.grid(row=3,column=2)
buton_6.grid(row=3,column=3)
buton_multi.grid(row=3,column=4)

#------------FILA 3 _-------------------
buton_1=Button(frame,text="1",width=3,command=lambda:dataPush("1"))
buton_2=Button(frame,text="2",width=3,command=lambda:dataPush("2"))
buton_3=Button(frame,text="3",width=3,command=lambda:dataPush("3"))
buton_rest=Button(frame,text="-",width=3,command=lambda:setOperator("-"))
buton_1.grid(row=4,column=1)
buton_2.grid(row=4,column=2)
buton_3.grid(row=4,column=3)
buton_rest.grid(row=4,column=4)

#-------FILA 4--------------
buton_0=Button(frame,text="0",width=3,command=lambda:dataPush("0"))
buton_coma=Button(frame,text=",",width=3,command=lambda:dataPush("0"))
buton_igual=Button(frame,text="=",width=3,command=lambda:showResult())
buton_sum=Button(frame,text="+",width=3,command=lambda:setOperator("+"))
buton_0.grid(row=5,column=1)
buton_coma.grid(row=5,column=2)
buton_igual.grid(row=5,column=3)
buton_sum.grid(row=5,column=4)

buton_clear=Button(frame,text="CR",width=3,command=lambda:clear())
buton_clear.grid(row=6,column=1)

root.mainloop()
