---
label: "Step 5: Elastoplastic Analysis"
---

# Step 5: Elastoplastic Analysis

## Load combination

Edit load combination:

*   In the LOADS tab in the ribbon choose _Load comb__inations_.
*   In _Load combination analysis options_ in the Load Manager change _Analysis_ to _Elastoplastic Analysis_ for Combination 1.

Add a new load combination for the wall section:

*   In the load manager, add another load combination by pressing the _Add a new load combination_ button.
*   Double click the name of the new load combination to rename it. Name it "LC2 6.10b Wind+".
*   In _Load combination analysis options_ change _Analysis_ to _Elastoplastic Analysis_.
*   In the settings for the load combination on left hand side, change Design case to 6.10b - Variable load.
*   Also change _Variable load type_ to _Wind load_ and _Self-weight of walls_ to _Unfavorable_.
*   In _Load definitions_ include the two load definitions as Unfavorable.
*   In _Horizontal loads_ include the user-defined load _Wind+_.
*   Press Run analysis (F5).

[![](https://optumce.com/wp-content/uploads/2021/11/load-combinations-EP-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/load-combinations-EP.png)

*   When the analysis is done, close the Analysis Progress window. The RESULTS tab is now active.

## Elastoplastic analysis result

The elastoplastic analysis results in different types of results; Direct results from the finite element analysis and post processed code check results. Also the input parameters for the calculation can be illustrated.

## Finite element results

### Displacements

*   Select _Combination 1_ in the load manager.

In the RESULTS tab, the displacement plot "_Panel |U|"_ is displayed. This is the actual in-plane displacement. Elastoplastic behaviour of the concrete and reinforcement is taken into account in this calculation, making the result very accurate, compared to a linear elastic calculation.

*   Add a check mark in the _Show displacement_ box in the ribbon, and adjust the scaling using the mouse wheel while the cursor is on the scale input field, to show the wall section in deformed shape.
*   Select the other load combination in the load manager and check if the displacement corresponds to the direction of the applied horizontal loads.

[![](https://optumce.com/wp-content/uploads/2021/11/displacement-plot-1-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/displacement-plot-1.png)

### Stresses

In _Stresses_ in the _Panel_ section in the ribbon, select "_Panel σc2_", the minimum of the principal stresses in the concrete (the (absolute) highest compression stresses in the concrete). The biggest compression is in this case 10.7 MPa, as displayed in the colour bar in the scale section in the ribbon, which is the maximum allowable compression stress in the elastoplastic finite element calculation:

σ = ν · fck / γc = 0.5 · 30 MPa / 1.40 = 10.7 MPa

[![](https://optumce.com/wp-content/uploads/2021/12/sigma-c2-1024x555.png)](https://optumce.com/wp-content/uploads/2021/12/sigma-c2.png)

*   Drag the left limit in the Scale bar in the ribbon to the center or even higher, to intensify the compression struts/paths in the wall section.

[![](https://optumce.com/wp-content/uploads/2021/12/sigma-c2-limit-1024x922.png)](https://optumce.com/wp-content/uploads/2021/12/sigma-c2-limit.png) 

Explore many other results of the finite element calculation in the Panel, Rebar, Joints and Reactions sections in the ribbon. The input parameters for the calculation is grouped in the Model section in the ribbon. This is a great tool for visual control of the model inputs.

## Code check results

Code check includes calculations of walls and beams. The results are made in the post processing, after the FE calculations, in compliance with EN 1992 (EC2), and with similarities to the analyses used in the calculation software provided by the danish concrete element association, Betonelement-Foreningen. The panels in the wall section are divided into slices, and for each of these a second order analysis is performed, checking the stability and the out of plane displacement. Also the wall beams are recognized and analysed. In the RESULTS tab, the results are presented visually. More details, including the NM-curves, tables and summarizing plots are available in the report, which is explained in the next step of the tutorial.

### Wall slice utilization

The utilization of the wall slices are visualized for each load combination in the "_Code Check M0Ed/M0Rd_" plot in the _Wall column_ menu in the _Code check_ section in the ribbon. 

[![](https://optumce.com/wp-content/uploads/2021/12/wall-slice-utilization-1024x555.png)](https://optumce.com/wp-content/uploads/2021/12/wall-slice-utilization.png) 

Explore more results in the _Code check_ menu and calculated input parameters in the _Geometry_ menu.

### Beam moment

The internal moment for the beams are visualized for each load combination in the "_Beams M_" plot in the _Section forces_ menu in the _Beams_ section in the ribbon. Also the other section force plots are available in this menu. The horizontal joint is included in the calculation of section forces. 

[![](https://optumce.com/wp-content/uploads/2021/12/beam-moment-1024x793.png)](https://optumce.com/wp-content/uploads/2021/12/beam-moment.png)

The positive and negative moment bearing capacity plots, _MRd+_ and _MRd-_ are available in the _Section forces_ menu, displaying the capacities calculated at mid beam, with no normal force, and without including the horizontal joint. 

[![](https://optumce.com/wp-content/uploads/2021/12/beam-positive-moment-capacity-1024x816.png)](https://optumce.com/wp-content/uploads/2021/12/beam-positive-moment-capacity.png) 

Next step is generating a report.