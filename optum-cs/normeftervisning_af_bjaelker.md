# Normeftervisning af bjælker

## Generelt

## Anvendelsesområde

Beregningsmetoden anvendes til armerede betonbjælker, hvilket inkluderer:

*   Overliggere i væg
*   Vægge der regnes som bjælker (”Calculate beam section forces” sat til ”Yes”)

Det er en forudsætning for beregningerne at der anvendes en betonstyrke på 50 MPa eller under.

## Overligger-detektion

Alle huller i væggene løbes igennem. Kun 400 mm brede huller eller derover betragtes.

Hvis vægfeltet mellem oversiden af et hul og enten oversiden af vægelementet eller undersiden af et tilpas stort\* hul har en højde der er mindre end bjælkelængden (=hulbredden), detekteres en bjælke.

\* Tilpas stort hul: Et hul som måler mere end 150 mm vandret eller lodret, eller mere end 20% af den samlede bjælkelængde eller -højde.

## Bestemmelse af snitkræfter

Snitkræfter:

*   M = Moment (kNm)
*   V = Forskydningskraft (kN)
*   N = Normalkraft (kN)

Snitkræfter bestemmes gennem integration af indre spændinger og altså ikke ud fra ydre laster.

Etagekrydsudstøbning over bjælke (modelleret som væg) inkluderes i bestemmelse af snitkræfter.

Moment regnes om center-aksen, altså $y = (h_{bjælke} + h_{etagekryds}) / 2$ og derfor ikke nødvendigvis om neutralaksen.

## Huller i bjælker

**Tilfælde hvor kapacitet ikke beregnes**

Kapaciteter beregnes ikke hvis et vægelement der regnes som bjælke indeholder et hul som måler mere end 20% af den samlede bjælkelængde eller -højde.

Der gives i rapporten en advarsel om at der er huller i bjælken og at de ikke inkluderes i beregning af kapaciteter, hvis hullerne er mindre end i tilfældene beskrevet herover. Der advares ligeledes om at momentkurven regnes om center-aksen.

**Brand på over- og underside**

Det detekteres om en bjælke påvirkes af brand på over- og underside. Hvis bare en lille del af den pågældende rand er fri, regnes den brandpåvirket. I detektionen betragtes strækninger på randen med tilstødende vægge, huller og etagekryds.

# Nomenklatur

