# 🎓 Impacto da Escolaridade nos Salários no Brasil - TCC (IFES SI)

> **Autor**: Lucas Garcia de Souza  
> **Curso**: Bacharelado em Sistemas de Informação (2023–2026)  
> **Instituição**: Instituto Federal do Espírito Santo (IFES)

---

## 📌 Descrição do Projeto

Este projeto de Trabalho de Conclusão de Curso (TCC) investiga **o impacto da escolaridade sobre os salários no mercado de trabalho brasileiro**, com foco em **padrões regionais e setoriais**. A análise é baseada nos microdados da **PNAD Contínua (PNADC)**, utilizando técnicas modernas de **engenharia de dados**, **análise estatística**, **visualização interativa** e **machine learning**.

---

## 🎯 Objetivo Geral

Analisar como a escolaridade influencia os salários no Brasil, considerando:

- Região  
- Setor econômico  
- Sexo  
- Cor/Raça  
- Faixa etária  

---

## 📚 Metodologia

- **Base de Dados**: Microdados da PNADC (IBGE)  
- **Pré-processamento**:
  - Leitura FWF com `pandas.read_fwf`
  - Amostragem estratificada por UF
  - Limpeza e categorização de colunas
- **Análises**:
  - Estatísticas descritivas
  - Regressão Linear Múltipla
  - Clusterização (K-Means)
  - Detecção de outliers
- **Visualização**:
  - Gráficos interativos com React.js + Chart.js
  - Mapas com Plotly/Folium
  - Dashboard final com React + API FastAPI

---

## 🧱 Arquitetura do Projeto

```
📦 devTCC/
├── backend/
│   └── main.py                  # API com FastAPI
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── variables/
│   │   └── App.jsx
│   └── vite.config.js
├── pipeline/
│   ├── pipeline_tcc.py          # Script ETL e análises
│   └── airflow/                 # DAGs para automação
├── docker-compose.yml
└── README.md
```

---

## 📊 Funcionalidades do Dashboard

### ✅ Indicadores principais
- Total de registros analisados  
- Média de renda nacional  
- Percentual de pessoas com renda zero  

### ✅ Distribuições demográficas
- Percentual por sexo  
- Percentual por cor/raça  
- Nível de escolaridade  
- Distribuição por estado (UF)  

### ✅ Gráficos de renda média
- Por escolaridade  
- Por UF (com/sem outliers)  
- Por setor econômico  
- Comparação por sexo e raça  

### ✅ Mapas interativos
- Renda média por UF  
- Percentual de renda zero por UF  

### ✅ Casos notáveis / Outliers
- Pessoas com alta renda e baixa escolaridade  
- Ranking das maiores rendas por estado  

### 🔜 Modelos preditivos e clusterização *(em desenvolvimento)*
- Gráfico real vs previsto  
- Dispersão com clusters (K-Means)  
- Tabela de métricas (R², RMSE, MAE)  

---

## 🚀 Tecnologias Utilizadas

| Camada          | Ferramentas e Tecnologias                      |
|-----------------|------------------------------------------------|
| **Linguagem**    | Python, JavaScript (React)                    |
| **Backend**      | FastAPI, Pandas, Sklearn, Statsmodels         |
| **Frontend**     | React.js, Vite, Chart.js, Plotly.js           |
| **ETL**          | Pandas, NumPy                                 |
| **Visualização** | Matplotlib, Seaborn, Folium                   |
| **Orquestração** | Apache Airflow                                |
| **Containerização** | Docker, Docker Compose                    |
| **Outros**       | VS Code, Git, GitHub, Jupyter Notebooks       |

---

## 📦 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/tcc-salarios-escolaridade.git
cd tcc-salarios-escolaridade
```

### 2. Subir os serviços com Docker

```bash
docker-compose up --build
```

### 3. Acessar os serviços

- 🌐 **Frontend**: [http://localhost:5173](http://localhost:5173)  
- ⚙️ **API FastAPI**: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ⛅ **Airflow** (se configurado): [http://localhost:8080](http://localhost:8080)  

---

## 📈 Resultados Esperados

- ✅ Análise estatística da influência da escolaridade nos salários  
- ✅ Visualização interativa para diferentes demografias e regiões  
- 🔍 Insights de desigualdades e padrões regionais/setoriais  
- 🔄 Possibilidade de replicar e expandir para anos diferentes  

---

## 📋 Status Atual do Projeto

| Etapa                     | Status       |
|--------------------------|--------------|
| Pipeline de dados        | ✅ Concluído  |
| Análises estatísticas    | ✅ Concluídas |
| Modelos de regressão     | ✅ Desenvolvidos |
| Clusterização            | 🔜 Em andamento |
| Dashboard com React      | ✅ Funcional  |
| Integração via API       | ✅ Parcial    |
| Automação com Airflow    | 🔜 Planejada  |

---

## 📌 Licença

Este projeto está sob a Licença MIT. Veja o arquivo `LICENSE.md` para mais informações.

---

## 🤝 Agradecimentos

- Instituto Federal do Espírito Santo - IFES  
- Professores orientadores do curso de Sistemas de Informação  
- Comunidade open-source por bibliotecas incríveis  

> _“Educação é a arma mais poderosa que você pode usar para mudar o mundo.” – Nelson Mandela_