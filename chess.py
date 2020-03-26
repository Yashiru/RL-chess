import piece
import data
from sklearn import preprocessing

class Board:
    A1 = [1, 1] 
    A2 = [1, 2]
    A3 = [1, 3]
    A4 = [1, 4]
    A5 = [1, 5]
    A6 = [1, 6]
    A7 = [1, 7]
    A8 = [1, 8]
    B1 = [2, 1]
    B2 = [2, 2] 
    B3 = [2, 3]
    B4 = [2, 4]
    B5 = [2, 5]
    B6 = [2, 6]
    B7 = [2, 7]
    B8 = [2, 8]
    C1 = [3, 1]
    C2 = [3, 2] 
    C3 = [3, 3]
    C4 = [3, 4]
    C5 = [3, 5]
    C6 = [3, 6]
    C7 = [3, 7]
    C8 = [3, 8]
    D1 = [4, 1]
    D2 = [4, 2]
    D3 = [4, 3]
    D4 = [4, 4]
    D5 = [4, 5]
    D6 = [4, 6]
    D7 = [4, 7]
    D8 = [4, 8]
    E1 = [5, 1]
    E2 = [5, 2]
    E3 = [5, 3]
    E4 = [5, 4]
    E5 = [5, 5]
    E6 = [5, 6]
    E7 = [5, 7]
    E8 = [5, 8]
    F1 = [6, 1]
    F2 = [6, 2]
    F3 = [6, 3]
    F4 = [6, 4]
    F5 = [6, 5]
    F6 = [6, 6]
    F7 = [6, 7]
    F8 = [6, 8]
    G1 = [7, 1]
    G2 = [7, 2] 
    G3 = [7, 3]
    G4 = [7, 4]
    G5 = [7, 5]
    G6 = [7, 6]
    G7 = [7, 7]
    G8 = [7, 8]
    H1 = [8, 1]
    H2 = [8, 2]
    H3 = [8, 3]
    H4 = [8, 4]
    H5 = [8, 5]
    H6 = [8, 6]
    H7 = [8, 7]
    H8 = [8, 8]

    def __init__(self):
        self.lines = ["A", "B", "C", "D", "E", "F", "G", "H"]
        self.envPiece = [0.02096, 0.04247, 0.01837, 0.06111, 0.09933, 0.06244, 0.07424, 0.03588, 0.02943, 0.07676, 0.05608, 0.03618]
        self.letterPieces = [
            ["T", "C", "F", "Q", "K", "F", "C", "T"], 
            ["P", "P", "P", "P", "P", "P", "P", "P"], 
            [".", ".", ".", ".", ".", ".", ".", "."], 
            [".", ".", ".", ".", ".", ".", ".", "."], 
            [".", ".", ".", ".", ".", ".", ".", "."], 
            [".", ".", ".", ".", ".", ".", ".", "."], 
            ["p", "p", "p", "p", "p", "p", "p", "p"], 
            ["t", "c", "f", "q", "k", "f", "c", "t"]
        ]
        self.data = data.Data(self)
        self.LoadPieceObjects()

    def LoadPieceObjects(self):
        self.pieces = []
        i = 0
        lineCounter = 0
        for line in self.letterPieces:
            self.pieces.append([])
            for letter in line:
                envIndex = 0

                if letter == "T": # Tour
                    envIndex = 0
                if letter == "C": # cavalier
                    envIndex = 1            
                if letter == "F": # fou
                    envIndex = 2
                if letter == "Q": # Queen
                    envIndex = 3
                if letter == "K": # King
                    envIndex = 4
                if letter == "P": # pion
                    envIndex = 5

                if letter == "t": # opponent's Tour
                    envIndex = 6
                if letter == "c": # opponent's cavalier
                    envIndex = 7            
                if letter == "f": # opponent's fou
                    envIndex = 8
                if letter == "q": # opponent's Queen
                    envIndex = 9
                if letter == "k": # opponent's King
                    envIndex = 10
                if letter == "p": # opponent's pion
                    envIndex = 11

                envVal = self.envPiece[envIndex]

                if i < 16 and letter != ".":
                    newPiece = piece.Piece(letter, 0, envVal)
                    self.pieces[lineCounter].append(newPiece)
                if i >= 16 and letter != ".":
                    newPiece = piece.Piece(letter, 1, envVal)
                    self.pieces[lineCounter].append(newPiece)
                if letter == ".":
                    newPiece = piece.Piece(".", -1, 0)
                    self.pieces[lineCounter].append(newPiece)

                i = i+1
            lineCounter = lineCounter+1
        print(self.Board())

    def Board(self):
        return self.DisplayBoard()

    def DisplayBoard(self):
        displayedBoard = ""
        for line in self.pieces:
            for piece in line:
                displayedBoard = displayedBoard + piece.DisplayLetter() + " "
            displayedBoard = displayedBoard + "\n"
        return displayedBoard
    
    def GetEnvironnement(self):
        return self.data.GetEnvironnement(self.pieces)

    def Move(self, from_square, to_square):
        temp_from_square = [-1, -1]
        temp_to_square = [-1, -1]

        temp_from_square[0] = from_square[0]-1
        temp_from_square[1] = from_square[1]-1
        temp_to_square[0] = to_square[0]-1
        temp_to_square[1] = to_square[1]-1

        # return self.VerifyMoveLegallity(self.pieces[temp_from_square[1]][temp_from_square[0]], temp_from_square, temp_to_square)
        pieceInSquare = self.GetPieceInSquare(temp_from_square)
        freedom = self.VerifyMovementFreedomness(pieceInSquare, temp_from_square, temp_to_square)
        if self.VerifyMoveLegallity(pieceInSquare, temp_from_square, temp_to_square) and freedom[0] == True:
            self.MovePiece(pieceInSquare, temp_from_square, temp_to_square)

        else:
            return False

    def MovePiece(self, givenPiece, from_square, to_square):
        self.letterPieces[from_square[1]][from_square[0]] = "."
        self.letterPieces[to_square[1]][to_square[0]] = givenPiece.DisplayLetter()
        self.pieces[from_square[1]][from_square[0]] = piece.Piece(".", -1, 0)
        self.pieces[to_square[1]][to_square[0]] = givenPiece
        print(self.Board())
        
    def VerifyMoveLegallity(self, givenPiece, from_square, to_square):
        if givenPiece.DisplayLetter().lower() == ".":
            print("the square \"from_square\" contain no piece")
            return False
        else:
            return givenPiece.VerifyMoveLegallity(from_square, to_square)

    def VerifyMovementFreedomness(self, givenPiece, from_square, to_square):
        piece = givenPiece.DisplayLetter().lower()
        if piece == "t": # Tour
            return self.CheckForPiecePresenceInLine(from_square, to_square)

        if piece == "f": # fou
            return self.CheckForPiecePresenceInDiagonal(from_square, to_square)

        if piece == "c": # cavalier
            return self.CheckForPiecePresenceInEndSquareWithJump(from_square, to_square)

        if piece == "q": # Queen
            return

        if piece == "k": # King
            return

        if piece == "p": # pion
            return

            

    def CheckForPiecePresenceInLine(self, from_square, to_square):
        movementFreedom = True
        hitEnemy = False
        if (self.GetPieceInSquare(from_square).GetTeam() != self.GetPieceInSquare(to_square).GetTeam()) and (self.GetPieceInSquare(from_square).DisplayLetter() != "." and self.GetPieceInSquare(to_square).DisplayLetter() != "."):
            hitEnemy = True

        if from_square[0] == to_square[0] and from_square[1] < to_square[1]:
            for i in range(from_square[1]+1, to_square[1]):
                if self.letterPieces[i][from_square[0]] != ".":
                    print("Movement is not free")
                    movementFreedom = False
            if self.GetPieceInSquare(to_square).DisplayLetter() != "." and hitEnemy == False:
                print("End case is a team piece")
                movementFreedom = False

        if from_square[0] == to_square[0] and from_square[1] > to_square[1]:
            for i in range(to_square[1], from_square[1]):
                if self.letterPieces[i][from_square[0]] != ".":
                    print("Movement is not free")
                    movementFreedom = False
            if self.GetPieceInSquare(to_square).DisplayLetter() != "." and hitEnemy == False:
                print("End case is a team piece")
                movementFreedom = False



        if from_square[1] == to_square[1] and from_square[0] < to_square[0]:
            for i in range(from_square[0]+1, to_square[0]):
                if self.letterPieces[from_square[1]][i] != ".":
                    print("Movement is not free")
                    movementFreedom = False
            if self.GetPieceInSquare(to_square).DisplayLetter() != "." and hitEnemy == False:
                movementFreedom = False
                print("End case is a team piece")

        if from_square[1] == to_square[1] and from_square[0] > to_square[0]:
            for i in range(to_square[0], from_square[0]-1):
                if self.letterPieces[from_square[1]][i] != ".":
                    print("Movement is not free")
                    movementFreedom = False
            if self.GetPieceInSquare(to_square).DisplayLetter() != "." and hitEnemy == False:
                movementFreedom = False
                print("End case is a team piece")

        return [movementFreedom, hitEnemy]

    def CheckForPiecePresenceInEndSquareWithJump(self, from_square, to_square):
        movementFreedom = True
        hitEnemy = False
        if (self.GetPieceInSquare(from_square).GetTeam() != self.GetPieceInSquare(to_square).GetTeam()) and (self.GetPieceInSquare(from_square).DisplayLetter() != "." and self.GetPieceInSquare(to_square).DisplayLetter() != "."):
            hitEnemy = True
        if self.GetPieceInSquare(from_square).GetTeam() == self.GetPieceInSquare(to_square).GetTeam():
            movementFreedom = False

        return [movementFreedom, hitEnemy]
        
    def CheckForPiecePresenceInDiagonal(self, from_square, to_square):
        if to_square[0] > from_square[0]:
            if to_square[1] > from_square[1]: #droite bas
                for i in range(from_square[1], to_square[1]):
                    print([to_square[0]+i, to_square[1]+i])
                    print(self.GetPieceInSquare([to_square[0]+i, to_square[1]+i]).DisplayLetter())
                   
        return [False, False]

        #     else: #droite haut

        # else:
        #     if to_square[1] > to_square[1]: #gauche bas

        #     else: #gauche haut
        

    def CheckForPiecePresenceInL(self, from_square, to_square):
        return

    def GetPieceInSquare(self, square):
        return self.pieces[square[1]][square[0]]