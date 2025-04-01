import sympy as sp

# Definir la variable
x = sp.Symbol('x')

# Definir la ecuación: x^2 - 4 = 0
ecuacion = x**2 - 4

# Resolver la ecuación
soluciones = sp.solve(ecuacion, x)

# Mostrar las soluciones
print("Las soluciones de la ecuación son:", soluciones)


 
