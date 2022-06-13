import tkinter
from functools import partial
from typing import Optional


class Board:
    def __init__(self):
        self.rows: list = []
        self.reset()

    def reset(self):
        self.rows = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                if self.rows[i][j] != "X" and self.rows[i][j] != "O":
                    tkinter.Button(window, text="", height=8, width=20, state=tkinter.DISABLED,
                                   font=("Courier", 16)).grid(column=j, row=i)


class Player:
    def __init__(self, name, character):
        self.name: str = name
        if character not in ["X", "O"]:
            raise ValueError("Character must be either X or O")
        self.character: str = character


class XOGame:
    def __init__(self, player_1: Player, player_2: Player):
        self.reset_game()
        self.board: Board = Board()
        self.player1: Player = player_1
        self.player2: Player = player_2
        self.current_player: Player = self.player1
        self.winner: Optional[Player] = None
        self._draw_board()

    def click_button(self, i, j):
        if self.board.rows[i][j] == "" and self.winner is None:
            self.board.rows[i][j] = self.current_player.character
            tkinter.Button(
                window, text=self.current_player.character, height=8, width=20,
                state=tkinter.DISABLED, font=("Courier", 16)).grid(column=j, row=i)

            if self._check_win():
                self.winner = self.current_player
                self.board.disable_buttons()

    def _check_win(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]]

        for combination in winning_combinations:
            if (
                    self.board.rows[combination[0][0]][combination[0][1]]
                    == self.board.rows[combination[1][0]][combination[1][1]]
                    == self.board.rows[combination[2][0]][combination[2][1]]):
                if self.board.rows[combination[0][0]][combination[0][1]] != "":
                    return True
        return False

    def reset_game(self):
        self.board = Board()
        self.current_player = self.player1
        self.winner = None
        self._draw_board()

    def _draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                tkinter.Button(
                    window, text="", height=8, width=20,
                    command=partial(self.click_button, i, j),
                    font=("Courier", 16)).grid(column=j, row=i)


window = tkinter.Tk()
window.title("TIC TAC TOE Game By Abdelkarim El Halabi")
window.geometry("875x792")

p1 = Player("Player 1", "X")
p2 = Player("Player 2", "O")

game = XOGame(p1, p2)

tkinter.Button(window, text="Restart Game", height=8, width=20, command=reset_game).grid(column=2, row=14)
window.resizable(False, False)
window.mainloop()
