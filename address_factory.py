from bit import Key
from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey
import random
import string
from bitcoinaddress import Wallet
from mnemonic import Mnemonic
from hdwallet.utils import is_mnemonic
from hdwallet import *
import bitcoinlib.wallets
import bitcoinlib.keys as Keys


class Address(object):
    address: list = list()

    def getAdrs(self):
        return self.address


class Lib1(Address):

    def __init__(self) -> None:
        super().__init__()
        self.GetAddress()

    def GetAddress(self):
        key = Key()
        self.address.clear()
        self.address.append([key.address, key.to_wif(), "Lib1"])

class Lib2(Address):
    MAX = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.GetAddress1()
        self.GetAddress2()
        # self.GetAddress3()

    def GetAddress3(self):

        for x in range(5):
            setup('mainnet')
            xx = random.randint(1,self.MAX)
            priv = PrivateKey(secret_exponent=xx)
            pub = priv.get_public_key()
            address = pub.get_address()
            self.address.append(
                [address.to_string(), priv.to_wif(), priv.to_bytes()])

    def GetAddress2(self):
        setup('mainnet')
        priv = PrivateKey()

        pub = priv.get_public_key()

        address = pub.get_address()

        self.address.append(
            [address.to_string(), priv.to_wif(), priv.to_bytes()])

    def GetAddress1(self):
        setup('mainnet')
        x = random.randrange(
            1, self.MAX)
        priv = PrivateKey(secret_exponent=x)

        pub = priv.get_public_key()

        address = pub.get_address()
        self.address.append(
            [address.to_string(), priv.to_wif(), priv.to_bytes()])

