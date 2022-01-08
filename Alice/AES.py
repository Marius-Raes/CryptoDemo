import random
import operator

def encryptMessage(key, message):
    if len(message) % 16 != 0:
        message = message + chr(0)
    
    while len(message) % 16 != 0:
        message = message + chr(random.randint(1, 256))

    chunks = []

    for i in range(0, int(len(message)/16)):
        chunks.append("")
        for j in range(i * 16, (i+1) * 16):
            chunks[i] = chunks[i] + message[j]
    
    grids = []

    for chunk in chunks:
        grids.append(createGrid(chunk))

    encryptedMessage = ""

    for grid in grids:
        for i in range(0,4):
            for j in range(0,4):
                encryptedMessage = encryptedMessage + chr(grid[i][j])
    
    return message


        

def createGrid(chunk):
    grid = [[0 for x in range(4)] for y in range(4)] 
    
    k = 0;
    for i in range(0, 4):
        for j in range(0, 4):
            grid[i][j] = ord(chunk[k])
            k+=1
    return grid
    


print(encryptMessage(123, "hallo der hvordan går det med deg?"))
