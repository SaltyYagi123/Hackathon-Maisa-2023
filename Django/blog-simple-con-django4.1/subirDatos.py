import pandas as pd
import sqlite3
import uuid

# Leer el archivo CSV
df = pd.read_csv('search_data.csv')

# Generar identificadores únicos para la columna 'id' como enteros
df['id'] = range(1, len(df) + 1)

# Añadir una columna "resume"
df['resume'] = ''

# Reordenar las columnas para que 'id' esté al inicio
df = df[['id'] + [col for col in df.columns if col != 'id']]

# Guardar los datos en la base de datos SQLite
conn = sqlite3.connect('db.sqlite3')

# Crear la tabla core_factify con id como clave primaria
df.to_sql('core_factifys', conn, if_exists='replace', index=False,
          dtype={'id': 'INTEGER PRIMARY KEY'})

# Cerrar la conexión a la base de datos
conn.close()
