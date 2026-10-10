# Genetic algorithm for helicopter rotor conceptual design: problem definition and method plan

## Author
Name SURNAME
Defence Technologies Master's Programme
ITU Aviation Institute
Istanbul, Türkiye
name.surname@itu.edu.tr

## Abstract
Conceptual design of a helicopter main rotor is a process in which many coupled variables are mostly set by experience and iteration; when one variable changes, the whole calculation is repeated. The thesis combines a hover performance model based on blade element momentum theory (BEMT) with a genetic algorithm to develop a method that optimises five conceptual design variables (rotor radius, chord, number of blades, tip speed and twist) for hover power and rotor mass under a given mission requirement. To date, the literature has been reviewed, the design space of the five variables has been set from published ranges, and a hover performance model has been written; the model will be validated against the Westland Lynx rotor. The seminar covers the problem definition, a collective summary of genetic algorithm use in engineering design, and the detailed method plan: the BEMT–GA workflow, chromosome encoding, candidate objective functions, constraints, algorithm settings and the validation strategy. No numerical results are presented; the closing slide states the next steps and the timeline to the thesis defence. The expected contribution is a systematic conceptual sizing tool that shortens the design loop and explores regions of the design space not reached by manual iteration.

## Keywords
genetic algorithm, rotor conceptual design, blade element momentum theory, hover performance, helicopter, design optimisation

## Thesis Status
The thesis is titled "Helicopter Rotor Conceptual Design with Genetic Algorithm Optimisation" and is supervised by Assoc. Prof. Dr. Ayşe Kaya [fictional]. The thesis proposal was submitted in May 2026. The study aims to develop a sizing method for the conceptual design of a helicopter main rotor supported by a genetic algorithm [1]. So far the literature has been surveyed; the five design variables and their ranges (radius 5.5–7.0 m, chord 0.25–0.45 m, two to five blades, tip speed 190–230 m/s, linear twist −6 to −14 degrees) have been set from published rotorcraft data [2], [3]; and a hover performance model based on blade element momentum theory has been written in Python. The model has been run once for a trial case; the single value obtained has not yet been checked and is therefore not reported.

In the coming semester the plan is, in order, to connect the genetic algorithm to the model through an existing library (DEAP or pymoo), to validate the model against the Westland Lynx rotor data, and, if time allows, to add a forward-flight model. The author works in rotary-wing design at a defence industry company; for confidentiality reasons no company data are used, only data from the open literature. No human participants or personal data are involved, so no ethics committee approval is required.

## Relation of the Thesis to Defence Technologies
Türkiye runs indigenous rotary-wing platform programmes such as Gökbey. In these programmes the main rotor is the subsystem that produces lift and determines performance; at the conceptual stage, rotor sizing today relies largely on experience and manually driven iteration. Because a change in one variable requires every other calculation to be repeated, conceptual design takes time and only a small part of the design space is examined. The dependence on experienced designers also makes the result sensitive to who performs the sizing.

The tool developed in the thesis will start from the mission requirement (maximum weight and the resulting thrust demand), scan the rotor conceptual variables systematically and generate candidate designs according to a chosen objective function. The expected benefit is a shorter conceptual design loop and the evaluation of design-space regions that manual iteration cannot reach; the size of this gain has not yet been measured and will be assessed in the thesis by comparison with the Lynx reference design. The method is platform independent and can be reused for unmanned rotorcraft of different weight classes.

## Seminar Topic
The seminar first defines the problem: which variables are involved in the conceptual design of a helicopter main rotor, how these variables depend on each other and how the classical conceptual sizing approach proceeds [2], [3]. Leishman [2] gives the BEMT formulation and the typical ranges of rotor parameters; Johnson [3] treats the coupled sizing equations and the trade between hover power and rotor mass. The study that applies the classical method to the Westland Lynx rotor [4] is introduced as the validation reference: it sizes the rotor step by step without optimisation and reports the resulting geometry and hover power, which the thesis will reproduce.

The second part summarises the operation of the genetic algorithm (population, fitness evaluation, selection, crossover, mutation and the new-generation loop) and its use in engineering design problems, drawing on the review [1], which surveys operators and parameter settings and finds that real-coded encodings with adaptive mutation are most common for continuous design variables, and on the rotor conceptual design paper recommended by the supervisor [5]. Sources are not visited one by one; their methods and findings are given together under the relevant heading.

The third and longest part is the method plan: the BEMT–genetic algorithm workflow, the assumptions of the hover performance model, the encoding of design variables as a chromosome, candidate objective functions and constraints (an indirect tip Mach limit through the tip speed range, an upper bound on blade loading, the thrust demand from the mission weight), algorithm settings and library choice, the validation strategy with the Lynx rotor, and the current state and timeline. Since no numerical results exist yet, the seminar ends with a "next steps" slide instead of a results section.

## Seminar–Thesis Relation
The seminar covers the "problem definition and method plan" part of the thesis; the literature survey, the construction of the design-variable space and the writing of the hover performance model carried out in the first semester fall within this scope. Because the thesis has no numerical results yet, no findings are presented; the single value from the trial run of the hover model is not shown because it has not been validated. The forward-flight model, the comparison with the reference design and the discussion of results belong to later semesters and are outside the seminar.

## Acknowledgements
The author thanks Assoc. Prof. Dr. Ayşe Kaya [fictional] for her guidance and colleagues at the author's workplace for discussions on rotor sizing practice. No external funding was received.

## Declaration of AI Use
Claude (Anthropic) was used in preparing this form and the seminar presentation. The tool was used to structure the content through a question-and-answer interview with the author, to edit the texts for language and format, to format the references in IEEE style and check them through Crossref, to fill the form and presentation templates, and to redraw the design-variable chart with values set by the author. The data, analyses, findings and interpretations of the thesis and the selection of sources belong to the author; the tool was not used for these purposes. ChatGPT (OpenAI) was occasionally used for debugging code. The author is responsible for the accuracy of the text and the suitability of the sources.

## References
[1] S. Katoch, S. S. Chauhan, and V. Kumar, "A review on genetic algorithm: past, present, and future," Multimedia Tools and Applications, vol. 80, no. 5, pp. 8091–8126, 2021, doi: 10.1007/s11042-020-10139-6.
[2] J. G. Leishman, Principles of Helicopter Aerodynamics, 2nd ed. Cambridge, U.K.: Cambridge Univ. Press, 2006.
[3] W. Johnson, Rotorcraft Aeromechanics. Cambridge, U.K.: Cambridge Univ. Press, 2013, doi: 10.1017/CBO9781139235655.
[4] D. Novak, T. Bucak, and A. Domitrović, "Helicopter main rotor conceptual design: application to a Westland Lynx helicopter," Promet – Traffic & Transportation, vol. [DOĞRULANACAK], no. [DOĞRULANACAK], pp. [DOĞRULANACAK], 2008.
[5] [DOĞRULANACAK: AHS Forum paper, 2011].
