# https://docs.python.org/3/library/turtle.html

import turtle

SIZE = 50

display = turtle.Screen()

# Piece pictures drawn by me, board image from Chess.com
rookB = "black-rook.gif"
rookW = "white-rook.gif"
knightB = "black-knight.gif"
knightW = "white-knight.gif"
bishopB = "black-bishop.gif"
bishopW = "white-bishop.gif"
queenB = "black-queen.gif"
queenW = "white-queen.gif"
kingB = "black-king.gif"
kingW = "white-king.gif"
pawnB = "black-pawn.gif"
pawnW = "white-pawn.gif"
white_wins = "white-wins.gif"
black_wins = "black-wins.gif"
stalemate = "stalemate.gif"
display.addshape(rookB)
display.addshape(rookW)
display.addshape(knightB)
display.addshape(knightW)
display.addshape(bishopB)
display.addshape(bishopW)
display.addshape(queenB)
display.addshape(queenW)
display.addshape(kingB)
display.addshape(kingW)
display.addshape(pawnB)
display.addshape(pawnW)
display.addshape(white_wins)
display.addshape(black_wins)
display.addshape(stalemate)


# represents the chessboard
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.squareSize = SIZE
        self.screenSize = self.width * self.squareSize
        self.whiteTurn = True
        self.cur_piece = None
        self.piecesDic = {}  # where the coordinates of the pieces will be stored

    def end_turn(self):
        self.whiteTurn = not self.whiteTurn

    def get_piece(self, x, y):
        return self.piecesDic.get((x, y))


