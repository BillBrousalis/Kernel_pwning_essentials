#!/usr/bin/env python3
import sys

def howto():
  print('Provide string to hexify as argument.\n'
        'ex. ./str2hex.py flag.txt\n')
  exit()

def hexify(string):
  return ''.join([hex(ord(c))[2:] for c in string[::-1]])

if __name__ == '__main__':
  if len(sys.argv) < 2: howto()
  string = sys.argv[1]
  print(f'{string} --> 0x{hexify(string)}')
