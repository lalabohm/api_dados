from crud.crud_main import insert_dados, ler_dados, delete_user
from data_models.models import User, Task
from datetime import datetime
from fastapi import FastAPI
import uvicorn

app = FastAPI()

user1 = User(
             name = "pedro",
             email = "pedro@idp.edu.br",
             created = datetime.now()
             )

task1 = Task(
            created = datetime.now(),
            updated = datetime.now(),
            task = 'Estudar FastAPI',
            priority = 'Alta',
            status = 'Iniciado',
            userid = 1
            )

#insert_dados(user1)
#insert_dados(task1)

@app.get('/primeiro_endpoint')
def meu_primeiro_endpoint():
    return 'Olá IDP, bora desenvolver na WEB!'

@app.get('/leitura_tabela')
def ler_tabela(entidade:int):
    print(entidade, type(entidade))
    if entidade == 1:
        tabela = User
    if entidade == 2:
        tabela = Task
    return ler_dados(tabela)

@app.post('/insert_user')
def inserir_user(nome_in:str,email_in:str):
    usuario = User(name=nome_in,email=email_in,created=datetime.now())
    insert_dados(usuario)
    return ler_dados(User)

@app.post('/insert_task')
def inserir_task(task_in:str,priority_in:str,status_in:str,uid_in:int):
    tarefa = Task(created=datetime.now(),updated=datetime.now(),task=task_in,priority=priority_in,status=status_in,userid=uid_in)
    insert_dados(tarefa)
    return ler_dados(Task)

@app.delete('/del_user')
def delete_user_id(id:int):
    return delete_user(id,User)
    

@app.put('/update_user')
def update_user_id():
    return 'TODO'


uvicorn.run(app,host='0.0.0.0',port=8888)