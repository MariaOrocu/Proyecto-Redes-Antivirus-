import tkinter as tk
import secundaria
import tercera


def mostrar_secundaria():
    principal.pack_forget()
    tercera.pack_forget()
    secundaria.pack(side="top", fill="both", expand=True)

def mostrar_tercera():
    principal.pack_forget()
    secundaria.pack_forget()
    tercera.pack(side="top", fill="both", expand=True)

def mostrar_principal():
    secundaria.pack_forget()
    tercera.pack_forget()
    principal.pack(side="top", fill="both", expand=True)


root = tk.Tk()
root.maxsize(width=300, height=300)
root.minsize(width=300, height=300)
principal = tk.Frame(root)
boton = tk.Button(principal, text="Login", command=mostrar_secundaria)
boton.place(x=10, y=10)
boton_m = tk.Button(principal, text="Registro", command=mostrar_tercera)
boton_m.place(x=70, y=10)
root.title("proyecto")
root.iconbitmap=("antivirus.ico")
secundaria = secundaria.ventana_secundaria(root, mostrar_principal)
tercera=tercera.ventana_tercera(root, mostrar_principal)
mostrar_principal()
root.mainloop()
