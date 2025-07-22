blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_val=[1]):
    blockchain.append([last_transaction_val, transaction_amount])
    
    
def get_user_input():
    return float(input('Your transaction amount please: '))

user_transaction_amount= get_user_input()
add_value(user_transaction_amount)

user_transaction_amount= get_user_input()
add_value(user_transaction_amount,get_last_blockchain_value())

user_transaction_amount=get_user_input()
add_value(user_transaction_amount,get_last_blockchain_value())

print(blockchain)
