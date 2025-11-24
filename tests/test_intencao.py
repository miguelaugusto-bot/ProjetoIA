import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.bot import resposta

#pytest
cenarios_de_teste = [
    
    # Teste de Iniciação
    ("oi tudo bem", "Oi! Tudo bem?"), 
    ("bom dia", "Oi! Tudo bem?"),
    
    # Teste Técnico
    ("por que meu site aparece como não seguro?", "Para o caso do site estar apresentando insegurança indico seguir essa wiki: https://www.locaweb.com.br/ajuda/wiki/site-nao-seguro-como-resolver/"),
    ("o que significa o Erro 500?", "Sobre o erro 500: https://www.locaweb.com.br/ajuda/wiki/erro-500"),
    ("Como usar o Instalador de Aplicativos para por o WordPress?", "Como instalar o wordpress: https://www.locaweb.com.br/ajuda/wiki/"),
    
    # Teste de Variações 
    ("Instalar WP.", "Como instalar o wordpress: https://www.locaweb.com.br/ajuda/wiki/instalacao-facil-e-pratica-de-wordpress-hospedagem-de-sites/"), 
    
    # Teste de Segurança (mais para falhas)
    ("receita de bolo de cenoura", "INDECISO"),
    ("sdjkfhsdjvsdkfh", "não entendi") 
]

@pytest.mark.parametrize("pergunta, trecho_esperado", cenarios_de_teste)
def testar_chatbot(pergunta, trecho_esperado):
    """
    Este teste roda automaticamente para cada par na lista acima.
    """
    print(f"\nTestando: '{pergunta}'")
    
    resposta_bot = resposta(pergunta)
    
    # Verifica se o trecho esperado está dentro da resposta do bot
    assert trecho_esperado.lower() in resposta_bot.lower(), \
        f"FALHOU! Pergunta: '{pergunta}' | Esperado: '{trecho_esperado}' | Veio: '{resposta_bot}'"