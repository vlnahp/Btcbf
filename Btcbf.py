import requests
from bit import Key
from time import sleep, time
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from multiprocessing import Manager, Process

if os.path.exists(os.getcwd()+"/cache.txt") == False:
    open("cache.txt", "w+")


class Btcbf():

    def __init__(self):
        self.cores = 0
        self.prev_n = 0
        self.start_n = 0
        self.end_n = 0
        self.seq = False
        self.privateKey = None
        self.start_r = 0
        load_data = open("address.txt", "r").readlines()
        load_data = [x.rstrip() for x in load_data]
        # Remove invalid wallet addresses
        load_data = [x for x in load_data if x.find(
            'wallet') == -1 and len(x) > 0]
        load_data = dict(zip(load_data, load_data))
        self.load_data = load_data

        self.process_list = []
        self.manager = Manager()

        # Declare threadsafe variables that are sharable across the processes
        self.cur_n = self.manager.Value('i', 0)
        self.start_t = self.manager.Value('i', 0)

        # Whether we use `Process` or `ThreadPoolExecutor` to run the task
        self.use_process = False

    def speed(self):
        while True:
            if self.cur_n.value != 0:
                cur_t = time()
                n = self.cur_n.value
                if self.prev_n == 0:
                    self.prev_n = n
                elapsed_t = cur_t-self.start_t.value
                print("current n: "+str(n)+", current rate: "+str(abs(n-self.prev_n)//2)+"/s" +
                      f", elapsed time: [{str(elapsed_t//3600)[:-2]}:{str(elapsed_t//60%60)[:-2]}:{int(elapsed_t%60)}], total: {n-self.start_r} ", end="\r")
                self.prev_n = n
                if self.seq:
                    open("cache.txt", "w").write(
                        f"{self.cur_n.value}-{self.start_r}-{self.end_n}")
            sleep(2)

    def random_brute(self):
        key = Key()
        if key.address in self.load_data.keys():
            print("Wow matching address found!!")
            print("Public Adress: "+key.address)
            print("Private Key: "+key.to_wif())
            # the found privatekey and address saved to "foundkey.txt"
            f = open("foundkey.txt", "a")
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(510)
            exit()

    def random_brute_process(self, cur_n, core_number):
        print(f'Starting core {core_number} ... \n')

        count = 0
        r = range(100000000000000000)
        for _ in r:
            self.random_brute()

            count = count + 1

            # Wait until we executed 10000 times, then we will update the variable since updating a threadsafe variable is a big cost
            # Doing this, we can improve the performance significantly
            if count == 10000:
                cur_n.value = cur_n.value + count
                count = 0

        print("Stopping\n")

    def sequential_brute(self, n):
        self.cur_n.value = n
        key = Key().from_int(n)
        if key.address in self.load_data.keys():
            print("Wow matching address found!!")
            print("Public Adress: "+key.address)
            print("Private Key: "+key.to_wif())
            # the found privatekey and address saved to "foundkey.txt"
            f = open("foundkey.txt", "a")
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()

    def random_online_brute(self, n):
        self.cur_n.value = n
        key = Key()
        the_page = requests.get(
            "https://blockchain.info/q/getreceivedbyaddress/"+key.address+"/").text
        if int(the_page) > 0:
            print(the_page)
            print("Wow active address found!!")
            print(key.address)
            print(key.to_wif())
            # the found privatekey and address saved to "foundkey.txt"
            f = open("foundkey.txt", "a")
            f.write(key.address+"\n")
            f.write(key.to_wif()+"\n")
            f.close()
            sleep(500)
            exit()

    def num_of_cores(self):
        available_cores = cpu_count()
        cores = input(
            f"\nNumber of available cores: {available_cores}\n \n How many cores to be used? (leave empty to use all available cores) \n \n Type something>")

        if cores == "":
            self.cores = int(available_cores)
        elif cores.isdigit():
            cores = int(cores)
            if 0 < cores <= available_cores:
                self.cores = cores
            elif cores <= 0:
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

        print('\n')

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
        user_input = input(
            "\n What do you want to do? \n \n   [1]: generate random key pair \n   [2]: generate public address from private key \n   [3]: brute force bitcoin offline mode \n   [4]: brute force bitcoin online mode \n   [0]: exit \n \n Type something>")
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
            method_input = input(
                " \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input == "1":
                target = self.random_brute_process
                self.use_process = True
            elif method_input == "2":
                if open("cache.txt", "r").read() != "":
                    r0 = open("cache.txt").read().split("-")
                    print(f"resume range {r0[0]}-{r0[2]}")
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\nResuming ...\n")
                        self.start_t.value = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq = True
                        for i in range(self.start_n, self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Stopping\n")
                        exit()
                else:
                    range0 = input(
                        "\n Enter range in decimals(example:1-100)>")
                    r0 = range0.split("-")
                    r0.insert(1, r0[0])
                    open("cache.txt", "w").write("-".join(r0))
                    with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                        print("\n Starting ...")
                        self.start_t.value = time()
                        self.start_r = int(r0[1])
                        self.start_n = int(r0[0])
                        self.end_n = int(r0[2])
                        self.seq = True
                        for i in range(self.start_n, self.end_n):
                            pool.submit(self.sequential_brute, i)
                        print("Stopping\n")
                        exit()
            else:
                print("exitting...")
                exit()
        elif user_input == "4":
            method_input = input(
                " \n Enter the desired number: \n \n   [1]: random attack \n   [2]: sequential attack \n   [0]: exit \n \n Type something>")
            if method_input == "1":
                target = self.random_online_brute
            elif method_input == "2":
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

        if self.use_process:
            self.start_t.value = time()
            self.start_n = 0

            self.num_of_cores()
            for core_number in range(0, self.cores):
                process = Process(target=target, args=(
                    self.cur_n, core_number))
                self.process_list.append(process)

            for process in self.process_list:
                process.start()

            for process in self.process_list:
                process.join()

            print("Stopping\n")
            exit()
        else:
            with ThreadPoolExecutor(max_workers=self.num_of_cores()) as pool:
                r = range(100000000000000000)
                print("\n Starting ...")
                self.start_t.value = time()
                self.start_n = 0
                for i in r:
                    pool.submit(target, i)
                print("Stopping\n")
                exit()


if __name__ == "__main__":
    obj = Btcbf()
    try:
        t0 = threading.Thread(target=obj.get_user_input)
        t1 = threading.Thread(target=obj.speed)
        t1.daemon = True
        t0.daemon = True
        t0.start()
        t1.start()
        sleep(4000000)  # stay in the `try..except`
        sleep(4000000)  # stay in the `try..except`
    except KeyboardInterrupt:
        print("\n\nCtrl+C pressed. \nexitting...")
        exit()
    else:
        print(f"\n\nError: {Exception.args}\n")
        exit()
