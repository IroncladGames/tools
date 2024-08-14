# Solar Forge

All in one tool for creating and managing assets loaded by the game.

## Coordinate Systems

- x = cross
- y = up
- z = forward

All axes in SolarForge are rendered RGB to match XYZ. So Green = Up, Blue = Forward

## Asset Loading

Game assets always reference other game assets. The simplest example is meshes referencing textures by name. If you load up a mesh file at where does SolarForge find the texture files? SolarForge will always search for assets by name the exact way the game does. First in any assigned mods, then in the assigned Sins2 base folder.
