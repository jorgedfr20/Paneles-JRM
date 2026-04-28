# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:30:37 2026
from pulp import *

def optimizar_paneles(demanda1, demanda2, demanda3,
                      area1, area2, area3,
                      horas_sol=4.5):
    """
    #O"ptimiza la cantidad de paneles solares para 3 casas minimizando el costo.

   # Parámetros:
   # demanda1, demanda2, demanda3: consumo mensual (kWh)
   # area1, area2, area3: área disponible (m2)
    #horas_sol: horas promedio de sol al día

   # Retorna:
    #diccionario con resultados"""

    # Convertir demanda mensual a diaria
    d1 = demanda1 / 30
    d2 = demanda2 / 30
    d3 = demanda3 / 30

    # Crear modelo
    modelo = LpProblem("Optimizacion_Paneles", LpMinimize)

    # Variables de decisión (enteras)
    A1 = LpVariable('A1', lowBound=0, cat='Integer')
    B1 = LpVariable('B1', lowBound=0, cat='Integer')
    C1 = LpVariable('C1', lowBound=0, cat='Integer')

    A2 = LpVariable('A2', lowBound=0, cat='Integer')
    B2 = LpVariable('B2', lowBound=0, cat='Integer')
    C2 = LpVariable('C2', lowBound=0, cat='Integer')

    A3 = LpVariable('A3', lowBound=0, cat='Integer')
    B3 = LpVariable('B3', lowBound=0, cat='Integer')
    C3 = LpVariable('C3', lowBound=0, cat='Integer')

    # Función objetivo (minimizar costo)
    modelo += (
        190*(A1+A2+A3) +
        205*(B1+B2+B3) +
        255*(C1+C2+C3)
    )

    # Restricciones de energía
    modelo += (400*A1 + 450*B1 + 550*C1) * horas_sol / 1000 >= d1, "Energia_Casa1"
    modelo += (400*A2 + 450*B2 + 550*C2) * horas_sol / 1000 >= d2, "Energia_Casa2"
    modelo += (400*A3 + 450*B3 + 550*C3) * horas_sol / 1000 >= d3, "Energia_Casa3"

    # Restricciones de área
    modelo += 1.9*A1 + 2.1*B1 + 2.5*C1 <= area1, "Area_Casa1"
    modelo += 1.9*A2 + 2.1*B2 + 2.5*C2 <= area2, "Area_Casa2"
    modelo += 1.9*A3 + 2.1*B3 + 2.5*C3 <= area3, "Area_Casa3"

    # Resolver
    modelo.solve(PULP_CBC_CMD(msg=0))

    # Resultados
    resultados = {
        "Casa 1": {
            "A": A1.varValue,
            "B": B1.varValue,
            "C": C1.varValue
        },
        "Casa 2": {
            "A": A2.varValue,
            "B": B2.varValue,
            "C": C2.varValue
        },
        "Casa 3": {
            "A": A3.varValue,
            "B": B3.varValue,
            "C": C3.varValue
        },
        "Costo Total": value(modelo.objective)
    }

    return resultados
@author: User
"""

