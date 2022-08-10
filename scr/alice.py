from time import sleep
import RSA
import AES
import json

keys = RSA.createKeys()

print(keys)


with open('scr/toBob.json', 'w') as fp:
    json.dump(keys['public'], fp)


sleep(15)

with open('scr/toAlice.json', 'r') as fp:
    symKeyEncrypted = json.load(fp)

symKey = RSA.decrypt(keys["private"], symKeyEncrypted)

encMess = AES.encryptMessage(symKey, "Men hvorfor heter hun da hønse Lovisa?")


print(AES.decryptMessage(symKeyEncrypted, encMess))