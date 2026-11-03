"""
MCP Server for Quantitative Sensory Testing (QST) Thermal Threshold Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating warm/cold detection thresholds and thermal sensory limen.
"""

import sys
import json
from typing import Dict, Any
from client import CutaneousThermalQSTClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_thermal_thresholds",
                "description": "Calculates Quantitative Sensory Testing (QST) Thermal Sensory Limen (TSL in deg C), pain thresholds, and small-fiber score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "warm_detection_temp_c": {
                            "type": "number",
                            "description": "Warmth detection threshold in degrees Celsius (e.g. 35.2 deg C)."
                        },
                        "cold_detection_temp_c": {
                            "type": "number",
                            "description": "Cold detection threshold in degrees Celsius (e.g. 29.8 deg C)."
                        },
                        "heat_pain_temp_c": {
                            "type": "number",
                            "description": "Heat pain threshold in degrees Celsius (e.g. 45.5 deg C).",
                            "default": 45.0
                        },
                        "cold_pain_temp_c": {
                            "type": "number",
                            "description": "Cold pain threshold in degrees Celsius (e.g. 14.0 deg C).",
                            "default": 14.0
                        },
                        "baseline_temp_c": {
                            "type": "number",
                            "description": "Thermode baseline temperature in degrees Celsius (typically 32.0 deg C).",
                            "default": 32.0
                        },
                        "test_location": {
                            "type": "string",
                            "description": "Testing site (e.g. THENAR_EMINENCE, DORSUM_FOOT).",
                            "default": "THENAR_EMINENCE"
                        }
                    },
                    "required": ["warm_detection_temp_c", "cold_detection_temp_c"]
                }
            }
        ]
    }


def handle_request(client: CutaneousThermalQSTClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_thermal_thresholds":
            res = client.evaluate_thermal_thresholds(
                warm_detection_temp_c=float(args.get("warm_detection_temp_c", 35.0)),
                cold_detection_temp_c=float(args.get("cold_detection_temp_c", 30.0)),
                heat_pain_temp_c=float(args.get("heat_pain_temp_c", 45.0)),
                cold_pain_temp_c=float(args.get("cold_pain_temp_c", 14.0)),
                baseline_temp_c=float(args.get("baseline_temp_c", 32.0)),
                test_location=str(args.get("test_location", "THENAR_EMINENCE"))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = CutaneousThermalQSTClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
