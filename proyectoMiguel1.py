import pandas as pd

Datos= pd.read_csv('Datos.csv', index_col="id")



DatosFiltrados2= Datos [(Datos['gastos'] <= Datos['ganancias_anuales']*0.75)]   
DatosFiltrados2= DatosFiltrados2[["gastos", "ganancias_anuales"]]
print(DatosFiltrados2)

DatosFiltrados2.to_csv('DatosFiltrados2.csv')

