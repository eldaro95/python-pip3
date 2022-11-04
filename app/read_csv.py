import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader=csv.reader(csvfile,delimeter=',')
        header=next(reader)
        data=[]
    for row in reader:
        iterable =zip(header,row)
        mobdur={key:value for key, value in iterable}
        data.append(mobdur)
    return data

if __name__=='__main__'
    data = read_csv('./app/sample.csv')
    print(data[0])