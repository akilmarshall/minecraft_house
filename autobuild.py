import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
'''
    This function will create a cube at the specified (x,y,z) coordinate
    the inner dimensions are defined by 2*distX and 2*distZ with an inner height of distY 
'''
def cube(game, distX, distY, distZ, x, y, z, material):
    #floor
    game.setBlocks(
            x-distX, y      , z-distZ,
            x+distX, y      , z+distZ,
            material)
    #walls
    game.setBlocks(
            x-distX, y       , z-distZ,
            x+distX, y+distY , z-distZ,
            material)
    game.setBlocks(
            x-distX, y       , z+distZ,
            x+distX, y+distY , z+distZ,
            material)
    game.setBlocks(
            x-distX, y       , z-distZ,
            x-distX, y+distY , z+distZ,
            material)
    game.setBlocks(
            x+distX, y       , z-distZ,
            x+distX, y+distY , z+distZ,
            material)
    #ceiling
    game.setBlocks(
            x-distX, y+distY , z-distZ,
            x+distX, y+distY , z+distZ,
            material)
'''
    woodDoor and ironDoor create their respective doors at the (x,y,z) coordinate specified
'''
def woodDoor(game,x,y,z):
    game.setBlock(
            x,y,z,
            block.DOOR_WOOD.id,2)
    game.setBlock(
            x,y+1,z,
            block.DOOR_WOOD.id,9)
def ironDoor(game,x,y,z):
    game.setBlock(
            x,y,z,
            block.DOOR_IRON.id,2)
    game.setBlock(
            x,y+1,z,
            block.DOOR_IRON.id,9)
'''
    bed spawns a bed whoses pillow side is at the (x,y,z) coordinate specified, in 1 or 4 orientations
'''
def bed(game,x,y,z,orientation):
    if orientation == 0:
        game.setBlock(
                x,y,z,
                block.BED.id,8)
        game.setBlock(
                x,y,z-1,
                block.BED.id,0)
    elif orientation == 1:
        game.setBlock(
                x,y,z,
                block.BED.id,10)
        game.setBlock(
                x,y,z+1,
                block.BED.id,2)
    elif orientation == 2:
        game.setBlock(
                x,y,z,
                block.BED.id,9)
        game.setBlock(
                x+1,y,z,
                block.BED.id,5)
    elif orientation == 3:
        game.setBlock(
                x,y,z,
                block.BED.id,11)
        game.setBlock(
                x-1,y,z,
                block.BED.id,3)
'''
    akil spawns a model house Akil created using some of the functions above at the specified (x,y,z) coordinate
'''
def akil(game,x,y,z):
    delay = 1
    game.postToChat("Hello, world. Spawning Akil's house in")
    game.postToChat("3")
    sleep(delay)
    game.postToChat("2")
    sleep(delay)
    game.postToChat("1")
    sleep(delay)
    #void the area
    game.setBlocks(
            x-20,y-1,z-20,
            x+20,y+100,z+20,
            block.AIR.id)
    #create a floor
    game.setBlocks(
            x-4,y-1,z-4,
            x+4,y-1,z+4,
            block.BRICK_BLOCK.id)
    #create walls, by fixing z at the -7 and +7 value with out restricting x
    #and then fixing x at -7 and +7 without restricting z
    game.setBlocks(
            x-3,y+0,z-3,
            x+3,y+4,z-3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x-3,y+0,z+3,
            x+3,y+4,z+3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x-3,y+0,z-3,
            x-3,y+4,z+3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x+3,y+0,z-3,
            x+3,y+4,z+3,
            block.WOOD_PLANKS.id)
    #build a pyramid roof shape
    j=0
    for i in range(4, 1, -1):
        game.setBlocks(
                x-i,y+4+j,z-i,
                x+i,y+4+j,z+i,
                block.BRICK_BLOCK.id)
        j+=1
    #lower door block
    game.setBlock(
            x+3,y+0,z+0,
            block.DOOR_WOOD.id,2)
    #upper door block
    game.setBlock(
            x+3,y+1,z,
            block.DOOR_WOOD.id,9)
    #place bed
    game.setBlock(
            x-2,y+0,z-2,
            block.BED.id)
    game.setBlock(
            x-2,y+0,z-1,
            block.BED.id,8)
    #place torches
    game.setBlock(
            x+2,y+2,z+2,
            block.TORCH.id)
    game.setBlock(
            x+2,y+2,z-2,
            block.TORCH.id)
    game.setBlock(
            x-2,y+2,z+2,
            block.TORCH.id)
    game.setBlock(
            x-2,y+2,z-2,
            block.TORCH.id)
    #make windows
    game.setBlocks(
            x-3,y+1,z-2,
            x-3,y+1,z+2,
            block.GLASS_PANE.id)
    game.setBlocks(
            x+2,y+1,z-3,
            x-2,y+1,z-3,
            block.GLASS_PANE.id)
    game.setBlocks(
            x+2,y+1,z+3,
            x-2,y+1,z+3,
            block.GLASS_PANE.id)
    game.setBlocks(
            x+3,y+1,z+1,
            x+3,y+1,z+2,
            block.GLASS_PANE.id)
    game.setBlocks(
            x+3,y+1,z-1,
            x+3,y+1,z-2,
            block.GLASS_PANE.id)
    #make a patio
    game.setBlocks(
            x+4,y-1,z+3,
            x+7,y-1,z-3,
            block.WOOD_PLANKS.id)
    #put fence on the patio
    game.setBlocks(
            x+4,y+0,z+3,
            x+7,y+0,z+3,
            block.FENCE.id)
    game.setBlocks(
            x+4,y+0,z-3,
            x+7,y+0,z-3,
            block.FENCE.id)
    game.setBlocks(
            x+7,y+0,z-3,
            x+7,y+0,z+3,
            block.FENCE.id)
    #make a fence gate
    game.setBlock(
            x+7,y+0,z+0,
            block.FENCE_GATE.id,1)