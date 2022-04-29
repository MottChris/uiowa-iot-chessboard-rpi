## Input String
#  --------------
# r n b q k b n r
# p p p p p p p p
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# P P P P P P P P
# R N B Q K B N R

# output string
# rnbqkbnrpppppppp................................PPPPPPPPRNBQKBNR
# This representation is important because we can select certain squares 
#   through integer / modular math:
#   
def clean_board_str(board_str):
  cleaned_str = board_str.replace(" ", "")
  cleaned_str = cleaned_str.replace("\n", "")

  return cleaned_str

def testPrint():
    print("Hello world")
    return

# Input node int as number between 0 - 288 (i think 288)
def node_hasPiece(nodeNum, cleaned_game_str):
  # ensure inputted node spot is piece eligable
  cleaned_str = cleaned_game_str[::-1]
  if nodeNum // 16 % 2 == 1 and nodeNum % 16 % 2 == 1:
    i = nodeNum // 16 // 2
    j = (16 - (nodeNum % 16)) // 2
    print(f'{i},{j}')

    # if there is no peice on the spot, return false
    if(cleaned_str[i * 7 + j] == '.'):
      return False
    else:
      #print(f"Piece was found on : ({i}, {j}), n = {nodeNum} char = {cleaned_game_str}")
      return True
  else: 
    return False


def UCItoNodeNums(uciMove):
  translateDict = {'a' : 0,
                 'b' : 1,
                 'c' : 2,
                 'd' : 3,
                 'e' : 4,
                 'f' : 5,
                 'g' : 6,
                 'h' : 7}
  #print(translateDict)
  count = 1
  nodeNumFrom = 0
  nodeNumTo = 0
  for char in uciMove:
    if count == 1: # add j (file) value
      nodeNumFrom += translateDict[char] * 2 + 1
    elif count == 2: # add rank portion to value
      nodeNumFrom += (int(char) * 2 - 1) * 17
    elif count == 3:
      nodeNumTo += translateDict[char] * 2 + 1
    elif count == 4:
      nodeNumTo += (int(char) * 2 - 1) * 17

    count += 1
  return nodeNumFrom, nodeNumTo