class Lib3(Address):
    MAINNET = "mainnet"
    PUBADDR1 = "pubaddr1"
    PUBADDR1C = "pubaddr1c"
    PUBADDR3 = "pubaddr3"
    PUBADDRBC1_P2WPKH = "pubaddrbc1_P2WPKH"
    PUBADDRBC1_P2WSH = "pubaddrbc1_P2WSH"
    WIF = "wif"
    HEX = "hex"

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_Add3()
        self.get_Add4()
        self.get_Add5()
        #self.get_Add1()
        self.get_Add2()
        self.get_Add6()

    def get_Add1(self):
        wallet = Wallet()
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        adr1 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1]
        self.address.append([adr1, key, hex_])
        adr2 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1C]
        self.address.append([adr2, key, hex_])
        adr3 = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR3]
        self.address.append([adr3, key, hex_])
        adr4 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WSH]
        self.address.append([adr4, key, hex_])
        adr5 = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WPKH]
        self.address.append([adr5, key, hex_])

    def get_Add6(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WPKH]
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add2(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1C]
        key = wallet.key.__dict__[self.MAINNET].__dict__[self.WIF]
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add3(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[
            self.MAINNET].__dict__[self.PUBADDRBC1_P2WSH]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add4(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR3]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

    def get_Add5(self):
        wallet = Wallet()
        adr = wallet.address.__dict__[self.MAINNET].__dict__[self.PUBADDR1]
        key = (wallet.key.__dict__[self.MAINNET].__dict__[self.WIF])
        hex_ = wallet.key.__dict__[self.HEX]
        self.address.append([adr, key, hex_])

class Lib4(Address):

    def __init__(self) -> None:
        super().__init__()
        self.language = "english"
        self.address.clear()
        self.get_addr1()
        self.get_addr3()
        self.get_addr2()
        self.get_addr4()
        self.get_addr5()
        self.get_addr6()
        self.get_addr7()
        self.get_addr8()

    def get_addr8(self):

        i: BIP49HDWallet = BIP49HDWallet()
        wo = Mnemonic(self.language).generate()

        h = is_mnemonic(wo)
        if h:
            i.from_mnemonic(wo)
            add2 = i.p2wsh_in_p2sh_address()
            self.address.append([add2, i.wif(), wo])

    def get_addr7(self):
        try:
            i: BIP49HDWallet = BIP49HDWallet()
            m = Mnemonic(self.language)
            wo = m.generate(strength=128)
            h = is_mnemonic(wo)
            if h:
                i.from_mnemonic(wo)
                add2 = i.p2wsh_in_p2sh_address()
                self.address.append([add2, i.wif(), wo])

        except BaseException as e:
            print(e)

    def get_addr2(self):
        i: BIP44HDWallet = BIP44HDWallet()

        m = Mnemonic(self.language)
        wo = m.generate(strength=128)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            add2 = i.p2wpkh_address()
            self.address.append([add2, i.wif(), wo])

    def get_addr3(self):
        i: BIP44HDWallet = BIP44HDWallet()
        m = Mnemonic(self.language)
        wo = m.generate(strength=128)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            addr3 = i.p2wsh_address()
            self.address.append([addr3, i.wif(), wo])

    def get_addr1(self):
        i: BIP44HDWallet = BIP44HDWallet()

        m = Mnemonic(self.language)
        wo = m.generate(strength=128)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            addr = i.p2wsh_in_p2sh_address()
            self.address.append([addr, i.wif(), wo])

    def get_addr4(self):
        i: BIP44HDWallet = BIP44HDWallet()

        m = Mnemonic(self.language)
        wo = m.generate(strength=256)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            add2 = i.p2wpkh_address()
            self.address.append([add2, i.wif(), wo])

    def get_addr5(self):
        i: BIP44HDWallet = BIP44HDWallet()

        m = Mnemonic(self.language)
        wo = m.generate(strength=256)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            addr3 = i.p2wsh_address()
            self.address.append([addr3, i.wif(), wo])

    def get_addr6(self):
        i: BIP44HDWallet = BIP44HDWallet()
        m = Mnemonic(self.language)
        wo = m.generate(strength=256)
        h = is_mnemonic(mnemonic=wo)
        if h:
            i.from_mnemonic(wo)
            addr = i.p2wsh_in_p2sh_address()
            self.address.append([addr, i.wif(), wo])

class Lib5(Address):
    LANGUAGE = 'english'
    SEGWIT = 'segwit'
    P2SH_SEGWIT = 'p2sh-segwit'
    BITCOIN = 'bitcoin'

    def __init__(self) -> None:
        super().__init__()
        self.address.clear()
        self.get_adr1()
        self.get_adr2()
        self.get_adr3()
        #self.get_adr4()
        self.get_adr5()
        self.get_adr6()

    def get_adr1(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        
        w = bitcoinlib.wallets.wallet_create_or_open(name, keys=p, network=self.BITCOIN)
        key_ = w.get_key()
        wif = key_.wif
        address = key_.address
        self.address.append([address, wif, p])

    def get_adr2(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=p, network=self.BITCOIN, witness_type=self.SEGWIT)
        key_ = w.get_key()
        wif = key_.wif
        address = key_.address
        self.address.append([address, wif, p])

    def get_adr3(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        p = Mnemonic(language=self.LANGUAGE).generate()
        
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=p, network=self.BITCOIN, witness_type=self.P2SH_SEGWIT)
        key_ = w.get_key()
        wif = key_.wif
        address = key_.address
        self.address.append([address, wif, p])

    def get_adr4(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        w = bitcoinlib.wallets.wallet_create_or_open(
            name, keys=[Keys.HDKey(), Keys.HDKey().public()], network=self.BITCOIN)
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, "Lib5"])

    def get_adr5(self):
        name = random.choice(string.ascii_letters)
        bitcoinlib.wallets.wallet_delete_if_exists(name)
        w = bitcoinlib.wallets.wallet_create_or_open(name, network=self.BITCOIN)
        key_ = w.get_key()
        self.address.append([key_.address, key_.wif, "Lib5"])

    def get_adr6(self):
        k = Keys.HDKey(multisig=True)
        self.address.append([k.address(),k.private_byte,k.private_hex])
        
class AddressFact():
    def createAdress(self, typ):
        targetclass = typ
        return globals()[targetclass]()



    
