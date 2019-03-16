#Libraries we need
from autobuild import *

#some variables we need to set
mc = minecraft.Minecraft.create("127.0.0.1", 4711)
me = mc.player.getTilePos()
#sample_house(mc, me.x, me.y, me.z)
#Build a house below this line!
