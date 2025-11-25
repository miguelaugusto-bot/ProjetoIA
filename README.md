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
***>Aviso:* Atualmente o projeto esta em estado de prototipo, com falhas e diversos erros, pois a base é inferior da esperada e ainda esta decorando ao invés de aprendendo.**

**Decisões Técnicas:**  
Nossa IA é um chatbot em LSTM para compreender e entender as duvidas do cliente independente da forma que indique, para trazer respostas pré-definidas pelo sistema interno afim de agilizar o processo de sondagem, retorno e possivel solução da pergunta ou problema apresentado relacionado a dominio, hospedagem e e-mail profissional na internet. Inicialmente as respostas também deveriam ser definidas com a IA de acordo com regras e uma base em portugues, contudo, se tornou complexo aplicar.  


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

### Configuração de Setup
```bash
    python setup.py
```

### Instalar Dependências
```bash
    pip install -r requirements.txt
```


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


# Dados Utilizados
 
 - **Origem**: Todos os dados utilizados dentro do banco de dados vieram da [registro.br](https://registro.br/ajuda/) e [Locaweb](https://www.locaweb.com.br/ajuda/)
 - **Esquema**: A base de dados é separada por duas colunas, sendo as perguntas(frases frequentes dos usuario) e respostas(retornos objetivos e diretos de acordo com a duvida indicada).
 - **Cuidados éticos/privacidade**: Não possuimos nenhum direito aos dados utilizados e isso é um projeto open-source intuitivo e educacional para a Uninove.


# Resultados

<div align="center">
<h2>Balanceamento de Classes:</h2>
    <img src="reports/balanceamento_de_classes.png" width="80%">
    <p><b> O intuito é verificar a quantidade de perguntas possuem a determinada resposta e distribuir da melhor forma a quantidade no momento da aprendizagem. </b></p>
    <br><br>

<h2>Distribuição de Frases:</h2>
    <img src="reports/distribuicao_de_frases.png" width="80%">
    <p><b> Verificar a quantidade de palavras possuem ao todo nas perguntas. </b></p>
    <br><br>

<h2>Acurácia e Perca:</h2>
    <img src="reports/grafico_acuracia_perca.png" width="80%">
    <p><b>São dois gráficos essenciais para a analise de aprendizagem da IA </b></p><br>
    <p><b>Acurácia: Tem o intuito de sondar a precisão da IA dentro do treino e suas validações </b></p>
    <p><b>Perca: Entender se a IA esta aprendendo durante o processo de treino (na situação aplicada, esta apenas decorando ainda)</b></p>
    <br><br>

<h2>Matriz de Confusão:</h2>  
    <img src="reports/matriz_confusao.png" wwidth="45%">
    <p><b>O gráfico de matrix de confusão é essencial para entender se a IA estava entendo a relação das perguntas e respostas (entretanto ainda permanece decorando)</b></p>
    <br><br>

<p>Ainda possui muitos residuos e ruidos a serem aplicados que precisam ser corrigidos e analisado, contudo, esse processo será uma feature</p>
</div>


# Créditos

**Autores:**  
Christian Angelo - 2225106566  
Denis Dias dos Santos - 2225105349  
Miguel Augusto Stanichesqui Torres Nunes - 2225103506  
Nathan Moura Vieira - 2225102755  
Vinicius Amaral dos Santos - 2224104454  
Vinicius Barauna - 2225102634  
