import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from dominio.mapa import Mapa
from dominio.rutas import buscar_ruta

print("semilla | transitables | pasos | exploradas")
for semilla in range(1, 11):
    mapa = Mapa.generar(20, 20, semilla)
    transitables = 400 - mapa.contar("#")
    ruta = buscar_ruta(mapa, mapa.inicio, mapa.meta)
    print(f"{semilla:>7} | {transitables:>12} | {ruta.distancia:>5} | {ruta.exploradas:>10}")
    