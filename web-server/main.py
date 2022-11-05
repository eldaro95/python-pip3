import store
from fastapi import FastAPI as fp
from fastapi.responses import HTMLResponse as web

#fastapi permite crear estructura para el servidor
#response html permite definir en formato HTML una pagina

#Para ejecutar se usa el comando: uvicorn main:app --reload

app = fp()

@app.get('/')
def getlist():
    return[1,2,3]

@app.get('/contact', response_class=web)
def getlist():
    return '''
    <h1> Hola perro </h1>
    <p> Primer parrafo </p>
'''

def run():
    store.get_cat()
    
    
if __name__=='__main__':
    run()