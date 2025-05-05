# 📦 Diagnóstico de Entidades de Dados

Um estudo de caso prático de Data Science e Engenharia de Dados.

---

## 🎯 Objetivo

Você está monitorando execuções de entidades de dados (ETLs, cargas, syncs etc.) e quer responder perguntas como:

- Quais entidades falham com mais frequência?
- Qual o tempo médio de execução por entidade, categoria ou servidor?
- As execuções estão dentro do tempo esperado?
- Existem padrões de falhas por horário, dia da semana ou servidor?

---

## 🧱 Estrutura do Projeto

Feito por **Lucas Costa Ribeiro** – Engenheiro de Sistemas e Cientista de Dados.

    project-root/
    ├── data/
    │ ├── raw/ # Dados brutos (Mockaroo, simulados)
    │ ├── processed/ # CSV com dados limpos e padronizados
    │ └── mart/ # Tabelas normalizadas (modelo estrela)
    ├── db/ # Scripts para criação da base de dados
    ├── notebooks/ # Análises exploratórias (se aplicável)
    ├── bi/ # Arquivo Power BI (.pbix)
    ├── README.md # Descrição do projeto
    └── requirements.txt # Dependências Python

---

## 🔄 Pipeline de Dados

### 🐍 Etapa Python – Processamento & Preparação

Responsável por:
- Leitura e limpeza dos dados
- Cálculo de campos derivados:
  - Tempo médio por entidade
  - Desvio da execução
- Construção de modelo estrela:
  - Dimensões: Entidade, Tempo, Servidor, Categoria
  - Fato: Execuções
- Exportação para CSVs prontos para o Power BI

### 📊 Etapa Power BI – Visualização & Insights

Responsável por:
- Dashboard de desempenho por entidade e categoria
- Taxa de sucesso/erro por período e por servidor
- Tendências e padrões por hora e dia da semana
- Detecção de outliers ou execuções anormais
- Comparativo entre tempo real e tempo esperado

---

## 📌 Próximos Passos

- [ ] Finalizar visualizações no Power BI
- [ ] Explorar previsão de falhas com modelos simples (opcional)
- [ ] Automatizar o pipeline com `cron` ou `Airflow` (extra)
- [ ] Adicionar testes unitários nos scripts Python
- [ ] Publicar no GitHub e incluir portfólio pessoal

---

## 🚀 Resultado Esperado

Um painel completo que permita **identificar gargalos, falhas e oportunidades de melhoria** na execução das suas entidades de dados.

---

> Projeto educacional com dados simulados. Adaptável para ambientes reais.
