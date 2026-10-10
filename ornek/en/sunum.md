---
dil: en
baslik: Genetic algorithm for helicopter rotor conceptual design: problem and method plan
hazirlayan: Name SURNAME
program: Defence Technologies Master's Programme
kurum: ITU Aviation Institute
danisman: Assoc. Prof. Dr. Ayşe Kaya
tarih: 02.12.2026
eposta: name.surname@itu.edu.tr
sayfa_no: evet
yz_satiri: Form and slides were edited with the assistance of Claude (Anthropic); content and responsibility belong to the presenter.
---

## [icindekiler] Contents
- Introduction · 4 min
- Literature review · 8 min
- Research method · 14 min
- Next steps · 4 min

## [metin] 3 · Introduction: why rotor sizing is hard
mesaj: Five conceptual rotor variables are coupled; changing one restarts the whole calculation.
- The main rotor produces lift and sets the performance of the helicopter
- Five variables at the conceptual stage: radius, chord, blade number, tip speed, twist
- Current practice is experience-based and iterative [2], [3]
> Explain with an example how radius affects hover power, mass and the tip-speed limit.

## [tablo] 5 · Method: design variables
mesaj: Five variables, ranges from the literature.
Gene | Variable | Range | Source
R | Radius | 5.5–7.0 m | [3]
c | Chord | 0.25–0.45 m | [3]
N | Blades | 2–5 | [2]
Vt | Tip speed | 190–230 m/s | [2]
Ranges will be re-checked against the Lynx reference [4].

## [surec] 5 · Method: BEMT–GA workflow
mesaj: Each individual is evaluated by the hover model; the GA loop runs until convergence.
### Step 1 · Encode
- Five variables as a real-coded chromosome
### Step 2 · Evaluate
- BEMT hover model: power and mass
### Step 3 · Select and vary
- Tournament selection, crossover, mutation
> Transition: the workflow is set; now the constraints.

## [tesekkur] Acknowledgements
I thank my advisor Assoc. Prof. Dr. Ayşe Kaya for her guidance and my colleagues at my workplace for discussions on rotor sizing practice.

## [kaynaklar] References
[1] S. Katoch, S. S. Chauhan, and V. Kumar, "A review on genetic algorithm: past, present, and future," Multimedia Tools and Applications, vol. 80, no. 5, pp. 8091–8126, 2021, doi: 10.1007/s11042-020-10139-6.
[2] J. G. Leishman, Principles of Helicopter Aerodynamics, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2006.
[3] W. Johnson, Rotorcraft Aeromechanics. Cambridge, U.K.: Cambridge Univ. Press, 2013, doi: 10.1017/CBO9781139235655.
[4] D. Novak, T. Bucak, and A. Domitrović, "Helicopter main rotor conceptual design: application to a Westland Lynx helicopter," Promet – Traffic & Transportation, 2008.
