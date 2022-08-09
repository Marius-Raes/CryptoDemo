from keyCreatorRSA import *
import json
def sendToBob(msg, operation):
    
    print("sending message '{}' to alice".format(msg))
    if(operation == "overwrite"):
        f = open("internet.json", "w")
    elif(operation == "append"):
        f = open("internet.json", "a")

    packet = {"sender": "Alice", "reciver": "Bob", "msg": msg }
    
    f.write('\n')
    f.write(json.dumps(packet))
    f.close()
    
    return

RSAkeys = createKeys();

sendToBob(RSAkeys['public'], "overwrite")





AliceSecretMessage = "I'm responsible for my own happiness? I can't even be responsible for my own breakfast!" 


