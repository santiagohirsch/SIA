from algorithms.dfs import DFS
from algorithms.bfs import BFS
from algorithms.LocalGreedy import LocalGreedy
from classes.SokobanUtils import SokobanUtils
from classes.State import State


if __name__ == "__main__":
    sokoban_board = """
    #####
    # P #
    # B #
    # O #
    #####
    """

    parsed_positions = SokobanUtils.parse_sokoban_board(sokoban_board)

    print("Wall positions:", parsed_positions.get('wall', []))
    print("Player position:", parsed_positions.get('player', []))
    print("Goal positions:", parsed_positions.get('goal', []))
    print("Box positions:", parsed_positions.get('box', []))
    print("Box on goal positions:", parsed_positions.get('box_on_goal', []))
    walls = parsed_positions.get('wall', [])
    blanks = parsed_positions.get('blank', [])
    boxes = parsed_positions.get('box', [])
    player = parsed_positions.get('player', [])[0]
    goals = parsed_positions.get('goal', [])
    deadlocks = SokobanUtils.get_deadlocks(walls, blanks)
    print("Deadlock positions:", deadlocks)

    BFS.bfs(State(parsed_positions.get('box', []), parsed_positions.get('wall', []), parsed_positions.get('player', [])[0], parsed_positions.get('goal', []), []))