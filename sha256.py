k =(0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, \
	0xab1c5ed5,	0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, \
	0x9bdc06a7, 0xc19bf174,	0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, \
	0x4a7484aa, 0x5cb0a9dc, 0x76f988da,	0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, \
	0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,	0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, \
	0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,	0xa2bfe8a1, 0xa81a664b, \
	0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,	0x19a4c116, \
	0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,	\
	0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, \
	0xc67178f2)

def rotR(num, amountToRotate):
	array = format(num, '032b')
	return int(array[-amountToRotate:] + array[:-amountToRotate], 2)


def limitTo8bitHex(num):
	return int(format(num, '08x')[-8:], 16)
	
def sha256(text):

	h0 = 0x6a09e667
	h1 = 0xbb67ae85
	h2 = 0x3c6ef372
	h3 = 0xa54ff53a
	h4 = 0x510e527f
	h5 = 0x9b05688c
	h6 = 0x1f83d9ab
	h7 = 0x5be0cd19


	
	

	message = text.encode("utf-8").hex()
	message = bin(int(message, 16))[2:] 
	
	
	while len(message) < len(text)*8:
		message = '0' + message
	#message = ''

	#Get the length of the message in binary
	L = bin(len(str(message)))[2:] #[2:] is used to avoid the 0b

	message += "1" #appends a 1 to the binary value

	#Adds zeros until the message length is a multiple of 512 bits
	while (len(message) + len(L)) % 512 is not 0: #checks if message is 512 bits long
		message += "0"
		
	message = message + L
	

	#Process the message in successive 512-bit chunks:
	"""break message into 512-bit chunks"""
	chunks = []
	while len(message) > 0:
		chunks.insert(0, message[-512:])
		message = message[0:-512]
		

	w = []
	for chunk in chunks:
		i = 0
		while i < 16:
			w.append(chunk[32*i:32*(i+1)])
			i += 1
		while i < 64:
			w.append('00000000000000000000000000000000') #32 zeros
			i += 1

		#Extend the first 16 words into the remaining 48 words w[16..63] of the message
		#	schedule array:
		i = 16
		while i < 64:
			s0 = rotR(int(w[i-15], 2), 7) ^ rotR(int(w[i-15], 2), 18) ^ (int(w[i-15], 2) >> 3)
			s1 = rotR(int(w[i-2], 2), 17) ^ rotR(int(w[i-2], 2), 19) ^ (int(w[i-2], 2) >> 10)
			w[i] = format(limitTo8bitHex(int(w[i-16], 2) + s0 + int(w[i-7], 2) + s1), '032b')
			i += 1
			
		#w[0] = '00000010000000000000000000000000' #Used to check the main loop works

		#Initialize working variables to current hash value:
		a = h0
		b = h1
		c = h2
		d = h3
		e = h4
		f = h5
		g = h6
		h = h7

		#Compression function main loop:
		i = 0
		while i < 64:
			S1 = rotR(e, 6) ^ rotR(e, 11) ^ rotR(e, 25)
			ch = (e & f) ^ ((~e) & g)
			temp1 = limitTo8bitHex(h + S1 + ch + k[i] + int(w[i], 2))
			S0 = rotR(a, 2) ^ rotR(a, 13) ^ rotR(a, 22)
			maj = (a & b) ^ (a & c) ^ (b & c)
			temp2 = limitTo8bitHex(S0 + maj)

			h = g
			g = f
			f = e
			e = limitTo8bitHex(d + temp1)
			d = c
			c = b
			b = a
			a = limitTo8bitHex(temp1 + temp2)

			i += 1
			
		#Add the compressed chunk to the current hash value:
		h0 = limitTo8bitHex(h0 + a)
		h1 = limitTo8bitHex(h1 + b)
		h2 = limitTo8bitHex(h2 + c)
		h3 = limitTo8bitHex(h3 + d)
		h4 = limitTo8bitHex(h4 + e)
		h5 = limitTo8bitHex(h5 + f)
		h6 = limitTo8bitHex(h6 + g)
		h7 = limitTo8bitHex(h7 + h)

		#Produce the final hash value (big-endian):
		finalHash = format(h0, '#010x') + format(h1, '08x')
		finalHash += format(h2, '08x') + format(h3, '08x')
		finalHash += format(h4, '08x') + format(h5, '08x')
		finalHash += format(h6, '08x') + format(h7, '08x')
		return finalHash
