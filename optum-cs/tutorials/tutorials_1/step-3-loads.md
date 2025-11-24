---
label: "Step 3: Loads"
---

# Step 3: Loads

## Self weight

Edit the self weight of the wall:

*   In the BLOCKS tab in the ribbon, choose the wall block named "200 mm C30 S500 2xØ8/400 S500 2xØ8/250" (or any other wall block).
*   In the wall block properties the default value of _Weight \[kN/m³\]_ is _25_.
*   Load from masonry, insulation etc. acting on the façade is added by changing _Surface load \[kN/m²\]_ in _Vertical surface_ load to _2_. 

[![](https://optumce.com/wp-content/uploads/2021/11/self-weight-properties.png)](https://optumce.com/wp-content/uploads/2021/11/self-weight-properties.png)

## Load types and load definitions

Create load definitions:

*   In the LOADS tab in the ribbon choose _Define loads_. 
*   In the load types table, add four more load types by pressing _New_. 
*   Change the names, Categories and Nominal loads as pictured below. 
*   In the load definitions table, add another load definition by pressing _New_. 
*   Change the names and included load types as pictured below.

[![](https://optumce.com/wp-content/uploads/2021/11/load-types-and-definitions-1-1024x490.png)](https://optumce.com/wp-content/uploads/2021/11/load-types-and-definitions-1.png)

## Assign loads

Assign the load definitions to the model: 

*   In the LOADS tab in the ribbon choose _Assign loads_. 
*   Choose the create mode _Surface load_ in the ribbon. 
*   Choose the Load definition named "F01 Office" and assign it to the decks on level 2, 3 and 4 by clicking on the decks.
*   Assign the load definition named "R01 Roof" to the deck on level 5. 

[![](https://optumce.com/wp-content/uploads/2021/11/assign-loads-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/assign-loads.png)

## Horizontal loads

Create horizontal load cases:

*   In the LOADS tab in the ribbon choose _Wind generation_. 
*   Create a new set of in plane horizontal loads by selecting "D (4 - 6) (Level 1 - Level 5)" in the table and pressing _New load for selected wall_. 
*   Rename the new set of loads from "(user defined)" to "Wind+". 
*   Change _Shear forces \[kN\]_ to _20_ for the top level and _40_ for the three others. 

[![](https://optumce.com/wp-content/uploads/2021/11/horizontal-loads.png)](https://optumce.com/wp-content/uploads/2021/11/horizontal-loads.png)

## Lateral wind loads

Lateral loads are assigned to the concrete elements (panels) via the properties.

*   In the LOADS tab in the ribbon choose _Assign loads_. 
*   Select a panel in the wall. In the _Model outline_ on left hand side, _Wall 1_ is highlighted.
*   Expand it and click _Panels_. All panels in _Wall 1_ are now selected. 
*   In the concrete element properties locate _Second order analysis options_ and change _Characteristic lateral load \[kN/m²\]_ in to _\-1.5_. 

A positive value is pressure on the front side of the panel and negative is suction. The blue z-axis in the local coordinate system on the wall points towards the frontside.

*   Ensure that _Lateral load category_ is _V (Wind load)_.

[![](https://optumce.com/wp-content/uploads/2021/11/lateral-loads-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/lateral-loads.png)

Next step is setting up a load combination and making a calculation.

Read more about [loads in the documentation](/optum-cs/loads/).