from time import sleep
import RSA
import AES
import json

keys = RSA.createKeys()


print(" Hi bob i am sending you my public RSA key")
with open('scr/toBob.json', 'w') as fp:
    json.dump({'publicKey': keys['public']}, fp)


sleep(10)

with open('scr/toAlice.json', 'r') as fp:
    symKeyEncrypted = json.load(fp)['symKey']

symKey = RSA.decrypt(keys["private"], symKeyEncrypted)
print(" I decrypted the symetric key using my private key.")
print(" We both now have the symetric key, i will use it to send an encrypted message to you :)")

encMess = AES.encryptMessage(symKey, "Men hvorfor heter hun da hønse Lovisa?")

with open('scr/toBob.json', 'w') as fp:
    json.dump({'message': encMess}, fp)


sleep(10)
with open('scr/toAlice.json', 'r') as fp:
    encMessFromBob = json.load(fp)['message']

print(" I got your message and decrypted it using the symetric key")
print(" your message read '{}'".format(AES.decryptMessage(symKey, encMessFromBob)))

sleep(5)