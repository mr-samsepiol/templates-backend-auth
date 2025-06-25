from flask_jwt_extended import get_jwt, jwt_required
from src.core.blacklist import blacklist
from src.models import db, User

from flask import jsonify

def user_register(data):
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'error': f'El usuario {data.get("email")} ya existe.'}), 401
    
    user = User(
        name=data.get('name'),
        email=data.get('email'),
        profile_id=data.get('profile_id'),
        company_id=data.get('company_id') 
    )
    user.set_password(data.get('password'))

    db.session.add(user)
    db.session.commit()

    if not user.id:
        return jsonify({'error': 'Error al crear el usuario.'}), 500
    
    access_token = user.create_access_token()

    if not access_token:
        return jsonify({'error': 'Error al generar el token de acceso.'}), 500
    
    return jsonify({
            'message': 'Bienvenido',
            'user': user.to_dict(),
            'token': access_token
        }), 201

def user_login(email, password):
    try:
        user = User.query.filter((User.email == email) | (User.username == email)).first()
        if not user:
            return jsonify({'error': f'El usuario {email} no existe.'}), 404
        if not user.check_password(password):
            return jsonify({'error': f'Credenciales inválidas.'}), 401
        
        access_token = user.create_access_token()

        if not access_token:
            return jsonify({'error': 'Error al generar el token de acceso.'}), 500
        
        return jsonify({
            'message': 'Bienvenido',
            'data': {
                **user.to_dict(),
                'token': access_token
            }
        }), 200
        
    except Exception as e:
        print(f"Error en login: {str(e)}")
        return jsonify({'error': 'Error interno del servidor.'}), 500

@jwt_required()
def user_logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({
        "message": "Sesión cerrada exitosamente",
        "data": None
    }), 200