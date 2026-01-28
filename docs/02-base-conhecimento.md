# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Descrição da base |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não houve modificações da base

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são utilizados para fornecer um contexto financeiro para IA e gerar respostas precisas ao usuário

```
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS?
{json.dumps(produtos, indent=2, ensure_ascii=False)}
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.


CLIENTE: João Silva, 32 anos, perfil moderado

OBJETIVO: Construir reserva de emergência

PATRIMÔNIO: R$ 15000.0 | RESERVA R$ 10000.0

TRANSAÇÕES RECENTES:
|      data|    descricao|   categoria|  valor|    tipo|
|----------|-------------|------------|-------|--------|
|2025-10-01|      Salário|     receita| 5000.0| entrada|
|2025-10-02|      Aluguel|     moradia| 1200.0|   saida|
|2025-10-03| Supermercado| alimentacao|  450.0|   saida|
|2025-10-05|      Netflix|       lazer|   55.9|   saida|
|2025-10-07|     Farmácia|       saude|   89.0|   saida|
|2025-10-10|  Restaurante| alimentacao|  120.0|   saida|
|2025-10-12|         Uber|  transporte|   45.0|   saida|
|2025-10-15| Conta de Luz|     moradia|  180.0|   saida|
|2025-10-20|     Academia|       saude|   99.0|   saida|
|2025-10-25|  Combustível|  transporte|  250.0|   saida|

ATENDIMENTOS ANTERIORES:
|      data|    canal|                  tema|                                                           resumo| resolvido|
|----------|---------|----------------------|-----------------------------------------------------------------|----------|
|2025-09-15|     chat|                   CDB|                   Cliente perguntou sobre rentabilidade e prazos|       sim|
|2025-09-22| telefone|       Problema no app|                         Erro ao visualizar extrato foi corrigido|       sim|
|2025-10-01|     chat|         Tesouro Selic| Cliente pediu explicação sobre o funcionamento do Tesouro Direto|       sim|
|2025-10-12|     chat|     Metas financeiras|          Cliente acompanhou o progresso da reserva de emergência|       sim|
|2025-10-25|    email| Atualização cadastral|                              Cliente atualizou e-mail e telefone|       sim|

PRODUTOS DISPONÍVEIS?
```
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.0,
    "indicado_para": "Reserva de emergÃªncia e iniciantes"
  },
  {
    "nome": "CDB Liquidez DiÃ¡ria",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.0,
    "indicado_para": "Quem busca seguranÃ§a com rendimento diÃ¡rio"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.0,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.0,
    "indicado_para": "Perfil moderado que busca diversificaÃ§Ã£o"
  },
  {
    "nome": "Fundo de AÃ§Ãµes",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "VariÃ¡vel",
    "aporte_minimo": 100.0,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]
```
