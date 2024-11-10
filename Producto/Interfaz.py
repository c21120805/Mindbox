import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Gestión de Productos")
root.geometry("300x250")

nombre_var = tk.StringVar()
precio_var = tk.StringVar()
cantidad_var = tk.StringVar()

def agregar_producto():
    nombre = nombre_var.get()
    try:
        precio = float(precio_var.get())
        cantidad = int(cantidad_var.get())
        
        producto = Producto(nombre, precio, cantidad)
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

tk.Label(root, text="Nombre del Producto:").pack(pady=5)
tk.Entry(root, textvariable=nombre_var).pack(pady=5)

tk.Label(root, text="Precio del Producto:").pack(pady=5)
tk.Entry(root, textvariable=precio_var).pack(pady=5)

tk.Label(root, text="Cantidad en Inventario:").pack(pady=5)
tk.Entry(root, textvariable=cantidad_var).pack(pady=5)

tk.Button(root, text="Agregar Producto", command=agregar_producto).pack(pady=10)


root.mainloop()