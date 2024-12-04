from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Hardware, Desktop, Laptop, Tablet, OutrosHardware, Periferico, Cadeira, Monitor, PenDrive, OutrosPeriferico
import logging

app = Flask(__name__, template_folder='../templates', static_folder='../static')



# Configura o caminho do banco de dados (ajuste se necessário)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../inventarioTi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa modificações de rastreamento (opcional)
# Inicializa a conexão do Flask com o banco de dados
db.init_app(app)
# Garantir que as tabelas sejam criadas ao iniciar a aplicação
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('menu.html')
@app.route('/inserirCategorias')
def inserirCategorias():
    return render_template('inserirCategorias.html')

logging.basicConfig(level=logging.DEBUG)

@app.route('/inserirHardware')
def inserirHardware():
    return render_template('inserirHardware.html')

@app.route('/inserirPeriferico')
def inserirPeriferico():
    return render_template('inserirPeriferico.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

@app.route('/listarHardware')
def listarHardware():
    return render_template('listarHardware.html')
@app.route('/listarPeriferico')
def listarPeriferico():
    return render_template('listarPeriferico.html')

@app.route('/inserirDesktop',methods=['GET','POST'])
def inserirDesktop():
    if request.method == 'POST':
        ram=request.form['ram']
        cpu=request.form['cpu']
        sistema_operacional=request.form['sistema_operacional']
        status=request.form['status']
        placa_video=request.form['placa_video']

        novo_hardware = Hardware(ram=ram, cpu=cpu, sistema_operacional=sistema_operacional, status=status)
        db.session.add(novo_hardware)
        db.session.commit()

        # Cria o Desktop relacionado
        novo_desktop = Desktop(id_hardware=novo_hardware.id_patrimonio, placa_video=placa_video)
        db.session.add(novo_desktop)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirDesktop.html')

@app.route('/listarDesktop')
def listarDesktop():
    desktops = Desktop.query.all()
    return render_template('listarDesktop.html', desktops=desktops)

@app.route('/inserirLaptop', methods=['GET', 'POST'])
def inserirLaptop():
    if request.method == 'POST':
        ram = request.form['ram']
        cpu = request.form['cpu']
        sistema_operacional = request.form['sistema_operacional']
        status = request.form['status']
        marca = request.form['marca']

        novo_hardware = Hardware(ram=ram, cpu=cpu, sistema_operacional=sistema_operacional, status=status)
        db.session.add(novo_hardware)
        db.session.commit()

        novo_laptop = Laptop(id_hardware=novo_hardware.id_patrimonio, marca=marca)
        db.session.add(novo_laptop)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirLaptop.html')

# Rota para listar Laptop
@app.route('/listarLaptop')
def listarLaptop():
    laptops = Laptop.query.all()
    return render_template('listarLaptop.html', laptops=laptops)


@app.route('/inserirTablet', methods=['GET', 'POST'])
def inserirTablet():
    if request.method == 'POST':
        ram = request.form['ram']
        cpu = request.form['cpu']
        sistema_operacional = request.form['sistema_operacional']
        status = request.form['status']
        marca = request.form['marca']

        novo_hardware = Hardware(ram=ram, cpu=cpu, sistema_operacional=sistema_operacional, status=status)
        db.session.add(novo_hardware)
        db.session.commit()

        novo_tablet = Tablet(id_hardware=novo_hardware.id_patrimonio, marca=marca)
        db.session.add(novo_tablet)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirTablet.html')

# Rota para listar Tablet
@app.route('/listarTablet')
def listarTablet():
    tablets = Tablet.query.all()
    return render_template('listarTablet.html', tablets=tablets)


@app.route('/inserirOutrosHardware', methods=['GET', 'POST'])
def inserir_outros_hardware():
    if request.method == 'POST':
        tipo = request.form['tipo']
        descricao = request.form['descricao']

        novo_outro_hardware = OutrosHardware(tipo=tipo, descricao=descricao)
        db.session.add(novo_outro_hardware)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirOutrosHardware.html')

# Rota para listar Outros Hardware
@app.route('/listarOutrosHardware')
def listarOutrosHardware():
    outros_hardwares = OutrosHardware.query.all()
    return render_template('listarOutrosHardware.html', outros_hardwares=outros_hardwares)

@app.route('/inserirCadeira', methods=['GET', 'POST'])
def inserirCadeira():
    if request.method == 'POST':
        modelo = request.form['modelo']
        marca = request.form['marca']
        status = request.form['status']

        novo_periferico = Periferico(marca=marca, status=status)
        db.session.add(novo_periferico)
        db.session.commit()

        nova_cadeira = Cadeira(id_periferico=novo_periferico.id_patrimonio, modelo=modelo)
        db.session.add(nova_cadeira)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirCadeira.html')

# Rota para listar Cadeiras
@app.route('/listarCadeira')
def listar_cadeira():
    cadeiras = Cadeira.query.all()
    return render_template('listarCadeira.html', cadeiras=cadeiras)


# Rota para inserir Monitor
@app.route('/inserirMonitor', methods=['GET', 'POST'])
def inserirMonitor():
    if request.method == 'POST':
        tipo_tela = request.form['tipo_tela']
        resolucao = request.form['resolucao']
        modelo = request.form['modelo']
        marca = request.form['marca']
        status = request.form['status']

        novo_periferico = Periferico(marca=marca,status=status)
        db.session.add(novo_periferico)
        db.session.commit()

        novo_monitor = Monitor(id_periferico=novo_periferico.id_patrimonio, tipo_tela=tipo_tela, resolucao=resolucao, modelo=modelo)
        db.session.add(novo_monitor)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirMonitor.html')

# Rota para listar Monitores
@app.route('/listarMonitor')
def listarMonitor():
    monitores = Monitor.query.all()
    return render_template('listarMonitor.html', monitores=monitores)

@app.route('/inserirPenDrive', methods=['GET', 'POST'])
def inserirPenDrive():
    if request.method == 'POST':
        capacidade = request.form['capacidade']
        marca = request.form['marca']
        status = request.form['status']

        novo_periferico = Periferico(marca=marca,status=status)
        db.session.add(novo_periferico)
        db.session.commit()

        novo_pen_drive = PenDrive(id_periferico=novo_periferico.id_patrimonio, capacidade=capacidade)
        db.session.add(novo_pen_drive)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirPenDrive.html')

# Rota para listar Pen Drives
@app.route('/listarPenDrive')
def listarPenDrive():
    pen_drives = PenDrive.query.all()
    return render_template('listarPenDrive.html', pen_drives=pen_drives)


# Rota para inserir Outros Periférico
@app.route('/inserirOutrosPerifericos', methods=['GET', 'POST'])
def inserirOutrosPerifericos():
    if request.method == 'POST':
        tipo = request.form['tipo']
        descricao = request.form['descricao']

        novo_outro_periferico = OutrosPeriferico(nome=tipo, descricao=descricao)
        db.session.add(novo_outro_periferico)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('inserirOutrosPerifericos.html')

# Rota para listar Outros Periféricos
@app.route('/listarOutrosPeriferico')
def listarOutrosPeriferico():
    outros_perifericos = OutrosPeriferico.query.all()
    return render_template('listarOutrosPeriferico.html', outros_perifericos=outros_perifericos)


@app.route('/removerLaptop/<int:id>', methods=['POST'])
def removerLaptop(id):
    laptop = Laptop.query.get(id)

    if laptop:
        hardware=laptop.hardware
        db.session.delete(laptop)  # Exclui o laptop
        db.session.delete(hardware)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarLaptop'))  # Redireciona para a página de listagem

@app.route('/removerTablet/<int:id>', methods=['POST'])
def removerTablet(id):
    tablet = Tablet.query.get(id)

    if tablet:
        hardware=tablet.hardware
        db.session.delete(tablet)  # Exclui o laptop
        db.session.delete(hardware)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarTablet'))  # Redireciona para a página de listagem


@app.route('/removerDesktop/<int:id>', methods=['POST'])
def removerDesktop(id):
    desktop = Desktop.query.get(id)

    if desktop:
        hardware=desktop.hardware
        db.session.delete(desktop)  # Exclui o laptop
        db.session.delete(hardware)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarDesktop'))  # Redireciona para a página de listagem


@app.route('/removerOutrosHardware/<int:id>', methods=['POST'])
def removerOutrosHardware(id):
    outrosHardware = OutrosHardware.query.get(id)

    if outrosHardware:
        db.session.delete(outrosHardware)
        db.session.commit()

    return redirect(url_for('listarOutrosHardware'))

#Remover Perifericos
#Remover Pendrive

@app.route('/removerPenDrive/<int:id>', methods=['POST'])
def removerPenDrive(id):
    pen_drive = PenDrive.query.get(id)

    if pen_drive:
        periferico=pen_drive.periferico
        db.session.delete(pen_drive)  # Exclui o laptop
        db.session.delete(periferico)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarPenDrive'))  # Redireciona para a página de listagem

#Remover Monitor
@app.route('/removerMonitor/<int:id>', methods=['POST'])
def removerMonitor(id):
    monitor = Monitor.query.get(id)

    if monitor:
        periferico=monitor.periferico
        db.session.delete(monitor)  # Exclui o laptop
        db.session.delete(periferico)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarMonitor'))  # Redireciona para a página de listagem

#Remover Cadeira
@app.route('/removerCadeira/<int:id>', methods=['POST'])
def removerCadeira(id):
    cadeira = Cadeira.query.get(id)

    if cadeira:
        periferico=cadeira.periferico
        db.session.delete(cadeira)  # Exclui o laptop
        db.session.delete(periferico)  # Remove o hardware
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listar_cadeira'))  # Redireciona para a página de listagem

#Remover Outros Perifericos
@app.route('/removerOutrosPerifericos/<int:id>', methods=['POST'])
def removerOutrosPerifericos(id):
    outro_periferico = OutrosPeriferico.query.get(id)

    if outro_periferico:
        db.session.delete(outro_periferico)  # Exclui o laptop
        db.session.commit()  # Confirma as exclusões
        # Confirma a exclusão

    return redirect(url_for('listarOutrosPeriferico'))  # Redireciona para a página de listagem
# Roda a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)


