"""
src/models/schemas.py
Pydantic schemas for request/response validation.

DEUDA TÉCNICA INTENCIONAL:
  - [MEDIA]  Campos sin descripción (Field sin description)
  - [BAJA]   Clase Config sin uso de model_config (Pydantic v1 style en v2)
  - [BAJA]   Tipo 'Any' usado sin necesidad (python:S5322)
"""
from typing import Optional, Any
from pydantic import BaseModel, Field, ConfigDict, EmailStr



# ── Estudiante ────────────────────────────────────────────────

class EstudianteCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    codigo: str
    nombre: str
    email: EmailStr
    semestre: int

    # [DEUDA] Pydantic v1 style — debería ser model_config = ConfigDict(...)
    #class Config:
        #str_strip_whitespace = True


class EstudianteResponse(BaseModel):
    codigo: str
    nombre: str
    email: str
    semestre: int
    activo: bool


# ── Materia ───────────────────────────────────────────────────

class MateriaCreate(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    # [DEUDA] tipo Any innecesario — debería ser Optional[str]
    descripcion: Any = None


class MateriaResponse(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    descripcion: Optional[str] = None


# ── Nota ──────────────────────────────────────────────────────

class NotaCreate(BaseModel):
    codigo_estudiante: str
    codigo_materia: str
    actividad: str
    valor: float


class NotaResponse(BaseModel):
    id: int
    codigo_estudiante: str
    codigo_materia: str
    actividad: str
    valor: float
    aprobado: bool
