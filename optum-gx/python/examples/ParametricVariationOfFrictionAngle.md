# Parametric variation of friction angle.
In this example we investigate the stability of an excavation with varying friction angle of a uniform soil layer. 

![**`Figure 1.1`** Geometry of Excavation.](../../static/example-figures/Example_parametric_phi/model.png)

![**`Figure 1.2`** Factor of Safety for 30 degree friction angle.](../../static/example-figures/Example_parametric_phi/Collapse_Phi_30.png)

The script outputs the following table (in plain text): 
| Friction angle (deg), | Displacement (mm), | Factor of safety |
|-----------------------|--------------------|------------------|
| 30.00                 | 290.36             | 1.18             |
| 35.00                 | 183.90             | 1.43             |
| 40.00                 | 132.54             | 1.72             |
| 45.00                 | 104.65             | 2.05             |

Screenshots of the Factor of Safety results from GX are saved to the directory the script is running from. More options for detailed result plots are available with the function [take_picture()](../functions/model-and-stage/operations/take_picture/), which is used in the [Unconfined seepage](./Example8_Slope_Seepage.md) example.

:::code source="../../static/code-files/ParametricVariationOfFrictionAngle.py" :::