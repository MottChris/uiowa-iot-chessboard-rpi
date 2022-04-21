
import chess
import time
import sys
import dijkstar as djk
import helper_function as hf
import Graph

def getNodeCoordsStr(node):
    return f'{node % 17},{node // 17}'

board = chess.Board()
## View Legal Moves
board.legal_moves

print(board)
board = chess.Board()

for i in range(10):
  
  print(board)
  legal_moves = str(board.legal_moves)
  print(str(board.legal_moves))
  # User Move
  move = input("Make white move: ")
  board.push_san(move)
  # populate graph with game state after user moves

  time.sleep(1)


  print(str(legal_moves[1]))
  # populate the graph with new game state
  graph = djk.Graph()
  cleaned_str = hf.clean_board_str(str(board))
  print(f"cleaned str{cleaned_str}")
  
  graph = Graph.create_graph(graph, cleaned_str)
  time.sleep(1)

  legal_moves_ai = list(board.legal_moves)
  #print(f"Move: {legal_moves_ai}")
  board.push_uci(str(legal_moves_ai[1]))
  # get node nums for the move
  fromNode, tonNode =  hf.UCItoNodeNums(str(legal_moves_ai[1]))
  path = djk.find_path(graph, fromNode, tonNode)
  print(path.nodes)
  print("move: " + getNodeCoordsStr(path.nodes[0]))
  print("RAISE MAGNET")
  for node in path.nodes[1:]:
      print("move: " + getNodeCoordsStr(node))

  print("LOWER MAGNET")


  # Generate path of nodes for that movement