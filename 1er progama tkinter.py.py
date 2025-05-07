import tkinter as tk 
def saludar():
    nombre=entrada_nombre.get()
    edad=entrada_edad.get()
    etiqueta_resultado.config(text=f"Hola {nombre}, tu edad es de {edad}")
    

ventana = tk.Tk() 
ventana.title("Mi primera app grafica") 
ventana.geometry("400x200")
ventana.config(bg="aquamarine")

etiqueta_nombre = tk.Label(ventana, text="Ingresa tu nombre:") 
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana) 
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Ingresa tu edad")
etiqueta_edad.pack()

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton = tk.Button(ventana, text="Mostrar saludo", command=saludar) 
boton.pack() 
etiqueta_resultado = tk.Label(ventana, text="") 
etiqueta_resultado.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

etiqueta = tk.Label (ventana, text="El autor de este programa fue: Jorge Mendoza Rodriguez")
etiqueta.pack()

ventana.mainloop()
