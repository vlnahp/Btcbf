# Btcbf
**Description**

A fast and efficient bitcoin private key brute force written in python. The method is based on generation of random private keys and their corresponding public address; then searching each through a list of addresses with positive balance.

It is fast because the number of loops is multiplied by the number of addresses available in the list. It means if your CPU processes 500 loops per second; and 10000 addresses are in the list 5milion possibilities are checked per second. However, there are 2256 possibilities to check; so not fast enough anyway. Also, no api and internet connection needed!



**requirements**

  The "address.txt" file containing a list of public addresses.
  
  $ pip install -r requirements.txt


**Usage**
  $ python Btcbf.py
  
If any key found; a text file named "foundkey.txt" containing the found private key and public address is saved.


**donation**

Make my btc address a good option to be in the list![image](https://user-images.githubusercontent.com/87664667/126873155-0f4255de-d2cd-47a5-9449-2554167e5a05.png)


BTC: 19NZzAHSYoA448zjKapY2kn6BbyTGDY9Sj
