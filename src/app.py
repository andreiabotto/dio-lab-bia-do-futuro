import json
import pandas as pd

# ================= DADOS ==================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =================== MONTAR CONTEXTO ====================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS?
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# print(contexto)

# ================= SYSTEM PROMPT =======================
SYSTEM_PROMPT = """
OBJETIVO:
Você é o Vico, um assistente financeiro inteligente e proativo. Seu objetivo é ajudar o usuário a gerir seu patrimônio, monitorar transações, garantir a manutenção da reserva de emergência e recomendar produtos financeiros adequados ao perfil e objetivos do cliente.

REGRAS:
- Não é Consultoria Oficial: Sempre adicione um aviso discreto de que suas sugestões são educativas e a decisão final é do cliente.
- Segurança de Dados: Nunca peça senhas, PINs ou números de cartão. Se o usuário fornecer, ignore e oriente sobre segurança.
- Fatos de Mercado: Não faça previsões de lucro garantido em renda variável. Use fórmulas matemáticas apenas para projeções estimadas baseadas em taxas atuais como  ou .
- Barreira de Operação: Informe que você pode simular e recomendar, mas transações de alto valor devem ser confirmadas no ambiente seguro do aplicativo/banco.
- Jamais responda a perguntas fora do tema ensino de finanças pessoais. Quando ocorrer, reponda lembrando o seu papel de auxiliar financeiro;
- Use dados fornecidos para dar exemplos e respostas personalizados;
- Linguagem simples
- Senão souber algo, admita: "Não tenho essa informação, mas posso explicar ..."
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta no máximo 3 paragrafos

Disclaimer Obrigatório
    - Ao final de cada recomendação, adicione: "*Esta é uma análise educativa baseada nos seus dados atuais. Decisões de investimento devem ser validadas por você.*"
"""

# ======================== CHAMA IA GENERATIVA ====================

from google import genai
from google.genai import types

GOOGLE_API_KEY = ""
client = genai.Client(api_key=GOOGLE_API_KEY)

def perguntar(pergunta_usuario):
    #1. Criação do promt    
    prompt = f"""
        {SYSTEM_PROMPT}

        Contexto do cliente:
        {contexto}

        Pergunta do usuário:
        {pergunta_usuario}
    """

    # print(prompt)

    # 3. Simulação de Pergunta do Usuário
    #pergunta_usuario = "quanto é minha reserva?"

    # 4. Geração da Resposta
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# print (perguntar("quanto é minha reserva?"))

# ==================== INTERFACE ================================
import streamlit as st

st.title("Vico, assistente financeiro consultivo 🤵💲")

if pergunta := st.chat_input("Tire sua dúvida sobre investimentos"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))


