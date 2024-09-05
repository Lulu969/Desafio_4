import numpy as np

B = 20  
H = 0.3 
n = 0.03  
S = 0.0003  

n_rango = (n * (1 - 0.1), n * (1 + 0.1))  
S_rango = (S * (1 - 0.1), S * (1 + 0.1))  

def calcular_flujo(B, H, n, S):
    return (1 * (B * H)**(5/3) * n * (B + 2 * H)**(2/3) * np.sqrt(S))

Q_n_base = calcular_flujo(B, H, n, S)
Q_n_lower = calcular_flujo(B, H, n_rango[0], S)
Q_n_upper = calcular_flujo(B, H, n_rango[1], S)

Q_S_lower = calcular_flujo(B, H, n, S_rango[0])
Q_S_upper = calcular_flujo(B, H, n, S_rango[1])

sensibilidad_n = ((Q_n_upper - Q_n_lower) / Q_n_base) * 100
sensibilidad_S = ((Q_S_upper - Q_S_lower) / Q_n_base) * 100

print(f"Flujo Q (n base): {Q_n_base:.4f} m³/s")
print(f"Flujo Q (n límite inferior): {Q_n_lower:.4f} m³/s")
print(f"Flujo Q (n límite superior): {Q_n_upper:.4f} m³/s")
print(f"Flujo Q (S límite inferior): {Q_S_lower:.4f} m³/s")
print(f"Flujo Q (S límite superior): {Q_S_upper:.4f} m³/s")
print(f"Sensibilidad respecto a n: {sensibilidad_n:.2f}%")
print(f"Sensibilidad respecto a S: {sensibilidad_S:.2f}%")
