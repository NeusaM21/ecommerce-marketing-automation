"""
Módulo: whatsapp_bot.py
Descrição: Simula envio de mensagem no WhatsApp via API (ex: Twilio).
Este exemplo é simplificado apenas para fins de demonstração.
"""

def enviar_mensagem(numero, mensagem):
    """
    Simula envio de mensagem via WhatsApp.
    
    Parâmetros:
        numero (str): Número de telefone do cliente com código do país (ex: +5511999999999)
        mensagem (str): Texto da mensagem a ser enviada
    """
    print(f"[SIMULADO] Enviando mensagem para {numero} via WhatsApp:")
    print(f">>> {mensagem}")