import DataFrame_MySQL as dm
import pandas as pd

df = pd.read_csv('names.csv')

con = dm.get_connection()
dm.Push_to_MySQL(df,'testtable2',con)
