#Libraries we need
import mcpi.minecraft as minecraft
import mcpi.block as block
from autobuild import *
from time import sleep

#some variables we need to set
mc = minecraft.Minecraft.create("127.0.0.1", 4711)
me = mc.player.getTilePos()

#Build a house below this line!
#block.NAME.id