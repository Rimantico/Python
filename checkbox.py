from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title( 'Ejemplo de seleccion múltiple' )
frame = Frame( window )
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
e
book_1 = Checkbutton( frame , text = 'Seguridad y alta disponibilidad' , 
variable = var_1 , onvalue = 1 , offvalue = 0 )
book_2 = Checkbutton( frame , text = 'Servicios de Red e Internet' , 
variable = var_2 , onvalue = 1 , offvalue = 0 )
book_3 = Checkbutton( frame , text = 'Programacion en Python' , 
variable = var_3 , onvalue = 1 , offvalue = 0 )
def dialog() :
    str = 'Tu eleccion:'
    if var_1.get() == 1 : str += '\nSeguridad y alta disponibilidad'
    if var_2.get() == 1 : str += '\nServicios de Red e Internet'
    if var_3.get() == 1 : str += '\nProgramacion en Python'
    box.showinfo( 'Selection' , str )
btn = Button( frame , text = 'Elige' , command = dialog )
btn.pack( side = RIGHT , padx = 5 )
book_1.pack( side = LEFT )
book_2.pack( side = LEFT )
book_3.pack( side = LEFT )
frame.pack( padx = 30, pady = 30 )
window.mainloop()
