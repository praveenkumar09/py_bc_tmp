blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_val=[1]):
    blockchain.append([last_transaction_val, transaction_amount])


add_value(2)
add_value(3,get_last_blockchain_value())
add_value(4,get_last_blockchain_value())

print(blockchain)
