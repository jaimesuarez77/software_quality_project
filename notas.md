src/models/schemas.py:16
  /home/jaime/Documents/laboratorio-ci/Proyectos/Quality_proy/software_quality_project/sqp/src/models/schemas.py:16: PydanticDeprecatedSince20: Support for class-based `config` is deprecated, use ConfigDict instead. Deprecated in Pydantic V2.0 to be removed in V3.0. See Pydantic V2 Migration Guide at https://errors.pydantic.dev/2.13/migration/
    class EstudianteCreate(BaseModel):

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================================ tests coverage =================================================================================
________________________________________________________________ coverage: platform linux, python 3.12.3-final-0 ________________________________________________________________

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
Required test coverage of 60.0% reached. Total coverage: 78.10%
========================================================================= 24 passed, 1 warning in 1.59s =========================================================================
(venv) jaime@jaime-HP-EliteBook-840-14-inch-G9-Notebook-PC:~/Documents/laboratorio-ci/Proyectos/Quality_proy/software_quality_project/sqp$ 

{"status":"ok","message":"Software Quality API"}
python3 --version && python3 --version && command -v python3 && command -v python

pytest --cov=src --cov-report=xml:reports/coverage.xml --cov-report=html:reports/htmlcov --cov-fail-under=60 --junitxml=reports/junit.xml

python3 -m pip install --no-cache-dir -r requirements.txt