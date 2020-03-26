class Data:
    def __init__(self, board):
        self.board = board
        return 

    def GetActionTable(self): 
        actionTable = [] 
        fromlineCounter = 0
        fromLetterCounter = 0
        tolineCounter = 0
        toLetterCounter = 0
        for line in self.board.letterPieces:
            for letter in line:
                for lineForLetter in self.board.letterPieces:
                    for letterForLetter in line:
                        action = self.board.lines[fromLetterCounter] + "" + str(fromlineCounter+1) + " " + self.board.lines[toLetterCounter]+ "" + str(tolineCounter+1)
                        actionTable.append(action)
                        toLetterCounter = toLetterCounter + 1
                    tolineCounter = tolineCounter + 1
                    toLetterCounter = 0
                tolineCounter = 0
                fromLetterCounter = fromLetterCounter + 1
            fromlineCounter = fromlineCounter + 1
            fromLetterCounter = 0
        return actionTable
    
    def GetEnvironnement(self, pieces):
        env = [[]]
        colCounter = 0
        lineCounter = 0
        for line in pieces:
            for piece in line:
                env[lineCounter].append(piece.GetEnvValue())
                colCounter = colCounter + 1
            if lineCounter < 7:
                env .append([])
            lineCounter = lineCounter + 1

        print(env)
        return env
