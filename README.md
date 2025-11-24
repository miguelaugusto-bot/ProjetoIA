<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![FastText](https://img.shields.io/badge/FastText-Support-blue?style=for-the-badge)

</div>

# Projeto de Inteligência Artificial (HelpDesk ChatIA)

**Membros:**  

| RA | Integrante | Papel principal |
|------------|----|------------------|
| 2225106566 | Christian Angelo | Documentação / Engenharia de Dados |
| 2225105349 | Denis Dias dos Santos | Documentação / Engenharia de Dados |
| 2225103506 | Miguel Augusto Stanichesqui Torres Nunes | Gerência / Documentação |
| 2225102755 | Nathan Moura Vieira | Apresentação / Modelagem de Dados |
| 2224104454 | Vinicius Amaral dos Santos | Avaliação & Gráficos / Engenharia de Dados |
| 2225102634 | Vinicius Barauna | Avaliação & Gráficos / Modelagem de Dados |

**Apresentação:**  
    Link para a apresentação do projeto de IA:  
    -  
    problema → dados → IA → execução ao vivo → resultados → conclusão.  

**Descrição:**  
A proposta do projeto é o desenvolvimento de uma Inteligência Artificial capaz de auxiliar empresas e startups em duvidas relacionadas a produtos de hospedagem, email e dominios, sanando as principais perguntas antes de qualquer atendimento helpdesk, como se fosse um pré atendimento para estabelecer possiveis soluções sem a necessidade de um atendente.  

**Decisões Técnicas:**  



---
# Como Instalar:

## Requisitos:
Para o projeto é necessario efetuar a instalação:  
**Versão do Python:** Requer Python 3.13.x ou superior. (versões anteriores funcionam, mas pode apresentar erros)  
**Ambiente Virtual:** (Opcional, mas recomendado como o google colab)  

## Criar o ambiente virtual
### Windows
```bash
    python -m venv .venv
    .venv\Scripts\activate
```

### Linux / Mac
```bash
    python3 -m venv .venv
    source .venv/bin/activate
```

### Instalar Dependências
```bash
    pip install -r requirements.txt
```
---
# Estrutura do Projeto:

```text
ProjetoIA_2025_Turma41/  
├── data/                  # Dados brutos e externos 
│   ├── dataset.csv        # Perguntas e Respostas para treino  
│   └── cc.pt.300.vec.gz   # Vetores do FastText (baixado pelo setup.py ou pelo treinamento-lstm.ipynb)  
│  
├── models/                # Artefatos treinados (O "Cérebro") 
│   ├── chatbot_lstm_final.keras  # O modelo de Deep Learning salvo  
│   ├── tokenizer.pkl      # Dicionário de palavras  
│   └── label_encoder.pkl  # Tradutor de respostas (IDs -> Texto)  
│  
├── notebooks/             # Área de Experimentação (Jupyter) 
│   ├── treinamento-lstm.ipynb  # Notebook principal de treino  
│   └── exploracao.ipynb        # Notebook para testes manuais rápidos  
│  
├── reports/               # Métricas e Evidências do Treino
│   ├── grafico_acuracia_perca.png          # Mostra que a IA aprendeu (Loss caindo)  
│   ├── balanceamento_classes.png           # Distribuição das perguntas por tema  
│   ├── matriz_confusao.png                 # Onde a IA acertou vs. onde errou  
│   └── balanceamento_de_classes.png        # Precisão detalhada por assunto  
│  
├── src/                   # Código Fonte (Produção)
│   └── bot.py             # Lógica limpa do Chatbot para importação  
│  
├── tests/                 # Testes Automatizados
│   └── test_intencoes.py  # Script de teste (pytest)  
│  
├── requirements.txt       # Lista de bibliotecas necessárias  
├── setup.py               # Script para baixar o FastText e configurar pastas  
└── README.md              # Documentação do projeto  
```
---

# Dados Utilizados

---

# Resultados

**Balanceamento de Classes:**  
<img src="reports/balanceamento_de_classes.png" width="800px">

**Distribuição de Frases:**  
<img src="reports/distribuicao_de_frases.png" width="800px">

**Acurácia e Perca:**  
<img src="reports/grafico_acuracia_perca.png" width="800px">

**Matriz de Confusão:**  
<img src="reports/matriz_confusao.png" width="800px">

---

