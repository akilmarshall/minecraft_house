import mcpi.block as block
from time import sleep


class builder:
    def __init__(self, game):
        self.game = game
        self.me = self.game.player

    def _x(self):
        """
        return current x coordinate position
        """
        return self.game.player.getTilePos().x

    def _y(self):
        """
        return current y coordinate position
        """
        return self.game.player.getTilePos().y

    def _z(self):
        """
        return current z coordinate position
        """
        return self.game.player.getTilePos().z

    def _place_wool(self, x: int, y: int, z: int, material, option):
        """
        place a wool block of the specified color at the given (x,y,z)
        coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.WOOL.id for the expected behavior
        :param option       string describing the color of the wool block
        """
        select = {'white': 0, 'orange': 1, 'magenta': 2, 'light_blue': 3,
                  'yellow': 4, 'lime': 5, 'pink': 6, 'grey': 7,
                  'light_grey': 8, 'cyan': 9, 'purple': 10, 'blue': 11,
                  'brown': 12, 'green': 13, 'red': 14, 'black': 15}
        if option is None:
            self.game.setBlock(x, y, z, material, select['white'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_wood(self, x: int, y: int, z: int, material, option):
        """
        place a wood block of the specified type at the given (x,y,z)
        coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.WOOD.id for the expected behavior
        :param option       string describing the type of the wood block
        """
        select = {'oak': 0, 'spruce': 1, 'birch': 2}
        if option is None:
            self.game.setBlock(x, y, z, material, select['oak'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_tall_grass(self, x: int, y: int, z: int, material, option):
        """
        place a tall grass block of the given type at the (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.GRASS_TALL.id for the expected
                            behavior
        :param option       string describing the type of the tall grass block
        """
        select = {'shrub': 0, 'grass': 1, 'fern': 2}
        if option is None:
            self.game.setBlock(x, y, z, material, select['shurb'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_torch(self, x: int, y: int, z: int, material, option):
        """
        place a torch on the given face of the block at the (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.TORCH.id for the expected
                            behavior
        :param option       string describing the cardinal orientation of the
                            torch
        """
        select = {'east': 1, 'west': 2, 'south': 3, 'north': 4, 'up': 5}
        if option is None:
            self.game.setBlock(x, y, z, material, select['east'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_stone_brick(self, x: int, y: int, z: int, material, option):
        """
        place a stone brick of the specified type at the (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.STONE_BRICK.id for the expected
                            behavior
        :param option       string describing the type of the stone brick
        """
        select = {'stone': 0, 'mossy': 1, 'cracked': 2, 'chiseled': 3}
        if option is None:
            self.game.setBlock(x, y, z, material, select['stone'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_stone_slab(self, x: int, y: int, z: int, material, option):
        """
        place a stone slab of the specified type at the (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.STONE_SLAB.id for the expected
                            behavior
        :param option       string describing the type of the stone slab
        """
        select = {'stone': 0, 'sstone': 1, 'wood': 2, 'cstone': 3,
                  'brick': 4, 'sbrick': 5}
        if option is None:
            self.game.setBlock(x, y, z, material, select['stone'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_tnt(self, x: int, y: int, z: int, material, option):
        """
        place tnt of the specified type at the (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.TNT.id for the expected behavior
        :param option       string describing the type of tnt
        """
        select = {'inactive': 0, 'active': 1}
        if option is None:
            self.game.setBlock(x, y, z, material, select['inactive'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_leaf(self, x: int, y: int, z: int, material, option):
        """
        place a leaf block of the specified type at the given (x,y,z)
        coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.LEAVES.id for the expected behavior
        :param option       string describing the type of leaf block
        """
        select = {'oak': 1, 'spruce': 2, 'birch': 3}
        if option is None:
            self.game.setBlock(x, y, z, material, select['oak'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_sandstone(self, x: int, y: int, z: int, material, option):
        """
        place a sandstone block of the specified type at the given (x,y,z)
        coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.SANDSTONE.id for the expected
                            behavior
        :param option       string describing the type of sandstone block
        """
        select = {'sstone': 0, 'chiseled': 1, 'smooth': 2}
        if option is None:
            self.game.setBlock(x, y, z, material, select['sstone'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_stair(self, x: int, y: int, z: int, material, option):
        """
        place a stair of the specified type and orientation at the given
        (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.STAIRS_WOOD.id or
                            block.STAIRS_COBBLESTONE.id for the expected
                            behavior
        :param option       string describing the orientation of the stair
                            block
        """
        select = {'east': 0, 'west': 1, 'south': 2, 'north': 3, 'ueast': 4,
                  'uwest': 5, 'usouth': 6, 'unorth': 7}
        if option is None:
            self.game.setBlock(x, y, z, material, select['east'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_ladder(self, x: int, y: int, z: int, material, option):
        """
        place a ladder, chest, furnace, or fence gate in the specified
        orientation at the given (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.LADDER.id, block.CHEST.id,
                            block.FURNACE_ACTIVE, block.FURNACE_INACTIVE,
                            or block.FENCE_GATE for the expected behavior
        :param option       string describing the orientation of the block
        """
        select = {'north': 2, 'south': 3, 'west': 4, 'east': 5}
        if option is None:
            self.game.setBlock(x, y, z, material, select['north'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_nether_reactor_core(self, x: int, y: int, z: int, material,
                                   option):
        """
        place a nether reactor core of the specified type at the given (x,y,z)
        coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.NETHER_REACTOR_CORE.id for the
                            expected behavior
        :param option       string describing the type of nether reactor core
        """
        select = {'unused': 0, 'active': 1, 'inactive': 2}
        if option is None:
            self.game.setBlock(x, y, z, material, select['unused'])
        else:
            self.game.setBlock(x, y, z, material, select[option])

    def _place_liquid(self, x: int, y: int, z: int, material, option):
        """
        place a stationary liquid block of the specified type and level at the
        given (x,y,z) coordinate
        :param x	    x coordinate
        :param y	    y coordinate
        :param z	    z coordinate
        :param material     must be block.WATER_STATIONARY.id or
                            block.LAVA_STATIONARY.id for the expected behavior
        :param option       int [0-7] 0 being the highest level, 7 the lowest
        """
        if option is None:
            self.game.setBlock(x, y, z, material, 7)
        else:
            self.game.setBlock(x, y, z, material, option)

    def _validate(self, material, option):
        """
        if the passed option is None, a default option is selected otherwise
        the option is accepted as is
        :param material         of the form block.{type}.id
        :param option           string key
        """
        defaults = {block.WOOL.id: 'white', block.WOOD.id: 'oak',
                    block.SAPLING.id: 'oak', block.GRASS_TALL: 'shrub',
                    block.TORCH.id: 'east', block.TORCH.id: 'east',
                    block.STONE_SLAB.id: 'stone', block.TNT.id: 'inactive',
                    block.LEAVES.id: 'oak', block.SANDSTONE.id: 'sstone',
                    block.STAIRS_WOOD.id: 'east',
                    block.STAIRS_COBBLESTONE.id: 'east',
                    block.LADDER.id: 'north', block.CHEST.id: 'north',
                    block.FURNACE_ACTIVE.id: 'north',
                    block.FURNACE_INACTIVE.id: 'north',
                    block.FENCE_GATE.id: 'north', block.WATER_STATIONARY.id: 0,
                    block.LAVA_STATIONARY.id: 0,
                    block.NETHER_REACTOR_CORE: 'unused'
                    }
        if option is None:
            return defaults[material]
        else:
            return option

    def place_block(self, material, x: int, y: int, z: int, option=None):
        """
        place block with coordinates relative to the map
        :param material     type of block to place, looks like
                            'block.{TYPE}.id'
        :param x            x coordinate relative to the player
        :param y            y coordinate relative to the player
        :param z            z coordinate relative to the player
        :param option       optional parameter to specify the data for blocks
                            that support this operation
        """
        relative_x = self._x() + x
        relative_y = self._y() + y
        relative_z = self._z() + z
        calls = {
                 block.WOOD.id: self._place_wood,
                 block.WOOL.id: self._place_wool,
                 block.SAPLING.id: self._place_wood,
                 block.GRASS_TALL.id: self._place_tall_grass,
                 block.TORCH.id: self._place_torch,
                 block.STONE_BRICK.id: self._place_stone_brick,
                 block.STONE_SLAB.id: self._place_stone_slab,
                 block.STONE_SLAB_DOUBLE.id: self._place_stone_slab,
                 block.TNT.id: self._place_tnt,
                 block.LEAVES.id: self._place_leaf,
                 block.SANDSTONE.id: self.place_sandstone,
                 block.STAIRS_WOOD.id: self._place_stair,
                 block.STAIRS_COBBLESTONE.id: self._place_stair,
                 block.LADDER.id: self._place_ladder,
                 block.CHEST.id: self._place_ladder,
                 block.FURNACE_ACTIVE.id: self._place_ladder,
                 block.FURNACE_INACTIVE.id: self._place_ladder,
                 block.FENCE_GATE.id: self._place_ladder,
                 block.LAVA_STATIONARY.id: self._place_liquid,
                 block.WATER_STATIONARY.id: self._place_liquid,
                 block.NETHER_REACTOR_CORE.id: self._place_nether_reactor_core,
                 }
        if material in calls:
            calls[material](relative_x, relative_y, relative_z,
                            material, self._validate(option))
        else:
            self.game.setBlock(relative_x, relative_y, relative_z, material)

    def place_block_absolute(self, material, x: int, y: int, z: int,
                             option=None):
        """
        place block with coordinates relative to the map
        :param material     type of block to place, looks like
                            'block.{TYPE}.id'
        :param x            x coordinate relative to the player
        :param y            y coordinate relative to the player
        :param z            z coordinate relative to the player
        :param option       optional parameter to specify the data for blocks
                            that support this operation
        """
        calls = {
                 block.WOOD.id: self._place_wood,
                 block.WOOL.id: self._place_wool,
                 block.SAPLING.id: self._place_wood,
                 block.GRASS_TALL.id: self._place_tall_grass,
                 block.TORCH.id: self._place_torch,
                 block.STONE_BRICK.id: self._place_stone_brick,
                 block.STONE_SLAB.id: self._place_stone_slab,
                 block.STONE_SLAB_DOUBLE.id: self._place_stone_slab,
                 block.TNT.id: self._place_tnt,
                 block.LEAVES.id: self._place_leaf,
                 block.SANDSTONE.id: self.place_sandstone,
                 block.STAIRS_WOOD.id: self._place_stair,
                 block.STAIRS_COBBLESTONE.id: self._place_stair,
                 block.LADDER.id: self._place_ladder,
                 block.CHEST.id: self._place_ladder,
                 block.FURNACE_ACTIVE.id: self._place_ladder,
                 block.FURNACE_INACTIVE.id: self._place_ladder,
                 block.FENCE_GATE.id: self._place_ladder,
                 block.LAVA_STATIONARY.id: self._place_liquid,
                 block.WATER_STATIONARY.id: self._place_liquid,
                 block.NETHER_REACTOR_CORE.id: self._place_nether_reactor_core,
                 }
        if material in calls:
            calls[material](x, y, z,
                            material, self._validate(option))
        else:
            self.game.setBlock(x, y, z, material)

    def place_blocks(self, x0: int, y0: int, z0: int,
                     x1: int, y1: int, z1: int,
                     material, option=None):
        """
        fill the area between (x0,y0,z0) and (x1,y1,z1) with blocks of the
        specified material
        :param material     type of block to place, looks like
                            'block.{TYPE}.id'
        :param x0            x coordinate relative to the player
        :param y0            y coordinate relative to the player
        :param z0            z coordinate relative to the player
        :param x1            x coordinate relative to the player
        :param y2            y coordinate relative to the player
        :param z3            z coordinate relative to the player
        :param option       optional parameter to specify the data for blocks
                            that support this operation
        """
        for i in range(abs(x0 - x1) + 1):
            x = min(x0, x1) + i
            for j in range(abs(y0 - y1) + 1):
                y = min(y0, y1) + j
                for k in range(abs(z0 - z1) + 1):
                    z = min(z0, z1) + k
                    self.place_block(material, x, y, z, option=option)

    def place_blocks_absolute(self, x0: int, y0: int, z0: int,
                              x1: int, y1: int, z1: int,
                              material, option=None):
        """
        fill the area between (x0,y0,z0) and (x1,y1,z1) with blocks of the
        specified material
        :param material     type of block to place, looks like
                            'block.{TYPE}.id'
        :param x0            x coordinate relative to the player
        :param y0            y coordinate relative to the player
        :param z0            z coordinate relative to the player
        :param x1            x coordinate relative to the player
        :param y2            y coordinate relative to the player
        :param z3            z coordinate relative to the player
        :param option       optional parameter to specify the data for blocks
                            that support this operation
        """
        for i in range(abs(x0 - x1) + 1):
            x = min(x0, x1) + i
            for j in range(abs(y0 - y1) + 1):
                y = min(y0, y1) + j
                for k in range(abs(z0 - z1) + 1):
                    z = min(z0, z1) + k
                    self.place_block_absolute(material, x, y, z, option=option)

    def place_hollow_cuboid(self, x: int, y: int, z: int,
                            xlen: int, ylen: int, zlen: int,
                            material, option=None):
        x += self._x()
        y += self._y()
        z += self._z()
        self.place_blocks(x, y, z,
                          x, y + ylen, z + zlen,
                          material, option=option)
        self.place_blocks(x, y, z,
                          x + xlen, y, z + zlen,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x + xlen, y, z,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x, y + ylen, z,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x, y, z + zlen,
                          material, option=option)

    def place_hollow_cuboid_absolute(self, x: int, y: int, z: int,
                                     xlen: int, ylen: int, zlen: int,
                                     material, option=None):
        self.place_blocks(x, y, z,
                          x, y + ylen, z + zlen,
                          material, option=option)
        self.place_blocks(x, y, z,
                          x + xlen, y, z + zlen,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x + xlen, y, z,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x, y + ylen, z,
                          material, option=option)
        self.place_blocks(x + xlen, y + ylen, z + zlen,
                          x, y, z + zlen,
                          material, option=option)

    def place_wood_door(self, x: int, y: int, z: int):
        """
        place a wood door and the specified Cartesian triple
        :param x	x coordinate to place door at
        :param y        y coordinate to place door at
        :param z        z coordinate to place door at
        """
        x += self._x()
        y += self._y()
        z += self._z()
        self.game.setBlock(x, y, z, block.DOOR_WOOD.id, 2)
        self.game.setBlock(x, y + 1, z, block.DOOR_WOOD.id, 9)

    def place_wood_door_absolute(self, x: int, y: int, z: int):
        """
        place a wood door and the specified Cartesian triple
        :param x	x coordinate to place door at
        :param y        y coordinate to place door at
        :param z        z coordinate to place door at
        """
        self.game.setBlock(x, y, z, block.DOOR_WOOD.id, 2)
        self.game.setBlock(x, y + 1, z, block.DOOR_WOOD.id, 9)

    def place_iron_door(self, x: int, y: int, z: int):
        """
        place an iron door and the specified Cartesian triple
        :param x	x coordinate to place door at
        :param y        y coordinate to place door at
        :param z        z coordinate to place door at
        """
        x += self._x()
        y += self._y()
        z += self._z()
        self.game.setBlock(x, y, z, block.DOOR_IRON.id, 2)
        self.game.setBlock(x, y + 1, z, block.DOOR_IRON.id, 9)

    def place_iron_door_absolute(self, x: int, y: int, z: int):
        """
        place an iron door and the specified Cartesian triple
        :param x	x coordinate to place door at
        :param y        y coordinate to place door at
        :param z        z coordinate to place door at
        """
        self.game.setBlock(x, y, z, block.DOOR_IRON.id, 2)
        self.game.setBlock(x, y + 1, z, block.DOOR_IRON.id, 9)

    def place_bed(self, x: int, y: int, z: int, option=0):
        """
        spawn a bed at the specified Cartesian triple with an orientation
        (1, 2, 3, or 4, default 1)
        :param game             game instance
        :param x	        x coordinate to place bed at
        :param y                y coordinate to place bed at
        :param z                z coordinate to place bed at
        :param orientation      TODO correspond 1, 2, 3, 4 to cardinal
                                directions for this documentation
        """
        x += self._x()
        y += self._y()
        z += self._z()
        if option == 0:
            self.game.setBlock(x, y, z, block.BED.id, 8)
            self.game.setBlock(x, y, z - 1, block.BED.id, 0)
        elif option == 1:
            self.game.setBlock(x, y, z, block.BED.id, 10)
            self.game.setBlock(x, y, z + 1, block.BED.id, 2)
        elif option == 2:
            self.game.setBlock(x, y, z, block.BED.id, 9)
            self.game.setBlock(x + 1, y, z, block.BED.id, 5)
        elif option == 3:
            self.game.setBlock(x, y, z, block.BED.id, 11)
            self.game.setBlock(x - 1, y, z, block.BED.id, 3)

    def place_bed_absolute(self, x: int, y: int, z: int, option=0):
        """
        spawn a bed at the specified Cartesian triple with an orientation
        (1, 2, 3, or 4, default 1)
        :param game             game instance
        :param x	        x coordinate to place bed at
        :param y                y coordinate to place bed at
        :param z                z coordinate to place bed at
        :param orientation      TODO correspond 1, 2, 3, 4 to cardinal
                                directions for this documentation
        """
        x += self._x()
        y += self._y()
        z += self._z()
        if option == 0:
            self.game.setBlock(x, y, z, block.BED.id, 8)
            self.game.setBlock(x, y, z - 1, block.BED.id, 0)
        elif option == 1:
            self.game.setBlock(x, y, z, block.BED.id, 10)
            self.game.setBlock(x, y, z + 1, block.BED.id, 2)
        elif option == 2:
            self.game.setBlock(x, y, z, block.BED.id, 9)
            self.game.setBlock(x + 1, y, z, block.BED.id, 5)
        elif option == 3:
            self.game.setBlock(x, y, z, block.BED.id, 11)
            self.game.setBlock(x - 1, y, z, block.BED.id, 3)


# old API methods


def cube(game, distX, distY, distZ, x, y, z, material):
    '''
        This function will create a cube at the specified (x,y,z) coordinate
        the inner dimensions are defined by 2*distX and 2*distZ with an inner
        height of distY
    '''
    """
    creates a cube at the specified Cartesian triple. The inner dimensions are
    2 * distX and 2 * distZ with an inner height of distY
    :param game         game instance
    :param distX        one of the inner dimensions is 2 * distX
    :param distY        one of the inner dimensions is 2 * distY
    :param distZ        inner height = distY
    :param x            x coordinate at the cube's center
    :param y            y coordinate at the cube's center
    :param z            z coordinate at the cube's center
    :param material     block type to make the cube out of
    """
    # floor
    game.setBlocks(
            x - distX, y, z - distZ,
            x + distX, y, z + distZ,
            material)
    # walls
    game.setBlocks(
            x - distX, y, z - distZ,
            x + distX, y + distY, z - distZ,
            material)
    game.setBlocks(
            x - distX, y, z+distZ,
            x + distX, y + distY, z + distZ,
            material)
    game.setBlocks(
            x - distX, y, z-distZ,
            x - distX, y + distY, z + distZ,
            material)
    game.setBlocks(
            x + distX, y, z - distZ,
            x + distX, y + distY, z + distZ,
            material)
    # ceiling
    game.setBlocks(
            x - distX, y + distY, z - distZ,
            x + distX, y + distY, z + distZ,
            material)


def wood_door(game, x, y, z):
    """
    place a wood door and the specified Cartesian triple
    :param game     game instance
    :param x	    x coordinate to place door at
    :param y        y coordinate to place door at
    :param z        z coordinate to place door at
    """
    game.setBlock(
            x, y, z,
            block.DOOR_WOOD.id, 2)
    game.setBlock(
            x, y + 1, z,
            block.DOOR_WOOD.id, 9)


def iron_door(game, x, y, z):
    """
    place an iron door and the specified Cartesian triple
    :param game     game instance
    :param x	    x coordinate to place door at
    :param y        y coordinate to place door at
    :param z        z coordinate to place door at
    """
    game.setBlock(
            x, y, z,
            block.DOOR_IRON.id, 2)
    game.setBlock(
            x, y + 1, z,
            block.DOOR_IRON.id, 9)


def bed(game, x, y, z, orientation=1):
    """
    spawn a bed at the specified Cartesian triple with an orientation
    (1, 2, 3, or 4, default 1)
    :param game             game instance
    :param x	            x coordinate to place bed at
    :param y                y coordinate to place bed at
    :param z                z coordinate to place bed at
    :param orientation      TODO correspond 1, 2, 3, 4 to cardinal directions
                            for this documentation
    """
    if orientation == 0:
        game.setBlock(
                x, y, z,
                block.BED.id, 8)
        game.setBlock(
                x, y, z - 1,
                block.BED.id, 0)
    elif orientation == 1:
        game.setBlock(
                x, y, z,
                block.BED.id, 10)
        game.setBlock(
                x, y, z + 1,
                block.BED.id, 2)
    elif orientation == 2:
        game.setBlock(
                x, y, z,
                block.BED.id, 9)
        game.setBlock(
                x + 1, y, z,
                block.BED.id, 5)
    elif orientation == 3:
        game.setBlock(
                x, y, z,
                block.BED.id, 11)
        game.setBlock(
                x - 1, y, z,
                block.BED.id, 3)


def sample_house(game, x, y, z):
    """
    sample_house spawns a model house created using some of the functions above
    at the specified Cartesian triple
    :param game     game instance
    :param x	    x coordinate to place door at
    :param y        y coordinate to place door at
    :param z        z coordinate to place door at
    """
    delay = 1
    game.postToChat('Spawing in the sample_house')
    game.postToChat('3')
    sleep(delay)
    game.postToChat('2')
    sleep(delay)
    game.postToChat('1')
    sleep(delay)
    # void the area
    game.setBlocks(
            x - 20, y - 1, z - 20,
            x + 20, y + 100, z + 20,
            block.AIR.id)
    # create a floor
    game.setBlocks(
            x - 4, y - 1, z - 4,
            x + 4, y - 1, z + 4,
            block.BRICK_BLOCK.id)
    # create walls, by fixing z at the -7 and +7 value with out restricting x
    # and then fixing x at -7 and +7 without restricting z
    game.setBlocks(
            x - 3, y + 0, z - 3,
            x + 3, y + 4, z - 3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x - 3, y + 0, z + 3,
            x + 3, y + 4, z + 3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x - 3, y + 0, z - 3,
            x - 3, y + 4, z + 3,
            block.WOOD_PLANKS.id)
    game.setBlocks(
            x + 3, y + 0, z - 3,
            x + 3, y + 4, z + 3,
            block.WOOD_PLANKS.id)
    # build a pyramid roof shape
    for j, i in enumerate(range(4, 1, -1)):
        game.setBlocks(
                x - i, y + 4 + j, z - i,
                x + i, y + 4 + j, z + i,
                block.BRICK_BLOCK.id)
    # lower door block
    game.setBlock(
            x + 3, y + 0, z + 0,
            block.DOOR_WOOD.id, 2)
    # upper door block
    game.setBlock(
            x + 3, y + 1, z,
            block.DOOR_WOOD.id, 9)
    # place bed
    game.setBlock(
            x - 2, y + 0, z - 2,
            block.BED.id)
    game.setBlock(
            x - 2, y + 0, z - 1,
            block.BED.id, 8)
    # place torches
    game.setBlock(
            x + 2, y + 2, z + 2,
            block.TORCH.id)
    game.setBlock(
            x + 2, y + 2, z - 2,
            block.TORCH.id)
    game.setBlock(
            x - 2, y + 2, z + 2,
            block.TORCH.id)
    game.setBlock(
            x - 2, y + 2, z - 2,
            block.TORCH.id)
    # make windows
    game.setBlocks(
            x - 3, y + 1, z - 2,
            x - 3, y + 1, z + 2,
            block.GLASS_PANE.id)
    game.setBlocks(
            x + 2, y + 1, z - 3,
            x - 2, y + 1, z - 3,
            block.GLASS_PANE.id)
    game.setBlocks(
            x + 2, y + 1, z + 3,
            x - 2, y + 1, z + 3,
            block.GLASS_PANE.id)
    game.setBlocks(
            x + 3, y + 1, z + 1,
            x + 3, y + 1, z + 2,
            block.GLASS_PANE.id)
    game.setBlocks(
            x + 3, y + 1, z - 1,
            x + 3, y + 1, z - 2,
            block.GLASS_PANE.id)
    # make a patio
    game.setBlocks(
            x + 4, y - 1, z + 3,
            x + 7, y - 1, z - 3,
            block.WOOD_PLANKS.id)
    # put fence on the patio
    game.setBlocks(
            x + 4, y + 0, z + 3,
            x + 7, y + 0, z + 3,
            block.FENCE.id)
    game.setBlocks(
            x + 4, y + 0, z - 3,
            x + 7, y + 0, z - 3,
            block.FENCE.id)
    game.setBlocks(
            x + 7, y + 0, z - 3,
            x + 7, y + 0, z + 3,
            block.FENCE.id)
    # make a fence gate
    game.setBlock(
            x + 7, y + 0, z + 0,
            block.FENCE_GATE.id, 1)
