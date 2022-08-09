import json
import random

def readFromAlice():
    f = open("internet.json", "r")
    packet = f.readlines()[-1]
    f.close()
    return json.loads(packet)['msg']

def sendToAlice(msg, operation):
    print("sending message '{}' to alice".format(msg))
    if(operation == "overwrite"):
        f = open("internet.json", "w")
    elif(operation == "append"):
        f = open("internet.json", "a")

    packet = {"sender": "Bob", "reciver": "Alice", "msg": msg }

    f.write('\n')
    f.write(json.dumps(packet)) 
    f.close()
    return

def createSymetricKeys(e, n): 
    plaintextKey = random.getrandbits(128)
    encryptedKey = plaintextKey**e % n

    return {"plaintextKey": plaintextKey, "encryptedKey": encryptedKey}


BobSecretMessage = "It gets easier. Every day, it gets a little easier. But you gotta do it every day - that's the hard part. But it does get easier"

publicKey = readFromAlice()

symKeys = createSymetricKeys(publicKey['e'], publicKey['n'])

sendToAlice(symKeys['encryptedKey'], "append")



