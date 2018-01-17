import numpy
import quandl as qn

df = qn.get('WIKI/GOOGL')

print(df.head())