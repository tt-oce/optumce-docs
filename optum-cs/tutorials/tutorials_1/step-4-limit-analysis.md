---
label: "Step 4: Limit Analysis"
---

# Limit Analysis

## Load combination

Create a load combination:

*   In the LOADS tab in the ribbon choose _Load combinations_.

In the Load Manager on the right hand side all load combinations are listed. _Wall section: D_ has one load combination "Combination 1".

*   In _Load combination analysis options_ in the Load Manager check that _Analysis_ is set to _Limit Analysis_.

On left hand side, settings for _Combination 1_ are displayed.

*   Check that _Design case_ is set to _6.10a - Permanent load_.
*   Check that Load definition _F01 Office_ and _R01 Roof_ are included as unfavorable.
*   Press Run analysis (F5).

[![](https://optumce.com/wp-content/uploads/2021/11/load-combinations-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/load-combinations.png)

*   When the analysis is done, close the Analysis Progress window. The RESULTS tab is now active.

[![](https://optumce.com/wp-content/uploads/2021/11/analysis-progress-300x236.png)](https://optumce.com/wp-content/uploads/2021/11/analysis-progress.png)

## Limit analysis result

In this example the calculation results in a load multiplier of 2.27. For design case 6.10a, this means that all permanent loads multiplied by a factor of 2.27 will result in structural failure. The displacement plot "_Panel |U|_" that is shown, illustrates the collapse mechanism for this load.

[![](https://optumce.com/wp-content/uploads/2021/11/result-limit-analysis-1024x555.png)](https://optumce.com/wp-content/uploads/2021/11/result-limit-analysis.png)

The weakest place in the structure is easily located in this way. The load multiplier illustrates sufficient bearing capacity. But the stresses are not the real stresses and a code check cannot be made. For this an elastoplastic analysis is needed.

Next step is the elastoplastic calculations.