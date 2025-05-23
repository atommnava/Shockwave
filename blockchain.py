#!/usr/bin/python
# -> coding: utf-8 -*-

from hashlib import sha256

def updateHash(*args):
    hashingText = ""; h = sha256()
    for arg in args:
        hashingText += str(arg)

    h.update(hashingText.encode('utf-8'))
    return h.hexdigest()

#print(updateHash("Hello world", "Hello"))

class Block():
    data = None
    hash = None
    nonce = 0
    prevHash = "0" * 64
    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updateHash(
        self.prevHash,
            self.number,
            self.data,
            self.nonce)

    def __str__(self):
        return str("Block #: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n"
                   %(self.number,
                     self.hash,
                     self.prevHash,
                     self.data,
                     self.nonce))

class Blockchain:

    difficulty = 3
    def __init__(self, chain=[]):
        self.chain = chain


    def add(self, block):
        self.chain.append(block)


    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.prevHash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1

    def isValid(self):
        for i in range(1, len(self.chain)):
            _prev = self.chain[i].prevHash
            _curr = self.chain[i - 1].hash()
            if _prev != _curr or _curr[:self.difficulty] != "0" * self.difficulty:
                return False

        return True



def main():
    AtomsBlockchain = Blockchain()
    database = ["Hello, Atom!", "How R u doin?", "Hello", "Bye"]

    num = 0
    for data in database:
        num += 1
        AtomsBlockchain.mine(Block(data, num))

    for block in AtomsBlockchain.chain:
        print(block)

    # AtomsBlockchain.chain[2].data = "CORRUPTED DATA"
    # AtomsBlockchain.mine(AtomsBlockchain.chain[2])
    print(f"State: ", AtomsBlockchain.isValid())


if __name__ == '__main__':
    main()