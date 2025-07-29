from hash_util import hash_string_256, hash_block

class Verification:
    
    
    def valid_proof(self,transactions, last_hash, proof):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        guess_hash = hash_string_256(guess)
        return guess_hash[0:2] == '00'

    def verify_chain(self, blockchain):
        for (idx, block) in enumerate(blockchain):
            if idx == 0:
                continue
            if block.previous_hash != hash_block(blockchain[idx-1]):
                return False
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                return False
        return True

    def verify_transactions(self, open_transactions, get_balance):
        return all([self.verify_transaction(tx, get_balance) for tx in open_transactions])

    def verify_transaction(self,transaction, get_balance):
        balance_amount = get_balance(transaction.sender)
        return balance_amount >= transaction.amount
