import math
import codecs
import secrets
class Encryption():
    # s = 'Attack at dawn. cover the face fuck the base spare njenga'
    # f = None
    # g = None
    # init = None
    # key = 'password'
    IV = secrets.token_hex(nbytes=3)

    def __init__(self, plaintext, passwd):
        self.key = passwd
        #self.string_to_binary(self.s, self.key)
        self.rot13(plaintext, passwd)

    # def rot13(self, plaintext, passwd):
    #     self.s = codecs.encode(plaintext, 'rot_13')
    #     print(f"rot13 ciphertext: {self.s}")
    #     self.string_to_binary(self.s, passwd, self.IV)

    def rot13(self, plaintext, passwd):

        alphabet2 = [i for i in '123456789,.?!@#$ %^&*()_+=-:/[]{}|']
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']
        rotated_plain_text = []
        #print(plaintext)
        row1 = alphabet[:13]
        row1_symb = alphabet2[:17]
        row2 = alphabet[13:]
        row2_symb = alphabet2[17:]
        print(f'row1 sym: {row1_symb}')
        print(f'row2 sym: {row2_symb}')
        for i in plaintext:
            if i in row1:
                rotated_plain_text.append(row2[row1.index(i)])
            if i in row2:
                rotated_plain_text.append(row1[row2.index(i)])
            if i in row1_symb:
                rotated_plain_text.append(row2_symb[row1_symb.index(i)])
            if i in row2_symb:
                rotated_plain_text.append(row1_symb[row2_symb.index(i)])
            # if i in alphabet2:
            #     rotated_plain_text.append(i)
        print('check out for this: ', rotated_plain_text)
        self.s = ''.join(rotated_plain_text)
        print(f'rotated-plain_text1xx: {self.s}')
        self.string_to_binary(self.s, passwd, self.IV)

    def string_to_binary(self, s, key, IV):
        self.ptextbin = bin(int.from_bytes(s.encode(), 'big'))[2:]
        self.init = bin(int.from_bytes(key.encode(), 'big')) [2:]
        self.IVbin = bin(int.from_bytes(IV.encode(), 'big'))[2:]
        

        print('Plain text in binary: ', self.ptextbin)
        print('IV in binary: ', self.IVbin)
        # print('key in binary:', self.init)


        #self.split(self.ptextbin)
        self.cipher_IV_xor(self.ptextbin, self.IVbin)

    def cipher_IV_xor(self, ptextbin, IVbin):
        IVbin_length = len(self.IVbin)
        cipher_length = len(self.ptextbin)
        x = math.ceil(cipher_length/IVbin_length)     
        self.IVbin *= x
        self.IVbin = self.IVbin[:len(self.ptextbin)] 
        print("padded cipher_IV_xor: ", self.IVbin)
        print(f"the length of ciphertext: {len(self.ptextbin)}")
        print(f"the length of the key: {len(self.IVbin)}")
        self.cIV_xor = '{1:0{0}b}'.format(len(self.ptextbin), int(self.ptextbin, 2) ^ int(self.IVbin, 2))
        print(f"XORed cipher and IV: {self.cIV_xor}")
        self.split(self.cIV_xor)

    def split(self, cIV_xor):
        if len(cIV_xor)% 2 > 0:
            self.ptfin = self.cIV_xor.zfill(len(self.cIV_xor) +1)
            print('PT with padded bits: {}, length: {}'.format(self.ptfin, len(self.ptfin)))
            self.padded = True
        else:
            self.ptfin = cIV_xor
            self.padded = False
        print(len(self.ptfin))
        a = len(self.ptfin)
        self.b = int(a/2)
    
        self.chunk1 = self.ptfin[:self.b]
        self.chunk2 = self.ptfin[self.b:]

        print(self.ptfin)
        print('Chunk 1:',self.chunk1)
        print('chunk 2:',self.chunk2)

        self.keychunk1Xor(self.chunk1, self.b)
        self.keychunk2Xor(self.chunk2)

    def keychunk1Xor(self, chunk1, b):
        self.init = bin(int.from_bytes(self.key.encode(), 'big'))[2:]
        #self.init = bin(int.from_bytes(key.encode(), 'big')) [2:]
        print('Key in Binary:', self.init)
        lenct = len(self.chunk1)
        lenkey = len(self.init)

        final_key = ""
        
        if(isinstance(lenct/lenkey, float)==True):
            div_num = int(lenct/lenkey)
            increment_num = div_num+1

        else:
            increment_num = int(lenct/lenkey)

        for i in range (0,increment_num):
            final_key+=self.init
        self.reverse(self.chunk1, self.b)

    def reverse(self, chunk1,b):
        self.f=chunk1[b-1::-1]
        print('Reversed Chunk:',self.f)
        

    def keychunk2Xor(self, chunk2):
        self.init = bin(int.from_bytes(self.key.encode(), 'big'))[2:]
        #self.init = bin(int.from_bytes(key.encode(), 'big')) [2:]
        print('Key in Binary:', self.init)
        lenct = len(chunk2)
        lenkey = len(self.init)

        final_key = ""
        
        if(isinstance(lenct/lenkey, float)==True):
            div_num = int(lenct/lenkey)
            increment_num = div_num+1

        else:
            increment_num = int(lenct/lenkey)

        for i in range (0,increment_num):
            final_key+=self.init
        self.shift(self.chunk2)

    def shift(self,chunk2):
        self.g=(self.chunk2[7:]+chunk2[:7])
        print('Shifted Chunk2:',self.g)
        self.concatinate(self.f,self.g)
        
    def concatinate(self,f,g):
        self.h = self.f + self.g
        print('Concatinated:',self.h)
        self.xor(self.h)

    def xor(self, h):
        print(len(self.init))
        print(len(self.h))
        lenct = len(self.h)
        lenkey = len(self.init)

        final_key = ""
        
        if(isinstance(lenct/lenkey, float)==True):
            div_num = int(lenct/lenkey)
            increment_num = div_num+1

        else:
            increment_num = int(lenct/lenkey)

        for i in range (0,increment_num):
            final_key+=self.init

        self.init = final_key[:lenct]

        print('New Key:' +self.init+' Lenght: '+str(len(self.init)))
        self.x = '{1:0{0}b}'.format(len(self.h), int(self.h, 2) ^ int(self.init, 2))
        self.cipherfinResult = ''.join(chr(int(self.x[i:i+7], 2)) for i in range(0, len(self.x), 8))
        print(f"cipherbits: {self.x}")
        print("cipher text: ", self.cipherfinResult)
        print(f"length: {len(self.x)}")

    def getfinbin(self):
        return self.x

    def getIV(self):
        return self.IV 
        
    def display(self):
        return self.cipherfinResult
        


if __name__ == "__main__":
    window = Encryption()


