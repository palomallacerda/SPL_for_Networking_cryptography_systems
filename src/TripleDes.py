
#Password hashing Iterations - KEEP CONSTANT through out this application existence.
from Crypto.Protocol.KDF import PBKDF2
from getpass import getpass
from Crypto.Hash import SHA256
from Crypto.Cipher import DES
pi = 100005
#password SALT, This variable should remain constant throught out this application life. This will make RAINBOW HASH TABLES USELESS
#For deactivating salting, just leave salt="" i.e. blank in paranthesis.
#DO NOT CHANGE BELOW VALUE AT ANY COST-------------------------------------------------------------------------------------------
salt_const = b"$ez*}-d3](%d%$#*!)$#%s45le$*sohailmirzaft75456dgfdrrrrfgfs^"
#DO NOT CHANGE ABOVE VALUE AT ANY COST-------------------------------------------------------------------------------------------


def encrypt(message, key_enc):

	#hashing original image in SHA256
	hash_of_original = SHA256.new(data=message)

	#Salting and hashing password
	key_enc = PBKDF2(key_enc, salt_const, 48, count=pi)
	try:

		cipher1 = DES.new(key_enc[0:8], DES.MODE_CBC, key_enc[24:32])
		ciphertext1 = cipher1.encrypt(message)
		cipher2 = DES.new(key_enc[8:16], DES.MODE_CBC, key_enc[32:40])
		ciphertext2 = cipher2.decrypt(ciphertext1)
		cipher3 = DES.new(key_enc[16:24], DES.MODE_CBC, key_enc[40:48])
		ciphertext3 = cipher3.encrypt(ciphertext2)

		ciphertext3 += hash_of_original.digest()
	except Exception as e:
		print("ERROR: ", e)
		return False
	
	return ciphertext3

#decrypting function
def decrypt(message, key_enc):

	#extracting hash and cipher data without hash
	extracted_hash = message[-32:]
	encrypted_data = message[:-32]

	#salting and hashing password
	key_dec = PBKDF2(key_dec, salt_const, 48, count=pi)

	try:
		cipher1 = DES.new(key_dec[16:24], DES.MODE_CBC, key_dec[40:48])
		plaintext1 = cipher1.decrypt(encrypted_data)
		cipher2 = DES.new(key_dec[8:16], DES.MODE_CBC, key_dec[32:40])
		plaintext2 = cipher2.encrypt(plaintext1)
		cipher3 = DES.new(key_dec[0:8], DES.MODE_CBC, key_dec[24:32])
		plaintext3 = cipher3.decrypt(plaintext2)
	except Exception as e:
		print("ERROR: ", e)
		return False
	
	#hashing decrypted plain text
	hash_of_decrypted = SHA256.new(data=plaintext3)

	#matching hashes
	if hash_of_decrypted.digest() == extracted_hash:
		return plaintext3
	else:
		return False