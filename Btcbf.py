import urllib
from bit import Key
from time import sleep, time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

if os.path.exists(os.getcwd()+"/cache.txt") == False:
    open("cache.txt", "w+")

class Btcbf():
    def __init__(self):
        self.start_t = 0
        self.prev_n = 0
        self.cur_n = 0
        self.start_n = 0
        self.end_n = 0
        self.seq = False
        self.privateKey = None
        self.start_r = 0
        self.load_data = open("address.txt", "r").read()

        
    def speed(self):
        while True:
            if self.cur_n != 0:
                cur_t = time()
                n = self.cur_n
                if self.prev_n == 0:
                    self.prev_n = n
                elapsed_t=cur_t-self.start_t
                print("current n: "+str(n)+", current rate: "+str(abs(n-self.prev_n)//2)+"/s"+f", elapsed time: [{str(elapsed_t//3600)[:-2]}:{str(elapsed_t//60%60)[:-2]}:{int(elapsed_t%60)}], total: {n-self.start_r} ", end="\r")
                self.prev_n = n
                if self.seq:
                    open("cache.txt","w").write(f"{self.cur_n}-{self.start_r}-{self.end_n}")
            sleep(2)
        
    def random_brute(self, n):
        self.cur_n=n
        key = Key()
        if  self.load_data.find(key.address) != -1:
                print("Wow matching address found!!")
                print("Public Adress: "+key.address)
                print("Private Key: "+key.to_wif())
                f = open("foundkey.txt", "a") # the found privatekey and address saved to "foundkey.txt"
                f.write(key.address+"\n")
                f.write(key.to_wif()+"\n")
                f.close()
                sleep(500)
                exit()
            
    def sequential_brute(self, n):
        self.cur_n=n
        key = Key().from_int(n)
        if self.load_data.find(key.address) != -1:
            print("Wow matching address found!!")
            print("Public Adress: "+key.address)
            print("Private Key: "+key.to_wif())
            f = open("foundkey.txt", "a") # the found privatekey and address saved to "foundkey.txt"
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()
    
    
    def random_online_brute(self, n):
        self.cur_n = n
        key = Key()
        url = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/"+key.address+"/")
        if int(url.read())>0:
            print(url.read())
            print("Wow active address found!!")
            print(key.address)
            print(key.to_wif())
            f = open("foundkey.txt", "a") # the found privatekey and address saved to "foundkey.txt"
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()
            
            
            
    def num_of_cores(self):
        available_cores = cpu_count()
        cores = input(f"\nNumber of available cores: {available_cores}\n \n How many cores to be used? (leave empty to use all available cores) \n \n Type something>")
        if cores == "":
            self.cores = int(available_cores)
        elif cores.isdigit():
            cores = int(cores)
            if 0 < cores <= available_cores:
                self.cores = cores
            elif cores<=0 :
                print(f"Hey you can't use {cores} number of cpu cores!!")
                input("Press Enter to exit")
                raise ValueError("negative number!")
            elif cores > available_cores:
                print(f"\n You only have {available_cores} cores")
                print(f" Are you sure you want to use {cores} cores?")
                core_input = input("\n[y]es or [n]o>")
                if core_input == "y":
                    self.cores = cores
                else:
                    print("using available number of cores")
                    self.cores = available_cores
        else:
            print("Wrong input!")
            input("Press Enter to exit")
            exit()
            
    def generate_random_address(self):
        key = Key()
        print("\n Public Address: "+key.address)
        print(" Private Key: "+key.to_wif())
    
    def generate_address_fromKey(self):
        if self.privateKey != "":
            key = Key(self.privateKey)
            print("\n Public Address: "+key.address)
            print("\n Your wallet is ready!")
        else:
            print("no entry")
            
    def get_user_input(self):
        user_input = input("\n What do you want to do? \n \n   [1]: generate random key pair \n   [2]: generate public address from private key \n   [3]: brute force bitcoin offline mode \n   [4]: brute force bitcoin online mode \n   [0]: exit \n \n Type something>")
        if user_input == "1":
            self.generate_random_address()
            print("\n Your wallet is ready!")
            input("\n Press Enter to exit")
            exit()
        elif user_input == "2":
            self.privateKey = input("\n Enter Private Key>")
            try:
                self.generate_address_fromKey()
            except:
                print("\n incorrect key format")
            input("Press Enter to exit")
            exit()
        elif user_input == "3":
            method_input = input(" \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input=="1":
                target = self.random_brute
            elif method_input=="2":
                if open("cache.txt", "r").read() != "":
                    r0=open("cache.txt").read().split("-")
                    print(f"resume range {r0[0]}-{r0[2]}")
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\nResuming ...\n")
                        self.start_t = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq=True
                        for i in range(self.start_n,self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Stopping\n")
                        exit()
                else:
                    range0 = input("\n Enter range (example:1-100)>")
                    r0 = range0.split("-")
                    r0.insert(1,r0[0])
                    open("cache.txt", "w").write("-".join(r0))
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\n Starting ...")
                        self.start_t = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq=True
                        for i in range(self.start_n,self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Stopping\n")
                        exit()
            else:
                print("exitting...")
                exit()
        elif user_input == "4":
            method_input = input(" \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input=="1":
                target = self.random_online_brute
            elif method_input=="2":
                print("sequential online attack will be available soon!")
                input("Press Enter to exit")
                exit()
            else:
                print("exitting...")
                exit()
        elif user_input == "0":
            print("exitting")
            sleep(2)
            exit()
        else:
            print("No input. <1> chosen automatically")
            self.generate_random_address()
            print("Your wallet is ready!")
            input("Press Enter to exit")
            exit()
        with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
            r = range(100000000000000000)
            print("\n Starting ...")
            self.start_t = time()
            self.start_n = 0
            for i in r:
                pool.submit(target, i)
            print("Stopping\n")
            exit()



if __name__ =="__main__":
        obj = Btcbf()
        try:
            t0 = threading.Thread(target=obj.get_user_input)
            t1 = threading.Thread(target=obj.speed)
            t1.daemon = True
            t0.daemon = True
            t0.start()
            t1.start()
            sleep(4000000) # stay in the `try..except`
            sleep(4000000) # stay in the `try..except`
        except KeyboardInterrupt:
            print("\n\nCtrl+C pressed. \nexitting...")
            exit()
        else:
            print(f"\n\nError: {Exception.args}\n")
            exit()
            
    
