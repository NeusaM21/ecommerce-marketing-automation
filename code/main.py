"""
main.py
Descrição: Arquivo principal para orquestrar a automação de e-mails e mensagens para e-commerce.
"""

from modules.email_sender import send_email
from modules.whatsapp_bot import enviar_mensagem
from modules.lead_scoring import score_lead

# Simulação de dados fictícios (exemplo real pode ser carregado via CSV/Excel)
clientes = [
    {
        "nome": "Clara Souza",
        "email": "clara@email.com",
        "telefone": "+5511999990001",
        "abandonou_carrinho": True,
        "visitou_3x": True,
        "comprou_antes": False
    },
    {
        "nome": "Carlos Lima",
        "email": "carlos@email.com",
        "telefone": "+5511988880002",
        "abandonou_carrinho": False,
        "visitou_3x": True,
        "comprou_antes": True
    }
]

# Execução principal
for cliente in clientes:
    score = score_lead(cliente)
    
    print(f"\nCliente: {cliente['nome']}")
    print(f"Score: {score}")

    if score >= 15:
        mensagem = f"Olá {cliente['nome']}, ainda está de olho no seu carrinho? Temos uma oferta exclusiva pra você!"
        
        # Simula envio por WhatsApp
        enviar_mensagem(cliente["telefone"], mensagem)
        
        # Envia e-mail real
        send_email(cliente["email"], "🛒 Sua oferta exclusiva está aqui!", mensagem)