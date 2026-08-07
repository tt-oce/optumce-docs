---
hidden: true
---
# 1 Stochastic Analysis – Introductory Example

The following example introduces the possibilities for stochastic analysis available in GX, in this case via the Python interface. The problem considered is a strip footing of width $B$ resting on a deposit of clay with undrained shear strength $s_u$.

---

## 1.1 Variability of material parameters

The undrained shear strength is modeled as a lognormally distributed random variable with mean value $\mu = 80$ kPa and a coefficient of variation $\text{COV} = \sigma/\mu \times 100\% = 30\%$. The probability density function of the lognormal distribution is given by

$$
f(x;\sigma_{\ln},\mu_{\ln}) = \frac{1}{x\sigma_{\ln}\sqrt{2\pi}}\exp\left(-\frac{(\ln x - \mu_{\ln})^2}{2\sigma_{\ln}^2}\right) \tag{1.1}
$$

where

$$
\sigma_{\ln} = \sqrt{\ln(1+\text{COV}^2)}, \quad \mu_{\ln} = \ln\mu - \tfrac{1}{2}\sigma_{\ln}^2 \tag{1.2}
$$

The cumulative distribution function is given by

$$
F(x;\sigma_{\ln},\mu_{\ln}) = \tfrac{1}{2}\,\text{erfc}\left(-\frac{\ln x - \mu_{\ln}}{\sigma_{\ln}\sqrt{2}}\right) \tag{1.3}
$$

![](/static/random-fields/su_dist_pdf.png){#relight}
![](/static/random-fields/su_dist_pdf-inverted.png){#redark}
![](/static/random-fields/su_dist_cdf.png){#relight}
![](/static/random-fields/su_dist_cdf-inverted.png){#redark}
:::custom-caption
Figure 1.1: Lognormal distribution of undrained shear strength ($\mu = 80$ kPa, COV = 30%).
:::

---

## 1.2 Random fields

<!-- TODO: describe correlation lengths and random field generation -->

A typical realization of the random field, extracted directly from the simulation results, is shown in Figure 1.2.

![](/static/random-fields/su_field_run1.png){#relight}
![](/static/random-fields/su_field_run1-inverted.png){#redark}
:::custom-caption
Figure 1.2: Realization of the undrained shear strength random field (run 1, $L_x = 50$ m, $L_y = 10$ m).
:::

---

## 1.3 Deterministic analysis

<!-- TODO: deterministic FS for mean strength (legacy: FS = 1.65) -->

---

## 1.4 Stochastic analysis

A total of 1,000 Monte Carlo simulations are carried out for each footing width. The resulting distributions of the factor of safety are shown in Figure 1.3. The red curves correspond to an infinite correlation length, i.e. a lognormal distribution with mean 1.65 and COV = 30%.

![](/static/random-fields/fs_hist_B05.png){#relight}
![](/static/random-fields/fs_hist_B05-inverted.png){#redark}
![](/static/random-fields/fs_hist_B1.png){#relight}
![](/static/random-fields/fs_hist_B1-inverted.png){#redark}
![](/static/random-fields/fs_hist_B2.png){#relight}
![](/static/random-fields/fs_hist_B2-inverted.png){#redark}
:::custom-caption
Figure 1.3: Probability distributions of factor of safety for $B = 0.5$, 1 and 2 m based on 1,000 runs.
:::

---

## 1.5 Collapse mechanisms

The variability of the $s_u$ distribution modelled by random fields gives rise to a variety of collapse mechanisms. A quick overview of the variability of these can be gauged by plotting the probability distribution function of the mobilized mass. An example, for $B$ = 2 m is shown in Figure 1.4.

![](/static/random-fields/mass_hist_B2.png){#relight}
![](/static/random-fields/mass_hist_B2-inverted.png){#redark}
:::custom-caption
Figure 1.4: Probability distribution of mobilized mass (excluding footing) for $B$ = 2 m.
:::

To rerun particular Monte Carlo instances, the Seed should be set to the run number and the number of Monte Carlo runs should be set to 1.

<!-- TODO: GX snapshots of runs 351, 167 and 42 (legacy Figure 57.10) -->
