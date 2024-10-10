from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_engine = create_engine('sqlite:///base_tarefas.db', echo=True)

Session = sessionmaker(bind=db_engine)

# CREATE
def insert_dados(dados):
    with Session() as session:
        session.add(dados)
        session.commit()

# READ
def ler_dados(tabela):
    with Session() as session:
        registros = session.query(tabela).all()
    return registros

# UPDATE
def update_dados(tabela):
    return 'TODO'

# DELETE
def delete_user(id_in,model):
    print(id_in,model)
    with Session() as session:
        registros_deletado = session.query(model).filter_by(id=id_in).first()
        session.delete(registros_deletado)
        session.commit()
    return 'Registro deletado com sucesso!'
