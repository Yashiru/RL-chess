class Piece:
    def __init__(self, letter, team, envVal):
        self.letter = letter
        self.team = team
        if letter != ".":
            self.envValue = envVal
        else:
            self.envValue = 0

    def DisplayLetter(self):
        return self.letter

    def GetTeam(self):
        return self.team

    def GetEnvValue(self):
        return self.envValue
    
    def VerifyMoveLegallity(self, from_square, to_square):
        piece = self.DisplayLetter().lower()
        if piece == "t": # Tour
            return from_square[0] == to_square[0] or from_square[1] == to_square[1]
        if piece == "c": # Cavalier
            return (abs(from_square[0] - to_square[0]) == 2 and abs(from_square[1] - to_square[1]) == 1) or (abs(from_square[1] - to_square[1]) == 2 and abs(from_square[0] - to_square[0]) == 1)
        if piece == "f": # fou
            return abs(from_square[0] - to_square[0]) == abs(from_square[1] - to_square[1])
        if piece == "q": # Queen
            return (from_square[0] == to_square[0] or from_square[1] == to_square[1]) or (abs(from_square[0] - to_square[0]) == abs(from_square[1] - to_square[1]))
        if piece == "k": # King
            return ((abs(from_square[0] - to_square[0]) == abs(from_square[1] - to_square[1])) and (abs(from_square[0] - to_square[0]) == 1)) or ((from_square[0] == to_square[0] and abs(from_square[1] - to_square[1]) == 1) or (from_square[1] == to_square[1] and abs(from_square[0] - to_square[0]) == 1))
        if piece == "p": # pion
            if self.GetTeam() == 0:
                if from_square[1] == 1:
                    return from_square[0] == to_square[0] and (from_square[1] - to_square[1] == -1 or from_square[1] - to_square[1] == -2)
                else:
                    return from_square[0] == to_square[0] and from_square[0] - to_square[0] == -1 
            else: 
                if from_square[1] == 6:
                    return from_square[0] == to_square[0] and (from_square[1] - to_square[1] == 1 or from_square[1] - to_square[1] == 2)
                else:
                    return from_square[0] == to_square[0] and from_square[1] - to_square[1] == 1 

