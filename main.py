import sys


class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

class Scoreboard:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._board = [None] * capacity
        self._n = 0

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]
                j -= 1
            self._board[j] = entry

    def board(self):
        rank = 1
        for i in self._board:
            if not i == None:
                print("Best Player ", rank, "-> Nama: ", i.get_name(), ", Point: ", i.get_score())
            else:
                print("Best Player ", rank, "-> None")
            rank += 1

def main():
    bestPlayer = int(input("Jumlah best player: "))
    scoreBoard = Scoreboard(bestPlayer)

    i = 1
    while i>0:
        print("""\n1. Tambah pemain\n2. Lihat papan score\n3. Keluar""")
        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            playername = str(input("Nama pemain: "))
            playerPoint = str(input("Point pemain: "))
            gameEntry = GameEntry(playername, playerPoint)
            scoreBoard.add(gameEntry)
        elif pilihan == 2:
            scoreBoard.board()
        else:
            sys.exit()
main()
