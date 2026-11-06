from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.crear_bd import crear_tablas
from persistencia.empleado_dao import EmpleadoDAO

# emp = Empleado("Juanito", "correo@gmail.com")

# emp2 = Empleado(
#     correo="julio@gmail.com",
#     nombre="julio",
# )

# print(emp.mostrar_datos())
# print(emp2.mostrar_datos())

# desarrollo = Departamento("Desarrollo")

# desarrollo.agregar_empleado(emp)
# desarrollo.agregar_empleado(emp2)
# print("cantidad: ", desarrollo.cantidad_empleados())
# print("lista empleados")
# for empleado in desarrollo.empleados:
#     print(empleado.mostrar_datos())

# print(desarrollo.cantidad_empleados())
# for empleado in desarrollo.empleados:
#     print(empleado.mostrar_datos())

crear_tablas()

emp = Empleado("correo@gmail.cl","juanito")
print(emp.mostrar_datos())
EmpleadoDAO.insertar(emp)
print(emp.mostrar_datos())
