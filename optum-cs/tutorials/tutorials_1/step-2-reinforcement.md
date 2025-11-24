---
label: "Step 2: Reinforcement"
---

# Step 2: Reinforcement

## Reinforcement types

OPTUM CS has three types of reinforcement: Net reinforcement, reinforcement (blocks) and discrete rebars (blocks).

## Net reinforcement

Edit the net reinforcement properties:

*   Click wall block "200 mm C30 S550 2xØ6/150" in the BLOCKS tab (the wall block that was used when creating the wall).
*   Change _Steel_ to _S500_. Change _Cover, frontside \[mm\]_ and _Cover, backside \[mm\]_ to _25._
*   Change _Horizontal Reinforcement_ to 2xØ8/400 and _Vertical Reinforcement_ to 2xØ8/250, by changing _Diameter \[mm\]_, _Layers_ and _Spacing \[mm\]._
*   Also change _Anchorage \[mm\]_ to 320 for both directions. The name of the wall block automatically updates.

These changes will apply to all walls that use this block. 

[![](https://optumce.com/wp-content/uploads/2021/11/net-reinforcement.png)](https://optumce.com/wp-content/uploads/2021/11/net-reinforcement.png)

## Reinforcement

*   Choose the reinforcement block named "S550 2xØ12 S550 2xØ6/150" from the BLOCKS tab in the ribbon.
*   In the reinforcement block properties change the _Diameter \[mm\]_ of the _Beam Top / Column Right Rebars_ to _12._

Create beam reinforcement above the door and window hole:

*   Click the top left corner of the door hole and click a second point above the top right corner of the window. The cursor will automatically snap to the point in the bottom of the horizontal joint.

[![](https://optumce.com/wp-content/uploads/2021/11/reinforcement-block-1-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/reinforcement-block-1.png)

*   Press ESC to leave the tool.
*   Select the reinforcement geometry that was just created.
*   Change _Rebar extension (-) \[mm\]_ and _Rebar extension (+) \[mm\]_ to _480_.

[![](https://optumce.com/wp-content/uploads/2021/11/reinforcement-edit-1-1024x725.png)](https://optumce.com/wp-content/uploads/2021/11/reinforcement-edit-1.png) 
Create column reinforcement:

*   Choose the reinforcement block again and add reinforcement between the door and the window by clicking two corner points.
*   Change Rebar extension (+) \[mm\] to 480 in the reinforcement properties.

[![](https://optumce.com/wp-content/uploads/2021/11/reinforcement-column-1024x579.png)](https://optumce.com/wp-content/uploads/2021/11/reinforcement-column.png) 

Assign reinforcement automatically:

*   Click the reinforcement button in the top left corner of the canvas.
*   In the menu, change _Beams_ and _Columns_ to _Minimum (creates blocks)_ and click OK.

New reinforcement blocks are created and reinforcement geometries inserted if missing. 

[![](https://optumce.com/wp-content/uploads/2021/11/reinforcement-automatic-1024x554.png)](https://optumce.com/wp-content/uploads/2021/11/reinforcement-automatic.png) 

The reinforcement replace the net reinforcement in both directions.

## Discrete rebars

Add vertical stringers:

*   Choose the rebar block named "S550 Ø25" from the BLOCKS tab in the ribbon.
*   Create a vertical stringer in each side of the wall elevation by clicking two points; first a point at the bottom of the wall, then a point just below the top of the top concrete element.

Add rebars to beams:

*   Choose the rebar block named "S550 Ø20" from the BLOCKS tab in the ribbon.
*   Change _Number of bars_ to _2_.
*   Create rebars in the bottom of the two long beams in level 1 and 2 by clicking start and end point.
*   Adjust the position of the discrete rebars by changing _X Offset \[mm\]_ and _Y Offset \[mm\]_ for _Start_ and _End_ in the properties for the rebar geometries.

[![](https://optumce.com/wp-content/uploads/2021/11/rebars-1024x554.png)](https://optumce.com/wp-content/uploads/2021/11/rebars.png) 
Next step is adding loads.