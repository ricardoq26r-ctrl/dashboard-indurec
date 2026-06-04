import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_excel("indurec.xlsx")
df = df.dropna(axis=1, how="all")
df["% Reprocesos"] = (df["REPROCESOS"] / df["N°SERVICIOS"]) * 100

st.title("Dashboard de Reprocesos - Indurec")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Servicios Totales", int(df["N°SERVICIOS"].sum()))
col2.metric("Reprocesos Totales", int(df["REPROCESOS"].sum()))
col3.metric("% Reprocesos Promedio", f"{df['% Reprocesos'].mean():.1f}%")
col4.metric("Costo Total S/", f"{df['COSTO DE REPROCESOS'].sum():,.2f}")

st.divider()

fig1 = px.bar(df, x="MES", y="N°SERVICIOS", title="Servicios por Mes",
              text_auto=True, color_discrete_sequence=["#2563EB"])
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.bar(df, x="MES", y="REPROCESOS", title="Reprocesos por Mes",
              text_auto=True, color_discrete_sequence=["#DC2626"])
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(df, x="MES", y="% Reprocesos", title="% Reprocesos por Mes",
               markers=True, color_discrete_sequence=["#D97706"])
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.line(df, x="MES", y="COSTO DE REPROCESOS",
               title="Costo de Reprocesos por Mes (S/)",
               markers=True, color_discrete_sequence=["#16A34A"])
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Tabla de Datos")
st.dataframe(df, use_container_width=True)
