from datetime import date, timedelta
import random
import sys
import os

# Agregar el directorio padre al path para poder importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models import db
from models.user import *
from main import app

def seed_database():
    """Poblar la base de datos con datos de prueba"""

    # Limpiar datos existentes
    db.drop_all()
    db.create_all()

    # Crear productos de seguros
    products = [
        {
            'name': 'Seguro de Vida Básico',
            'category': 'vida',
            'description': 'Cobertura básica de vida para empleados',
            'coverage_details': {
                'muerte_natural': 500000,
                'muerte_accidental': 1000000,
                'invalidez_total': 500000
            },
            'base_price': 150,
            'min_age': 18,
            'max_age': 65
        },
        {
            'name': 'Seguro de Gastos Médicos Mayores',
            'category': 'salud',
            'description': 'Cobertura médica completa',
            'coverage_details': {
                'hospitalizacion': 2000000,
                'consultas': 50000,
                'medicamentos': 100000
            },
            'base_price': 300,
            'min_age': 0,
            'max_age': 80
        },
        {
            'name': 'Seguro Dental',
            'category': 'salud',
            'description': 'Cobertura dental preventiva y correctiva',
            'coverage_details': {
                'limpieza': 2000,
                'curaciones': 5000,
                'ortodoncia': 50000
            },
            'base_price': 80,
            'min_age': 0,
            'max_age': 99
        },
        {
            'name': 'Seguro de Accidentes Personales',
            'category': 'accidentes',
            'description': 'Protección contra accidentes',
            'coverage_details': {
                'muerte_accidental': 300000,
                'invalidez_permanente': 300000,
                'gastos_medicos': 50000
            },
            'base_price': 100,
            'min_age': 18,
            'max_age': 70
        }
    ]

    for product_data in products:
        product = InsuranceProduct(**product_data)
        db.session.add(product)

    # Crear recompensas
    rewards = [
        {
            'name': 'Tarjeta de Regalo Amazon $500',
            'description': 'Tarjeta de regalo para compras en Amazon',
            'points_required': 1000,
            'category': 'tarjetas_regalo',
            'stock': 50
        },
        {
            'name': 'Día Libre Adicional',
            'description': 'Un día libre adicional para disfrutar',
            'points_required': 800,
            'category': 'tiempo_libre',
            'stock': 100
        },
        {
            'name': 'Voucher Restaurante $300',
            'description': 'Voucher para cena en restaurantes participantes',
            'points_required': 600,
            'category': 'gastronomia',
            'stock': 30
        },
        {
            'name': 'Audífonos Bluetooth',
            'description': 'Audífonos inalámbricos de alta calidad',
            'points_required': 1200,
            'category': 'tecnologia',
            'stock': 20
        },
        {
            'name': 'Curso Online Udemy',
            'description': 'Acceso a curso de desarrollo profesional',
            'points_required': 400,
            'category': 'educacion',
            'stock': 100
        }
    ]

    for reward_data in rewards:
        reward = Reward(**reward_data)
        db.session.add(reward)

    # Crear recursos educativos
    resources = [
        {
            'title': 'Importancia del Seguro de Vida',
            'description': 'Conoce por qué es fundamental tener un seguro de vida',
            'content': 'El seguro de vida es una herramienta financiera que...',
            'resource_type': 'article',
            'category': 'seguros_vida',
            'points_reward': 50
        },
        {
            'title': 'Cómo Elegir tu Seguro de Salud',
            'description': 'Guía completa para seleccionar el mejor seguro médico',
            'content': 'Al elegir un seguro de salud, debes considerar...',
            'resource_type': 'article',
            'category': 'seguros_salud',
            'points_reward': 50
        },
        {
            'title': 'Video: Beneficios Laborales en México',
            'description': 'Video explicativo sobre beneficios laborales',
            'resource_type': 'video',
            'category': 'beneficios',
            'url': 'https://www.youtube.com/watch?v=example',
            'points_reward': 75
        },
        {
            'title': 'Quiz: Conocimientos Básicos de Seguros',
            'description': 'Pon a prueba tus conocimientos sobre seguros',
            'resource_type': 'quiz',
            'category': 'evaluacion',
            'points_reward': 100
        }
    ]

    for resource_data in resources:
        resource = EducationalResource(**resource_data)
        db.session.add(resource)

    # Crear empresa de prueba
    company_user = User(
        email='admin@techcorp.com',
        user_type=UserType.COMPANY
    )
    company_user.set_password('admin123')
    db.session.add(company_user)
    db.session.flush()

    company = Company(
        user_id=company_user.id,
        name='TechCorp Solutions',
        rfc='TCH890123456',
        industry='tecnologia',
        size='mediana',
        address='Av. Reforma 123, CDMX',
        phone='55-1234-5678',
        contact_person='Ana Rodríguez'
    )
    db.session.add(company)
    db.session.flush()

    # Crear empleados de prueba
    employees_data = [
        {
            'email': 'maria.gonzalez@techcorp.com',
            'employee_id': 'EMP001',
            'first_name': 'María',
            'last_name': 'González',
            'position': 'Desarrolladora Senior',
            'department': 'Tecnología',
            'points': 850
        },
        {
            'email': 'carlos.lopez@techcorp.com',
            'employee_id': 'EMP002',
            'first_name': 'Carlos',
            'last_name': 'López',
            'position': 'Gerente de Ventas',
            'department': 'Ventas',
            'points': 1200
        },
        {
            'email': 'ana.martinez@techcorp.com',
            'employee_id': 'EMP003',
            'first_name': 'Ana',
            'last_name': 'Martínez',
            'position': 'Diseñadora UX',
            'department': 'Diseño',
            'points': 650
        }
    ]

    for emp_data in employees_data:
        emp_user = User(
            email=emp_data['email'],
            user_type=UserType.EMPLOYEE
        )
        emp_user.set_password('password123')
        db.session.add(emp_user)
        db.session.flush()

        employee = Employee(
            user_id=emp_user.id,
            company_id=company.id,
            employee_id=emp_data['employee_id'],
            first_name=emp_data['first_name'],
            last_name=emp_data['last_name'],
            position=emp_data['position'],
            department=emp_data['department'],
            points=emp_data['points'],
            hire_date=date.today() - timedelta(days=random.randint(100, 1000)),
            birth_date=date(1985 + random.randint(0, 15), random.randint(1, 12), random.randint(1, 28))
        )
        db.session.add(employee)

    db.session.commit()
    print("✅ Base de datos poblada con datos de prueba")

if __name__ == '__main__':
    with app.app_context():
        seed_database()