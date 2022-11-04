import matplotlib.pyplot as plt

def bar_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig('bar.png')
    plt.close()
    
def pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,labels=labels)
    ax.axis('Equals')
    plt.savefig('pie.png')
    plt.close()
    
if __name__=="__main__":
    labels =['A','B','C']
    values=[10,40,200]
    bar_chart(labels,values)
    pie_chart(labels,values)