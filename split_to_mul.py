import struct
import time


def read_in_chucks(fileh,chunk_size=8):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = fileh.read(chunk_size)
        if not data:
            break
        #print(data)
        data_int = struct.unpack("Q", data)[0]#解成无符号整型
        yield data_int


def split_fp(fileh,bigNum):
    """split big num"""
    f = open(fileh,"rb")#rb 读取二进制文件
    valid_prime_list = []
    num = 0
    for data_int in read_in_chucks(f):
        num += 1
        if(num % 5000 == 0):
            print(str(data_int) +" " +str(bigNum))
        
        while(bigNum % data_int == 0):
            valid_prime_list.append(data_int)
            bigNum //= data_int #整型 近似?
        
    if(bigNum == 1):
        print(valid_prime_list)
    else:
        valid_prime_list.append(data_int)
        print(valid_prime_list)
        print("not completely split")


def convert_str_to_int(fileh):
    """change str file to 01 file"""
    f = open(fileh,"r")
    obj_f = open(fileh+"_new","ab+")
    for line in f:
        line=line.replace(","," ")
        line=line.replace("["," ")
        line=line.replace("]"," ")

        c_array = line.split()
        print(c_array[0])
        for c in c_array:
            #c_int = int("9223372036854775807")
            c_int = int(c)   
            c_int = struct.pack("Q", c_int)#大端 b'\xff\xff\xff\xff\xff\xff\xff\x7f'
            obj_f.write(c_int)
    f.close()

def count_f_to_big_num(testfile):
    """change file to a big num.
        file must be a multiply of 8"""
    ff = open(testfile,"rb")
    data_stack = []
    base = 2**64
    bignum = 0
    i = 0
    for data_int in read_in_chucks(ff):
        data_stack.append(data_int)
    data_stack.reverse()
    for data_int in data_stack:
        bignum += base*data_int*i
        i += 1
    print(bignum)
    return bignum
    

startt = time.time()
bignum = 2019560988821480321949784364899098444169216
#bignum = count_f_to_big_num("test.txt")
split_fp("prime",bignum)
endt = time.time()
print("time:%s" %(endt-startt))

'''
valid_prime_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 47, 60046081,2770937238187]
res =1
bignum = 2019560988821480321949784364899098444169216
for i in valid_prime_list:
    res *= i
print(res)
'''