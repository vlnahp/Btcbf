# BTCBF                                                                
This repo is a fork of this [repo](https://github.com/vlnahp/Btcbf). This repo fixes bugs and optimized the bruteforce speed.

## **Description**

A fast and efficient bitcoin private key bruteforce application written in python. The method is based on the generation of random private keys and their corresponding public address. The public address is searched in a list to see if it matches any.

It is fast because the number of loops is multiplied by the number of addresses available in the list. It means if your CPU processes 500 loops per second and 10000 addresses are in the list 5 milion possibilities are checked per second. However, there are 2^256 possibilities to check.  

## The Goal
Is to prove bitcoin is secure.

## **Setup**

The "wallets.txt" file contains a list of bitcoin addresses. These are used are used to compare against. [Top 100 richest](https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html)

1. Install [Python](https://www.python.org/downloads/)
2. Download this repo:

`$ git clone https://github.com/meesvw/Btcbf.git`

3. Install requirements:

`$ pip install -r requirements.txt`

4. Run the code:

`$ python3 btcbf.py`

## **Donation**
> NANO: nano_3hsbm1yhsio64gs9u8gi4hqhapydmmn9n6m8g6ijktfukjkp5bisjxm8wh6r
