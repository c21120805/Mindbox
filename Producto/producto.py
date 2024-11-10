import tkinter as tk
from tkinter import messagebox

# Excepciones personalizadas
class ProductoInvalidoException(Exception):
    pass

class PrecioInvalidoException(Exception):
    pass

class CantidadInvalidaException(Exception):
    pass

class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or not nombre.isalpha():
            raise ProductoInvalidoException("El nombre del producto no es valido.")
        if precio <= 0:
            raise PrecioInvalidoException("El precio debe ser mayor que cero.")
        if cantidad < 0:
            raise CantidadInvalidaException("La cantidad no puede ser negativa.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def mostrar_detalles(self):
        valor_total = self.calcular_valor_total()
        return (f"Producto: {self.nombre}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Valor total: ${valor_total:.2f}")

productos_registrados = []

def agregar_producto():
    nombre = nombre_var.get()
    try:
        precio = float(precio_var.get())
        cantidad = int(cantidad_var.get())
    
        producto = Producto(nombre, precio, cantidad)
        productos_registrados.append(producto)
        detalles = producto.mostrar_detalles()
        messagebox.showinfo("Detalles del Producto", detalles)
    except ProductoInvalidoException as e:
        messagebox.showerror("Error de Producto", str(e))
    except PrecioInvalidoException as e:
        messagebox.showerror("Error de Precio", str(e))
    except CantidadInvalidaException as e:
        messagebox.showerror("Error de Cantidad", str(e))
    except ValueError:
        messagebox.showerror("Error de Entrada", "Asegúrese de que precio y cantidad sean numéricos.")
    finally:
        nombre_var.set("")
        precio_var.set("")
        cantidad_var.set("")

def mostrar_productos_registrados():
    if not productos_registrados:
        messagebox.showinfo("Productos Registrados", "No hay productos registrados.")
    else:
        detalles_todos = "\n\n".join([producto.mostrar_detalles() for producto in productos_registrados])
        messagebox.showinfo("Productos Registrados", detalles_todos)

root = tk.Tk()
root.title("Gestión de Productos")
root.geometry("400x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

nombre_var = tk.StringVar()
precio_var = tk.StringVar()
cantidad_var = tk.StringVar()
producto_var = tk.StringVar()

tk.Label(frame, text="Nombre del Producto:", bg="#1E3A5F", fg="white").grid(row=0, column=0, sticky="e", pady=5)
tk.Entry(frame, textvariable=nombre_var, width=25).grid(row=0, column=1, pady=5)

tk.Label(frame, text="Precio del Producto:", bg="#1E3A5F", fg="white").grid(row=1, column=0, sticky="e", pady=5)
tk.Entry(frame, textvariable=precio_var, width=25).grid(row=1, column=1, pady=5)

tk.Label(frame, text="Cantidad en Inventario:", bg="#1E3A5F", fg="white").grid(row=2, column=0, sticky="e", pady=5)
tk.Entry(frame, textvariable=cantidad_var, width=25).grid(row=2, column=1, pady=5)

tk.Button(frame, text="Agregar Producto", command=agregar_producto, bg="#800020", fg="white").grid(row=3, columnspan=2, pady=10)
tk.Button(frame, text="Mostrar Productos Registrados", command=mostrar_productos_registrados, bg="#800020", fg="white").grid(row=4, columnspan=2, pady=10)


root.mainloop()