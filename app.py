#!/usr/bin/env python3
import chess
import time
import sys
import dijkstar as djk
import helper_function as hf
import Graph

import serial
import time

# Arduino serial connection
if __name__ == '__main__':
 ser = serial.Serial('/dev/ttyACM0', 9600)
 ser.reset_input_buffer()

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

  command_bytes = str.encode("M" + getNodeCoordsStr(path.nodes[0]))
  ser.write(command_bytes + b"\n")
  print("M" + getNodeCoordsStr(path.nodes[0]))
  
  # wait for response from serial comm.
  tdata = ser.read().decode("utf-8")  
  data_left = ser.inWaiting()  # Get the number of characters ready to be read
  tdata += ser.read(data_left).decode("utf-8")
  print(f'{tdata} received.')

  # raise magnet up to the board
  command_bytes = str.encode("S1")
  ser.write(command_bytes + b"\n")
  print("S1")
  
  # wait for response
  tdata = ser.read().decode("utf-8")  
  data_left = ser.inWaiting()  # Get the number of characters ready to be read
  tdata += ser.read(data_left).decode("utf-8")
  print(f'{tdata} received.')

  # loop through the rest of the moves
  for node in path.nodes[1:]:
      print("M" + getNodeCoordsStr(node))
      command_bytes = str.encode("M" + getNodeCoordsStr(path.nodes[0]))
      ser.write(command_bytes + b"\n")

      tdata = ser.read().decode("utf-8")  
      data_left = ser.inWaiting()  # Get the number of characters ready to be read
      tdata += ser.read(data_left).decode("utf-8")
      print(f'{tdata} received.')

  print("S0")
  command_bytes = str.encode("S0")
  ser.write(command_bytes + b"\n")

  tdata = ser.read().decode("utf-8")  
  data_left = ser.inWaiting()  # Get the number of characters ready to be read
  tdata += ser.read(data_left).decode("utf-8")
  print(f'{tdata} received.')


  # Generate path of nodes for that movement