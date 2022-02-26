import requests
import json
from bit import Key
from multiprocessing import Pool, cpu_count, freeze_support
from time import sleep, time


time_0 = time()
load_data = open("address.txt", "r").read()
prev_t = 0
prev_n=0


def random_brute(n):
    global prev_t,prev_n
    key = Key()
    time_cur=time()
    elapsed_t = int(time_cur-time_0)
    # speed algo
    if elapsed_t>(prev_t + 5):
        print("current n: "+str(n)+", current rate: "+str((n-prev_n)/5)+"/s"+", elapsed time: "+str(elapsed_t/60)+"minutes\r", end="\r")
        prev_t=elapsed_t
        prev_n=n
    if load_data.find(key.address) != -1:
            print("Wow matching address found!!")
            print("Public Adress: "+key.address)
            print("Private Key: "+key.to_wif())
            f = open("foundkey.txt", "a") # the found key and address saved to "foundkey.txt"
            f.write(key.address)
            f.write(key.to_wif())
            f.close()
            sleep(500)
            exit()
            
            
            
def random_online_brute(n):
    global prev_t,prev_n
    key = Key()
    time_cur=time()
    elapsed_t = int(time_cur-time_0)
    # speed algo
    if elapsed_t >(prev_t + 5):
        print("current n: "+str(n)+", current rate: "+str((n-prev_n)/5)+"/s"+", elapsed time: "+str(elapsed_t/60)+"minutes\r", end="\r")
        prev_t=elapsed_t
        prev_n=n
    url = requests.get("https://blockchain.info/q/getreceivedbyaddress/"+key.address+"/")
    if int(url.text)>0:
        print(url.text['transaction_count'])
        print("Wow active address found!!")
        print(key.address)
        print(key.to_wif())
        f = open("foundkey.txt", "a") # the found key and address saved to "foundkey.txt"
        f.write(key.address+"\n")
        f.write(key.to_wif()+"\n")
        f.close()
        sleep(500)
        exit()

            
            
def num_of_cores():
    available_cores = cpu_count()
    cores = input("\navailable number of cores: "+str(available_cores)+"\n \n How many cores to be used? (leave empty to use all available cores) \n \n Type something>")
    if cores == "":
        cores = int(available_cores)
    elif cores.isdigit():
        if 0 < int(cores) <= available_cores:
            pass
        elif int(cores)<=0 :
            print("Hey you can't use negative number of cpu cores!!")
            input("Press Enter to exit")
            exit()
        elif int(cores) > available_cores:
            print("\n You only have "+str(available_cores)+" cores")
            print(" Are you sure you want to use {0} cores?".format(cores))
            core_input = input("\n [y] or [n]>")
            if core_input == "y":
                cores = int(cores)
            else:
                print("using available number of cores")
                cores = int(available_cores)
        return cores
    else:
        print("Wrong input!")
        input("Press Enter to exit")
        exit()

def generate_random_address():
    key = Key()
    print("\n Public Address: "+key.address)
    print(" Private Key: "+key.to_wif())
    
def generate_address_fromKey(privateKey):
    if privateKey != "":
        key = Key(privateKey)
        print("\n Public Address: "+key.address)
        print("\n Your wallet is ready!")
    else:
        print("no entry")


def multiprocessing():
    if __name__ == "__main__":
        freeze_support()
        user_input = input("\n What do you want to do? \n \n   [1]: generate random key pair \n   [2]: generate public address from private key \n   [3]: brute force bitcoin offline mode \n   [4]: brute force bitcoin online mode \n   [0]: exit>> \n \n Type something>")
        if user_input == "1":
            generate_random_address()
            print("\n Your wallet is ready!")
            input("\n Press Enter to exit")
            exit()
        if user_input == "2":
            private_key = input("\n Enter Private Key>")
            try:
                generate_address_fromKey(private_key)
            except:
                print("\n incorrect key format")
            input("Press Enter to exit")
            exit()
        elif user_input == "3":
            method_input = input(" \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input=="1":
                target = random_brute
            elif method_input=="2":
                print("sequential attack will be available soon!")
                input("Press Enter to exit")
                exit()
            else:
                print("exitting...")
                exit()
            cores_to_be_used = num_of_cores()
        elif user_input == "4":
            method_input = input(" \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input=="1":
                target = random_online_brute
            elif method_input=="2":
                print("sequential attack will be available soon!")
                input("Press Enter to exit")
                exit()
            else:
                print("exitting...")
                exit()
            cores_to_be_used = num_of_cores()
        elif user_input == "0":
            print("exitting")
            sleep(2)
            exit()
        else:
            print("No input. <1> chosen automatically")
            generate_random_address()
            print("Your wallet is ready!")
            input("Press Enter to exit")
            exit()
        with Pool(processes=int(cores_to_be_used)) as pool:
            r = range(100000000000000000)
            print("Starting ...")
            results = pool.imap_unordered(target, r)
            print("Running ...")
            tuple(results)
            print("Stopping")
            print()
if __name__ =="__main__":
    multiprocessing()
