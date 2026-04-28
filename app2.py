# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:34:54 2026
import streamlit as st
from modelo import optimizar_paneles

st.set_page_config(page_title="Optimización Paneles Solares", page_icon="☀️", layout="wide")

# ─── HEADER ─────────────────────────────────────────────
st.markdown("""
<div style="background: linear-gradient(90deg, #1a3a5c, #2d6a9f);
padding: 1rem; border-radius: 10px; color: white;">
<h2>☀️ Optimización de Paneles Solares</h2>
<p>Modelo de Programación Lineal - Minimización de Costos</p>
</div>
""", unsafe_allow_html=True)

# ─── SIDEBAR ────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Parámetros")

    st.subheader("🏠 Casa 1")
    demanda1 = st.number_input("Consumo mensual (kWh)", value=355)
    area1 = st.number_input("Área techo (m²)", value=100)

    st.subheader("🏠 Casa 2")
    demanda2 = st.number_input("Consumo mensual (kWh) ", value=342)
    area2 = st.number_input("Área techo (m²) ", value=120)

    st.subheader("🏠 Casa 3")
    demanda3 = st.number_input("Consumo mensual (kWh)  ", value=302)
    area3 = st.number_input("Área techo (m²)  ", value=176)

    st.subheader("🌞 Condiciones")
    horas_sol = st.number_input("Horas de sol", value=4.5)

    resolver = st.button("🚀 Resolver Optimización")

# ─── RESULTADOS ─────────────────────────────────────────
if resolver:
    resultado = optimizar_paneles(
        demanda1, demanda2, demanda3,
        area1, area2, area3,
        horas_sol
    )

    st.success("✅ Optimización completada")

    # Mostrar resultados por casa
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🏠 Casa 1")
        st.write(resultado["Casa 1"])

    with col2:
        st.subheader("🏠 Casa 2")
        st.write(resultado["Casa 2"])

    with col3:
        st.subheader("🏠 Casa 3")
        st.write(resultado["Casa 3"])

    # Costo total
    st.markdown("---")
    st.subheader("💰 Costo Total")
    st.write(f"${resultado['Costo Total']:.2f}")
else:
    st.info("👈 Ajusta los parámetros y presiona 'Resolver Optimización'")
@author: User
"""

