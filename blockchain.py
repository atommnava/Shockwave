#!/usr/bin/python
# -> coding: utf-# -*-

from hashlib import sha256

def updateHash(*args):
    hashingText = ""; h = sha256()
    for arg in args:
        hashingText += str(arg)

    h.update(hashingText.encode('utf-8'))
    return h.hexdigest()

print(updateHash("Hello world", "Hello"))

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

    def __str__(self):
        return str("Block #: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(self.number, self.hash, self.prevHash, self.data, self.nonce))

class Blockchain():
    pass

def main():
    block = Block("Hello, Atom!", 1)
    print(block)

if __name__ == '__main__':
    main()