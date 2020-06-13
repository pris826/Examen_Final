from tkinter import ttk
from tkinter import *
import math
from datetime  import date
from datetime  import datetime

window = Tk()

ancho =600
alto =200
window.geometry(str(ancho)+"x"+str(alto))
window.title("Examen Final")
lbl111 = Label(window, text="Bienvenido")

lbl111.grid(column=1, row=0)

lbl = Label(window, text="Nombre")

lbl.grid(column=0, row=1)


txt = Entry(window,width=10)

txt.grid(column=1, row=1)

lbl2 = Label(window, text="Apellido")

lbl2.grid(column=0, row=2)

txt2 = Entry(window,width=10)

txt2.grid(column=1, row=2)

lbl3 = Label(window, text="Día")

lbl3.grid(column=0, row=3)

txt3 = Entry(window,width=10)

txt3.grid(column=1, row=3)

lbl4 = Label(window, text="Mes")

lbl4.grid(column=0, row=4)

txt4 = Entry(window,width=10)

txt4.grid(column=1, row=4)

lbl5 = Label(window, text="Año")

lbl5.grid(column=0, row=5)

txt5 = Entry(window,width=10)

txt5.grid(column=1, row=5)
labelText = StringVar()
labelText.set("Aca se verá el resultado de las funciones")
lbl11 = Label(window, textvariable=labelText)
lbl11.grid(column=0, row=7)

def codigo_hexadecimal():
    dia =hex(int( txt3.get()))
    mes =hex(int( txt4.get()))
    año =hex(int( txt5.get()))
    resultado = dia+"/"+mes+"/"+año
    labelText.set(str(resultado))

btn6 = Button(window, text="funcion 1", command=codigo_hexadecimal)

btn6.grid(column=1, row=6)

def vida_en_horas():
    dia =int( txt3.get())
    mes =int( txt4.get())
    año =int( txt5.get())
    fecha_cad1 =str(dia)+"-"+str(mes)+"-"+str(año)
    hoy= datetime.today()
    fecha1 = datetime.strptime(fecha_cad1, '%d-%m-%Y')
    tiempo = hoy-fecha1
    numeroDias=tiempo.days*24
    labelText.set("Usted nacio el "+ str(dia)+"/"+str(mes)+"/"+str(año)+" y ha vivido "+str(numeroDias)+" horas")

btn7 = Button(window, text="funcion 2", command=vida_en_horas)

btn7.grid(column=2, row=6)

def letras_par_o_impar():
    nombre=txt.get()
    apellido=txt2.get()
    todo= nombre+apellido  
    todo2= nombre+" "+apellido 
    suma=  len(todo)
    respuesta="impar"
    if suma%2==0:
        respuesta="par"
    labelText.set(todo2+" su nombre junto con su apellido es "+respuesta)

    lbl.configure(text="Button was clicked !!")

btn8 = Button(window, text="funcion 3", command=letras_par_o_impar)

btn8.grid(column=3, row=6)

def vocales_y_consonantes():
    nombre=str(txt.get())
    apellido=str(txt2.get())
    Suma = 0
    for vc in nombre:
        if vc == 'a' or vc =='A' or vc =='e' or vc =='E' or vc =='i' or vc =='I' or vc =='o' or vc =="O" or vc =="u" or vc =="U":
            Suma += 1
    for vc in nombre:
        if vc == 'a' or vc =='A' or vc =='e' or vc =='E' or vc =='i' or vc =='I' or vc =='o' or vc =="O" or vc =="u" or vc =="U":
            Suma += 1
    Con1=len(nombre)
    Con2=len(apellido)
    SalidaConsola=Con1+Con2-Suma

    labelText.set(nombre + " " + apellido + ' tiene {} vocales y {} consonantes.'.format(Suma,SalidaConsola))
    
btn9 = Button(window, text="funcion 4", command=vocales_y_consonantes)

btn9.grid(column=4, row=6)

def nombre_y_apellido_al_reves():
    text80 = txt.get()+" "+txt2.get()
    text80 = text80[::-1]
    labelText.set(txt.get()+" "+txt2.get()+"Su nombre y apellido es" + text80) 

btn10 = Button(window, text="funcion 5", command=nombre_y_apellido_al_reves)

btn10.grid(column=5, row=6)


window.mainloop()

