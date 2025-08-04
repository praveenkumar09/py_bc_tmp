from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from binascii import hexlify, unhexlify


class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key
            
            
    def save_keys(self):
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet.txt', mode='w') as wallet_file:
                    wallet_file.write(self.public_key)
                    wallet_file.write('\n')
                    wallet_file.write(self.private_key)
            except (IOError,IndexError):
                print('Wallet creation failed')   
        

    def load_keys(self):
        try:
            with open('wallet.txt', mode='r') as wallet_file:
                keys = wallet_file.readlines()
                self.public_key = keys[0][:-1]
                self.private_key = keys[1]
        except (IOError,IndexError):
            print('Wallet load failed')

    def generate_keys(self):
        private_key = RSA.generate(1024, Random.new().read)
        public_key = private_key.publickey()
        return (hexlify(private_key.exportKey(format='DER')).decode('ascii'), hexlify(public_key.exportKey(format='DER')).decode('ascii'))
    
    
    def sign_transaction(self,sender, recipient, amount):
        #Create signer identity
        signer = PKCS1_v1_5.new(RSA.importKey(unhexlify(self.private_key)))
        #create a hashed payload
        hash_for_transaction = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8'))
        #create the signature
        signature = signer.sign(hash_for_transaction)
        return hexlify(signature).decode('ascii')
    
    @staticmethod
    def verify_transaction(transaction):
        public_key = RSA.importKey(unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        hash_for_transaction = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
        return verifier.verify(hash_for_transaction,unhexlify(transaction.signature))
