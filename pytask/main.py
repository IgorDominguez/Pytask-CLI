import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from db.functions import add_task_db, list_tasks, list_unique_task

app = typer.Typer()
console = Console()

task_app = typer.Typer()
app.add_typer(task_app, name="task")

# ... task
@task_app.command("add")
def add_task():
    console.print(Panel("Adicionar uma Tarefa", style="bold blue"))

    title_task = Prompt.ask("Título da tarefa")
    content_task = Prompt.ask("Descrição (opcional)", default="", show_default=False)

    add_task_db(title_task, content_task)

    console.print(Panel(f"✓ Tarefa [bold]{title_task}[/bold] adicionada com sucesso!", style="bold blue"))

@task_app.command("list")
def add_task():
    console.print(Panel("Listar todas as tarefas", style="bold blue"))

    tasks = list_tasks()

    table = Table(border_style="blue")

    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Título", style="white")
    table.add_column("Descrição", style="dim")

    for task in tasks:
        table.add_row(
            str(task["task_id"]),
            task["titulo"],
            task["conteudo"] or "—"
        )

    console.print(table)

@task_app.command("view")
def add_task(id: int):
    console.print(Panel("Listar uma tarefa específica", style="bold blue"))

    task = list_unique_task(id)

    try:
        table = Table(border_style="blue")

        table.add_column("Título", style="white")
        table.add_column("Descrição", style="dim")

        table.add_row(
            task["titulo"],
            task["conteudo"] or "—"
        )

        console.print(table)
    except:
        console.print(Panel("Esta tarefa ainda não foi criada :(", style="bold red"))

if __name__ == '__main__':
    app()