|     |     |
| --- | --- |
| $A_k$ | Areal omsluttet af centerlinjerne i væggene i vridningsberegningen. |
| $A_s$ | Armeringens tværsnitsareal. |
| $A_{sw}$ | Forskydningsarmeringens tværsnitsareal pr. bøjle. |
| $E_{cm}$ | Sekantelasticitetsmodulet. |
| $E_s$ | Armeringens elasticitetsmodul. |
| $F_{td,bund}$ | Krav til forankringskraft ved kombineret forskydning og vridning for hovedjern i bjælkebund. |
| $F_{td,V}$ | Krav til forankringskraft ved ren forskydning. |
| $F_{td,T}$ | Krav til forankringskraft ved ren vridning. |
| $M_{Ed}$ | Det største regningsmæssige moment i bjælken. |
| $M_{Rd}$ | Den regningsmæssige momentkapacitet. |
| $N_c$ | Betontrykresultant. |
| $N_s$ | Armeringstrækresultant. |
| $T_{Ed} | Regningsmæssig vridning. |
| $T_{Rd,max}$ | Den regningsmæssige vridningskapacitet, ved trykbrud i beton. |
| $T_{Rd,s}$ | Den regningsmæssige vridningskapacitet, ved trækbrud i bøjler. |
| $V_{Ed,max}$ | Den numerisk største regningsmæssige forskydningskraft i bjælken. |
| $V_{Ed,s}$ | Den numerisk største regningsmæssige forskydningskraft i bjælken, hvor der ses bort fra forskydningskraften i hver ende af bjælken, samt omkring understøtninger, inden for en afstand af $a_s = \cot\Theta \cdot z$. |
| $V_{Rd,max}$ | Den regningsmæssige forskydningskapacitet, ved trykbrud i beton. |
| $V_{Rd,max}'$ | Den regningsmæssige forskydningskapacitet, ved trykbrud i beton, inkl. reduktion fra vridning. |
| $V_{Rd,s}$ | Den regningsmæssige forskydningskapacitet, ved trækbrud i bøjler. |
| $V_{Rd,s}'$ | Den regningsmæssige forskydningskapacitet, ved trækbrud i bøjler, inkl. reduktion fra vridning. |
| $a_z$ | Tykkelse af skadet randzone, ifm. brand. |
| $b$ | Bjælkebredde. Den effektive bredde anvendes generelt i stedet for $b$: $b = b_{eff}$. |
| $b_{eff}$ | Effektiv bjælkebredde hvor der tages hensyn til dæklag i kold tilstand og indbrændingsdybde i brandtilfældet. |
| $c'$ | Afstand fra bjælkeside til center hovedarmeringsjern. Nederste lag hovedarmeringsjern anvendes her. Største værdi af afstand på for- og bagside anvendes her. |
| $\cot\Theta$ | Trykstangens hældning. 2.5 i brand, ellers 2.0. |
| $d$ | Diameter af armeringsjern. |
| $e$ | Excentricitet fra last. Vægtet ift. linjelasternes resultanter. |
| $f_{cm}$ | Middeltrykstyrken ved 28 døgn. |
| $f_{ywd}$ | Regningsmæssig flydestyrke for armeringsjern. |
| $h$ | Bjælkehøjde. |
| $i$ | Iterationsnummer. |
| $it$ | Antal iterationer. |
| $j$ | Armeringslag-nummer. |
| $k$ | Parameter vedr. elasticitetsmoduler. |
| $n$ | Antal armeringsjern i snit. |
| $s$ | Indbyrdes afstand mellem bøjler/armeringsjern. |
| $t_{ef}$ | Effektiv vægtykkelse til vridningsberegning. |
| $x$ | Nullinjedybde. Ofte lig trykzonehøjde. |
| $y_c'$ | Lodret afstand mellem bjælkemidte og betontrykresultant. |
| $y_s$ | Lodret afstand til center hovedjern fra bunden af bjælken. |
| $y_s'$ | Lodret afstand til center hovedjern fra bjælkemidte. |
| $z$ | Indre momentarm bestemt ud fra beregning af positiv momentkapacitet. |
| $\varepsilon_0$ | Kanttøjning. |
| $\varepsilon_{c1}$ | Tøjning ved højeste betonspænding. |
| $\varepsilon_{cu}$ | Brudtøjning for beton. |
| $\zeta$ | Dimensionsløs parameter vedr. nullinjedybde uden for tværsnit. |
| $\nu_t$ | Effektivitetsfaktor for forskydning gennem vridning. |
| $\nu_v$ | Effektivitetsfaktor for ren forskydning. |
| $\sigma_c$ | Betonspænding. |
| $\sigma_s$ | Armeringsspænding. |

## Momentkapacitet

## Beregning

Både positiv og negativ momentkapacitet bestemmes.

Momentkapacitet bestemmes ud fra bjælketværsnittet i midten af bjælken, altså ved $ X = L/2 $.

Beregningen svarer til metoden beskrevet i _Betonelementbyggeriers statik_ afsnit 2.1.3 og 6.1.1 og anvendt i Betonelement-Foreningens beregningsmodul Bjælkeberegning, hvor momentkapaciteten findes gennem en iterativ beregning, hvor kanttøjningen gennem et antal iterationer forøges lineært op til brudtøjningen.

Der tages ikke højde for krybning og svind i bjælken.

Normalkraften inkluderes i beregning af momentkapaciteten.

**Betonmateriale**

Som angivet i tabel 3.1 i DS/EN 1992-1-1:

$$
\varepsilon_{cu} = 0,0035
$$

$$
\varepsilon_{c1} = 0,0007 \cdot f_{cm}^{0,31}
$$

$$
f_{cm} = f_{ck} + 8 MPa
$$

$$
E_{cm} = 22000 \cdot \left[ \frac{f_{cm}}{10} \right]^{0,3}
$$

med $E_{cd}$ og $f_{cm}$ i $MPa$

$$
E_{cd} = \frac{E_{cm}}{\gamma_c}
$$

Der opereres med en ikke-lineær arbejdslinje som beskrevet i afsnit 3.1.5 (1) i DS/EN 1992-1-1:

