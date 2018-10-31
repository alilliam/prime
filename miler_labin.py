# coding=gbk
from random import randint
from math import sqrt
import threading
#from time import ctime,sleep
import time
import random
import signal
import os

def select_a_list(n): 
	if n < 2047: 
		return [2,] 
	elif n < 1373653: 
		return [2, 3] 
	elif n < 9080191: 
		return [31, 73] 
	elif n < 25326001: 
		return [2, 3, 5] 
	elif n < 3215031751: 
		return [2, 3, 7] 
	elif n < 4759123141: 
		return [2, 7, 61] 
	elif n < 1122004669633: 
		return [2, 13, 23, 1662803] 
	elif n < 2152302898747: 
		return [2, 3, 5, 7, 11] 
	elif n < 3474749660383: 
		return [2, 3, 5, 7, 11, 13] 
	elif n < 341550071728321: 
		return [2, 3, 5, 7, 11, 13, 17] 
	elif n < 3825123056546413051: 
		return [2, 3, 5, 7, 11, 13, 17, 19, 23] 
	elif n < 318665857834031151167461: 
		return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
	elif n < 3317044064679887385961981: 
		return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] 
	else: 
		return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 


def CtrlC():
	os._exit(0)

def isRangeOk(minData,maxData):
    if not (isinstance(minData, int) and isinstance(maxData, int)):
        print('You must give me integer')
        return False
    elif minData<2:
        print("minData must bigger than 2")
        return False
    else:
        return minData < maxData


def fastExpMod(b,e,m):
	result = 1
	while e != 0:
		if(e&1 != 1):
			result = (result *b) % m
		e >>= 1
		result = result**2 % m
	return result
		

def calc_r_u(n):
	n -= 1
	r = 0

	while (n&1) == 0:
		r += 1
		n >>= 1
		
	return r,n


def Miller_Rabin_Is_Prime(n):
	#lista = [2,3,5,7,31,61,73]
	lista = select_a_list(n)
	if n <2:
		return False
	if n==2 or n==3:
		return True
	if (n&1) == 0:
		return False
	r,u = calc_r_u(n)
	for i in range(len(lista)):
		a = random.sample(lista,1)[0]
		lista.remove(a)
		z = pow(a,u,n)
		if z==1 or z==(n-1):
			continue
		
		for j in range(1,r):#u
			z=z**2 % n
			if z==1:
				return False
			if z==n-1:
				break
		if z != n-1:
			return False
	return True

def findPrimeInRange(minData,maxData):
	prime_list=[]
	print("arg1 %d ,arg2 %d" %(minData,maxData))
	if isRangeOk(minData,maxData):
		
		f=open('miler4.txt','a+')#二进制应该用ab+
		count = 0
		for p in range(minData,maxData):
			res = Miller_Rabin_Is_Prime(p)
			if res:
				count += 1
				prime_list.append(p)
				#print(p)
				if count % 5000 == 0:
					print(p)
					f.write(str(prime_list)+'\n')
					prime_list=[]
		f.write(str(prime_list)+'\n')
		
		f.close()
		
	else:
	    print("wrong range!")





startt = time.time()
res = Miller_Rabin_Is_Prime(2770937238187)
print(res)
'''
threads = []
arg_list=[]


print("#---------------------------------#")
print("please input 2 number for range")
print("#---------------------------------#")

start_num = input("please input the start number:")
end_num = input("please input the end number:")
start_num = int(start_num)
end_num = int(end_num)

findPrimeInRange(start_num,end_num)
'''


'''
arg_list.append(start_num)
step_number =int( (end_num - start_num)/4)
p = start_num
for i in range(3):
    p += step_number
    arg_list.append(p)
arg_list.append(end_num)


number = range(len(arg_list)-1)
if len(arg_list) >= 2:
	for i in number:
	    t = threading.Thread(target=findPrimeInRange,args=(arg_list[i],arg_list[i+1]-1))
	    threads.append(t)

signal.signal(signal.SIGINT,CtrlC)
signal.signal(signal.SIGTERM,CtrlC)
for i in number:
    threads[i].start()
    print("thread %d is running " %i)

for i in number:
    threads[i].join()

'''
endt = time.time()
print("time:%s" %(endt-startt))









