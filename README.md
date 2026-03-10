# Personal Finance Analyzer

## Objetivo

O Personal Finance Analyzer é uma aplicação desenvolvida para auxiliar no registro, análise e visualização de dados financeiros pessoais. Seu principal objetivo é transformar transações financeiras brutas em informações úteis, permitindo uma tomada de decisão mais informada sobre suas finanças. A aplicação gera estatísticas financeiras detalhadas, gráficos intuitivos de gastos, insights automáticos e calcula a capacidade de investimento mensal do usuário.

## Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

*   **Linguagem Principal:** Python
*   **Bibliotecas:**
    *   **Pandas:** Para manipulação e análise eficiente de dados.
    *   **SQLite:** Como banco de dados leve para armazenamento das transações.
    *   **Matplotlib:** Para a geração de gráficos e visualizações de dados.
    *   **Streamlit:** Para a criação de uma interface web simples e interativa.

## Estrutura do Projeto

A estrutura de diretórios e arquivos do projeto é organizada da seguinte forma:

```
personal-finance-analyzer/
├── README.md
├── main.py
├── database.py
├── analysis.py
├── charts.py
├── investment_analysis.py
├── requirements.txt
└── data/
    └── transactions.db
```

*   `README.md`: Este arquivo, contendo a descrição do projeto, instruções e informações relevantes.
*   `main.py`: O arquivo principal da aplicação Streamlit, responsável pela interface do usuário e integração dos módulos.
*   `database.py`: Contém as funções para inicialização do banco de dados SQLite e operações de CRUD (Criar, Ler, Atualizar, Deletar) de transações.
*   `analysis.py`: Módulo responsável por calcular estatísticas financeiras e gerar insights automáticos.
*   `charts.py`: Contém as funções para a criação dos gráficos financeiros utilizando Matplotlib.
*   `investment_analysis.py`: Módulo dedicado ao cálculo da capacidade de investimento e recomendações.
*   `requirements.txt`: Lista as dependências Python necessárias para o projeto.
*   `data/`: Diretório para armazenar o arquivo do banco de dados `transactions.db`.

## Estrutura do Banco de Dados

O banco de dados `transactions.db` utiliza uma única tabela chamada `transactions` com a seguinte estrutura:

| Campo         | Descrição                               |
| :------------ | :-------------------------------------- |
| `id`          | Identificador único da transação        |
| `date`        | Data da transação (formato TEXT)        |
| `type`        | Tipo da transação (`income` ou `expense`) |
| `amount`      | Valor da transação (REAL)               |
| `category`    | Categoria da transação (e.g., `food`, `salary`, `rent`) |
| `description` | Descrição detalhada da transação        |
| `fixed_expense` | Indica se é uma despesa fixa (BOOLEAN) |

**Exemplo de Registros:**

```
1 | 2026-03-05 | expense | 45.90 | food | almoço | False
2 | 2026-03-06 | income | 3000 | salary | salário | False
3 | 2026-03-07 | expense | 1200 | rent | aluguel | True
```

## Funcionalidades do Sistema

### Registro de Transações

O usuário pode registrar novas transações informando:

*   Data
*   Valor
*   Categoria
*   Descrição
*   Tipo (receita ou despesa)
*   Indicação se é um gasto fixo ou variável

### Estatísticas Financeiras

O sistema calcula e exibe automaticamente:

*   Saldo total atual
*   Total de receitas
*   Total de despesas
*   Média diária de gastos
*   Categoria com maior gasto

**Exemplo:**

```
Saldo atual: R$820
Maior categoria de gasto: Alimentação (38%)
Média diária de gastos: R$72
```

### Sistema de Gráficos

Para uma visualização clara das finanças, a aplicação gera os seguintes gráficos:

1.  **Gastos por Categoria:** Um gráfico de pizza que mostra a proporção dos gastos em diferentes categorias.
    *   Exemplo:
        *   Alimentação 40%
        *   Moradia 30%
        *   Transporte 20%
        *   Lazer 10%

2.  **Receita vs Despesa:** Um gráfico de barras comparando o total de receitas e despesas.

3.  **Evolução do Saldo:** Um gráfico de linha que ilustra como o saldo financeiro evolui ao longo do tempo.

### Insights Automáticos

O sistema analisa os padrões de gastos e oferece insights personalizados. Por exemplo:

*   `⚠️ Alimentação representa 42% dos seus gastos totais.`
*   `💡 Reduzindo 10% dessa categoria você economizaria cerca de R$180 por mês.`

### Módulo de Capacidade de Investimento

O módulo `investment_analysis.py` calcula a capacidade de investimento mensal do usuário com base nos seguintes passos:

1.  **Cálculo da Renda Total:** Soma de todas as transações do tipo `income`.
2.  **Cálculo dos Gastos Fixos:** Soma de todas as transações com `fixed_expense = True`.
3.  **Cálculo dos Gastos Variáveis:** Soma de todas as despesas restantes (`fixed_expense = False`).
4.  **Cálculo da Sobra Mensal:** `sobra = renda_total - gastos_totais`.
5.  **Cálculo da Capacidade de Investimento:** `capacidade_investimento = (sobra / renda_total) * 100`.

**Exemplo:**

*   **Entrada:**
    *   Renda mensal: R$3000
    *   Gastos fixos: R$1500
    *   Gastos variáveis: R$900
*   **Resultado:**
    *   Sobra mensal: R$600
    *   Capacidade de investimento: 20%

### Sistema de Recomendações

Com base na capacidade de investimento, o sistema fornece recomendações:

*   **Capacidade > 30%:** `🟢 Excelente capacidade de investimento.`
*   **Entre 10% e 30%:** `🟡 Capacidade moderada de investimento. Explore opções para otimizar seus gastos.`
*   **Menor que 10%:** `🔴 Capacidade baixa de investimento. Considere reduzir gastos variáveis.`

### Visualização da Capacidade Financeira

Um gráfico adicional de distribuição da renda é gerado, mostrando:

*   Renda total
*   Gastos fixos
*   Gastos variáveis
*   Valor investível

Isso proporciona uma visão clara de para onde o dinheiro está sendo direcionado.

## Execução do Projeto

Para rodar a aplicação localmente, siga os passos:

1.  **Clone o repositório** (se ainda não o fez).
2.  **Navegue até o diretório do projeto:**
    ```bash
    cd personal-finance-analyzer
    ```
3.  **Instale as dependências** listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run main.py
    ```

## Resultado Final da Aplicação

O dashboard final exibirá de forma clara e organizada:

*   Saldo atual
*   Estatísticas financeiras
*   Gráficos de gastos
*   Histórico de transações
*   Capacidade de investimento
*   Recomendações financeiras personalizadas

Este projeto demonstra habilidades em manipulação de dados, estrutura de software, análise financeira, visualização de dados e pensamento de produto, aspectos altamente valorizados por recrutadores em bancos e fintechs.
