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

piecesDic = {}

# represents the chessboard
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.squareSize = SIZE
        self.screenSize = self.width * self.squareSize

    def get_piece(self, x, y):
        return piecesDic.get((x, y))


def rook(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(rookB)
    else:
        piece.shape(rookW)
    piece.color = color
    piece.hasMoved = False
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


def knight(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(knightB)
    else:
        piece.shape(knightW)
    piece.color = color
    piece.hasMoved = None  # Doesn't matter, placeholder
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


def bishop(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(bishopB)
    else:
        piece.shape(bishopW)
    piece.color = color
    piece.hasMoved = None  # Doesn't matter, placeholder
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


def queen(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(queenB)
    else:
        piece.shape(queenW)
    piece.color = color
    piece.hasMoved = None  # Doesn't matter, placeholder
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


def king(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(kingB)
    else:
        piece.shape(kingW)
    piece.color = color
    piece.hasMoved = False
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


def pawn(color, x, y):
    piece = turtle.Turtle()
    piece.speed(0)
    if color == "black":
        piece.shape(pawnB)
    else:
        piece.shape(pawnW)
    piece.color = color
    piece.hasMoved = False
    piece.enpassantable = False
    piece.penup()
    piece.goto(25 + x * SIZE, 25 + y * SIZE)
    piecesDic[x, y] = piece
    return piece


# initialize all pieces
class Pieces:
    def __init__(self):
        self.bRook = rook("black", 0, 7)
        self.bKnight = knight("black", 1, 7)
        self.bBishop = bishop("black", 2, 7)
        self.bQueen = queen("black", 3, 7)
        self.bKing = king("black", 4, 7)
        self.bBishop2 = bishop("black", 5, 7)
        self.bKnight2 = knight("black", 6, 7)
        self.bRook2 = rook("black", 7, 7)
        self.bPawn = pawn("black", 0, 6)
        self.bPawn2 = pawn("black", 1, 6)
        self.bPawn3 = pawn("black", 2, 6)
        self.bPawn4 = pawn("black", 3, 6)
        self.bPawn5 = pawn("black", 4, 6)
        self.bPawn6 = pawn("black", 5, 6)
        self.bPawn7 = pawn("black", 6, 6)
        self.bPawn8 = pawn("black", 7, 6)
        self.wRook = rook("white", 0, 0)
        self.wKnight = knight("white", 1, 0)
        self.wBishop = bishop("white", 2, 0)
        self.wQueen = queen("white", 3, 0)
        self.wKing = king("white", 4, 0)
        self.wBishop2 = bishop("white", 5, 0)
        self.wKnight2 = knight("white", 6, 0)
        self.wRook2 = rook("white", 7, 0)
        self.wPawn = pawn("white", 0, 1)
        self.wPawn2 = pawn("white", 1, 1)
        self.wPawn3 = pawn("white", 2, 1)
        self.wPawn4 = pawn("white", 3, 1)
        self.wPawn5 = pawn("white", 4, 1)
        self.wPawn6 = pawn("white", 5, 1)
        self.wPawn7 = pawn("white", 6, 1)
        self.wPawn8 = pawn("white", 7, 1)

    # get position of king
    def getpos(self, color):
        if color == "white":
            return self.wKing.xcor() // SIZE, self.wKing.ycor() // SIZE
        else:
            return self.bKing.xcor() // SIZE, self.bKing.ycor() // SIZE


x = 10
display = turtle.Screen()
board = Board()

turtle.setup(board.screenSize + x, board.screenSize + x)  # change window size
boardPic = "board.gif"

# to make 0,0 the origin, x was added to fix center backgroud
turtle.setworldcoordinates(x, x, board.screenSize, board.screenSize)
display.bgpic(boardPic)

# used to recenter background pic https://stackoverflow.com/questions/49086447/
# turtle-graphics-how-can-background-image-in-the-center-after-setting-the-world
canvas = display.getcanvas()
canvas.itemconfig(display._bgpic, anchor="sw")  # pylint: disable=W0212
# end of centering code

pieces = Pieces()

whiteTurn = True
piece = None  # stores selected piece


# used to loop
def loop_control():
    pass


# generates possible diagonal moves
def diagonal_movement(x_old, y_old):
    possible_moves = []

    #used to reduce repetition
    def loops(a, b, c, d):
        i = x_old + c
        j = y_old + d
        while i*c <= a*c and j*d <= b*d: #flipping inequality direction
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
    del piecesDic[(victim.xcor() // SIZE, victim.ycor() // SIZE)]
    victim.hideturtle()


# return which color is in check, no if no one is
def check(x=-1, y=-1, color="no"):
    black_king = pieces.getpos("black")
    white_king = pieces.getpos("white")
    if x != -1 and y != -1 and color != "no":
        if color == "white":
            white_king = x, y
        else:
            black_king = x, y
    for x, y in piecesDic:
        piece = piecesDic[(x, y)]
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
            # used to reduce repetition
            def loops(a, b, c, d, e):
                temp_cor = [x + a, y + b]
                while temp_cor[e]*d >= c*d:
                    if (temp_cor[0], temp_cor[1]) == cur_king:
                        return board.get_piece(temp_cor[0], temp_cor[1]).color
                    if board.get_piece(temp_cor[0], temp_cor[1]):
                        break
                    temp_cor[0] += a
                    temp_cor[1] += b
            # left
            loops(-1, 0, 0, 1, 0)
            # up
            loops(0, 1, 7, -1, 1)
            # right
            loops(1, 0, 7, -1, 0)
            # down
            loops(0, -1, 0, 1, 1)

        # takes care of bishop and rest of Queen's moves
        if piece.shape() == bishopB or piece.shape() == bishopW or piece.shape() == queenB or piece.shape() == queenW:
            possible_moves = diagonal_movement(x, y)
            if cur_king in possible_moves:
                return piecesDic.get(cur_king).color
        if piece.shape() == knightB or piece.shape() == knightW:
            possible_moves = [(x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2),
                              (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2)]
            if cur_king in possible_moves:
                return piecesDic.get(cur_king).color
    return "no"


# checks if it is checkmate
def checkmate():
    pass


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
def pawnmovement(x_old, y_old, x, y, piece, captured):
    d = pawndir(piece)  # which way is the pawn going
    if (x == x_old - 1 or x == x_old + 1) and y == y_old + d:
        # check for en passant
        if board.get_piece(x, y_old) and board.get_piece(x, y_old).enpassantable:
            captured = board.get_piece(x, y_old)

        if captured:
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
    if (y == 7 or y == 0) and not captured:
        capture(piece)  # get rid of old pawn
        return queen(piece.color, x_old, y_old)
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


def gameplay(x, y):
    x = x // SIZE
    y = y // SIZE

    global piece, whiteTurn, piecesDic
    if piece:
        x_old = piece.xcor() // SIZE
        y_old = piece.ycor() // SIZE
        if (x_old, y_old) == (x, y):
            piece = None
            return 0

        # if applicable, the piece that is being captured will be stored here
        captured = board.get_piece(x, y)

        # cannot capture your own piece
        if captured and captured.color != oppcolor(piece):
            piece = None
            return 0

        # checks if king would be in check after move
        if check_caller(x, y, piece, piecesDic, x_old, y_old) == piece.color:
            piece = None
            return 0

        # checks movement for every piece
        if piece.shape() == pawnW or piece.shape() == pawnB:
            piece = pawnmovement(x_old, y_old, x, y, piece, captured)
            if not piece:
                return 0

        if piece.shape() == rookB or piece.shape() == rookW:
            if x != x_old and y != y_old:
                piece = None
                return 0
        if piece.shape() == bishopB or piece.shape() == bishopW:
            possible_moves = diagonal_movement(x_old, y_old)
            if (x, y) not in possible_moves:
                piece = None
                return 0
        if piece.shape() == queenB or piece.shape() == queenW:
            diagonal_moves = diagonal_movement(x_old, y_old)
            if x != x_old and y != y_old and (x, y) not in diagonal_moves:
                piece = None
                return 0
        if piece.shape() == knightB or piece.shape() == knightW:
            possible_moves = [(x_old + 1, y_old + 2), (x_old + 2, y_old + 1), (x_old + 2, y_old - 1),
                              (x_old + 1, y_old - 2), (x_old - 1, y_old - 2), (x_old - 2, y_old - 1),
                              (x_old - 2, y_old + 1), (x_old - 1, y_old + 2)]
            if (x, y) not in possible_moves:
                piece = None
                return 0
            if captured:
                capture(captured)
        if piece.shape() == kingB or piece.shape() == kingW:
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
                if piece.color == "white":
                    if board.get_piece(sevenorzero, 0):
                        cur_rook = board.get_piece(sevenorzero, 0)
                        if board.get_piece(sevenorzero, 0).hasMoved:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                    if sevenorzero == 7:
                        if board.get_piece(5, 0) or board.get_piece(6, 0):
                            piece = None
                            return 0
                    else:
                        if board.get_piece(1, 0) or board.get_piece(2, 0) or board.get_piece(3, 0):
                            piece = None
                            return 0
                else:
                    if board.get_piece(sevenorzero, 7):
                        cur_rook = board.get_piece(sevenorzero, 7)
                        if board.get_piece(sevenorzero, 7).hasMoved:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                    if sevenorzero == 7:
                        if board.get_piece(5, 7) or board.get_piece(6, 7):
                            piece = None
                            return 0
                    else:
                        if board.get_piece(1, 7) or board.get_piece(2, 7) or board.get_piece(3, 7):
                            piece = None
                            return 0
                # makes sure king isn't already in check, and doesn't move through check
                for i in range(2):
                    if check_caller(x_old + (i * temp), y, piece, piecesDic, x_old, y_old) == piece.color:
                        piece = None
                        return 0

                if piece.hasMoved:
                    piece = None
                    return 0
                # castling time :)
                if piece.color == "white":
                    if sevenorzero == 7:
                        cur_rook.speed(5)
                        del piecesDic[7, 0]
                        # 275, 25
                        cur_rook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                        piecesDic[5, y] = cur_rook

                        piece.speed(5)
                        del piecesDic[x_old, y_old]
                        # 275, 25
                        piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                        piecesDic[6, y] = piece
                    else:
                        cur_rook.speed(5)
                        del piecesDic[0, 0]
                        # 175, 25
                        cur_rook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                        piecesDic[3, y] = cur_rook

                        piece.speed(5)
                        del piecesDic[x_old, y_old]
                        # 275, 25
                        piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                        piecesDic[x, y] = piece
                else:
                    if sevenorzero == 7:
                        cur_rook.speed(5)
                        del piecesDic[7, 7]
                        # 275, 375
                        cur_rook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                        piecesDic[5, y] = cur_rook

                        piece.speed(5)
                        del piecesDic[x_old, y_old]
                        # 275, 25
                        piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                        piecesDic[6, y] = piece
                    else:
                        cur_rook.speed(5)
                        del piecesDic[0, 7]
                        # 175, 375
                        cur_rook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                        piecesDic[3, y] = cur_rook

                        piece.speed(5)
                        del piecesDic[x_old, y_old]
                        # 275, 25
                        piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                        piecesDic[x, y] = piece
                # castling done, so end move
                piece = None
                whiteTurn = not whiteTurn
                return 0

            possible_moves = [(x_old, y_old + 1), (x_old + 1, y_old + 1), (x_old + 1, y_old), (x_old + 1, y_old - 1),
                              (x_old, y_old - 1), (x_old - 1, y_old - 1), (x_old - 1, y_old), (x_old - 1, y_old + 1)]
            
            if (x, y) not in possible_moves:
                piece = None
                return 0
        if piece.shape() != knightB and piece.shape() != knightW:
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
                    if x == temp_x and y == temp_y and captured.color != piece.color \
                            and piece.shape() != pawnB and piece.shape() != pawnW:
                        capture(captured)
                    else:
                        piece = None
                        return 0
        for g in piecesDic:
            if piecesDic[g].shape() == pawnB:
                piecesDic[g].enpassantable = False
            if piecesDic[g].shape() == pawnW:
                piecesDic[g].enpassantable = False
        if (piece.shape() == pawnB or piece.shape() == pawnW) and (y == y_old + 2 or y == y_old - 2):
            piece.enpassantable = True
        piece.speed(5)
        del piecesDic[x_old, y_old]
        piece.goto(25 + x * SIZE, 25 + y * SIZE)
        piecesDic[x, y] = piece
        piece.hasMoved = True
        piece = None
        whiteTurn = not whiteTurn
    else:
        piece = board.get_piece(x, y)
        if not piece:
            return 0
        if piece.color == "white" and not whiteTurn:
            piece = None
        elif piece.color == "black" and whiteTurn:
            piece = None


turtle.onscreenclick(gameplay, 1)

turtle.mainloop()
