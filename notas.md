# 1. Verificar que git está instalado
git --version

# 2. Clonar tu fork (reemplaza TU-USUARIO con tu usuario GitHub)
git clone https://github.com/jaimesuarez77/software_quality_project.git

# 3. Entrar a la carpeta del proyecto
cd software_quality_project

# 4. Verificar que estás en la rama main y conectado a tu fork
git remote -v
# Debes ver: origin  https://github.com/jaimesuarez77/software_quality_project.git

# 5. Agregar el repositorio original como upstream (para actualizaciones futuras)
git remote add upstream https://github.com/duvanfr/software_quality_project.git

# 6. Crear una rama de trabajo con el nombre del equipo
git checkout -b feature/grupoOR
# Reemplaza "equipo-01" con el identificador de tu equipo

# 7. Confirmar que la rama fue creada
git branch

# Crear y activar entorno virtual

# En Mac/Linux:
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar las pruebas existentes y ver la cobertura actual
python -m pytest tests/ -v --cov=src --cov-report=term-missing

# Debes ver: 24 passed, cobertura ~78%
____________________________________________________________________________________________

# Arrancar el servidor de desarrollo
uvicorn main:app --reload

# Probar que responde
curl http://localhost:8000/
# {"status": "ok", "message": "Software Quality API"}

# Crear un estudiante de prueba
curl -X POST http://localhost:8000/estudiantes/ \
  -H "Content-Type: application/json" \
  -d '{"codigo":"E001","nombre":"Ana García","email":"ana@test.com","semestre":5}'

Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
src/__init__.py                        0      0   100%
src/models/__init__.py                 0      0   100%
src/models/database.py                18      0   100%
src/models/schemas.py                 37      0   100%
src/routers/__init__.py                0      0   100%
src/routers/estudiantes.py            41     11    73%   58-62, 67-72
src/routers/materias.py               31      6    81%   36, 50-54
src/routers/notas.py                  52     22    58%   50-54, 59-63, 68-73, 78-83, 88, 93
src/services/__init__.py               0      0   100%
src/services/academic_service.py      31      7    77%   28-31, 41-44, 72
----------------------------------------------------------------
TOTAL                                210     46    78%

cambiar toda la función:

def reporte_academico(codigo_estudiante: str) -> dict:
    """
    Genera un reporte completo de un estudiante.

    [DEUDA MEDIA] Función con demasiadas responsabilidades:
    valida existencia, calcula promedio, filtra notas, clasifica.
    Debería dividirse en funciones más pequeñas.
    """
    estudiantes = get_estudiantes()

    if codigo_estudiante.upper() not in estudiantes:
        return {"error": "Estudiante no encontrado"}

    estudiante = estudiantes[codigo_estudiante.upper()]
    notas = [n for n in get_notas()
             if n["codigo_estudiante"] == codigo_estudiante.upper()]

    # [DEUDA BAJA] Variable declarada y no usada
    #materias_vistas = set(n["codigo_materia"] for n in notas)
    #conteo_materias = len(materias_vistas)  # declarada pero el valor no se retorna

    aprobadas = [n for n in notas if es_aprobado(n["valor"])]
    reprobadas = [n for n in notas if not es_aprobado(n["valor"])]

    if notas:
        promedio = round(sum(n["valor"] for n in notas) / len(notas), 2)
    else:
        promedio = 0.0

    return {
        "estudiante": estudiante["nombre"],
        "total_notas": len(notas),
        "aprobadas": len(aprobadas),
        "reprobadas": len(reprobadas),
        "promedio": promedio,
    }

python3 -m pip install --no-cache-dir -r requirements.txt