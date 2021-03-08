from Crypto import *
from time import asctime
import pprint 

pp = pprint.PrettyPrinter(indent = 4)

blockchain = Blockchain()
transactions = []

block = Block(transactions, asctime(), 0)
blockchain.addBlock(block)

block = Block(transactions, asctime(), 1)
blockchain.addBlock(block)


block = Block(transactions, asctime(), 2)
blockchain.addBlock(block)

the_object = blockchain.chainJSONenconde()
pp.pprint(the_object)

print("Length: ", len(blockchain.chain))

