# Perfume Market Research Automation - ETL Project

### Problem Description
A perfume store needs to automate its daily market research to understand the prices charged by competitors. Currently, an employee has to open the first 10 pages of Mercado Livre EVERY DAY and collect the following information to calculate indicators:
- Brand
- Regular price
- Discounted price
- Number of reviews
- Review rating

### Project Objective
This project aims to automate the process of data collection, indicator calculation, and result visualization using open-source tools, without generating additional costs for the company.

### Project Stages

1. **Data Collection with Scrapy**
   - We used the Python Scrapy library to perform web scraping of the required information. Scrapy is a powerful open-source tool that allows for quick and efficient data extraction from the web.

2. **Data Processing and Indicator Calculation with Pandas**
   - The collected data were processed and analyzed using the Pandas library. Pandas is a highly efficient open-source library for data manipulation and analysis in Python. Through it, we calculated the indicators of interest for the perfume store.

3. **Data Storage with SQLite**
   - After processing, the data were stored in a SQLite database. SQLite is a lightweight, open-source database engine that requires minimal setup and ensures no additional costs.

4. **Result Visualization with Streamlit**
   - To facilitate the visualization and interpretation of the data, we developed an interactive dashboard using Streamlit. Streamlit is an open-source library that allows for the rapid creation of interactive web applications for data visualization.

### Tools Used
- **Scrapy**: For web scraping data.
- **Pandas**: For data processing and analysis.
- **SQLite**: For data storage.
- **Streamlit**: For interactive data visualization.

### Benefits
- **Process Automation**: Reduction of manual work and increased efficiency in data collection.
- **Advanced Data Analysis**: Calculation of indicators to support decision-making.
- **Clear and Intuitive Visualization**: Facilitates data interpretation and market insights.

### Key Findings
- **Highest Average Price**: The brand BVLGARI has the highest average price, at R$620.27.
- **Best Rating**: Avon has an average rating of 4.725, nearly tied with Prada at 4.7, and ahead of VERSACE.
- **Consistent Ratings**: JEQUITI has the same average rating as VERSACE.
- **Rating Distribution**: Most perfume ratings fall between 4.3 and 4.7.
- **Largest Discount**: The largest discount was given on a perfume by AZZARO, reaching R$658.31.
- **Price vs. Rating Correlation**: There is no clear correlation between price and rating.
- **Total Perfumes Analyzed**: 537 perfumes were analyzed from the first 10 pages.
- **Total Brands**: 181 brands were identified, with an average price of R$44.43.

### Contact
For more information, questions, or suggestions, contact [Your Name] at [youremail@example.com].

---

This project is developed with open-source tools, showcasing skills in data engineering and a commitment to efficient and economical solutions.

---

# Perfume Market Research Automation - Projeto de ETL

### Descrição do Problema
Uma loja de perfumes precisa automatizar sua pesquisa de mercado diária para entender os preços praticados pelos concorrentes. Atualmente, um colaborador tem que abrir as primeiras 10 páginas do Mercado Livre TODO DIA e coletar as seguintes informações para calcular indicadores:
- Marca
- Preço normal
- Preço com desconto
- Número de avaliações
- Valor da avaliação

### Objetivo do Projeto
Este projeto visa automatizar o processo de coleta de dados, cálculo de indicadores e visualização dos resultados, utilizando ferramentas de código aberto (Open Source), sem gerar custos adicionais para a empresa.

### Etapas do Projeto

1. **Coleta de Dados com Scrapy**
   - Utilizamos a biblioteca Scrapy do Python para realizar o Web Scraping das informações necessárias. O Scrapy é uma poderosa ferramenta de código aberto que permite a extração de dados da web de forma rápida e eficiente.

2. **Processamento e Cálculo de Indicadores com Pandas**
   - Os dados coletados foram processados e analisados utilizando a biblioteca Pandas. O Pandas é uma biblioteca de código aberto altamente eficiente para manipulação e análise de dados em Python. Através dele, calculamos os indicadores de interesse da loja de perfumes.

3. **Armazenamento dos Dados com SQLite**
   - Após o processamento, os dados foram armazenados em um banco de dados SQLite. O SQLite é um mecanismo de banco de dados leve e de código aberto que requer configuração mínima e garante a ausência de custos adicionais.

4. **Visualização dos Resultados com Streamlit**
   - Para facilitar a visualização e interpretação dos dados, desenvolvemos um dashboard interativo utilizando o Streamlit. O Streamlit é uma biblioteca de código aberto que permite a criação rápida de aplicações web interativas para visualização de dados.

### Ferramentas Utilizadas
- **Scrapy**: Para o Web Scraping dos dados.
- **Pandas**: Para processamento e análise dos dados.
- **SQLite**: Para armazenamento dos dados.
- **Streamlit**: Para visualização interativa dos dados.

### Benefícios
- **Automação do Processo**: Redução de trabalho manual e aumento da eficiência na coleta de dados.
- **Análise de Dados Avançada**: Cálculo de indicadores para suporte à tomada de decisão.
- **Visualização Clara e Intuitiva**: Facilita a interpretação dos dados e insights do mercado.

### Conclusões Principais
- **Maior Preço Médio**: A marca BVLGARI tem o maior preço médio, com R$620,27.
- **Melhor Avaliação**: Avon tem uma avaliação média de 4,725, quase empatada com Prada (4,7) e à frente de VERSACE.
- **Avaliação Consistente**: JEQUITI tem a mesma avaliação média de VERSACE.
- **Distribuição de Avaliações**: A maioria das avaliações de perfume está entre 4,3 e 4,7.
- **Maior Desconto**: O maior desconto foi dado em um perfume da AZZARO, chegando a R$658,31.
- **Correlação Preço vs. Avaliação**: Não há uma correlação clara entre preço e avaliação.
- **Total de Perfumes Analisados**: 537 perfumes nas 10 primeiras páginas.
- **Total de Marcas**: 181 marcas com um preço médio de R$44,43.

### Contato
Para mais informações, dúvidas ou sugestões, entre em contato com [Seu Nome] através do email [seuemail@exemplo.com].

---

Este projeto é desenvolvido com ferramentas de código aberto, demonstrando habilidades em engenharia de dados e compromisso com soluções eficientes e econômicas.
