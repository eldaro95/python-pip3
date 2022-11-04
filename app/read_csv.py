import csv
from operator import itemgetter

def read_csv(path):
    with open(path,'r') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        header=next(reader) #Sacar la primera fila como cabecera
        data=[] #Crear una lista para guardar los diccionarios
        
        #Generar un ciclo para crear los diccionarios
        for row in reader:
            iterable =zip(header,row) #Crear tuplas con iterables
            datadic={key:value for key, value in iterable} #convertir tuplas en diccionarios 
            data.append(datadic)
        return data 
        

if __name__=='__main__':
    data = read_csv('sample.csv')
    print(data[0])