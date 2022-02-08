import requests
import json
from bit.crypto import ECPrivateKey
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from time import sleep
from bit.format import bytes_to_wif, public_key_to_address

s= open("address.txt", "r").read()

def generate_private_key():
    private_key = ECPrivateKey()
    return private_key
    
def check_list(n):
    privkey = generate_private_key()
    wif = bytes_to_wif(privkey.secret, compressed=True)
    z = public_key_to_address(privkey.public_key.format())
    if s.find(z) != -1:
            print("Wow matching address found!!")
            print(z)
            print(wif)
            f = open("foundkey.txt", "a") # the found key and address saved to "foundkey.txt"
            f.write(z)
            f.write(wif)
            f.close()
        #else: # uncommenting this part makes our code slow down
            #print ('false')
            #print(wif.decode("utf-8"))
            #print(z)
            
def check_list_online(n):
    privkey = generate_private_key()
    wif = bytes_to_wif(privkey.secret, compressed=True) #private.wif(compressed=False) 
    z = public_key_to_address(privkey.public_key.format()).encode("utf-8")
    url = requests.get("https://blockchain.coinmarketcap.com/api/address?address="+str(z)+"&symbol=BTC&start=1&limit=10")
    data = json.loads(url.text)
    if data['transaction_count']>0:
        print(data['transaction_count'])
        print("Wow active address found!!")
        print(z.decode('utf-8'))
        print(wif)
        f = open("foundkey.txt", "a") # the found key and address saved to "foundkey.txt"
        f.write(z.decode('utf-8'))
        f.write(wif)
        f.close()
        exit()

            
            
def num_of_cores():
    available_cores = cpu_count()
    cores = input("How many cores to be used? (leave empty to use all available cores): ")
    num = 0
    if cores == "":
        num = int(available_cores)
    elif cores.isdigit():
        if 0 < int(cores) <= available_cores:
            num = int(cores)
        elif int(cores)<=0 :
            print("Hey you can't use negative number of cpu cores!!")
            sleep(5)
            exit()
        elif int(cores) > available_cores:
            print("Haha, you only have "+str(available_cores)+" cores. So we use "+str(available_cores)+" cores!!")
            num = int(available_cores)
    else:
        print("Wrong input!")
        print("exitting...")
        sleep(5)
        exit()
    return num

def generate():
    privkey = generate_private_key()
    print("Public Address: "+public_key_to_address(privkey.public_key.format()))
    print("Private Key: "+bytes_to_wif(privkey.secret, compressed=True))


def multiprocessing():
    if __name__ == "__main__":
        inp = input("What do you want to do? <<options: [gen]: generate wallet address and private key, [brute1]: brute force bitcoin offline, [brute2]: brute force bitcoin online, [exit]: exit>> ")
        if inp == "gen":
            generate()
            print("Your wallet is ready!")
            e = input("Press any key to exit")
            exit()
        elif inp == "exit":
            print("exitting")
            sleep(5)
            exit()
        elif inp == "brute1":
            target = check_list
            processn = num_of_cores()
        elif inp == "brute2":
            print("OK I will consume whole your internet")
            target = check_list_online
            processn = num_of_cores()
        else:
            print("No input. <gen> chosen automatically")
            generate()
            print("Your wallet is ready!")
            f = input("Press any key to exit")
            exit()
        with Pool(processes=processn) as pool:
            r = range(100000000000000000)
            print("Starting ...")
            results = tqdm(pool.imap_unordered(target, r), total=10e15)
            print("Running ...")
            tuple(results)
            print("Stopping")
            print()
multiprocessing()
