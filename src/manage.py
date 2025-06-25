from src.main import app
from src.models import db
from flask_migrate import Migrate
import click

migrate = Migrate(app, db)

# Importar la función seed
from src.seeders import initial_data

@app.cli.command("seed")
def seed():
    """Sembrar datos iniciales en la base de datos."""
    click.echo("🚀 Ejecutando seed de datos iniciales...")
    initial_data()
    click.echo("💯 Ejecución de seed completada.")
