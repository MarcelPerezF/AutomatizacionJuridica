#Sistema Automatizacion Juridica

#Codigo para recibir los datos del Excel:
import pandas as pd
infoExcel = pd.read_excel('Desktop/prueba2.xls', header=18, usecols='A, E, AE')
infoExcel2 = infoExcel.dropna()

# Agregar linea:
insert_rows = 2
infoExcel2.index = range(0, insert_rows * len(infoExcel2), insert_rows)
infoExcel2 = infoExcel2.reindex(index = range(insert_rows * len(infoExcel2))) 

# Agregar columna:
infoExcel2=infoExcel2.assign(Comentario="")
m1 = infoExcel2.to_string()

print(m1)

#Codigo para crear excel:
writer = pd.ExcelWriter('Desktop/Inventario_Expediente_FECHAACTUAL.xlsx', engine='xlsxwriter')
infoExcel2.to_excel(writer, sheet_name='Expediente_FECHAACTUAL', index=False)
writer.close()

