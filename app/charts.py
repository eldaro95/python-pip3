import matplotlib.pyplot as plt

def bar_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    ax.autoscale()
    fig.autofmt_xdate()
    plt.title(f'Grafico de barra de: {name}')
    plt.savefig(f'./imgs/bar_{name}.png')
    plt.close()
    
def pie_chart(name,labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels,autopct='%1.1f%%',shadow=True)
    ax.axis('equal')
    plt.title(f'Grafico de pastel de: {name}')
    plt.savefig(f'./imgs/pie_{name}.png')
    plt.close()
    

if __name__=="__main__":
    labels =['A','B','C']
    values=[900,800,200]
    pie_chart(labels,values)