#!/usr/bin/python
# -> coding: utf-# -*-

from hashlib import sha256

def updateHash(*args):
    for arg in args:
        print(arg)

updateHash("One", "Two", 3)

class Block():
    data = None
    hash = None
    nonce = 0
    prevHash = "0" * 64
    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updateHash(self.prevHash, self.number, self.data, self.nonce)

class Blockchain():
    pass

def main():
    block = Block("Hello, Atom!", 1)

if __name__ == '__main__':
    main()