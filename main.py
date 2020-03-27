import chess
import model
import data
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

board = chess.Board()
model = model.RlModel()

print(board.data.GetActionTable()[np.argmax(model.predict(board.GetEnvironnement()))])
