# Tareas — Historial de acciones

Versión 1.0 · 2026-10-14 · Una tarea = un commit. Cada tarea cierra uno o más CA con su prueba. Las pruebas se escriben antes que el código de la tarea.

| ID | Tarea | Cierra | Prueba (archivo) | Commit sugerido |
|---|---|---|---|---|
| T-01 | Clase `Nodo` propia | — (soporte) | `tests/test_nodo.py` | `feat(nodo): clase Nodo` |
| T-02 | `Pila` vacía: `esta_vacia`, `tamano`, errores en `desapilar`/`cima` | CA-18 (base) | `tests/test_pila.py` (vacía: 3 casos) | `test(pila): casos vacía` · `feat(pila): errores en vacía` |
| T-03 | `Pila.apilar`, `desapilar`, `cima` con 1 y varios elementos | CA-H1 (base) | `tests/test_pila.py` (1 y N elementos) | `feat(pila): apilar y desapilar` |
| T-04 | `Pila.vaciar` | CA-17 (base) | `tests/test_pila.py` (`vaciar`: 3 casos) | `feat(pila): vaciar` |
| T-05 | `Accion` con los datos de la spec | CA-14, CA-15 (datos) | `tests/test_accion.py` | `feat(accion): datos de la acción` |
| T-06 | `Historial.registrar` y `cantidad` | CA-H3 | `tests/test_historial.py` | `feat(historial): registrar` |
| T-07 | `Historial.deshacer` (orden inverso, vacío) | CA-14, CA-18, CA-H1 | `tests/test_historial.py` | `feat(historial): deshacer` |
| T-08 | `Historial.rehacer` (orden inverso, vacío) | CA-16, CA-18, CA-H2 | `tests/test_historial.py` | `feat(historial): rehacer` |
| T-09 | Acción nueva vacía lo rehacible | CA-17, CA-H4 | `tests/test_historial.py` | `fix(historial): registrar vacía deshechas` |
| T-10 | Integrar al turno de Pedro: revertir/reaplicar efectos (posiciones, salud, objeto recogido) | CA-14, CA-15 | `tests/test_integracion_historial.py` | `feat(historial): integrado al turno` |
| T-11 | Opciones "deshacer" y "rehacer" en `main.py` | CA-18, CA-36 | prueba manual documentada en `docs/evidencias/` | `feat(consola): deshacer y rehacer` |

## Definición de hecho
Pruebas de la tarea pasando, docstrings con complejidad, `specs/trazabilidad.md` actualizado.
