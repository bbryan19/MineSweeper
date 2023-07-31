#!/usr/bin/env python3
import Board
import csv
import Piece
import Player


def main():
    inputs = []
    with open('input.csv', newline='') as input_file:
        reader = csv.reader(input_file)
        for item in reader:
            inputs.append(item)

    length = int(inputs[0][0])
    width = int(inputs[0][1])
    mine_total = int(inputs[0][2])

    board = Board.Board(length, width, mine_total)

    player = Player.Player('Bill')
    player.play(board)

if __name__ == '__main__':
    main()