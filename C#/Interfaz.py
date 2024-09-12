import tkinter as tk
from tkinter import messagebox, ttk
from API import apiAccidentes
from ordenamiento import Funciones_de_Ordenamiento as FO

class InterfazAPI:
    def __init__(self, master):
        self.master = master
        self.master.title("Consumo de API y Ordenamiento")
        self.master.geometry("500x400")

        self.api = apiAccidentes('https://www.datos.gov.co/resource/mg8y-amuh.json')
        self.ordenador = FO()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Datos de la API:")
        self.label.pack(pady=10)

        self.text_area = tk.Text(self.master, height=10, width=60)
        self.text_area.pack(pady=10)

        self.fetch_button = tk.Button(self.master, text="Obtener Datos", command=self.obtener_datos)
        self.fetch_button.pack(pady=5)

        self.sort_label = tk.Label(self.master, text="Selecciona un método de ordenamiento:")
        self.sort_label.pack(pady=5)

        self.sort_method = ttk.Combobox(self.master, values=["Merge Sort", "Quick Sort", "Selection Sort", "Insertion Sort"])
        self.sort_method.pack(pady=5)
        self.sort_method.current(0)  # Establecer el método por defecto

        self.sort_button = tk.Button(self.master, text="Ordenar", command=self.ordenar_datos)
        self.sort_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="Resultados:")
        self.result_label.pack(pady=10)

        self.result_area = tk.Text(self.master, height=10, width=60)
        self.result_area.pack(pady=10)

    def obtener_datos(self):
        try:
            arreglo = self.api.consumo()
            self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto
            self.text_area.insert(tk.END, str(arreglo))  # Mostrar datos obtenidos
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ordenar_datos(self):
        metodo = self.sort_method.get()
        datos = self.text_area.get(1.0, tk.END).strip()
        
        if not datos:
            messagebox.showwarning("Advertencia", "Primero obtén los datos de la API.")
            return
        
        # Convertir el texto en una lista de enteros
        try:
            arreglo = eval(datos)  # Usar eval para convertir el texto en lista (asegúrate de que los datos sean seguros)
        except Exception as e:
            messagebox.showerror("Error", "Error al procesar los datos.")
            return

        if metodo == "Merge Sort":
            resultado = self.ordenador.MergeSort(arreglo)
        elif metodo == "Quick Sort":
            resultado = self.ordenador.quick(arreglo)
        elif metodo == "Selection Sort":
            resultado = self.ordenador.SelectionSort(arreglo)
        elif metodo == "Insertion Sort":
            resultado = self.ordenador.InsertionSort(arreglo)

        self.result_area.delete(1.0, tk.END)  # Limpiar el área de resultados
        self.result_area.insert(tk.END, str(resultado))  # Mostrar resultados ordenados

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazAPI(root)
    root.mainloop()