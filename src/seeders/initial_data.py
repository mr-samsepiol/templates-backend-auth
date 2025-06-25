from src.main import app
from src.models import db, User, Company
import click

from werkzeug.security import generate_password_hash

def initial_data():
    with app.app_context():
        click.echo("✏ Escribiendo datos iniciales...")

        click.echo("🗑 Limpiando datos anteriores...")
        User.query.delete()
        Company.query.delete()
        db.session.commit()

        click.echo("🏢 Creando compañías: APP")
        def create_company(name, rfc, industry, address, phone, contact_person):
            return Company(
                name=name,
                rfc=rfc,
                industry=industry,
                address=address,
                phone=phone,
                contact_person=contact_person
            )

        APP = create_company("APP", "APP150515", "IT", "456 APP St, Mexico City", "555-5678", "Jane Doe")
        db.session.add_all([APP])
        db.session.flush()

        click.echo("👥 Creando usuarios")
        def create_user(username, email, company_id):
            return User(
                username=username,
                email=email,
                password=generate_password_hash("123456"),
                company_id=company_id
            )

        jhondoe = create_user("jhondoe", "jhondoe@domain.example", APP.id)
        janedoe = create_user("janedoe", "janedoe@domain.example", APP.id)
        db.session.add_all([jhondoe, janedoe])
        db.session.flush()

        db.session.commit()
        click.echo("✅ Datos iniciales escritos correctamente.")
