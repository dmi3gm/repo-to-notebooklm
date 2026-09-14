## NSTD.5 - Engagement, Attention, and Motivation

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `NarrativeEngagementBoundary@Context`, a DPF-local boundary record for one narrative rendering.

### NSTD.5:1 - Problem frame

Use this pattern when a narrative must be followed, remembered, cared about, or acted on, but engagement risks distorting source structure, persuasion boundary, ethical use, evidence use, assurance, or policy interpretation.

First useful move: state the intended engagement effect, the source structures that may not be distorted for that effect, and the non-admissible downstream use.

What goes wrong if missed: attention becomes confidence. Suspense, identification, emotional salience, fluency, and memorability make readers rely on the narrative beyond its source relation.

What this buys: engagement can be designed as support for declared use, not as an authority amplifier.

### NSTD.5:2 - Problem

Narratives often work because they attract attention and organize memory. That value is real. But the same mechanisms can overpersuade, hide uncertainty, simplify conflict, or make a reader treat a narrative as evidence, assurance, or permission.

### NSTD.5:3 - Forces

| Force | Tension |
| --- | --- |
| Attention vs source fidelity | Engagement can help readers reach source structure or distract from it. |
| Motivation vs manipulation | Motivation may be appropriate for teaching but unsafe for decisions or policy. |
| Memory vs overconfidence | Memorable stories can feel more certain than their sources. |
| Reader diversity vs one route | A motivating route for one group may mislead or harm another. |

### NSTD.5:4 - Solution

Record engagement as a bounded use support.

```text
NarrativeEngagementBoundary@Context:
  narrativeRenderingRef:
  intendedEngagementEffect:
  protectedSourceStructureRefs:
  languageStateFacetProfileRef?:
  coarseningOrPrecisionOwnerRefs?:
  affectedReaderOrGroupRefs?:
  persuasionBoundary:
  nonAdmissibleUse:
  ethicsOwnerRefs?:
  evidenceOrAssuranceOwnerRefs?:
  lowValueRepairAction:
```

Admit engagement only when it serves the declared use and does not widen authority. If engagement depends on artistic, literary, dramatic, compressed, or simplified wording, name whether the live issue is a language-state profile (`C.2.LS`), controlled coarsening (`A.6.3.CSC`), explanation-facing rendering (`E.17.EFP`), or precision restoration (`E.10`, `A.6.P`, `C.16.Q`). If engagement increases reliance pressure, route the stronger claim to ethics, evidence, assurance, gate, policy, or work owners.

Design engagement through a protected-structure loop.

1. Name the intended engagement effect: attention, curiosity, emotional salience, identification, suspense, memorability, motivation, or willingness to continue.
2. Name the protected source structures that may not be distorted to get that effect.
3. Choose the device: example, analogy, scene, viewpoint, contrast, unresolved tension, repetition, rhythm, visual image, or narrative hook.
4. State what the device is allowed to change: order, salience, language state, compression, repetition, or route.
5. State what it is not allowed to change: evidence strength, source truth, agency, responsibility, moral permission, policy authority, work authorization, or proof status.
6. Evaluate the result through `NSTD.6`, not through liking alone.

Use a reliance-pressure ladder.

| Reader reaction sought | Typical safe use | Extra owner needed if stronger |
| --- | --- | --- |
| Keep reading | Orientation or teaching support | None unless source loss or manipulation risk appears. |
| Remember a structure | Learning or source-return support | `NSTD.6` reconstruction evidence; `NSTD.8` for learning route. |
| Care about a problem | Motivation for attention or inquiry | `D.1` through `D.5` if harm, affected parties, conflict, or decision pressure is live. |
| Trust a claim | Not owned by engagement | `A.10`, `B.3`, source owner, assurance owner. |
| Decide or act | Not owned by engagement | Decision, policy, ethics, work, or gate owner. |

Engagement can fail in two opposite ways. It may be too weak: readers do not stay with the material long enough to recover the selected source structure. It may be too strong: readers rely on the story past the source-return boundary. The repair is different. Low attention may need a better hook, example, rhythm, or viewpoint. Overreliance needs weaker claim language, source-return markers, affected-party routing, or lower admissible use.

When engagement uses artistic or literary language, do not reduce the issue to style preference. Ask which language-state facet changed: articulation, closure, anchoring, representation factor, threshold, compression, or cue. A more literary passage can be better for a memorial or exploratory essay and worse for a technical source-return task. The declared use and protected source structures decide.

### NSTD.5:5 - Archetypal Grounding

#### Mature worked slice: engagement without persuasion capture

A learning narrative about FPF uses a dramatic failure story: a team blindly follows a pattern checklist and damages its project. The story is engaging, but it may over-persuade if it implies that FPF prevents all such failures or that the named team is evidence. `NSTD.5` keeps interest useful and bounded.

```text
NarrativeEngagementBoundary@FPFFailureStory:
  narrativeRenderingRef: FPFLearningRoute@v1
  engagementDevice: failed-use contrast with tension and repair
  protectedSourceStructureRefs:
    - pattern conditions
    - forces
    - neighboring exits
    - evaluation and improvement route
  intendedEffect: keep attention and make misuse recognizable
  persuasionOrHarmRisk: reader treats story as proof of FPF superiority or as blame of a real group
  sourceFidelityRisk: checklist failure hides the actual source relation being taught
  precisionBackoff: mark the story as an archetype and return to pattern body for authority
  evaluationReturn: `NSTD.6` checks reconstruction, not emotional agreement
```

Before:

> This disaster proves why teams must use FPF.

After:

> This fictionalized failure case shows one misuse: treating a pattern as a checklist after the governing situation has changed. It motivates attention, but the authority returns to the pattern body and the evidence or assurance claim would need its own owner.

#### Mature worked slice: homotopy interest without analogy capture

A homotopy lesson uses the image of a loop "slipping around a hole". The image is engaging and memorable, but it may cause learners to think all deformations are allowed. `NSTD.5` protects the formal boundary:

```text
NarrativeEngagementBoundary@HomotopyLoopImage:
  engagementDevice: vivid analogy
  protectedSourceStructureRefs: deformation under constraints, invariant, formal definition, proof-status boundary
  intendedEffect: sustain attention through abstraction
  persuasionOrHarmRisk: low, unless used to make a false certainty claim
  sourceFidelityRisk: analogy replaces condition-bound definition
  precisionBackoff: state where analogy stops and return to formal statement
  evaluationReturn: learner marks allowed and blocked deformation conditions
```

#### Engagement device selection matrix

| Device | Buys | Risk | Required repair handle |
| --- | --- | --- | --- |
| Tension | Keeps attention across uncertainty. | Reads as evidence closure. | Name uncertainty and source return. |
| Failure story | Makes misuse vivid. | Becomes blame or proof by anecdote. | Mark archetype, evidence owner, and protected structure. |
| Analogy | Makes abstraction traversable. | Replaces definition or proof boundary. | State analogy stop condition. |
| Character viewpoint | Improves salience. | Imports agency or responsibility. | Use `NSTD.4` literalization repair. |
| Surprise reveal | Supports memory and curiosity. | Hides source constraints from worker as well as reader. | Return to `NSTD.1` and `NSTD.2` before composing. |
| Humor or style | Reduces attention cost. | Coarsens terms beyond later use. | Use `C.2.LS`, `A.6.3.CSC`, and `E.10` when claim-bearing. |

#### Calibration for engagement quality

| Value | Engagement condition |
| --- | --- |
| `2` | The narrative is interesting, but protected structures, persuasion risk, or precision backoff are not recoverable. |
| `3` | Engagement device and intended effect are named, but source-fidelity or harm repair is weak. |
| `4` | Engagement supports declared use while preserving source return, precision backoff, and ethics and evidence exits. |
| `5` | A low-engagement and high-engagement variant can be compared, and the high-engagement variant improves attention without lowering `NSTD.6` source recovery or owner routing. |

#### FPF owner teaching

`NSTD.5` is the pattern that prevents "make it interesting" from becoming a hidden ethics, evidence, or quality claim. FPF already distinguishes value, evidence, assurance, affected parties, language state, and quality terms. Narrative work does not override those distinctions; it adds a design concern: attention must be earned without capturing the selected source structure past the declared use.

An explanation of FPF uses a story of a team fixing a broken pattern. The engagement effect is motivation and memory. Protected source structures are EntityOfConcern, forces, solution, checks, and source-return condition. The story may not be used as proof that the pattern works in all domains. Evaluation must check reconstruction, not only enjoyment.

A science-communication narrative may use tension around an unresolved experiment. The protected structures are the actual measurement, the attempted explanation, the uncertainty, and the boundary between "suggests" and "shows". If the story makes readers feel that the policy decision is settled, `NSTD.5` lowers the engagement design or routes policy and ethics claims to their owners.

A homotopy lesson may use a memorable image of stretching loops. The image is admissible only if learners can still recover definition boundaries and source-return points. If the image helps memory but makes learners treat all deformations as equivalent without conditions, repair source selection and event or model support before adding more vivid imagery.

A franchise continuation may use suspense, stakes, and identification. Those devices are useful when they protect attention to causal plot and character agency. They fail when fan-service or shock replaces continuity, source constraints, or agency support.

Live commentary may use excitement to keep listeners oriented. The protected structures are observed event, provisional inference, score state, and uncertainty. Engagement fails when suspense turns prediction into fact or blame into settled responsibility.

Choose engagement devices by protected structure, not by taste alone.

| Device | Good use | Failure mode | Repair |
| --- | --- | --- | --- |
| Hook | Creates initial attention for a source-returnable route. | Becomes clickbait or false problem statement. | Add source-return promise and blocked overread. |
| Tension | Keeps unresolved relation visible. | Converts uncertainty into dramatic certainty. | Name unresolved relation and evidence owner. |
| Identification | Helps readers track a role or viewpoint. | Turns sympathy into permission, blame, or policy. | Add affected-party and ethics routing. |
| Analogy | Makes abstract structure graspable. | Replaces definition or proof boundary. | State where analogy stops and source returns. |
| Repetition | Keeps source spine memorable. | Repeats slogan without reconstruction. | Pair each repeat with a reconstruction task. |
| Compression | Makes route usable under attention budget. | Drops distinctions needed for downstream use. | Use `A.6.3.CSC` or narrow admissible use. |
| Literary style | Supports felt sense, pacing, or atmosphere. | Becomes quality authority or source-authority signal. | Route language-state and evaluate declared-use quality. |

Do not remove engagement just because it is dangerous. Low engagement can make source recovery impossible because readers never stay with the route. The pattern's job is to bind engagement to a declared use, protected structure, and owner routing. A dry but unmemorable explanation can fail `NSTD.6` for learning use; a vivid but overpersuasive story can fail for evidence or ethics boundary. Both failures are real, but they have different repairs.

Filled engagement-boundary records:

```text
NarrativeEngagementBoundary@FPFLearningRoute:
  intendedEngagementEffect: motivation and memory for pattern-use reconstruction
  protectedSourceStructureRefs: EntityOfConcern; forces; solution; relations; source-return condition
  languageStateFacetProfileRef: plain teaching narrative with repeated anchors
  affectedReaderOrGroupRefs: new FPF authors and reviewers
  persuasionBoundary: may motivate study; may not prove FPF authority or tell readers to bypass checks
  nonAdmissibleUse: evidence of FPF correctness; replacement for pattern bodies
  lowValueRepairAction: add reconstruction task, source-return prompt, or lower motivational slogan
```

```text
NarrativeEngagementBoundary@HomotopyAnalogy:
  intendedEngagementEffect: curiosity and retention for abstract structure
  protectedSourceStructureRefs: definitions; examples; proof-status boundary; formal return
  languageStateFacetProfileRef: analogy plus formal boundary markers
  persuasionBoundary: analogy may invite exploration, not replace proof
  nonAdmissibleUse: theorem proof, formal definition, or exam solution without source return
  lowValueRepairAction: add formal boundary, counterexample, or source-return step before more metaphor
```

```text
NarrativeEngagementBoundary@FranchiseContinuationProbe:
  intendedEngagementEffect: suspense, identification, and stakes for private storycraft critique
  protectedSourceStructureRefs: canon constraint; continuity; character agency; causal plot support
  affectedReaderOrGroupRefs: private reviewers; no public audience permission implied
  persuasionBoundary: emotional satisfaction does not override source-pack or rights boundary
  nonAdmissibleUse: publication, canon authority, or rights claim
  lowValueRepairAction: repair continuity, agency, or causal support before increasing drama
```

```text
NarrativeEngagementBoundary@LiveCommentary:
  intendedEngagementEffect: attention under unfolding uncertainty
  protectedSourceStructureRefs: observed event; provisional inference; score state; official return
  affectedReaderOrGroupRefs: listeners and any named parties if blame or harm framing appears
  persuasionBoundary: suspense and emotion do not settle blame, prediction, or official fact
  nonAdmissibleUse: final evidence, disciplinary judgment, or settled tactical analysis
  lowValueRepairAction: add uncertainty markers, source-return route, or lower blame wording
```

### NSTD.5:6 - Bias-Annotation

This pattern blocks engagement-authority drift: attention, identification, suspense, memorability, or motivation is treated as truth support, ethics clearance, assurance, policy permission, or work authorization. Repair by naming protected source structures, persuasion boundary, affected readers when live, and direct owners for stronger claims. Scope: DPF-local for engagement in narrative renderings; it does not govern all persuasion or ethics work.

### NSTD.5:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD5-1` | Engagement effect is named as use support. |
| `CC-NSTD5-2` | Protected source structures are named. |
| `CC-NSTD5-3` | Persuasion, policy, work, evidence, ethics, and assurance use boundaries are explicit when live. |
| `CC-NSTD5-4` | Affected readers, listeners, or groups are named when harm or manipulation risk is live. |
| `CC-NSTD5-5` | Low engagement does not automatically fail declared-use rendering quality; low source recovery does fail source-recovery quality when source recovery is required. |
| `CC-NSTD5-6` | Artistic, literary, dramatic, simplified, or memorable wording is routed to language-state, coarsening, explanation, or precision owners when it changes source recovery, authority, or declared use. |

### NSTD.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency as truth | Smooth narrative is treated as supported claim. | Route evidence to `A.10` and evaluate source recovery in `NSTD.6`. |
| Identification as permission | Readers identify with a protagonist and infer what they should do. | Add persuasion boundary and route policy or work claims to owners. |
| Artisticness as adequacy | More literary or memorable wording is treated as a better narrative regardless of lost structure. | State the language-state or engagement choice, then evaluate source recovery and source return through `NSTD.6`; use `A.6.3.CSC` if distinctions were deliberately dropped. |
| Engagement-only success | Readers liked it but cannot reconstruct source structure. | Add reconstruction task and repair via `NSTD.1` through `NSTD.3`. |

### NSTD.5:9 - Consequences

The benefit is safer narrative power: attention is used without stealing evidence or ethics authority. The cost is that designers must state when engagement is not enough.

### NSTD.5:10 - Rationale

The best narrative practice does not reject engagement. It disciplines engagement by purpose, audience, source fidelity, and ethical boundary. FPF makes those boundaries explicit and owner-routed.

### NSTD.5:11 - SoTA-Echoing

Green and Brock's "The Role of Transportation in the Persuasiveness of Public Narratives" treats transportation as a persuasion-relevant effect; Dahlstrom and Ho's "Ethical Considerations of Using Narrative to Communicate Science" makes accuracy loss, policy influence, and affected readers visible; Mengelkamp et al.'s "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" shows engagement and metacomprehension can mislead without explicit goals; Georgiou et al.'s "Large-scale study of human memory for meaningful narratives" warns that memory can preserve summary and order while losing source detail. The DPF adopts engagement as a design characteristic but routes persuasion, harm, bias, evidence, and assurance through FPF owners.

Operational payload:

- From transportation research, engagement can change persuasion. `NSTD.5` therefore treats engagement as a power, not as decoration.
- From science-communication ethics, narrative can change accuracy, policy interpretation, and perceived obligation. The pattern therefore requires non-admissible downstream use and affected-reader routing when live.
- From reading-goal research, explicit goals matter. A narrative that works for motivation may fail for comprehension, and a narrative that feels understood may increase overconfidence.
- From memory research, long narratives can preserve gist and sequence while losing source detail. `NSTD.5` therefore protects source structures and sends learning cases to reconstruction tasks.
- From FPF language-state and coarsening patterns, literary, compressed, or memorable wording is a change in representation, not an automatic quality increase.

The practical consequence is that engagement is evaluated by its service to declared use and protected structure. It is not a moral permission slip, evidence boost, or universal quality value.

### NSTD.5:12 - Relations

