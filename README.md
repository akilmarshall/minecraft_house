# A Small Extension to MCPI
original documentation exists at https://www.stuffaboutcode.com/p/minecraft-api-reference.html

The goal of this repository is to add some additional functions to make placing blocks that are direction/color variable or things like doors.

### Hollow Cube

```python
cube(game, distX, distY, distZ, x, y, z, material)
```
This function is kinda buggy. Spawns a cube in the specified game instance, with specified interior distances at the (x,y,z) coordinate triple of the specifed material.

example:
```python

```

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

### Sameple House

```python
sample_house(game, x, y ,z)
```
Places a sample_house in the specified game instance at an (x,y,z) coordinate triple.
