from time import sleep
import RSA
import AES
import json

sleep(10)
with open('scr/toBob.json', 'r') as fp:
    alicePublic = json.load(fp)

print("Bob: Hi Alice, i am sending you a symetric AES key that i encrypted using the public key you sent me")

symKey = AES.createKey()

symKeyEncrypted = RSA.encrypt(alicePublic, symKey)

with open('scr/toAlice.json', 'w') as fp:
    json.dump(symKeyEncrypted, fp)


sleep(10)
with open('scr/toBob.json', 'r') as fp:
    encMessFromAlice = json.load(fp)['message']


print("Bob: I got your message and decrypted it using the symetric key")
print("Bob: your message read '{}'".format(AES.decryptMessage(symKey, encMessFromAlice)))
print("Bob: i am sending you an answer")

encMess = AES.encryptMessage(symKey, "fordi det er Magda baklengs...... Hvis du vrir og snur og vender på bokstavene!")