Uses `A.6.3.NAR`, `NSTD.1`, `NSTD.3`, `NSTD.6`, `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, `C.16.Q`, `D.1` through `D.5`, `A.10`, `B.3`, `E.17`, and `G.11`. Reopen when reader telemetry, harm assessment, source fidelity, language-state profile, coarsening relation, precision repair, or persuasion boundary changes. Support-map entry: open `Semiotic And Language-Precision Bridge` when interesting, literary, artistic, memorable, hook, cue, coarsening, or explanation language becomes load-bearing; open `DPF Precision Restoration And Owner Map` when engagement, adequacy, quality, value, or persuasion terms overload; open `Source Use And Refresh Map` when persuasion, memory, cognition, or ethics source claims carry the boundary.

### NSTD.5:End

## NSTD.6 - Declared-Use Narrative Rendering Quality Evaluation

> **Type:** DPF evaluation pattern body

> **Primary EntityOfConcern:** `NarrativeRenderingQualityEvaluationCharacteristicSpace@Context`, an evaluation `CharacteristicSpace` for one evaluated narrative rendering kind and declared use.

### NSTD.6:1 - Problem frame

Use this pattern when a team must decide whether one admitted narrative rendering version is good enough for one declared reader or listener use. An editor may evaluate a directly authored or already existing product without knowing how its author produced it. State whether the present question concerns that product's current quality, a promised source-to-result relation, or assurance about actual construction work; these questions need different evidence.

Evaluated object kind: `NarrativeRenderingVersion@Context`, meaning one admitted narrative rendering version with admitted source basis, selected source structures, declared use, ordering rule, and source-return condition. A source text, source pack, style guide, seminar script, slide deck, generated output before `C.35` admission, or broad communication plan is not this evaluated object.

First useful move: state "quality of which admitted narrative rendering version, for which declared use, under which temporal posture and rendering mediation mode, against which contrast cases?" Then name one admissible narrative rendering, one below-floor narrative rendering, and one wrong-kind object that must return to evaluation selection.

What goes wrong if missed: readability, elegance, engagement, expert approval, or generated fluency substitutes for epiplexity, source-return discipline, and bounded use.

What this buys: a repeatable evaluation that can feed `E.23` improvement without confusing characteristics, measurements, eval programs, evidence, assurance, or gates.

Quality target: this pattern evaluates quality for one declared use under source-structure selection fit, `NarrativeRenderingEpiplexity`, ordering recoverability, temporal-posture and role fit, source-return readiness, bounded engagement, and owner-routed evidence, assurance, ethics, publication, and work claims.

### NSTD.6:2 - Problem

Narrative rendering quality for declared use is not one property. A narrative can be fluent but structurally false, engaging but ethically unsafe, technically accurate but unusable for learners, or source-faithful but impossible to follow. A useful evaluation needs object-kind fit, characteristic slots, value meanings, evidence basis, missingness rules, floor, exceptional meaning, result-row shape, and repair actions.

### NSTD.6:3 - Forces

| Force | Tension |
| --- | --- |
| Fluency vs epiplexity | A readable narrative may pull too little selected source structure into the rendering for the declared use. |
| Engagement vs bounded use | A motivating narrative may overpersuade. |
| Local usability vs reusable scale | A project can use a small rubric, but DPF needs reusable value meanings. |
| Measurement vs evaluation | Some values may be measured through `C.16`; many are ordinal content evaluations. |
| Improvement vs Goodhart pressure | Indicatorized characteristics help loops, but unmeasured tracked concerns must prevent proxy capture. |

### NSTD.6:4 - Solution

Construct and use one narrative rendering quality evaluation characteristic space for one declared use. Reuse a sufficient current specification and result when their object, question and conditions still match.

For the structural-amount question, `NarrativeRenderingEpiplexity` specializes [`C.2.8 U.ExtractableStructuralInformation`](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c28---uextractablestructuralinformation): the structure this reader or observer can extract. Its three bearers are the receiving narrative episteme, the publication form expressing it, and the specified reader or observer. The selected source structure, correctness criterion, usable prior knowledge, operations, help, access and budget qualify this tuple. An unambiguous rendering reference can identify the account and expression. Use the existing epiplexity basis, scale and evidence fields below to retain the qualifications needed for the comparison; they do not create another bearer or record kind.

Begin with named additional and missing relations when a qualitative comparison answers the question. If a number is useful, count correctly recovered selected semantic relations at a declared grain, optionally as `n/N` for a fixed nonempty selected set. Each unit preserves participants, predicate, polarity, modality and action-changing conditions. Repeated words, headings or arrows do not add units. Retain which relations were recovered: equal counts can differ in suitability for the next use. A different ordinal or nonnegative structural weighting needs its own explicit structural meaning; a utility weighting is another score. A formal bit estimate needs the mapping in `C.2.8`, not merely the name epiplexity.

State whether the basis is a conditional design walkthrough, an actual reading or a mapped formal estimate. One response establishes the recovery observed in that trial and can ground an extractability estimate; it does not establish a maximum, impossibility after failure, or reliability across a reader class. An exact computational amount requires the corresponding method and model. Keep the first response, actual help and source returns. Familiar structure can be recovered from an expression; an expert's independent correction of false or absent instruction earns that expression no credit. Recovery of what a source asserts and recovery of warranted subject structure use different correctness questions.

Compare forms with claims and relevant conditions held constant. Added or changed substantive claims can identify another episteme through `C.2.1`; changed access, preparation or help qualifies another comparison. A transfer or perturbation result belongs to its tested condition or robustness question and adds nothing to the original amount by itself. Compare effort and usefulness separately through `C.11.CRC` and `C.11`; keeping the sufficient rendering is an available result.

```text
NarrativeRenderingQualityEvaluationCharacteristicSpace@Context:
  evaluatedObjectKindRef: NarrativeRenderingVersion@Context
  declaredUseScope:
  objectKindFitRule:
  discriminatingCaseSet:
  characteristicSlotSet:
  epiplexityBasisRule:
  scaleBindingSet:
  valueMeaningSet:
  evidenceBasisRule:
  missingnessAndLoweringRule:
  resultRowShape:
  floorAndExceptionalMeaning:
  protectedTradeoffSet:
  stopOrReopenCondition:
  neighboringGoverningPatternRefs:
```

Object-kind fit:

| Object-kind case | Handling |
| --- | --- |
| Admissible narrative rendering | Evaluate all load-bearing characteristics for the declared use. |
| Below-floor narrative rendering | Evaluate and return low-value repair actions. |
| Wrong-kind object before invocation | Return to evaluation selection; choose admitted source basis, style, seminar, generation, publication, or evidence owner. |
| Wrong-kind object after invocation | Record explicit object-kind-fit defect and stop; do not silently assign values to unrelated coordinates. |

Default value meanings for the other ordinal content-quality characteristics follow. `NarrativeRenderingEpiplexity` uses its own structural scale above; the following 0–5 labels do not assign its amount, missingness or use threshold:

| Value | Meaning |
| --- | --- |
| `0` | Wrong-kind object, no admissible basis, or evaluation must stop before value use. |
| `1` | Object is a narrative rendering but unusable for the declared use. |
| `2` | Orientation only; source return is needed before reliance. |
| `3` | Locally usable with named limitations and repair obligations. |
| `4` | Good for declared use with bounded losses and source return. |
| `5` | Strong for declared use; the current source relation, response to a meaningful change, and consequential boundary cases are replayable. Actual construction or repair history is additionally replayable when a historical claim is part of the declared use. |

For reliance-bearing or teaching use, the default for structural recovery is that every relation declared necessary for that use must be recoverable under the specified support and evidence conditions. State those necessary relations at the grain the decision needs; a short account of the required distinction and stop can suffice. There is no generic structural-amount floor of `4`. Keep the amount and satisfaction of the use condition separate: unrelated extra relations cannot compensate for a missing necessary relation.

The other load-bearing quality characteristics retain default floor `4` on their own scales, including `OrderingRecoverability` and `SourceReturnReadiness`. When the selected source structure is a constraint-governed unfolding structure, `DemonstrativeSliceRecoverability` is load-bearing and may not be below `4`. A local low-risk orientation use may set those quality floors to `3` only if non-admissible downstream use is explicit. Neither numeral translates into a structural amount. A narrower use fixes its structure selection before evaluation; removing a difficult relation after observing the answer changes the basis rather than improving the original amount.

Result-row shape:

```text
NarrativeRenderingQualityResultRow@Context:
  narrativeRenderingVersionRef:
  declaredUseScopeRef:
  characteristicId:
  characteristicName:
  scaleRef:
  value:
  evidenceBasisRefs:
  missingnessClass:
  loweringReason:
  repairAction:
  directOwnerRefs:
  reopenCondition:
```

Package the rows before feeding an improvement loop:

```text
NarrativeRenderingQualityEvaluationResult@Context:
  evaluatedNarrativeRenderingVersionRef:
  declaredUseScopeRef:
  evaluationCharacteristicSpaceRef: NarrativeRenderingQualityEvaluationCharacteristicSpace@Context
  evaluationPurpose:
  evidenceBasisRefs:
  resultRows:
  protectedTradeoffSet:
  belowFloorRows:
  candidateImprovementProposalRows?:
  nonUseBoundary:
  stopOrReopenCondition:
```

When repeated improvement is wanted, open `E.22` first if the quality question is not already framed. Then use `E.23` with `NSTD.6` as the object-under-improvement evaluation. This DPF does not mint a local loop kind.

```text
NarrativeRenderingImprovementLoopInput@Context:
  e22QuestionFrameRef?:
  objectUnderImprovementRef: NarrativeRenderingVersion@Context
  objectVersionBeforeRef:
  objectUnderImprovementEvaluationRef: NSTD.6
  improvementAim:
  protectedTradeoffSet:
  costAndRiskAccount:
  allowedChangeSlice:
    narrativeRenderingVersion | NSTD.1-intake | NSTD.2-ordering |
    NSTD.3-event-model | NSTD.4-viewpoint | NSTD.5-engagement |
    NSTD.7-generated-carrier-admission | NSTD.8-learning-route |
    evaluationCharacteristicSpace
  returnedFindingOrProposalRows:
  expectedReEvaluationResultForm: NarrativeRenderingQualityEvaluationResult@Context
  neighboringGoverningPatternRefs:
  stopContinueSwitchOrHoldCondition:
```

`E.23` may claim improvement only after the changed object version is re-evaluated through `NSTD.6` or through a declared stronger evaluation. If the loop changes the source pack, source-currentness, generated-carrier admission, learning publication carrier, publication face, ethics claim, evidence claim, assurance claim, or evaluation characteristic space, the loop must name the neighboring governing pattern and either keep it as the allowed change slice or open separate work. Style edits, prompt retries, or additional drama are admissible loop operations only when their expected movement under `NSTD.6` is stated and protected trade-offs are checked. `B.4` is relevant only when the narrative episteme or learning route is claimed to evolve across use and renewed operation; `G.11` handles refresh when source currentness, reader telemetry, teaching-test evidence, generated-narrative practice, or FPF edition changes.

Before assigning values, recover the source and use basis for the question being answered.

For current-product evaluation, name the selected subject structures, intended reader work and necessary prerequisites, then trace what the present rendering preserves, hides or loses. Use the task and qualified subject sources to establish the needed structure; the rendering can help refine that basis but cannot excuse its own omissions. Recover its ordering rationale, source-return condition, and the event or mechanism, viewpoint, agency, engagement and learning-route relations that matter to this use through `NSTD.1` through `NSTD.5` and `NSTD.8`. Point to actual source and rendering passages. If this account is reconstructed now, identify it as an evaluation of the current product, with its uncertainties, not a record of what the author did. Missing manufacturing notes do not by themselves lower current-product values; missing subject basis, inaccessible return or unsupported relation still does.

For a promised transformation, compare the named source and result versions against the promised preservation or change. This can establish their present fidelity relation without establishing the actual sequence of manufacturing actions. For a claim about actual construction or repair, obtain records or other admissible evidence of those actions and distinguish them from a plausible reconstruction. Trace the applicable `NSTD.1` selection, `NSTD.2` ordering, `NSTD.3` mechanism, `NSTD.4` viewpoint, `NSTD.5` engagement and `NSTD.8` learning-route decisions. If their history cannot be established, leave that historical or assurance claim unsupported and return it to its owner. A good product does not supply the missing history.

Object admission remains a separate prerequisite of this full evaluation. When the object is generated output, a reconstructed plan or a favourable product judgement does not supply `NSTD.7`/`C.35` admission. A current-product result or source-to-result comparison can inform further work, but reuse as evidence must satisfy `A.10`; assurance, publication authority and human learning-effect claims still need their own basis and governing owner.

Use this evaluation sequence:

1. Object-kind fit: is this an admitted narrative rendering version, not source text, source pack, slide deck, prompt output, style guide, or broad communication plan?
2. Evidence fit for the question: for current-product quality, recover selected source structures, ordering, source return and relevant relations from the subject/use basis and present rendering; for promised fidelity, compare the named source and result; for actual construction or repair, recover evidence of the claimed actions. Keep these conclusions distinct.
3. Declared-use fit: is the reader or listener use narrow enough to evaluate, and are non-admissible downstream uses stated?
4. Load-bearing characteristics: assign values only to the characteristics needed for the declared use, but include every characteristic whose failure would make the use unsafe or useless.
5. Low-value repair: for every value below floor, name the smallest repair route before proposing style, drama, or generation retries.
6. Re-evaluation route: if any repair changes the object version or selected source basis, plan a new `NSTD.6` evaluation before claiming improvement.

Missingness and lowering rules:

| Missing or defect condition | Lowering rule |
| --- | --- |
| Selected source structures cannot be identified from the subject/use basis | Leave the structural amount unassigned and return the exact selection gap to `NSTD.1`. A missing basis is not a small amount; apply any actual object-kind defect separately. |
| Reader, correctness criterion or other action-changing structural-comparison condition cannot be recovered | Leave the amount unassigned at that scope; retain any narrower supported result and continue independently answerable diagnosis. An absent observation is not a zero. |
| Ordering rule absent | `OrderingRecoverability` no higher than `2`. |
| Source temporal posture, rendering mediation mode, narrating worker, or reader role absent | `TemporalPostureAndRoleFit` no higher than `2`; return to `NSTD.1` before trusting evaluation. |
| Source-structure selection rationale or reader-interest hypothesis absent | Return to `NSTD.1` before style or engagement repair; the existing temporal-posture/use quality rule remains no higher than `2`. For structural amount, identify whether selection, correctness or observer conditions are actually missing. If so, leave the amount unassigned; a missing field alone does not erase a recoverable basis. |
| Source-return condition absent | `SourceReturnReadiness` no higher than `2`. |
| Constraint-governed unfolding structure is selected but the rendering declares only a sequence, route card, story line, or lesson chain | `DemonstrativeSliceRecoverability` no higher than `2`; return to `NSTD.1`, `NSTD.2`, and `A.22.CGUS` or the local governing pattern before treating the narrative as a rendering of the wider structure. |
| Artistic, literary, simplified, or dramatic wording changes source recovery without owner routing | `LanguageStatePrecisionAndCoarseningFit` no higher than `2`; return to `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, or `C.16.Q` before treating style repair as improvement. |
| Early hook, vibe, story seed, or route hint is evaluated as an admitted narrative rendering | Wrong-kind object for this evaluation; return to `A.16.1`, then `NSTD.1` and `NSTD.2` when route selection becomes explicit. |
| Engagement effect asserted without persuasion boundary when influence is live | `EngagementBoundedness` no higher than `3` and ethics owner must be named. |
| Generated output not admitted through `C.35` | Wrong-kind object for this evaluation; return to `NSTD.7` and `C.35`. |
| Evidence or assurance claim made without owner | Qualify the unsupported claim and route it to `A.10` or `B.3`; lower a relevant quality value only under its own meaning. An unsupported structural amount is unassigned rather than numerically penalized. |
| Manufacturing or repair history absent while the current-product basis is available | Do not lower a product characteristic for this absence alone. Leave any historical claim unsupported and return the evidence or assurance question to its owner; apply every relevant source, use, admission and missingness rule independently. |

A defined trial that recovers none of the selected relations supports observed recovery `0` on that scale, not impossible extraction. An empty denominator supports no fraction. Wrong-kind handling precedes amount assignment. A qualified design estimate can remain available without an actual trial; obtain a trial when its possible outcomes can change the receiving decision.

Default narrative rendering quality characteristics:

| Characteristic | Evaluation question | Low-value repair action |
| --- | --- | --- |
| `SourceStructureSelectionFit` | Are the selected source structures and reader-interest or use hypothesis explicit, non-magical, and well matched to the declared use? | Reopen `NSTD.1`; reconstruct or revise the source-structure selection rationale before changing style, drama, or prompt wording. |
| `NarrativeRenderingEpiplexity` | What selected structure can this observer correctly extract from the narrative episteme through this expression under the declared conditions, and how does that compare with the alternative? | Use `C.2.8` for the common characteristic. Return a selection gap to `NSTD.1`; repair the missing or false relation, its expression or its usable source return through the relevant NSTD method. A better basis declaration alone does not increase amount. `C.33` separately governs architecture-description adequacy when that question is live. |
| `OrderingRecoverability` | Can the reader say why this sequence was chosen and what it hides? | Reopen `NSTD.2`; state ordering rule, preserved relations, and lost relations. |
| `DemonstrativeSliceRecoverability` | When a constraint-governed unfolding structure is selected, can the reader recover the wider structure, the demonstrative slice, and the hidden branches, loops, alternatives, direct exits, or stop conditions? | Reopen `NSTD.1` and `NSTD.2`; name the selected CGUS or local block, the demonstrative slice, preserved constraints, lost structure, and return to `A.22.CGUS` or the local governing pattern. |
| `TemporalPostureAndRoleFit` | Do source temporal posture, rendering mediation mode, intended rendering Work role, any actual performer and role assignment, any load-bearing narrative voice or viewpoint, reader or listener role, uncertainty, automated-narrativization admission case, and source-return obligation match the declared use? | Reopen `NSTD.1`; mark retrospective, live, prospective, architecture-mediated, or mixed posture; repair the Work-role, actual-performer, narrative-function, admission, and reader-role split; lower claims that overread provisional or fictional structure. |
| `EventMechanismSupport` | Can the reader reconstruct events, mechanisms, dependencies, or state changes when required? | Reopen `NSTD.3`; add mechanism support or lower causal language. |
| `ViewpointAgencyDiscipline` | Does viewpoint reveal source structure without false agency, capability, responsibility, or permission? | Reopen `NSTD.4`; split protagonist, actant, role, agency, and ethics owners. |
| `EngagementBoundedness` | Does engagement support declared use without widening authority? | Reopen `NSTD.5`; add persuasion boundary or reduce engagement device. |
| `LanguageStatePrecisionAndCoarseningFit` | Does the chosen plain, technical, literary, compressed, didactic, or cue-like language state fit the declared use without hiding relation precision, quality sense, source loss, or route authority? | Publish the language-state facet profile when threshold-bearing, use `A.6.3.CSC` for narrowed-use coarsening, `E.17.EFP` for explanation-facing retelling, `A.16.1`/`A.16.2` for cue or backoff, and `E.10`, `A.6.P`, or `C.16.Q` for precision restoration. |
| `EthicsEvidenceAssuranceRouting` | Are value, harm, evidence, assurance, and policy claims routed to owners? | Route to `D.1` through `D.5`, `A.10`, `B.3`, or relevant owner. |
| `MediumAndPublicationFit` | Does the carrier fit the reader and use without changing the claim? | Route publication or audience-unit questions to `E.17`, `E.17.AUD`, or `NSTD.8`. |
| `SourceReturnReadiness` | Does the narrative tell readers when and where to return to the admitted source basis or direct governing pattern? | Add source-return condition or narrow admissible use. |

### NSTD.6:5 - Archetypal Grounding

#### Mature value bank: full result rows

Use this bank when a narrative rendering "sounds good" and therefore tempts the worker to skip evaluation. Each row evaluates an admitted rendering version for one declared use. The same text may receive different values for a different use.

