# Making a Mod to Mutate an Existing Ship

This is a simple tutorial show all the steps necessary to make our starting TEC scout corvettes super fast.

1. Create a folder for your mod. For this example we will use [examples/mods/super_fast_trader_scout_corvette](../examples/mods/super_fast_trader_scout_corvette)

2. Add a `trader_scout_corvette.unit` file. This will overwrite the `trader_scout_corvette` provided in the base game. Increase `max_linear_speed` from `1200` to `12000`, also incrase `hyperspace.speed` and `hyperspace.charge_time`.

3. Add a `trader_scout_corvette.unit_skin` file to change it's ship name from `trader_scout_corvette_name` to `super_fast_trader_scout_corvette_name`.

4. Add a `en.localized_text_csv` to contain the name to `SUPER FAST SCOUT!`.

5. Run `py .\run-peon.py -s .\examples\mods\super_fast_trader_scout_corvette\ -d .out\super_fast_trader_scout_corvette\`

6. You will now have generated a mod zip package file `super_fast_trader_scout_corvette.zip` that can be uploaded.

7. Browse to [mod.io/sins2](https://mod.io/g/sins2) and Click "Add Mod" in Top Right.

8. Fill out the form describing the mod and add a Logo.

9. `compatibility-version-x` tags are important. As the game evolves the data formats may break mods and the this version will have to be updated. For now select `compatibility-version-2`.

10. Get to STEP 3. Upload your Mod file. Upload the `.zip` file created above.

11. Continue until Mod Status is Accepted.

12. Load up the game. 

13. Navigate to Modding -> Mod.io

14. Select your new mod (Super Fast TEC Scout Corvette) and press Subscribe.

15. Navigate to Modding -> Installed and press Apply Changes.

16. Start a new game and build a super fast scout.

