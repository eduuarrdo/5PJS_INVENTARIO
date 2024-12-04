from flask import request, render_template, redirect, url_for
import sqlite3

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    conn = sqlite3.connect('./inventarioTi.db')
    cursor = conn.cursor()

    # Tabela para armazenar dados de Hardware (comum a todos os tipos)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hardware (
        id_patrimonio INTEGER PRIMARY KEY AUTOINCREMENT,
        ram TEXT,
        cpu TEXT,
        sistema_operacional TEXT,
        status TEXT
    )''')

    # Tabelas específicas para cada tipo de Hardware
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS desktop (
        id_hardware INTEGER PRIMARY KEY,
        placa_video TEXT,
        FOREIGN KEY(id_hardware) REFERENCES hardware(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS laptop (
        id_hardware INTEGER PRIMARY KEY,
        marca TEXT,
        FOREIGN KEY(id_hardware) REFERENCES hardware(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tablet (
        id_hardware INTEGER INTEGER PRIMARY KEY,
        marca TEXT,
        FOREIGN KEY(id_hardware) REFERENCES hardware(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS outros_hardware (
        id_patrimonio INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        descricao TEXT
    )''')

    # Tabela para armazenar dados de Periféricos (comum a todos os tipos)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS periferico (
        id_patrimonio INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT,
        status TEXT
    )''')

    # Tabelas específicas para cada tipo de Periférico
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadeira (
        id_periferico INTEGER PRIMARY KEY,
        modelo TEXT,
        FOREIGN KEY(id_periferico) REFERENCES periferico(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monitor (
        id_periferico INTEGER PRIMARY KEY,
        tipo_tela TEXT,
        resolucao TEXT,
        modelo TEXT,
        FOREIGN KEY(id_periferico) REFERENCES periferico(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pen_drive (
        id_periferico INTEGER PRIMARY KEY,
        capacidade TEXT,
        FOREIGN KEY(id_periferico) REFERENCES periferico(id_patrimonio)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS outros_periferico (
        id_patrimonio INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        descricao TEXT
    )''')

    conn.commit()
    conn.close()


# Chame a função para criar as tabelas
criar_tabelas()


