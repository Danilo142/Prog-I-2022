from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    # Relaciones
    qualifications = db.relationship('Qualification', back_populates="user", cascade="all, delete-orphan")
    poems = db.relationship('Poem', back_populates="user", cascade="all, delete-orphan")

    #Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')

    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)

    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f'<Name: {self.name}, email : {self.email}, role: {self.role}>'

    # Objeto a JSON
    def to_json(self):
        poems = [poem.to_json_short() for poem in self.poems]
        qualifications = [qualification.to_json() for qualification in self.qualifications]
        user_json = {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email,
            'role' : self.role,
            'poems' : poems,
            'qualifications' : qualifications,
            'num_poems': len(self.poems),
            'num_score': len(self.qualifications)
        }
        return user_json

    def to_json_short(self):
        user_json = {
            'id' : self.id,
            'name' : self.name,
            'email' : self.email
        }
        return user_json

    @staticmethod
    # JSON a objeto
    def from_json(user_json):
        id = user_json.get('id')
        name = user_json.get('name')
        email = user_json.get('email')
        password = user_json.get('password')
        role = user_json.get('role')
        return User(id=id, name=name, email=email, plain_password=password, role=role)