| Case | Characteristic | Value | Evidence basis | Low-value repair |
| --- | --- | --- | --- | --- |
| FPF seminar handout | `NarrativeRenderingEpiplexity` | Qualitative illustration; no numerical amount established | The case assumes learners can recover `EntityOfConcern`, forces, solution and neighboring exits. These aspect names do not define equal semantic units, a denominator or an observed reading protocol. | Retain the stated recovery. If transfer matters, try choosing a governing pattern in a new situation and qualify that separate result; it does not increase the original amount. |
| FPF seminar handout | `SourceReturnReadiness` | `5` | Every slogan-like line has a source pattern return and one reconstruction exercise. | No proposal unless source patterns change. |
| FPF seminar handout | `EngagementBoundaryFit` | `4` | Failure story is marked as archetype, not evidence. | Add an explicit evidence-owner exit if the story is used in public adoption material. |
| Homotopy explanation | `LanguageStatePrecisionAndCoarseningFit` | `3` | Analogy is vivid but learners may not know where formal conditions return. | Add an analogy-stop line and a formal boundary task. |
| Homotopy explanation | `OrderingRecoverability` | `4` | Didactic order is named and proof order is deferred by value. | To reach `5`, add a second problem where learner maps story order to formal dependency order. |
| Franchise continuation probe | `SourceReturnReadiness` | `4` | Private source-pack constraints and non-publication boundary are named. | Add a continuity perturbation test: change one premise and check whether event support remains valid. |
| Live commentary | `EventMechanismSupport` | `3` | Observation and provisional interpretation are separated, but later telemetry return is only generic. | Add specific official record, replay, or statistics return condition. |
| Generated graph-to-text narrative | `GeneratedCarrierAdmissionFit` | `2` | Output is fluent, but source plan and selected lost relations are not admitted. | Return to `NSTD.7`; do not call this an admitted rendering yet. |

#### An existing product and an unknown manufacturing history

An editor receives an admitted handout rendering with a declared onboarding use, qualified subject basis and source-return links, but no manufacturing or repair journal. The editor reconstructs the needed source relations from the intended work and subject sources, follows their use through the present explanation and exercises, and tests a meaningful changed case. A missing return or a false relation is a current-product defect. No journal is needed to identify or repair it, and a strong present boundary test can support a high product value without inventing an earlier repair.

If the same editor is instead asked whether the handout faithfully transforms a named seminar, the seminar and handout must be compared. If asked whether the author performed a prescribed review or made a particular correction, evidence of that action is also needed. Current fidelity or a successful reader attempt cannot answer that historical question. If the supplied text is unadmitted generated output, return it to `NSTD.7`/`C.35` before treating it as an admitted rendering.

#### Before and after evaluation repair

Before evaluation statement:

> The narrative is strong because readers liked it and remembered the main point.

Failure: engagement and memory are treated as total quality. Source recovery, relation strength, owner routing, and use boundary are absent.

After evaluation statement:

> For the declared onboarding use, the illustrative recovery result is that learners can reconstruct the pattern-use route; a numerical amount needs a specified relation set, conditions and evidence. Source-return readiness receives value `3` because two slogans lack pattern-body refs, and engagement boundary receives value `4` because the failure story is marked as archetypal. The first repair is to add source-return refs for the slogans before changing style.

Now `E.23` has a concrete changed slice: add two source-return refs and re-evaluate source-return readiness. Revisit the amount only if the changed access or explanation can change structural recovery. An earlier amount label is reusable only through its recoverable selection, scale, conditions and evidence; an unsupported `4` does not become `4/5`.

#### Adjacent-value calibration

For structural-amount calibration, fix five relations in a narrative about reusing a review after a display change: reuse requires the same claims, the same question, and the same qualification window; an unavailable required argument stops the new check and returns it to the source; that stop preserves unrelated review results. This adapts ME.22's content example. The condition, stop and source return form one compound unit at this declared grain. Hold the reader, case facts, material, operations, help and budget constant. The counts below illustrate nested constructed recovery sets, not three observed trials or a universal five-point rubric. Another selected set uses its own count or denominator without conversion to five labels.

| Correctly recovered units | Selected set size | Meaning at the fixed conditions |
| --- | --- | --- |
| `3` | `5` | `3/5`: the three reuse conditions are correctly recovered. |
| `4` | `5` | `4/5`: those same conditions plus the required-argument stop and return are correctly recovered. |
| `5` | `5` | `5/5`: those four units plus preservation of unrelated results are correctly recovered. |

The other characteristics use their own ordinal quality meanings:

| Characteristic | `3` means | `4` means | `5` means |
| --- | --- | --- | --- |
| `OrderingRecoverability` | Order is named, but wrong reconstruction remains likely. | Order, preserved relations, lost relations, and misread block are explicit. | Conflicting order layers are handled and tested. |
| `EventMechanismSupport` | Events are coherent, but support strength is partly inferred from wording. | Relation strength and reconstruction target are explicit. | A wording or viewpoint change does not change recovered support strength. |
| `ViewpointOwnerRouting` | Viewpoint is useful, but agency or responsibility repair is incomplete. | Viewpoint function and literal owner exits are recoverable. | Reader can remove or swap viewpoint without losing source structure. |
| `EngagementBoundaryFit` | Interest exists, but source fidelity or persuasion boundary is weak. | Interest supports declared use while protecting source and owner exits. | A higher-engagement variant improves attention without lowering source recovery. |
| `GeneratedCarrierAdmissionFit` | Generated output is plausible, but source plan or admission is incomplete. | Source plan, method, admission, and evaluation route are explicit. | Source perturbation and responsibility probes both pass. |
| `LearningRouteReconstructionFit` | Learners can retell the route but not reliably reconstruct source relations. | Learners reconstruct source spine and source-return boundaries. | Learners transfer the route to a new case and identify the correct neighboring owner. |

#### Evaluation-to-improvement repair input without process theatre

`NSTD.6` does not create a big improvement program. It creates result rows. A repeated improvement loop needs only:

```text
NarrativeRenderingImprovementLoopInput@Context:
  objectVersionRef: admitted narrative rendering version
  evaluationResultRefs: selected `NSTD.6` rows
  improvementAim: raise one declared value without lowering protected trade-offs
  allowedChangedSlice: wording, source-return link, ordering marker, viewpoint repair, engagement device, generated source plan, or learning task
  protectedTradeoffSet: source fidelity, owner routing, engagement, cost, reader burden
  expectedReEvaluationForm: rerun the affected `NSTD.6` rows and any neighbor owner checks
```

If the change is "regenerate until better", the object version and changed slice are gone. If the change is "add a source-return link and an analogy-stop task", `E.23` can operate and `NSTD.6` can re-evaluate.

#### FPF owner teaching

`C.2.8` governs structural amount for architecture and non-architecture narratives alike. `NSTD.6` applies it to the admitted rendering and the selected observer/use conditions. `C.33` retains the separate architecture-description adequacy question. Source-selection fit, source-return readiness, effort and usefulness remain separately judged; a story need not be an architecture description for its structural amount to be compared.

Pass case: an FPF seminar handout narrates how a practitioner moves from problem frame to forces to solution and checks. It names FPF pattern source sections, ordering rule, learner reconstruction task, and source-return points. Its necessary source relations are recoverable under the declared support; the other selected quality characteristics can reach `4` or `5` on their own scales. The handout is not evidence that FPF is correct, and those quality labels do not assign its structural amount.

Fail despite fluency: a polished architecture story says one chosen architecture "won" because it felt coherent, hides rejected candidates, omits architectural characteristics, and gives no source-return path. The needed architecture relations are missing, so the structural-use condition fails; assign an amount only when its selection and conditions are established. `OrderingRecoverability` and `SourceReturnReadiness` can fall below their own floors even if engagement is high.

Wrong-kind object: an LLM produces a fluent story before `C.35` carrier admission and before selected source structures are recoverable. The object returns to `NSTD.7` and `C.35`; `NSTD.6` may record object-kind-fit value `0`, but that is no structural amount and it must not evaluate the text as an admitted narrative rendering.

### NSTD.6:6 - Bias-Annotation

This pattern blocks proxy-as-quality drift: readability, fluency, liking, engagement, expert approval, or generated-text benchmark value replaces object-kind fit and declared-use rendering quality. It also blocks the opposite drift where a test program is treated as the characteristic itself. Repair by selecting the evaluated object kind, scales, value meanings, evidence basis, missingness and lowering rules, floor, result rows, and repair actions. Scope: DPF-local for evaluating narrative rendering versions; it does not govern evidence, assurance, gate, decision, or publication authority.

### NSTD.6:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD6-1` | Evaluated object kind, declared use, and object-kind fit rule are explicit. |
| `CC-NSTD6-2` | At least three discriminating cases are present: pass, below-floor, and wrong-kind. |
| `CC-NSTD6-3` | Each characteristic has a declared qualitative comparison or a bound scale. Structural-amount values preserve their tuple, selection, conditions, granularity and evidence kind; generic quality labels do not substitute. |
| `CC-NSTD6-4` | Value meanings, evidence basis, missingness rules, floor, exceptional meaning, and stop or reopen condition are declared. |
| `CC-NSTD6-5` | Result rows include value, evidence basis, lowering reason, repair action, owner, and reopen condition. |
| `CC-NSTD6-6` | Measurement, eval program, evidence, assurance, gate, decision, publication, and pattern-quality claims route to owners. |
| `CC-NSTD6-7` | If repeated improvement is claimed, the `E.22` or `E.23` input names object version, `NSTD.6` as evaluation, improvement aim, protected trade-offs, allowed change slice, cost and risk account, and expected re-evaluation form. |
| `CC-NSTD6-8` | No quality movement is claimed until the changed narrative rendering version or declared changed slice is re-evaluated by `NSTD.6` or a declared stronger evaluation. |
| `CC-NSTD6-9` | Current-product reconstruction, source-to-result fidelity and evidence of actual construction or repair remain distinct; absence of manufacturing history neither defeats a supported product judgement nor licenses an unsupported historical or admission claim. |

### NSTD.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency benchmark value as quality | Smoothness replaces structure recovery. | Inspect the selected relations and evidence. Return a missing basis or repair a demonstrated loss through `NSTD.1` through `NSTD.3`; fluency alone establishes neither a high nor a low amount. |
| Style repair as precision repair | A nicer wording pass is treated as sufficient while relation kind, quality sense, language-state threshold, or coarsening loss remains hidden. | Lower `LanguageStatePrecisionAndCoarseningFit`; apply the selected FPF precision, coarsening, explanation, or language-state owner before assigning value movement to style gains. |
| Prompt loop as improvement | The worker keeps regenerating more engaging drafts without a named object version, allowed change slice, protected trade-offs, or re-evaluation. | Open `E.22` when needed, route the repair to `E.23`, and re-evaluate the changed version through `NSTD.6`; otherwise keep the generated text as an unadmitted candidate carrier under `NSTD.7` and `C.35`. |
| Evaluation theft | Quality result is used as evidence, assurance, or gate. | Keep `NSTD.6` as evaluation; route wider use to `A.10`, `B.3`, or gate owner. |
| Wrong-kind evaluation | Source text, style guide, script, or generated output is evaluated as narrative rendering. | Apply object-kind fit and return to the correct evaluation or admission owner. |
| Reconstructed history as evidence | A plausible route inferred from a good product is reported as the author's actual construction or repair. | Retain the current-product result and mark the historical claim unestablished until its own evidence is obtained. |
| Characteristics as eval programs | Test scripts or automated checks are treated as characteristics. | Keep characteristics in `A.19.ECS`; automated evals are measurement or eval-program carriers under direct owners. |

### NSTD.6:9 - Consequences

The benefit is a usable improvement target: `E.23` can improve narrative versions because values, floors, evidence, and repairs are declared. The cost is heavier evaluation before reliance-bearing use.

### NSTD.6:10 - Rationale

`A.19.ECS` says improvement cannot be better than its evaluation. `NSTD.6` specializes that lesson for narrative renderings: first recover object kind and use, then choose characteristics that discriminate narrative rendering quality for that declared use.

### NSTD.6:11 - SoTA-Echoing

FPF `A.19.ECS` and `C.16` supply the characteristic-space and result-row discipline. FPF `C.2.8` supplies the common reader-relative structural-amount characteristic and its qualified formal epiplexity specialization. `C.33` retains architecture-description adequacy. Amount, extraction effort, learning and task usefulness are different questions; their answers need not increase together. FPF `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, and `C.16.Q` supply the language-state, cue, backoff, coarsening, explanation, lexical, relation, and quality-term repairs that narrative work often needs under different vocabulary. Castricato et al.'s "Towards a Formal Model of Narratives" supports evaluating narrator-reader information flow, reader story-model evolution, uncertainty, and conveyed-information accuracy. Mengelkamp et al.'s "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" and Georgiou et al.'s "Large-scale study of human memory for meaningful narratives" make declared learner use, memory, and overconfidence measurable pressures. Ma et al.'s "Text-to-Text Automatic Story Generation: A Survey" and Rahman et al.'s "Game Knowledge Management System: Schema-Governed LLM Pipeline for Executable Narrative Generation in RPGs" show that generated narratives need coherence, controllability, structural and semantic evaluation, and human-study probes rather than fluency alone. The DPF adopts those moves through `A.19.ECS`, `C.16`, the `C.2.8` specialization and domain scale rules, and FPF owner-routing for language-state and precision repairs, not by importing a generic writing-quality rubric.

### NSTD.6:12 - Relations

Uses `A.19.ECS`, `A.17`, `A.18`, `C.2.8`, `C.16`, `C.16.Q`, `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, `C.33`, `E.22`, `E.23`, `B.4`, `A.10`, `B.3`, `E.17`, `C.35`, and `G.11`. `C.2.8` defines structural amount for all admitted source domains; `C.33` is used when architecture-description adequacy is current. `E.23` consumes `NSTD.6` result rows only after object version, allowed change slice, protected trade-offs, cost and risk, and re-evaluation form are explicit. `B.4` is used only for an evolution claim over a narrative episteme, learning route, or other holon under repeated use; `G.11` handles currentness and refresh. Reopen when evaluated object kind, declared use, source pack, characteristic set, language-state profile, cue or backoff status, coarsening or explanation relation, precision-restoration result, epiplexity basis, value meanings, floor, evidence basis, allowed improvement slice, or low-value repair route changes. Support-map entry: open `Architecture and Narrative Work Bridge` when `NarrativeRenderingEpiplexity` is architecture-relevant or tied to `C.33`; open `Semiotic And Language-Precision Bridge` for language-state, coarsening, explanation, relation, or quality-word repairs; open `Source Use And Refresh Map` when evidence basis or source-currentness supports a value; open `DPF Precision Restoration And Owner Map` when a characteristic name risks becoming a new ontology.

### NSTD.6:End

## NSTD.7 - Automated Narrativization and Story Planning

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `AutomatedNarrativizationAdmissionCase@Context`, a DPF-local case record for generated or tool-assisted narrative output.

### NSTD.7:1 - Problem frame

Use this pattern when LLM, NLG, graph-to-text, data-to-text, story-planning, schema-governed generation, or search is used to produce or repair narrative renderings.

First useful move: split admitted source basis, generated carrier, source-to-narrative relation, structure capture or loss, correspondence, generation method, evaluation, evidence, assurance, and human admission responsibility.

What goes wrong if missed: generated fluency, schema compliance, controllability, or story-plan coherence becomes source authority.

What this buys: automation can help produce narrative candidates without admitting them as source-grounded renderings before checks.

### NSTD.7:2 - Problem

Automated systems can produce fluent, coherent-looking, and controllable-looking narratives that fail source grounding, plot or event consistency, schema constraints, source-return discipline, ethical boundary, or human interpretive responsibility. The issue is not whether generation is useful. It is what kind of object has been produced and what owner can use it.

### NSTD.7:3 - Forces

| Force | Tension |
| --- | --- |
| Fast generation vs admission | Tools can produce carriers quickly, but admission requires owner checks. |
| Schema control vs source truth | A valid story schema does not prove source fidelity. |
| Fluency vs correspondence | Fluent text can lose selected structure. |
| Automation vs responsibility | Human responsibility for source selection and admission remains explicit. |

### NSTD.7:4 - Solution

Use a kind-splitting record before evaluating or publishing generated output as a narrative rendering.

```text
AutomatedNarrativizationAdmissionCase@Context:
  sourceMaterialOrSourcePackRef:
  generatedCarrierRef:
  generationMethodOrMethodDescriptionRef:
  sourcePlanRef?:
  plotOrEventPlanRef?:
  schemaConstraintRefs?:
  c35AdmissionRef:
  narRelationRef:
  structureCaptureLossRef:
  correspondenceRef:
  evaluationRef:
  evidenceOwnerRefs?:
  assuranceOwnerRefs?:
  humanAdmissionResponsibilityRef:
  nonAdmissibleUse:
  repairOrRejectCondition:
```

Owner split:

| Claim kind | Owner |
| --- | --- |
| Source basis or source pack | `G.2`, `A.10`, `E.17.EFP` |
| Generated or discovered carrier admission | `C.35` |
| Source-to-narrative relation | `A.6.3.NAR` and this DPF |
| Structure capture and loss | `C.2.8` for reader-relative structural amount, applied through `NSTD.6`; `C.33` for architecture-description adequacy |
| Correspondence or preservation | `C.34` |
| Generation procedure | method or method-description owner, with source-pack grounding |
| Narrative rendering quality evaluation | `NSTD.6`, `A.19.ECS`, `C.16` |
| Repeated quality improvement | `E.22` when the quality question is not framed, then `E.23` using `NSTD.6` result rows and re-evaluation |
| Evidence | `A.10` |
| Assurance | `B.3` |
| Ethics, harm, bias, affected parties | `D.1` through `D.5` |
| Human responsibility for admission | role, assignment, work, decision, or governance owner as applicable |

Use a six-stage generated-narrative pipeline. Each stage may be lightweight, but it must not be skipped by a fluent final carrier.

| Stage | Required separation | Typical failure |
| --- | --- | --- |
| Source grounding | Admitted source basis, source pack, selected structures, source-currentness, and non-use boundary are named before generation. | The prompt is treated as admitted source basis; missing constraints are invented by the model. |
| Content planning | Source structures to include, omit, foreground, or protect are listed. | The generator chooses content implicitly and loses the denominator for epiplexity. |
| Discourse or sequence planning | Ordering rule, reveal rule, event plan, or learning route is stated. | Plausible prose hides wrong chronology, causality, proof order, or canon order. |
| Realization | Language state, style, compression, viewpoint, and engagement devices are selected as rendering choices. | Tone and fluency are mistaken for source fidelity. |
| Admission | `C.35` or an equivalent admission owner separates generated carrier from admitted narrative rendering. | Prompt output is used directly in teaching, publication, or decision support. |
| Evaluation and repair | `NSTD.6` evaluates the admitted rendering, and low values route repair through the smallest owner. | Regeneration continues until it "sounds better" without re-evaluation. |

