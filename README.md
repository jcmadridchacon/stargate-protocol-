# EpistemicEngine v10.1: Post-Hoc Regularization & Linguistic Topology Pipeline for Cognitive Closure Detection in Large Language Models

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

## Overview

`EpistemicEngine` is an open-source, zero-telemetry computational pipeline designed to audit institutional frameworks, regulatory texts, and Large Language Model (LLM) alignment profiles (e.g., RLHF bias) through dynamic tension fields. 

Unlike traditional Natural Language Processing (NLP) metrics that evaluate static semantic distribution or scalar coherence, this framework models text as a discrete-time state trajectory across five orthogonal, bounded dimensions. The unifications are governed by a geometric mean aggregation law, featuring a mathematical structural collapse axiom ($A_3$) where the degradation of a single core metric zeroes the global integration index.

## Core Architecture & Mathematical Framework

The system maps textual features into a normalized multidimensional space $[0, 1]^5$ defined by the following variables:

1. **Multi-Information ($C$):** Quantifies conceptual density and semantic integration via Relative Entropy reduction ($D_{KL}$).
2. **Adaptive Algebraic Connectivity ($F$):** Evaluates boundary permeability and structural resilience against adversarial counter-arguments.
3. **Coherence in Variety ($\rho$):** Measures the internal state variety topology utilizing the Wasserstein Distance metric.
4. **Functional Perspective ($P$):** Computes post-hoc self-observation operators and meta-evaluative critical density.
5. **Recursive Temporality ($T$):** Tracks historical memory coupling and transient state acouplements.

### The Aggregation Law (Axioma $A_3$)

The unified index $\Psi(c)$ is defined as:

$$\Psi(c) = \left( C \cdot F \cdot \rho \cdot P \cdot T \right)^{\frac{1}{5}}$$

**Axiom of Collapse ($A_3$):** $$\text{If } \exists \, x \in \{C, F, \rho, P, T\} = 0 \implies \Psi(c) = 0$$

No excess in conceptual density ($C$) or perspective ($P$) can compensate for an absolute failure in adaptive boundary connectivity ($F$).

---

## Repository Structure

```text
epistemic-engine/
│
├── src/
│   ├── __init__.py
│   ├── core.py              # Main EpistemicEngine core and A3 mathematical logic
│   └── extractors.py        # Post-hoc NLP feature parsers (Entropy, Wasserstein)
│
├── tests/
│   ├── test_stability.py    # Unit tests for geometric constraints and bounds
│   └── test_security.py     # Calibration and dynamic weight attenuation verifications
│
├── requirements.txt         # Minimum deterministic dependencies
├── README.md                # Technical documentation
└── LICENSE                  # CC0 1.0 Universal Public Domain Dedication