$$
\frac{\sigma_c}{f_{cm}} = \frac{k \eta-\eta^2}{1+(k-2)\eta}
$$

hvor

$$
\eta = \varepsilon_c / \varepsilon_{c1}
$$

$\varepsilon_{c1}$ er tøjningen ved højeste spænding

$$
k = 1,05 \cdot E_{cm} \cdot \varepsilon_{c1} / f_{cm}
$$

Dog beregnes $k$ med $f_{ck}$ i stedet for $f_{cm}$:

$$
k = 1,05 \cdot \frac{E_{cm} \cdot \varepsilon_{c1}}{f_{ck}}
$$

**Iterationsprocessen**

1.  Først vælges en værdi for kanttøjningen $\varepsilon_0$.
2.  Herefter bestemmes $x$ ud fra projektionsligningen.
3.  Tværsnittets samlede momentkapacitet $M_{Rd}$ fås af momentligningen om tværsnittets nullinje.
4.  En ny værdi af kanttøjningen vælges og det undersøges om resultatet for $M_{Rd}$ er gunstigere.

1: Kanttøjningen

Kanttøjningen $\varepsilon_0$ bestemmes:

$$
\varepsilon_0 = \frac{i}{it} \varepsilon_{cu}
$$

hvor $i$ angiver iterationsnummeret og $it$ antallet af iterationer. I sidste iteration er kanttøjningen $\varepsilon_{cu}$.

$\zeta$ bestemmes:

Oftest, og i tilfælde hvor normalkraften er 0, er $\zeta = 0$.

$$
\zeta = \left\lbrace  
\begin{array}{ll}  
0 & \textrm{for } x \leq h \\  
\frac{x-h}{x} & \textrm{for } x > h \\  
\end{array} \right. 
$$

2: Trykzonehøjden

Trykzonehøjden, = nullinjedybden $x$, bestemmes:

$$
x = \frac{1}{2 A} \cdot \left( -B + \sqrt{B^2 - 4 A C} \right) 
$$

hvor

$$
A = f_{cd} \cdot b \cdot N_c'
$$

$$
B = N_{Ed} + \sum{b_j}
$$

$$
C = \sum{c_j}
$$

hvor 

$N_{Ed}$ er normalkraften

$$
N_c' = \frac{k}{2} \frac{\varepsilon_0}{\varepsilon_{c1}} \left(  1 - \zeta^2 + \frac{K_A - K_B}{K_B^3} \cdot \left\lbrace K_B^2 \cdot \left( 1 - \zeta^2 \right) + 2 K_B \cdot \left( 1 - \zeta \right) + 2 \ln \frac{1 - K_B}{1 - \zeta \cdot K_B} \right\rbrace \right)
$$

$$
b_j = \left\lbrace   
\begin{array}{ll}  
\varepsilon_0 \cdot A_{s,j} \cdot E_{s,j} & \textrm{hvis } 2 \cdot \sigma_{s,j,(i-1)} - \sigma_{s,j,(i-2)} < f_{yd} \\  
A_{s,j} \cdot f_{yd} & \textrm{hvis } 2 \cdot \sigma_{s,j,(i-1)} - \sigma_{s,j,(i-2)} \geq f_{yd} \\
\end{array}  
\right. 
$$

$$
c_j = \left\lbrace   
\begin{array}{ll}  
\left(h - y_{s,j}\right) \cdot \varepsilon_0 \cdot A_{s,j} \cdot E_{s,j} & \textrm{hvis } 2 \cdot \sigma_{s,j,(i-1)} - \sigma_{s,j,(i-2)} < f_{yd} \\  
0 & \textrm{hvis } 2 \cdot \sigma_{s,j,(i-1)} - \sigma_{s,j,(i-2)} \geq f_{yd} \\  
\end{array}  
\right.
$$

hvor

$$
K_A = \frac{\varepsilon_0}{k \cdot \varepsilon_{c1}}
$$

$$
K_B = \left( 2-k \right) \cdot \frac{\varepsilon_0}{\varepsilon_{c1}}
$$

$A_{s,j}$ og $E_{s,j}$ er areal og E-modul for hvert lag, $j$, af hovedjern i bjælken.

$y_{s,j}$ angiver afstand til center hovedjern fra bunden af bjælken (for positivt moment).

Herefter kan spændinger i hovedjern bestemmes:

