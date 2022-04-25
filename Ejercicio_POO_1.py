class Cliente:
    
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __str__(self):
        return '{} {} melo'.format(self.nombre,self.apellidos)
    

class Empresa:
    
    def __init__(self, clientes=[]):
        self.clientes = clientes
        
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")
    
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(c,"> BORRADO")
                return
        print("Cliente no encontrado")

hector = Cliente(nombre="Hector",apellidos="Costa Guzman", dni="111111A")
juan = Cliente("222222B","Juan","Gonzales Marquez")
daniel = Cliente("111111C","Daniel","Almario Quintero")
empresa= Empresa(clientes=[hector,juan])
empresa.mostrar_cliente("222222B")
empresa.borrar_cliente("222222B")
print(str(juan))