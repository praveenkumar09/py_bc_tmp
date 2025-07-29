from functools import reduce
from collections import OrderedDict
from pickle import dumps, loads

from hash_util import hash_block
from block import Block
from transaction import Transaction
from verification import Verification

MINING_REWARD = 10
blockchain = []


class Blockchain:
    def __init__(self, hosting_node_id):
        genesis_block = Block(0, '', [], 100, 0)
        self.chain = [genesis_block]
        self.open_transactions = []
        self.load_data()
        self.hosting_node = hosting_node_id

    def load_data(self):
        try:
            with open("blockchain.p", mode='rb') as file_ob:
                file_content = loads(file_ob.read())
                self.chain = file_content['chain']
                self.open_transactions = file_content['open_transactions']
        except FileNotFoundError:
            pass
        finally:
            print('clean up done here!')

    def save_data(self):
        try:
            with open("blockchain.p", mode='wb') as file_ob:
                save_data = {
                    'chain': self.chain,
                    'open_transactions': self.open_transactions
                }
                file_ob.write(dumps(save_data))
        except:
            print('Saving Failed')

    def proof_of_work(self):
        last_block = self.chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        verifier = Verification()
        while not verifier.valid_proof(self.open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        participant = self.hosting_node
        amount_sent = self.calculate_tx_amount(participant, 'sender')
        amount_received = self.calculate_tx_amount(participant, 'recipient')
        return amount_received - amount_sent

    def calculate_tx_amount(self, participant, person):
        amount = 0
        block_tx_list = [[tx.amount for tx in block.transactions
                          if getattr(tx, person) == participant] for block in self.chain]
        if person == 'sender':
            pending_open_tx_list = [tx.amount
                                    for tx in self.open_transactions if getattr(tx, person) == participant]
            block_tx_list.append(pending_open_tx_list)
        amount = reduce(lambda tx_sum, tx_amount: tx_sum +
                        sum(tx_amount) if len(tx_amount) > 0 else tx_sum + 0, block_tx_list, 0)
        return amount

    def get_last_blockchain_value(self):
        """ Returns the last value of the current block chain"""
        if len(self.chain) > 0:
            return self.chain[-1]
        else:
            return None

    def add_transaction(self, recipient, sender, amount=1.0):
        new_transaction = Transaction(sender, recipient, amount)
        verifier = Verification()
        if (verifier.verify_transaction(new_transaction, self.get_balance)):
            self.open_transactions.append(new_transaction)
            return True
        return False

    def mine_block(self):
        last_block = self.chain[-1]
        print([tx.to_ordered_dict() for tx in last_block.transactions])
        hashed_block = hash_block(last_block)
        proof = self.proof_of_work()
        reward_transaction = Transaction(
            'MINING', self.hosting_node, MINING_REWARD)
        copied_Transactions = self.open_transactions[:]
        copied_Transactions.append(reward_transaction)
        block = Block(len(self.chain), hashed_block,
                      copied_Transactions, proof)
        self.chain.append(block)
        self.open_transactions = []
        self.save_data()
