from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe para Hardware
class Hardware(db.Model):
    __tablename__ = 'hardware'
    id_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ram = db.Column(db.String, nullable=True)
    cpu = db.Column(db.String, nullable=True)
    sistema_operacional = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=True)

    # Relacionamentos com as tabelas específicas
    desktop = db.relationship('Desktop', backref='hardware', uselist=False)
    laptop = db.relationship('Laptop', backref='hardware', uselist=False)
    tablet = db.relationship('Tablet', backref='hardware', uselist=False)

# Classe para Desktop
class Desktop(db.Model):
    __tablename__ = 'desktop'
    id_hardware = db.Column(db.Integer, db.ForeignKey('hardware.id_patrimonio'), primary_key=True)
    placa_video = db.Column(db.String, nullable=True)

# Classe para Laptop
class Laptop(db.Model):
    __tablename__ = 'laptop'
    id_hardware = db.Column(db.Integer, db.ForeignKey('hardware.id_patrimonio'), primary_key=True)
    marca = db.Column(db.String, nullable=True)

# Classe para Tablet
class Tablet(db.Model):
    __tablename__ = 'tablet'
    id_hardware = db.Column(db.Integer, db.ForeignKey('hardware.id_patrimonio'), primary_key=True)
    marca = db.Column(db.String, nullable=True)

# Classe para outros tipos de Hardwarere
class OutrosHardware(db.Model):
    __tablename__ = 'outros_hardware'
    id_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String, nullable=True)
    descricao = db.Column(db.String, nullable=True)

# Classe para Periférico
class Periferico(db.Model):
    __tablename__ = 'periferico'
    id_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String, nullable=True)
    status = db.Column(db.String, nullable=True)

    # Relacionamentos com dispositivos periféricos específicos
    cadeira = db.relationship('Cadeira', backref='periferico', uselist=False, cascade="all, delete")
    monitor = db.relationship('Monitor', backref='periferico', uselist=False, cascade="all, delete")
    pen_drive = db.relationship('PenDrive', backref='periferico', uselist=False, cascade="all, delete")

# Classe para Cadeira
class Cadeira(db.Model):
    __tablename__ = 'cadeira'
    id_periferico = db.Column(db.Integer, db.ForeignKey('periferico.id_patrimonio'), primary_key=True)
    modelo = db.Column(db.String, nullable=True)

# Classe para Monitor
class Monitor(db.Model):
    __tablename__ = 'monitor'
    id_periferico = db.Column(db.Integer, db.ForeignKey('periferico.id_patrimonio'), primary_key=True)
    tipo_tela = db.Column(db.String, nullable=True)
    resolucao = db.Column(db.String, nullable=True)
    modelo = db.Column(db.String, nullable=True)

# Classe para PenDrive
class PenDrive(db.Model):
    __tablename__ = 'pen_drive'
    id_periferico = db.Column(db.Integer, db.ForeignKey('periferico.id_patrimonio'), primary_key=True)
    capacidade = db.Column(db.String, nullable=True)

# Classe para outros Perifericos
class OutrosPeriferico(db.Model):
    __tablename__ = 'outros_periferico'
    id_patrimonio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String, nullable=True)
    descricao = db.Column(db.String, nullable=True)
    # Não há relação com a tabela 'periferico'
