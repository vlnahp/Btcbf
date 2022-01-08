import requests
import json
from bit import Key
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from time import sleep

with open("address.txt", "r") as file:
    s = file.read()


def generate_private_key():
    return Key()


def check_list(n):
    privkey = generate_private_key()
    z = privkey.address
    if s.find(z) != -1:
        wif = privkey.to_wif()
        print("Wow matching address found!!")
        print(z)
        print(wif)
        with open("foundkey.txt", "a") as result: # Save found keys to "foundkey.txt"
            result.write(f"address: {z}\nwif: {wif}\n===")
     #else: # uncommenting this part makes our code slow down
         #print ('false')
         #print(privkey.to_wif())
         #print(z)


def check_list_online(n):
    privkey = generate_private_key()
    wif = privkey.to_wif()
    z = privkey.address
    url = requests.get("https://blockchain.coinmarketcap.com/api/address?address="+str(z)+"&symbol=BTC&start=1&limit=10")
    data = json.loads(url.text)
    if data['transaction_count'] > 0:
        print(data['transaction_count'])
        print("Wow active address found!!")
        print(z)
        print(wif)
        with open("foundkey.txt", "a") as result: # Save found keys to "foundkey.txt"
            result.write(f"address: {z}\nwif: {wif}\n===")
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
    print("Public Address: " + privkey.address)
    print("Private Key: " + privkey.to_wif())


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
