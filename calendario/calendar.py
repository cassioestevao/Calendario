import tkinter as tk
import calendar
from tkinter import messagebox

root = tk.Tk()
root.title("Calendario | Cássio Estevão ")
root.configure(bg="purple")
root.geometry("660x450")
root.resizable(False, False)

def mostrar_calendario(year):
    cal = calendar.calendar(int(year))
    return cal

def exibir_calendario():
    year = entry_ano.get()
    try:
        year = int(year)
        cal = mostrar_calendario(year)
        text_calendario.delete(1.0, tk.END)
        text_calendario.insert(tk.END, cal)
    except ValueError:
        messagebox.showerror("Erro", "Ano inválido")

label_ano = tk.Label(root, 
                     text="Digite o ano:",
                     width=10,
                     bg="purple",
                     fg="white"
                     )
label_ano.pack()

entry_ano = tk.Entry(root,
                     bg="purple",
                     fg="white"
                     )
entry_ano.pack()

button_exibir = tk.Button(root, 
                          text="Exibir Calendário", 
                          command=exibir_calendario,
                          anchor=tk.CENTER,
                          bg="purple",
                          fg="white"
                          )
button_exibir.pack()

text_calendario = tk.Text(root,
                          bg="purple",
                          fg="white",
                          relief="solid", 
                          border=1,
                          height=25, 
                          width=75,
                          )
text_calendario.pack()

root.mainloop()
