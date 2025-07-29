from utility.verification import Verification
from blockchain import Blockchain

from uuid import uuid4


class Node:

    def __init__(self):
        #self.id = str(uuid4())
        self.id='MAX'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """ Returns the input of the user as a float"""
        transaction_recipient = input(
            'Enter the recipient of the transaction:')
        transaction_amount = float(input('Your transaction amount please: '))
        return (transaction_recipient, transaction_amount)

    def get_user_choice(self):
        user_input = input('Your choice:')
        return user_input

    def print_block_chain_elements(self):
        # Output the blockchain list to the console
        for block in self.blockchain.get_chain():
            print('Outputting block')
            print(block)

    def print_balance(self):
        print('Balance of {} : {:6.2f}'.format(
            self.id, self.blockchain.get_balance()))

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Please choose : ')
            print("1: Add a new transaction value.")
            print('2: Mine a new block')
            print("3: Output a blockchain block")
            print("4: Get Balance")
            print("5: Verify transaction")
            print('q: Quit')
            user_input = self.get_user_choice()
            if (user_input == '1'):
                transaction_data = self.get_transaction_value()
                transaction_recipient, transaction_amount = transaction_data
                result = self.blockchain.add_transaction(
                    transaction_recipient, self.id, amount=transaction_amount)
                if result:
                    self.blockchain.save_data()
                    print('Transaction added successfully')
                    self.print_balance()
                else:
                    print('Transaction failed!. Insufficient Balance!')
            elif (user_input == '2'):
                self.blockchain.mine_block()
                self.print_balance()
            elif (user_input == '3'):
                self.print_block_chain_elements()
            elif (user_input == '4'):
                self.print_balance()
            elif (user_input == '5'):
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif (user_input == 'q'):
                print("You have decided to quit, bye!")
                waiting_for_input = False
            else:
                print('Input was invalid!. Please try again with the choices provided!')
            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_block_chain_elements()
                print('Verification failed, Invalid blockchain!')
                break
        else:
            print('User left!')
            
node = Node()
node.listen_for_input()          
