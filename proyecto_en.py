#trabajamos con streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from io import StringIO
import numpy as np
import os
import sys

# cargamos los datos
df1 = pd.read_csv(r"C:\Users\pc\Downloads\CVD_cleaned.csv")
df2 = pd.read_csv(r"C:\Users\pc\Downloads\cardio_train.csv")
df3 = pd.read_csv(r"C:\Users\pc\Downloads\heart_statlog_cleveland_hungary_final.csv")

st.title('Análisis de Enfermedades y Riesgos en la Salud Cardiovascular')

# visualizamos los datos del primer dataframe
st.subheader('Vista previa de los datos del df1')
st.write(df1.head())

# identificación de variables numéricas y categóricas del primer dataset
variables_numericas1 = df1.select_dtypes(include=['float64', 'int64']).columns.tolist()
variables_categoricas1 = [col for col in df1.select_dtypes(include=['object', 'category']).columns if df1[col].nunique() < 20]

st.write("Variables numéricas detectadas:", variables_numericas1)
st.write("Variables categóricas detectadas:", variables_categoricas1)

# buscamos las matrices de correlación del primer dataset
if variables_numericas1:
    st.subheader("Matriz de Correlación")
    correlacion_matrix1 = df1[variables_numericas1].corr()
    st.dataframe(correlacion_matrix1)

    st.subheader("Mapa de Calor de Correlaciones")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlacion_matrix1, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# relacionamos entre dos variables numéricas del primer dataframe
st.sidebar.subheader("Relación entre dos variables numéricas")
x_var1 = st.sidebar.selectbox("Selecciona la variable X", variables_numericas1, key="x_var1")
y_var1 = st.sidebar.selectbox("Selecciona la variable Y", variables_numericas1, key="y_var1")

if x_var1 and y_var1:
    st.subheader(f"Relación entre {x_var1} y {y_var1}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df1, x=x_var1, y=y_var1, ax=ax)
    ax.set_title(f"Relación entre {x_var1} y {y_var1}")
    ax.set_xlabel(x_var1)
    ax.set_ylabel(y_var1)
    st.pyplot(fig)

# analizamos la distribución de variables numéricas del primer dataframe
st.sidebar.subheader("Análisis de Distribución del Primer Dataframe")
selected_var1 = st.sidebar.selectbox("Selecciona una variable para analizar su distribución", variables_numericas1, key="selected_var1")

if selected_var1:
    st.subheader(f"Distribución de {selected_var1}")
    fig, ax = plt.subplots()
    sns.histplot(df1[selected_var1], kde=True, ax=ax)
    ax.set_title(f"Distribución de {selected_var1}")
    ax.set_xlabel(selected_var1)
    st.pyplot(fig)

# tendencia entre variables categóricas y numéricas del primer dataframe
st.sidebar.subheader("Análisis de Tendencias en el Primer Dataframe")
categorical_var1 = st.sidebar.selectbox("Selecciona una categoría", variables_categoricas1, key="categorical_var1")
trend_var1 = st.sidebar.selectbox("Selecciona una variable numérica para la tendencia", variables_numericas1, key="trend_var1")

if categorical_var1 and trend_var1:
    st.subheader(f"Tendencia de {trend_var1} por {categorical_var1}")
    trend_df1 = df1.groupby(categorical_var1)[trend_var1].mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=trend_df1, x=categorical_var1, y=trend_var1, ax=ax)
    ax.set_title(f"Tendencia de {trend_var1} por {categorical_var1}")
    ax.set_xlabel(categorical_var1)
    ax.set_ylabel(trend_var1)
    st.pyplot(fig)

