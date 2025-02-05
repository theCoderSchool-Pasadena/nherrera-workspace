player = 1
marking = ""
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
gamewon = False


def placeMark(marking, board, xindex, yindex):
  board[xindex][yindex] = marking


def checkwin(board):
  global gamewon
  if board[0][0] == board[0][1] and board[0][1] == board[0][
      2] and board[0][0] != '-':
    print("THE waffle house has found its new host")
    return
  elif board[1][0] == board[1][1] and board[1][1] == board[1][
      2] and board[1][0] != '-':
    print("smol baby won")
    return
  elif board[2][0] == board[2][1] and board[2][1] == board[2][
      2] and board[2][0] != '-':
    print(
      "legend of zelda tears of the kingdom ultimate deluxe ultra oled switch with macaroni and cheese special limited edition gluten free fat free water free  pain free with screen protector and ultra mega deluxe pro controller mega jumbo dress with tassels"
    )
    gamewon = True
    return
  elif board[0][0] == board[1][0] and board[1][0] == board[2][
      0] and board[0][0] != '-':
    print(
      "james shapiro fhkjffhf sajgshghsfhsdgsahjfsdjgfsadejhfsjfsdfsdjhshdfhwshag fjhsdgahjgsdhdghjsdghjsgjsdgjhsgfhsjgshjgfhjdsf ghsjdfghfjgdhjfsagjhsdghfsgdfsajhgksdhjfgsajgakhjhfgsafhjsdgahgsdafjgsjhdfjhdsgfahfgfhjfshfkgfkjaghakfhgafgsjgajfajfhgjasdhghfjkgfhjafghjfgjhfgdsjhfhafgshfgjshjgsdajfhsjdfasj"
    )
    gamewon = True
    return
  elif board[0][1] == board[1][1] and board[1][1] == board[2][
      1] and board[0][1] != '-':
    print(" mama mia baby got some diarihea")
    gamewon = True
    return
  elif board[0][2] == board[1][2] and board[1][2] == board[2][
      2] and board[0][2] != '-':
    print(
      "legend of zelda tears of the kingdom ultimate deluxe ultra oled switch with macaroni and cheese special limited edition gluten free fat free water free  pain free with screen protector and ultra mega deluxe pro controller mega jumbo dress with tassels"
    )
    gamewon = True
    return
  elif board[0][0] == board[1][1] and board[1][1] == board[2][
      2] and board[0][0] != '-':
    print(" food is food")
    gamewon = True
    return
  elif board[0][2] == board[1][1] and board[1][1] == board[2][
      0] and board[0][2] != '-':
    print(" khdfhdsjffdhsjfkdsjhsdkjf jdhjfhsfsjfhskjjsdkhgksjdhj")
    gamewon = True
    return
  elif board[0][0] != "-" and board[0][1] != "-" and board[0][
      2] != "-" and board[1][0] != "-" and board[1][1] != "-" and board[1][
        2] != "-" and board[2][0] != "-" and board[2][1] != "-" and board[2][
          2] != "-" and gamewon == False:
    print("stalemate")


print("Welcome to tictactoe")
while gamewon != True:
  for row in board:
    for i in row:
      print(i, end=" ")
    print()
  print("player: " + str(player) + "'s turn")
  ind = input("what x do you want to pick? ")
  ind = int(ind)
  gi = input("what y do you want to pick? ")
  gi = int(gi)
  if player == 1:
    marking = "X"
    placeMark(marking, board, ind, gi)
    player += 1
  elif player == 2:
    marking = "O"
    placeMark(marking, board, ind, gi)
    player -= 1
  checkwin(board)
