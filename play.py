#!/usr/bin/env python3
import Board
import csv
import Piece

def play(board):
    dead = 0
    win = 0
    while not dead and not win:
        print("Your move: ")
        # Take user input and make move

        # if player chooses mine --> dead = 1
        # if player finds all mines by revealing every square that is not a mine --> win = 1



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
    print(board)

    play(board)

if __name__ == '__main__':
    main()