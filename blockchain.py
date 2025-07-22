# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current block chain"""
    if len(blockchain) > 0:
        return blockchain[-1]
    else:
        return None


def add_transaction(transaction_amount, last_transaction_val):
    """ Append a new value as well as the last blockchain value to the block chain
    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction_val: The last blockchain transaction (default [1])
    """
    if last_transaction_val == None:
        last_transaction_val = [1]
    blockchain.append([last_transaction_val, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user as a float"""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice:')
    return user_input


def print_block_chain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)
        
        
def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False    
    return is_valid         
        

waiting_for_input = True
while waiting_for_input:
    print('Please choose : ')
    print("1: Add a new transaction value.")
    print("2: Output a blockchain block")
    print("h: Manipulate the blockchain")
    print('q: Quit')
    user_input = get_user_choice()
    if (user_input == '1'):
        user_transaction_amount = get_transaction_value()
        add_transaction(user_transaction_amount, get_last_blockchain_value())
    elif (user_input == '2'):
        print_block_chain_elements()
    elif (user_input == 'h'):
        if len(blockchain) > 0:
            blockchain[0] = [2]    
    elif (user_input == 'q'):
        print("You have decided to quit, bye!")
        waiting_for_input = False
    else:
        print('Input was invalid!. Please try again with the choices provided!')
    if not verify_chain():
        print_block_chain_elements()
        print('Verification failed, Invalid blockchain!')   
        break
else:    
    print('User left!')
