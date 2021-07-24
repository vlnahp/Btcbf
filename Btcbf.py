import os
from bitcoin import privkey_to_address
import codecs
import hashlib
import base58
import mmap
from tqdm import tqdm
import sys
for a in tqdm(range(int(10e15))):
      pass
      a = os.urandom(32).hex()
      padding = '80' + a
      # print( padding ) 
      hashedVal = hashlib.sha256(codecs.decode(padding, 'hex')).hexdigest()
      checksum = hashlib.sha256(codecs.decode(hashedVal, 'hex')).hexdigest()[:8]
      # print( hashedVal )
      # print( padding+checksum )
      payload = padding + checksum
      wif = base58.b58encode(codecs.decode(payload, 'hex'))
      #print(wif.decode('utf-8'))
      z = privkey_to_address(wif.decode("utf-8")).encode("utf-8")
      with open('address.txt') as f:
            s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            if s.find(z) != -1:
               print("true")
               print(a)
               print(z)
               print( wif.decode('utf-8') )
               sys.stdout = open("foundkey.txt", "w")
               print(a)
               print(z)
               print( wif.decode('utf-8') )
               sys.stdout.close()
               exit()
            #else: 
               #print ('false')
               #print(wif.decode("utf-8"))
               #print(z)

