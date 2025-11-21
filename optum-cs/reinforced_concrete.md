# Reinforced Concrete

Reinforced concrete is represented as a fully cracked material in OPTUM CS. The concrete can carry compression and shear, while the reinforcement carries tension. The reinforcement can also function as confinement in the case of shear. Some of the main results of the finite element analysis are the concrete and reinforcement stresses.

For the elastoplastic case, the concrete and reinforcement have different stiffness. Therefore, the stiffness of the concrete will be governing when in compression, while the stiffness of the reinforcement will be governing when in tension. The stiffness of the reinforcement is usually much lower than the concrete stiffness.

The concrete itself is defined by a compressive strength and a tensile strength, which is usually taken as zero. The design compressive strength depends on a so-called effectiveness factor, which is a single number below 1 multiplied onto the characteristic strength. The effectiveness factor depends on several things, e.g. cracks in the concrete and the actual stress-strain curve of the material. Per default, a value of 0.5 for the effectiveness factor is defined, but it can be changed if needed.

OPTUM CS has two types of reinforcement. The first type is smeared reinforcement, which is used to represent the rebar mesh of panels and stirrups in beams and columns. The advantage of smeared reinforcement is that it is not necessary to model each individual bar. Instead, the smeared reinforcement can be considered as an equivalent layer of steel instead of individual bars.

The second type  is discrete reinforcement. This type is used to represent the rebars in beams and columns as well as stringer reinforcement. Discrete reinforcement is generally used when there are few destinct bars, e.g. in a beam.

The bond between the reinforcement and the concrete is important to include in the calculations. For both types of reinforcement, the anchorage properties describe the minimum distance from a free end until the rebar can sustain the maximum (yield) stress. For the smeared reinforcement, this is included by decreasing the strength of the reinforcement near free edges, e.g. holes and the edges of the panel. The strength is decreased linearly. A anchorage distance of e.g. 200 mm means that the mesh reinforcement cannot be fully utilized in a zone of 200 mm near any edge, and at a distance of 100 mm from an edge only 50 % of the strength will be available.

The discrete rebars are slightly different as they are represented using a bar element in the finite element calculation. The anchorage properties works by simply limiting the amout of force that can be tranferred between the concrete material and the discrete rebar. 

## Concrete and steel stresses

OPTUM CS uses local coordinate systems for each grid with the local $x$ along the grid and the local $y$ pointing upwards. The sign convention in OPTUM CS follows what is used in most literature with positive stresses being tension and negative stresses being compression. The two non-zero principal stresses are ordered as $\sigma_2 \leq \sigma_1$, i.e. $\sigma_2$ being more compressive than $\sigma_1$. The principal strains follow the same principles with $\varepsilon_2 \leq \varepsilon_1$. In plane stress, the two principal stresses are given as

$$
\left.\begin{array}{l} \sigma_1\\ 
\sigma_2\end{array}\right\rbrace = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2} 
$$

The finite element analysis uses three types of stresses: Total stresses, concrete stresses and reinforcement (steel) stresses. The total stresses are the ones used for the equilibrium, while the concrete and steel stresses are given as

$$
\sigma = \sigma\_c + \sigma\_s 
$$

where subscript $c$ denotes concrete stresses and subscript $s$ denotes steel stresses. The reinforcement only carries normal forces, e.g. the concrete must carry all shear stresses.

The use of concrete and steel stresses as separate entities also enable the use of reinforcement as confinement: Even if the total stresses are zero, the reinforcement can be activated and carry tension, while the concrete carry an equal amount of compression.

## Elasticity

OPTUM CS uses a linear-elastic rigid-plastic material model for reinforced concrete. In the elastic domain, the stresses and strains are related to each other directly:

$$
\varepsilon^{e} = \mathbb{C}\sigma \qquad \Leftrightarrow \qquad \sigma = \mathbb{D}\,\varepsilon^{e}
$$

where $\mathbb{C}$ is the compliance modulus and $\mathbb{D} = \mathbb{C}^{-1}$ is the stiffness modulus. The compliance modulus can be expressed in terms of Young's modulus, $E$, and Poisson's ratio, $\nu$, and takes the following form for plane stress:

$$
\mathbb{C} = \frac{1}{E} 
\begin{bmatrix}1 & -\nu & 0 \\  -\nu & 1 & 0 \\0 & 0 & 2\,(1 + \nu) \end{bmatrix}
$$

For cracked concrete, Poisson's ratio is generally assumed to be zero. For the reinforcement an equivalent stiffness is used defined as

$$
\hat{E}_s = E_s \frac{A_s}{t}
$$

