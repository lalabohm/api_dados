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
def update_dados(id_in, model, novos_dados):
    with Session() as session:
        registro = session.query(model).filter_by(id=id_in).first()
        if registro:
            for key, value in novos_dados.items():
                setattr(registro, key, value) 
            session.commit()
            return 'Registro atualizado com sucesso!'
        else:
            return 'Registro não encontrado.'

# DELETE
def delete_user(id_in, model):
    with Session() as session:
        registro_deletado = session.query(model).filter_by(id=id_in).first()
        if registro_deletado:
            session.delete(registro_deletado)
            session.commit()
            return 'Registro deletado com sucesso!'
        else:
            return 'Registro não encontrado.'