# visualizamos los datos del segundo dataset pero primero pasamos la columna de días a años
df2['Age'] = (df2['Age']//365).astype(int)
st.subheader('Vista previa de los datos del df2')
st.write(df2.head())

# identificamos las variables numéricas y categóricas del segundo dataset y covertimos la primera columna de días a años
variables_numericas2 = df2.select_dtypes(include=['float64', 'int64']).columns.tolist()
variables_categoricas2 = [col for col in df2.select_dtypes(include=['object', 'category']).columns if df2[col].nunique() < 20]

st.write("Variables numéricas detectadas:", variables_numericas2)
st.write("Variables categóricas detectadas:", variables_categoricas2)

# buscamos las matrices de correlación del segundo dataframe
if variables_numericas2:
    st.subheader("Matriz de Correlación del segundo dataframe")
    correlacion_matrix2 = df2[variables_numericas2].corr()
    st.dataframe(correlacion_matrix2)

    st.subheader("Mapa de Calor de Correlaciones del segundo dataframe")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlacion_matrix2, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# relacionamos entre dos variables numéricas del segundo dataframe
st.sidebar.subheader("Relación entre dos variables numéricas del segundo dataframe")
x_var2 = st.sidebar.selectbox("Selecciona la variable X", variables_numericas2, key="x_var2")
y_var2 = st.sidebar.selectbox("Selecciona la variable Y", variables_numericas2, key="y_var2")

if x_var2 and y_var2:
    st.subheader(f"Relación entre {x_var2} y {y_var2}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df2, x=x_var2, y=y_var2, ax=ax)
    ax.set_title(f"Relación entre {x_var2} y {y_var2}")
    ax.set_xlabel(x_var2)
    ax.set_ylabel(y_var2)
    st.pyplot(fig)


# analizamos de distribución de variables numéricas del segundo dataframe
st.sidebar.subheader("Análisis de Distribución del segundo Dataframe")
selected_var2 = st.sidebar.selectbox("Selecciona una variable para analizar su distribución", variables_numericas2, key="selected_var2")

if selected_var2:
    st.subheader(f"Distribución de {selected_var2}")
    fig, ax = plt.subplots()
    sns.histplot(df2[selected_var2], kde=True, ax=ax)
    ax.set_title(f"Distribución de {selected_var2}")
    ax.set_xlabel(selected_var2)
    st.pyplot(fig)

# tendencia entre variables categóricas y numéricas del segundo dataframe
st.sidebar.subheader("Análisis de Tendencias del segundo Dataframe")
categorical_var2 = st.sidebar.selectbox("Selecciona una categoría", variables_categoricas2, key="categorical_var2")
trend_var2 = st.sidebar.selectbox("Selecciona una variable numérica para la tendencia", variables_numericas2, key="trend_var2")

if categorical_var2 and trend_var2:
    st.subheader(f"Tendencia de {trend_var2} por {categorical_var2}")
    trend_df2 = df2.groupby(categorical_var2)[trend_var2].mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=trend_df2, x=categorical_var2, y=trend_var2, ax=ax)
    ax.set_title(f"Tendencia de {trend_var2} por {categorical_var2}")
    ax.set_xlabel(categorical_var2)
    ax.set_ylabel(trend_var2)
    st.pyplot(fig)

# visualizamos los datos del tercer dataframe
st.subheader('Vista previa de los datos del tercer Dataframe')
st.write(df3.head())

# identificamos las variables numéricas y categóricas del tercer dataframe
variables_numericas3 = df3.select_dtypes(include=['float64', 'int64']).columns.tolist()
variables_categoricas3 = [col for col in df3.select_dtypes(include=['object', 'category']).columns if df3[col].nunique() < 20]

st.write("Variables numéricas detectadas:", variables_numericas3)
st.write("Variables categóricas detectadas:", variables_categoricas3)

# buscamos las matrices de correlación del tercer dataframe
if variables_numericas3:
    st.subheader("Matriz de Correlación del tercer dataframe")
    correlacion_matrix3 = df3[variables_numericas3].corr()
    st.dataframe(correlacion_matrix3)

    st.subheader("Mapa de Calor de Correlaciones del tercer dataframe")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlacion_matrix3, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# relacionamos entre dos variables numéricas del tercer dataframe
st.sidebar.subheader("Relación entre dos variables numéricas")
x_var3 = st.sidebar.selectbox("Selecciona la variable X", variables_numericas3, key="x_var3")
y_var3 = st.sidebar.selectbox("Selecciona la variable Y", variables_numericas3, key="y_var3")

if x_var3 and y_var3:
    st.subheader(f"Relación entre {x_var3} y {y_var3}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df3, x=x_var3, y=y_var3, ax=ax)
    ax.set_title(f"Relación entre {x_var3} y {y_var3}")
    ax.set_xlabel(x_var3)
    ax.set_ylabel(y_var3)
    st.pyplot(fig)

# analizamos la distribución de variables numéricas del tercer dataframe
st.sidebar.subheader("Análisis de Distribución del tercer Dataframe")
selected_var3 = st.sidebar.selectbox("Selecciona una variable para analizar su distribución", variables_numericas3, key="selected_var3")

if selected_var3:
    st.subheader(f"Distribución de {selected_var3}")
    fig, ax = plt.subplots()
    sns.histplot(df3[selected_var3], kde=True, ax=ax)
    ax.set_title(f"Distribución de {selected_var3}")
    ax.set_xlabel(selected_var3)
    st.pyplot(fig)

# tendencia entre variables categóricas y numéricas del tercer dataframe
st.sidebar.subheader("Análisis de Tendencias del tercer Dataframe")
categorical_var3 = st.sidebar.selectbox("Selecciona una categoría", variables_categoricas3, key="categorical_var3")
trend_var3 = st.sidebar.selectbox("Selecciona una variable numérica para la tendencia", variables_numericas3, key="trend_var3")

if categorical_var3 and trend_var3:
    st.subheader(f"Tendencia de {trend_var3} por {categorical_var3}")
    trend_df3 = df3.groupby(categorical_var3)[trend_var3].mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=trend_df3, x=categorical_var3, y=trend_var3, ax=ax)
    ax.set_title(f"Tendencia de {trend_var3} por {categorical_var3}")
    ax.set_xlabel(categorical_var3)
    ax.set_ylabel(trend_var3)
    st.pyplot(fig)


