---
label: "Step 1: Geometry"
---

# Step 1: Gemoetry

## Overview

In OPTUM CS the model is described through different types of blocks. Each block is used for several geometries. A block includes e.g. the concrete and steel material parameters, the reinforcement arrangement and other parameters.

## **Walls**

Create a wall:

*   Choose the wall block named "200 mm C30 S550 2xØ6/150" from the BLOCKS tab in the ribbon, by clicking it.

![](https://optumce.com/wp-content/uploads/2021/11/wall-block-1.png)

*   Create a wall by clicking two grid line intersections, D/4 and D/6.

[![](https://optumce.com/wp-content/uploads/2021/11/wall-on-gridlines.png)](https://optumce.com/wp-content/uploads/2021/11/wall-on-gridlines.png)

*   Press ESC to leave the tool.

Edit the wall:

*   Select the wall by clicking the wall geometry.
*   In the _Properties_ pane, locate properties related to the Wall and change _Top level_ to _Level 5_.

[![](https://optumce.com/wp-content/uploads/2021/11/wall-properties-1024x823.png)](https://optumce.com/wp-content/uploads/2021/11/wall-properties.png) 
Control the view: Pan by using middle mouse button and orbit by using Ctrl + middle mouse button.

## **Decks**

In OPTUM CS Decks distribute vertical loads to the surrounding walls and create horizontal joints where they intersect with walls. Create decks:

*   Choose the deck block named "300 mm" from the BLOCKS tab in the ribbon.
*   Move up one level using the green arrow in the left top corner of the canvas.
*   Create a deck by clicking two grid line intersections, D/4 and F/6.

[![](https://optumce.com/wp-content/uploads/2021/11/draw-deck-1-1024x771.png)](https://optumce.com/wp-content/uploads/2021/11/draw-deck-1.png)

*   Press ESC to leave the tool.

Edit deck:

*   Select the deck geometry. Use TAB to cycle through objects at cursor.
*   In the deck properties change _Span Direction_ to _4_.

[![](https://optumce.com/wp-content/uploads/2021/11/span-direction-1024x906.png)](https://optumce.com/wp-content/uploads/2021/11/span-direction.png) 
Now copy the deck to Level 3, 4 and 5:

*   Select the deck, press Ctrl + c to begin copying,
*   click grid line intersection D/4, move up one level (use keypad plus "+"),
*   press Ctrl + v to begin pasting,
*   click grid line intersection D/4,
*   move up one level,
*   paste again by clicking and
*   continue until all levels have decks.

[![](https://optumce.com/wp-content/uploads/2021/11/copy-paste-decks-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/copy-paste-decks.png) 
Horizontal joints are automatically created where decks and walls collide, using the highlighted horizontal joint block, in this case the one named "C25 2xØ12 Ø8/300". The wall now contains four concrete elements / panels.

*   Press ESC to leave the tool.

## **Holes**

*   Choose the hole block named "1000x2100" from the BLOCKS tab in the ribbon.

Create a hole by clicking two points on the wall geometry:

*   First the insertion point
*   then a point in one of the four quadrants around the insertion point to choose the relative position.

[![](https://optumce.com/wp-content/uploads/2021/11/draw-hole-1024x775.png)](https://optumce.com/wp-content/uploads/2021/11/draw-hole.png)

*   Press ESC to leave the tool.

Edit the hole:

*   Select the hole geometry.
*   In the hole properties change _X Offset \[mm\]_ to _800_ to move the hole 800 mm away from the edge of the wall.

Create a new hole block:

*   Right click the hole block named "1000x2100" and
*   choose _Clone_ in the pop up menu.

[![](https://optumce.com/wp-content/uploads/2021/11/clone-hole-block.png)](https://optumce.com/wp-content/uploads/2021/11/clone-hole-block.png)

*   In the sized hole properties for the new hole block change _Height \[mm\]_ to _1300_.

Create a hole on the next level above the first hole:

*   Move the cursor to the top left corner of the first hole,
*   keep Alt key down to snap to vertical (or horizontal) auxiliary line,
*   move cursor up,
*   click to create insertion point,
*   release Alt key,
*   click second point to choose relative position and insert hole.

[![](https://optumce.com/wp-content/uploads/2021/11/alt-snap-hole-1024x627.png)](https://optumce.com/wp-content/uploads/2021/11/alt-snap-hole.png)

*   Press ESC to leave the tool.

Edit the hole:

*   Select the new hole geometry.
*   In the hole properties change _Y Offset \[mm\]_ to 3_800_ to move the hole to a position 3800 mm above the bottom of the wall.

Create freely sized holes on the wall using the hole block named "Hole". Try to make the wall elevation look like the one in the next illustration. Try to make use of snap and copy-paste. Copy-paste multiple holes by pressing the Shift key to select several holes. 
[![](https://optumce.com/wp-content/uploads/2021/11/holes-in-wall-elevation-2-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/holes-in-wall-elevation-2.png)

## Vertical joints

*   Choose the vertical joint block named "S550 2xØ8/300" from the BLOCKS tab in the ribbon.

Create a vertical joint by clicking two points on the wall geometry:

*   First a point on level 1,
*   then a point on level 2.

The wall now contains four concrete elements.

*   Press ESC to leave the tool.

To edit the position on the wall, select the vertical joint geometry, locate the properties related to the vertical joint and change _Offset \[mm\]_. 
[![](https://optumce.com/wp-content/uploads/2021/11/vertical-joint-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/vertical-joint.png) 
Next step is adding reinforcement.