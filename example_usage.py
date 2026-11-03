"""
Example Usage: Quantitative Sensory Testing (QST) Thermal Thresholds.
Demonstrates non-invasive calculation of Thermal Sensory Limen (TSL) and small-fiber evaluation.
"""

from client import CutaneousThermalQSTClient


def main():
    client = CutaneousThermalQSTClient()
    print("=== Quantitative Sensory Testing (QST) Thermal Demo ===")

    # Test Case 1: Healthy normal thermal perception (Thenar eminence)
    res1 = client.evaluate_thermal_thresholds(
        warm_detection_temp_c=35.4,
        cold_detection_temp_c=29.6,
        heat_pain_temp_c=45.8,
        cold_pain_temp_c=12.5,
        test_location="THENAR_EMINENCE"
    )
    print("\nTest Case 1: Healthy Thermal Sensory Limen (Hand)")
    print(f"  Warm Detection: {res1['warm_detection_temp_deg_c']} deg C | Cold Detection: {res1['cold_detection_temp_deg_c']} deg C")
    print(f"  Thermal Sensory Limen (TSL): {res1['thermal_sensory_limen_tsl_deg_c']} deg C")
    print(f"  Heat Pain: {res1['heat_pain_temp_deg_c']} deg C | Cold Pain: {res1['cold_pain_temp_deg_c']} deg C")
    print(f"  Small Fiber Score: {res1['small_fiber_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Small fiber neuropathy / widened thermal sensory limen
    res2 = client.evaluate_thermal_thresholds(
        warm_detection_temp_c=41.5,
        cold_detection_temp_c=24.0,
        heat_pain_temp_c=48.5,
        cold_pain_temp_c=6.0,
        test_location="DORSUM_FOOT"
    )
    print("\nTest Case 2: Small Fiber Neuropathy Pattern (Dorsum Foot)")
    print(f"  TSL: {res2['thermal_sensory_limen_tsl_deg_c']} deg C")
    print(f"  Small Fiber Score: {res2['small_fiber_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