$$
\sigma_{s,j,i} = E_{s,j} \cdot \varepsilon_0 \cdot \frac{\left( h-x-y_{s,j} \right)}{x}
$$

hvor 

$$
-f_{yd} \leq \sigma_{s,j,i} \leq f_{yd}
$$

3: Momentkapaciteten

$$
M_{Rd} = y_c' \cdot N_c + \sum y_{s,j}' \cdot N_{s,j}
$$

hvor

$$
y_c' = \frac{h}{2} - (t' - 1) \cdot x
$$

$$
N_c = N' \cdot x \cdot b 
$$

$$
y_{s,j}' = \frac{h}{2} - y_{s,j} 
$$

$$
N_{s,j} = \sigma_{s,j} \cdot A_{s,j} 
$$

hvor

$$
t' = \frac{N_c''}{N_c'} 
$$

$$
N_c'' = \frac{k}{3} \frac{\varepsilon_0}{\varepsilon_{c1}} \left( 1 - \zeta^3 - \frac{K_A - K_B}{2 K_B^4} \cdot \left\lbrace - 2 K_B^3 \cdot \left( 1 - \zeta^3 \right) - 3 K_B^2 \cdot \left( 1 - \zeta^2 \right) - 6 K_B \cdot \left( 1 - \zeta \right) - 6 \ln \frac{1 - K_B}{1 - \zeta \cdot K_B} \right\rbrace \right) 
$$

4: Ny værdi for kanttøjning

Ny værdi for kanttøjning $\varepsilon_0$ og $\zeta$ bestemmes. Se pkt. 1.

## Brand

I brandtilfældet reduceres bjælketværsnittet, betonegenskaber og armeringsegenskaber som beskrevet i [Brand generelt](/brand-generelt/). Afstande måles fra kant bjælke minus skadet randzone \\(a\_z\\). Følgende udtryk beregnes anderledes.

$$
K_A = 2^{\frac{1}{3}} \cdot \frac{\varepsilon_{c1}}{k \cdot \varepsilon_0} 
$$

$$
K_B = 3 \cdot \left( \frac{\varepsilon_{c1}}{\varepsilon_{0}} \right)^{2}
$$

$$
N_c' = \frac{K_B}{K_A} \left[ <br>\frac{1}{6} \left( \ln \frac{1-K_A+K_A^2}{\left( 1 + K_A \right)^2} - \ln \frac{\zeta^2 - K_A \cdot \zeta + K_A^2}{\left( \zeta + K_A \right)^2} \right) + \frac{1}{\sqrt{3}} \left( \arctan \frac{2-K_A}{\sqrt{3} \cdot K_A} - \arctan \frac{2 \zeta-K_A}{\sqrt{3} \cdot K_A} \right)<br>\right]
$$

$$
N_c'' = \frac{K_B}{3} \ln \frac{K_A^3 + 1}{K_A^3 + \zeta^3} 
$$

## Udnyttelse af momentkapacitet

Udnyttelsesgraden bestemmes som $M_{Ed} / M_{Rd}$.

## Forskydningskapacitet

## Beregning

Forskydningskapacitet bestemmes ud fra bjælketværsnittet i midten af bjælken, altså ved $x = L/2$.

Hvis en bjælke ikke indeholder lukkede bøjler, men kun har netarmering lodret, kan den implementerede beregning af forskydningskapacitet ikke anvendes. Derfor returneres en kapacitet på 0, en udnyttelsesgrad på -100% og der vises en advarsel i rapporten.

Hvis bjælken indeholder mere end én gruppe bøjler betragtes den der ligger i midten af bjælken.

**Effektiv bredde**

$b_{eff} = \min (b, b')$

hvor $b' = 2 \cdot (b - 2 \cdot c')$

I beregningerne anvendes den effektive bredde, $b = b_{eff}$.

**Excentricitet fra last**

Excentriciteten, $e$, anvendes i et led i beregningen af forskydningskapaciteten, hvor der tages højde for vridning.

Den resulterende excentricitet beregnes som en vægtet værdi, ift. linjelasternes resultanter.

En samlet kraft $P_{tot}$ bestemmes som forskellen mellem største og mindste forskydningssnitkraft.

