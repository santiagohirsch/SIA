import sys
from classes.SokobanUtils import SokobanUtils
from classes.State import State
from algorithms.DFS import DFS
from algorithms.BFS import BFS
from algorithms.LocalGreedy import LocalGreedy

if __name__ == "__main__":
    # Set algorithm and map as None
    options = {'algorithm': None, 'map': None}

    # Run through params to find algorithm and map
    i = 1
    while i < len(sys.args):
        if sys.args[i] == '-a' or sys.args[i] == 'algorithm':
            options['algorithm'] = sys.args[i+1]
        elif sys.args[i] == '-m' or sys.args[i] == 'map':
            options['map'] = sys.args[i+1]
        i += 2

    # Check if parameters where received
    if options['algorithm'] is None or options['map'] is None:
        print("Program was executed incorrectly please check readme file for instructions.")
        exit(1)
    
    # find map file
    try:
        with open(options['map'], 'r') as file:
            sokoban_board = file.read()
    except FileNotFoundError:
        print(f"Error: Map {sokoban_board} not found.")

    # find algorithm file
    try:
        with open(options['algorithm'], 'r') as file:
            algorithm = file.read()
    except FileNotFoundError:
        print(f"Error: Algorithm {algorithm} not found.")

    parsed_positions = SokobanUtils.parse_sokoban_board(sokoban_board)

    print("Wall positions:", parsed_positions.get('wall', []))
    print("Player position:", parsed_positions.get('player', []))
    print("Goal positions:", parsed_positions.get('goal', []))
    print("Box positions:", parsed_positions.get('box', []))
    print("Box on goal positions:", parsed_positions.get('box_positio', []))
    walls = parsed_positions.get('wall', [])
    blanks = parsed_positions.get('blank', [])
    boxes = parsed_positions.get('box', [])
    player = parsed_positions.get('player', [])[0]
    goals = parsed_positions.get('goal', [])
    deadlocks = SokobanUtils.get_deadlocks(walls, blanks)
    print("Deadlock positions:", deadlocks)

    # BFS.search(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))
    LocalGreedy.local_greedy(State(set(boxes), set(walls), player, set(goals), set(deadlocks)))