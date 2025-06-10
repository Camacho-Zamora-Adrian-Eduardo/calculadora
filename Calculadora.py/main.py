import tkinter as tk
ventana=tk.Tk()
ventana.title("Camacho Zamora Adrian Eduardo-Calculadora")
ventana.resizable(0,0)

resultado=0
signo=" "

def calcula(valor,operacion):
    if (operacion=="+"):
        resultado=float(resultado)+float(valor)
    else:
        if (operacion=="-"):
            resultado=float(resultado)-float(valor)
        else:
            if (operacion=="*"):
                resultado=float(resultado)*float(valor)
            else:
                if (operacion=="/"):
                    resultado=float(resultado)/float(valor)
                else:
                    resultado=float(valor)
                    entrada.delete(0,tk.END)
                    entrada.insert(tk.END,resultado)

#Numeros del 0 al 9
def concatenar(valor):
    if entrada.get()!="0":
        
        entrada.insert(tk.END,valor)
    else:
        entrada.delete(0,tk.END)
        entrada.insert(tk.END,valor)

#Poner el .
def ponpunto():
    if entrada.get().find(".")==-1:
        entrada.insert((tk.END),".")

#Poner el signo +/-
def cambiarsigno():
    vl=float(entrada.get())
    entrada.delete(0,tk.END)
    entrada.insert(0,str(-vl))

#Poner boton C
def limpiar():
    global result
    
    entrada.delete(0, tk.END)
    entrada.insert(tk.END,"0")

#Poner boton CE
def limpiarTodo():
    entrada.delete(0, tk.END)
    entrada.insert("end","0")

#Poner boton Del
def quitar():
    txt1=entrada.get()
    txt=txt1[:len(txt1)-1]
    entrada.delete(0,tk.END)
    entrada.insert(tk.END,txt)

#Poner boton potencia




entrada=tk.Entry(ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right",state="normal")
entrada.insert(0,"0")
entrada.grid(row=0, column=0, columnspan=4)
text=""
ventana.grid_rowconfigure(8, weight=1)
ventana.grid_columnconfigure(8, weight=1)

btnMC=tk.Button(ventana, text="MC", width=4, height=1).grid (row=7, column=0,columnspan=1, padx=1, pady=2)
btnMR=tk.Button(ventana, text="MR", width=4, height=1 ).grid (row=3, column=0,columnspan=2,padx=1, pady=2)
btnMmas=tk.Button(ventana, text="M+", width=4, height=1 ).grid (row=3, column=1,columnspan=1,padx=1, pady=2)
btnMmenos=tk.Button(ventana, text="M-", width=4, height=1 ).grid (row=3, column=1,columnspan=2,padx=1, pady=2)
btnMS=tk.Button(ventana, text="MS", width=4, height=1 ).grid (row=3, column=2,columnspan=1,padx=1, pady=2)
btnM=tk.Button(ventana, text="M", width=4, height=1 ).grid (row=3, column=2, columnspan=2,padx=1, pady=2)

btnporciento=tk.Button(ventana, text="%", width=10, height=3 ).grid (row=4, column=0, columnspan=1, padx=2, pady=1)
btnCE=tk.Button(ventana, text="CE", width=10, height=3,command=lambda:limpiarTodo() ).grid (row=4, column=1, columnspan=1, padx=2, pady=1)
btnC=tk.Button(ventana, text="C", width=10, height=3,command=lambda:limpiar() ).grid (row=4, column=2, columnspan=1, padx=2, pady=1)
btngato=tk.Button(ventana, text="#", width=10, height=3,command=lambda:quitar() ).grid (row=4, column=3, columnspan=1, padx=2, pady=1)

btn1X=tk.Button(ventana, text="1/X", width=10, height=3 ).grid (row=5, column=0, columnspan=1, padx=2, pady=1)
btnX2=tk.Button(ventana, text="X2", width=10, height=3 ).grid (row=5, column=1, columnspan=1)
btn2X=tk.Button(ventana, text="2√X", width=10, height=3 ).grid (row=5, column=2, columnspan=1)
btnentre=tk.Button(ventana, text="/", width=10, height=3,command=lambda:calcula("/") ).grid (row=5, column=3, columnspan=1)

btn7=tk.Button(ventana, text="7", width=10, height=3,command=lambda:concatenar("7") ).grid (row=6, column=0, columnspan=1, padx=2, pady=1)
btn8=tk.Button(ventana, text="8", width=10, height=3,command=lambda:concatenar("8") ).grid (row=6, column=1, columnspan=1)
btn9=tk.Button(ventana, text="9", width=10, height=3,command=lambda:concatenar("9") ).grid (row=6, column=2, columnspan=1)
btnX=tk.Button(ventana, text="X", width=10, height=3,command=lambda:calcula("*") ).grid (row=6, column=3, columnspan=1)

btn4=tk.Button(ventana, text="4", width=10, height=3,command=lambda:concatenar("4") ).grid (row=7, column=0, columnspan=1, padx=2, pady=1)
btn5=tk.Button(ventana, text="5", width=10, height=3,command=lambda:concatenar("5") ).grid (row=7, column=1, columnspan=1)
btn6=tk.Button(ventana, text="6", width=10, height=3,command=lambda:concatenar("6") ).grid (row=7, column=2, columnspan=1)
btnMenos=tk.Button(ventana, text="-", width=10, height=3,command=lambda:calcula("-") ).grid (row=7, column=3, columnspan=1)

btn1=tk.Button(ventana, text="1", width=10, height=3,command=lambda:concatenar("1") ).grid (row=8, column=0, columnspan=1, padx=2, pady=1)
btn2=tk.Button(ventana, text="2", width=10, height=3,command=lambda:concatenar("2") ).grid (row=8, column=1, columnspan=1)
btn3=tk.Button(ventana, text="3", width=10, height=3,command=lambda:concatenar("3") ).grid (row=8, column=2, columnspan=1)
btnMas=tk.Button(ventana, text="+", width=10, height=3,command=lambda:calcula(entrada.get(),"+") ).grid (row=8, column=3, columnspan=1)

btnMasMenos=tk.Button(ventana, text="+/-", width=10, height=3,command=lambda:cambiarsigno() ).grid (row=9, column=0, columnspan=1, padx=2, pady=1)
btn0=tk.Button(ventana, text="0", width=10, height=3,command=lambda:concatenar("0") ).grid (row=9, column=1, columnspan=1)
btnPunto=tk.Button(ventana, text=".", width=10, height=3,command=lambda:ponpunto() ).grid (row=9, column=2, columnspan=1)
btnIgual=tk.Button(ventana, text="=", width=10, height=3,bg="blue" ).grid (row=9, column=3, columnspan=1)








ventana.mainloop()
