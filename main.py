import argparse
import random

olympus = [
    "Estates",
    "Bonsai Plaza",
    "Arcadia Supercarrier",
    "Turbine",
    "Docks",
    "Elysium",
    "Energy Depot",
    "Farmstead",
    "Grow Towers",
    "Golden Gardens",
    "Hammond Labs",
    "Hydroponics",
    "Orbital Cannon",
    "Fight night",
    "Phase Runner",
    "Rift",
    "Solar array",
    "Oasis"
]

kings = [
    "Airbase",
    "Capacitor",
    "Artillery",
    "Broken Relay",
    "Bunker",
    "Cage",
    "Caustic Treatment",
    "Crashed Ship",
    "Crash Site",
    "Containment",
    "Crytpo's Map Room",
    "Gauntlet",
    "Salvage",
    "Market",
    "The Pit",
    "Labs",
    "Swamps",
    "The Rig",
    "Repulsor"
]

storm_point = [
    "Highpoint",
    "North Pad",
    "The Wall",
    "Lightning Rod",
    "Storm Catcher",
    "Command Center",
    "Checkpoint",
    "Cascade Falls",
    "Thunder Watch",
    "Launch Pad",
    "Antenna",
    "Cenote Cave",
    "Barometer",
    "Gale Station",
    "Fish Farms",
    "The Mill",
    "Ship Fall"
]

characters = [
    "Ash",
    "Mad Maggie",
    "Bloodhound",
    "Gibraltar",
    "Lifeline",
    "Pathfinder",
    "Wraith",
    "Bangalore",
    "Caustic",
    "Mirage",
    "Octane",
    "Wattson",
    "Crypto",
    "Revenant",
    "Loba",
    "Rampart",
    "Horizon",
    "Fuse",
    "Valkyrie",
    "Seer"
]

maps = [
    "OLYMPUS",
    "KINGS CANYON",
    "STORM POINT",
    "WORLD'S EDGE"
]

def main(map_choice, num_characters=None):
    if num_characters is not None and num_characters <= 3 and num_characters > 0:
        print("Characters:")


        for i in range(num_characters):
            char_choice = random.choice(characters)
            print("\t" + char_choice)
            characters.remove(char_choice) # to ensure we don't get any duplicates

    print("Drop Location: ")
    if map_choice == "Olympus":
        print("\t" + random.choice(olympus)) 
    elif map_choice == "Kings Canyon":
        print("\t" + random.choice(kings))
    elif map_choice == "Storm Point": 
        print("\t" + random.choice(storm_point))
    else:
        print("Invalid map selection\nMaps are: \n\tOlympus\n\tKings Canyon\n\tStorm Point")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Apex Randomizer")
    parser.add_argument('--map', type=str)
    parser.add_argument('--characters', type=int, required=False)

    args = parser.parse_args()
    if args.characters is None:
        main(args.map)
    else:
        main(args.map, args.characters)
