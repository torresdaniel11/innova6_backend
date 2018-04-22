class Producto:

    def __init__(self, nombre, color, procioVenta, cantidad):
        self.nombre,
        self.color,
        self.precioVenta,
        self.cantidad

    def solicitarProducto(self, nombre, color, procioVenta, cantidad):
        self.validarCantidad(cantidad)
        return Producto(nombre, color, procioVenta, cantidad)

    def validarCantidad(self, cantidad):
        if cantidad < 0:
            self.cantidad = 0
        elif cantidad > 1000:
            self.cantidad = 1000
        else:
            self.cantidad = cantidad

