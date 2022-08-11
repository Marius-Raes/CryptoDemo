from time import sleep
import RSA
import AES
import json

keys = RSA.createKeys()


print("Alice: Hi bob i am sending you my public RSA key")
with open('scr/toBob.json', 'w') as fp:
    json.dump(keys['public'], fp)


sleep(15)

with open('scr/toAlice.json', 'r') as fp:
    symKeyEncrypted = json.load(fp)

symKey = RSA.decrypt(keys["private"], symKeyEncrypted)
print("Alice: I decrypted the symetric key using my private key.")
print("Alice: We both now have the symetric key, i will use it to send an encrypted message to you :)")

encMess = AES.encryptMessage(symKey, "Men hvorfor heter hun da hønse Lovisa?")

with open('scr/toBob.json', 'w') as fp:
    json.dump({'message': encMess}, fp)


