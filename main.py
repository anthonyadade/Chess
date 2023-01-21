#https://docs.python.org/3/library/turtle.html

import turtle

SIZE = 50


display = turtle.Screen()

#Piece pictures drawn by me, board image from Chess.com
rookB = "D:/Chess/Black Rook.gif"
rookW = "D:/Chess/White Rook.gif"
knightB = "D:/Chess/Black Knight.gif"
knightW = "D:/Chess/White Knight.gif"
bishopB = "D:/Chess/Black Bishop.gif"
bishopW = "D:/Chess/White Bishop.gif"
queenB = "D:/Chess/Black Queen.gif"
queenW = "D:/Chess/White Queen.gif"
kingB = "D:/Chess/Black King.gif"
kingW = "D:/Chess/White King.gif"
pawnB = "D:/Chess/Black Pawn.gif"
pawnW = "D:/Chess/White Pawn.gif"
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

class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.squareSize = SIZE
        self.screenSize = self.width*self.squareSize

    def getPiece(self, x, y):
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
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
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
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
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
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
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
    piece.hasMoved = None #Doesn't matter, placeholder
    piece.penup()
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
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
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
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
    piece.goto(25 + x*SIZE, 25 + y*SIZE)
    piecesDic[x, y] = piece
    return piece


#initialize all pieces
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

x = 10
display = turtle.Screen()
board = Board()

turtle.setup(board.screenSize+x, board.screenSize+x) #change window size
boardPic = "D:/Chess/board.gif"

#to make 0,0 the origin, x was added to fix center backgroud
turtle.setworldcoordinates(x, x, board.screenSize, board.screenSize)
display.bgpic(boardPic)
#used to recenter background pic https://stackoverflow.com/questions/49086447/
# turtle-graphics-how-can-background-image-in-the-center-after-setting-the-world
canvas = display.getcanvas()
canvas.itemconfig(display._bgpic, anchor="sw")  # pylint: disable=W0212
#end of centering code

pieces = Pieces()

whiteTurn = True
piece = None #stores selected piece

#generates possible diagonal moves
def diagonalMovement(xOld, yOld):
    possibleMoves = []
    # possible moves top right
    i = xOld + 1
    j = yOld + 1
    while i <= 7 and j <= 7:
        possibleMoves.append((i, j))
        if board.getPiece(i, j):
            break
        i += 1
        j += 1
    # possible moves top left
    i = xOld - 1
    j = yOld + 1
    while i >= 0 and j <= 7:
        possibleMoves.append((i, j))
        if board.getPiece(i, j):
            break
        i -= 1
        j += 1
    # possible moves bottom left
    i = xOld - 1
    j = yOld - 1
    while i >= 0 and j >= 0:
        possibleMoves.append((i, j))
        if board.getPiece(i, j):
            break
        i -= 1
        j -= 1
    # possible moves bottom right
    i = xOld + 1
    j = yOld - 1
    while i <= 7 and j >= 0:
        possibleMoves.append((i, j))
        if board.getPiece(i, j):
            break
        i += 1
        j -= 1
    return possibleMoves