For schema-governed generation, treat schema compliance as one input, not as admission. A schema can constrain scene fields, character roles, location, source refs, branch structure, or game-engine requirements. It cannot prove that selected source structures were preserved, that evidence is sufficient, or that human responsibility was assigned. Record schema constraints in the admission case, then test structural and semantic correspondence through `C.34` and `NSTD.6`.

For LLM-assisted analysis or theme generation, treat the model output as an interpretive aid. The worker must still own source selection, coding or theme acceptance, reflexive judgment, and downstream use. A generated theme, plot plan, or source plan may become admitted source basis for later narrative work only after admission and source-return conditions are explicit.

Use three probes before relying on automated output:

1. Source perturbation probe: remove or change one constraint in the admitted source basis and check whether the generated carrier changes in the expected way. If it does not, the output may not be grounded in the declared admitted source basis.
2. Structure recovery probe: ask a reader or evaluator to reconstruct selected source structures from the generated carrier without seeing the prompt. Low recovery returns to content planning or ordering.
3. Responsibility probe: ask who is accountable for source selection, admission, publication, and reliance. If the answer is "the model", the case is not admitted.

### NSTD.7:5 - Archetypal Grounding

#### Mature generated-narrative pipeline: graph-to-text case

An AI agent receives a source graph and produces a polished explanation. `NSTD.7` treats the output as a candidate carrier until the source plan, method, admission, and evaluation path are explicit.

```text
GeneratedNarrativePipelineRecord@GraphToTextTeaching:
  sourceMaterialOrSourcePackRef: concept graph with dependency, example, counterexample, and evidence links
  selectedSourceStructureRefs: prerequisite chain, contrast pairs, evidence-return points
  generatorOrMethodRef: LLM-assisted graph-to-text workflow
  sourcePlanRef: selected nodes and relations to preserve
  discourseOrStoryPlanRef: didactic dependency order with contrast reveal
  realizationCarrierRef: generated prose candidate
  admissionOwnerRef: `C.35`
  evaluationOwnerRef: `NSTD.6`
  humanResponsibilityOwnerRef: human narrator or teacher
  blockedOverread: fluent output is not source truth, admission, evidence, assurance, or improvement
  refreshCondition: source graph, generator behavior, schema, or evaluation result changes
```

Pipeline steps:

1. Source plan: select nodes, relations, losses, and source-return refs.
2. Discourse plan: choose ordering rule through `NSTD.2`.
3. Realization: generate wording.
4. Admission: decide whether the carrier-borne output can be admitted and evaluated as a narrative rendering through `C.35`.
5. Evaluation: evaluate through `NSTD.6`.
6. Repair: use `E.23` only after object version and changed slice are explicit.

#### Probe suite for generated narrative

| Probe | Question | Pass condition | Failure repair |
| --- | --- | --- | --- |
| Source perturbation | If one source relation changes, does the generated narrative change at the right place? | The affected sentence, order marker, or source-return link changes. | Recover source plan; do not rely on prompt fluency. |
| Structure recovery | Can a reader reconstruct selected source structure from the output? | Reader recovers nodes and relations needed for declared use and knows lost relations. | Add source-return markers or narrow declared use. |
| Responsibility | Who is responsible for source selection, admission, and publication? | Human or tool-owner roles are explicit; generated output has no authority by fluency. | Route to `C.35`, `A.10`, `B.3`, `E.17`, or ethics owners. |
| Schema-governance | Does schema constrain output or only decorate the prompt? | Missing source slots prevent admission or lower evaluation. | Make schema executable or mark it as weak guide. |
| Improvement evidence | Is the new variant better under `NSTD.6` rows? | Re-evaluation shows expected value movement without protected trade-off loss. | Keep variant as candidate and reframe through `E.22`/`E.23`. |

#### Before and after repair: generated seminar outline

Before:

> The generated outline sounds coherent and covers all important ideas, so it can be used as a DPF learning route.

Failure: source plan, admission, reconstruction task, and evaluation route are missing. "Covers all important ideas" is the model's hidden selection, not a source structure.

After:

> The generated outline is a candidate teaching publication carrier. Its source plan selects `EntityOfConcern`, forces, solution, relation exits, and improvement loop. Its discourse plan uses didactic prerequisite order. It is not a DPF pattern and not a public teaching route until `C.35` admits the carrier and `NSTD.8`/`NSTD.6` show that learners can reconstruct the source spine.

#### Mature generated-storycraft boundary

For the franchise continuation probe, a generated scene is especially risky because fluency and tone can hide source-pack violations. The DPF does not need to teach storycraft in full. It needs to require source-plan and responsibility discipline:

- source pack before scene;
- continuity and agency constraints before plot twist;
- private-use boundary before publication-like wording;
- perturbation test before claiming consistency;
- `NSTD.6` evaluation before improvement;
- human responsibility before any reliance-bearing use.

#### Calibration for generated narrative

| Value | Generated-carrier condition |
| --- | --- |
| `2` | Output is fluent, but source plan, admission, or evaluation route is missing. |
| `3` | Source plan exists, but probes or responsibility split are incomplete. |
| `4` | Source plan, discourse plan, admission, evaluation, and responsibility are explicit for declared use. |
| `5` | Perturbation, recovery, responsibility, and improvement probes pass across at least two heterogeneous generated cases. |

#### FPF owner teaching

`NSTD.7` is not a prompt-engineering trick. It applies FPF's carrier discipline to generated narrative: produced text is a carrier, not source truth; admission is separate from fluency; improvement needs evaluation rows; source currentness and generator behavior can decay. This is why `C.35`, `G.2`, `G.11`, `A.10`, `B.3`, `E.17`, `NSTD.6`, and `E.23` remain visible.

An LLM drafts a story-like explanation of FPF pattern use from source notes. `NSTD.7` records the prompt output as generated carrier, the source notes as admitted source basis, the prompt and generator as method-description context, and `C.35` as admission owner. Only after selected source structures, losses, and source-return condition are recovered may `NSTD.6` evaluate it as a narrative rendering.

A graph-to-text system turns an event graph into a match recap. The event graph, source timestamp, uncertainty markers, and official-result refresh route are admitted source basis for this rendering. The generated recap is a carrier. If the system adds causal explanations not in the graph, those claims are not admitted by graph-to-text success. Repair by lowering causal language, adding source return, or opening the evidence owner.

A game story-planning pipeline generates a branching scene. The schema may require objective, location, actors, traits, constraints, and available actions. `NSTD.7` treats those fields as method and source-plan support, not as proof of playable, coherent, or ethically acceptable narrative. Structural, semantic, executable, and human probes remain separate from fluency.

An LLM proposes themes from interview notes for qualitative narrative analysis. The generated theme list is not the researcher's interpretation by default. Human interpretive agency remains live: the researcher checks source excerpts, reflexive stance, alternative readings, and admissible use before any narrative rendering or report uses the generated material.

Use admission and rejection examples.

| Generated carrier | Admit as narrative rendering? | Reason |
| --- | --- | --- |
| A fluent summary from a prompt with no source refs. | No. | Admitted source basis and selected structure are not recoverable. |
| A graph-to-text candidate with source event ids, ordering rule, and explicit lost relations. | Candidate after `C.35`. | It can proceed to `NSTD.6`, but source recovery and relation strength still need value assignment. |
| A schema-valid RPG scene that ignores a required canon constraint. | No for source-faithful use. | Schema compliance does not establish correspondence. |
| A generated FPF seminar outline with source-spine refs and reconstruction tasks. | Candidate teaching publication carrier. | It remains outside DPF pattern bodies and needs `NSTD.8`/`NSTD.6`. |
| A generated metaphor for homotopy that helps intuition but lacks proof boundary. | Orientation cue only. | It may feed `A.16.1` or `NSTD.1`, not admitted rendering quality yet. |

When automated repair is used, preserve version identity. "Regenerate until better" destroys improvement evidence. Record the previous carrier, changed prompt or method, selected changed slice, expected value movement, protected trade-offs, and re-evaluation route. A generated variant can be more fluent and still worse on epiplexity, source return, or agency discipline.

Pipeline variants by source type:

| Source type | Content plan | Discourse or story plan | Admission danger | Evaluation focus |
| --- | --- | --- | --- | --- |
| Knowledge graph or event graph | Select nodes, edges, event ids, uncertainty, and omissions. | Choose traversal, grouping, and return links. | Treating graph coverage as semantic truth. | Epiplexity, ordering recoverability, relation strength. |
| Architecture source pack | Select structures, candidate trade-offs, decisions, telemetry, and residual exceptions. | Use decision-memory or trade-off route. | Treating generated explanation as architecture decision or assurance. | Structural-information capture, correspondence, source return. |
| Fictional canon or source pack | Select canon constraints, premise, agency, continuity, and non-use boundary. | Use causal plot plus reveal order. | Treating private generated scene as authorized continuation. | Continuity, character agency, causal support, rights boundary. |
| Teaching source spine | Select concepts, dependencies, examples, counterexamples, tasks. | Use didactic prerequisite route with repeated anchors. | Treating generated outline as source framework. | Reconstruction tasks, learning-route quality, source-return readiness. |
| Qualitative notes or interviews | Select excerpts, themes, alternative readings, reflexive stance. | Use analysis narrative with traceable source excerpts. | Treating generated theme as researcher judgment. | Human interpretive agency, source traceability, ethical boundary. |

If a pipeline variant requires a source type not covered by the current source pack, mark the case as a source-refresh trigger rather than silently generalizing. A graph-to-text claim, for example, may require a more specific graph-to-text source than a general NLG survey. A game narrative pipeline may need executable or playability probes that a plain text-generation source does not supply.

### NSTD.7:6 - Bias-Annotation

This pattern blocks generated-fluency admission drift: an LLM, NLG system, graph-to-text tool, schema, or story planner produces coherent text and that text is treated as admitted narrative rendering, evidence, assurance, or source authority. Repair by splitting generated carrier, admitted source basis, generation method, source-to-narrative relation, capture or loss, correspondence, evaluation, and human admission responsibility. Scope: DPF-local for automated narrativization; it does not replace `C.35` admission or source-pack owners.

### NSTD.7:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD7-1` | Generated carrier is separated from admitted source basis, selected source structure, admitted narrative rendering, evidence, and assurance. |
| `CC-NSTD7-2` | `C.35` admission is present before generated output feeds candidate, narrative, or teaching use. |
| `CC-NSTD7-3` | Source plan, plot or event plan, schema constraints, and generation method are named when relied on. |
| `CC-NSTD7-4` | Fluency, coherence, controllability, schema compliance, and story planning do not become authority, evidence, or admission. |
| `CC-NSTD7-5` | Human admission responsibility is explicit for source selection, interpretation, publication, and reliance-bearing use. |
| `CC-NSTD7-6` | A generated variant is not called an improvement unless an exact changed rendering version or changed slice is re-evaluated through `NSTD.6` and handed to `E.22` or `E.23` with protected trade-offs, cost and risk, and expected re-evaluation form. |

### NSTD.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluent generated output as narrative rendering | Carrier admission and source recovery are skipped. | Apply `C.35`, recover selected structure, then evaluate through `NSTD.6`. |
| Schema compliance as source fidelity | The story satisfies a schema but changes the selected source structure or a constraint in the admitted source basis. | Add `C.34` correspondence checks; use `C.2.8` through `NSTD.6` for selected structural recovery and loss, and `C.33` for architecture-description adequacy when that question is current. |
| Automation as responsibility holder | Tool output is treated as responsible admission. | Name human role assignment, method, work, decision, or governance owner. |
| Regeneration as improvement | The worker generates another fluent variant and treats it as quality movement. | Keep the variant as a generated carrier until admission, run `NSTD.6` on the changed rendering version, and use `E.22` or `E.23` only after the improvement question, protected trade-offs, cost and risk, and re-evaluation form are explicit. |

### NSTD.7:9 - Consequences

The benefit is productive automation without false authority. The cost is an admission step and repair or rejection route for generated carriers.

### NSTD.7:10 - Rationale

Modern NLG, LLM, graph-to-text, data-to-text, and story-planning practice makes generation useful but not self-justifying. FPF already has the owners needed for admission, source, structure, correspondence, evaluation, evidence, assurance, and work responsibility.

### NSTD.7:11 - SoTA-Echoing

#### Operational comparison against domain vocabulary

This DPF intentionally translates domain vocabulary into FPF owner work instead of importing it whole. When narratology says story, discourse, and presentation, this package asks: what source structure is selected, what order is chosen, what is foregrounded, and what source return remains? When cognitive narratology says event model, transportation, perspective, or memory, this package asks: which reconstruction target, engagement device, viewpoint, or evaluation characteristic is being changed? When NLG says content planning, discourse planning, and realization, this package asks: what is the source plan, what is the ordering rule, what is the generated carrier, and what admission and evaluation route owns it?

The practical consequence is a repair rule. If a domain term helps the worker choose or repair a narrative move, keep it as DPF vocabulary. If it starts carrying evidence, assurance, ethics, agency, publication, or Core ontology, route the claim to the FPF owner and state the blocked overread.

Gatt and Krahmer's `Survey of the State of the Art in Natural Language Generation` separates content planning, discourse planning, and realization; Alabdulkarim et al.'s "Automatic Story Generation: Challenges and Attempts" and Cardona-Rivera and Ware et al.'s "The Story So Far on Narrative Planning" keep story planning, plot structure, and consistency visible; Chakrabarty et al.'s "SceneCraft" and Rahman et al.'s "Game Knowledge Management System" show schema-governed and interactive generation pressures; Ma et al.'s "Text-to-Text Automatic Story Generation: A Survey" names coherence, consistency, diversity, controllability, datasets, and evaluation limits; Nguyen-Trung and Nguyen's "Narrative-Integrated Thematic Analysis" requires human interpretive agency. The DPF adopts these as owner-splitting requirements rather than as one automation pattern that grants trust.

Operational payload:

- From NLG, keep content planning, discourse planning, and realization separate. If a tool only returns final prose, reconstruct or reject the missing planning stages before reliance.
- From story-generation surveys, coherence and controllability are necessary but not sufficient. They must be connected to selected source structure, correspondence, admission, and declared use.
- From narrative planning, plot or event plan is a method artifact. It can guide generation but cannot become source truth.
- From schema-governed generation, schema fields can support repair and normalization, but schema compliance is not semantic fidelity or human evaluation.
- From interactive game generation, executable or playability probes may be needed when the narrative must function inside an engine or workflow; text fluency alone is the wrong evidence.
- From LLM-assisted qualitative analysis, human interpretive agency remains load-bearing. Generated themes, routes, or plans are aids until admitted by the responsible worker.

The practical consequence is that `NSTD.7` should make automated work more usable, not more magical. It protects speed by preventing hidden authority transfer from model output to source truth.

### NSTD.7:12 - Relations

Uses `G.2`, `C.35`, `A.6.3.NAR`, `C.2.8` for structural amount, `C.33` for architecture-description adequacy, `C.34`, `NSTD.6`, `A.19.ECS`, `C.16`, `E.22`, `E.23`, `A.10`, `B.3`, `D.1` through `D.5`, and `G.11`. `E.22`/`E.23` apply only after carrier admission and `NSTD.6` result rows exist; generation retries remain carrier candidates until re-evaluation. Reopen when admitted source basis, generator, method, schema, admission note, evaluation result, or generated-narrative SoTA changes. Support-map entry: open `Source Use And Refresh Map` when generation, NLG, story-planning, schema, or source-pack claims are relied on; open `DPF Precision Restoration And Owner Map` when generated source plan, plot plan, schema constraint, admission, correspondence, or responsibility words blur object kinds; open `Semiotic And Language-Precision Bridge` when prompt output changes language state, coarsening, cue, or quality wording.

### NSTD.7:End

## NSTD.8 - Learning-Route Narrative Rendering and Reconstruction Return

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `LearningNarrativeRoute@Context`, a source-returnable learning route plus its teaching or learning publication-carrier relation and evaluation route.

### NSTD.8:1 - Problem frame

Use this pattern when a complex source structure must be taught, explained, or learned through a narrative route, and the route must preserve enough structure for learners to reconstruct and apply it later. The governed object is the instructional route and its relation to source structure, not every explanation or reference publication. A publication used only for lookup or a professional decision need not become a course.

First useful move: name learner use, source-structure spine, learning-step ordering rule, source-return links, learner reconstruction tasks, and evaluation route. For an existing route, begin at one consequential transition: recover the current question, what the learner has already met, the contribution now needed and the support actually available there.

Architecture warning: the source corpus may have a good reference architecture and still make a bad learning route if copied directly into the course. Engineers often make a blocked topic route: one coherent module after another, with each topic concentrated in its own lesson. That can be excellent for a reference manual, API, or architecture description, but weak for learning when learners must discriminate neighboring cases, retrieve earlier distinctions, and transfer the structure under varied cues.

What goes wrong if missed: the explanation is engaging and memorable, but learners retain examples, slogans, analogies, and mood while losing architecture, relation records, proof obligations, pattern-use routes, source-return conditions, or improvement cycles.

What this buys: the learning publication carrier instantiates a declared narrative route over source structures, rather than becoming a hidden replacement for the source corpus.

### NSTD.8:2 - Problem

Teaching and learning routes expressed through publication carriers need sequence, examples, repetition, analogy, and motivation. But those choices can obscure source structure and make learners think the learning route is the framework, proof, or method itself. A DPF pattern should not contain the lesson, seminar script, or explainer text. It should govern how such a carrier is designed, tested, and repaired.

A common engineering failure is the reference-manual course. The course follows the module architecture of the source: first all of topic A, then all of topic B, then all of topic C, each with concentrated examples. Learners can follow each block locally, but later fail to choose the right pattern, distinguish nearby structures, remember earlier conditions, or transfer across domains. The repair is not to destroy the source architecture. Keep the source architecture as source return, then design a different learning-route architecture with deliberate interleaving, spaced retrieval, recurring anchors, and transfer tasks.

### NSTD.8:3 - Forces

| Force | Tension |
| --- | --- |
| Didactic route vs source corpus | Learning order may differ from publication order, proof order, architecture order, or framework order. |
| Source architecture vs learning-route architecture | High cohesion and low coupling can be good for the source corpus but harmful when copied as blocked topic instruction. |
| Local fluency vs durable discrimination | Blocked topic lessons feel orderly and efficient, while interleaving can feel harder but can improve later choice and transfer. |
| Coverage vs spaced retrieval | A course can cover every topic once and still leave learners unable to retrieve earlier structures when they matter later. |
| Engagement vs reconstruction | Learners may enjoy a story, analogy, example, or lesson without reconstructing source structure. |
| Carrier specificity vs pattern generality | Lessons, slides, scripts, worked examples, and exercises are needed, but pattern bodies must stay general. |
| Local teaching evidence vs package authority | Test-run evidence helps a learning route, but does not by itself make the package authoritative. |

