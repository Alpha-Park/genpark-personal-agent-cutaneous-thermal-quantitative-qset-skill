---
name: genpark-personal-agent-cutaneous-thermal-quantitative-qset-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Quantitative Sensory Testing (QST) thermal detection thresholds, thermal sensory limen (TSL), and small-fiber neuropathy.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Quantitative Sensory Testing (QST) Thermal Threshold Skill

A sovereign personal agent capability for assessing unmyelinated C-fibers (warmth detection), thinly myelinated A-delta fibers (cold detection), and calculating the Thermal Sensory Limen (TSL).

## Core Capabilities
- **Thermal Sensory Limen (TSL)**: Calculates the differential span ($WDT - CDT$) between warmth and cold perception.
- **Small-Fiber Neuropathy Gating**: Detects early loss of epidermal thermosensory nerve endings before large-fiber involvement.
- **Thermal Allodynia Detection**: Identifies paradoxical heat/cold hyperalgesia linked to central sensitization.
- **Environmental Thermal Ergonomics**: Prescribes room temperature corridors and hot/cold contrast therapy parameters.

## Fast Invocation
```python
from client import CutaneousThermalQSTClient

client = CutaneousThermalQSTClient()
res = client.evaluate_thermal_thresholds(
    warm_detection_temp_c=35.4,
    cold_detection_temp_c=29.6
)
print("TSL Limen:", res["thermal_sensory_limen_tsl_deg_c"], "deg C")
print("Small Fiber Score:", res["small_fiber_score"])
```
