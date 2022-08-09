import RSA
import AES
print("hallo")


keys = RSA.createKeys()

print(keys)

encrypted = RSA.encrypt(keys["public"], 133700000)

print(encrypted)

print(RSA.decrypt(keys["private"], encrypted))

symKey = AES.createKey()


encMess = AES.encryptMessage(symKey, "fordi det er Magda baklengs...... Hvis du vrir og snur og vender på bokstavene!")

print(encMess)

print(AES.decryptMessage(symKey, encMess))