def capture(victim):
    del piecesDic[(victim.xcor()//SIZE, victim.ycor()//SIZE)]
    victim.hideturtle()


#return which color is in check, no if no one is
def check():
    #x is coordinates
    for x in piecesDic:
        if piecesDic[x].shape() == kingB:
            blackK = x
        if piecesDic[x].shape() == kingW:
            whiteK = x
    for x, y in piecesDic:
        piece = piecesDic[(x, y)]
        if piece.color == "white":
            curKing = blackK
        else:
            curKing = whiteK
        if piece.shape() == pawnW:
            if (x - 1, y + 1) == blackK or (x + 1, y + 1) == blackK:
                return "black"
        if piece.shape() == pawnB:
            if (x - 1, y - 1) == whiteK or (x + 1, y - 1) == whiteK:
                return "white"
        # below checks horizontal and vertical for rook and queen
        if piece.shape() == rookB or piece.shape() == rookW or piece.shape() == queenB or piece.shape() == queenW:
            # left
            tempX = x - 1
            tempY = y
            while tempX >= 0:
                if (tempX, tempY) == curKing:
                    return board.getPiece(tempX, tempY).color
                if board.getPiece(tempX, tempY):
                    break
                tempX -= 1
            # up
            tempX = x
            tempY = y + 1
            while tempY <= 7:
                if (tempX, tempY) == curKing:
                    return board.getPiece(tempX, tempY).color
                if board.getPiece(tempX, tempY):
                    break
                tempY += 1
            # right
            tempX = x + 1
            tempY = y
            while tempX <= 7:
                if (tempX, tempY) == curKing:
                    return board.getPiece(tempX, tempY).color
                if board.getPiece(tempX, tempY):
                    break
                tempX += 1
            # down
            tempX = x
            tempY = y - 1
            while tempY >= 0:
                if (tempX, tempY) == curKing:
                    return board.getPiece(tempX, tempY).color
                if board.getPiece(tempX, tempY):
                    break
                tempY -= 1
        # takes care of bishop and rest of Queen's moves
        if piece.shape() == bishopB or piece.shape() == bishopW or piece.shape() == queenB or piece.shape() == queenW:
            possibleMoves = diagonalMovement(x, y)
            if curKing in possibleMoves:
                return piecesDic.get(curKing).color
        if piece.shape() == knightB or piece.shape() == knightW:
            possibleMoves = [(x + 1, y + 2), (x + 2, y + 1), (x + 2, y - 1), (x + 1, y - 2),
                             (x - 1, y - 2), (x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2)]
            if curKing in possibleMoves:
                return piecesDic.get(curKing).color
    return "no"


def gameplay(x, y):
    x = x // SIZE
    y = y // SIZE

    global piece
    global whiteTurn
    global piecesDic
    if piece:
        xOld = piece.xcor()//SIZE
        yOld = piece.ycor()//SIZE
        if (xOld, yOld) == (x, y):
            piece = None
            return 0
        #cannot capture your own king
        if board.getPiece(x, y):
            if board.getPiece(x, y).shape() == kingW or (x, y) == board.getPiece(x, y).shape() == kingB:
                piece = None
                return 0
        # check if in check after piece is moved

        original = piecesDic.copy()
        piecesDic[x, y] = piece
        del piecesDic[xOld, yOld]
        inCheck = check()

        piecesDic = original.copy()
        print(inCheck)
        if inCheck == piece.color:
            piece = None
            return 0

        #checks movement for every piece
        if piece.shape() == pawnW:
            if (x == xOld - 1 or x == xOld + 1) and y == yOld + 1:
                captured = board.getPiece(x, y)
                if captured:
                    if captured.color == "black":
                        capture(captured)
                    else:
                        piece = None
                        return 0
                #en passant
                elif board.getPiece(x, yOld):
                    if board.getPiece(x, yOld).shape() == pawnB:
                        if board.getPiece(x, yOld).enpassantable:
                            capture(board.getPiece(x, yOld))
                        else:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                else:
                    piece = None
                    return 0
            elif (piece.hasMoved and y > yOld + 1) or (not piece.hasMoved and y > yOld + 2) or x != xOld or y < yOld:
                piece = None
                return 0
            piece.hasMoved = True
            if y == 7 and not board.getPiece(x, y):
                capture(piece)
                piece = queen("white", xOld, yOld)
        if piece.shape() == pawnB:
            if (x == xOld - 1 or x == xOld + 1) and y == yOld - 1:
                captured = board.getPiece(x, y)
                if captured:
                    if captured.color == "white":
                        capture(captured)
                    else:
                        piece = None
                        return 0
                #en passant
                elif board.getPiece(x, yOld):
                    if board.getPiece(x, yOld).shape() == pawnW:
                        if board.getPiece(x, yOld).enpassantable:
                            capture(board.getPiece(x, yOld))
                        else:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                else:
                    piece = None
                    return 0
            elif (piece.hasMoved and y < yOld - 1) or (not piece.hasMoved and y < yOld - 2) or x != xOld or y > yOld:
                piece = None
                return 0
            piece.hasMoved = True
            if y == 0 and not board.getPiece(x, y):
                capture(piece)
                piece = queen("black", xOld, yOld)
        if piece.shape() == rookB or piece.shape() == rookW:
            if x != xOld and y != yOld:
                piece = None
                return 0
        if piece.shape() == bishopB or piece.shape() == bishopW:
            possibleMoves = diagonalMovement(xOld, yOld)
            if (x, y) not in possibleMoves:
                piece = None
                return 0
        if piece.shape() == queenB or piece.shape() == queenW:
            diagonalMoves = diagonalMovement(xOld, yOld)
            if x != xOld and y != yOld and (x, y) not in diagonalMoves:
                piece = None
                return 0
        if piece.shape() == knightB or piece.shape() == knightW:
            possibleMoves = [(xOld + 1, yOld + 2), (xOld + 2, yOld + 1), (xOld + 2, yOld - 1), (xOld + 1, yOld - 2),
                             (xOld - 1, yOld - 2), (xOld - 2, yOld - 1), (xOld - 2, yOld + 1), (xOld - 1, yOld + 2)]
            if (x, y) not in possibleMoves:
                piece = None
                return 0
            captured = board.getPiece(x, y)
            if captured:
                if captured.color != piece.color:
                    capture(captured)
        if piece.shape() == kingB or piece.shape() == kingW:
            #take care of castling
            if (x, y) == (xOld - 2, yOld) or (x, y) == (xOld + 2, yOld):
                if x > xOld:
                    temp = -1
                    sevenorzero = 7
                else:
                    temp = 1
                    sevenorzero = 0
                #this checks if the corresponding rook has already moved
                #also checks if any pieces are in the way
                if piece.color == "white":
                    if board.getPiece(sevenorzero, 0):
                        curRook = board.getPiece(sevenorzero, 0)
                        if board.getPiece(sevenorzero, 0).hasMoved:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                    if sevenorzero == 7:
                        if board.getPiece(5, 0) or board.getPiece(6, 0):
                            piece = None
                            return 0
                    else:
                        if board.getPiece(1, 0) or board.getPiece(2, 0) or board.getPiece(3, 0):
                            piece = None
                            return 0
                else:
                    if board.getPiece(sevenorzero, 7):
                        curRook = board.getPiece(sevenorzero, 7)
                        if board.getPiece(sevenorzero, 7).hasMoved:
                            piece = None
                            return 0
                    else:
                        piece = None
                        return 0
                    if sevenorzero == 7:
                        if board.getPiece(5, 7) or board.getPiece(6, 7):
                            piece = None
                            return 0
                    else:
                        if board.getPiece(1, 7) or board.getPiece(2, 7) or board.getPiece(3, 7):
                            piece = None
                            return 0
                #makes sure king would not be in check
                original = piecesDic.copy()
                piecesDic[x, y] = piece
                del piecesDic[xOld, yOld]
                inCheck1 = check()
                piecesDic = original.copy()

                original = piecesDic.copy()
                piecesDic[x + temp, y] = piece
                del piecesDic[xOld, yOld]
                inCheck2 = check()
                piecesDic = original.copy()
                #king cannot move through check, end up in check, or already be in check
                #also has to be king's first move
                if inCheck1 == piece.color or inCheck1 == piece.color or piece.hasMoved or check() == piece.color:
                    piece = None
                    return 0
                #castling time :)
                if piece.color == "white":
                    if sevenorzero == 7:
                        curRook.speed(5)
                        del piecesDic[7, 0]
                        #275, 25
                        curRook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                        piecesDic[5, y] = curRook

                        piece.speed(5)
                        del piecesDic[xOld, yOld]
                        # 275, 25
                        piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                        piecesDic[6, y] = piece
                    else:
                        curRook.speed(5)
                        del piecesDic[0, 0]
                        # 175, 25
                        curRook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                        piecesDic[3, y] = curRook

                        piece.speed(5)
                        del piecesDic[xOld, yOld]
                        # 275, 25
                        piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                        piecesDic[x, y] = piece
                else:
                    if sevenorzero == 7:
                        curRook.speed(5)
                        del piecesDic[7, 7]
                        # 275, 375
                        curRook.goto(25 + 5 * SIZE, 25 + y * SIZE)
                        piecesDic[5, y] = curRook

                        piece.speed(5)
                        del piecesDic[xOld, yOld]
                        # 275, 25
                        piece.goto(25 + 6 * SIZE, 25 + y * SIZE)
                        piecesDic[6, y] = piece
                    else:
                        curRook.speed(5)
                        del piecesDic[0, 7]
                        # 175, 375
                        curRook.goto(25 + 3 * SIZE, 25 + y * SIZE)
                        piecesDic[3, y] = curRook

                        piece.speed(5)
                        del piecesDic[xOld, yOld]
                        # 275, 25
                        piece.goto(25 + 2 * SIZE, 25 + y * SIZE)
                        piecesDic[x, y] = piece
                #castling done, so end move
                piece = None
                whiteTurn = not whiteTurn
                return 0

            possibleMoves = [(xOld, yOld + 1), (xOld + 1, yOld + 1), (xOld + 1, yOld), (xOld + 1, yOld - 1),
                             (xOld, yOld - 1), (xOld - 1, yOld - 1), (xOld - 1, yOld), (xOld - 1, yOld + 1)]
            if (x, y) not in possibleMoves:
                piece = None
                return 0
        if piece.shape() != knightB and piece.shape() != knightW:
            tempX = xOld
            tempY = yOld
            while tempX != x or tempY != y:
                if tempX < x:
                    tempX += 1
                if tempY < y:
                    tempY += 1
                if tempX > x:
                    tempX -= 1
                if tempY > y:
                    tempY -= 1
                if board.getPiece(tempX, tempY):
                    captured = board.getPiece(tempX, tempY)
                    if x == tempX and y == tempY and captured.color != piece.color \
                            and piece.shape() != pawnB and piece.shape() != pawnW:
                        capture(captured)
                    else:
                        piece = None
                        return 0
        if (piece.shape() == pawnB or piece.shape() == pawnW) and (y == yOld + 2 or y == yOld - 2):
            piece.enpassantable = True
        else:
            for g in piecesDic:
                if piecesDic[g].shape() == pawnB:
                    piecesDic[g].enpassantable = False
                if piecesDic[g].shape() == pawnW:
                    piecesDic[g].enpassantable = False
        piece.speed(5)
        del piecesDic[xOld, yOld]
        piece.goto(25 + x * SIZE, 25 + y * SIZE)
        piecesDic[x, y] = piece
        piece = None
        whiteTurn = not whiteTurn
    else:
        piece = board.getPiece(x, y)
        if not piece:
            return 0
        if piece.color == "white" and not whiteTurn:
            piece = None
        elif piece.color == "black" and whiteTurn:
            piece = None


turtle.onscreenclick(gameplay, 1)

turtle.mainloop()
