# A Small Extension to MCPI
original documentation exists at https://www.stuffaboutcode.com/p/minecraft-api-reference.html

The goal of this repository is to add some additional functions to make placing blocks that are direction/color variable or things like doors.

## Example Code

### Sameple House

```python
sample_house(game, x, y ,z)
```
Places a sample_house in the specified game instance at an (x,y,z) coordinate triple.

### Hollow Cube

```python
cube(game, distX, distY, distZ, x, y, z, material)
```
This function is kinda buggy. Spawns a cube in the specified game instance, with specified interior distances at the (x,y,z) coordinate triple of the specifed material.

### Doors

```python
woodDoor(game, x, y, z)
```
Places a wood door in the specified game instance at the (x,y,z) coordinate triple.
```python
ironDoor(game, x, y, z)
```
Places an iron door in the specified game instance at the (x,y,z) coordinate triple.

### Beds

```python
bed(game, x, y, z, orientation)
```
Places a bed in the specified game instance at the (x,y,z) coordinate triple. Orientation is a number {1, 2, 3, 4} that controls the orientation of the bed.

### Colored Wool

```python
mc.setBlocks(me.x, me.y, me.z, block.WOOL.id, COLOR)
```
Where COLOR can be any of the following: **white**, **orange**, **magenta**, **light_blue**, **yellow**, **lime**, **pink**, **grey**, **light_grey**, **cyan**, **purple**, **blue**, **brown**, **green**, **red**, **black**.

### Wood

```python
mc.setBlocks(me.x, me.y, me.z, block.WOOD.id, TYPE)
```
Where TYPE can be any of the following: **oak**, **spruce**, **birch**.

### Sapling

```python
mc.setBlocks(me.x, me.y, me.z, block.SAPLING.id, TYPE)
```
Where TYPE can be any one of the following: **oak**, **spruce**, **birch**.

### Tall Grass
```python
mc.setBlocks(me.x, me.y, me.z, block.GRASS_TALL.id, TYPE)
```
Where TYPE can be any one of the following: **shurb**, **grass**, **fern**.

### Stone Brick
```python
mc.setBlocks(me.x, me.y, me.z, block.STONE_BRICK.id, TYPE)
```
Where TYPE can be any one of the following: **stone**, **mossy**, **cracked**, **chiseled**.

### Stone Slab
```python
mc.setBlocks(me.x, me.y, me.z, block.STONE_SLAB.id, TYPE)
```
Where TYPE can be any one of the following: **stone**, **sandstone**, **wooden**, **cobblestone**, **brick**, **stone_brick**.

### TNT
```python
mc.setBlocks(me.x, me.y, me.z, block.TNT.id, TYPE)
```
Where TYPE can be any one of the following: **inactive**, **active**.

Both blocks look the same, however the active TNT block will explode when hit.

### Leaves
```python
mc.setBlocks(me.x, me.y, me.z, block.LEAVES.id, TYPE)
```
Where TYPE can be any one of the following: **oak**, **spruce**, **birch**.

### Sandstone
```python
mc.setBlocks(me.x, me.y, me.z, block.STANDSTONE.id, TYPE)
```
Where TYPE can be any one of the following: **chiseled**, **smooth**.

### Stairs

```python
mc.setBlocks(me.x, me.y, me.z, block.STAIRS_WOOD.id, TYPE)
mc.setBlocks(me.x, me.y, me.z, block.STAIRS_COBBLESTONE.id, TYPE)
```
Where TYPE can be any one of the following: **east**, **west**, **south**, **north**, **ueast**, **uwest**, **usouth**, **unorth**.

Where the "u" directions are upside down.

### Chests and Furnaces
```python
mc.setBlocks(me.x, me.y, me.z, block.FURNACE_ACTIVE.id, TYPE)
mc.setBlocks(me.x, me.y, me.z, block.FURNACE_INACTIVE.id, TYPE)
```
Where TYPE can be any one of the following: **fnorth**, **fsouth**, **fwest**, **feast**.

### Neather Reactor Core
```python
mc.setBlocks(me.x, me.y, me.z, block.NEATHER_REACTOR_CORE.id, TYPE)
```
Where TYPE can be any one of the following: **unused**, **active**, **inactive**.