### NSTD.8:4 - Solution

Create a learning route record and keep teaching materials outside pattern bodies.

```text
LearningNarrativeRoute@Context:
  learnerUse:
  sourceStructureSpineRefs:
  unfoldingStructureRefs?:
  demonstrativeSliceRefs?:
  sourceArchitectureRef?:
  learningRouteArchitectureRule:
  learningStepOrderingRule:
  interleavingPlanRefs?:
  spacingOrRetrievalScheduleRefs?:
  recurringAnchorRefs?:
  sourceReturnLinkRefs:
  learnerReconstructionTaskRefs:
  applicationTaskRefs?:
  engagementBoundaryRef?:
  narrativeRenderingQualityEvaluationRef:
  improvementLoopInputRef?:
  learningPublicationCarrierRefs:
  blockedTopicOverread?:
  nonAdmissibleUse:
  refreshCondition:
```

Actual lessons, seminar outlines, slides, exercises, scripts, session notes, recordings, and examples are separate teaching or test-run files. This pattern states how to design and evaluate them.

When the route teaches a constraint-governed unfolding structure, list that wider structure in `unfoldingStructureRefs?` and the taught path in `demonstrativeSliceRefs?`. The lesson may guide attention through one slice so learners can start working, but it must also teach what the slice omits and where the full structure is governed.

Build the route in eight design passes.

| Pass | Work product | Failure it prevents |
| --- | --- | --- |
| Source-spine pass | A short list of structures learners must later reconstruct or apply. | The lesson becomes an inspirational story or example chain. |
| Architecture-split pass | A split between source architecture and learning-route architecture. | The source module structure is copied as the course structure by default. |
| Ordering pass | A learning-step rule that may differ from monolith, proof, publication, or architecture order. | Learners confuse teaching order with source order. |
| Interleaving pass | Planned returns to earlier and neighboring source structures across sessions, examples, or exercises. | Learners learn each topic in isolation and cannot choose between similar owners later. |
| Spacing or retrieval pass | Delayed retrieval points for source-spine items, boundary cases, and repair moves. | Learners recognize material during the block but cannot retrieve it after delay. |
| Anchor pass | Terms, diagrams, questions or cases attached to the current question, needed distinction and next use, with support available at the point of reconstruction. | Learners remember episodes but lose the framework, or meet a new demand before its necessary relation is available. |
| Reconstruction pass | Tasks that ask learners to rebuild source structure, not only recall the narrative. | Satisfaction and memory replace practical competence. |
| Evaluation pass | `NSTD.6` rows for one route version and declared learner use. | Teaching tweaks are treated as improvement without evidence. |

Do not optimize the learning-route architecture for local neatness. A locally neat blocked route can be globally weak: it gives learners the answer key for the current block, so they do not practice selecting the right owner under mixed cues. Interleaving is useful when the learner must later discriminate similar patterns, methods, proof obligations, architecture structures, or source-return owners. Spacing is useful when the learner must still retrieve a structure after other material has intervened. Use them as design moves with declared learner use, not as decorative variety.

#### Check attachment and support at the next use

Inspect the relation between a block or learning aid and both its surrounding context and its later use. What question is active, what distinction or action does this example, image, explanation or exercise enable, why is it needed here, and where will its result be used? A question, worked example, caption, short transition or later payoff can carry that relation. There is no compulsory five-field form and no quota of connective phrases. A repeated word is not enough when the reader still cannot connect the two uses.

Then inspect the route prefix: the material encountered up to the point where a new reconstruction or action is required. Identify the relevant distinctions already introduced, necessary prerequisites expected of this audience, newly introduced objects or relations, still-open questions and the means available now. Ask the reader to use those means on the next task. A relation shown only much later cannot support the current action unless a usable return makes it available. An overview is useful when it exposes the needed relation, not merely because it lists topics.

Keep three different repair questions separate:

- A missing attachment: restore the relation between the active question, the block or aid and its next use; correct a wrong return or an unexplained visual edge.
- An unsupported new demand: supply the necessary contrast, map, worked operation, recap, accessible representation or introduction order before relying on that operation. Check the promised prerequisite and assistance first; do not simplify away needed subject structure.
- A deliberate preparatory attempt: let the learner try a bounded problem before the explanation when that serves the learning design, preserve the attempted alternatives, and use subsequent instruction to compare and resolve them. Difficulty or an incorrect first attempt is not by itself a material defect, but unresolved failure is not evidence of productive preparation.

Use a stable supported initial case when the learner needs it to build the distinction before mixed selection. Interleaving, spacing and retrieval serve the declared later task; they do not require every first encounter to mix unfamiliar alternatives. Conversely, making every block easy by naming its answer does not test later independent selection. Judge the actual point and contribution rather than choosing one universal order.

Preserve the first response before a cue supplies the distinction being tested. Report the allowed help, help actually used, source contribution and the reader's prior expertise. A teacher-supported correction may fulfil the declared arrangement while leaving independent first recognition untested. An expert's successful reconstruction does not erase a contrary report from a less-prepared reader. Use an appropriately scoped observation if that reader's difficulty can change the repair.

Structural reconstruction demand is not experienced cognitive load. NSTD.6 applies C.2.8 as NarrativeRenderingEpiplexity to the narrative account, expression and observer under the selected reading conditions; it is neither a quantity to maximize unconditionally nor a burden meter. A material inspection or agent walkthrough can locate a missing relation and available support, but claims about human burden, learning, retention or transfer need their own observations and conditions. For reported burden, identify the person, segment, timing and instrument.

Recheck the changed attachment, the affected prefix and its next task while preserving unaffected source and route results. If the intended reader already recovers the relation and completes that task with the declared support, density alone is not a reason to insert another aid. Use `E.23` for a worthwhile repair; shortening, added pictures or extra repetition are not improvements without a changed useful result and protected qualities.

Use reconstruction tasks at several depths.

| Task depth | Example task | What it tests |
| --- | --- | --- |
| Recognition | "Which pattern owns this problem?" | Whether the learner can see the entry condition. |
| Reconstruction | "Rebuild the pattern-use route from source basis, forces, solution, and exit." | Whether source structure survived the narrative. |
| Transfer | "Apply the same route to a different domain case." | Whether the learner learned structure rather than anecdote. |
| Boundary | "Name the non-use condition and owner to return to." | Whether blocked overreads were retained. |
| Repair | "Given a low `NSTD.6` row, choose the smallest repair route." | Whether improvement discipline survived the lesson. |

The learning route may deliberately use examples, stories, rhythm, repetition, and analogy. Those devices are not defects. They become defects only when learners can no longer reconstruct the source spine or source-return boundary. A vivid example can be kept if the route also includes source-return markers and reconstruction tasks.

Telemetry does not have to be heavy. For a small route, it can be a short learner task result, a failed reconstruction note, or an observed confusion pattern. For a reliance-bearing or repeated course, telemetry should include route version, learner role, source spine covered, task result, repair action, and refresh condition. Do not describe this as evolution unless the route is treated as a holon across repeated operation and `B.4` is actually live.

If the route is improved across runs, first evaluate the concrete route version through `NSTD.6`. Use `E.22` when learner value, floor, protected trade-offs, evidence, or result form are still underframed; use `E.23` to repair a declared changed slice such as source spine, learning-step order, reconstruction tasks, learning publication carrier, engagement boundary, or evaluation characteristic space. Use `G.11` when source currentness, learner telemetry, teaching-test evidence, generated practice, or FPF edition changes; use `B.4` only when making an evolution claim about the learning route as a holon across repeated operation.

### NSTD.8:5 - Archetypal Grounding

#### Mature learning-route case: FPF onboarding route

`NSTD.8` is not a seminar-script pattern. It governs the learning route that a seminar, slide deck, tutorial, or exercise sequence may instantiate.

```text
LearningNarrativeRoute@FPFOnboarding:
  learnerUse: new practitioner can apply one FPF pattern without treating it as a recipe
  sourceArchitectureRef: FPF pattern language and monolith and source pattern organization
  sourceSpineRefs:
    - `EntityOfConcern`
    - problem frame
    - forces
    - solution as condition-bound move
    - conformance and checking
    - neighboring exits
    - quality and improvement loop
  unfoldingStructureRefs: A.22.CGUS when the route teaches unfolding from source to next use
  demonstrativeSliceRefs: first pattern-use route through one selected project case
  learningRouteArchitectureRule: interleaved pattern-use route, not monolith-reference order
  learningStepOrder:
    - failed ordinary use
    - recover object of concern
    - read forces
    - choose solution move
    - check boundary and neighboring owner
    - repair one low-value result
  interleavingPlanRefs:
    - return to `EntityOfConcern` after forces, solution, and quality checks
    - mix adjacent owner-choice cases after each new pattern
    - revisit source-return boundary in examples from at least two domains
  spacingOrRetrievalScheduleRefs:
    - short delayed retrieval at the start of the next session
    - later mixed owner-choice task after intervening material
    - final transfer task with no block label
  reconstructionTasks:
    - name the source pattern section behind each story beat
    - choose the governing pattern for a new case
    - state one source-return condition
  engagementBoundaryRef: failure story is an archetype, not evidence
  evaluationRouteRef: `NSTD.6` learning-route rows
  improvementLoopInputRef: `E.23` only after low-value rows exist
```

In this onboarding route, the opening failed use may be preparation rather than a failed capability assessment. The subsequent recovery of the object of concern must work with the attempted alternatives: show which object the next move governs and why the tempting alternative does not answer that question. Before the later neighbor-choice task, inspect whether those neighboring entries and their distinguishing condition are already available. If not, introduce the contrast or provide an accessible source return; merely adding another unlabeled failure would not supply it. If the entries are available, the mixed case can test their selection instead of prompting the answer.

A later diagram or recap should connect that choice to the next actual use. A wrong figure return calls for correcting the attachment, not automatically redesigning the entire course. After the repair, ask the reader to recover that relation and use it under the declared support. This is a design and checking example, not an observed learning gain.

An actual seminar file can contain jokes, slides, timing, exercises, and examples. The DPF pattern body does not. It tells the route designer what must survive in any carrier-borne teaching material: source spine, ordering rule, reconstruction tasks, source returns, engagement boundary, evaluation, and repair.

#### Mature learning-route case: repair a blocked engineering course

An engineering team wants a course on architecture patterns. Their first outline looks clean:

```text
Lesson 1: all source-structure intake.
Lesson 2: all ordering rules.
Lesson 3: all viewpoint and agency.
Lesson 4: all engagement.
Lesson 5: all evaluation.
```

This is a reference architecture for topics, not yet a learning architecture. It has high local coherence, but it tells learners which kind of problem they are solving inside each block. The hard work appears later: choosing whether a new failure is source selection, ordering, viewpoint, engagement, generated-carrier admission, evidence, assurance, or refresh.

Repair the route:

```text
LearningNarrativeRoute@ArchitecturePatternCourse:
  learnerUse: engineer chooses and repairs the right pattern under mixed project situations
  sourceArchitectureRef: topic map and source pattern bodies
  sourceSpineRefs:
    - selected source structure
    - ordering rule
    - viewpoint and agency split
    - engagement boundary
    - narrative rendering quality row
    - source-return and owner routing
  learningRouteArchitectureRule: spaced interleaving around recurring project cases
  learningStepOrder:
    - one motivating project failure
    - source-selection repair
    - different project failure requiring ordering repair
    - return to first failure and add viewpoint risk
    - mixed owner-choice exercise
    - delayed retrieval of source-return boundaries
    - final transfer to an unseen case
  interleavingPlanRefs:
    - every session mixes at least one current pattern with one earlier pattern
    - adjacent failure modes are compared side by side
    - examples rotate across FPF seminar, architecture explanation, homotopy explanation, generated carrier, and live commentary
  spacingOrRetrievalScheduleRefs:
    - start each session with a no-label retrieval task from a prior session
    - return to `EntityOfConcern`, source-return, and owner-routing at increasing delays
    - require one late repair of an old low-value row after new material intervenes
  blockedTopicOverread: a clean topic block is not evidence of durable pattern choice
  evaluationRouteRef: `NSTD.6` rows for transfer, source return, and learner reconstruction
```

The repaired route still preserves the source architecture. It simply refuses to treat that architecture as the course order. The learner sees a pattern, uses it, leaves it, then returns under a different cue. That is the point: source modules can stay modular while the learning route deliberately crosses module boundaries.

#### Mature learning-route case: homotopy explanation

```text
LearningNarrativeRoute@HomotopyIntro:
  learnerUse: learner distinguishes intuitive deformation picture from formal definition and proof boundary
  sourceSpineRefs:
    - topological space
    - path
    - homotopy relation under constraints
    - invariant
    - example and counterexample
    - proof-status return
  learningStepOrder:
    - image cue
    - constraint marker
    - formal definition return
    - example
    - counterexample
    - reconstruction task
  reconstructionTasks:
    - mark where analogy stops
    - state which deformations are not allowed
    - return one claim to formal source
  engagementBoundaryRef: vivid image cannot replace definition
  evaluationRouteRef: `NSTD.6` rows for ordering, language-state precision, and source return
```

If learners can retell the loop picture but cannot state the constraint boundary, the route is not successful. Add examples only after the source spine and reconstruction task are repaired.

#### Mature learning-route case: narrative DPF teaching route

A short course on this DPF may use the three probes: FPF seminar, franchise continuation, and homotopy explanation, with live commentary as a fourth transfer case. The route succeeds only if learners can see the same pattern set working across different domains:

| Step | Probe | Pattern focus | Transfer question |
| --- | --- | --- | --- |
| 1 | FPF seminar | `NSTD.1`, `NSTD.8` | What source spine must survive a learning route? |
| 2 | Franchise continuation | `NSTD.1`, `NSTD.2`, `NSTD.3`, `NSTD.7` | What counts as source pack and event support when facts are prospective or fictional? |
| 3 | Homotopy explanation | `NSTD.2`, `NSTD.5`, `NSTD.6` | Where does analogy stop and formal source return begin? |
| 4 | Live commentary | `NSTD.3`, `NSTD.6`, `G.11` | Which claims are provisional until later source return? |

The transfer question is the actual teaching test. Remembering case names is not learning. The learner must choose the live pattern and repair the failure in a new situation.

#### Before and after repair: teaching material inside pattern body

Before:

> This pattern should include a full seminar script so readers can immediately teach narrativization.

Failure: teaching-material carrier and DPF pattern body are collapsed. The carrier-borne material will age, distract, and hide the general route.

After:

> This pattern defines the learning route. Seminar scripts, slides, exercises, examples, recordings, and session notes stay in teaching publication carriers. The route records learner use, source spine, ordering rule, reconstruction tasks, evaluation, and refresh condition. A seminar publication carrier may instantiate it, and `NSTD.6` can evaluate the route version.

#### Calibration for learning routes

| Value | Learning-route condition |
| --- | --- |
| `2` | The route is engaging or organized, but source spine and reconstruction tasks are weak. |
| `3` | Source spine and order exist, but learner tasks mostly check recall or enthusiasm. |
| `4` | Learners reconstruct source relations, source returns, and boundary conditions for one declared use, including after at least one delay or mixed case. |
| `5` | Learners transfer the route to a heterogeneous case and repair a low-value row after interleaved and spaced practice, without confusing carrier, admitted source basis, and pattern authority. |

#### FPF owner teaching

`NSTD.8` connects narrative work to FPF learning without making education a local mythology. It reuses `E.11` for entry, `E.17` for publication carriers, `E.17.AUD` for audience units, `NSTD.5` for motivation, `NSTD.6` for evaluation, `E.22`/`E.23` for improvement, and `G.11` for refresh. The route may be small for a one-off explanation or versioned for a course. The source-return discipline is the same.

An FPF learning route, such as a seminar series or tutorial sequence, teaches the framework across several steps. The source-structure spine includes EntityOfConcern discipline, relation precision, pattern bodies, DPF authoring, architecture synthesis, evaluation, improvement loops, and source-return discipline. The learning order is didactic, not proof of FPF architecture. Learner tasks ask participants to reconstruct one pattern-use route from source basis and selected source structure, not only repeat a story or slogan.

A homotopy mini-course may start with pictures and deformation stories, but the source spine includes definitions, examples, counterexamples, theorem prerequisites, and proof-status boundaries. A reconstruction task might ask the learner to explain where an analogy stops and to return to a formal statement. If learners can retell the image but cannot mark the formal boundary, `NSTD.8` repairs the source spine and tasks before adding more examples.

A DPF onboarding route may teach narrative rendering through three cases: FPF seminar, franchise storycraft, and live commentary. The route is successful only if learners can reconstruct why all three open `NSTD.1`, why different patterns become live later, and why `NSTD.6` evaluates a declared rendering version rather than a general story. The test is transfer across cases, not recall of the case names.

A generated teaching route must pass through `NSTD.7` before it is trusted. Slides or examples produced by an LLM remain candidate carrier-borne material until the source spine, ordering rule, admission status, and reconstruction tasks are explicit. The learning route may use generated material, but the DPF pattern body does not absorb the generated lesson.

Use route versioning when teaching is repeated.

```text
LearningNarrativeRouteVersion@Context:
  routeRef:
  sourceSpineVersionRef:
  learnerRoleRef:
  learningStepOrderingRule:
  carrierRefs:
  reconstructionTaskRefs:
  evaluationResultRef:
  observedConfusionOrTelemetryRefs?:
  changedSliceSincePreviousVersion?:
  refreshCondition:
```

Versioning is not bureaucracy. It prevents the common failure where a teacher changes slides, examples, or order and then claims the course improved because it felt smoother. Improvement requires a route version, a declared changed slice, and re-evaluation. If the source spine changes because FPF changed, that is refresh through `G.11`, not merely local teaching preference.

Use a three-column lesson plan before writing materials.

| Source-spine item | Narrative or teaching move | Interleaving or spacing move |
| --- | --- | --- |
| Pattern entry condition | Recognition story, contrast case, or failed-use story. | Return after two other pattern cases and ask for owner choice without a label. |
| Forces | Tension sequence, stakeholder conflict, or trade-off map. | Compare with a different pattern's forces in a mixed exercise. |
| Solution move | Demonstration, guided reconstruction, or worked slice. | Reuse the same project case later with a different repair owner. |
| Boundary and non-use | Counterexample, wrong-owner case, or blocked overread. | Start a later session with a delayed boundary retrieval question. |
| Relations | Neighboring-pattern exit exercise. | Interleave adjacent exits so the learner must discriminate them. |
| Quality and improvement | Low-value row and repair exercise. | Revisit an old low-value row after new material and require a changed-slice repair. |

