# conftest.py — pytest root configuration
import sys
from pathlib import Path

# Agregar el directorio sqp/ al path de Python para que los imports funcionen
sqp_dir = Path(__file__).parent
sys.path.insert(0, str(sqp_dir))
