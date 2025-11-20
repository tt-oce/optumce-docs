# 4 Mohr-Coulomb

The Mohr-Coulomb is the most basic model capable of reproducing the key
features of soils. While more complex models in principle offer the
possibility of matching real soil behaviour better, the simplicity of
the MC model makes it an attractive alternative, provided that the
material parameters are chosen appropriately.

## 4.1 Summary of material parameters

The key material parameters are summarized below. More specialized
parameters are elaborated on in later sections.

### Stiffness {#stiffness .unnumbered}

- $E$: Young's modulus

- $\nu$: Poisson's ratio

### Strength {#strength .unnumbered}

- $c'$: cohesion

- $\phi'$: friction angle

## 4.2 Governing equations

### 4.2.1 Elasticity

Isotropic elasticity defined by $E$ and $\nu$ is used (see [Elasticity](/materials/2-elasticity)).

### 4.2.2 Failure surface

The Mohr-Coulomb failure surface is given by

$$
F = |\sigma_1-\sigma_3|+(\sigma_1'+\sigma_3')\sin\phi' - 2c'\cos\phi' \tag{4.1}
$$

where $c'$ and $\phi'$ are the cohesion and friction angle
respectively.\
Some possible depictions of the MC failure surface are shown in [Figure 5.1](/materials/5-tresca).

### 4.2.3 Flow rule

The flow potential is given by

$$
G = |\sigma_1-\sigma_3|+(\sigma_1'+\sigma_3')\sin\psi \tag{4.2}
$$

where $\psi$ is the dilation angle.

![](/static/mcy02.png){#relight}
![](/static/mcy02-inverted.png){#redark}
:::custom-caption
Figure 4.1: Possible depictions of Mohr-Coulomb yield surface in principal stress space. In (a) and (b), the principal stress ordering is
$\sigma_1\leq\sigma_2\leq\sigma_3$ while no particular ordering is
assumed in (c).
:::

In GX, the basic choice of flow rule is between Associated and
Nonassociated. In the former case, $\psi=\phi$. In the latter case,
$\psi$ is specified along with a possible cap on the dilation. That is,
it is possible to define a critical strain above which $\psi$ is set to
zero. For Dilation Cap = Yes, the critical strain may be specified
either in terms of a volumetric strain, $\varepsilon_{v,cr}$, or a
deviatoric strain $\varepsilon_{q,cr}$ (see [Notation](/materials/1-notation) for exact definition of these strains).

![](/static/mc_softning.png){#relight}
![](/static/mc_softning-inverted.png){#redark}
:::custom-caption
Figure 4.2: Softening Mohr-Coulomb material in triaxial
compression.
:::

### 4.2.4 Softening

Softening is activated by first choosing Softening = Yes. Three
parameters then define the properties of then softening stress-strain
curve: the residual friction angle, $\phi_\mathsf{residual}$, and two
characteristic deviatoric strains, $\varepsilon_{q,cr,1}$ and
$\varepsilon_{q,cr,2}$. These are sketched in Figure 4.2 with
respect to a triaxial compression test. The ultimate residual strength
is:

$$
q_{u,\mathsf{residual}} =|\sigma_1-\sigma_3|_{u,\mathsf{residual}} = \frac{2c'\sin\phi_{\mathsf{residual}}'}{1-\sin\phi_{\mathsf{residual}}'}(-\sigma_3'+c'/\tan\phi_{\mathsf{residual}}') \tag{4.3}
$$

where it is noted that only the friction angle and not the cohesion is
affected by the softening.

![](/static/mc_stress_strain.png){#relight}
![](/static/mc_stress_strain-inverted.png){#redark}
:::custom-caption
Figure 4.3: Response of Mohr-Coulomb in triaxial compression without and with a Volumetric Dilation Cap.
:::

## 4.3 Model response

The response of the MC material in triaxial compression is shown in
Figure 4.3. The ultimate deviatoric stress is given by

$$
q_u =|\sigma_1-\sigma_3|_u = \frac{2c'\sin\phi'}{1-\sin\phi}(-\sigma_3'+c/\tan\phi') \tag{4.4}
$$

