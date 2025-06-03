import tkinter as tk
ventana=tk.Tk()
ventana.title("Camacho Zamora Adrian Eduardo-Calculadora")

entrada=tk.Entry(ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4)

ventana.grid_rowconfigure(8, weight=1)
ventana.grid_columnconfigure(8, weight=1)

boton1=tk.Button(ventana, text="MC", width=4, height=1).grid (row=7, column=0,columnspan=1, padx=1, pady=2)
boton2=tk.Button(ventana, text="MR", width=4, height=1 ).grid (row=3, column=0,columnspan=2,padx=1, pady=2)
boton3=tk.Button(ventana, text="M+", width=4, height=1 ).grid (row=3, column=1,columnspan=1,padx=1, pady=2)
boton4=tk.Button(ventana, text="M-", width=4, height=1 ).grid (row=3, column=1,columnspan=2,padx=1, pady=2)
boton4=tk.Button(ventana, text="MS", width=4, height=1 ).grid (row=3, column=2,columnspan=1,padx=1, pady=2)
boton5=tk.Button(ventana, text="M", width=4, height=1 ).grid (row=3, column=2, columnspan=2,padx=1, pady=2)

boton6=tk.Button(ventana, text="%", width=10, height=3 ).grid (row=4, column=0, columnspan=1, padx=2, pady=1)
boton7=tk.Button(ventana, text="CE", width=10, height=3 ).grid (row=4, column=1, columnspan=1, padx=2, pady=1)
boton8=tk.Button(ventana, text="C", width=10, height=3 ).grid (row=4, column=2, columnspan=1, padx=2, pady=1)
boton9=tk.Button(ventana, text="#", width=10, height=3 ).grid (row=4, column=3, columnspan=1, padx=2, pady=1)

boton10=tk.Button(ventana, text="1/X", width=10, height=3 ).grid (row=5, column=0, columnspan=1, padx=2, pady=1)
boton11=tk.Button(ventana, text="X2", width=10, height=3 ).grid (row=5, column=1, columnspan=1)
boton12=tk.Button(ventana, text="2√X", width=10, height=3 ).grid (row=5, column=2, columnspan=1)
boton13=tk.Button(ventana, text="/", width=10, height=3 ).grid (row=5, column=3, columnspan=1)

boton14=tk.Button(ventana, text="7", width=10, height=3 ).grid (row=6, column=0, columnspan=1, padx=2, pady=1)
boton15=tk.Button(ventana, text="8", width=10, height=3 ).grid (row=6, column=1, columnspan=1)
boton16=tk.Button(ventana, text="9", width=10, height=3 ).grid (row=6, column=2, columnspan=1)
boton17=tk.Button(ventana, text="X", width=10, height=3 ).grid (row=6, column=3, columnspan=1)

boton18=tk.Button(ventana, text="4", width=10, height=3 ).grid (row=7, column=0, columnspan=1, padx=2, pady=1)
boton19=tk.Button(ventana, text="5", width=10, height=3 ).grid (row=7, column=1, columnspan=1)
boton20=tk.Button(ventana, text="6", width=10, height=3 ).grid (row=7, column=2, columnspan=1)
boton21=tk.Button(ventana, text="-", width=10, height=3 ).grid (row=7, column=3, columnspan=1)

boton22=tk.Button(ventana, text="1", width=10, height=3 ).grid (row=8, column=0, columnspan=1, padx=2, pady=1)
boton23=tk.Button(ventana, text="2", width=10, height=3 ).grid (row=8, column=1, columnspan=1)
boton24=tk.Button(ventana, text="3", width=10, height=3 ).grid (row=8, column=2, columnspan=1)
boton25=tk.Button(ventana, text="+", width=10, height=3 ).grid (row=8, column=3, columnspan=1)

boton26=tk.Button(ventana, text="+/-", width=10, height=3 ).grid (row=9, column=0, columnspan=1, padx=2, pady=1)
boton27=tk.Button(ventana, text="0", width=10, height=3 ).grid (row=9, column=1, columnspan=1)
boton28=tk.Button(ventana, text=".", width=10, height=3 ).grid (row=9, column=2, columnspan=1)
boton29=tk.Button(ventana, text="=", width=10, height=3 ).grid (row=9, column=3, columnspan=1)


ventana.mainloop()
