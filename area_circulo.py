import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora de area")
ventana.geometry("500x400")
ventana.config(bg="sky blue")

def calcular_area():
    try:
        radio = float(entrada_radio.get())
        area = (radio*radio)*3.14

        if area >= 100:
            resultado = f"el area es grande  {area}"
        else:
            resultado = f"el area es pequeña {area}"

        etiqueta_resultado.config(text=resultado)

    except ValueError:
        etiqueta_resultado.config(text="ingresa tus datos")

def cerrar ():
    ventana.destroy()

etiqueta1 = tk.Label(ventana, text="radio", bg="red")
etiqueta1.pack()
entrada_radio = tk.Entry(ventana, bg="yellow")
entrada_radio.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="sky blue")
etiqueta_resultado.pack()

boton_calcular = tk.Button(ventana, text="calcular area", command=calcular_area, bg="orange")
boton_calcular.pack()

boton = tk.Button(ventana, text="salir",command=cerrar)
boton.pack()

ventana.mainloop()