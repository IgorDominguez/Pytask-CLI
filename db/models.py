from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

db = create_engine("sqlite:///db/tasks.db")
Base = declarative_base()
Session = sessionmaker(db)

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())