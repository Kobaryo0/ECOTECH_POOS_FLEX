from dominio.empleado import Empleado

emp = Empleado("Juanito", "correo@gmail.com")

emp2 = Empleado(
    correo="julio@gmail.com",
    nombre="julio",
)

print(emp.mostrar_datos())
print(emp2.mostrar_datos())