import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from db.functions import add_task_db, list_tasks, list_unique_task, delete_task, add_project
import pyfiglet

app = typer.Typer()
console = Console()

task_app = typer.Typer()
app.add_typer(task_app, name="task")

# pytask
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        title = pyfiglet.figlet_format("Pytask CLI", font="small")
        console.print(f"[bold blue]{title}[/bold blue]")
        console.print("[dim]v0.1.0[/dim]")
        console.print("[dim]by Igor Dominguez :)[/dim]\n")

        table = Table(show_header=True, header_style="bold blue", border_style="blue")
        table.add_column("comando", style="cyan")
        table.add_column("descrição")

        table.add_row("task add <nome da tarefa>", "Adiciona uma nova tarefa")
        table.add_row("task list", "Lista todas as tarefas")
        table.add_row("task view <id da tarefa>", "Mostra uma tarefa específica")
        table.add_row("task delete <id da tarefa>", "Deleta uma tarefa")
        table.add_row("task done <id da tarefa>", "Marca uma tarefa como concluída")
        table.add_row("project add <nome do projeto>", "Adiciona um novo projeto")
        table.add_row("project list", "Lista todos os projetos")

        console.print(table)

# ... task
@task_app.command("add")
def add_task():
    console.print(Panel("Adicionar uma Tarefa", style="bold blue"))

    title_task = Prompt.ask("Título da tarefa")
    content_task = Prompt.ask("Descrição (opcional)", default="", show_default=False)
    project_task = Prompt.ask("ID do projeto (opcional)", default="", show_default=False)

    project_id = int(project_task) if project_task else None

    result = add_task_db(title_task, content_task, project_id)

    if result is not None:
        console.print(Panel(f"{result}", style="bold red"))
        return

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

@task_app.command("delete")
def add_task(id: int):
    console.print(Panel("Excluir uma tarefa específica", style="bold blue"))

    task = delete_task(id)

    try:
        if task == "deletado":
            console.print(Panel(f"✓ Tarefa [bold]{id}[/bold] Foi excluída com sucesso!", style="bold green"))
        elif task == "error":
            console.print(Panel(f"Tarefa [bold]{id}[/bold] não existe :(", style="bold red"))
        
    except:
        console.print(Panel("Esta tarefa ainda não foi criada :(", style="bold red"))

if __name__ == '__main__':
    app()