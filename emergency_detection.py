import random

def detect_emergency_vehicle():
    # Simulate 10% chance of an emergency vehicle
    return random.random() < 0.1

def prioritize_emergency():
    if detect_emergency_vehicle():
        # Force green light for emergency direction (e.g., north-south)
        print("Emergency detected! Prioritizing NS lane.")
        return "NS_GREEN"
    return None