where $t$ is the thickness of the panel, $A_s$ is the steel area per unit length, and $E_s$ is the Young's modulus for the reinforcement, usually around 200 GPa.

## Yield criteria

Generally a yield criterion or yield function limits the stresses. It is a function of the stresses and can be stated as

$$
F(\sigma) \leq 0
$$

where $F(\sigma) < 0$ corresponds to an elastic state, while $F(\sigma) = 0$ indicates yielding. In general, various other variables might be input to the yield function, e.g. to account for hardening, but currently in OPTUM CS, only the stresses are used for the yield functions.

Separate yield criteria are enforced for the concrete and reinforcement respectively. For the concrete, the Mohr-Coulomb criterion with a tension cut-off is used. For plane stress, the criterion takes the following form:

$$
\begin{array}{r} 
\sigma_{c1} \leq f_t \\ k\,\sigma_{c1} - \sigma_{c2} \leq f_c \\ - \sigma_{c2} \leq f_c\
\end{array}
$$

where $f_t$ and $f_c$ are the tensile and compressive strength, respectively, and $k$ is a friction parameter. For normal strength concrete, a friction angle of about $\varphi = 37^\circ$ is generally assumed corresponding to a friction coefficient of $\mu = 0.75$. The friction parameter $k$ is defined as

$$
k = \frac{1 + \sin\varphi}{1 - \sin\varphi} = \left(\sqrt{\mu^2 + 1} + \mu\right)^{2}
$$

If the tensile strength is zero, the friction angle does not come into play and the yield criterion is reduced to $\sigma_{c1} \leq f_t$ and $-\sigma_{c2} \leq f_c$.

For the reinforcement, the stress is limited by the yield strength, $f\_y\$. Moveover, for the finite element analysis it is assumed that the reinforcement only carries tension, i.e.

$$
0 \leq \sigma_s \leq f_y
$$

## Effectiveness factor (Strength reduction factor)

The compressive strength of the concrete depends on several factors. First and foremost is the characteristic strength, $f_{ck}$, which the mix is designed to achieve. Next is the design strength, $f_{cd}$, which related directly to the characteristic strength via a partial coefficient, $\gamma_c$:

$$
f_{cd} = \frac{f_{ck}}{\gamma_c}
$$

The effective design strength used in the finite element calculations is reduced further to account for the linear-elastic rigid-plastic approximation to the real stress-strain curve. The effectiveness factor, $\nu$, is split into two factors:

$$
\nu = \eta_{fc} \eta_{\varepsilon}
$$

where $\eta_{fc}$ depends on the characteristic compressive strength

$$
\eta_{fc} = \text{min} \left\lbrace 
\begin{array}{l}\left(\frac{30\text{MPa}}{f_{ck}}\right)^{1/3}\\ 
1 
\end{array} \right. 
$$

while $\eta_\varepsilon$ depends on the largest principal strain, $\varepsilon_1$:

$$
\eta_\varepsilon = \text{min} \left\lbrace 
\begin{array}{l}\frac{1}{1 + 80\\
,\varepsilon_1}\\
1 
\end{array} \right. 
$$

The largest principal strain is a measurement for the degree of cracking, and cracks parallel to the direction of compression lead to a decrease in the compressive strength.

OPTUM CS provides two options regarding the effectiveness factor. Either a fixed effectiveness factor can be specified for each concrete material, or the effectiveness factor is calculated as part of the finite element analysis in an iterative manner. The latter increase the complexity and running time of the analysis. In both cases, a result field of the residual effective compression strength is calculated and shown. When using a fixed effectiveness factor the residual strength might be negative, i.e. insufficient, due to excessive cracking. The residual strength is calculated as

$$
r_c = \nu \,f_{cd} - |\sigma_{c2}|
$$

A warning is given in the analysis dialog if the residual strength is insufficient. In that case several adjustments can be made to increase the residual strength:

*   Run the load combinations with variable effectiveness factor
*   Increase reinforcement, which limits the cracks
*   Increase concrete strength

## Anchorage

The bond between the reinforcement and the concrete is crucial to the behaviour of reinforced concrete structures. The anchorage of the smeared reinforcement, e.g. mesh reinforcement, is treated by reducing the yield strength near free edges. An anchorage length is given for the mesh reinforcement, which defines the zone near free edges where the strength is reduced. At the very edge, the strength is reduced to zero and a linear variation is then assumed until full strength is reached. In most cases the anchorage length will be in the magnitude of 40 times the diameter of the bars.

The discrete rebars are slightly different to the smeared reinforcement. The equilibrium equations of the rebars prescribe a normal force of zero at a free end, and a limit on the shear between the rebar and the concrete is enforced. This shear limit is derived from the anchorage length given by the user.