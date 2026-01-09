#creamos la clase
class Producto:
    def __init__(self, nombre, precio, stock): 
        self.nombre = nombre 
        self.precio = precio  
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a vender debe ser mayor que cero.")
            return

        if cantidad > self.stock:
            print(f"No hay stock suficiente de {self.nombre}. Stock disponible: {self.stock}")
        else:
            self.stock -= cantidad
            print(f"Venta realizada. Stock de {self.nombre} restante es de {self.stock}")   

    def reponer(self, cantidad):
        if cantidad <= 0:
            print ("Cantidad inválida.")
        else:    
            self.stock +=cantidad
            print(f"Stcok actualizado. Cantidad de stock del producto {self.nombre} es de {self.stock}")    


    