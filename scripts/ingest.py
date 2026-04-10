import requests
import pandas as pd

#1. URL de la api
url = "https://jsonplaceholder.typicode.com/posts"

#optener datos
response = requests.get(url)

3#convertir a json
data = response.json()

#4 convertir a dataframe
df = pd.DataFrame(data)

#5 mostrar primeras filas
print(df.head())

#6 guardar en csv
df.to_csv("data/raw_post.csv", index=False)

print("Datos guardados en data/raw_post.csv con exito")

print(df.info())