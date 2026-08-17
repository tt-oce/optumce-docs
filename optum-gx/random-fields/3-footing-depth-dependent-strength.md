# 3 Stochastic Analysis of Footing in Clay with Depth Dependent Strength

The following example involves the determination of the bearing capacity of a footing in a random field soil (see Figure 3.1). Undrained conditions are assumed and the Tresca model is used to model the soil. In contrast to the previous examples, the mean value of the undrained shear strength is not a constant but increases linearly with depth, from 10 kPa at the ground surface at a rate of 3 kPa/m. An example of a random strength field using these parameters is shown in Figure 3.3. We see that while there are significant strength fluctuations, especially vertically, the overall trend is a linear increase of strength with depth.

![](/static/random-fields/footing-model.png)
:::custom-caption
Figure 3.1: Footing in clay with strength increasing linearly with depth.
:::

A standard deterministic analysis is first conducted, leading to a bearing capacity of

$$
q_u = 124.5 \; \text{kN/m}^2 \tag{3.1}
$$

The associated collapse mechanism shown in Figure 3.2 is entirely dominated by vertical downwards movement, i.e. rotation is negligible.

![](/static/random-fields/footing-det-mechanism.png)
:::custom-caption
Figure 3.2: Collapse mechanism from deterministic analysis.
:::

![](/static/random-fields/footing-rf-profiles.png)
:::custom-caption
Figure 3.3: Random field with mean value of strength increasing linearly with depth. The profiles are taken at $x = -4$, $0$ and $4$ m of run 1.
:::

Next, a stochastic analysis is performed using 1,000 Monte Carlo runs. The resulting statistics are shown in Figure 3.4. We see that the mean value of the bearing capacity is similar to that of the deterministic analysis while the coefficient of variation (18.5%) is somewhat smaller than that of the material (30%), echoing the findings of the previous examples.

![](/static/random-fields/footing-qu-hist.png)
:::custom-caption
Figure 3.4: Probability distribution of bearing capacity.
:::

Finally, three examples of collapse mechanisms are shown in Figure 3.5. These all involve a significant rotation of the foundation, in contrast to the mechanism of the deterministic analysis.

![](/static/random-fields/footing-mech-run886.png)
![](/static/random-fields/footing-mech-run444.png)
![](/static/random-fields/footing-mech-run298.png)
:::custom-caption
Figure 3.5: Collapse mechanisms from stochastic analysis. From top to bottom: (a) run no 886, $q_u$ = 65.7 kN/m²; (b) run no 444, $q_u$ = 118.9 kN/m²; (c) run no 298, $q_u$ = 211.0 kN/m².
:::

Unlike the previous two examples, the mobilized mass is a poor discriminator here: it is 13.0, 11.4 and 13.0 m³/m for the three runs above even though their bearing capacities differ by more than a factor of three. The reason is the strength gradient, which pins the depth of the mechanism regardless of the particular realization, so it is the magnitude of $s_u$ within an almost-fixed volume that varies rather than the volume itself. The runs are therefore identified by bearing capacity.

## Code

:::code source="../../static/random-fields/code-files/Stochastic footing in clay.py" :::
