"""
Quantitative Sensory Testing (QST) & Cutaneous Thermal Threshold Engine.
Provides deterministic, zero-dependency modeling of warm detection threshold (WDT), cold detection threshold (CDT),
heat/cold pain thresholds, thermal sensory limen (TSL), and unmyelinated C-fiber / A-delta small fiber integrity.
"""

from typing import Dict, Any, List, Optional


class CutaneousThermalQSTClient:
    """
    Deterministic client for calculating Quantitative Sensory Testing (QST) thermal thresholds.
    Assesses unmyelinated C-fibers (warmth), thinly myelinated A-delta fibers (cold),
    and nociceptive thermal pain limits to detect small fiber neuropathy (SFN) and thermal allodynia.
    """

    def __init__(self):
        pass

    def evaluate_thermal_thresholds(
        self,
        warm_detection_temp_c: float,
        cold_detection_temp_c: float,
        heat_pain_temp_c: float = 45.0,
        cold_pain_temp_c: float = 14.0,
        baseline_temp_c: float = 32.0,
        test_location: str = "THENAR_EMINENCE"
    ) -> Dict[str, Any]:
        """
        Calculates Thermal Sensory Limen TSL = WDT - CDT (in deg C).
        Normative values at baseline 32.0 deg C:
        - WDT: 33.5 - 37.0 deg C
        - CDT: 28.5 - 31.0 deg C
        - TSL: 3.5 - 7.5 deg C
        - HPT: 42.5 - 48.0 deg C
        - CPT: 8.0 - 18.0 deg C
        """
        if warm_detection_temp_c <= cold_detection_temp_c:
            return {"error": "Warm detection temperature must exceed cold detection temperature"}

        tsl_deg_c = round(warm_detection_temp_c - cold_detection_temp_c, 2)
        loc = test_location.upper()

        # Neuro-Thermal Small Fiber Score (0 - 100):
        # TSL <= 6.5 deg C with normal pain thresholds -> 90 - 100
        # TSL > 12.0 deg C -> < 50
        score = 80.0
        if tsl_deg_c <= 6.0:
            score += 15.0
        elif tsl_deg_c <= 8.5:
            score += 5.0
        elif tsl_deg_c > 13.0:
            score -= 35.0
        elif tsl_deg_c > 10.0:
            score -= 20.0

        if heat_pain_temp_c < 39.0:
            # Heat hyperalgesia
            score -= 25.0
        elif 43.0 <= heat_pain_temp_c <= 48.0:
            score += 5.0

        final_score = round(min(100.0, max(5.0, score)), 1)

        is_hyperalgesic = heat_pain_temp_c < 40.0 or cold_pain_temp_c > 24.0

        if final_score >= 85.0 and not is_hyperalgesic:
            tier = "NORMAL_THERMAL_SENSORY_PERCEPTION"
            interp = f"Preserved delicate thermal discrimination (TSL {tsl_deg_c} deg C, WDT {warm_detection_temp_c} deg C, CDT {cold_detection_temp_c} deg C) at {loc}; intact C-fiber and A-delta sensory pathways."
            guidance = "Optimal small-fiber thermosensory function. Healthy autonomic vasoregulation and microvascular reflex."
        elif is_hyperalgesic:
            tier = "THERMAL_HYPERALGESIA_ALLODYNIA"
            interp = f"Premature pain threshold (Heat pain {heat_pain_temp_c} deg C or Cold pain {cold_pain_temp_c} deg C); indicates peripheral nociceptive sensitization."
            guidance = "Thermal hypersensitivity detected. Avoid extreme temperature exposure, hot baths, and consult neurology."
        elif tsl_deg_c <= 9.5:
            tier = "MILD_SMALL_FIBER_ATTENUATION"
            interp = f"Subtle widening of thermal sensory limen (TSL {tsl_deg_c} deg C); mild thermal threshold blunting."
            guidance = "Early small-fiber slowing. Optimize glycemic variability, ensure B-vitamin status, and limit cold drafts."
        else:
            tier = "SIGNIFICANT_SMALL_FIBER_NEUROPATHY"
            interp = f"Severe elevation in thermal detection threshold (TSL {tsl_deg_c} deg C > 10 deg C); marked loss of intraepidermal C and A-delta nerve fiber endings."
            guidance = "Small fiber neuropathy pattern detected. Institute strict thermal safety precautions against burns and seek specialized neurological evaluation."

        return {
            "test_location": loc,
            "baseline_temperature_deg_c": baseline_temp_c,
            "warm_detection_temp_deg_c": warm_detection_temp_c,
            "cold_detection_temp_deg_c": cold_detection_temp_c,
            "thermal_sensory_limen_tsl_deg_c": tsl_deg_c,
            "heat_pain_temp_deg_c": heat_pain_temp_c,
            "cold_pain_temp_deg_c": cold_pain_temp_c,
            "small_fiber_score": final_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
