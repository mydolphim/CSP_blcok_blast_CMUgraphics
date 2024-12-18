from cmu_graphics import *

import random

app.background = 'steelBlue'
app.score = 0

scoreBoard = Label(f"Score: {app.score}", 200, 30, size = 40, bold = True, font = "montserrat", fill = "White")

gridSize = 30
rows,cols = 8,8

board = Group()
occupiedGrid = [[False for _ in range(cols)] for _ in range(rows)]
placedBlocks = [[None for _ in range(cols)] for _ in range(rows)]
            
for row in range(rows):
    for col in range(cols):
        grid = Rect(col * gridSize, row * gridSize, gridSize, gridSize, fill = 'black', border = 'gray', borderWidth = 1)
        board.add(grid)
        
board.centerX = 200
board.centerY = 180

blockStorage = Group(
        Rect(50, 300, 100, 100, fill= None),
        Rect(150, 300, 100, 100, fill= None),
        Rect(250, 300, 100, 100, fill= None)
    )

def createBlock0(): # .
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'white', border = 'gray', borderWidth = 1),
    )

def createBlock1(): # ㅡ
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'yellow', border = 'gray', borderWidth = 1),
        Rect(gridSize, 0, gridSize, gridSize, fill = 'yellow', border = 'gray', borderWidth = 1)
    )
    
def createBlock2(): # ㅣ
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'blue', border = 'gray', borderWidth = 1),
        Rect(0, gridSize, gridSize, gridSize, fill = 'blue', border = 'gray', borderWidth = 1),
        )
        
def createBlock3(): # ㅣ
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'red', border = 'gray', borderWidth = 1),
        Rect(0, gridSize, gridSize, gridSize, fill = 'red', border = 'gray', borderWidth = 1),
        Rect(0,gridSize*2, gridSize,gridSize, fill = 'red', border = 'gray', borderWidth = 1)
        )
        
def createBlock4(): # ㅡ
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'aqua', border = 'gray', borderWidth = 1),
        Rect(gridSize, 0, gridSize, gridSize, fill = 'aqua', border = 'gray', borderWidth = 1),
        Rect(gridSize*2,0, gridSize,gridSize, fill = 'aqua' , border = 'gray', borderWidth = 1)
    )
    
def createBlock5(): # r
    return Group(
            Rect(0,0, gridSize, gridSize, fill = 'yellow', border = 'gray', borderWidth = 1),
            Rect(gridSize, 0, gridSize, gridSize, fill = 'yellow', border = 'gray', borderWidth = 1),
            Rect(0,gridSize,gridSize, gridSize, fill = 'yellow', border = 'gray', borderWidth = 1)
        )
        
        
def createBlock6(): # ㅁ
    return Group(
            Rect(0,0, gridSize, gridSize, fill = 'forestGreen', border = 'gray', borderWidth = 1),
            Rect(gridSize, 0, gridSize, gridSize, fill = 'forestGreen', border = 'gray', borderWidth = 1),
            Rect(0,gridSize,gridSize, gridSize, fill = 'forestGreen', border = 'gray', borderWidth = 1),
            Rect(gridSize, 30, gridSize, gridSize, fill = 'forestGreen', border = 'gray', borderWidth = 1)
        )
        
def createBlock7(): # ㅏ
    return Group(
        Rect(0,0, gridSize, gridSize, fill = 'lightGreen', border = 'gray', borderWidth = 1),
        Rect(0, gridSize, gridSize, gridSize, fill = 'lightGreen', border = 'gray', borderWidth = 1),
        Rect(0,gridSize*2, gridSize,gridSize, fill = 'lightGreen', border = 'gray', borderWidth = 1),
        Rect(gridSize,30, gridSize,gridSize, fill = 'lightGreen', border = 'gray', borderWidth = 1)
        )
        
def createBlock8(): # ㅓ
    return Group(
        Rect(0,gridSize, gridSize, gridSize, fill = 'red', border = 'gray', borderWidth = 1),
        Rect(gridSize, 0, gridSize, gridSize, fill = 'red', border = 'gray', borderWidth = 1),
        Rect(gridSize,gridSize, gridSize,gridSize, fill = 'red', border = 'gray', borderWidth = 1),
        Rect(gridSize,gridSize * 2, gridSize,gridSize, fill = 'red', border = 'gray', borderWidth = 1)
        )
        
def createBlock9(): # ㅗ
    return Group(
        Rect(gridSize,0, gridSize, gridSize, fill = 'purple', border = 'gray', borderWidth = 1),
        Rect(0, gridSize, gridSize, gridSize, fill = 'purple', border = 'gray', borderWidth = 1),
        Rect(gridSize,gridSize, gridSize,gridSize, fill = 'purple', border = 'gray', borderWidth = 1),
        Rect(gridSize * 2,gridSize, gridSize,gridSize, fill = 'purple', border = 'gray', borderWidth = 1)
        )

