import pandas as pd

Datos= pd.read_csv('Datos.csv', index_col="id")

DatosFiltrados = Datos [(Datos['gastos'] <= Datos['ganancias_anuales'])]
print(DatosFiltrados)

DatosFiltrados2= Datos [(Datos['gastos'] <= Datos['ganancias_anuales']*0.75)]   
print(DatosFiltrados2)

