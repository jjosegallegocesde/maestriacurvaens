import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Datos de ejemplo para la Curva S
tiempo = np.array([2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023])  # Años.)
nokia = np.array([8,20,20,13,13,16,48,64,64,50,64])
samsung = np.array([13,16,16,12,12,12,16,64,64,50,50])
apple = np.array([8,8,12,12,12,12,12,12,12,48,48])
huawei = np.array([8,13,13,12,20,24,40,50,50,50,48])
asusRog = np.array([0,0,0,0,0,28,48,64,64,50,50])  

#fondo
sns.set(style="whitegrid")

# Crear la gráfica de la Curva S utilizando Seaborn
sns.lineplot(x=tiempo, y=nokia, label='NOKIA')
sns.lineplot(x=tiempo, y=samsung, label='SAMSUNG')
sns.lineplot(x=tiempo, y=apple, label='APPLE')
sns.lineplot(x=tiempo, y=huawei, label='HUAWEI')
sns.lineplot(x=tiempo, y=asusRog, label='ASUS ROG')

# Configurar etiquetas y título
plt.xlabel('Tiempo')
plt.ylabel('Desempeño camara en Mpx')
plt.title('Análisis desempeño capacidad de cámara fotográfica')


#Guardo
plt.savefig('curvaMaestria.png')

# Mostrar leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
