from . import db

from sqlalchemy.orm import relationship

from datetime import datetime

class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rfc = db.Column(db.String(13), unique=True, nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    contact_person = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relaciones
    users = relationship("User", back_populates="company")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rfc': self.rfc,
            'industry': self.industry,
            'address': self.address,
            'phone': self.phone,
            'contact_person': self.contact_person,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat()
        }