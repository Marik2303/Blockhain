import unittest
from blockchain import Blockchain, Transaction, Block


class TestBlockchain(unittest.TestCase):
    def test_create_transaction(self):
        tx = Transaction("Alice", "Bob", 50)
        self.assertEqual(tx.sender, "Alice")
        self.assertEqual(tx.receiver, "Bob")
        self.assertEqual(tx.amount, 50)

    def test_create_block(self):
        block = Block("0", [Transaction("Alice", "Bob", 50)])
        self.assertEqual(block.previous_hash, "0")
        self.assertIsNotNone(block.hash)
        self.assertIsNotNone(block.merkle_root)

    def test_mine_block(self):
        blockchain = Blockchain()
        blockchain.add_transaction(Transaction("Alice", "Bob", 50))
        blockchain.add_transaction(Transaction("Bob", "Charlie", 20))
        blockchain.mine_block()
        self.assertEqual(len(blockchain.chain), 1)

    def test_validate_blockchain(self):
        blockchain = Blockchain()
        blockchain.add_transaction(Transaction("Alice", "Bob", 50))
        blockchain.add_transaction(Transaction("Bob", "Charlie", 20))
        blockchain.mine_block()
        self.assertTrue(blockchain.validate_blockchain())


if __name__ == "__main__":
    unittest.main()