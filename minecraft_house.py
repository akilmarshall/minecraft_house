# Libraries we need
import autobuild
import mcpi.minecraft as minecraft
import mcpi.block as block


# mc is the game instance
mc = minecraft.Minecraft.create('127.0.0.1', 4711)
# me is an object containing the players x, y, and z coordinate
# me = mc.player.getTilePos()
# autobuild.sample_house(mc, me.x, me.y, me.z)


build = autobuild.builder(mc)
build.place_block(block.LEAVES.id, 2, 2, 2, option='spruce')
