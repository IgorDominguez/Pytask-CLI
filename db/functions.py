from .models import Session, Task, Project, Base, db
from typing import Optional

def create_db():
    Base.metadata.create_all(db)

def add_task_db(title: str, content: str, project_id: Optional[int] = None):
    session = Session()

    try:
        if project_id is not None:
            project = session.query(Project).filter_by(project_id=project_id).first()
            
            if not project:
                return f"O Projeto com ID {project_id} não existe :("

        task = Task(titulo=title, conteudo=content, project_id=project_id)
        session.add(task)
        session.commit()

    except Exception as e:
        session.rollback()
        return f"Erro! {e}"

    finally:
        session.close()

def list_tasks():
    session = Session()

    try:
        tasks = []
        task = session.query(Task).all()
        for tarefa in task:
            tasks.append({
                "task_id": tarefa.task_id,
                "titulo": tarefa.titulo,
                "conteudo": tarefa.conteudo
            })

        return tasks

    except:
        session.rollback()
        return "Erro! Perdão"
    finally:
        session.close()

def list_unique_task(task_id: int):
    session = Session()

    try:
        task = session.query(Task).filter_by(task_id=task_id).first()
        return {
            "titulo": task.titulo,
            "conteudo": task.conteudo
        }
    
    except Exception as e:
        session.rollback()
        return e
    finally:
        session.close()

def add_project(name: str, dscpt: Optional[str] = None):
    session = Session()

    try:
        project = Project(name=name, description=dscpt)
        session.add(project)
        session.commit()

    except Exception as e:
        session.rollback()
        return e
    finally:
        session.close()

def list_project_unique(project_id: int):
    session = Session()

    try:
        tasks = []
        project = session.query(Project).filter_by(project_id=project_id).first()

        if not project:
            return None

        for tarefa in project.tasks:
            tasks.append({
                "project_id": tarefa.project_id,
                "task_id": tarefa.task_id,
                "titulo": tarefa.titulo,
                "conteudo": tarefa.conteudo
            })
        
        return tasks
    
    except Exception as e:
        session.rollback()
        return e
    finally:
        session.close()

def delete_task(task_id: int):
    session = Session()

    try:
        task = session.query(Task).filter_by(task_id=task_id).first()
        
        if task:
            session.delete(task)
            session.commit()
            return "deletado"
        else:
            return "error"

    except Exception as e:
        session.rollback()
        return e
    finally:
        session.close()