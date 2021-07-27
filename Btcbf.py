from os import urandom
from bitcoin import privkey_to_address
from codecs import decode, encode
from hashlib import sha256
from base58 import b58encode
import mmap
from tqdm import tqdm
from sys import stdout

def gen(): 
      for a in tqdm(range(int(10e15))):
            pass
            a = urandom(32).hex()
            padding = '80' + a
            # print( padding ) 
            hashedVal = sha256(decode(padding, 'hex')).hexdigest()
            checksum = sha256(decode(hashedVal, 'hex')).hexdigest()[:8]
            # print( hashedVal )
            # print( padding+checksum )
            payload = padding + checksum
            wif = b58encode(decode(payload, 'hex'))
            #print(wif.decode('utf-8'))
            z = privkey_to_address(wif.decode("utf-8")).encode("utf-8")
            #print("Private Key: " + wif.decode('utf-8')) #Uncomment in order to use as address generater 
            #print("public address: " + z.decode("utf-8")) #Uncomment in order to use as address generater 
            with open('address.txt') as f:
                  s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) # search for the generated address in the "address.txt" 
                  if s.find(z) != -1:
                        print("true")
                        print(a)
                        print(z)
                        print( wif.decode('utf-8') )
                        stdout = open("foundkey.txt", "w") # the found key and address saved to "foundkey.txt"
                        print(a)
                        print(z)
                        print( wif.decode('utf-8') )
                        stdout.close()
                        exit()
                  #else: # uncommenting this part makes our code slow down
                        #print ('false')
                        #print(wif.decode("utf-8"))
                        #print(z)
gen()