The left column is the source spine and must remain source-returnable. The middle column is the immediate publication-carrier design. The right column is the learning-route architecture: how the route crosses topic boundaries and returns over time. If the middle column becomes the only remembered structure, the route has failed even if the lesson was popular. If the right column is empty in a multi-session course, the route is probably a reference manual wearing course clothes.

Learning-route recipes:

| Route type | Source spine | Narrative devices allowed | Reconstruction evidence |
| --- | --- | --- | --- |
| FPF onboarding route | Pattern entry, EoC, forces, solution, relations, checks, improvement loop. | Practitioner story, failed-use contrast, recurring source-return prompt. | Learner selects correct owner and reconstructs one pattern-use route. |
| Mathematical explanation route | Definitions, examples, theorem prerequisites, proof-status boundaries. | Analogy, diagram story, dependency sequence, counterexample. | Learner marks where analogy stops and returns to formal statement. |
| Architecture explanation route | Candidate structures, characteristics, decisions, trade-offs, telemetry. | Trade-off story, viewpoint over stakeholder role, decision-memory path. | Learner separates architecture description, decision, realized structure, and telemetry. |
| Generated teaching route | Source spine plus generated carrier admission route. | Generated examples or slides after `C.35` and source recovery. | Learner tasks plus admission and evaluation record show the carrier-borne material did not replace admitted source basis or selected source structure. |
| Live debrief route | Event record, provisional interpretation, official correction, source return. | Recap story, tension order, role viewpoint. | Learner distinguishes observation, inference, prediction, and official update. |

For a short one-off teaching note, the route can be tiny: one source-spine item, one ordering rule, one reconstruction question, one source-return link. For a repeated seminar or course, the route should have versioned carriers, task results, and low-value repairs. The size changes; the source-return discipline does not.

Do not use popularity as learning evidence. Attendance, satisfaction, applause, or "people liked the story" may be engagement telemetry, but it is not reconstruction evidence. Reconstruction evidence asks whether learners can rebuild the source relation, apply it to a new case, name a boundary, or choose a repair.

### NSTD.8:6 - Bias-Annotation

This pattern blocks learning-route-as-framework drift: a lesson sequence, seminar sequence, slide deck, story arc, exercise set, analogy chain, or memorable teaching case is treated as the source framework. Repair by naming learner use, source-structure spine, learning-step ordering rule, reconstruction tasks, source-return links, learning publication-carrier refs, engagement boundary, and evaluation route. Scope: DPF-local for learning narrative routes; it does not admit teaching material into pattern bodies.

It also blocks blocked-topic architecture drift: the source corpus is modular, so the course is made modular in the same way. Repair by separating source architecture from learning-route architecture. Keep the source modules for source return, then add interleaving and spacing when the learner must later discriminate, retrieve, or transfer structures across topic boundaries.

### NSTD.8:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD8-1` | Learner use and source-structure spine are named. |
| `CC-NSTD8-2` | Learning-step ordering rule and source-return links are explicit. |
| `CC-NSTD8-3` | Learner reconstruction tasks test source structure, not only recall of narrative highlights. |
| `CC-NSTD8-4` | Actual teaching materials remain outside DPF pattern bodies. |
| `CC-NSTD8-5` | Evaluation uses `NSTD.6`; repeated improvement uses `E.22` when the quality question is underframed and `E.23` only after exact route version, changed slice, protected trade-offs, cost and risk, and re-evaluation form are explicit. |
| `CC-NSTD8-6` | For multi-session or transfer-bearing routes, source architecture is separated from learning-route architecture, and any blocked topic order is either justified for the learner use or repaired with interleaving, spacing, delayed retrieval, and mixed cases. |
| `CC-NSTD8-7` | Material attachments and consequential prefixes connect the current question, available structure/support and next use; missing relations, unsupported demands and deliberate preparatory attempts receive different repairs or continuation. |
| `CC-NSTD8-8` | First and helped responses, source contribution, prior expertise and human learning or burden claims retain their own evidence boundaries; structural density is not treated as observed cognitive load. |

### NSTD.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Learning route as source structure | Lesson sequence, seminar order, analogy chain, or explainer order is treated as framework architecture, proof order, or source structure. | Declare learning-step ordering rule and source-return links. |
| Reference manual as course | The source topic map is copied into lessons one topic at a time. | Keep the topic map as source architecture; design a learning-route architecture with interleaved and spaced retrieval. |
| Blocked practice fluency | Learners perform well inside each topic block because the block label gives away the owner. | Add mixed owner-choice cases and delayed no-label retrieval before claiming transfer. |
| Materials inside pattern body | Slides or exercises are inserted into DPF patterns. | Move them to teaching publication-carrier files and reference only the carrier relation. |
| Recall as reconstruction | Learners remember examples but cannot use patterns. | Add reconstruction and application tasks; evaluate through `NSTD.6`. |
| Fluent blocks without a usable connection | Each paragraph reads well, but the current question, aid or later use cannot be related. | Inspect both endpoints and the affected prefix; restore the missing relation or usable return, then repeat the next task. |
| Difficulty judged without its teaching function | Every hard transition is compressed, or every unsuccessful attempt is called productive. | Separate an unsupported demand from deliberate preparation; provide the missing support or make subsequent instruction resolve the attempted alternatives. |
| Teaching tweak as evolution | A revised slide, example, or prompt is described as evolved route quality without telemetry and re-evaluation. | Treat the tweak as an `E.23` changed slice after `NSTD.6`; use `G.11` for refresh and reserve `B.4` for actual evolution claims over the route across operation. |

### NSTD.8:9 - Consequences

The benefit is a teachable path that stays source-returnable and can be improved without confusing entertainment with understanding. The cost is maintaining separate teaching publication carriers and evaluation evidence.

### NSTD.8:10 - Rationale

Didactic primacy requires examples, analogies, routes, interleaving, and spaced returns. Ontological discipline requires that learning publication carriers do not become the source framework. This pattern holds both: the route is designed, tested, and refreshed without entering pattern bodies as teaching content.

The architectural lesson is counterintuitive for engineers. In a source corpus, strong modularity often helps: each pattern or topic has its own boundary, internal coherence, and relation exits. In a learning route, copying that modularity can hurt. Learners need to meet similar structures under varied cues, return to earlier distinctions after delay, and practice choosing the right owner when the block label is gone. Therefore the course architecture is a transformation over the source architecture, not a mirror of it.

### NSTD.8:11 - SoTA-Echoing

Mengelkamp et al.'s "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" makes study goals and metacomprehension risk visible; Georgiou et al.'s "Large-scale study of human memory for meaningful narratives" shows that long narratives can be remembered as gist and sequence rather than source detail; Hoffmann's "The Tensions of Scientific Storytelling" supplies a science-storytelling example where unresolved tension and source return matter. Dunlosky et al.'s "Improving Students' Learning With Effective Learning Techniques" rates practice testing and distributed practice as high-utility techniques and treats interleaved practice as promising for appropriate situations. Rohrer and Taylor's "The shuffling of mathematics problems improves learning" directly shows the risk of standard blocked textbook practice and the benefit of spaced and mixed practice in mathematics problems. Kang's "Spaced Repetition Promotes Efficient and Effective Learning" gives a policy-level synthesis: spacing repeated encounters with material improves long-term learning and can be combined with tests. `NSTD.8` retains the Dunlosky, Rohrer–Taylor and Kang contributions as historical anchors for spacing and interleaving questions. The bounded source contributions here inform learning-route design, reconstruction and source return, not a complete pedagogy doctrine.

