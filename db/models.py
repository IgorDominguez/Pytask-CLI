from sqlalchemy import create_engine, Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Relationship
from datetime import datetime

db = create_engine("sqlite:///db/tasks.db")
Base = declarative_base()
Session = sessionmaker(db)

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())

class Task(Base):
    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=True)
    finalizada = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())

    project = Relationship('Project', backref='tasks', lazy='subquery')