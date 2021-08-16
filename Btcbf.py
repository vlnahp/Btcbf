from bit.crypto import ECPrivateKey
from bit.format import bytes_to_wif, public_key_to_address
import mmap
from tqdm import tqdm
from sys import stdout
from multiprocessing import Pool, cpu_count

def generate_private_key():
    private_key = ECPrivateKey()
    return private_key
    
def generate_address():
    address = public_key_to_address(generate_private_key().public_key.format())
    return address

def check_list(n):
    n
    z = generate_address().encode("utf-8")
    wif = bytes_to_wif(generate_private_key().secret)
    #print("Address: " + z.decode('utf-8')) #Uncomment in order to use as address generater
    #print("Pravate key: " + wif) #Uncomment in order to use as address generater
    with open('address.txt') as f:
                  s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) # search for the generated address in the "address.txt" 
                  if s.find(z) != -1:
                        print("Wow matching address found!!")
                        print(z.decode('utf-8'))
                        print(wif)
                        stdout = open("foundkey.txt", "w") # the found key and address saved to "foundkey.txt"
                        print(z.decode('utf-8'))
                        print(wif)
                        stdout.close()
                        exit()
                  #else: # uncommenting this part makes our code slow down
                        #print ('false')
                        #print(wif.decode("utf-8"))
                        #print(z)


def num_of_cores():
    available_cores = cpu_count()
    cores = input("How many cores to be used? (leave empty to use all available cores): ")
    if cores == "":
        return int(available_cores)
    if cores.isdigit():
        if 0 < int(cores) <= available_cores:
            return int(cores)
        if int(cores)<=0 :
            print("Hey you can't use negative number of cpu cores!!")
            exit()
        if int(cores) > available_cores:
            print("Haha, you only have "+str(available_cores)+" cores. So we use "+str(available_cores)+" cores!!")
            return int(available_cores)
    else:
        print("Wrong input!")
        exit()

def multiprocessing():
    if __name__ == "__main__":
        with Pool(processes=num_of_cores()) as pool:
            #progress_bar = tqdm(total=10e10)
            print("mapping ...")
            results = tqdm(pool.imap_unordered(check_list, range(100000000000000000)), total=10e10)
            print("running ...")
            tuple(results)  # fetch the lazy results
            print("done")

multiprocessing()
