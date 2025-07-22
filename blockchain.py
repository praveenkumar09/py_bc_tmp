#Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current block chain"""
    return blockchain[-1]


def add_value(transaction_amount, last_transaction_val=[1]):
    """ Append a new value as well as the last blockchain value to the block chain
    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction_val: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction_val, transaction_amount])
    
    
def get_user_input():
    """ Returns the input of the user as a float"""
    return float(input('Your transaction amount please: '))

user_transaction_amount= get_user_input()
add_value(user_transaction_amount)

user_transaction_amount= get_user_input()
add_value(user_transaction_amount,get_last_blockchain_value())

user_transaction_amount=get_user_input()
add_value(user_transaction_amount,get_last_blockchain_value())

print(blockchain)
