# Quantitative Sensory Testing (QST) Thermal Threshold Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Quantitative Sensory Testing (QST) thermal thresholds, Thermal Sensory Limen (TSL), and small-fiber neuropathy.

```mermaid
flowchart TD
    Thermode["Peltier Thermode Dynamic Temperature Ramp (1 deg C/s)"] --> ThresholdCapture["Perception Trigger: WDT, CDT, HPT, CPT"]
    ThresholdCapture --> TSL_Math["Thermal Sensory Limen (TSL = WDT - CDT)"]
    TSL_Math --> FiberScore["Small-Fiber C / A-Delta Neuropathy Engine"]
    FiberScore --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **German Neurological QST Standards (DFNS)**: Implements validated equations for thermal sensory limen and pain thresholds.
- **Small-Fiber Neuropathy & Allodynia Screening**: Sensitive detection of intraepidermal nerve fiber density decline.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CutaneousThermalQSTClient

client = CutaneousThermalQSTClient()
result = client.evaluate_thermal_thresholds(
    warm_detection_temp_c=35.4,
    cold_detection_temp_c=29.6
)
print("Thermal Sensory Limen:", result["thermal_sensory_limen_tsl_deg_c"], "deg C")
print("Classification:", result["classification"])
```

## License
Apache-2.0