For the attachment and prefix-support work, [Noetel et al. (2022)](https://journals.sagepub.com/doi/10.3102/00346543211052329) supports mechanism-specific attention to signaling, correspondence and pacing rather than a rule to add pictures everywhere. [Sinha and Kapur (2021)](https://journals.sagepub.com/doi/abs/10.3102/00346543211019105) supports distinguishing problem solving followed by instruction from unsupported failure; its conditional, largely mathematics/physics evidence does not make all difficulty productive. [Wesenberg et al. (2025)](https://doi.org/10.1016/j.cedpsych.2024.102328) motivates checking whether a worked example also permits a consequentially wrong rule; the studied brief units do not establish a universal order for long routes. [Krieglstein et al. (2025)](https://doi.org/10.1007/s10648-024-09980-0) shows why retrospective load reports need an explicit timing and segment: the reported primacy effect concerns self-report in the studied setting, not a conversion from source-structure density to human burden. These contributions qualify the choice of support and the inference from a reader response; none validates this entire route method or its ordinal values.

Operational payload:

- From reading-goal work, declare the learner use before the lesson route. A route for curiosity, exam preparation, professional use, or framework authoring needs different reconstruction tasks.
- From metacomprehension risk, ask learners to reconstruct or apply source structure, not only rate whether they understood.
- From memory work, long routes need anchors and returns. Repetition should protect source spine rather than repeat slogans.
- From spacing work, one concentrated encounter with a topic is not enough for durable learning. Put delayed retrieval points into the route and evaluate whether earlier structures survive intervening material.
- From interleaving work, blocked topic practice can hide the real choice problem. Mix adjacent owners, cases, or problem types when the learner must later decide which structure applies.
- From engineering architecture discipline, preserve the source architecture for source return but do not copy it as the learning-route architecture unless the learner use really is reference lookup.
- From scientific storytelling, unresolved tension can be taught honestly. The route can preserve open questions instead of pretending closure.
- From FPF improvement-loop patterns, teaching improvement needs route versions, low-value findings, changed slices, and re-evaluation.

The practical consequence is that `NSTD.8` is not a course-design doctrine. It is a source-return and learning-route architecture discipline for narrative learning routes and their publication carriers. It tells when a teaching story still serves the source framework, when it has become its own misleading object, and when a tidy blocked course should be repaired into interleaved and spaced learning.

### NSTD.8:12 - Relations

Uses `A.6.3.NAR`, `E.6`, `E.11`, `E.17`, `E.17.AUD`, `NSTD.1`, `NSTD.2`, `NSTD.5`, `NSTD.6`, `E.21`, `E.22`, `E.23`, `B.4`, and `G.11`. `NSTD.5` bounds motivation and interest; `NSTD.6` evaluates one route version; `E.22` frames under-specified quality questions; `E.23` repairs a declared changed slice; `G.11` refreshes source, telemetry, edition, or practice currentness; `B.4` is only for evolution claims over the learning route. Reopen when learner use, source spine, source architecture, learning-route architecture, interleaving plan, spacing or retrieval schedule, teaching-test evidence, source currentness, edition, or evaluation result changes. Support-map entry: open `Architecture and Narrative Work Bridge` when the learning route narrates architecture, copies source architecture as course architecture, uses views, source spine, or actual-structure feedback; open `Semiotic And Language-Precision Bridge` when didactic coarsening, cue or backoff, explanation, style, or language-state choice matters; open `Source Use And Refresh Map` when teaching, memory, cognition, interleaving, spacing, or learner-test source support changes; use the refresh route when learner telemetry changes.

### NSTD.8:End

## Heterogeneous Acceptance Cases

These cases test whether the DPF handles several narrative domains without importing their materials into pattern bodies.

Each case below must have a construction route before `NSTD.6` evaluation. A pass is not "someone wrote a good narrative and the checklist liked it"; a pass is that the pattern set tells the worker how to move from source structures to a draftable narrative route, then how to evaluate and repair it.

### Case A - FPF Learning Route Probe With Seminar Carrier

Use: multi-session or slide-deck teaching publication carrier for FPF. Actual slides, scripts, exercises, and session notes stay in separate teaching files.

Patterns opened: `NSTD.1`, `NSTD.2`, `NSTD.3`, `NSTD.5`, `NSTD.6`, `NSTD.8`.

Source structures that must survive: pattern body structure, EntityOfConcern discipline, relation owner routing, source-return conditions, quality evaluation, DPF relation records, and improvement loop.

Temporal posture and rendering mediation mode: prospective planned learning route over current FPF source structures; direct source-structure mode unless an architecture-of-FPF explanation is explicitly opened as architecture-mediated support.

Ordering rule: didactic prerequisite order, with explicit divergence from monolith order when helpful.

Construction route:

1. `NSTD.1`: select the learner use first, then choose the source-structure spine: `EntityOfConcern`, relation owner routing, pattern body shape, source return, DPF package relation, quality evaluation, and improvement loop.
2. `NSTD.2`: build a didactic prerequisite sequence from that spine; state where it diverges from monolith order and what this hides.
3. `NSTD.3`: turn each session into a reconstruction target: after the session, the learner should be able to reconstruct one pattern-use route from source basis and selected source structure, not only repeat the teaching story.
4. `NSTD.5`: add motivation devices only where they protect attention without replacing source return; slogans and examples remain subordinate to reconstructable source structure.
5. `NSTD.8`: create the learning route record with recurring anchors, source-return links, reconstruction tasks, and application tasks before writing slides or scripts.
6. `NSTD.6`: evaluate the route once the above source and use basis is recoverable. A missing structural-amount basis returns to source-spine selection; a demonstrated relation loss calls for repair of the selection, expression or usable source return through the relevant NSTD method before style polish. Compare any numerical amount only at its stated scale and conditions.

Intentionally lost or deferred: full monolith detail, all neighboring patterns, all source-pack rows, and advanced formal variants. These return through source links.

Owner routing: teaching publication-carrier and audience-unit claims to `E.17` and `E.17.AUD`; evaluation to `NSTD.6`; source claims to `G.2`; evidence to `A.10`; refresh to `G.11`.

Low `NSTD.6` repair: if learners enjoy sessions but cannot reconstruct pattern use, repair `NSTD.2`, `NSTD.3`, and `NSTD.8` before changing only style.

### Case B - Franchise Continuation Storycraft

Use: continuation-style narrative planning for a well-known space-opera franchise such as `Star Wars`, used only as storycraft and source-pack test material. This is not unauthorized publication guidance and does not include generated sequel content.

Patterns opened: `NSTD.1`, `NSTD.2`, `NSTD.3`, `NSTD.4`, `NSTD.5`, `NSTD.6`, `NSTD.7` when generation is used.

Source structures that must survive: canon constraints, continuity, premise and theme, character agency, causal plot structure, viewpoint, stakes, and source-return to admitted canon references.

Temporal posture and rendering mediation mode: prospective fictional source structure over an admitted canon or local source pack; direct source-structure mode unless architecture of a fictional organization or technology is separately opened as a source structure.

Ordering rule: plot-causal order with possible reveal order; reveal order must not hide causal support.

Construction route:

1. `NSTD.1`: create a bounded source pack for private storycraft testing: admitted canon references, continuity constraints, premise and theme constraints, character-agency constraints, and non-admissible publication use.
2. `NSTD.2`: choose plot-causal order and separately mark reveal order; every reveal must point back to a causal or continuity support relation.
3. `NSTD.3`: build an event or mechanism support map for the proposed plot: initiating condition, constraint, conflict, action, consequence, update, and unresolved tension.
4. `NSTD.4`: choose viewpoint and protagonist function, then split narrative agency from role, responsibility, capability, rights, or moral permission.
5. `NSTD.5`: use stakes, curiosity, and identification only after source constraints are protected; fan-service is allowed only when it performs a plot or source-return function.
6. `NSTD.7`: if generated outputs are used, treat them as carriers to admit and repair, not as authorized sequel content.
7. `NSTD.6`: evaluate continuity, character agency, causal plot support, viewpoint discipline, and `NarrativeRenderingEpiplexity`; repair structure before increasing drama.

Intentionally lost or deferred: exhaustive canon, production rights, fan-service catalogue, and publication permission. These are outside this DPF case.

Owner routing: canon source pack to `G.2`; generated outputs to `C.35` and `NSTD.7`; agency and responsibility wording to `NSTD.4`, `A.13`, `A.2`, and ethics owners when needed; publication and rights claims outside this DPF.

Low `NSTD.6` repair: continuity drift, premise mismatch, character-agency collapse, escalation without causal structure, fan-service replacing plot function, viewpoint confusion, or stakes without source return repair through `NSTD.1` through `NSTD.4`, not by adding more dramatic prose.

### Case C - Homotopy Theory Explanation

Use: graph-heavy and structure-heavy mathematical theory rendered into sequential explanatory narrative for learners.

Patterns opened: `NSTD.1`, `NSTD.2`, `NSTD.3`, `NSTD.5`, `NSTD.6`, and `NSTD.8` if taught as a series.

Source structures that must survive: definitions, dependency order, examples, counterexamples, proof-status boundaries, theorem prerequisites, and source return to formal statements.

Temporal posture and rendering mediation mode: retrospective or atemporal explanatory route over existing mathematical source structures; direct source-structure mode unless a teaching architecture or knowledge-graph architecture is explicitly used as mediation.

Ordering rule: didactic dependency order with source-return to formal proof order.

Construction route:

1. `NSTD.1`: select the learner use and source structures: definitions, dependency graph, examples, counterexamples, theorem prerequisites, proof-status boundaries, and formal-source return.
2. `NSTD.2`: choose didactic dependency order; explicitly mark where it differs from formal proof order, historical order, or publication order.
3. `NSTD.3`: define the reconstruction target for each step: what the learner must be able to state, distinguish, use in an example, or return to as formal proof status.
4. `NSTD.5`: use analogy, curiosity, or visual intuition only after the formal boundary is named; an analogy may motivate but may not become the theorem.
5. `NSTD.8`: if the explanation becomes a series, turn dependencies into session anchors and reconstruction tasks rather than a sequence of entertaining analogies.
6. `NSTD.6`: evaluate whether learners can recover definitions, dependency order, example boundaries, proof-status boundaries, and source-return points; low values repair source selection and ordering before adding more metaphor.

Intentionally lost or deferred: full proof detail, every lemma, historical order, and advanced generalizations not needed for declared learner use.

Owner routing: mathematical-lens claims to `C.29` when used; evidence or proof-status claims to their proof or source owner and `A.10` when evidence is claimed; publication-unit and audience claims to `E.17`.

Low `NSTD.6` repair: if learners can retell an analogy but cannot state definitions, dependency order, example boundaries, or proof status, repair `NSTD.1`, `NSTD.2`, and `NSTD.3`; do not raise engagement alone.

### Case D - Live Event Commentary

Use: live commentary for an unfolding football match or analogous event stream, used for listener orientation and later review only under source-return conditions.

Patterns opened: `NSTD.1`, `NSTD.2`, `NSTD.3`, `NSTD.4`, `NSTD.5`, and `NSTD.6`.

Source structures that must survive: score state, event sequence, possession or control changes, tactical or situational structure, actor roles, uncertainty, provisional interpretation, and return to official result, telemetry, statistics, or recording.

Temporal posture and rendering mediation mode: live unfolding event stream; direct source-structure mode. Architecture-mediated mode opens only if the commentary is explicitly about structure of a team, venue, broadcast system, or other holon and uses architecture descriptions as admitted source basis.

Ordering rule: live event order with explicit prediction and uncertainty markers; later recap may use causal or tension order but must not erase which claims were provisional during the live event.

Construction route:

1. `NSTD.1`: name listener use, live temporal posture, intended commentator Work role, any actual performer and role assignment, load-bearing commentator voice or viewpoint, event-source owner, provisional interpretation boundary, and source-return route.
2. `NSTD.2`: follow live event order while marking when the sequence is observation, inference, tactical interpretation, or prediction.
3. `NSTD.3`: preserve event and state-update support so listeners can reconstruct what changed, who acted, and what remains uncertain.
4. `NSTD.4`: keep viewpoint and agency wording from assigning responsibility, intention, or capability beyond the observable or sourced basis.
5. `NSTD.5`: use tension and suspense only as attention support; it cannot make predictions, disputed rulings, or emotional framing into settled evidence.
6. `NSTD.6`: evaluate whether the listener can distinguish observed event, provisional interpretation, uncertainty, and source-return obligation.

Intentionally lost or deferred: full official statistics, all off-camera events, post-match medical or disciplinary facts, and later tactical analysis. These return through official source refs, telemetry, or recording.

Owner routing: official facts to event source owners and evidence owners when asserted; publication or broadcast carrier to publication owners; ethics or harm framing to `D.1` through `D.5`; refresh to `G.11` when official record or telemetry changes.

Low `NSTD.6` repair: if listeners remember drama but cannot distinguish observed event from commentator inference or later official correction, repair `NSTD.1`, `NSTD.2`, `NSTD.3`, and `NSTD.4` before increasing engagement.

## Support Maps

These maps are reference material reached from pattern work, not a second reading sequence before the pattern bodies. Use the pattern bodies first. Open a map when a `Relations` section, low-value repair action, source-return condition, or owner-routing doubt points to it.

Fast entry: `NSTD.1` and `NSTD.2` send architecture-mediated structure and rendering-mediation questions to the architecture bridge; `NSTD.4` through `NSTD.6` send language-state, quality wording, viewpoint, engagement, and epiplexity precision questions to the semiotic and precision maps; `NSTD.7` sends generated-carrier, source-basis, and admission questions to source use and precision maps; `NSTD.8` sends teaching-route and learner-reconstruction questions to the architecture bridge, semiotic bridge, and refresh route when those owners become live.

## Architecture and Narrative Work Bridge

Use this bridge when narrative-language work is doing architecture-like structural work under different words. The point is not to turn every narrator into an architect or every architecture record into prose. The point is to let narrators borrow FPF architecture discipline when they select structures, choose viewpoints, decide what to foreground, and later test whether readers recovered the intended structure.

| Architecture-work locus | Narrative-studies wording that may name the same ontological work | FPF use in this DPF |
| --- | --- | --- |
| architecture-relevant problem pressure in `C.32.P2S` | narrative problem, communicative pressure, audience confusion, motivation gap, future-scenario need, story problem | Use `NSTD.1` to name reader or listener use and source-structure selection rationale; use `C.32.P2S` only when the pressure is genuinely about holon architecture carry-through. |
| selected structure or unknown structure | admitted source basis, storyworld, event field, canon constraint, mechanism, proof dependency, thematic relation, situation structure | Name selected source structures explicitly; use `A.22`, `C.30`, or domain owners when structure claims become load-bearing. |
| architecture structural view and viewpoint in `C.30.ASV` | focalization, narrative viewpoint, perspective, lens, whose path through the material, what the reader is allowed to see | Use `NSTD.4` for voice or focalization wording; cite `C.30.ASV` when the viewpoint is over architecture-relevant selected structures. |
| architecture description in `C.30.AD` | synopsis, outline, story bible, explanatory account, learning route, narrative-rendering publication carrier | Use `A.6.3.NAR` for structure-to-sequence rendering and `E.17` for publication; use `C.30.AD` only when the source or target is an architecture description. |
| candidate structure set and trade-off in `C.32` | alternative plots, possible story plans, scenario branches, competing explanation routes, narrative design alternatives | Keep alternatives visible before picking the route; use `NSTD.2` for ordering and `NSTD.6` for declared-use quality. Use `C.32` only for architecture candidate synthesis. |
| project architecture decision in `C.32.PAD` | chosen narrative route, selected plot or order, editorial commitment, scenario commitment | Treat the chosen narrative route as DPF-local unless it is also an architecture decision. Do not let narrative commitment authorize work, evidence, ethics, or architecture decisions. |
| developer or transformer role receiving architecture work | writer, teacher, commentator, story designer, tool operator, performer, generator controller | Name the intended rendering Work role in `NSTD.1`; use `NSTD.4` for narrative voice or viewpoint; use A.15-family patterns only when method, actual role assignment, Work, readiness, or performed-work claims become live. |
| reader-relative structural amount in `C.2.8`, architecture-description adequacy in `C.33`, and narrative source return in `NSTD.6` | what selected relations this reader can extract from the narrative, what remains missing, and when the source or an architecture description must be consulted | Use `NSTD.6` for `NarrativeRenderingEpiplexity` under C.2.8 and for the separate source-return judgement. Use `C.33` for the architecture-description adequacy question. |
| structural correspondence in `C.34` | canon fidelity, same storyworld, adaptation faithfulness, explanation still same-enough, narrative order preserving source relation | Use `C.34` when same-enough preservation matters for architecture; otherwise keep correspondence local to DPF and domain owners and state lost structure and non-admissible use. |
| realized structure, operation, telemetry, feedback in `C.32.P2S` and `G.11` | reader reception, learner reconstruction, field test, replay, audience misunderstanding, generated-output repair, official result after live commentary | Use `NSTD.6`, `NSTD.8`, `E.23`, and `G.11` for evaluation, improvement, and refresh. Use architecture feedback owners only when actual holon structure or architecture-characteristic results are being checked. |

Training transfer works both ways. Architects already practice selected-structure discipline, viewpoints, trade-offs, source return, and actual-structure feedback; to become better narrators they must add reader or listener role, ordering rationale, event support, focalization, engagement boundaries, and declared-use narrative quality. Narrators already practice audience, sequence, viewpoint, tension, and reception; to become better structural workers they must add selected-source discipline, architecture-style view and correspondence discipline, explicit loss accounting, source return, and owner routing.

## Semiotic And Language-Precision Bridge

Narrative work is also semio work: it changes signs, carriers, salience, sequence, viewpoint, articulation, closure, and reader interpretation. The DPF should not translate every narrative problem into a new narratology term. When an FPF pattern already owns the problem under different language, the DPF uses that owner and adds only the narrative-specific selection, ordering, engagement, and reception discipline.

| Narrative-studies wording or problem | FPF owner to use | DPF consequence |
| --- | --- | --- |
| "make it more interesting", "more literary", "more artistic", "more memorable", or "more story-like" | `NSTD.5` for engagement, `C.2.LS` plus `C.2.4` through `C.2.7` when a language-state profile matters, and `NSTD.6` for declared-use quality | Artistic or memorable wording is admissible only as use support or language-state choice. It does not by itself increase source truth, source recovery, evidence, ethics, assurance, or permission. |
| early hook, vibe, image, tension, felt mismatch, story seed, or low-articulation direction | `A.16.1` for a pre-articulation cue pack, then `NSTD.1` and `NSTD.2` only when source selection and route selection are explicit | Preserve the cue without pretending that the narrative purpose, selected route, claim, method, or quality endpoint already exists. |
| preconceptual or dynamic-quality pull toward a more artistic rendering | `C.16.Q` as `QS.PreconceptualFit` or related signal-pack treatment, often with `A.16.1` and `C.2.LS` before endpoint evaluation | Treat the felt artistic pull as a real cue or signal only under explicit witness, anchor, and articulation discipline. It is not yet a characteristic, value, proof of narrative quality, or permission to drop source structure. |
| overcommitted plot frame, failed explanatory frame, or too-strong narrative route | `A.16.2` for reopen, sketch-backoff, respecify, or retire; `A.6.P`/`C.16.Q` only when relation or quality precision is actually repairable | Back off the narrative route honestly instead of hiding retreat behind "refined", "made subtler", or "more nuanced" prose. |
| simplified, didactic, redacted, compressed, or audience-safe retelling | `A.6.3.CSC`, with `E.17.EFP` when the rendering is explanation-facing | State narrower admissible use, source-loss mode, blocked downstream use, and source-return condition before treating the retelling as useful. |
| clearer explanation, tutorial wording, onboarding story, or source-linked retelling | `E.17.EFP` plus `A.6.3.NAR` when sequence and narrative order are load-bearing | Classify whether the rendering is source-pinned, source-linked reconstruction, didactic retelling, or speculative retelling; do not let helpful explanation become a second semantic rule track. |
| "same story", adaptation fidelity, canon continuity, or narrative correspondence | `C.34`, with `NSTD.2` and `NSTD.6` for order and declared-use quality | State same-enough relation, preserved relations, lost relations, and non-admissible use rather than relying on the word "faithful". |
| "quality", "good narrative", "adequate story", "strong explanation", or "better style" | `C.16.Q` for overloaded quality wording, `A.19.ECS`/`C.16`/`NSTD.6` for evaluation, `F.18` for durable names | Recover bearer, evaluation frame, quality sense, characteristic or bundle, and value meaning before using the term as improvement guidance. |
| relation words such as "supports", "grounds", "maps", "connects", "based on", or "aligned with" inside narrative rationale | `A.6.P` and direct relation owners such as `A.6.6`, `C.34`, `A.10`, or `B.3` when selected | Restore relation kind, endpoints, qualifiers, admissible use, and blocked overread before the narrative rationale is reused. |
| style, genre, tradition, scene, technique, voice, or tone used as an FPF-governed decision | `E.10` trigger scan; `F.18` only for reusable durable names; `NSTD.4` and `NSTD.5` for DPF-local voice and engagement | Keep craft vocabulary useful, but do not let style words mint ontology, authority, or quality values. |

The practical rule is bidirectional in reading but one-directional in dependency. DPF authors may freely read FPF patterns as solution resources for narrative problems. FPF Core patterns do not depend on this DPF. If a narrative problem is really a source relation, relation precision, coarsening, explanation, language-state move, quality-term, evidence, assurance, ethics, publication, generated-carrier, or refresh problem, the DPF names the FPF owner and then states only the narrative-specific source selection, sequence, reader-use, and reception consequences.

## Source Use And Refresh Map

Use `G.2` source rows to ground the narrative-studies, cognitive, teaching, ethics-risk, and generation claims used by this package. A source row does not become an ethics, evidence, assurance, admission, or authority owner. When a source row is absent, stale, ambiguous, or too narrow for a relied-on claim, keep the claim bounded and route refresh through `G.2`/`G.11`.

| Source line | DPF locus supported | Use boundary |
| --- | --- | --- |
| Hoffmann, "The Tensions of Scientific Storytelling" | `NSTD.1`, `NSTD.3`, `NSTD.5` | Scientific narrative can organize discovery, mechanism, attempts, calculations, and unresolved tension, but it does not create evidence or assurance. |
| Schmid, `Narratology: An Introduction`, and Chihaia, `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` | `NSTD.2`, `NSTD.4`, precision map, source-use refresh | Use source-material vocabulary only after restoring admitted source basis and selected source structure; use selection, composition, linearization, rearrangement, perspectivization, voice, and tradition and audience plurality as DPF vocabulary; do not import fiction-bound terms into Core ontology. |
| Nguyen, "A Review of Mechanistic Models of Event Comprehension"; Chen and Xu, "Neural and Behavioral Evidence for Differential Processing of Narrative Perspective in Novel Reading"; Mengelkamp et al., "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives"; Georgiou et al., "Large-scale study of human memory for meaningful narratives" | `NSTD.3`, `NSTD.4`, `NSTD.6`, `NSTD.8` | Event, hierarchy, prediction, updating, viewpoint, reading goal, metacomprehension, and memory effects inform reconstruction checks; they do not prove source truth. |
| Castricato et al., "Towards a Formal Model of Narratives"; prospective narrative practice such as design-fiction or experiential-futures sources | `NSTD.1`, `NSTD.2`, `NSTD.4`, `NSTD.6`, acceptance cases | Intended rendering Work role, actual performer when claimed, reader or listener role, narrative voice or viewpoint, reader story-model evolution, uncertainty, and temporal posture become explicit and distinct drafting or evaluation positions; these rows do not create FPF Core ontology. |
| Green and Brock, "The Role of Transportation in the Persuasiveness of Public Narratives"; Dahlstrom and Ho, "Ethical Considerations of Using Narrative to Communicate Science"; Meretoja, "Narrative and Human Existence: Ontology, Epistemology, and Ethics" as background only; FPF `D.1` through `D.5` | `NSTD.5`, `NSTD.6`, acceptance cases | Engagement and persuasion are real design effects, but ethics, harm, evidence, and assurance stay with FPF owners. |
| Dunlosky et al., "Improving Students' Learning With Effective Learning Techniques"; Rohrer and Taylor, "The shuffling of mathematics problems improves learning"; Kang, "Spaced Repetition Promotes Efficient and Effective Learning" | `NSTD.8`, `NSTD.6`, architecture bridge, source-use refresh | Learning-route architecture may need spaced retrieval and interleaving rather than blocked topic order; a coherent source architecture must not be copied automatically as the course architecture. |
| Gatt and Krahmer, `Survey of the State of the Art in Natural Language Generation`; Alabdulkarim et al., "Automatic Story Generation: Challenges and Attempts"; Cardona-Rivera and Ware et al., "The Story So Far on Narrative Planning"; Chakrabarty et al., "SceneCraft"; Ma et al., "Text-to-Text Automatic Story Generation: A Survey"; Rahman et al., "Game Knowledge Management System"; Nguyen-Trung and Nguyen, "Narrative-Integrated Thematic Analysis" | `NSTD.7` | Generation splits content planning, discourse planning, method, schema, repair, admission, evaluation, and human interpretive agency; fluency never grants authority. |

Refresh condition: use `G.11` when source pack, FPF Core edition, narrative-studies source basis, generated-narrative practice, reader telemetry, teaching-test evidence, or evaluation results change.

## DPF Precision Restoration And Owner Map

These terms are local working vocabulary unless a source owner and naming owner admit a more durable term. The map states the owner and blocks accidental `U.*` minting.

| Term | Kind and owner | Use in this DPF | Blocked overread |
| --- | --- | --- | --- |
| admitted source basis | Existing FPF source or episteme use; `G.2`, `A.10`, `E.17.EFP` as applicable | Admitted source pack, source publication carrier, architecture description, pattern body, event record, formal text, or other episteme from which selected source structures may be recovered for this narrative use | Not the selected source structure by itself and not a permission to treat every mentioned object as source authority |
| selected source structure | Existing FPF structure use; `A.22`, `A.6.3.NAR`; `C.2.8` when reader-relative structural amount is compared and `C.33` for architecture-description adequacy | Structure that must remain recoverable after rendering | Not the narrative rendering and not evidence authority |
| source-structure selection rationale | DPF-local slot under `NSTD.1`, with source-owner support when needed | Why these structures were selected for the declared reader or listener use and not merely because the current rendering foregrounded them | Not proof that the selection is correct and not a substitute for source, evidence, or architecture owners |
| source temporal posture | DPF-local slot under `A.6.3.NAR` and `NSTD.1` | Whether the selected source structure or admitted source basis concerns retrospective or reverse-engineered actual structure or event record, live unfolding, prospective planned structure, prospective fictional structure or canon, or a mixed case | Not evidence strength, chronology, or publication date by itself |
| rendering mediation mode | DPF-local slot under `A.6.3.NAR` and `NSTD.1` | Whether narrative rendering is direct source-structure rendering, architecture-mediated rendering, or mixed | Not a claim that all narrativization is architecture and not a reason to bypass architecture owners when architecture is live |
| architecture-mediated narrativization route | Rendering mediation mode using architecture understanding, architecture description, views, viewpoints, decisions, candidate structures, or telemetry as mediating source | Narrate actual or future holon structure for a declared reader or listener use | Not architecture decision, not architecture description itself, and not implementation authority |
| rendering Work role | DPF-local project role reference under `NSTD.1`; recover an actual system, role assignment, and Work through their direct FPF patterns when those claims are made | Writer, teacher, commentator, story designer, tool operator, or another role proposed to arrange selected source structure into narrative | Not the role holder, actual performer, narrative voice or viewpoint, source authority, admission responsibility, evidence source, or ethical decision maker by this reference alone |
| reader or listener role | DPF-local role-use slot under `NSTD.1`, `NSTD.6`, and publication and audience owners when needed | Intended receiver role whose use constrains source selection, order, viewpoint, engagement, and source return | Not a generic audience, not authority, and not source truth |
| reader-interest or use hypothesis | DPF-local slot under `NSTD.1` and test object for `NSTD.6` | Explicit guess about what the receiver needs to understand, do, remember, decide not to decide, or return to source for | Not a guarantee of actual comprehension without evaluation or telemetry |
| narrative rendering | DPF-local name for the receiving-side episteme and rendering relation under `A.6.3.NAR`; carrier or publication availability routes to `E.17` or the direct publication owner | One version of source structure rendered as sequence | Not source truth, carrier identity, assurance, or publication permission |
| narrative purpose | Relation slot in `NSTD.1` | Declared reader-use aim tied to source structure | Not free persuasion goal |
| ordering rule | Relation slot in `NSTD.2` | Rule that orders source structure into sequence | Not physical time, proof order, or work order unless the source supports it |
| event model | DPF-local vocabulary under `NSTD.3`, with causal claims routed to `C.28` | Reader-recoverable account of events, mechanism, dependency, or state change | Not causal evidence by itself |
| viewpoint | DPF-local vocabulary under `NSTD.4` | Position from which the rendering presents the source | Not evidence, responsibility, or source authority |
| focalized object | DPF-local vocabulary under `NSTD.4` | Object, role, holon, relation, or source locus made salient by viewpoint | Not a new agent or protagonist kind |
| voice | DPF-local vocabulary under `NSTD.4` | Rendering stance and speaker arrangement | Not authority, evidence, or moral permission |
| protagonist | DPF-local storycraft vocabulary under `NSTD.4` | Reader-facing center of action or attention when useful | Not necessarily an `A.13` agent, role holder, or responsible party |
| actant | DPF-local narratology vocabulary under `NSTD.4` | Function in a narrative relation or plot grammar | Not `U.Role`, `U.RoleAssignment`, or capability without direct owner |
| agency or personification | Governed by `A.13`, `A.2`, `A.2.1`; local wording check in `NSTD.4` | Humanlike or agent-like presentation of a source bearer | Does not assign responsibility, capability, permission, or decision authority |
| engagement effect | DPF-local characteristic candidate in `NSTD.5` and `NSTD.6` | Attention, motivation, memorability, or following support | Not truth, evidence, assurance, or ethical clearance |
| persuasion boundary | Ethics and value routing through `D.1` through `D.5`; local slot in `NSTD.5` | Limit on influence, decision pressure, or action invitation | Not policy permission or work authorization |
| generated source plan | Method or source-plan reference; `G.2`, `C.35`, `NSTD.7` | Source representation supplied to a generator | Not an admitted source structure until owner checks pass |
| plot or event plan | Method-description or generation-plan element; `NSTD.7` | Planned sequence for generated narrative | Not source truth or event evidence |
| schema constraint | Method or generation constraint; `NSTD.7`, `C.35` | Formal or informal constraint on generation | Not assurance or evidence sufficiency |
| generation method | Method or method-description claim; direct method owners plus `C.35` | Procedure used to produce a carrier | Not admission of its output |
| repair loop | Improvement method; `E.22` when the question needs framing and `E.23` after values exist | Repeated repair of a narrative rendering version or DPF scale set under re-evaluation | Not evaluation itself, not prompt retry, and not proof of quality movement without re-evaluation |
| learning narrative route | Teaching or learning route design plus publication-carrier relation governed by `NSTD.8`, `E.17`, `E.17.AUD` | Narrative route over source structures for learner reconstruction or application | Not the pattern body and not the teaching material itself |
| learner reconstruction task | Teaching work item or evaluation evidence; `NSTD.8`, `A.15`, `NSTD.6` | Task that tests whether learners can recover selected source structure and source-return boundaries | Not proof of general understanding without evidence and scale |
| narrative rendering epiplexity | Narrative specialization of the `C.2.8 U.ExtractableStructuralInformation` relation characteristic, applied in `NSTD.6` with its scale and evidence basis | What selected structure the reader can correctly extract from the narrative episteme through its publication form under the specified conditions | A qualitative comparison or declared structural-scale result; its name alone supplies neither a bit estimate nor a material-quality, learning or assurance conclusion |
| narrative rendering quality characteristic | Evaluation characteristic; `A.19.ECS`, `C.16`, `NSTD.6` | Characteristic used to evaluate one narrative rendering version for declared use and source-return obligations | Not an eval program, evidence record, assurance claim, or gate |
| narrative language-state facet profile | Existing FPF language-state profile use; `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, and `C.2.7` | Decomposable statement of articulation, closure, anchoring, representation factors, and thresholds for a narrative rendering or cue | Not a master maturity value, not artistic merit, and not quality by itself |
| pre-articulation narrative cue | Existing FPF cue-pack use; `A.16.1` | Preserved hook, tension, image, felt mismatch, or route hint before narrative purpose, route, claim, or quality endpoint is honest | Not a selected route, not a claim, not a method, and not proof that a story should be written |
| preconceptual narrative fit signal | Existing FPF quality-term precision use; `C.16.Q` with `QS.PreconceptualFit`, and `A.16.1` when still cue-like | Felt rightness, dynamic-quality-like pull, or artistic fit before the DPF can honestly publish a characteristic or route | Not a metric, not `NarrativeRenderingEpiplexity`, not source fidelity, and not sufficient evidence that the rendering works |
| coarsened narrative rendering | Existing FPF coarsening use; `A.6.3.CSC`, with `NSTD.2` and `NSTD.6` for narrative order and quality | A simplified, compressed, redacted, didactic, or audience-safe rendering that remains useful only under narrower admissible use and source return | Not source replacement, not explanation faithfulness by itself, and not evidence or assurance |
| explanation-facing narrative rendering | Existing FPF explanation-use profile; `E.17.EFP`, with `A.6.3.NAR` when narrative ordering is load-bearing | Narrative rendering that helps a reader understand an already available source episteme or publication | Not a second semantic rule track and not operative evidence without the direct owner |
| narrative precision restoration | FPF precision-restoration route; `E.10`, `A.6.P`, `C.16.Q`, `C.2.P`, and the direct owner selected by the recovered claim | Repair of overloaded narrative wording such as support, alignment, quality, style, adequacy, source, route, or same-story claims | Not synonym polishing and not a reason to create local DPF ontology when FPF already owns the claim |
| artistic or literary rendering mode | DPF-local craft and use choice under `NSTD.4` and `NSTD.5`, with `C.2.LS` when language-state thresholds matter | Voice, tone, genre, scene, tension, or literary technique used to support declared reader use while preserving source-return limits | Not higher truth, higher epiplexity, ethical permission, or quality value unless `NSTD.6` evaluates it for the declared use |

Do not use `C.9` operationally in this package. Agency and role claims use `A.13`, `A.2`, `A.2.1`, `A.2.2`, `A.19.ECS`, `C.16`, `D.1` through `D.5`, `A.10`, and `B.3`.

## Name And Edition Route

Package name: `Narrativization and Narrative Studies Principles Framework`.

Public prefix for package pattern ids: `NSTD.*`.

`NSTD.*` is the package-local pattern prefix for this Domain Principle Framework. It is not an FPF Core id. The rejected `NAR.*` DPF prefix would collide with Core `A.6.3.NAR`.

```text
FrameworkEditionDependencyRecord@NarrativizationAndNarrativeStudiesPrinciplesFramework:
  frameworkEditionRef: NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-09-09
  dependsOnEditionRefs: FPFCorePatternSet@current
  dependencyReason: DPF reuses FPF Core relation, source, coarsening, explanation, language-state, precision-restoration, constraint-governed unfolding, ethics, evidence, assurance, quality, publication, generated-carrier, and refresh governing patterns
  compatibilityBoundary: DPF may add domain patterns but may not redefine Core A.6.3.NAR, A.22.CGUS, A.6.3.CSC, E.17.EFP, A.6.P, C.2.LS, A.16.1, A.16.2, C.16.Q, E.10, F.18, D.1 through D.5, A.10, B.3, A.19.ECS, C.16, or C.35
  deprecationOrSupersessionRefs: none for this package edition
  refreshConditionRefs: source-pack change, FPF Core edition change, failed teaching test run, generated-narrative SoTA change, evaluation-scale defect
  e53ConformanceNote: dependency points from this DPF toward FPF Core; Core has no reverse dependency
```

## DPF Relation Records

These `PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesPrinciplesFramework` records state package relations that matter during use, refresh, and reuse.

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesPrinciplesFramework:
  relationId: PFR-NSTD-CORE-DEP-001
  sourceRef: NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-09-09
  targetRef: FPFCorePatternSet@current
  relationFunction: Framework edition dependency
  governedUse: DPF patterns rely on FPF Core relation, source, evaluation, ethics, evidence, assurance, generated-carrier, publication, and refresh owners
  directGoverningPatternRef: E.4.PFR
  dependencyOrEditionEffect: DPF depends on Core; Core has no reverse dependency
  blockedStrongerReading: not Core specialization by dependency and not permission to redefine Core owners
  refreshOrSupersessionCondition: refresh when relevant FPF Core edition changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-NAR-SPEC-001
  sourceRef: NSTD.1 through NSTD.8
  targetRef: A.6.3.NAR
  relationFunction: Specialization and pattern-use support
  governedUse: DPF narrows Core structure-to-narrative rendering for narrative studies and teaching uses
  directGoverningPatternRef: A.6.3.NAR
  dependencyOrEditionEffect: DPF inherits Core relation obligations and adds domain checks
  blockedStrongerReading: DPF does not redefine Core A.6.3.NAR, E.17.EFP, source, evidence, ethics, or assurance owners
  sourceReturnCondition: return to Core when a DPF row tries to govern the source-to-rendering relation generally
  refreshOrSupersessionCondition: refresh when A.6.3.NAR changes the Core relation slots or source-return obligations
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-CGUS-DEP-001
  sourceRef: NSTD.1, NSTD.2, NSTD.6, and NSTD.8
  targetRef: A.22.CGUS
  relationFunction: Downstream use of constraint-governed unfolding structures
  governedUse: narrative rendering may select, order, evaluate, or teach a demonstrative slice over a wider constraint-governed unfolding structure
  directGoverningPatternRef: A.22.CGUS
  dependencyOrEditionEffect: DPF depends on Core CGUS distinctions; Core has no reverse dependency on this DPF
  blockedStrongerReading: narrative sequence, learning route, or framework carrier is not the selected unfolding structure by presentation
  sourceReturnCondition: return to A.22.CGUS or the local FPF governing pattern when preserved and lost structure, admissible next form, direct exit, or stop condition is missing
  refreshOrSupersessionCondition: refresh when A.22.CGUS, E.18.3, A.6.3.NAR, or local CGUS block guidance changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-SRC-REUSE-001
  sourceRef: Source Use And Refresh Map under G.2
  targetRef: NSTD.1 through NSTD.8
  relationFunction: Source or decision reuse
  governedUse: source rows support narratology, science-storytelling, teaching, evaluation, and generation claims by value
  directGoverningPatternRef: G.2
  blockedStrongerReading: source rows do not become ethical, evidence, assurance, or authority owners
  sourceReturnCondition: return to G.2 when source classification, currentness, rival tradition, or exact source row is missing
  refreshOrSupersessionCondition: refresh when source basis or SoTA currentness changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-EVAL-001
  sourceRef: NSTD.6
  targetRef: NSTD.1 through NSTD.8
  relationFunction: Quality framing, evaluation, or improvement
  governedUse: evaluate one narrative rendering version or learning route for declared use and feed repair to E.23 when values exist
  directGoverningPatternRef: A.19.ECS
  preservationOrAdmissionRef: NarrativeRenderingQualityEvaluationCharacteristicSpace@Context
  blockedStrongerReading: NSTD.6 is not evidence, assurance, admission, publication, gate, decision, or pattern-quality authority
  sourceReturnCondition: return to A.19.ECS or C.16 when object kind, scale, value meaning, or measurement basis is defective
  refreshOrSupersessionCondition: refresh when evaluation floor, characteristics, use, evidence basis, or low-value repair route changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-IMPROVEMENT-001
  sourceRef: NarrativeRenderingQualityEvaluationResult@Context
  targetRef: E.22 and E.23
  relationFunction: Narrative rendering quality-loop transfer
  governedUse: improve one exact narrative rendering version or declared changed slice by rerunning NSTD.6 after repairs
  directGoverningPatternRef: E.23; E.22 when the improvement question needs framing
  preservationOrAdmissionRef: NarrativeRenderingImprovementLoopInput@Context
  blockedStrongerReading: an NSTD.6 low value, style suggestion, prompt retry, or generated variant is not an improvement claim until the changed object version is re-evaluated
  sourceReturnCondition: return to NSTD.6 when object version, declared use, result rows, protected trade-offs, allowed change slice, cost and risk, or expected re-evaluation form is missing
  refreshOrSupersessionCondition: refresh through G.11 when source currentness, reader telemetry, teaching-test evidence, FPF edition, generated-narrative practice, or evaluation characteristic space changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-GENCARRIER-001
  sourceRef: generated or discovered carrier that may carry a candidate narrative rendering
  targetRef: NSTD.7
  relationFunction: Produced-carrier admission
  governedUse: admit or reject generated narrative output before it is evaluated as narrative rendering or used in teaching
  directGoverningPatternRef: C.35
  preservationOrAdmissionRef: AutomatedNarrativizationAdmissionCase@Context
  blockedStrongerReading: generated fluency, coherence, controllability, or schema compliance is not source authority, evidence, assurance, or admission
  sourceReturnCondition: return to C.35 when produced carrier, described structure, preserved structure, lost structure, or receiving owner is missing
  refreshOrSupersessionCondition: refresh when generator, source plan, schema, source edition, or admission result changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-TEACHING-CARRIER-001
  sourceRef: external FPF seminar or teaching test-run publication carrier
  targetRef: NSTD.8
  relationFunction: Publication or teaching publication-carrier relation
  governedUse: teaching files expose or test a learning narrative route without entering DPF pattern bodies
  directGoverningPatternRef: E.17
  preservationOrAdmissionRef: LearningNarrativeRoute@Context
  blockedStrongerReading: teaching publication carrier is not the DPF pattern body, not FPF source authority, and not a narrative rendering quality result
  sourceReturnCondition: return to source patterns when teaching examples lose selected source structure
  refreshOrSupersessionCondition: refresh when learner telemetry, session sequence, source structure spine, or carrier publication condition changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-TEACHING-EVAL-001
  sourceRef: external FPF seminar or teaching test-run publication carrier
  targetRef: NSTD.8 and NSTD.6
  relationFunction: Narrative-route evaluation and improvement relation
  governedUse: evaluate learner reconstruction and source-return readiness for the learning route, then feed repair to E.23 when values exist
  directGoverningPatternRef: NSTD.6; E.23 when improvement values exist
  preservationOrAdmissionRef: NarrativeRenderingQualityResultRow@Context
  blockedStrongerReading: evaluation result is not publication permission, source authority, evidence, assurance, or package authority
  sourceReturnCondition: return to NSTD.6 when evaluated object kind, value meaning, evidence basis, or low-value repair route is missing
  refreshOrSupersessionCondition: refresh when learner telemetry, quality floor, evaluation result, or improvement route changes
```

```text
PatternFrameworkRelationRecord@NarrativizationAndNarrativeStudiesDPF:
  relationId: PFR-NSTD-ETHICS-EVIDENCE-ASSURANCE-001
  sourceRef: NSTD.4 and NSTD.5
  targetRef: D.1-through-D.5, A.10, B.3
  relationFunction: Governing-pattern relation
  governedUse: route agency, responsibility, persuasion, harm, evidence, and assurance claims out of narrative-effects vocabulary
  directGoverningPatternRef: direct owner named by claim kind
  blockedStrongerReading: viewpoint, protagonist, actant, engagement, or fluency does not assign responsibility, capability, evidence, assurance, or moral permission
  sourceReturnCondition: return to direct owner when claim-bearing ethics, evidence, assurance, or responsibility language appears
  refreshOrSupersessionCondition: refresh when FPF ethics, evidence, or assurance owner guidance changes
```

## Refresh Route

Use this route when the package is already being applied and one of its source, evaluation, or carrier assumptions changes.

1. Return to `G.2` when a load-bearing source line is absent, stale, too narrow, contradicted, or used beyond its stated boundary.
2. Return to `NSTD.6` when the evaluated object kind, declared use, value meaning, quality characteristic, evidence basis, or low-value repair route changes.
3. Use `E.22` when the improvement question is underframed: purpose, floor, protected trade-offs, expected evidence, result form, or cost and risk are not explicit.
4. Use `E.23` only for an exact changed narrative rendering version or declared changed slice with `NSTD.6` re-evaluation planned.
5. Use `G.11` refresh when FPF Core edition, generated-narrative practice, reader telemetry, teaching-test evidence, source pack, or the `NSTD.6` evaluation characteristic space changes.
6. Keep test-run publication carriers outside pattern bodies; use them as evidence or examples only through the direct owner named by the claim.


# SOURCE_FILE: USING-FPF.md
---
# Using FPF and Engineering DPF Suite

Use the publications in this folder to help with the project's work. Paths below are relative to the folder containing this file.

## Choose what to read

Start with the actual situation, the object being worked on, and the result the answer needs to support. If a pattern is already named, find it directly. Otherwise use `Readme.md`, `Engineering DPF Suite/README.md`, and `Engineering DPF Suite/ENGINEERING-DPF-SUITE-REFERENCE.md` to choose relevant publications and patterns. Search for alternative formulations of the question; include English terms when the user's language differs from the sources.

To perform a selected method, read its description, applicability conditions, and the related patterns needed for that use. To use a particular technique, read its section together with the conditions it depends on. Apply it to the facts and constraints of the task.

Explain results and give feedback in the language of the project's work. Preserve the source distinctions that affect the answer. Cite the patterns and locations used. State assumptions, missing evidence, use limits, and the need for human judgement where they affect the decision. Let the current question determine the next step.

## File structure

A publication contains several patterns, located by their IDs. For example:

| Markdown | Meaning |
| --- | --- |
| `## SYSE.24 - Choose How the Project Will Obtain a Needed Engineering Result` | Start of pattern `SYSE.24` |
| `### SYSE.24:4 - Solution` | Section of that pattern |
| `#### SYSE.24:4.1 - Name one result and one decision` | Subsection |
| `### SYSE.24:End` | End of the pattern |

IDs also occur in contents tables and cross-references. Match a heading at the start of a line to locate the pattern itself. Line numbers help retrieve portions of a file; IDs locate a pattern after its line numbers change. A reference such as `SYSE.24:4.1` points to a subsection; read it through to the next heading of the same or a higher level.

## Search and read

Use `rg` (ripgrep), or the environment's equivalent search tool with regular expressions. Run these commands with this folder as the working directory, or prepend its actual path to the file arguments.

Find Reference entries for “obtain a needed engineering result: build or buy”:

```sh
rg -n -i -C 2 'buy|build|obtain the result' -- "Engineering DPF Suite/ENGINEERING-DPF-SUITE-REFERENCE.md"
```

Locate the file and the start and end lines of the selected pattern:

```sh
rg -n --no-ignore -g '*.md' '^## SYSE\.24 |^### SYSE\.24:End[ \t]*\r?$' -- .
```

Read that pattern in full:

```sh
rg -U --no-heading --no-line-number --no-filename --color never '(?ms)^## SYSE\.24 [^\r\n]*\r?\n.*?^### SYSE\.24:End[ \t]*\r?$' -- "Engineering DPF Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md"
```

Here `-U` enables multiline search; `(?m)` makes `^` and `$` match line starts and ends, and `(?s)` lets a dot match a newline. `(?ms)` combines them. `.*?` matches through to the nearest specified `:End` heading; `\r?\n` accepts Windows and Unix line endings. Substitute another ID and file as needed; escape literal dots in IDs as `\.`.

For other searches, `-F` treats the query as literal text, `-i` ignores case, and `-C 2` includes neighbouring lines. `--no-ignore` searches files even in a Git-ignored folder; `-g '*.md'` selects Markdown files.

If the tool truncates a long result, read the selected text in successive line ranges with the available file reader. Folder search already covers separate publications; no combined file is needed.