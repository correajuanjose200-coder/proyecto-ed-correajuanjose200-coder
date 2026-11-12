# Última Dosis — Proyecto integrador (Estructuras de Datos, ID 706132)

Juego por turnos en consola: Pedro cruza una ciudad infectada con el antídoto hasta el aeropuerto mientras los zombies lo persiguen.

## Requisitos
- Python 3.11 o superior
- `pip install pytest`

## Ejecutar
```bash
python main.py
```

## Pruebas
```bash
pytest
```

## Estructura
- `specs/`: artefactos SDD (constitución, historias, MoSCoW, estructuras, specs por componente)
- `estructuras/`: una estructura por módulo, implementadas desde cero
- `dominio/`: lógica del juego
- `tests/`: pruebas con pytest
- `ANALISIS.md`, `BITACORA.md`, `docs/`

Autor: Juan José Correa

## Estado de la entrega final
- Implementado: pila, cola, inventario, historial (deshacer y rehacer con efectos), mapa con generación por semilla, BFS para los zombis, juego completo en consola.
- No implementado: AVL, montículo, cola de turnos, antídoto, aturdimiento (ver `specs/00-producto/moscow.md`).
- Controles: `w/a/s/d` mover, `x` esperar, `u N` usar, `g N` soltar, `z` deshacer, `r` rehacer, `i` inventario, `q` salir.
- Semilla: `python main.py 5` genera otro mapa.
