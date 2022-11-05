import utils
import read_csv as rc
import charts
import pandas as pd
from collections import Counter

def run():
    
    f1='Sending Country Code'
    f2='Participant Age'
    
    df=pd.read_csv('sample.csv')
    
    df=df[df[f2]>=27] #filtrar solo los que cumplan
    
    #Graficar con pandas incluido conteo de f1
    s10=list(dict(df[f1].value_counts()).keys())
    s11=list(dict(df[f1].value_counts()).values())
    charts.pie_chart('Pandas de '+f1,s10,s11)
 
    #Graficar con pandas incluido conteo de f2
    p10=list(dict(df[f2].value_counts()).keys())
    p11=list(dict(df[f2].value_counts()).values())
    charts.bar_chart('Pandas de '+f2,p10,p11)
    
    #Sale diferente que el otro metodo (verificar)

if __name__ == '__main__':
    run()