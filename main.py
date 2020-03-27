import chess
import model
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

board = chess.Board()
model = model.RlModel()

print(model.predict(board.GetEnvironnement()))

