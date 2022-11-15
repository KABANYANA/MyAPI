from fastapi import FastAPI, Request
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')

@storage.get('/')
def index():
    return "This is my API"

@storage.get('/today')
def today():
    return "This is Natural Language Processing"

@storage.get('/mynames')
def names(First_name:bool = False, last_name:bool = False):
    full_names = ""
    if First_name:
        full_names += 'Joyeuse'
    if last_name:
        full_names += 'KABANYANA'
        
    return full_names

if __name__ == "__main__":
    storage.run
#if __name__=='__main__':
    #app.run()
    