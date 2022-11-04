import read_csv as rc
from collections import Counter

def fmin(campo,num,data):
  result= list(filter(lambda item: float(item[campo])>=num, data))
  return result

def feq(campo,num,data):
  result= list(filter(lambda item: float(item[campo])==num, data))
  return result

def count(campo,data):
    base=list(map(lambda x:x[campo], data))
    fields = Counter(list(base))
    labels=sorted(fields.keys())
    values=fields.values()
    return labels, values
    

if __name__ == '__main__':
  a = fmin(12,rc.read_csv('sample.csv'))
  f= 'Participant Age'
  l1,l2=count(f,a)
  print (l1,l2)
  
  