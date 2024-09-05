import math

def taylor_ln(x, n_terms=4):
    if x <= 0:
        raise ValueError("x debe ser mayor que 0")
    
    # Derivadas en x=1
    f_1 = math.log(1)  
    f_primero_1 = 1     
    f_doble_1 = -1 
    f_triple_1 = 2   
    f_cuatro_1 = -6   

    # Serie de Taylor
    x_1 = x - 1  # Desplazamos x a 0
    aproximacion = f_1 + f_primero_1 * x_1 \
                    + (f_doble_1 / 2) * (x_1 ** 2) \
                    + (f_triple_1 / 6) * (x_1 ** 3) \
                    + (f_cuatro_1 / 24) * (x_1 ** 4)

    return aproximacion

x_value = 2.5
aproximacion = taylor_ln(x_value)

true_value = math.log(x_value)

error_relative = abs(true_value - aproximacion) / true_value * 100

print(f"Aproximación de ln({x_value}) usando Taylor: {aproximacion}")
print(f"Valor verdadero de ln({x_value}): {true_value}")
print(f"Error relativo porcentual: {error_relative:.2f}%")
