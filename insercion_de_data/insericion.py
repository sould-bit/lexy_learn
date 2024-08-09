#%%
import pandas as pd


from sqlalchemy import create_engine

host='172.22.167.209'
user='jhon_root'
password='****'
database='lexy_DB'
port = '3306'



#pasamos la base de datos 
df = pd.read_csv('../words_v_0.4.csv')
df2 = pd.read_csv('../american_slang1.csv')


engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")


table_name = 'american_slang'

try:
    df2.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print("Datos subidos exitosamente a la base de datos")
except Exception as e:
    print(f"Error al subir los datos: {e}")