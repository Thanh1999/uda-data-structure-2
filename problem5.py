import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
        
    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
    

    
class BlockChain:
    def __init__(self):
        self.chain = []

    def get_last_block_hash(self):
       if len(self.chain) > 0:
          return self.chain[-1].hash
       return ''
    
    def is_valid(self, block):
       return self.get_last_block_hash() == block.previous_hash
        
    def add_block(self, block):
       if block is not None and self.is_valid(block):
          self.chain.append(block)

    def print_chain(self): 
        for block in self.chain: 
            print("Timestamp:", block.timestamp) 
            print("Data:", block.data) 
            print("Hash:", block.hash) 
            print("Previous Hash:", block.previous_hash) 
            print()
        print("--------------------------------------\n") 


## Test case 1 - Added both 2 blocks to the chain
blockchain = BlockChain()
block1 = Block(time.time(), "Block 1", blockchain.get_last_block_hash()) 
blockchain.add_block(block1) 
block2 = Block(time.time(), "Block 2", blockchain.get_last_block_hash()) 
blockchain.add_block(block2) 
blockchain.print_chain()

## Test case 2 - second block can't be added
blockchain = BlockChain()
block1 = Block(time.time(), "Block 3", blockchain.get_last_block_hash()) 
blockchain.add_block(block1) 
block2 = Block(time.time(), "Block 4", "ah172bxfsd") 
blockchain.add_block(block2) 
blockchain.print_chain()

## Test case 3 - None object can't be added
blockchain = BlockChain()
block1 = Block(time.time(), "Block 5", blockchain.get_last_block_hash()) 
blockchain.add_block(block1) 
block2 = None
blockchain.add_block(block2) 
blockchain.print_chain()