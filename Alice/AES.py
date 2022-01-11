import random
from stepsAES import *
from keyScheduler import *

def encryptMessage(key, message):
    # if message does not naturally fill the last grid a null character is added to indicate the end of the message
    # and random characters are added untill it does.
    if len(message) % 16 != 0:
        message = message + chr(0)
    while len(message) % 16 != 0:
        message = message + chr(random.randint(1, 256))

    # the message is split into 16 byte chunks
    chunks = []
    for i in range(0, int(len(message)/16)):
        chunks.append("")
        for j in range(i * 16, (i+1) * 16):
            chunks[i] = chunks[i] + message[j]
    
    # each chunk is turned into a 4x4 grid that can be encrypted using AES algorithim
    grids = []
    for chunk in chunks:
        grids.append(createGrid(chunk))

    # key is expanded into 11 roundkeys one for each full round and 2 for the start and end 
    roundkeys = keyExpander(key, 11)

    # each grid is encrypted using AES
    for grid in grids:
        addRoundKey(grid, roundkeys[0])
        for i in range(1, 10):
            oneRound(grid, roundkeys[i])
        
        lastRound(grid, roundkeys[10])
    
    
    # The encrypted grids are converted and combined tinto the ecncrypted message 
    encryptedMessage = ""
    for grid in grids:
        for i in range(0,4):
            for j in range(0,4):
                encryptedMessage = encryptedMessage + chr(grid[i][j])
    
    return encryptedMessage


        

def createGrid(chunk):
    grid = [[0 for x in range(4)] for y in range(4)] 
    
    k = 0;
    for i in range(0, 4):
        for j in range(0, 4):
            grid[i][j] = ord(chunk[k])
            k+=1
    return grid
    

def oneRound(grid, roundkey):
    subBytes(grid)
    shiftRows(grid)
    mixColumns(grid)
    addRoundKey(grid, roundkey)

def lastRound(grid, roundkey):
    subBytes(grid)
    shiftRows(grid)
    addRoundKey(grid, roundkey)



print(encryptMessage(123, "hallo der hvordan går det med deg?"))
