# [Iron Engine 3 Tools](https://github.com/IroncladGames/tools)

Public tools provided by Ironclad Games to support modding Iron Engine 3. 
Iron Engine 3 was used to build [Sins of a Solar Empire II](https://store.steampowered.com/app/1575940/Sins_of_a_Solar_Empire_II/)

## Getting Started

- If you are new to git or don't like using the command line, we recommend using https://git-fork.com/ to download these files. Downloading them directly from github will not work. After installing Fork, click File->Clone and use https://github.com/IroncladGames/tools as the repository URL. Fork is a commerical product but there are also a number of free git GUI's out there.
- Most of Iron Engine 3's tools have a soft dependency on [Python 3.x](https://www.python.org/downloads/) to automate cleaning up any JSON files that are generated.
- Download and install `.NET Framework 4.7.2 Runtime` from https://dotnet.microsoft.com/download/dotnet-framework (needed for `SolarForge` and `Peon`)

## Potential Issues

- Do not have a folder structure with spaces in name as they do not work well as command line arguments necessary for Peon.
  - `c:/My Cool Tools` should be `c:/my_cool_tools` or `c:/MyCoolTools`

## [Documentation](./docs/)

- [Making a Mod to Mutate an Existing Ship](./docs/making_a_mod_to_mutate_existing_ship.md)

## [SolarForge](./SolarForge/bin/)

GUI editor for working with:

- Scenarios (maps)
- Particle Effects
- Beam Effects
- Meshes
- Units

### Quick Start

- Run `SolarForge.exe` in [SolarForge/bin](./SolarForge/bin).
- You will be prompted to find the game folder that contains `sins2.exe` as all game assets are located side-by-side in this folder. This is necessary for resolving dependencies between assets. For example a Particle Effect will require finding Textures and Scenarios will require all knowledge of planets and other game assets.
- More documentation on how to use SolarForge will be forthcoming.

## [MeshBuilder](./MeshBuilder/bin/)

Converts raw `gltf` mesh files into Iron Engine 3 specific `mesh` files (either binary or json).

More information on how to author meshes and convert them to `.gltf` from other formats will be forthcoming.

### Quick Start

From command line:
```
.\MeshBuilder\bin\MeshBuilder.exe --input_path=examples/meshes/advent_interceptor_strikecraft.gltf --output_folder_path=.out --mesh_output_format=binary
```

### Mesh Textures

Mesh Textures have specific requirements to look correct with Iron Engine 3's shaders. Use [Texconv](https://github.com/Microsoft/DirectXTex/wiki/Texconv) to convert from `.png` to `.dds` using the specifications below. This process can be simplified and automated by using Peon.

For clarity, user interface elements should stay as `.png` and information on particle textures will be forthcoming.

| Type | Format | Command Line | Example |
| --- | --- | --- | --- |
| [Color](#mesh-color-texture) | `BC7_UNORM` | `Texconv.exe -f BC7_UNORM -y "<path/in.png>" -o "<path/out.dds>"` | [advent_interceptor_strikecraft_clr.png](./examples/meshes/textures/advent_interceptor_strikecraft_clr.png) |
| [Mask](#mesh-mask-texture) | `BC7_UNORM` | `Texconv.exe -f BC7_UNORM -y "<path/in.png>" -o "<path/out.dds>"` | [advent_interceptor_strikecraft_msk.png](./examples/meshes/textures/advent_interceptor_strikecraft_msk.png) |
| [ORM](#mesh-orm-texture) | `BC7_UNORM` | `Texconv.exe -f BC7_UNORM -y "<path/in.png>" -o "<path/out.dds>"` | [advent_interceptor_strikecraft_orm.png](./examples/meshes/textures/advent_interceptor_strikecraft_orm.png) |
| [Normal Map](#mesh-normal-map-texture) | `BC5_SNORM` | `Texconv.exe -f BC5_SNORM -y "<path/in.png>" -o "<path/out.dds>"` | [advent_interceptor_strikecraft_nrm.png](./examples/meshes/textures/advent_interceptor_strikecraft_nrm.png) |

#### Mesh Color Texture

| Red | Green | Blue | Alpha |
| --- | --- | --- | --- |
| red | green | blue | opacity (material dependent) |

#### Mesh Mask Texture

| Red | Green | Blue | Alpha |
| --- | --- | --- | --- |
| primary team color | secondary team color | emissive mask strength | emissive hue strength |

#### Mesh ORM Texture

| Red | Green | Blue | Alpha |
| --- | --- | --- | --- |
| occlusion | roughness | metalness | unused |

#### Mesh Normal Map
- Iron Engine 3 expects a BC5_SNORM dds texture that only encodes x and y. 
- We highly recommend you create a `.png` normal map and convert it to dds with Texconv as described above or Peon as described below. The `.png` should be authored as follows:

| Red | Green | Blue | Alpha |
| --- | --- | --- | --- |
| tangent | bitangent | normal | unused |

- Where the coordinate system is:
	- Positive Y up 
	- Positive Z forward 
	- Positive X right
- In order for normals to work correctly mesh tangents must be exported as Mikktspace tangents.
- If you want to avoid using mesh tangents you will be able to disable Mikkelsen's method and use Schuler's derivative based method which we've left for use in the shader.
- More documentation on how to author mesh normals (and meshes in general) will be forthcoming.

### Effect Textures
Generally the same as a Mesh Texture. All particle textures must have `.texconv` file in the same folder for Peon to build them properly. Refer to [Using Peon to Build Textures](#using-peon-to-build-textures).

### General Texture Notes
All texture sizes must be multiples of 4.

### Using Peon to Build Textures

It is possible to generate `.dds` texture files using the rules described above but we recommend using Peon to automate this process when packaging Mods. Just keep the raw `.png` files and don't worry about generating the correct `.dds` files yourself.

Peon will build textures in two ways:
1. Peon will look for `.mesh_material` file found side-by-side textures to determine the role of each texture. This will be generated by [MeshBuilder](#MeshBuilder). For example [advent_interceptor_strikecraft.mesh_material](./examples/meshes/textures/advent_interceptor_strikecraft.mesh_material)
2. Peon will look for a `.texconv` file in the same directory side-by-side your source textures. This file has rules describing the textures found in the folder.
```
{
    "*.png": "Particle"
}
```

#### Example

1. Download [Texconv](https://github.com/Microsoft/DirectXTex/wiki/Texconv)
2. Run Peon with path to `texconv.exe`
```
py run-peon.py -s .\examples\meshes\textures\ -d .out\converted_mesh_textures\ --texconv_exe_path c:/path/to/your/texconv.exe
py run-peon.py -s .\examples\particles\textures\ -d .out\converted_particle_textures\ --texconv_exe_path c:/path/to/your/texconv.exe
```

### Mesh Materials
Coming at a later date.


## [JSON Schemas](./json_schemas)

[JSON Schema](https://json-schema.org/) files are provided for all entity files used by Iron Engine 3. This will assist authoring and allows files to be validated before they are even loaded.

If using [Visual Studio Code](https://code.visualstudio.com/) you will get auto-complete and invalid value squiggles due to [.vscode/settings.json](./.vscode/settings.json) added to this repo. Check out [trader_scout_corvette.unit](./examples/mods/super_fast_trader_scout_corvette/trader_scout_corvette.unit).

## [Peon](./Peon/bin/)

Peon is a build tool used to prepare and package files for mods. 
- Peon will take any source folder of random structure and prepare it for the structure required for a mod.
- Peon will do any necessary data conversion on source files.
  - `.png` -> `.dds` with optimal settings (e.g. normals vs colors). Refer to [Mesh Textures](#mesh-textures) for more details.
  - `.csv` -> `.localized_text` json

For example given the source:
```
source/foo
    /new_ship
        - new_ship.unit
        - new_ship.mesh
        - new_ship_texture_clr.png
        - new_ship.weapon
        /random_folder_for_more_stuff
            - en.localized_text_csv
```

Peon will restructure the data in a form that the game expects:
```
out/foo
    /entities
        - new_ship.unit
        - new_ship.weapon
    /meshes
        - new_ship.mesh
    /textures
        - new_ship_texture_clr.dds
    /localized_text
        - en.localized_text
```

Peon will then generate `foo.zip` in a form that can be directly uploaded as a complete Mod.

### Quick Start

Use `run-peon.py` script to simplify the command line arguments necessary to run Peon.

```
py .\run-peon.py -s .\examples\mods\super_fast_trader_scout_corvette\ -d .out\super_fast_trader_scout_corvette\
```

### Building Shaders

We will be providing official `.hlsl` shaders at a later date. If you want to create your own shaders you can use Peon to compile them for the game.

If you would like to use Peon to compile shaders:

- Download [DirectXShaderCompiler](https://github.com/microsoft/DirectXShaderCompiler/releases).

```
py .\run-peon.py -s .\examples\shaders\ -d .out\shaders\ --fxc_exe_path c:/path/to/fxc.exe
```

## [LocalizedTextBuilder](./LocalizedTextBuilder/bin/)

Very simple command line app that converts [csv](https://en.wikipedia.org/wiki/Comma-separated_values) files to Iron Engine 3 compatible localized text in `JSON` format.
