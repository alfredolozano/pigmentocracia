import os
import csv

#Function to get the right color of a person
def getAvgColors(arrayColors):
	aux = arrayColors**2
	aux = avg(aux)
	return avg



#Para cada archivo
with open('/home/g/Desktop/ColorProject/namesData/nameFiles.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	#Extraer los colores para cada id de nombre (contador)
	for row in reader:
		name = row['name']
		n = row['n']
		#Crear csv
		cad = "echo '' > " + fileName + ".csv"
		os.system(cad)
		#Crear un csv y llenar con *idDiputado y *color
		for idPerson in range(0,n):
			colors = get_colors(idPerson)
			avgColors = getAvgColors(colors)
			#Escribe en el nuevo csv el id y el color promedio
			cad2 = fileName + ".csv"
			with open(cad2, 'w') as csvfile:
			    fieldnames = ['idPerson', 'color']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			    writer.writeheader()
			    writer.writerow({'idPerson': idPerson, 'color': avgColors})