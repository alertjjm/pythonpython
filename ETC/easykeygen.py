
keylist=[0x5B,0x13,0x49,0x77,0x13,0x5E,0x7D,0x13]
xrolist=[0x10,0x20,0x30]
keystr=''
cur=0
for i in keylist:
    keystr=keystr+chr(xrolist[cur]^i)
    cur=(cur+1)%3
print(keystr)