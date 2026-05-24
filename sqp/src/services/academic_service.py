"""
src/services/academic_service.py
Business logic layer.

DEUDA TÉCNICA INTENCIONAL:
  - [ALTA]   Código duplicado entre calcular_promedio_estudiante y calcular_promedio_materia
  - [ALTA]   División por cero sin controlar en promedio (python:S3518)
  - [MEDIA]  Magic numbers sin constante nombrada
  - [BAJA]   Variable declarada y no usada (python:S1481)
  
REFACTORIZADO:
  - reporte_academico() dividida en funciones pequeñas (obtener_estudiante, clasificar_notas)
"""
from typing import Optional, Tuple, List
from src.models.database import get_notas, get_estudiantes, get_materias

NOTA_MINIMA_APROBACION: float = 3.0

def es_aprobado(nota: float) -> bool:
    return nota >= NOTA_MINIMA_APROBACION


def calcular_promedio_estudiante(codigo):
    notas = [n for n in get_notas()
             if n["codigo_estudiante"] == codigo]
    if not notas:
        return 0.0
    return round(sum(n["valor"] for n in notas) / len(notas), 2)


def calcular_promedio_materia(codigo: str) -> float:
    """
    Calcula el promedio de notas de una materia.

    [DEUDA ALTA] Duplicación con calcular_promedio_estudiante.
    [DEUDA ALTA] División por cero si la materia no tiene notas.
    """
    notas = [n for n in get_notas() if n["codigo_materia"] == codigo.upper()]
    total = sum(n["valor"] for n in notas)
    # [DEUDA] ZeroDivisionError si notas está vacío
    return round(total / len(notas), 2)


def obtener_estudiante(codigo_estudiante: str) -> Optional[dict]:
    """
    Valida y retorna los datos del estudiante.
    
    Args:
        codigo_estudiante: Código del estudiante a buscar.
        
    Returns:
        dict con datos del estudiante o None si no existe.
    """
    estudiantes = get_estudiantes()
    if codigo_estudiante.upper() not in estudiantes:
        return None
    return estudiantes[codigo_estudiante.upper()]


def clasificar_notas(notas: List[dict]) -> Tuple[List[dict], List[dict]]:
    """
    Separa notas en aprobadas y reprobadas.
    
    Args:
        notas: Lista de diccionarios con información de notas.
        
    Returns:
        Tupla (aprobadas, reprobadas) con las notas clasificadas.
    """
    aprobadas = [n for n in notas if es_aprobado(n["valor"])]
    reprobadas = [n for n in notas if not es_aprobado(n["valor"])]
    return aprobadas, reprobadas


def reporte_academico(codigo_estudiante: str) -> dict:
    """
    Genera un reporte académico de un estudiante.
    
    Responsabilidades delegadas a funciones especializadas:
    - obtener_estudiante(): validación y obtención de datos
    - clasificar_notas(): separación de notas
    - calcular_promedio_estudiante(): cálculo de promedio
    
    Args:
        codigo_estudiante: Código del estudiante.
        
    Returns:
        dict con reporte académico o error si no existe.
    """
    estudiante = obtener_estudiante(codigo_estudiante)
    if not estudiante:
        return {"error": "Estudiante no encontrado"}
    
    notas = [n for n in get_notas() 
             if n["codigo_estudiante"] == codigo_estudiante.upper()]
    
    aprobadas, reprobadas = clasificar_notas(notas)
    promedio = calcular_promedio_estudiante(codigo_estudiante.upper())
    
    return {
        "estudiante": estudiante["nombre"],
        "total_notas": len(notas),
        "aprobadas": len(aprobadas),
        "reprobadas": len(reprobadas),
        "promedio": promedio,
    }

def estadisticas_globales() -> dict:
    """
    Retorna estadísticas globales del sistema.

    [DEUDA MEDIA] Lógica de negocio mezclada con acceso a datos.
    """
    notas = get_notas()
    estudiantes = get_estudiantes()
    materias = get_materias()

    # [DEUDA] División por cero si no hay notas
    promedio_global = round(sum(n["valor"] for n in notas) / len(notas), 2) if notas else 0.0

    return {
        "total_estudiantes": len(estudiantes),
        "total_materias": len(materias),
        "total_notas": len(notas),
        "promedio_global": promedio_global,
    }
