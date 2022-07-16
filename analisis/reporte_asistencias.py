import pandas as pd

estudiantes = pd.read_csv("datos\estudiante.csv", delimiter=',')
print(estudiantes)

asistencias = pd.read_csv("datos\sistencia.csv", delimiter=',')
print(asistencias)

sistencia = pd.read_csv("datos\sistencia.csv", delimiter=',')
asistencias_completas = pd.merge(estudiantes,sistencia, on="cedula", how="left")
print(asistencias_completas)

asistencias_completas.to_csv("datos\completo.csv")
