from time import sleep
import RSA
import AES
import json

sleep(5)
with open('scr/toBob.json', 'r') as fp:
    alicePublic = json.load(fp)['publicKey']

print(" Hi Alice, i am sending you a symetric AES key that i encrypted using the public key you sent me")

symKey = AES.createKey()

symKeyEncrypted = RSA.encrypt(alicePublic, symKey)

with open('scr/toAlice.json', 'w') as fp:
    json.dump({'symKey': symKeyEncrypted}, fp)


sleep(10)
with open('scr/toBob.json', 'r') as fp:
    encMessFromAlice = json.load(fp)['message']


print(" I got your message and decrypted it using the symetric key")
print(" your message read '{}'".format(AES.decryptMessage(symKey, encMessFromAlice)))
print(" i am sending you an answer")

encMess = AES.encryptMessage(symKey, "fordi det er Magda baklengs...... Hvis du vrir og snur og vender på bokstavene!")

with open('scr/toAlice.json', 'w') as fp:
    json.dump({'message': encMess}, fp)

sleep(10)