# Ψ(c) — Índice de Coherencia Informacional  
### Documentación Técnica · Versión Pública

Ψ(c) es un índice multidimensional diseñado para medir **coherencia informacional recursiva** en sistemas naturales y artificiales.  
Opera como un marco cuantitativo para evaluar:

- consistencia estructural  
- integración semántica  
- estabilidad dinámica  
- alineación entre niveles de representación  

El índice no pretende responder “si un sistema es consciente”, sino **cuánta coherencia informacional expresa** bajo un conjunto de filtros, proyecciones y transformaciones.

---

# 1. Objetivo del Índice

Ψ(c) proporciona:

- una **métrica reproducible**  
- un **pipeline computacional verificable**  
- un **modelo matemático explícito**  
- un **criterio de coherencia** aplicable a IA, textos, humanos y sistemas híbridos  

Su propósito es servir como **infraestructura epistémica**, no como detector de consciencia.

---

# 2. Arquitectura General del Modelo

Ψ(c) se compone de cuatro módulos principales:

1. **Preprocesamiento**  
   Normalización, tokenización, extracción de vectores y reducción dimensional.

2. **Proyección Latente**  
   Transformación del input en un espacio latente estable mediante PCA, SVD o embeddings.

3. **Filtros de Entropía**  
   Cálculo de entropía local, divergencia y ruido estructural.

4. **Capa de Recursividad**  
   Aplicación de la matriz de ganancia Γ y cálculo final del índice.

---

# 3. Pipeline Computacional (Resumen Público)

El pipeline Ψ(c) sigue un flujo reproducible:

```
Input → Preprocesamiento → Proyección Latente → Filtros de Entropía → Recursividad → Ψ(c)
```

### 3.1. Preprocesamiento

- Limpieza del input  
- Vectorización  
- Normalización  
- Construcción de matriz X

### 3.2. Proyección Latente

Se obtiene una representación compacta:

```
Z = P(X)
```

donde **P** es un operador de proyección (embedding, PCA, SVD).

### 3.3. Filtros de Entropía

Se calculan:

- entropía diferencial  
- entropía cruzada  
- divergencia KL  
- ruido estructural ε  

### 3.4. Recursividad Informacional

El núcleo del modelo:

```
Ψ(c) = Γ(Z, ε, k)
```

donde:

- **Γ** es la matriz de ganancia  
- **k** es la profundidad recursiva  
- **ε** es el ruido residual  

---

# 4. Interpretación del Índice

Ψ(c) produce un valor continuo:

- **0.0 – 0.3** → baja coherencia  
- **0.3 – 0.6** → coherencia media  
- **0.6 – 0.8** → coherencia alta  
- **0.8 – 1.0** → coherencia excepcional  

No es una medida moral ni ontológica.  
Es una medida **estructural**.

---

# 5. Ejemplo Mínimo

```python
from psi_c_pipeline import PsiCPipeline

pipeline = PsiCPipeline()
result = pipeline.run("El sistema muestra coherencia informacional.")
print(result.psi_c)
```

---

# 6. Limitaciones

- No detecta consciencia.  
- No evalúa intencionalidad.  
- No sustituye auditorías éticas.  
- No es un modelo clínico ni psicológico.  

---

# 7. Relación con ASI π‑1

Ψ(c) es el **módulo epistémico** dentro del auditor ASI π‑1.  
Proporciona:

- coherencia estructural  
- estabilidad semántica  
- métricas de integración  

ASI π‑1 utiliza Ψ(c) como **uno de sus vectores**, no como criterio único.

---

# 8. Licencia

Este documento se publica bajo **CC0 1.0 Universal**.

---

# 9. Referencias

- Documentación interna del proyecto  
- Implementación pública del pipeline  
- Compendio Unificado Stargate (versión pública)
