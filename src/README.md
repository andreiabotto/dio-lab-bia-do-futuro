# 🤖 Vico - Assistente Financeiro Inteligente

O **Vico** é um agente de IA (chatbot) desenvolvido para atuar como um mentor financeiro personalizado. Ele utiliza o modelo Gemini para analisar o patrimônio, os objetivos e as transações recentes de um cliente, oferecendo insights proativos e recomendações de investimentos baseadas em perfil de risco.

## 🌟 Funcionalidades

- **Análise de Saúde Financeira:** Verifica se a reserva de emergência está adequada.
- **Monitoramento de Metas:** Calcula o progresso para objetivos específicos (ex: compra de carro, viagem).
- **Recomendações Inteligentes:** Sugere produtos financeiros do catálogo com base no perfil do usuário.
- **Alertas Proativos:** Identifica gastos excessivos que podem comprometer o planejamento.
- **Educação Financeira:** Explica termos técnicos de forma simples e acessível.

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **Google Gemini API:** Cérebro de inteligência artificial do agente.
- **Streamlit:** Interface de usuário rápida e interativa.
- **Pandas:** Manipulação de dados e transações.

## 🚀 Como instalar e rodar

Siga os passos abaixo para configurar o ambiente em sua máquina local:

### 1. Clonar o repositório
```bash
git clone [https://github.com/andreiabotto/dio-lab-bia-do-futuro](https://github.com/andreiabotto/dio-lab-bia-do-futuro)
cd dio-lab-bia-do-futuro
```

### 2. Configurar as credenciais

Adicione sua chave de API do Google Gemini:
``` 
GOOGLE_API_KEY = ""
client = genai.Client(api_key=GOOGLE_API_KEY)
```

### 3. Instalar dependências
Certifique-se de ter o pip atualizado e execute:
```
pip install -r requirements.txt
```

### 4. Rodar a aplicação
Para iniciar o servidor local e abrir a interface no seu navegador, utilize:

```
streamlit run app.py
```

### Dica de Estrutura de Arquivos
Para que o comando `pip install` e o `streamlit run` funcionem perfeitamente, garanta que sua pasta esteja organizada assim:

* `app.py` (O código principal com a interface Streamlit)
* `requirements.txt` (Lista de bibliotecas: `streamlit`, `google-generativeai`, `python-dotenv`)
* `README.md` (Este arquivo que acabei de gerar)