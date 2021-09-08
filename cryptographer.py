import sys
import os


class Crypto(object):

    # s = None
    # f = None
    # g = None
    # init = None
    # keyfile = 'password'

    # def __init__(self):
    #     super(Encfile, self).__init__()
    #     open_file()

    def encryption(filename, keyfile):
        # with open(sys.argv[1], "rb") as infile:
        with open(filename, "rb") as infile:
            file = infile.read()
        print("File opened: %s " % (filename))
        print("Keyfile: ", keyfile)
        # string_to_bin(filename, keyfile)

        # def string_to_bin(self, s, keyfile):
        ptextbin = file
        print("File bytes: ", ptextbin[:50])
        file_bits = bin(int.from_bytes(ptextbin, 'big'))[2:]
        print("File bits: {} Length of bits: {}".format(file_bits[:50], len(file_bits)))
        # init = bin(int.from_bytes(keyfile.encode(), 'big'))[2:]
        init = bin(int.from_bytes(keyfile, 'big'))[2:]
        len_file = len(file_bits)
        if len(init) > len_file:
            init = init[:len_file]

        print("keyfile in binary: ", init)
        # split(file_bits)

        # # def bits_to_bytes(self, res):
        # # // is truncating division - try 9//4 = 2
        # # to_bytes() - array of bytes representing an integer
        # # bit_length() - number of bits
        # # 'big' - byteorder is "big" i.e. the most significant byte is at the beginning of the byte array
        # byte_res = int(res, 2).to_bytes((len(res) + 7) // 8, byteorder='big')
        # print("File cipher bytes: ", byte_res[:50])
        # return byte_res

        # def split(self,file_bits):
        a = len(file_bits)
        fer = len(keyfile)
        print("init length: ",len(init))
        print("Key Length: ",fer)
        print("Length of bit stream: ", a)
        b = int(a/2)
        c = a-b
        print("Length of first chunk: ", b)
        print("Length of second chunk: ", c)
        d=(file_bits[:b])
        e=(file_bits[b:])
        print("First Chunk: ", d[:50])
        print("Second Chunk: ", e[:50])
        # reverse(b, d)
        # shift(e)

        # def reverse(self, b, d):
        f = d[b-1::-1]
        print("Reversed first chunk: " + f[:50])
        # return f

        # def shift(self, e):
        g = (e[5:]+e[:5])
        print("Second chunk after shift by 5 : " + g[:50])
        # concatenate(f, g)

        # def concatenate(self,f,g):
        h = f + g
        print("concatenated: ", h[:50] + " ... ")
        # xor(h, init)

        # def xor(self, h, init):
        x = '{1:0{0}b}'.format(len(h), int(h, 2) ^ int(init, 2))
        print('File Cipher in Binary: ', x[:50])
        # write_to_file(x)
        qwe = len(x)
        print("Length of cipher stream: ", qwe)

        # def write_to_file(self, x):
        outPut_file = filename+".enc"
        with open(outPut_file, "w") as out_file:
        # write bytes to file
            out_file.write(x)
            out_file.close()
            os.remove(filename)
            print("+++ File encryption completed. +++")


    def decryption(filename, keyfile):
        # def open_file(self):
        with open(filename, "r") as infile:
            file = infile.read()
        print("File opened: %s " % (filename))
        # string_to_bin(s, key)

        # def string_to_bin(self, s, key):
        ctextbin = file
        init = bin(int.from_bytes(keyfile, 'big'))[2:]
        print("File content in bits: ", ctextbin[:50])
        len_file = len(ctextbin)
        if len(init) > len_file:
            init = init[:len_file]
        print("Key in binary: ", init)
        # xor(ctextbin, init)

        # def bits_to_bytes(self, res):
        # // is truncating division - try 9//4 = 2
        # to_bytes() - array of bytes representing an integer
        # bit_length() - number of bits
        # 'big' - byteorder is "big" i.e. the most significant byte is at the beginning of the byte array
        # byte_res = int(res, 2).to_bytes((len(res) + 7) // 8, byteorder='big')
        # print("File bytes: ", byte_res[:50])
        # return byte_res

        # def xor(self, ctextbin, init):
        x = '{1:0{0}b}'.format(len(ctextbin), int(ctextbin, 2) ^ int(init, 2))
        print('XORred: ', x[:50])
        # split(x)

        # def split(self, x):
        a = len(x)
        print("Chunk length: ", a)
        b = int(a / 2)
        c = a - b
        d = (x[:b])
        e = (x[b:])
        print("First Chunk: {} Chunk length: {}".format(d[:50] + " ...", len(d)))
        print("Second Chunk: {} Chunk length: {}".format(e[:50] + " ...", len(e)))
        # reverse(b, d)
        # shift(e)

        # def reverse(self, b, d):
        f = d[b-1::-1]
        print("Reversed first chunk ", f[:50])

        # def shift(self, e):
        print("Second chunk before shift: ", e[:50])
        g = (e[-5:] + e[:-5])
        print("Second chunk after reverse shift by 5 : ", g[:50])
        # concatenate(f, g)

        # def concatenate(self, f, g):
        h = (f) + (g)
        # write_bits_to_file(h)
        # data = bits_to_bytes(h)
        data = int(h, 2).to_bytes((len(h) + 7) // 8, byteorder='big')
        print("File bytes: ", data[:50])
        # write_to_file(data)

        # def write_to_file(self, data):
        outfile = os.path.splitext(filename)[0]
        with open(outfile, "wb") as out_file:
            # Write bytes to the file"file.txt"
            out_file.write(data)
            out_file.close()
            os.remove(filename)
            print(" ++ Decryption Completed. ++ ")


