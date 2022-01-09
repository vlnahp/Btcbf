from bit import Key
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

with open('wallets.txt', 'r') as file:
  wallets = file.read()

def RBF(r):
  for _ in range(1000000):
    pk = Key()
    if pk.address in wallets:
      print(f'Found: {pk.address}')
      with open(f'./{pk.address}', 'w') as result:
        result.write(f'{pk.to_wif()}')

with ProcessPoolExecutor() as executor:
  print(f'Running on {cpu_count()} cores')
  executor.map(RBF, range(cpu_count()))
print('Done...')
