import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora de área")
ventana.geometry("500x400")
ventana.config(bg="sky blue")

etiqueta1 = tk.Label(ventana, text="Radio", bg="red")
etiqueta1.pack()

entrada_radio = tk.Entry(ventana, bg="yellow")
entrada_radio.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="sky blue")
etiqueta_resultado.pack()

boton_calcular = tk.Button(ventana, text="Calcular área", bg="orange")
boton_calcular.pack()

boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="orange")
boton_cerrar.pack()

boton_calcular.config(command=lambda: etiqueta_resultado.config(
    text=(f"El área es grande: {(float(entrada_radio.get())**2 * 3.14):}"
          if (float(entrada_radio.get())**2 * 3.14) >= 100
          else f"El área es pequeña: {(float(entrada_radio.get())**2 * 3.14):}")
    if entrada_radio.get().replace(".", "", 1).isdigit()
    else "Ingresa un valor numérico válido"
))

ventana.mainloop()