# used to generate a piece on the board
def piece_setup(color, shape, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    piece.shape(shape)
    piece.color = color
    piece.hasMoved = False
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    board.piecesDic[x, y] = piece
    return piece


# initialize all pieces
class Pieces:
    def __init__(self):
        self.bRook = piece_setup("black", rookB, 0, 7)
        self.bKnight = piece_setup("black", knightB, 1, 7)
        self.bBishop = piece_setup("black", bishopB, 2, 7)
        self.bQueen = piece_setup("black", queenB, 3, 7)
        self.bKing = piece_setup("black", kingB, 4, 7)
        self.bBishop2 = piece_setup("black", bishopB, 5, 7)
        self.bKnight2 = piece_setup("black", knightB, 6, 7)
        self.bRook2 = piece_setup("black", rookB, 7, 7)
        self.bPawn = piece_setup("black", pawnB, 0, 6)
        self.bPawn2 = piece_setup("black", pawnB, 1, 6)
        self.bPawn3 = piece_setup("black", pawnB,  2, 6)
        self.bPawn4 = piece_setup("black", pawnB, 3, 6)
        self.bPawn5 = piece_setup("black", pawnB, 4, 6)
        self.bPawn6 = piece_setup("black", pawnB, 5, 6)
        self.bPawn7 = piece_setup("black", pawnB, 6, 6)
        self.bPawn8 = piece_setup("black", pawnB, 7, 6)
        self.wRook = piece_setup("white", rookW, 0, 0)
        self.wKnight = piece_setup("white", knightW, 1, 0)
        self.wBishop = piece_setup("white", bishopW, 2, 0)
        self.wQueen = piece_setup("white", queenW, 3, 0)
        self.wKing = piece_setup("white", kingW, 4, 0)
        self.wBishop2 = piece_setup("white", bishopW, 5, 0)
        self.wKnight2 = piece_setup("white", knightW, 6, 0)
        self.wRook2 = piece_setup("white", rookW, 7, 0)
        self.wPawn = piece_setup("white", pawnW, 0, 1)
        self.wPawn2 = piece_setup("white", pawnW, 1, 1)
        self.wPawn3 = piece_setup("white", pawnW, 2, 1)
        self.wPawn4 = piece_setup("white", pawnW, 3, 1)
        self.wPawn5 = piece_setup("white", pawnW, 4, 1)
        self.wPawn6 = piece_setup("white", pawnW, 5, 1)
        self.wPawn7 = piece_setup("white", pawnW, 6, 1)
        self.wPawn8 = piece_setup("white", pawnW, 7, 1)

    # get position of king
    def getpos(self, color):
        if color == "white":
            return self.wKing.xcor() // SIZE, self.wKing.ycor() // SIZE
        else:
            return self.bKing.xcor() // SIZE, self.bKing.ycor() // SIZE


backgroundFix = 10
display = turtle.Screen()
board = Board()

turtle.setup(board.screenSize + backgroundFix, board.screenSize + backgroundFix)  # change window size
boardPic = "board.gif"

# to make 0,0 the origin, backgroundFix was added to fix center background
turtle.setworldcoordinates(backgroundFix, backgroundFix, board.screenSize, board.screenSize)
display.bgpic(boardPic)

# used to recenter background pic https://stackoverflow.com/questions/49086447/
# turtle-graphics-how-can-background-image-in-the-center-after-setting-the-world
canvas = display.getcanvas()
canvas.itemconfig(display._bgpic, anchor="sw")  # pylint: disable=W0212
# end of centering code

pieces = Pieces()


# generates possible diagonal moves
def diagonal_movement(x_old, y_old):
    possible_moves = []

    # used to reduce repetition
    def loops(a, b, c, d):
        i = x_old + c
        j = y_old + d
        while i * c <= a * c and j * d <= b * d:  # flipping inequality direction
            possible_moves.append((i, j))
            if board.get_piece(i, j):
                break
            i += c
            j += d

    # possible moves top right
    loops(7, 7, 1, 1)
    # possible moves top left
    loops(0, 7, -1, 1)
    # possible moves bottom left
    loops(0, 0, -1, -1)
    # possible moves bottom right
    loops(7, 0, 1, -1)
    return possible_moves


# removes a piece visually and from our dictionary
def capture(victim):
    del board.piecesDic[(victim.xcor() // SIZE, victim.ycor() // SIZE)]
    victim.hideturtle()


# Scans for non-diagonal checks from a rook or queen. If a check is found, returns which color is in check,
# otherwise returns None
def non_diagonal_check(cur_x, cur_y, cur_king):
    # used to reduce repetition
    def loops(a, b, c, d, e):
        temp_cor = [cur_x + a, cur_y + b]
        while temp_cor[e] * d >= c * d:
            if (temp_cor[0], temp_cor[1]) == cur_king:
                return board.get_piece(temp_cor[0], temp_cor[1]).color
            if board.get_piece(temp_cor[0], temp_cor[1]):
                break
            temp_cor[0] += a
            temp_cor[1] += b

    directions = {"left": [-1, 0, 0, 1, 0], "up": [0, 1, 7, -1, 1],
                  "right": [1, 0, 7, -1, 0], "down": [0, -1, 0, 1, 1]}
    for a, b, c, d, e in directions.values():
        check_found = loops(a, b, c, d, e)
        if check_found:
            return check_found


# return which color is in check, no if no one is
def check(x=-1, y=-1, color="no"):
    black_king = pieces.getpos("black")
    white_king = pieces.getpos("white")
    # king's position will be outdated if it was just moved, so we pass in the new pos in this case
    if x != -1 and y != -1 and color != "no":
        if color == "white":
            white_king = x, y
        else:
            black_king = x, y
    for x, y in board.piecesDic:
        piece = board.piecesDic[(x, y)]
        if piece.color == "white":
            cur_king = black_king
        else:
            cur_king = white_king
        if piece.shape() == pawnW:
            if (x - 1, y + 1) == black_king or (x + 1, y + 1) == black_king:
                return "black"
        if piece.shape() == pawnB:
            if (x - 1, y - 1) == white_king or (x + 1, y - 1) == white_king:
                return "white"
        # below checks horizontal and vertical for rook and queen
        if piece.shape() == rookB or piece.shape() == rookW or piece.shape() == queenB or piece.shape() == queenW:
            check_found = non_diagonal_check(x, y, cur_king)
            if check_found:
                return check_found
        # takes care of bishop and rest of Queen's moves
        if piece.shape() == bishopB or piece.shape() == bishopW or piece.shape() == queenB or piece.shape() == queenW:
            possible_moves = diagonal_movement(x, y)
            if cur_king in possible_moves:
                return board.piecesDic.get(cur_king).color
        if piece.shape() == knightB or piece.shape() == knightW:
            possible_moves = [(x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2),
                              (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2)]
            if cur_king in possible_moves:
                return board.piecesDic.get(cur_king).color
    return "no"


# white pawns move in +y direction, black pawns move in -y direction
def pawndir(pawn):
    if pawn.color == "white":
        return 1
    else:
        return -1


# returns "white" if given a black piece, and vise versa
def oppcolor(piece):
    if piece.color == "white":
        return "black"
    else:
        return "white"


# checks if user has selected a legal pawn move
# checking if a piece is blocking the movement is only done for promoting a pawn (at least in this function)
def pawnmovement(x_old, y_old, x, y, piece, captured, just_checking):
    d = pawndir(piece)  # which way is the pawn going
    if (x == x_old - 1 or x == x_old + 1) and y == y_old + d:
        # check for en passant
        if board.get_piece(x, y_old) and (board.get_piece(x, y_old).shape() == pawnW or
                                          board.get_piece(x, y_old).shape() == pawnB) \
                and board.get_piece(x, y_old).enpassantable:
            captured = board.get_piece(x, y_old)

        if captured:
            if not just_checking:  # if we aren't just checking, actually capture
                capture(captured)
            captured = None
        else:
            return None
    # I am multiplying by d because the pawn can only move up if white, and down if black
    elif (piece.hasMoved and y * d > (y_old + d) * d) or \
            (not piece.hasMoved and y * d > (y_old + (2 * d)) * d) or x != x_old or y * d < y_old * d:
        return None
    # piece.hasMoved = True
    # promoting pawn to a queen, which happens at the end of the board, at y == 0 or 7, and nothing is in the way
    if (y == 7 or y == 0) and not captured and not just_checking:
        capture(piece)  # get rid of old pawn
        if piece.color == "white":
            piece = piece_setup(piece.color, queenW, x_old, y_old)
        else:
            piece = piece_setup(piece.color, queenB, x_old, y_old)
        board.piecesDic[x_old, y_old] = piece
        return piece
    return piece


# used to temporarily move a piece to determine if a player is in check
def check_caller(x, y, piece, piecesDic, x_old, y_old):
    # if a piece is at x, y, it will be saved in og
    og = None
    if board.get_piece(x, y):
        og = board.get_piece(x, y)

    del piecesDic[x_old, y_old]
    piecesDic[x, y] = piece
    if piece.shape() == kingB or piece.shape() == kingW:
        in_check = check(x, y, piece.color)
    else:
        in_check = check()
    piecesDic[x_old, y_old] = piece
    del piecesDic[x, y]
    if og:
        piecesDic[x, y] = og
    return in_check


# can determine if the current move is possible. If just checking, nothing in game is altered (no
# pieces are moved or altered)
def move_possible(x, y, just_checking):
    x_old = board.cur_piece.xcor() // SIZE
    y_old = board.cur_piece.ycor() // SIZE
    if (x_old, y_old) == (x, y):
        board.cur_piece = None
        return 0

    # if applicable, the piece that is being captured will be stored here
    captured = board.get_piece(x, y)

    # cannot capture your own piece
    if captured and captured.color != oppcolor(board.cur_piece):
        board.cur_piece = None
        return 0

    # checks if king would be in check after move
    if check_caller(x, y, board.cur_piece, board.piecesDic, x_old, y_old) == board.cur_piece.color:
        board.cur_piece = None
        return 0

    # checks movement for every piece
    if board.cur_piece.shape() == pawnW or board.cur_piece.shape() == pawnB:
        board.cur_piece = pawnmovement(x_old, y_old, x, y, board.cur_piece, captured, just_checking)
        if not board.cur_piece:
            return 0

    if board.cur_piece.shape() == rookB or board.cur_piece.shape() == rookW:
        if x != x_old and y != y_old:
            board.cur_piece = None
            return 0
    if board.cur_piece.shape() == bishopB or board.cur_piece.shape() == bishopW:
        possible_moves = diagonal_movement(x_old, y_old)
        if (x, y) not in possible_moves:
            board.cur_piece = None
            return 0
    if board.cur_piece.shape() == queenB or board.cur_piece.shape() == queenW:
        diagonal_moves = diagonal_movement(x_old, y_old)
        if x != x_old and y != y_old and (x, y) not in diagonal_moves:
            board.cur_piece = None
            return 0
    if board.cur_piece.shape() == knightB or board.cur_piece.shape() == knightW:
        possible_moves = [(x_old + 1, y_old + 2), (x_old + 2, y_old + 1), (x_old + 2, y_old - 1),
                          (x_old + 1, y_old - 2), (x_old - 1, y_old - 2), (x_old - 2, y_old - 1),
                          (x_old - 2, y_old + 1), (x_old - 1, y_old + 2)]
        if (x, y) not in possible_moves:
            board.cur_piece = None
            return 0
        if captured and not just_checking:
            capture(captured)
    if board.cur_piece.shape() == kingB or board.cur_piece.shape() == kingW:
        # take care of castling
        if (x, y) == (x_old - 2, y_old) or (x, y) == (x_old + 2, y_old):
            if x > x_old:
                temp = 1
                sevenorzero = 7
            else:
                temp = -1
                sevenorzero = 0
            # this checks if the corresponding rook has already moved
            # also checks if any pieces are in the way
            if board.cur_piece.color == "white":
                if board.get_piece(sevenorzero, 0):
                    cur_rook = board.get_piece(sevenorzero, 0)
                    if board.get_piece(sevenorzero, 0).hasMoved:
                        board.cur_piece = None
                        return 0
                else:
                    board.cur_piece = None
                    return 0
                if sevenorzero == 7:
                    if board.get_piece(5, 0) or board.get_piece(6, 0):
                        board.cur_piece = None
                        return 0
                else:
                    if board.get_piece(1, 0) or board.get_piece(2, 0) or board.get_piece(3, 0):
                        board.cur_piece = None
                        return 0
            else:
                if board.get_piece(sevenorzero, 7):
                    cur_rook = board.get_piece(sevenorzero, 7)
                    if board.get_piece(sevenorzero, 7).hasMoved:
                        board.cur_piece = None
                        return 0
                else:
                    board.cur_piece = None
                    return 0
                if sevenorzero == 7:
                    if board.get_piece(5, 7) or board.get_piece(6, 7):
                        board.cur_piece = None
                        return 0
                else:
                    if board.get_piece(1, 7) or board.get_piece(2, 7) or board.get_piece(3, 7):
                        board.cur_piece = None
                        return 0
            # makes sure king isn't already in check, and doesn't move through check
            for i in range(2):
                if check_caller(x_old + (i * temp), y, board.cur_piece, board.piecesDic, x_old, y_old)\
                        == board.cur_piece.color:
                    board.cur_piece = None
                    return 0

            if board.cur_piece.hasMoved:
                board.cur_piece = None
                return 0
            # castling time :)
            if board.cur_piece.color == "white" and not just_checking:
                if sevenorzero == 7:
                    cur_rook.speed(5)
                    del board.piecesDic[7, 0]
                    # 275, 25
                    cur_rook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                    board.piecesDic[5, y] = cur_rook

                    board.cur_piece.speed(5)
                    del board.piecesDic[x_old, y_old]
                    # 275, 25
                    board.cur_piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                    board.piecesDic[6, y] = board.cur_piece
                else:
                    cur_rook.speed(5)
                    del board.piecesDic[0, 0]
                    # 175, 25
                    cur_rook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                    board.piecesDic[3, y] = cur_rook

                    board.cur_piece.speed(5)
                    del board.piecesDic[x_old, y_old]
                    # 275, 25
                    board.cur_piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                    board.piecesDic[x, y] = board.cur_piece
            elif not just_checking:
                if sevenorzero == 7:
                    cur_rook.speed(5)
                    del board.piecesDic[7, 7]
                    # 275, 375
                    cur_rook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                    board.piecesDic[5, y] = cur_rook

                    board.cur_piece.speed(5)
                    del board.piecesDic[x_old, y_old]
                    # 275, 25
                    board.cur_piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                    board.piecesDic[6, y] = board.cur_piece
                else:
                    cur_rook.speed(5)
                    del board.piecesDic[0, 7]
                    # 175, 375
                    cur_rook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                    board.piecesDic[3, y] = cur_rook

                    board.cur_piece.speed(5)
                    del board.piecesDic[x_old, y_old]
                    # 275, 25
                    board.cur_piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                    board.piecesDic[x, y] = board.cur_piece
            if just_checking:
                return board.cur_piece
            # castling done, so end move
            board.cur_piece = None
            board.end_turn()
            return 0

        possible_moves = [(x_old, y_old + 1), (x_old + 1, y_old + 1), (x_old + 1, y_old), (x_old + 1, y_old - 1),
                          (x_old, y_old - 1), (x_old - 1, y_old - 1), (x_old - 1, y_old), (x_old - 1, y_old + 1)]

        if (x, y) not in possible_moves:
            board.cur_piece = None
            return 0
    if board.cur_piece.shape() != knightB and board.cur_piece.shape() != knightW:
        temp_x = x_old
        temp_y = y_old
        while temp_x != x or temp_y != y:
            if temp_x < x:
                temp_x += 1
            if temp_y < y:
                temp_y += 1
            if temp_x > x:
                temp_x -= 1
            if temp_y > y:
                temp_y -= 1
            if board.get_piece(temp_x, temp_y):
                captured = board.get_piece(temp_x, temp_y)
                if x == temp_x and y == temp_y and captured.color != board.cur_piece.color \
                        and board.cur_piece.shape() != pawnB and board.cur_piece.shape() != pawnW:
                    if not just_checking:
                        capture(captured)
                else:
                    board.cur_piece = None
                    return 0
    if just_checking:
        return board.cur_piece
    for g in board.piecesDic:
        if board.piecesDic[g].shape() == pawnB:
            board.piecesDic[g].enpassantable = False
        if board.piecesDic[g].shape() == pawnW:
            board.piecesDic[g].enpassantable = False
    if (board.cur_piece.shape() == pawnB or board.cur_piece.shape() == pawnW) and (y == y_old + 2 or y == y_old - 2):
        board.cur_piece.enpassantable = True
    board.cur_piece.speed(5)
    del board.piecesDic[x_old, y_old]
    board.cur_piece.goto(25 + x * SIZE, 25 + y * SIZE)
    board.piecesDic[x, y] = board.cur_piece
    board.cur_piece.hasMoved = True
    board.cur_piece = None
    board.end_turn()
    return "success"  # returns if a move was successfully completed


def gameplay(click_x, click_y):
    click_x = click_x // SIZE
    click_y = click_y // SIZE

    if board.cur_piece:
        if not move_possible(click_x, click_y, False):  # if it was not a successful move, just end this function
            return 0
        all_moves = {}

        # looping through all coordinates and seeing what pieces can go to it
        # this is used to check for checkmate or stalemate
        for x in range(8):
            for y in range(8):
                temp_dic = board.piecesDic.copy()  # I use a temp copy to loop through so the compiler doesn't complain
                #  about the dictionary changing. It changes when the 'check_caller' function is called, but the
                # compiler doesn't know that it gets changed right back to the original dictionary in the same function.
                for px, py in temp_dic:
                    board.cur_piece = board.piecesDic[px, py]
                    if board.cur_piece.color == "white" and not board.whiteTurn:
                        board.cur_piece = None
                        continue
                    elif board.cur_piece.color == "black" and board.whiteTurn:
                        board.cur_piece = None
                        continue
                    if move_possible(x, y, True):  # if piece can go to x, y, it is stored
                        all_moves[board.cur_piece] = all_moves.get(board.cur_piece, []) + [x, y]
        if all_moves == {}:  # if no moves remain, the game is over!
            gameover = turtle.Turtle()
            if check() == "no":  # if it is a players turn and they have no legal moves left, it is stalemate
                print("stalemate")
                gameover.shape(stalemate)
            elif board.whiteTurn:  # otherwise whoever is in check and has no legal moves loses
                print("checkmate, black wins!")
                gameover.shape(black_wins)
            else:
                print("checkmate, white wins!")
                gameover.shape(white_wins)
            gameover.penup()
            gameover.speed(1)
            gameover.goto(4 * SIZE, 4 * SIZE)  # game over picture moves to center of screen
        board.cur_piece = None
    else:
        board.cur_piece = board.get_piece(click_x, click_y)  # stores the piece the player clicks on
        if not board.cur_piece:  # if the player clicked on a square with no piece
            return 0
        if board.cur_piece.color == "white" and not board.whiteTurn:  # player tried to move opponents piece
            board.cur_piece = None
        elif board.cur_piece.color == "black" and board.whiteTurn:
            board.cur_piece = None


turtle.onscreenclick(gameplay, 1)

turtle.mainloop()