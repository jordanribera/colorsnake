#!/usr/bin/env python3
import sys

VERSION_NUMBER = 0


class ColorSnake():
    real_commands = ['version', 'lscolors']
    colors = {}
    filetypes = {}

    def get_ls_colors():
        pass


if __name__ == "__main__":

    csnake = ColorSnake()
    command = 'version'

    if len(sys.argv) > 1:
        if sys.argv[1] in csnake.real_commands:
            command = str(sys.argv[1])

    if command == 'version':
        print(str(VERSION_NUMBER))

    if command == 'lscolors':
        print('lscolors')
