# Horizontal Joints

## Background

Horizontal joints are modelled as reinforced concrete in plane stress coupled with two interfaces. The core of the joint is defined by a height, _h_, and width, _b_, which are given as:

*   Height: Automatically set to the height of the associated deck.
*   Width: Defined by the user. Different width can be set for inner and outer joints. See example of inner and outer joint in below figure

![Left: Inner joint. Right: Outer joint (facades)](https://optumce.com/wp-content/uploads/2019/11/HorizontalJoints-1024x621.png)

In practice, a horizontal joint is usually associated with the following reinforcement:

*   Stringers: A number of horizontal rebars placed in the grout of the joint. Loop reinforcement (U-bars) are typically used to create a connection between the slabs and the joint.
*   Vertical reinforcement: Extruding reinforcement from the precast panel below the joint. This can be either simple rods or U-bars.

In OPTUM CS, the stringer reinforcement as well as the extruding rebars can be defined. The U-bars in the deck are not considered, and the capacity of the interface between the slab and joint should be checked separately.

## Modelling in OPTUM CS

Horizontal joints are automatically added to the model, whenever a deck intersects of a wall. Contrary to the other blocks, the horizontal joints functions as a mode, and the horizontal joint block selected as the current mode is added when intersections are detected.

As mentioned above, the horizontal joint comes in two different varieties, namely the inner joint with slabs from both sides, and the outer joint with slabs from one side. OPTUM CS automatically detects which type

The two different joint types are automatically registered by OPTUM CS in the following manner:

*   Outer joint: Used when a single deck ends on a wall.
*   Inner joint: Used either two decks meet on a wall or a single deck is placed across several walls.

In each case, the only different parameter in the joint definition is the width of the joint defined as "Outer Joint Width" and "Inner Joint Width". The reinforcement arrangement is identical.

![](https://optumce.com/wp-content/uploads/2018/11/horizontal_joint-1-1024x745.png)

The upper interface refers to the interface between the horizontal joint and precast concrete panel above, while the lower interface refers to the interface between the joint and the precast concrete panel below. It is only possible to define extruding reinforcement for the lower interface.