# 1 Notation

In this section, a number of frequently used quantities are defined.

---

## 1.1 Stress

The stress vector $\boldsymbol{\sigma}$ is given by:

$$
\begin{array}{lcl}
\boldsymbol{\sigma} = (\sigma_x,\sigma_y,\sigma_z,\tau_{xy},\tau_{yz},\tau_{zx})^{\textsf{{\tiny T}}} & & \textsf{(3D)}\\
\boldsymbol{\sigma} = (\sigma_x,\sigma_y,\sigma_z,\tau_{xy})^{\textsf{{\tiny T}}} & & \textsf{(plane strain)}\\
\boldsymbol{\sigma} = (\sigma_x,\sigma_y,\sigma_\theta,\tau_{xy})^{\textsf{{\tiny T}}} & & \textsf{(axisymmetry)}
\end{array} \tag{1.1}
$$

The conventional sign convention of continuum mechanics (compression taken as negative) is used throughout. The principal stresses are ordered as:

$$
\sigma_1\leq \sigma_2 \leq\sigma_3 \tag{1.2}
$$

For problems dominated by compression, $\sigma_1$ will usually be the numerically largest principal stress.\
The mean stress, noting the sign convention, is given by:

$$
p = -\tfrac{1}{3}(\sigma_x+\sigma_y+\sigma_z) = -\tfrac{1}{3}(\sigma_1+\sigma_2+\sigma_3) \tag{1.3}
$$

A related quantity, the modified mean stress, is defined as:

$$
\tilde p = p + c/\tan\phi \tag{1.4}
$$

where $c$ and $\phi$ are the Mohr-Coulomb cohesion and friction angle respectively.\
The deviatoric stress is given by

$$
q= \sqrt{\tfrac{1}{2}(\sigma_x-\sigma_y)^2+\tfrac{1}{2}(\sigma_y-\sigma_z)^2+\tfrac{1}{2}(\sigma_z-\sigma_x)^2+3\tau_{xy}^2+3\tau_{yz}^2+3\tau_{zx}^2} \tag{1.5}
$$

Under triaxial conditions, $\sigma_z=\sigma_1$, $\sigma_x=\sigma_y=\sigma_3$, $\tau_{xy}=\tau_{yz}=\tau_{zx}=0$, the mean and deviatoric stresses reduce to:

$$
p=-\tfrac{1}{3}(\sigma_1+2\sigma_3),\quad q= |\sigma_1-\sigma_3| \tag{1.6}
$$

The Lode angle is given by

$$
\theta = \arctan\left[\frac{1}{\sqrt 3}\left(\frac{\sigma_2-\sigma_3}{\sigma_1-\sigma_3}-1\right)\right] \tag{1.7}
$$

This angle varies between $-30^\circ$ corresponding to triaxial compression and $+30^\circ$ corresponding to triaxial extension.

---

## 1.2 Effective stress

The effective stress is given by

$$
\boldsymbol{\sigma}' = \boldsymbol{\sigma}+\boldsymbol{m}p_w \tag{1.8}
$$

where $m=(1,1,1,0,0,0)^{\textsf{{\tiny T}}}$ and $p_w$ is the fluid pressure. This is made up of a seepage pressure and possibly an excess pore pressure:

$$
p_w = p_s + p_e \tag{1.9}
$$

where $p_s$ is the seepage pressure (steady-state or transient) and $p_e$ is the excess pore pressure generated in response to deformation for the relevant analysis types and Drainage settings. It is noted that while stresses follow the standard continuum mechanics sign conventions (negative in compression), the opposite convention is used for fluid pressures.

---

## 1.3 Strain

The strain vector $\boldsymbol{\varepsilon}$ is given by:

$$
\begin{array}{lcl}
\boldsymbol{\varepsilon} = (\varepsilon_x,\varepsilon_y,\varepsilon_z,\tau_{xy},\tau_{yz},\tau_{zx})^{\textsf{{\tiny T}}}& & \textsf{(3D)}\\
\boldsymbol{\varepsilon} = (\varepsilon_x,\varepsilon_y,\varepsilon_z,\tau_{xy})^{\textsf{{\tiny T}}}& & \textsf{(plane strain)}\\
\boldsymbol{\varepsilon} = (\varepsilon_x,\varepsilon_y,\varepsilon_\theta,\tau_{xy})^{\textsf{{\tiny T}}}& & \textsf{(axisymmetry)}
\end{array} \tag{1.10}
$$

The conventional continuum mechanics sign convention (strains negative in contraction) is used throughout. The principal stresses are ordered as:

$$
\varepsilon_1\leq \varepsilon_2 \leq\varepsilon_3 \tag{1.11}
$$

For problems dominated by compression, $\varepsilon_1$ will usually be the numerically largest principal strain.

The volumetric strain is given by

$$
\varepsilon_v = \varepsilon_x+\varepsilon_y+\varepsilon_z = \varepsilon_1+\varepsilon_2+\varepsilon_3  \tag{1.12}
$$

The deviatoric strain is given by

$$
\varepsilon_q=\tfrac{2}{3}\sqrt{\tfrac{1}{2}(\varepsilon_x-\varepsilon_y)^2+\tfrac{1}{2}(\varepsilon_y-\varepsilon_z)^2+\tfrac{1}{2}(\varepsilon_z-\varepsilon_x)^2+\tfrac{3}{4}\gamma_{xy}^2+\tfrac{3}{4}\gamma_{yz}^2+\tfrac{3}{4}\gamma_{zx}^2}  \tag{1.13}
$$

A related quantity, often referred to as just the shear strain, is given by

$$
\gamma=\tfrac{3}{2}\varepsilon_q \tag{1.14}
$$

Under triaxial conditions, $\varepsilon_z=\varepsilon_1$, $\varepsilon_x=\varepsilon_y=\varepsilon_3$, $\tau_{xy}=\tau_{yz}=\tau_{zx}=0$, the volumetric and deviatoric strains reduce to:


$$
\varepsilon_v = \varepsilon_1+2\varepsilon_3, \quad \varepsilon_q = \tfrac{2}{3}|\varepsilon_1 - \varepsilon_3| \tag{1.15}
$$

---

### 1.3.1 Strain types

A basic premise of classic plasticity theory is the additive decomposition of the total strain into elastic and inelastic components. In GX, two types of inelastic strain are relevant: plastic strains and creep strains. The total strain is thus:

$$
\boldsymbol{\varepsilon} = \boldsymbol{\varepsilon}^{e} + \boldsymbol{\varepsilon}^{p} + \boldsymbol{\varepsilon}^{c} \tag{1.16}

$$

where

$$
\begin{array}{lcl}
\boldsymbol{\varepsilon}^{e} & = & \textsf{elastic strains}\\
\boldsymbol{\varepsilon}^{p} & = & \textsf{plastic strains}\\
\boldsymbol{\varepsilon}^{c} & = & \textsf{creep strains}
\end{array} \tag{1.17}
$$

