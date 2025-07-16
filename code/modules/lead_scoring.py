"""
Módulo: lead_scoring.py
Descrição: Define uma função simples de pontuação de leads com base no comportamento.
"""

def score_lead(cliente):
    """
    Atribui uma pontuação a um cliente com base em critérios simulados.

    Parâmetros:
        cliente (dict): Dados do cliente simulados com campos como:
            - abandonou_carrinho (bool)
            - visitou_3x (bool)
            - comprou_antes (bool)

    Retorna:
        int: Pontuação do lead.
    """
    score = 0

    if cliente.get("abandonou_carrinho"):
        score += 10

    if cliente.get("visitou_3x"):
        score += 5

    if cliente.get("comprou_antes"):
        score += 20

    return score