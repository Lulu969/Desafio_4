
def f(x):
    return 25 * x**3 - 6 * x**2 + 7 * x - 88

def f_primero(x):
    return 75 * x**2 - 12 * x + 7

def f_doble(x):
    return 150 * x - 12

def f_triple(x):
    return 150

x0 = 1
f_x0 = f(x0)
f_primero_x0 = f_primero(x0)
f_doble_x0 = f_doble(x0)
f_triple_x0 = f_triple(x0)

x = 3
taylor_approx = (f_x0 
                + f_primero_x0 * (x - x0) 
                + (f_doble_x0 / 2) * (x - x0)**2 
                + (f_triple_x0 / 6) * (x - x0)**3)
real_value = f(x)

relative_error = abs((real_value - taylor_approx) / real_value) * 100

print(f"Valor aproximado con serie de Taylor (tercer orden): {taylor_approx}")
print(f"Valor real de f(3): {real_value}")
print(f"Error relativo porcentual: {relative_error:.2f}%")
