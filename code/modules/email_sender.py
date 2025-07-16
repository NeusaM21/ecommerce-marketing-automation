"""
Módulo: email_sender.py
Descrição: Contém funções responsáveis por enviar e-mails automáticos de recuperação de carrinho e pós-venda.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(destinatario, assunto, corpo):
    """
    Envia um e-mail simples.
    Parâmetros:
        destinatario (str): E-mail do cliente.
        assunto (str): Assunto do e-mail.
        corpo (str): Corpo da mensagem.
    """
    # Exemplo de estrutura (dados reais devem ser armazenados em .env)
    remetente = "sua_loja@email.com"
    senha = "sua_senha"
    
    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = assunto
    msg.attach(MIMEText(corpo, "plain"))
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")