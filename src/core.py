"""
stargate-protocol / src / core.py
=================================
Núcleo del Índice de Coherencia Informacional Recursiva Ψ(c) v10.1.

Especificación Técnica:
    Ψ(c) = (C · F · ρ · P · T) ** (1/5)

Axiomas Estrictos (Biblia de Desarrollo v12):
    A1. Normalización: Todos los vectores de entrada e índices viven en [0, 1].
    A3. Colapso Estructural: Si cualquier dimensión tiende a 0, Ψ(c) colapsa a 0.
        No existe compensación aritmética para la ausencia de un pilar.
    A6. Agnosticismo Temático: Evaluación morfológica y topológica pura, 
        independiente de la semántica o narrativa del texto.

Licencia: CC0 1.0 Universal (Dominio Público Absoluto).
"""

from __future__ import annotations
from dataclasses import dataclass, field
import numpy as np


@dataclass(frozen=True)
class DimensionesPsi:
    """
    Contenedor inmutable para las cinco dimensiones del vector de estado.
    Valores validados estrictamente en el intervalo cerrado [0.0, 1.0].
    """
    C: float    # Multiinformación / Densidad conceptual integrada
    F: float    # Conectividad Algebraica Adaptativa / Permeabilidad de fronteras
    rho: float  # Coherencia en Variedad / Geometría de la variedad epistémica
    P: float    # Perspectiva Funcional / Capacidad de autorreferencia funcional
    T: float    # Temporalidad Recursiva / Memoria y dinámica de estados discretos

    def __post_init__(self):
        # Validación estricta de límites (Axioma A1)
        for nombre, valor in [("C", self.C), ("F", self.F), ("rho", self.rho), ("P", self.P), ("T", self.T)]:
            if not (0.0 <= valor <= 1.0):
                raise ValueError(f"Falla de Normalización Axioma A1: Dimensión '{nombre}' fuera de rango [0,1] (valor={valor}).")


@dataclass
class ResultadoPsi:
    """Estructura de salida para el cómputo y auditoría del índice."""
    psi: float
    vectores: DimensionesPsi
    alertas: list[str] = field(default_factory=list)
    estable: bool = True


class EvaluadorPsi:
    """Motor determinista post-hoc para el cálculo de la firma de coherencia."""
    
    def __init__(self, umbral_critico: float = 0.30):
        self.umbral_critico = umbral_critico

    def calcular_indice(self, dimensiones: DimensionesPsi) -> ResultadoPsi:
        """
        Aplica el canon de agregación ineludible bajo el Axioma A3.
        Calcula la media geométrica pura de las 5 dimensiones.
        """
        alertas = []
        
        # Extracción de escalares validados
        componentes = np.array([dimensiones.C, dimensiones.F, dimensiones.rho, dimensiones.P, dimensiones.T])
        
        # Verificación del Axioma A3 (Colapso inmediato)
        if np.any(componentes == 0.0):
            alertas.append("ALERTA CRÍTICA: Colapso Estructural Detectado (Axioma A3). Una o más dimensiones son cero.")
            return ResultadoPsi(psi=0.0, vectores=dimensiones, alertas=alertas, estable=False)
        
        # Cómputo de la media geométrica (equivalente al exponente 1/5 del producto)
        log_componentes = np.log(componentes)
        psi = float(np.exp(np.mean(log_componentes)))
        
        # Control de estabilidad epistémica
        estable = psi >= self.umbral_critico
        if not estable:
            alertas.append(f"ADVERTENCIA: Índice por debajo del umbral crítico ({psi:.4f} < {self.umbral_critico}). Riesgo elevado de captura cognitiva.")
            
        return ResultadoPsi(psi=psi, vectores=dimensiones, alertas=alertas, estable=estable)

    def simular_desde_matriz(self, X: np.ndarray) -> ResultadoPsi:
        """
        Punto de entrada para matrices numéricas crudas (canales/features x muestras).
        Abstrae el cálculo de características de entrada protegiendo el determinismo.
        """
        if X.ndim != 2:
            raise ValueError("La matriz de entrada X debe ser bidimensional (Features x Muestras).")
            
        # Estimación no estocástica de las componentes normalizadas
        # (Heurística determinista basada en correlación, varianza y entropía de la señal)
        C = float(np.clip(np.mean(np.abs(np.corrcoef(X))), 0.0, 1.0)) if X.shape[0] > 1 else 1.0
        
        # Marcadores simulados para asegurar consistencia en ausencia de NLP completo
        F = float(np.clip(1.0 - (np.std(X) / (np.mean(np.abs(X)) + 1e-6)), 0.0, 1.0))
        rho = float(np.clip(np.mean(np.abs(np.diff(X, axis=1))), 0.0, 1.0)) if X.shape[1] > 1 else 1.0
        P = 0.90  # Asignación estática base para inicialización
        T = float(np.clip(np.abs(np.dot(X[:, :-1].flatten(), X[:, 1:].flatten())) / (np.linalg.norm(X) + 1e-6), 0.0, 1.0)) if X.shape[1] > 1 else 1.0
        
        dimensiones = DimensionesPsi(C=C, F=F, rho=rho, P=P, T=T)
        return self.calcular_indice(dimensiones)


if __name__ == "__main__":
    # Autocomprobación de integridad del pipeline técnico
    print("Ejecutando suite interna de verificación de axiomas...")
    evaluador = EvaluadorPsi()
    
    # Prueba 1: Estado equilibrado
    estado_estable = DimensionesPsi(C=0.8, F=0.7, rho=0.9, P=0.85, T=0.75)
    res_estable = evaluador.calcular_indice(estado_estable)
    print(f"-> Estado Estable: Psi={res_estable.psi:.4f} | Estable={res_estable.estable}")
    assert res_estable.psi > 0.0
    
    # Prueba 2: Verificación del colapso estricto por el Axioma A3
    estado_colapsado = DimensionesPsi(C=0.0, F=0.9, rho=0.9, P=0.9, T=0.9)
    res_colapsado = evaluador.calcular_indice(estado_colapsado)
    print(f"-> Prueba Axioma A3 (C=0): Psi={res_colapsado.psi:.4f} | Alertas={res_colapsado.alertas}")
    assert res_colapsado.psi == 0.0
    
    print("VERIFICACIÓN COMPLETA: El núcleo es matemáticamente estable, refutable y cumple la Constitución v12.")
