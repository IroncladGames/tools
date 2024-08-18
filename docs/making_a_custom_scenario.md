# Making a Custom Scenario (Map)

-  Run SolarForge and File -> New -> Scenario

-  Change `Name` and `Description`, but preserve the `:` prefix. The `:` tells the engine that these are NOT localized strings. Otherwise you will have to also provide localized string files with your new Scenario which is out of scope for this tutorial.

-  By default the topology of all new Scenarios is randomly Generated every game. If do not want this selection Scenario -> Bake Preview.
    - Before you Bake Preview it is important that you set the Skybox, otherwise you will have to manually edit your Scenario as this feature is missing SolarForge (will come soon). The game requires a skybox and won't look correct if none is provided. We recommend `skybox_random`.
    - ![Pick Skybox](images/making_a_custom_scenario/pick_skybox.png)

-  Modify the Scenario as you see fit. More documentation will be provided in the future.

-  File -> Save. Browse to %localappdata%/sins2/mods/. Make a new folder here with your scenario name. Then another folder called `scenarios`. Then save your new scenario file here.
```
C:\Users\Jamie\AppData\Local\sins2\mods\my_first_map\scenarios\my_first_map.scenario
```

-  Add a new file `.mod_meta_data` to the root of your new mod folder. For example `C:\Users\Jamie\AppData\Local\sins2\mods\my_first_map\.mod_meta_data`.
  
```
{
    "compatibility_version": 2
}
```

-  Add a new folder side-by-side `scenarios` called `uniforms`

-  Add `scenario.uniforms` file inside `uniforms` folder. Add a `scenarios` list with your new map here. This tells the engine show this scenario in the front end browser. You also have to add a stub for `fake_server_scenarios`. This will be fixed in a future patch.

```
C:\Users\Jamie\AppData\Local\sins2\mods\my_first_map\uniforms\scenario.uniforms
```
```
{
    "scenarios": [
        "my_first_map"
    ],
    "fake_server_scenarios": []
}
```

Your folder structure should now look like this:

![Final Folder Structure](images/making_a_custom_scenario/folder_structure.png)

- Load the game and Open Modding -> Local tab. Your new mod should be there. Click Enable.

![Modding View](images/making_a_custom_scenario/modding_view.png)

- Go to "Manage" Tab and you should see my_first_map in the mods list. Click "Apply Changes".

-  You should now be able to pick your new map in the list of maps.

![Front End Scenario List](images/making_a_custom_scenario/front_end_scenario_list.png)

- With version 28.4 and above you can host a multiplayer game with your new map. As a host you will auto-magically stream the content to all other players.
