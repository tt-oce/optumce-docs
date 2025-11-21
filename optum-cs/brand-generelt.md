# Brand generelt (Fire in general)

I brandtilfældet reduceres tværsnittet, betonegenskaber og armeringsegenskaber som funktion af temperaturen.

## Bestemmelse af temperatur

En standardbrandpåvirkning betragtes, hvorved temperaturen kan bestemmes iht. DS/EN 1992-1-2 DK NA under Anneks A, Temperaturprofiler:  


$$
\Theta_1(x,t) = 312 \cdot \log_{10}(8 \cdot t+1) e^{-1,9 \cdot k(t) \cdot x} \cdot \sin{\frac{\pi}{2} - k(t) \cdot x} 
$$

$$
k(t) = \sqrt{\frac{\pi \cdot \rho \cdot c_p}{750 \cdot \lambda \cdot t}} 
$$

For to-, tre- og firesidet brandpåvirkning kan temperaturen bestemmes ved superposition af temperaturkurverne tilhørende brandpåvirkning fra hver side, som beskrevet i DS/EN 1992-1-2 DK NA under Anneks A, Temperaturprofiler.

## Reduktion af betonegenskaber

Betonens styrke og E-modul reduceres for hele tværsnittet med følgende udtryk: 

$$
f_{cd}(\Theta_M) = k_c(\Theta_M) \cdot f_{cd} 
$$

$$
E_{cd}(\Theta_M) = (k_c(\Theta_M))^2 \cdot E_{cd}
$$

$k_c(\Theta_M)$ er reduktionsfaktor for betonstyrken ved M-punktet.  
$k_c(\Theta)$ bestemmes gennem interpolation ud fra værdierne angivet i figur 1 NA i afsnit 3.2.2.1(1)P i DS/EN 1992-1-2 DK NA, svarende til et kalkholdigt tilslag (søsand/granit):  
[![](https://staging.optumce.com/wp-content/uploads/2023/03/Screenshot-2023-03-03-092202.png)](https://staging.optumce.com/wp-content/uploads/2023/03/Screenshot-2023-03-03-092202.png)

{.compact}
| $\Theta [^\circ C]$ | $k_c(\Theta) [-]$ |
| --- | --- |
| 20  | 1,0 |
| 200 | 1,0 |
| 500 | 0,8 |
| 900 | 0   |

## Reduktion af betontværsnit

Tykkelsen af den skadede randzone $a_z$ bestemmes ud fra formel (B.12) i afsnit B.2(7) i DS/EN 1992-1-2:

$$
a_z = w \left[ 1 - \frac{k_{c,m}}{k_c(\Theta_M)} \right]  
$$

hvor  

$$
[ w = 0,5 \cdot b ]  
$$

$k_{c,m}$ er middelreduktionskoefficienten som bestemmes ud fra formel (B.11) i afsnit B.2(6) i DS/EN 1992-1-2:  

$$
k_{c,m} = \frac{(1-0,2/n)}{n} \sum_{i=1}^{n}{k_c(\Theta_i)}
$$

$k_c(\Theta_i)$ er reduktionsfaktor for betonstyrken ved punkter i tværsnittets zoner.  
I beregningen er antallet af zoner sat til $n = 10$.

## Reduktion af armeringsegenskaber

Armeringens flydestyrke og E-modul reduceres som funktion af temperaturen.  
Styrkereduktionen afhænger af temperaturen og armeringstypen og bestemmes gennem interpolation ud fra værdierne angivet i tabel 1 NA og tabel 2 NA i afsnit 3.2.3(5) i DS/EN 1992-1-2 DK NA , bortset fra E-modul for varmvalset og kolddeformeret stål som fremgår af tabel 3.2a i afsnit 3.2.3 i DS/EN 1992-1-2.

**Varmvalset**

{.compact}
| $\Theta [^\circ C]$ | $f_{sy}(\Theta)/f_{yk} [-]$ | $E_s(\Theta)/E_s [-]$ |
| --- | --- | --- |
| 20  | 1,00 | 1,00 |
| 100 | 0,96 | 1,00 |
| 200 | 0,88 | 0,90 |
| 300 | 0,77 | 0,80 |
| 400 | 0,65 | 0,70 |
| 500 | 0,47 | 0,60 |
| 600 | 0,27 | 0,31 |
| 700 | 0,13 | 0,13 |
| 800 | 0,05 | 0,09 |
| 900 | 0,02 | 0,07 |
| 1000 | 0,01 | 0,04 |
| 1100 | 0,00 | 0,02 |
| 1200 | 0,00 | 0,00 |

**Kolddeformeret**

{.compact}
| $\Theta [^\circ C]$ | $f_{sy}(\Theta)/f_{yk} [-]$ | $E_s(\Theta)/E_s [-]$ |
| --- | --- | --- |
| 20  | 1,00 | 1,00 |
| 100 | 0,99 | 1,00 |
| 200 | 0,95 | 0,87 |
| 300 | 0,89 | 0,72 |
| 400 | 0,78 | 0,56 |
| 500 | 0,57 | 0,40 |
| 600 | 0,30 | 0,24 |
| 700 | 0,12 | 0,08 |
| 800 | 0,05 | 0,06 |
| 900 | 0,02 | 0,05 |
| 1000 | 0,01 | 0,03 |
| 1100 | 0,00 | 0,02 |
| 1200 | 0,00 | 0,00 |

**Bratkølet**

{.compact}
| $\Theta [^\circ C]$ | $f_{sy}(\Theta)/f_{yk} [-]$ | $E_s(\Theta)/E_s [-]$ |
| --- | --- | --- |
| 20  | 1,00 | 1,00 |
| 100 | 0,98 | 1,00 |
| 200 | 0,94 | 1,00 |
| 300 | 0,89 | 0,99 |
| 400 | 0,78 | 0,96 |
| 500 | 0,55 | 0,79 |
| 600 | 0,27 | 0,48 |
| 700 | 0,10 | 0,21 |
| 800 | 0,00 | 0,08 |
| 900 | 0,00 | 0,03 |
| 1000 | 0,00 | 0,00 |
| 1100 | 0,00 | 0,00 |
| 1200 | 0,00 | 0,00 |