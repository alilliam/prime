import sys,os

kilobytes = 1024
megabytes = kilobytes * 1024
gigabytes = megabytes * 1024
chunksize = 4 * gigabytes

def split(filename,chunksize):
    fromfp  = open(filename,"rb")
    partnum = 0
    while(True):
        chunk = fromfp.read(chunksize)
        if not chunk:
            break
        partnum += 1
        #objname = str(partnum) + ".txt"
        tofp = open("part1.txt","ab+")
        tofp.write(chunk)
        tofp.close()
    fromfp.close()

try:
    split("miler4.txt",chunksize)
except:
    print("Error during split")
else:
    print("split finished!")
    