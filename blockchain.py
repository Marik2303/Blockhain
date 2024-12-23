import time
import hashlib


#hash with use SHA-256
def hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()



class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.amount}"



class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.merkle_root = self.calculate_merkle_root(transactions)
        self.hash = self.calculate_block_hash()

    def calculate_merkle_root(self, transactions):
        # hashing and mercle-tree
        transaction_hashes = [hash(str(tx)) for tx in transactions]
        while len(transaction_hashes) > 1:
            transaction_hashes = [hash(transaction_hashes[i] + transaction_hashes[i + 1])
                                  for i in range(0, len(transaction_hashes), 2)]
        return transaction_hashes[0]

    def calculate_block_hash(self):
        return hash(str(self.previous_hash) + str(self.timestamp) + str(self.merkle_root))



class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def mine_block(self):
        last_block = self.chain[-1] if self.chain else None
        new_block = Block(last_block.hash if last_block else "0", self.pending_transactions)
        self.chain.append(new_block)
        self.pending_transactions = []

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.hash != current_block.calculate_block_hash():
                return False
        return True

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)



def demo():
    blockchain = Blockchain()

    # transaction
    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 20))
    blockchain.add_transaction(Transaction("Charlie", "David", 10))


    blockchain.mine_block()

    # out of blocks and validation of blockchain
    for block in blockchain.chain:
        print(f"Block Hash: {block.hash}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Transactions: {[str(tx) for tx in block.transactions]}")
        print("-" * 40)

    print(f"Blockchain valid: {blockchain.validate_blockchain()}")


if __name__ == "__main__":
    demo()