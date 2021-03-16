#PROGRAMA DEL EJERCICIO 1.2: FFT DE UNA GAUSSIANA

# Importar módulos
import numpy as np
import matplotlib.pyplot as plt

# Constantes
tini = 0          # Tiempo inicial
tfin = 500e-6     # Tiempo final
N = 1000+1        # Número de puntos
s0 = 10e-6        # Valor de la varianza
t0 = 10*s0        # Valor de la media

# Crear vector discreto de tiempo
t = np.linspace(tini, tfin, N) #Vector de tiempo que va de tini a tfin y tiene N puntos

# Calcular la gaussiana
gauss = np.exp( - np.power(t - t0, 2) / (2 * s0**2))

# Representar la gaussiana
plt.plot(t, gauss)
plt.show()

# Calcular la transformada rápida de Fourier
np.fft(gauss)

# Representar la transformada de la gaussiana
plt.plot(t, gauss)
plt.show()

