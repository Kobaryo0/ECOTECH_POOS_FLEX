class Empleado:
        
    def __init__(self,nombre:str, correo:str, id = None):
        self.nombre = nombre
        self.correo = correo
        self.id = id
    
    def mostrar_datos(self) -> str:
        return f"""nombre> {self.nombre} 
        \n correo: {self.correo}
        \n id: {self.id}"""