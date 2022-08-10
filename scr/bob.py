import RSA
import AES
import json

sleep(10)
with open('scr/toBob.json', 'r') as fp:
    alicePublic = json.load(fp)

print(alicePublic)

symKey = AES.createKey()

symKeyEncrypted = RSA.encrypt(alicePublic, symKey)

with open('scr/toAlice.json', 'w') as fp:
    json.dump(symKeyEncrypted, fp)



encMess = AES.encryptMessage(symKey, "fordi det er Magda baklengs...... Hvis du vrir og snur og vender på bokstavene!")


print(AES.decryptMessage(symKey, encMess))