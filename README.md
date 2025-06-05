# Projeto Final - RPA com Python

**Aluno:** Caio Matheus Caetano Silva  
**Curso:** Faculdade Impacta  
**Disciplina:** Robotic Process Automation (RPA)  
**Data:** Junho/2025

---

## 🧠 Descrição do Projeto

Este projeto é o trabalho final da disciplina de RPA. Ele utiliza a linguagem Python para realizar uma automação que envolve:

- Coleta de dados de uma API pública
- Armazenamento em banco de dados SQLite
- Processamento com expressões regulares (regex)
- Envio automatizado de um relatório por e-mail

---

## 🌐 API Utilizada

**API:** [Advice Slip API](https://api.adviceslip.com/)

### ✅ Justificativa:

Escolhi a Advice Slip por ser simples, gratuita e retornar mensagens de texto fáceis de trabalhar com regex. Isso permite focar nas etapas de automação, banco de dados e envio de e-mail.

---

## 🔧 Etapas do Projeto

1. **Coleta de Dados**
   - Utilizei a biblioteca `requests` para obter conselhos aleatórios da API.

2. **Armazenamento**
   - Criei o banco `projeto_rpa.db` com SQLite.
   - Tabela 1: `conselhos` (armazenamento do conselho original)
   - Tabela 2: `dados_processados` (armazenamento das palavras extraídas via regex)

3. **Processamento**
   - Através da biblioteca `re`, extraí palavras com 6 ou mais letras do conselho recebido.

4. **Envio de E-mail**
   - Automatizei o envio do e-mail usando `smtplib` com senha de aplicativo do Gmail.
   - O e-mail contém o conselho original e as palavras processadas.

---

## 🧪 Resultado Final

Ao executar o script Python:

- Um conselho aleatório é obtido da API
- As informações são salvas no banco de dados
- Palavras com 6 ou mais letras são extraídas e armazenadas
- Um e-mail automático é enviado com um resumo do projeto

---

## ✅ Conclusão

O projeto foi finalizado com sucesso, atendendo a todos os requisitos propostos na atividade prática.  
Tive uma pequena dificuldade ao configurar o envio de e-mail via Gmail, que exigiu ativar a verificação em duas etapas e gerar uma senha de app.  
No geral, foi uma boa oportunidade para aplicar conhecimentos de integração de APIs, banco de dados, regex e automação com Python.

---

## 📁 Arquivos incluídos

- `projeto_rpa.py` — Código Python completo
- `projeto_rpa.db` — Banco de dados SQLite com os dados coletados e processados
- `README.md` — Este arquivo explicativo

---