def createBlock10(): # ㅁ
    return Group(
            Rect(0,0, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize, 0, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize * 2, 0, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(0,gridSize,gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize, gridSize, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize * 2, gridSize, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(0,gridSize * 2,gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize, gridSize * 2, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1),
            Rect(gridSize * 2, gridSize * 2, gridSize, gridSize, fill = 'orange', border = 'gray', borderWidth = 1)
        )
        
def createBlock11(): # j
    return Group(
            Rect(gridSize, 0, gridSize, gridSize, fill = 'cyan', border = 'gray', borderWidth = 1),
            Rect(0, gridSize, gridSize, gridSize, fill = 'cyan', border = 'gray', borderWidth = 1),
            Rect(gridSize, gridSize, gridSize, gridSize, fill = 'cyan', border = 'gray', borderWidth = 1)
        )
        
def createBlock12(): #ㄱ
    return Group(
        Rect(0, 0, gridSize, gridSize, fill = 'gold', border = 'gray', borderWidth = 1),
        Rect(gridSize, 0, gridSize, gridSize, fill = 'gold', border = 'gray', borderWidth = 1),
        Rect(gridSize, gridSize, gridSize, gridSize, fill = 'gold', border = 'gray', borderWidth = 1)
        )

def createBlock13(): # ㄴ
    return Group(
        Rect(0, 0, gridSize, gridSize, fill = 'magenta', border = 'gray', borderWidth = 1),
        Rect(0, gridSize, gridSize, gridSize, fill = 'magenta', border = 'gray', borderWidth = 1),
        Rect(gridSize, gridSize, gridSize, gridSize, fill = 'magenta', border = 'gray', borderWidth = 1)
        )
        
# TODO: Make some z shapes        
        
blocksFns = [createBlock0,createBlock1, createBlock2, createBlock3 ,createBlock4, createBlock5, createBlock6, createBlock7,  createBlock8, createBlock9, createBlock10, createBlock11, createBlock12, createBlock13]

def spawnRandomBlock(): 
    block = choice(blocksFns)()
    return block
    
activeBlocks = []

def drawBlocks():
    activeBlocks.clear()
    for _ in range(len(blockStorage)):
        newBlock = spawnRandomBlock()
        activeBlocks.append(newBlock)

def changePlace():
        for i in range(min(len(blockStorage), len(activeBlocks))):
            if not blockStorage.children[i].containsShape(activeBlocks[i]):
                activeBlocks[i].centerX = blockStorage.children[i].centerX
                activeBlocks[i].centerY = blockStorage.children[i].centerY
                
def isSpaceOccupied(block):
    for shape in block:
        col = int((shape.left - board.left) // gridSize)
        row = int((shape.top - board.top) // gridSize)
        if not (0 <= row < rows and 0 <= col < cols) or occupiedGrid[row][col]:
            return True
    return False
    
def occupySpace(block):
    for shape in block.children:
        col = int((shape.left - board.left) // gridSize)
        row = int((shape.top - board.top) // gridSize)
        if 0 <= row < rows and 0 <= col < cols:
            if placedBlocks[row][col]:
                placedBlocks[row][col].visible = False
            occupiedGrid[row][col] = True
            placedBlocks[row][col] = shape
            shape.visible = True
    
def releaseSpace(block):
    for shape in block.children:
        col = int((shape.left - board.left) // gridSize)
        row = int((shape.top - board.top) // gridSize)
        if 0 <= row < rows and 0 <= col < cols:
            occupiedGrid[row][col] = False
            if placedBlocks[row][col]:
                placedBlocks[row][col].visible = False
                placedBlocks[row][col] = None
            
def clearRowOrColumn():
    rowsToClear = [row for row in range(rows) if all(occupiedGrid[row])]
    colsToClear = [col for col in range(cols) if all(occupiedGrid[row][col] for row in range(rows))]

    for row in rowsToClear:
        for col in range(cols):
            occupiedGrid[row][col] = False
            if placedBlocks[row][col]:
                placedBlocks[row][col].visible = False
                placedBlocks[row][col] = None

    for col in colsToClear:
        for row in range(rows):
            occupiedGrid[row][col] = False
            if placedBlocks[row][col]:
                placedBlocks[row][col].visible = False
                placedBlocks[row][col] = None
                
    clearCount = len(rowsToClear) + len(colsToClear)
    app.score += clearCount * 100
    scoreBoard.value = f"Score: {app.score}"

def onMousePress(mouseX,mouseY):
    app.dragging = None
    for block in activeBlocks:
        if block.hits(mouseX,mouseY):
            app.dragging = block
            app.dragging.toFront()
            releaseSpace(app.dragging)
            break
        
def onMouseDrag(mouseX,mouseY):
    if app.dragging:
        app.dragging.centerX = mouseX
        app.dragging.centerY = mouseY

def onMouseRelease(mouseX,mouseY):
    if app.dragging:
        if board.hits(mouseX, mouseY):
            app.dragging.left = rounded((app.dragging.left - board.left) / gridSize) * gridSize + board.left
            app.dragging.top = rounded((app.dragging.top - board.top) / gridSize) * gridSize + board.top
            if not isSpaceOccupied(app.dragging):
                occupySpace(app.dragging)
                activeBlocks.remove(app.dragging)
                clearRowOrColumn()
            else:
                changePlace()
        else:
            changePlace()
            
        app.dragging = None
        
    if len(activeBlocks) == 0:
        drawBlocks()
        changePlace()

drawBlocks()
changePlace()

cmu_graphics.run()