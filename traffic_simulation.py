import os
import sys
import optparse
import random
from sumolib import checkBinary
import traci

def simulate_traffic():
    # SUMO configuration
    sumo_binary = checkBinary('sumo')
    config_file = os.path.join('sumo_config', 'simple_map.sumocfg')
    
    traci.start([sumo_binary, "-c", config_file])
    
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        
        # Simulate random traffic density (replace with SUMO data)
        vehicles_north = traci.edge.getLastStepVehicleNumber("north_in")
        vehicles_south = traci.edge.getLastStepVehicleNumber("south_in")
        vehicles_east = traci.edge.getLastStepVehicleNumber("east_in")
        vehicles_west = traci.edge.getLastStepVehicleNumber("west_in")
        
        # Adjust traffic lights based on density (logic below)
        adjust_traffic_lights(vehicles_north, vehicles_south, vehicles_east, vehicles_west)
    
    traci.close()

def adjust_traffic_lights(north, south, east, west):
    # Simple algorithm: prioritize lane with higher density
    total_ns = north + south
    total_ew = east + west
    
    if total_ns > total_ew:
        traci.trafficlight.setPhase("intersection_0", 0)  # Green for NS
    else:
        traci.trafficlight.setPhase("intersection_0", 2)  # Green for EW

if __name__ == "__main__":
    simulate_traffic()
