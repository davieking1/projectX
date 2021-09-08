import math
import codecs
class Decryption():
    #ct = '101000011110000011000000000001001100101001101101110010000001111000101000001000010011010100010111101001001100000110011011011011011101110100010110010010011010001111101001001011011010000000101101100001011001010100110011001111001011100011010001010010011100110100010010010001010011000000110001111110110011100100010000000001010011001110110110101111010001000101110001101100000001011110111000001110000001000010111011101110100111110111101100111010110011010101011000'
    init = None
    #key = 'password'
    #s = ''
    IV = None

    def __init__(self, finbin_text, passwd, initial_vector):
        self.key = passwd
        self.IV = initial_vector
        self.xor(finbin_text, self.key)
        
    def xor(self, finbin_text, key):
        self.init = bin(int.from_bytes(key.encode(), 'big')) [2:]
        print('Key in Binary:', self.init)
      
        lenct = len(finbin_text)
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

        self.ux = '{1:0{0}b}'.format(len(finbin_text), int(finbin_text, 2) ^ int(self.init, 2))
        print('Text in binary:', self.ux)
        self.split(self.ux)

    def split(self, ux):
        a = len(self.ux)
        self.b = int(a/2)
        print(self.b)
    
        self.chunk1 = self.ux[:self.b]
        self.chunk2 = self.ux[self.b:]

        print(self.ux)
        print('Chunk 1:',self.chunk1)
        print('chunk 2:',self.chunk2)

        self.keychunk1Xor(self.chunk1, self.b)
        self.keychunk2Xor(self.chunk2)

    def keychunk1Xor(self, chunk1, b):
        self.init = bin(int.from_bytes(self.key.encode(), 'big'))[2:]
        print('Key in Binary:', self.init)
        lenct = len(chunk1)
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

    def reverse(self, chunk1, b):
        self.f=chunk1[b-1::-1]
        print('Reversed Chunk:',self.f)
        

    def keychunk2Xor(self, chunk2):
        self.init = bin(int.from_bytes(self.key.encode(), 'big'))[2:]
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
        self.g=(self.chunk2[-7:]+chunk2[:-7])
        print('Shifted Chunk2:',self.g)
        self.concatinate(self.f,self.g)

    def concatinate(self,f,g):
        self.h = self.f + self.g
        print('Concatinated:{} Length:{}'.format(self.h, len(self.h)))

        self.plaintext = self.h[1:]
        print("plaintext: {} length: {} ".format(self.plaintext, len(self.plaintext)))
        self.plaintext_Xor_IV(self.plaintext, self.IV)

    def plaintext_Xor_IV(self, plaintext, IV):
        self.IVbin = bin(int.from_bytes(IV.encode(), 'big'))[2:]
        IVbin_length = len(self.IVbin)
        cipher_length = len(self.plaintext)
        x = math.ceil(cipher_length/IVbin_length)     
        self.IVbin *= x
        self.IVbin = self.IVbin[:len(self.plaintext)] 
        print("padded cipher_IV_xor: ", self.IVbin)
        print(f"the length of ciphertext: {len(self.plaintext)}")
        print(f"the length of the key: {len(self.IVbin)}")
        self.cIV_xor = '{1:0{0}b}'.format(len(self.plaintext), int(self.plaintext, 2) ^ int(self.IVbin, 2))
        print(f"XORed cipher and IV: {self.cIV_xor}")
        print(f"length: {len(self.cIV_xor)}")
        self.bintostring(self.cIV_xor)
        
    def bintostring(self, cIV_xor):
        self.final = ""
        for i in range(0, len(self.cIV_xor), 8):
            bytes = self.cIV_xor[i:i+7]
            decstring = int(bytes, 2)
            self.final += chr(decstring)

        print(self.final)
        self.rot13(self.final)

    # def rot13(self, final):
    #     pt13 = codecs.decode(final, 'rot_13')
    #     print(f"rot13 plaintext: {pt13}")
    #     self.pt13 = pt13

    def rot13(self, final):

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
        for i in final :
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
        pt13 = ''.join(rotated_plain_text)
        print(f'rotated-plain_text1xx: {pt13}')
        self.pt13 = pt13

    def get_text(self):
        return self.pt13



if __name__ == "__main__":
    window = Decryption()