from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

db_engine = create_engine('sqlite:///base_tarefas.db', echo=True)
Session = sessionmaker(bind=db_engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    status = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="tasks")

Base.metadata.create_all(db_engine)

def create_user(name, email):
    new_user = User(name=name, email=email)
    with Session() as session:
        session.add(new_user)
        session.commit()
    return new_user

def read_users():
    with Session() as session:
        users = session.query(User).all()
    return users

def read_user_by_name(name):
    with Session() as session:
        user = session.query(User).filter_by(name=name).first()
    return user

def update_user(user_id, new_name=None, new_email=None):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            if new_name:
                user.name = new_name
            if new_email:
                user.email = new_email
            session.commit()
    return user

def delete_user(user_id):
    with Session() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
    return f"User {user_id} deleted"

def create_task(description, status, user_id):
    new_task = Task(description=description, status=status, user_id=user_id)
    with Session() as session:
        session.add(new_task)
        session.commit()
    return new_task

def read_tasks():
    with Session() as session:
        tasks = session.query(Task).all()
    return tasks

def update_task(task_id, new_description=None, new_status=None):
    with Session() as session:
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            if new_description:
                task.description = new_description
            if new_status:
                task.status = new_status
            session.commit()
    return task

def delete_task(task_id):
    with Session() as session:
        task = session.query(Task).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
    return f"Task {task_id} deleted"