Kraften $P_0$ er last fra væg over bjælken, men inkluderer også egenvægt af bjælken selv og forskydningskraft fra vægfelter i hver bjælkeende. $P_0$ virker med vægelementets excentricitet $e_0$ og bestemmes som forskellen mellem $P_{tot}$ og laster fra dæk og linjelaster der virker direkte på bjælken $P_i$:

$$P_0 = P_{tot} - \sum P_i$$

Direkte virkende dæklast $P_i$ har to excentriciteter, $e_{i,max}$ mod vægelementets forside og $e_{i,min}$ mod bagsiden. Derfor undersøges to scenarier. Direkte virkende linjelast $P_i$ virker med excentriciteten $e_i$, som herunder regnes $e_{i,max}= e_{i,min} = e_i$.

$$e_{max} = (P_0 \cdot e_0 + \sum (P_i \cdot e_{i,max})) / P_{tot}$$

$$e_{min} = (P_0 \cdot -e_0 + \sum (P_i \cdot e_{i,min})) / P_{tot}$$

Største numeriske excentricitet $e$ anvendes:

$$e = \max \left( |e_{max} |, | e_{min} | \right)$$

Bemærk: Metoden er forsimplet idet vægtningen foretages ud fra resultanterne fra hver linjelast.

**Forskydningskapacitet**

Dels bestemmes kapacitet ved trykbrud i beton $V_{Rd,max}$ og dels kapacitet af bøjler $V_{Rd,s}$.

Vridning inkluderes i kapacitetsberegningen, som beskrevet i afsnit 6.1.4 i _Betonelementbyggeriers statik_: 

$$
\frac{T_{Ed}}{T\_{Rd}} + \frac{V_{Ed}}{V_{Rd}} \leq 1 \Leftrightarrow  
V_{Ed} \leq \frac{V_{Rd} \cdot T_{Rd}}{V_{Rd} \cdot e + T_{Rd}}
$$

idet $T_{Ed} = V_{Ed} \cdot e$

$V_{Rd,max}$ beregnes med udtrykket i formel (6.9) i DS/EN 1992-1-1:

$$
V_{Rd,max} = \frac{\alpha_{cw} \cdot b \cdot z \cdot \nu\_v \cdot f_{cd}}{\left( \cot\Theta + \frac{1}{\cot\Theta} \right)} 
$$

$\alpha_{cw} = 1$ for ikke-forspændte bjælker ifølge 6.2.3(3) Note 3 i DS/EN 1992-1-1 DK NA.

Effektivitetsfaktor i forskydning ifølge formel (5.103 NA) i DS/EN 1992-1-1 DK NA:

$$
\nu_v = 0,7 - \frac{f_{ck}}{200} 
$$

$V_{Rd,s}$ beregnes med udtrykket i formel (6.8) i DS/EN 1992-1-1:

$$
V_{Rd,s} = frac{A\_{sw}}{2} z f\_{ywd} \cot\Theta 
$$

Vridningskapaciteten beregnes med udtrykket beskrevet i afsnit 6.1.3 i _Betonelementbyggeriers statik_:

$$
T_{Rd} = V_{l,Rd} (b-t_{ef}) = V_{v,Rd} (h-t_{ef}) = \min   
\left\lbrace \begin{array}{l}  
T_{Rd,max} \\  
T_{Rd,s} \\  
\end{array} \right. 
$$

$$
T_{Rd,max} = \frac{ t_{ef} \cdot A_k \cdot \nu_t \cdot f_{cd}}{\left( \frac{1}{\cot\Theta} + \cot\Theta \right)} 
$$

$$
T_{Rd,s} = \frac{A_{sw}}{s} \cdot A_k \cdot f_{ywd} \cdot \cot\Theta 
$$

hvor

$$
t_{ef} = \max   
\left\lbrace \begin{array}{l}  
\frac{A}{u} \\  
2 \cdot c' \\  
\end{array} \right. 
$$

$$
\frac{A}{u} = \frac{b \cdot h}{2 \cdot (b + h)} 
$$

$$
A_k = \left( b-t_{ef} \right) \left( h-t_{ef} \right)
$$

Effektivitetsfaktor i vridning ifølge formel (5.104 NA) i DS/EN 1992-1-1 DK NA:

$$
\nu_t = 0,7 \cdot \left( 0,7 - \frac{f_{ck}}{200} \right) = 0,7 \cdot \nu_v 
$$

