import tkinter as tk
from tkinter import messagebox

datos = {
    "circulo": {},
    "cuadrado": {},
    "rect": {},
    "tri": {}
}

def actualizar_resultados():
    resultados_text.delete("1.0", tk.END)
    for forma, valores in datos.items():
        if "a" in valores:
            if forma == "circulo":
                resultados_text.insert(tk.END, f"Círculo - Radio: {valores['r']} -Área: {valores['a']:.2f}\n")
            elif forma == "cuadrado":
                resultados_text.insert(tk.END, f"Cuadrado - Lado: {valores['l']} -Área: {valores['a']:.2f}\n")
            elif forma == "rect":
                resultados_text.insert(tk.END, f"Rectángulo - Base: {valores['b']}, Altura: {valores['h']} -Área: {valores['a']:.2f}\n")
            elif forma == "tri":
                resultados_text.insert(tk.END, f"Triángulo - Base: {valores['b']}, Altura: {valores['h']} -Área: {valores['a']:.2f}\n")

def limpiar():
    for w in area.winfo_children():
        w.destroy()

def pantalla_circulo():
    limpiar()
    tk.Label(area, text="Área del Círculo", font=("Arial", 14)).pack(pady=10)
    tk.Label(area, text="Radio:").pack()

    entrada = tk.Entry(area)
    entrada.pack(pady=5)

    res = tk.Label(area, text="")
    res.pack()

    if "r" in datos["circulo"]:
        entrada.insert(0, datos["circulo"]["r"])
        res.config(text=f"Área: {datos['circulo']['a']:.2f}")

    def calcular():
        try:
            r = float(entrada.get())
            a = 3.1416 * r ** 2
            datos["circulo"] = {"r": r, "a": a}
            res.config(text=f"Área: {a:.2f}")
            actualizar_resultados()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(area, text="Calcular", command=calcular).pack(pady=5)

def pantalla_cuadrado():
    limpiar()
    tk.Label(area, text="Área del Cuadrado", font=("Arial", 14)).pack(pady=10)
    tk.Label(area, text="Lado:").pack()

    entrada = tk.Entry(area)
    entrada.pack(pady=5)

    res = tk.Label(area, text="")
    res.pack()

    if "l" in datos["cuadrado"]:
        entrada.insert(0, datos["cuadrado"]["l"])
        res.config(text=f"Área: {datos['cuadrado']['a']:.2f}")

    def calcular():
        try:
            l = float(entrada.get())
            a = l ** 2
            datos["cuadrado"] = {"l": l, "a": a}
            res.config(text=f"Área: {a:.2f}")
            actualizar_resultados()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

    tk.Button(area, text="Calcular", command=calcular).pack(pady=5)

def pantalla_rect():
    limpiar()
    tk.Label(area, text="Área del Rectángulo", font=("Arial", 14)).pack(pady=10)
    tk.Label(area, text="Base:").pack()
    entrada_b = tk.Entry(area)
    entrada_b.pack(pady=5)

    tk.Label(area, text="Altura:").pack()
    entrada_h = tk.Entry(area)
    entrada_h.pack(pady=5)

    res = tk.Label(area, text="")
    res.pack()

    if "b" in datos["rect"]:
        entrada_b.insert(0, datos["rect"]["b"])
        entrada_h.insert(0, datos["rect"]["h"])
        res.config(text=f"Área: {datos['rect']['a']:.2f}")

    def calcular():
        try:
            b = float(entrada_b.get())
            h = float(entrada_h.get())
            a = b * h
            datos["rect"] = {"b": b, "h": h, "a": a}
            res.config(text=f"Área: {a:.2f}")
            actualizar_resultados()
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos.")

    tk.Button(area, text="Calcular", command=calcular).pack(pady=5)

def pantalla_tri():
    limpiar()
    tk.Label(area, text="Área del Triángulo", font=("Arial", 14)).pack(pady=10)
    tk.Label(area, text="Base:").pack()
    entrada_b = tk.Entry(area)
    entrada_b.pack(pady=5)

    tk.Label(area, text="Altura:").pack()
    entrada_h = tk.Entry(area)
    entrada_h.pack(pady=5)

    res = tk.Label(area, text="")
    res.pack()

    if "b" in datos["tri"]:
        entrada_b.insert(0, datos["tri"]["b"])
        entrada_h.insert(0, datos["tri"]["h"])
        res.config(text=f"Área: {datos['tri']['a']:.2f}")

    def calcular():
        try:
            b = float(entrada_b.get())
            h = float(entrada_h.get())
            a = 0.5 * b * h
            datos["tri"] = {"b": b, "h": h, "a": a}
            res.config(text=f"Área: {a:.2f}")
            actualizar_resultados()
        except ValueError:
            messagebox.showerror("Error", "Ingresa números válidos.")

    tk.Button(area, text="Calcular", command=calcular).pack(pady=5)

vent = tk.Tk()
vent.title("Áreas")
vent.geometry("600x500")
vent.config(bg="lightblue")

menu = tk.Frame(vent, bg="lightblue", width=120)
menu.pack(side="left", fill="y")

area = tk.Frame(vent, bg="white")
area.pack(side="top", expand=True, fill="both")

resultados_text = tk.Text(vent, height=7, bg="lightyellow", state="normal")
resultados_text.pack(side="bottom", fill="x")

tk.Button(menu, text="Círculo", command=pantalla_circulo, width=15).pack(pady=10)
tk.Button(menu, text="Cuadrado", command=pantalla_cuadrado, width=15).pack(pady=10)
tk.Button(menu, text="Rectángulo", command=pantalla_rect, width=15).pack(pady=10)
tk.Button(menu, text="Triángulo", command=pantalla_tri, width=15).pack(pady=10)
tk.Button(menu, text="Salir", command=vent.destroy, width=15).pack(pady=30)

pantalla_circulo()
vent.mainloop()