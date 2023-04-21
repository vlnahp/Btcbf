
# Btcbf  [![CodeFactor](https://www.codefactor.io/repository/github/vlnahp/btcbf/badge/main)](https://www.codefactor.io/repository/github/vlnahp/btcbf/overview/main)
Btcbf is a fast and efficient bitcoin private key brute force tool written in python. It works based on generating random or sequential private keys and their corresponding public address. Then checking the address through an online API or an offline database.

What makes Btcbf fast, is mainly the bit library. Thanks to its developer!

## **Quick Start**
```
 $ git clone https://github.com/vlnahp/Btcbf.git

 $ cd Btcbf

 $ pip install -r requirements.txt

 $ python Btcbf.py or  $ python3 Btcbf.py on Linux
```






## The Goal
The main goal is to ~~prove bitcoin is secure. At least until the day that Quantum computers start working against it~~ learn python! 

There are also some useful tools implemented.



## **Requirements**

  In offline mode, a database is necessary. By default, it is `address.txt` containing some addresses. Let's be honest, searching online takes too long and the addresses with balance included in the program are too scarce (as having a current text file with all addresses would make this repository over 5GB). So the users who wish, can download the latest text file from [here](http://addresses.loyce.club/) (direct [link](http://addresses.loyce.club/Bitcoin_addresses_LATEST.txt.gz)), rename and replace it with the "address.txt". But be careful about memory issues. Only use this database if you have sufficient RAM!

To install the requirements run the command below:

```$ pip install -r requirements.txt```  


## **Usage**
Just execute this command: `$ python Btcbf.py` or `$ python3 Btcbf.py` on Linux, Btcbf tells you what to do!

Type your desired action and follow instructions. (I love to interact with my program🙂)

Results will be saved to `foundkey.txt` in the main directory.

## **Licence**

Permissions of this strongest copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights. When a modified version is used to provide a service over a network, the complete source code of the modified version must be made available.




## Latest Release
Link to latest release(v1.2.0): [link](https://github.com/vlnahp/Btcbf/releases/download/v1.2.1/Btcbf-windows64-v.1.2.0.tar.xz)
