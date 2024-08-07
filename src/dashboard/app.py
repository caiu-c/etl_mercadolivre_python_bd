import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Função para carregar dados do banco de dados SQLite
@st.cache
def load_data():
    conn = sqlite3.connect('../data/quotes.db')
    df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)
    conn.close()
    return df

# Carregar e transformar dados
df = load_data()

# Título do Dashboard
st.title('Dashboard de Pesquisa de Mercado - Perfumes no Mercado Livre')

# KPIs Principais
st.subheader("KPIs Principais")
col1, col2, col3 = st.columns(3)

total_items = df.shape[0]
col1.metric(label="Número Total de Itens", value=total_items)

unique_brands = df['brand'].nunique()
col2.metric(label="Número de Marcas Únicas", value=unique_brands)

average_new_price = df['new_price'].mean()
col3.metric(label="Preço Médio Novo (R$)", value=f"{average_new_price:.2f}")

# Distribuição de Preços
st.subheader('Distribuição de Preços')
fig_price_distribution = px.histogram(df, x='new_price', nbins=20, title='Distribuição de Preços', color_discrete_sequence=['#636EFA'])
st.plotly_chart(fig_price_distribution)

# Desvio Padrão do Preço
price_std_dev = df['new_price'].std()
st.metric(label="Desvio Padrão do Preço (R$)", value=f"{price_std_dev:.2f}")

# Correlação entre Preço e Avaliação
price_rating_corr = df[['new_price', 'reviews_rating_number']].corr().iloc[0, 1]
st.metric(label="Correlação Preço vs Avaliação", value=f"{price_rating_corr:.2f}")
fig_price_vs_rating = px.scatter(df, x='new_price', y='reviews_rating_number', title='Relação entre Preço e Avaliação', color='reviews_rating_number', color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig_price_vs_rating)

# Número de Avaliações por Marca
st.subheader('Número de Avaliações por Marca')
reviews_by_brand = df.groupby('brand')['reviews_amount'].sum().sort_values(ascending=False)
fig_reviews_by_brand = px.bar(reviews_by_brand, x=reviews_by_brand.index, y=reviews_by_brand.values, title='Número de Avaliações por Marca', color=reviews_by_brand.values, color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig_reviews_by_brand)

# Proporção de Itens com Desconto
discount_items_ratio = (df['discount'] > 0).sum() / df.shape[0] * 100
st.metric(label="Proporção de Itens com Desconto (%)", value=f"{discount_items_ratio:.2f}%")

# Preço Médio com Desconto
average_discounted_price = df[df['discount'] > 0]['new_price'].mean()
st.metric(label="Preço Médio com Desconto (R$)", value=f"{average_discounted_price:.2f}")

# Média de Desconto por Marca
st.subheader('Média de Desconto por Marca')
average_discount_by_brand = df.groupby('brand')['discount'].mean().sort_values(ascending=False)
fig_average_discount_by_brand = px.bar(average_discount_by_brand, x=average_discount_by_brand.index, y=average_discount_by_brand.values, title='Média de Desconto por Marca', color=average_discount_by_brand.values, color_continuous_scale=px.colors.sequential.Inferno)
st.plotly_chart(fig_average_discount_by_brand)

# Percentual de Desconto por Marca
st.subheader('Percentual de Desconto por Marca')
average_discount_percentage_by_brand = df[df['old_price'] > 0].groupby('brand')['discount_percentage'].mean().sort_values(ascending=False)
fig_average_discount_percentage_by_brand = px.bar(average_discount_percentage_by_brand, x=average_discount_percentage_by_brand.index, y=average_discount_percentage_by_brand.values, title='Percentual de Desconto por Marca', color=average_discount_percentage_by_brand.values, color_continuous_scale=px.colors.sequential.Magma)
st.plotly_chart(fig_average_discount_percentage_by_brand)

# Itens com Maior Desconto
st.subheader('Itens com Maior Desconto')
top_discount_items = df.nlargest(10, 'discount')[['brand', 'old_price', 'new_price', 'discount']]
fig_top_discount_items = go.Figure(data=[go.Table(
    header=dict(values=list(top_discount_items.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[top_discount_items.brand, top_discount_items.old_price, top_discount_items.new_price, top_discount_items.discount],
               fill_color='lavender',
               align='left'))
])
fig_top_discount_items.update_layout(title='Itens com Maior Desconto')
st.plotly_chart(fig_top_discount_items)

# Distribuição de Avaliações
st.subheader('Distribuição de Avaliações')
fig_reviews_distribution = px.histogram(df, x='reviews_rating_number', nbins=20, title='Distribuição de Avaliações', color_discrete_sequence=['#EF553B'])
st.plotly_chart(fig_reviews_distribution)

# Avaliação Média por Marca
st.subheader('Avaliação Média por Marca')
average_rating_by_brand = df.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
fig_average_rating_by_brand = px.bar(average_rating_by_brand, x=average_rating_by_brand.index, y=average_rating_by_brand.values, title='Avaliação Média por Marca', color=average_rating_by_brand.values, color_continuous_scale=px.colors.sequential.Blues)
st.plotly_chart(fig_average_rating_by_brand)

# Preço Médio por Marca
st.subheader('Preço Médio por Marca')
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
fig_average_price_by_brand = px.bar(average_price_by_brand, x=average_price_by_brand.index, y=average_price_by_brand.values, title='Preço Médio por Marca', color=average_price_by_brand.values, color_continuous_scale=px.colors.sequential.Teal)
st.plotly_chart(fig_average_price_by_brand)
