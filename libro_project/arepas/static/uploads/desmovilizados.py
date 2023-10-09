import pandas as pd

try:
    with open("datos_desmovilizados.csv", "r") as file:
        line = file.readline()
        print(line)
except FileNotFoundError:
    print("El archivo no se encuentra en la ubicación especificada.")

ruta = r"datos_desmovilizados.csv"
df = pd.read_csv(ruta)
df = df[['Departamento','Año Desmovilización','Número Desmovilizados','FechaCorte','FechaActualizacion']]

print(df)