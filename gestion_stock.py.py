#creamos la clase
class Producto:
    def __init__(self, nombre, precio, stock): 
        self.nombre = nombre 
        self.precio = precio  
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= 0:
            print("\nLa cantidad a vender debe ser mayor que cero.")
            return

        if cantidad > self.stock:
            print(f"\nNo hay stock suficiente de {self.nombre}. Stock disponible: {self.stock}")
        else:
            self.stock -= cantidad
            print(f"\nVenta realizada. Stock de {self.nombre} restante es de {self.stock}")   

    def reponer(self, cantidad):
        if cantidad <= 0:
            print ("\nCantidad inválida.")
        else:    
            self.stock +=cantidad
            print(f"\nStcok actualizado. Cantidad de stock del producto {self.nombre} es de {self.stock}")  
#decidio poner un nuevo método solo para mostrar información y ahorrarme código

    def mostrar(self):
        print(f"\nNombre del producto: {self.nombre}")
        print(f"Precio del producto: {self.precio}€")
        print(f"Stock del producto: {self.stock}")          


 #me he informado en como crear lo que sería el equivalente a un main de java
if __name__ == "__main__":
    p1 = Producto("Televisión", 1200, 5)
    p2 = Producto("Consola", 500, 0)
    p3 = Producto("Bicicleta", 100, 10)

    p1.mostrar()
    p2.mostrar()
    p3.mostrar()

    p1.vender(3)
    p2.vender(5)
    p3.vender(1)

    p1.reponer(13)
    p2.reponer(10)
    p3.reponer(1)

    p1.mostrar()
    p2.mostrar()
    p3.mostrar()


    
