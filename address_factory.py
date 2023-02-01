from bit import Key
from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey
import random
from bitcoinaddress import Wallet
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import *

class Address(object):
    address : list = list()
    def getAdrs(self):
        return self.address
    
class Lib1(Address):
    
    address:list =list()
    
    def __init__(self) -> None:
        super().__init__()
        self.GetAddress()
    def GetAddress(self):
        key = Key()
        #self.address.append( [key.address,key.to_wif(),key.pub_to_hex()])
        self.address.clear()
        self.address.append( [key.address,key.to_wif(),"Lib1"])

class Lib2(Address):
    address:list=list()
    def __init__(self) -> None:
        super().__init__()
        self.address.clear() 
        self.GetAddress1()
        self.GetAddress2()
    def GetAddress2(self):
        setup('mainnet')
        priv = PrivateKey()
        pub = priv.get_public_key()
        address = pub.get_address()
        self.address.append([address.to_string(),priv.to_wif(),"lib2"])
    def GetAddress1(self):
        setup('mainnet')
        x = random.randint(1,115792089237316195423570985008687907852837564279074904382605163141518161494337)
        priv = PrivateKey(secret_exponent=x)
        pub = priv.get_public_key()
        address = pub.get_address()
        self.address.append([address.to_string(),priv.to_wif(),"lib2"])
        
class Lib3(Address):
    address:list=[]
    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_Add3()
        self.get_Add4()
        self.get_Add5()
        
    def get_Add3(self):
        wallet = Wallet()
        adr = wallet.address.__dict__['mainnet'].__dict__['pubaddrbc1_P2WSH']
        key = (wallet.key.__dict__['mainnet'].__dict__['wifc'])
        self.address.append([adr,key,0])
            
    def get_Add4(self):
        wallet = Wallet()
        adr = wallet.address.__dict__['mainnet'].__dict__['pubaddr3']
        key = (wallet.key.__dict__['mainnet'].__dict__['wifc'])
        self.address.append( [adr,key,0])
        

    def get_Add5(self):
        wallet = Wallet()
        adr = wallet.address.__dict__['mainnet'].__dict__['pubaddr1']
        key = (wallet.key.__dict__['mainnet'].__dict__['wifc'])
        self.address.append( [adr,key,0])
        
class Lib4(Address):
    address : list = list()
    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_addr1()
        self.get_addr3()
        self.get_addr2()
        self.get_addr4()
        self.get_addr5()
        self.get_addr6()
    
    def get_addr2(self):
        i : BIP44HDWallet = BIP44HDWallet()
        
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=128)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        
        add2 = i.p2wpkh_address()
        self.address.append([add2,i.wif(),wo])
        
    def get_addr3(self):
        i : BIP44HDWallet = BIP44HDWallet()
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=128)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        
        addr3 = i.p2wsh_address()
        
        self.address.append([addr3,i.wif(),wo])
        
        
    def get_addr1(self):
        i : BIP44HDWallet = BIP44HDWallet()
        passphrase:str =None
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=128)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        addr = i.p2wsh_in_p2sh_address()
        
        
        self.address.append([addr,i.wif(),wo])    
    
        
    def get_addr4(self):
        i : BIP44HDWallet = BIP44HDWallet()
        
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=256)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        
        add2 = i.p2wpkh_address()
        self.address.append([add2,i.wif(),wo])
        
    def get_addr5(self):
        i : BIP44HDWallet = BIP44HDWallet()
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=256)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        
        addr3 = i.p2wsh_address()
        
        self.address.append([addr3,i.wif(),wo])
        
        
    def get_addr6(self):
        i : BIP44HDWallet = BIP44HDWallet()
        passphrase:str =None
        language:str = "english"
        
        m = Mnemonic("english")
        wo = m.generate(strength=256)
        h= is_mnemonic(mnemonic=wo,language='english')
        i.from_mnemonic(wo,language=language)
       
        addr = i.p2wsh_in_p2sh_address()
        
        
        self.address.append([addr,i.wif(),wo])    
    
class AddressFact():
    def createAdress(self,typ):
        targetclass = typ
        return globals()[targetclass]()
  
