import sqlite3
import requests
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


EMAIL_REMETENTE = "matheuscaio827@gmail.com"
EMAIL_DESTINATARIO = "matheuscaio827@gmail.com"
SENHA_APP = "oezx aqmd rnxb yqmw"
NOME_BD = "projeto_rpa.db"


url = "https://api.adviceslip.com/advice"
response = requests.get(url)
data = response.json()
conselho = data["slip"]["advice"]


conn = sqlite3.connect(NOME_BD)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS conselhos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT
    )
''')
cursor.execute("INSERT INTO conselhos (texto) VALUES (?)", (conselho,))
conn.commit()

palavras = re.findall(r'\b\w{6,}\b', conselho)
resultado_processado = ', '.join(palavras)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_processados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original TEXT,
        palavras_extraidas TEXT
    )
''')
cursor.execute("INSERT INTO dados_processados (original, palavras_extraidas) VALUES (?, ?)", (conselho, resultado_processado))
conn.commit()
conn.close()


mensagem_email = MIMEMultipart()
mensagem_email["From"] = EMAIL_REMETENTE
mensagem_email["To"] = EMAIL_DESTINATARIO
mensagem_email["Subject"] = "Resumo do Projeto RPA - Caio Matheus Caetano Silva"

texto_email = f"""
Oi, professor(a)!

Esse é o resumo do meu projeto final da disciplina de RPA utilizando Python:

- Conselho coletado da API:
  "{conselho}"

- Palavras com 6 ou mais letras extraídas com regex:
  {resultado_processado}

O banco de dados 'projeto_rpa.db' foi criado e atualizado com sucesso.

Atenciosamente,  
Caio Matheus Caetano Silva
"""
mensagem_email.attach(MIMEText(texto_email, "plain"))


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
    servidor.login(EMAIL_REMETENTE, SENHA_APP)
    servidor.send_message(mensagem_email)

print("✅ Projeto executado com sucesso! Relatório enviado por e-mail.")