For trykbrud i beton er kapaciteten inkl. vridning:

$$
V_{Rd,max}' = \frac{V_{Rd,max} \cdot T_{Rd,max}}{V_{Rd,max} \cdot e + T_{Rd,max}}
$$

For trækkapacitet i bøjler er kapaciteten inkl. vridning:

$$
V_{Rd,s}' = \frac{V_{Rd,s} \cdot T_{Rd,s}}{V_{Rd,s} \cdot e + T_{Rd,s}} 
$$

I beregningerne bruges $\cot\Theta = 2,0$, hvilket er under den øvre grænseværdi på $\cot\Theta = 2,5$ ifølge formel (6.7a NA) i DS/EN 1992-1-1 DK NA.

**Forankring af hovedarmering**

Krav til forankring af hovedarmering ved bjælkeender beregnes ud fra forskydning og vridning, som beskrevet i _Betonelementbyggeriers statik_ afsnit 6.1.5.

For ren forskydning beregnes forankringskraften for hovedjern i bunden af bjælken:

$$
F_{td,V} = 0,5 \cdot V_{Ed} \cdot \cot\Theta 
$$

For ren vridning beregnes forankringskraften for hovedjern i hhv. top og bund af bjælken:

$$
F_{td,T} = 2 \cdot \max (F_{td,v} , F_{td,l}) 
$$

hvor

$$
F_{td,l} = \frac{T_{Ed}}{4 \cdot \left( b - t\_{ef} \right)} \cdot \cot\Theta 
$$

$$
F_{td,v} = \frac{T_{Ed}}{4 \cdot \left( h - t_{ef} \right)} \cdot \cot\Theta 
$$

For kombineret forskydning og vridning bliver forankringskraften:

$$
F_{td,bund} = F_{td,V} + F_{td,T} = 0,5 \cdot \cot\Theta + 2 \cdot \left( \frac{e \cdot V_{Ed}}{4 \cdot \left( \min(h, b) - t_{ef} \right)} \right) \cdot \cot\Theta 
$$

idet

$$
T_{Ed} = e \cdot V_{Ed}
$$

## Brand

I brandtilfældet reduceres bjælketværsnittet, betonstyrken og armeringsstyrken som beskrevet i [Brand generelt](/brand-generelt/). Excentriciteten forøges ved ensidig brandpåvirkning. Ellers anvendes samme formler som beskrevet.

**Reduktion af tværsnit**

$$
\begin{array}{ll}  
b_{eff} = b - a_z                & \textrm{for brand på en side} \\  
b_{eff} = b - 2 \cdot a_z   & \textrm{for brand på begge sider} \\ 
h_{eff} = h - a_z                & \textrm{for brand på enten over- eller underside} \\
h_{eff} = h - 2 \cdot a_z   & \textrm{for brand på både over- og underside} \\
h_{eff} = h                         & \textrm{hvis over- og underside ikke er brandpåvirket} \\  
\end{array}
$$

**Reduktion af flydestyrke**

Bøjlearmeringens flydestyrke reduceres som funktion af temperaturen, som bestemmes som en vægtet gennemsnits-bøjle-temperatur ud fra temperaturen i 10 punkter på bøjlen.

Der bestemmes både en temperatur for nederste halvdel og øverste halvdel. Den højeste af de to temperaturer anvendes.

**Forøgelse af excentricitet**

For ensidig brandpåvirkning forøges excentriciteten, $e$, med:

$0,5 \cdot a_z$ ved brand på forsiden, og

$-0,5 \cdot a_z$ ved brand på bagsiden.

## Udnyttelse af forskydningskapacitet

Udnyttelsesgraden bestemmes, under hensyntagen til vridning.

Dels for trykbrud i beton som $V_{Ed,max} / V_{Rd,max}'$

hvor $V_{Ed,max}$ er den numerisk største regningsmæssige forskydningskraft i bjælken.

Og dels for trækbrud i bøjlerne som $V_{Ed,s} / V_{Rd,s}'$

hvor $V_{Ed,s}$ er den numerisk største regningsmæssige forskydningskraft i bjælken, hvor der ses bort fra forskydningskraften i hver ende af bjælken, samt omkring understøtninger, inden for en afstand af $a_s = \cot\Theta \cdot z$.