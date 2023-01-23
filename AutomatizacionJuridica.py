#Codigo para recibir los datos del Excel:
import pandas
infoExcel = pandas.read_excel('Desktop/Prueba.xls', header=18, usecols='A, E')
m1 = infoExcel
print(m1)


#Codigo para crear excel:
