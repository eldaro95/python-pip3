import utils
import read_csv as rc
import charts
from collections import Counter

def run():
    data =rc.read_csv('sample.csv')
    #Filtrar datos por tiempo de mobilidad minima
    tmin=int(input('Ingrese la edad minima: '))
    result=utils.fmin('Participant Age',tmin,data)
    #Obtenemos datos de pais y contamos
    field1='Sending Country Code'
    l_pais , v_pais = utils.count(field1,result)
    charts.pie_chart(field1,l_pais,v_pais)
    
    #Obtenemos datos de edad y contamos
    field2='Participant Age'
    l_p , v_p = utils.count(field2,result)
    charts.bar_chart(field2,l_p,v_p) 
    #charts.pie_chart(pais,edad)
    
''' Para realizar graficos de una fila con datos en varias columnas
    if result>0:
        p_result=result[0]
        name=p_result['Project Reference']
        labels, values=utils.get_age(p_result) 
        charts.pie_chart(name,labels,values) 
'''

if __name__ == '__main__':
    run()