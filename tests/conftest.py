"""Configuración compartida de pytest (se amplía con cada componente)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
