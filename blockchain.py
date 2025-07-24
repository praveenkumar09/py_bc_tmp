import functools

MINING_REWARD = 10
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    """ Returns the last value of the current block chain"""
    if len(blockchain) > 0:
        return blockchain[-1]
    else:
        return None


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the block chain
    Arguments:
        :sender : The sender of the coins.
        :recipient: The recipient of the coins
        :amount: the amount of coins send with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    if (verify_transaction(transaction)):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_Transactions = open_transactions[:]
    copied_Transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': copied_Transactions
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input of the user as a float"""
    transaction_recipient = input('Enter the recipient of the transaction:')
    transaction_amount = float(input('Your transaction amount please: '))
    return (transaction_recipient, transaction_amount)


def get_user_choice():
    user_input = input('Your choice:')
    return user_input


def print_block_chain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)


def print_participants():
    print("Outputting participants")
    print(participants)


def verify_chain():
    for (idx, block) in enumerate(blockchain):
        if idx == 0:
            if block['previous_hash'] != genesis_block['previous_hash']:
                return False
        else:
            if block['previous_hash'] != hash_block(blockchain[idx-1]):
                return False
    return True


def calculate_tx_amount(participant, person):
    amount = 0
    block_tx_list = [[tx['amount'] for tx in block['transactions']
                      if tx[person] == participant] for block in blockchain]
    if person == 'sender':
        pending_open_tx_list = [tx['amount']
                                for tx in open_transactions if tx[person] == participant]
        block_tx_list.append(pending_open_tx_list)
    amount = functools.reduce(lambda tx_sum, tx_amount: tx_sum +
                              sum(tx_amount) if len(tx_amount) > tx_sum + 0 else 0, block_tx_list, 0)
    return amount


def get_balance(participant):
    amount_sent = calculate_tx_amount(participant, 'sender')
    amount_received = calculate_tx_amount(participant, 'recipient')
    return amount_received - amount_sent


def verify_transaction(transaction):
    balance_amount = get_balance(transaction['sender'])
    return balance_amount >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True
while waiting_for_input:
    print('Please choose : ')
    print("1: Add a new transaction value.")
    print('2: Mine a new block')
    print("3: Output a blockchain block")
    print("4: Output participants")
    print("5: Get Balance")
    print("6: Verify transaction")
    print("h: Manipulate the blockchain")
    print('q: Quit')
    user_input = get_user_choice()
    if (user_input == '1'):
        transaction_data = get_transaction_value()
        transaction_recipient, transaction_amount = transaction_data
        result = add_transaction(
            transaction_recipient, amount=transaction_amount)
        if result:
            print('Transaction added successfully')
        else:
            print('Transaction failed!. Insufficient Balance!')
    elif (user_input == '2'):
        if mine_block():
            open_transactions = []
    elif (user_input == '3'):
        print_block_chain_elements()
    elif (user_input == '4'):
        print_participants()
    elif (user_input == '5'):
        print('Balance of {} : {:6.2f}'.format(owner, get_balance('Max')))
    elif (user_input == '6'):
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif (user_input == 'h'):
        if len(blockchain) >= 1:
            blockchain[0] = blockchain[1]
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
