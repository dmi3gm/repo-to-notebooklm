## G.0 - Define Admissible Comparison and Aggregation for a Frame (CG-Spec)

> **Status:** Stable

**Tag.** Architectural pattern (foundational Standard; constrains G.1–G.5)
**Stage.** *design-time* legality gate (establishes comparison legality & evidence minima; constrains run-time gates)
**Primary output.** `CG‑Spec` — a notation-independent legality gate for a `CG‑Frame`, published to UTS (with explicit edition pins for downstream reproducibility and RSCR).
**Primary hooks.** `USM.ScopeSlice(G)`, `entityOfConcern`, `SCP`, `MinimalEvidence`, `CNSpecRef`, `Γ‑fold`, `Φ(CL)` / `Φ_plane` policy pins, `UTS` publication (Name Cards + edition pins).
**Non-duplication note.** Universal Part‑G invariants are cited through `G.Core` and are satisfied here **only via delegation** (`CC‑G0‑CoreRef` → `CC‑GCORE‑*`). Single‑governing definition CN/CG spec-ref discipline is enforced via `CC‑GCORE‑CN‑CG‑1` (no shadow specs; no competing defaults).

### G.0:1 - Problem frame

A team defines or evolves a `CG‑Frame` (e.g., a frame for creativity measurement, decision quality, architecture trade‑offs, or selected-set publication). Downstream comparison, aggregation, and publication of CHR‑typed observations (G.1–G.5 and beyond) must be:

* lawful with respect to measurement admissibility (scale/unit/polarity constraints),
* auditable with explicit evidence minima and provenance,
* reproducible via pinned editions and explicit policy ids,
* portable only via explicit crossings (bridges and reference-plane moves), never via implicit semantic leakage.

`CG‑Spec` is the single design-time object that fixes *what comparisons and aggregations are lawful in this frame*, under which pinned assumptions and minimal evidence requirements, so that run-time selection and publication can be audited without inventing new “local legality gates”.

Didactic subtitle: **Design-time rules for safe, auditable comparison.**

### G.0:2 - Problem

Without a single, frame-level legality standard:

* comparisons and aggregations drift into *implicit assumptions* (hidden scalarisation; silent totalisation of partial orders),
* numeric gates run on “whatever is available” rather than declared evidence minima and lane/carrier requirements,
* cross-context reuse happens without explicit crossing visibility and stated losses,
* selection outcomes become hard to audit because legality, evidence minima, and penalty routing are not pinned and traceable.

### G.0:3 - Forces

* **Pluralism vs. comparability.** Multiple traditions must co-exist while allowing admissible comparison where justified.
* **Expressiveness vs. safety.** Rich comparator sets and aggregators vs. measurement admissibility constraints.
* **Locality vs. portability.** Context-local semantics first; portability only via explicit bridges and explicit losses.
* **Assurance vs. agility.** Evidence minima must meet the claim threshold while staying light enough to adopt.
* **Design-time vs. run-time.** Keep legality standards and templates design-time; run-time only cites and applies them.

### G.0:4 - Solution — CG‑Spec as the design-time legality gate

`CG‑Spec` is a **notation-independent** UTS-published object that, for a given `CG‑Frame`, defines:

* the **ComparatorSet** (explicit, finite, typed) permitted in this frame,
* the **ScaleComplianceProfile** (SCP) that constrains lawful operations per characteristic,
* **MinimalEvidence** requirements per characteristic (lanes, carriers, freshness windows, crossing allowances, failure behavior),
* the frame’s **penalty and trust folding wiring** (by explicit policy ids and edition pins),
* **AcceptanceStubs** as design-time templates (thresholds remain governed by CAL, not by CG‑Spec),
* optional method-family hooks (e.g., illumination/QD or explore↔exploit guards) *as wiring only*, with semantics governed by the corresponding patterns.

`CG‑Spec` constrains downstream gate checks by being *referenced and pinned*; it is not itself an admissibility mechanism.

#### G.0:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part-G core invariants; governing-pattern citation)

**GCoreLinkageManifest (normative; size-controlled via profiles/sets).**

Effective obligations/pins/triggers are computed by union expansion of the referenced ids (per `G.Core:4.2`).
Profiles/sets + explicit deltas; `Nil‑elision` applies.

* `CoreConformanceProfileIds :=`
  * `GCoreConformanceProfileId.PartG.AuthoringBase`
  * `GCoreConformanceProfileId.PartG.TriStateGuard`
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
* `CorePinSetIds :=`
  * `GCorePinSetId.PartG.AuthoringMinimal`
  * `GCorePinSetId.PartG.CrossingVisibilityPins`
* `CorePinsRequired :=` *(delta over PinSets)*
  * `UTSRowId[]`
  * `ReferenceMap`
  * `ComparatorSetRef.edition`
  * `SCPRef.edition`
  * `ΓFoldRef.edition?`
  * `MinimalEvidenceRef.edition?`
  * `FailureBehaviorPolicyId?`
* `DefaultsConsumed := {DefaultId.GammaFoldForR_eff}` *(governing definition: `CC‑G5.4` per `G.Core.DefaultGoverningDefinitionIndex`)*
* `RSCRTriggerSetIds := {GCoreTriggerSetId.CGSpecGate}`
* `RSCRTriggerKindIds :=` *(delta over TriggerSets)*
  * `RSCRTriggerKindId.EvidenceSurfaceEdit`
  * `RSCRTriggerKindId.TokenizationOrNameChange`
  * `RSCRTriggerKindId.DefaultGoverningDefinitionChange`
* `TriggerAliasMapRef := ∅`

#### G.0:4.2 - CG‑Spec object model (normative)

`CG‑Spec` is authored per `CG‑Frame`. It SHALL:

* be **published to UTS** as a notation-independent object,
* reference CHR characteristics by id (measurement semantics remain governed by CHR packs),
* constrain what comparisons and aggregations are lawful in this frame via explicit comparator specs and SCP bindings,
* declare minimal evidence gates per characteristic, including explicit failure behavior wiring,
* cite `CN‑Spec` for normalization/comparability policies (no duplication and no shadow specs),
* publish edition pins and policy ids so downstream selection, parity, shipping, and refresh can be reproducible and RSCR-aware.

#### G.0:4.3 - CG‑Spec conceptual model (normative)

```
CG‑Spec :=
⟨
  UTS.id, Edition,
  Context, Purpose, Audience,

  Scope := USM.ScopeSlice(G) ⊕ Boundary{TaskKinds, ObjectKinds},

  entityOfConcern := ⟨GroundingHolon, ReferencePlane ∈ {world|concept|episteme}⟩,
  WorldRegime? ∈ {prep|live},          // only refines ReferencePlane=world; introduces no new planes

  ReferenceMap := minimal map{term/id → UTS|CHR|SoTA-pack refs},

  CNSpecRef := ⟨CN‑Spec ref, CNSpecRef.edition⟩,          // CN‑Spec is the governance card defined in A.19.CN (one governing definition)

  Characteristics := [CHR.Characteristic.id…],          // pointers only; authored in G.3 CHR pack

  // Edition-addressable segments (pins MUST be exposed)
  ComparatorSet := ⟨ComparatorSetId, ComparatorSetRef.edition, [ComparatorSpec…]⟩,
  SCP := ⟨SCPId, SCPRef.edition, map Characteristic.id → SCPEntry⟩,
  MinimalEvidence := ⟨MinEvId, MinimalEvidenceRef.edition?, map Characteristic.id → MinEvidenceEntry⟩,  // min pin: CGSpecRef.edition

  Γ‑fold := ⟨GammaFoldId, ΓFoldRef.edition?,   // pin the actual model/policy when a numerical fold is used
             defaultRef := DefaultId.GammaFoldForR_eff,
             override? := ⟨overrideRef, proof_refs, boundary_notes⟩
           ⟩,

  // Penalty routing and plane policies are by explicit policy ids.
  // For semantics (tri-state, penalties→R_eff-only, crossing visibility, set-return), cite G.Core and the governing definitions it identifies.
  CL‑Routing := ⟨policy_id, map Bridge.CL → penalty_spec⟩,
  Φ := ⟨phi_policy_id, phi_table_ref?, psi_policy_id?, phi_plane_policy_id?⟩,

  AcceptanceStubs := [AcceptanceStubId…],     // templates only; thresholds remain governed by CAL (G.4)

  // Optional hooks are wiring-only; semantics are governed by governing definitions.
  E/E‑LOG Guard? := ⟨policy_id, pins…⟩,
  Illumination? := ⟨
    Q_refs ⊆ Characteristics, D_refs ⊆ Characteristics,
    DescriptorMapRef.edition?, DistanceDefRef.edition?, DHCMethodRef.edition?,
    InsertionPolicyRef?, PromotionPolicyId?
  ⟩,

  RSCR := ⟨
  RSCRTestId[]?,             // SHOULD cover: illegal_op_refusals; unit and scale legality checks; freshness windows; // partial-order scalarisation refusals; threshold semantics; CL→R_eff routing;
                            // and refusal of degrade.order on unit mismatches (MM‑CHR).
    RSCRTriggerKindId[]
  ⟩,

  Naming := UTS Name Cards (twin labels plus bridge notes),
  PublicIdContinuity := ⟨governing definition, DRR link, refresh cadence, decay and aging policy, deprecations⟩,
  Provenance := ⟨carrier types, SoTA-pack refs, DRR/SCR linkage⟩
⟩
```

**Local typing notes (non-exhaustive; normative intent but no shadow specs).**

* `ComparatorSpec` MUST be typed against SCP/CHR constraints. Examples of lawful comparators are frame-local choices and are authored here (e.g., dominance where lawful; lexicographic over typed traits; medoid/median for ordinal where lawful; explicit weighted sums only where legality is proven and units are aligned).
* `MinimalEvidenceEntry` MUST declare: lane requirements, evidence carriers, freshness window (if any), and explicit failure behavior wiring. The semantics of `{pass|degrade|abstain}` and `degrade(mode=…)` are delegated to `G.Core`.

#### G.0:4.4 - Interfaces (normative)

| Interface          | Consumes                             | Produces / constrains                                                      |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- |
| **G.0‑1 Charter**  | CG‑Frame brief, USM scope signals    | `CG‑Spec.Scope`, `entityOfConcern`, `ReferenceMap`                         |
| **G.0‑2 SCP**      | CHR pack refs (G.3), legality proofs | `CG‑Spec.SCP` + bindings to lawful operators/aggregators                   |
| **G.0‑3 Evidence** | SoTA inputs (G.2), source and carrier provenance account (A.10)   | `CG‑Spec.MinimalEvidence`, `Γ‑fold` segment pins, `CL‑Routing`, `Φ` ids    |
| **G.0‑4 Publish**  | All above                            | Versioned `CG‑Spec@UTS` plus Name Cards, public-id continuity records, and RSCR tests and trigger kinds  |
| **G.0‑5 Expose_CrossingHooks** | `CG‑Spec` + crossing/plane/policy pins | GateCrossing inputs for `GateChecks` (`E.18/A.21`): plane checks, lane purity, lexical SD pins |
| **→ G.1**          | `CG‑Spec`                            | Generator guardrails (Comparator/SCP/MinEv pins); degrade/abstain wiring   |
| **→ G.2**          | `CG‑Spec`                            | Harvesting inclusion/exclusion and crossing policy constraints             |
| **→ G.3**          | `CG‑Spec`                            | Required CHR characteristics/scales/operators to exist                     |
| **→ G.4**          | `CG‑Spec`                            | Acceptance templates; evidence minima; Γ‑fold override proof hooks         |
| **→ G.5**          | `CG‑Spec`                            | Eligibility gates and explainability pins (Path/UTS/policy ids)            |
| **→ G.6**          | `CG‑Spec`                            | EvidenceGraph/SCR pinning surface (policy ids + Path/PathSlice discipline) |

#### G.0:4.5 - CG‑Spec authoring chassis (informative)

1. **Charter the frame.** Declare `Context`, `Scope`, `entityOfConcern`, boundary examples/non-examples, and `ReferenceMap`.
2. **Draft ComparatorSet and SCP.** Enumerate permitted comparator forms and bind each to CHR characteristics and legality constraints (scale/unit/polarity discipline). Attach guard bindings as explicit references/pins.
3. **Bind Characteristics.** For every comparison, identify the CHR characteristics of the quantities being compared and cite them by id (reuse/mint via UTS discipline).
4. **Declare MinimalEvidence.** For each characteristic: required lanes/carriers, freshness window, crossing allowances (if any), and explicit failure behavior wiring (tri-state semantics delegated to `G.Core`).
5. **Pin the support-composition basis.** Cite `DefaultId.GammaFoldForR_eff` for the model-qualified rule. A numerical fold or loss pins its actual receiving model, compatible inputs, dependency assumptions, and justification refs; monotonicity and boundedness alone are insufficient. When no common aggregate is justified, the referenced rule retains separate support and a bounded synthesis. Publish any actually used Φ/CL policy ids; keep acceptance thresholds in G.4.
6. **Publish and register regression tests.** Publish `CG‑Spec@UTS` with edition-pinned segments; register RSCR tests for the frame’s legality surfaces and evidence minima.
7. **Public-id continuity and refresh readiness.** Declare refresh cadence and deprecations with lexical continuity notes; ensure RSCR trigger kinds are emitted as canonical ids.

#### G.0:4.6 - Extensions (pattern-scoped; non-core)

All blocks below are `GPatternExtension` modules (PatternScopeId; not new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SpecRefSurfaces**

* **PatternScopeId:** `G.0:Ext.SpecRefSurfaces`
* **GPatternExtensionId:** `SpecRefSurfaces`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19.CN`
* **Uses:** `{A.19.CN}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CNSpecRef.edition` (and any CN-side policy ids referenced by `CG‑Spec` fields)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring-only):** `CG‑Spec` SHALL cite CN‑Spec; it SHALL NOT restate normalization/comparability semantics.

**GPatternExtension: BridgeAndCLWiring**

* **PatternScopeId:** `G.0:Ext.BridgeAndCLWiring`
* **GPatternExtensionId:** `BridgeAndCLWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `F.9`
* **Uses:** `{F.9, G.7}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeCardId/BridgeId` (when crossings are permitted)
  * `CL` / `CL^k` and `Φ`/`Φ_plane` policy ids (when penalties are in play)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring-only):** Crossing semantics and penalty routing are delegated to `G.Core`; this module only lists the required pins used by `CG‑Spec` entries.

**GPatternExtension: SoTAPaletteInputs**

* **PatternScopeId:** `G.0:Ext.SoTAPaletteInputs`
* **GPatternExtensionId:** `SoTAPaletteInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `SoTA-Pack@CG‑Frame` refs used to justify comparator admissibility, evidence minima, and crossing allowances (e.g., claim sheets, operator inventory, bridge matrix ids)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** Any SoTA palette/tradition semantics are governed by `G.2`. `G.0` only requires that `CG‑Spec` entries cite the needed SoTA artefacts for auditability.

**GPatternExtension: QDAndExplorationHooks**

* **PatternScopeId:** `G.0:Ext.QDAndExplorationHooks`
* **GPatternExtensionId:** `QDAndExplorationHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, C.23}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `InsertionPolicyRef?`
  * `FailureBehaviorPolicyId` / SoS‑LOG branch policy id when `degrade(mode=…)` is used
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring-only):** `CG‑Spec` may declare optional QD/exploration hooks; semantics remain governed by the referenced method patterns.

### G.0:5 - Archetypal Grounding — Tell–Show–Show; System / Episteme

#### G.0:5.1 - Archetype 1: System comparability under mixed evidence and unit constraints

**Tell.** Two labs compare energy efficiency results of a physical system where measurements use different rigs and units, and some evidence is missing.

**Show (failure without CG‑Spec).** The team averages an ordinal safety rating, mixes units (“kWh” vs “MJ”), and silently treats missing lanes as zeros. Cross-lab reuse happens without explicit bridge and loss notes, so selection becomes a black box.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* pins the lawful comparator(s) (e.g., unit-aligned ratio comparisons only; ordinal comparisons are order-only),
* declares `MinimalEvidence` lanes/carriers and freshness windows per characteristic,
* declares explicit failure behavior wiring (tri-state semantics delegated to `G.Core`),
* exposes Bridge and bounded-use pins when reuse projects between different local meanings under A.19.CN/F.9; unit conversion within the declared comparison basis follows CN-Spec and SCP,
* publishes the pinned editions so parity/refresh can detect drift.

#### G.0:5.2 - Archetype 2: Epistemic comparability for selected-set publication across traditions

**Tell.** A team selects an R&D set using multiple evaluation traditions: safety assurance, cost models, and readiness heuristics.

**Show (failure without CG‑Spec).** The team collapses partial orders into a single score, hides the threshold policy in code, and cannot explain why cross-tradition penalties changed between runs.

**Show (repair with CG‑Spec).** A conformant `CG‑Spec`:

* defines a comparator bundle (e.g., Pareto dominance + explicit lexicographic tiebreaks where lawful),
* pins `CNSpecRef.edition` and the editioned segments (`ComparatorSetRef.edition`, `SCPRef.edition`, `MinimalEvidenceRef.edition`),
* makes `AcceptanceStubs` explicit as templates while locating thresholds in CAL (G.4),
* ensures RSCR triggers are emitted when comparator or policy pins change.

### G.0:6 - Bias-Annotation

`CG‑Spec` can encode (and therefore amplify) biases if authored carelessly:

* **Tradition favoritism.** Comparator choices may privilege a tradition’s evidence style; mitigation: require explicit evidence minima and explicit crossing costs, and keep cross-tradition aggregation gated by explicit justifications.
* **Metric gaming and Goodhart effects.** Overemphasis on a single scalar can lead to gaming; mitigation: preserve set-return semantics and require explicit, auditable scalarisations when they are lawful and intended.
* **Hidden thresholds and opaque safety policy.** Embedding acceptance thresholds in prose or code hides value judgments; mitigation: keep thresholds in CAL acceptance clauses and pin policy ids.
* **Scope creep.** Comparisons leak across entityOfConcern or reference planes; mitigation: require explicit `entityOfConcern` and `ReferencePlane` pins and treat plane moves as explicit crossing events.

### G.0:7 - Conformance Checklist (normative)

| ConformanceId | Statement |
| --- | --- |
| **CC‑G0‑CoreRef** | `G.0` is conformant only if the applicable core obligations listed in `G.0:4.1` are satisfied (delegation to `CC‑GCORE‑*`; no shadow specs, no competing defaults, typed RSCR triggers, explicit pins). |
| CC‑G0‑01 | `CG‑Spec` is published as a notation-independent UTS object with explicit `Edition`, `Context`, `Scope`, `entityOfConcern`, and a minimum `ReferenceMap`. |
| CC‑G0‑02 | `CNSpecRef.edition` is present and identifies the edition of the external governance card cited by `CNSpecRef` (no local redefinition of CN semantics). *(Delegation target: `CC‑GCORE‑CN‑CG‑1`.)* |
| CC‑G0‑03 | `ComparatorSet` is explicit and finite; each comparator is typed and bound to `SCP` and referenced CHR characteristics; **anything not enumerated MUST be treated as illegal/abstain by default** (no implicit comparator defaults). |
| CC‑G0‑04 | `SCP` declares, per characteristic, the lawful operation regime needed for each referenced comparator (scale/unit/polarity constraints and any required proofs/refs). |
| CC‑G0‑05 | `MinimalEvidence` is declared per characteristic and includes explicit lane/carrier requirements, freshness window references (if any), and explicit failure behavior wiring (tri-state semantics delegated). If freshness windows are used, a stable reference making the applicable window recoverable (e.g., a `PathSliceId` with its declared time window) MUST be pinned for audit. |
| CC‑G0‑06 | The edition-addressable Γ-fold segment **MUST** cite `DefaultId.GammaFoldForR_eff` at `G.5 CC‑G5.4`. Pin any numerical model/policy actually used, with its receiving quantity, input meanings and scales, dependencies, operation and proof/justification refs as required by that governing rule and B.3/C.2.2. With no justified numerical fold, retain the separate support permitted by the governing rule; the segment is not a demand for a score. |
| CC‑G0‑07 | If crossing penalties are used, `CL‑Routing` and `Φ` policy ids are explicit and auditable (policy ids are exposed as pins/refs) **and are required pins for downstream SCR publication on penalised claims** (see `G.6`). |
| CC‑G0‑08 | `AcceptanceStubs` in `CG‑Spec` are templates only; any context-local thresholds/acceptance policies are governed by CAL acceptance artefacts (G.4) and are cited, not duplicated. |
| CC‑G0‑09 | RSCR tests and triggers for edits to legality surfaces and evidence minima are present and use canonical `RSCRTriggerKindId`s. The RSCR test set SHOULD cover at least: illegal_op_refusals; unit and scale legality checks; freshness windows; partial-order scalarisation refusals; threshold semantics; CL→`R_eff` routing; refusal of `degrade.order` on unit mismatches (MM‑CHR). |
| CC‑G0‑10 | `PublicIdContinuity` is declared: governing definition, DRR link, refresh cadence, decay and aging policy, and deprecations. Deprecations preserve lexical continuity (Δ-discipline; delegated to `CC‑GCORE‑ID‑*`). |
| CC‑G0‑11 | *(Conditional)* If `Illumination` / QD hooks are present, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and any `InsertionPolicyRef` / promotion policy ids are pinned (or explicitly marked absent) and are recorded in provenance/audit pins. |
| CC‑G0‑12 | *(Conditional)* If freshness windows influence gating/selection, they are published and enforced, and references making the relevant windows recoverable (`PathSliceId` with a declared time window, or equivalent) are recorded in SCR/audit pins. |
| CC‑G0‑13 | **Pre-flight numeric gates.** Any numeric comparison/aggregation declared in `ComparatorSet` has associated `GateChecks` for unit legality, scale legality, pinned SOP/editions, and declared comparability assumptions; failing any check requires refusing the operation or returning an `abstain` guard result (tri-state semantics delegated). |
| CC‑G0‑14 | **GateCrossing hook exposure.** Exports provide `Expose_CrossingHooks` inputs so `GateChecks` (`E.18/A.21`) can validate plane consistency, crossing intent, lane purity, and lexical SD; failures MUST block publication. |
| **CC‑G0‑Φ** | An actually used numerical Φ(CL) or plane-loss policy has a justified receiving quantity, scale, input interpretation, assumptions, and derivation or calibration under B.3/C.2.2. Publish the policy ids and any required table. Preserve the model's loss direction and bounds; monotonicity, boundedness, or clipping alone does not establish a valid loss model. |
| **CC‑G0‑Unknowns** | *Delegated.* Unknown handling MUST follow the tri-state guard semantics `{pass|degrade|abstain}` with no silent coercions. (See `CC‑GCORE‑GUARD‑1`.) |
| **CC‑G0‑CSLC** | Scale/unit/polarity legality MUST be proven before any aggregation; illegal arithmetic on ordinal/nominal values is nonconformant. (Governed by the relevant legality patterns; `G.0` only binds and cites.) |

### G.0:8 - Common Anti-Patterns and How to Avoid Them

* **Anti-pattern: shadow legality gates in downstream code.** Avoid by requiring downstream to cite `CG‑Spec` segments by id+edition.
* **Anti-pattern: “one number to rule them all”.** Avoid by preserving set-return outputs when only partial orders are lawful; any scalarisation must be explicit, typed, and justified.
* **Anti-pattern: thresholds inside CG‑Spec or CHR.** Avoid by keeping thresholds and acceptance logic in CAL and citing from `CG‑Spec` only via stubs/templates.
* **Anti-pattern: implicit crossings.** Avoid by requiring explicit bridge ids, CL/policy ids, and reference-plane pins.

### G.0:9 - Consequences

* **Lawful comparability.** The frame declares exactly what can be compared/aggregated and under what constraints.
* **Auditable selection.** Downstream selectors can justify outcomes via pinned legality surfaces and explicit evidence minima.
* **Explicit portability costs.** Cross-context reuse becomes deliberate and costed via visible crossings and penalties.
* **Lower drift under evolution.** Edition pinning + typed RSCR triggers makes comparability drift detectable and refreshable.

### G.0:10 - Rationale

`CG‑Spec` centralises frame-level comparability constraints so that:

* CHR authorship (G.3) remains about *measurement meaning* rather than implicit thresholds,
* CAL (G.4) governs context-local acceptance/threshold policies and proof ledgers,
* selectors and dispatchers (G.5) remain policy-governed and auditable rather than encoding hidden legality assumptions,
* refresh (G.11) can treat legality edits and pin changes as explicit causes with canonical trigger ids.

### G.0:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice in evaluation and governance by:

* treating “abstain / defer” as a first-class outcome rather than forcing a single brittle scalar (cf. selective prediction / abstention and set-valued reporting practices),
* preserving multiobjective / partial-order outputs as sets (Pareto / archive thinking) rather than silently collapsing to a scalar,
* emphasising reproducibility via explicit versioning/pinning of evaluation surfaces (editions) and explicit policy identifiers,
* making evidence minima explicit and auditable (a conceptual analogue of modern reproducibility/robustness checklists and evaluation protocols),
* keeping method-family specifics modular (e.g., QD/archives, open-ended exploration budgets) via explicit wiring to governing patterns rather than embedding method semantics into the universal legality gate.

### G.0:12 - Relations

**Builds on:** `G.Core`, `A.19.CN (CN‑Spec)`, `A.10 (evidence-provenance account)`, `A.17–A.19 / C.16 (MM‑CHR legality)`, `A.18 (CSLC)`, `B.3 (trust / Γ‑fold family)`, `F.* (contexts, bridges, CL, UTS)`, `E.10 (lexical rules)`, `E.5.* (notation independence discipline)`.
**Used by:** `G.1` (generator guards), `G.2` (harvesting constraints), `G.3` (required CHR), `G.4` (acceptance templates / proof hooks), `G.5` (eligibility gates), `G.6` (evidence/pin surfaces), and downstream parity/shipping/refresh where `CG‑Spec` is pinned.
**Publishes to:** `UTS` (Name Cards + editioned `CG‑Spec` segments).

### G.0:End

## G.1 - Author a Reusable CG-Frame Generator and Selector Kit

> **Status:** Stable

**Tag.** architectural pattern; *generator chassis* (design‑time kit / authoring scaffold)
**Normativity.** normative, except sections explicitly marked *informative*
**Stage.** *design‑time* authoring of a generator‑kit with a *run‑time* execution façade (policy‑governed; edition‑aware)
**Primary output.** the **six‑card chassis** `M1…M6` published as a **complete, reusable CG‑Frame kit**, plus a versioned **kit manifest** `CGKitId` that binds the six cards as a single reusable unit (view‑friendly inventory + wiring surface)
**Primary hooks.** see **§12 Relations** (notably `G.Core`, `G.0`, `G.2`, `G.5`, `G.10`, `G.11`)
**Working‑model first (informative).** prefer working models and didactic micro‑examples; escalate to formal harnesses only when risk warrants (per E.8).
**Non‑duplication note.** Universal Part‑G invariants (tri‑state guard, set-return, penalties→`R_eff`‑only, crossing visibility, typed RSCR triggers, Default Governing Definition Index, P2W split, linkage discipline, shipping boundary) are located through `G.Core` and their governing definitions are **only cited** here.

**Start here when.** You are authoring a reusable generator, selector, or set-result scaffold rather than a one-off plan, one-off comparison, or tool-specific method recipe.

**First output.** The six-card chassis `M1…M6` published as a reusable `CGKitId`-bound kit with a scope anchor, local SoTA set, variant pool, shortlist surface, and refresh-ready wiring.

**Neighboring FPF patterns.** Use `G.2` for the local SoTA set, `G.5` for governed set-return selection, `G.10` for shipping surfaces, `G.11` for refresh wiring, and `F.17` when the result must also land on a human-facing UTS surface.

**Common wrong neighboring-pattern changes.** If the real entry load is only a one-off governed comparison or shortlist, use `A.19.CPM` for comparing an admitted profile pair under an explicit comparator, `G.0` for comparison legality, or `G.5` for the shortlist; if the real entry load is project alignment rather than kit authoring, use `A.15`; if tooling choice is being treated as the first kit candidate, keep the case here only after the chassis and its bindings are explicit.

### G.1:1 - Problem frame

You are authoring a **CG‑Frame** and want a **repeatable scaffold** that connects:

* a declared **scope anchor** (`CG‑FrameContext`, `entityOfConcern`, governing spec refs),
* a **local SoTA set** (scoped and provenance‑anchored),
* a **variant pool** (candidate ideas / decision options / method variants),
* a **shortlist** (a set-result outcome, not a forced singleton),
* **publication‑ready bindings** into Part‑F artefacts (UTS rows, Name Cards, RSCR tests, worked examples),
* and **refresh readiness** (telemetry hooks + RSCR wiring) without redefining refresh or shipping.

This pattern is intentionally **a chassis**, not a method specification:

* harvesting semantics are governed by `G.2`,
* selection/dispatch semantics are governed by `G.5`,
* CHR/CAL payload semantics are governed by `G.3` / `G.4`,
* shipping semantics are governed by `G.10`,
* refresh orchestration governing definition is `G.11`.

### G.1:2 - Problem

Without a chassis, CG‑Frame authoring tends to fail in repeatable ways:

* **SoTA is not locally scoped**: inputs are “in the air”, not a reconstructible set.
* **Generation is ad‑hoc**: variant candidates are emitted without a stable trace of why/when/how.
* **Selection is opaque**: eligibility/acceptance and assurance are not pinned to explicit surfaces.
* **Outputs don’t land in reusable surfaces**: no clean hand‑off into UTS / RoleDescription / Concept‑Sets / RSCR.
* **No kit‑level snapshot**: the scaffold lacks a versioned manifest, so downstream can’t reliably cite “which chassis edition” was used.
* **Refresh is unplanned**: there is no canonical wiring from edits/telemetry/decay to RSCR causes along the P2W path.

### G.1:3 - Forces

* **Breadth vs. precision:** harvest wide enough to avoid local dogma, but keep the artefact actionable.
* **Generativity vs. assurance:** encourage novelty while keeping evidence, legality, and trust inspectable.
* **Local meaning vs. portability:** keep meaning local by default; crossing must be explicit and auditable.
* **Expressiveness vs. parsimony:** resist inventing new types/slots; prefer reuse and explicit wiring.
* **Stability vs. evolution:** keep stable IDs and pins while allowing SoTA, policies, and editions to evolve.
* **Didactic clarity vs. normative minimalism:** authors need a concrete scaffold, but universal invariants must not be duplicated outside `G.Core`.

### G.1:4 - Solution

#### G.1:4.1 - G.Core linkage (normative)

```
// Canonical form: see G.Core (Nil‑elision + Expansion rule for profiles/sets/pin‑sets).
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  // Prefer sets; use deltas for pattern‑specific additions.
  RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
  RSCRTriggerKindIds := { RSCRTriggerKindId.BaselineBindingEdit },

  // Kit identifiers governed by this pattern (the “six cards”).
  CorePinsRequired := {
    SoTAPaletteDescriptionId,
    SoTA_SetId,
    VariantPoolId,
    ShortlistId,
    CGFrameLibraryId,
    RefreshReadinessCardId,
    CGKitId,

    // Local pointer-map surface for vocabulary + observables-to-CHR anchoring.
    // (May cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics.)
    ReferenceMap,

    // RSCR regression tests used by the chassis (if any).
    RSCRTestId[]?,

    // For a planned baseline, identify the A.15.2 WorkPlan and local locator; add declaration ref, member designator and plan-local filling-row locator when A.15.3 applies.
    WorkPlanRef[]?
  },

  // Consumed defaults (each default cites the governing definition listed in `G.Core.DefaultGoverningDefinitionIndex`).
  DefaultsConsumed := {
    DefaultId.GammaFoldForR_eff,   // governing definition: CC-G5.4
    DefaultId.PortfolioMode,       // governing definition: CC-G5.23
    DefaultId.DominanceRegime      // governing definition: CC-G5.28
  }
⟩
```

**Citation rule (normative):** `CC‑GCORE‑*`, `RSCRTriggerKindId.*`, and `DefaultId.*` semantics are governed by their canonical definitions: primarily `G.Core`, and for the defaults above the definitions listed in `G.Core.DefaultGoverningDefinitionIndex`. `G.1` MUST NOT restate or redefine those semantics.

#### G.1:4.2 - Six‑module generator chassis (normative)

**Core artefact:** `CGFrameReadyGeneratorKit := ⟨M1, M2, M3, M4, M5, M6⟩`, where each `Mi` is a **card** with an explicit I/O surface and stable identifiers.
`CGKitId` identifies the versioned **kit manifest** (`CG‑Kit@CG‑Frame`) that lists the six card ids and the minimal wiring pins needed to treat the chassis as a reusable unit (this is **not** a shipping pack; shipping remains governed by `G.10`).

The chassis is *view‑friendly*: it is an inventory of “what exists and how it is wired”, not a second specification of CN/CG/CHR/CAL/selection semantics.



##### G.1:4.2.1 - M1 — CG‑FrameContext Card (scope anchor)


**Governs (kit surface):**

* `CG‑FrameContext` and its **binding pins**:

  * `entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩` *(pin set: `PartG.AuthoringMinimal`)*
  * `CNSpecRef.edition`, `CGSpecRef.edition` *(pin set: `PartG.AuthoringMinimal`)*
  * `ReferenceMap` *(cite `G.0:CG‑Spec.ReferenceMap`; do not duplicate semantics)*
  * any declared crossing/policy pins *(pin set: `PartG.CrossingVisibilityPins`)*

**Purpose:** provide the *single scope anchor* used by all downstream cards.

**Notes:** any spec-legality content is **cited** via `A.19.CN (CN‑Spec)` and `G.0 (CG‑Spec)` (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`); this card does not introduce a local “mini‑spec”.



##### G.1:4.2.2 - M2 — SoTA_Set@CG‑Frame (harvester output card)


**Governs (kit surface):**

* `SoTAPaletteDescriptionId` and `SoTA_SetId` bound to `CG‑FrameContext`
* explicit provenance anchors for the set (via `A.10`), and any published UTS stubs/rows when applicable

**Governing pattern:** harvesting discipline and SoTA-pack payload are governed by `G.2`.
In `G.1`, M2 is a *card in the chassis* and a wiring surface; it does not redefine the harvesting method. A relied-on coverage result cites G.2's `CoverageJudgementRef` with its HarvestPolicy basis, counted units and receiving question. M2 supplies no alternative family count.



##### G.1:4.2.3 - M3 — VariantPool (candidate inventory + emitter trace)


**Governs (kit surface):**

* `VariantPoolId` bound to `CG‑FrameContext`
* per‑candidate minimal traceability fields (emitter identity, `EmitterPolicyRef` (policy‑id/ref; defined by the governing pattern), method/generator refs when declared, edition pins, provenance anchors)
* optional, per‑candidate **assurance preview pointers** (e.g., `PathSliceId?` and/or `SCRId?` when early assurance is recorded) and optional **QD/Open‑Ended scaffolding stubs** (only when introduced by explicit `GPatternExtension` blocks)

**Guardrails (via G.Core):**

* tri‑state eligibility handling, penalties routing, crossing visibility, and set‑return constraints are not defined here; they are enforced via `G.Core` conformance.

**Governing pattern for method payload:** method‑specific emitter semantics remain in their governing definitions, cited through `Extensions` (e.g., the relevant `C.17`, `C.18`, and `C.19` definitions).
M3 MUST remain method‑agnostic in its core definition: it is an inventory surface, not an algorithm spec.



##### G.1:4.2.4 - M4 — Shortlist (selector output)


**Governs (kit surface):**

* `ShortlistId` bound to `CG‑FrameContext`
* a selected set of candidates plus rationale and SCR-addressable audit references required by G.5 (`SCRId` required; `DRRId` optional; cite `PathId/PathSliceId` when applicable). Add assurance records only when an actual named assurance claim is current.
* optional **front metadata or archive metadata** needed for reproducibility when used: ε‑front parameters and/or archive snapshot hooks, with governing-definition assignment through `G.5` / `C.18` / `C.19` (no local semantics in `G.1`)

**Governing pattern:** selection/dispatch semantics are governed by `G.5`.
M4 MUST preserve *set‑return semantics* (as governed by `G.Core`) and MUST NOT hard‑code a forced singleton outcome.



##### G.1:4.2.5 - M5 — CG‑FrameLibrary (published bindings index)


**Governs (kit surface):**

* `CGFrameLibraryId` bound to `CG‑FrameContext`
* an index of referenced CG‑Frame artefacts ready for reuse:

  * CHR/CAL/LOG bundles (by their ids; semantics governed by `G.3`, `G.4`, `G.8`)
  * published identifiers (UTS rows, Name Cards) per Part‑F governing definitions
  * additional Part‑F binding surfaces (e.g., RoleDescription templates, Concept‑Set rows) by ids locating those surfaces under their governing definitions
  * RSCR test identifiers (e.g., from `F.15`) and worked examples (where applicable)

**Boundary:** M5 is a **kit/library surface**, not shipping. If a shipped pack is needed, governing-definition assignment is `G.10`.



##### G.1:4.2.6 - M6 — RefreshReadiness Card (telemetry hooks + wiring)


**Governs (kit surface):**

* `RefreshReadinessCardId` bound to `CGFrameLibraryId` (and thus to `CG‑FrameContext`)
* `CGKitId` (the versioned kit manifest) binding `M1…M6` into a single reusable unit; it MUST enumerate the card ids and MAY carry references to deprecations/edition bumps minted by the canonical governing definitions
* declared telemetry hooks (what signals are observed, with what pins)
* declared RSCR wiring: which `RSCRTriggerKindId` are relevant (canonical ids), with minimal required payload pins. For a planned baseline, include the `A.15.2` WorkPlan reference and its local baseline locator; filling an independently declared position under `A.15.3` also requires the governing declaration reference, member designator and plan-local filling-row locator.

**Boundary:** orchestration semantics are governed by `G.11`.
M6 prepares *refresh‑readiness metadata* and wiring stubs; it does not define scheduling/priority heuristics.

#### G.1:4.3 - Minimal I/O surface (normative)

| Module | Consumes                                                                    | Produces                                                                               |
| ------ | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| M1     | CG‑Frame brief + `entityOfConcern` + `CNSpecRef/CGSpecRef` (edition‑pinned) | `CG‑FrameContext` + context pins                                                       |
| M2     | discovery inputs + inclusion criteria *(via G.2)*                           | `SoTA_SetId` (+ provenance anchors; optional UTS stubs/rows)                           |
| M3     | `SoTA_SetId` + local constraints + emitter policy pins *(via Extensions)*   | `VariantPoolId` (+ candidate trace/provenance; optional method payload via Extensions) |
| M4     | `VariantPoolId` + acceptance/eligibility surfaces *(via G.4/G.5)*           | `ShortlistId` (selected set / set-result) + rationale refs                                         |
| M5     | `ShortlistId` + CHR/CAL/LOG bundle refs + UTS/Name refs                     | `CGFrameLibraryId` (library index; publish‑ready bindings)                             |
| M6     | telemetry inputs + freshness/decay policy pins + RSCR tests                 | `CGKitId` + `RefreshReadinessCardId` (wiring to `G.11`; no orchestration governance)    |

#### G.1:4.4 - Extensions (pattern‑scoped; non‑core)

All method/discipline/generator specifics MUST be expressed as `GPatternExtension` blocks.

> Guard: `G.1:Ext.*` are **PatternScopeId** values (internal, pattern‑scoped), not new patterns and not new `PatternId`.



##### G.1:4.4.1 - GPatternExtension — `G.1:Ext.HarvesterWiring`


**PatternScopeId:** `G.1:Ext.HarvesterWiring`
**GPatternExtensionId:** `HarvesterWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTAPaletteDescriptionId`
* `SoTA_SetId`
* `CoverageJudgementRef` and its `HarvestPolicyRef` when coverage is consumed
* `ClaimSheetId[]` / `BridgeMatrixId` *(as referenced by the chosen G.2 pack form)*
* `CNSpecRef.edition`, `CGSpecRef.edition` *(already required via `GCorePinSetId.PartG.AuthoringMinimal`)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.SoTAHarvestSynthesis}`
**Notes (wiring‑only):** harvesting semantics (living review funnels, inclusion policy families, SoS indicator families, etc.) are defined by `G.2` and are not duplicated in `G.1`.



##### G.1:4.4.2 - GPatternExtension — `G.1:Ext.ShortlistWiring`


**PatternScopeId:** `G.1:Ext.ShortlistWiring`
**GPatternExtensionId:** `ShortlistWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.4}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ShortlistId`
* `SCRId` *(selector audit reference under G.5; its record carries assurance only when an actual named assurance claim is current under B.3)*
* `DRRId?` *(when a decision‑rationale artefact is minted; otherwise omitted)*
* `TaskSignatureRef?` *(if selection is task‑templated; otherwise omitted)*
* `AcceptanceClauseId[]` *(as referenced from `G.4` outputs)*
* any explicit selector policy pins *(policy‑id/ref; defined by the governing pattern)* when not defaulted (the omitted default cites its governing definition through `G.Core.DefaultGoverningDefinitionIndex`)

**Notes (wiring‑only):** `G.1` does not redefine selection: it binds M4’s output surface to the `G.5` selector/dispatcher kernel.



##### G.1:4.4.3 - GPatternExtension — `G.1:Ext.CreativityCHR`


**PatternScopeId:** `G.1:Ext.CreativityCHR`
**GPatternExtensionId:** `CreativityCHR`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.17`
**Uses:** `{C.17, G.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CHRPackId?` *(if creativity characteristics are published/typed)*
* edition/policy pins required by the chosen creativity characteristic set (governed by `C.17`)

**Notes (wiring‑only):** `G.1` only records which creativity characteristics are used for M3/M4 wiring; legality/typing lives in the CHR governing definitions.



##### G.1:4.4.4 - GPatternExtension — `G.1:Ext.NQD`


**PatternScopeId:** `G.1:Ext.NQD`
**GPatternExtensionId:** `NQD`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy id / ref, as defined by the governing definition)*
* `TaskSignatureRef?` *(when QD is enabled via TaskSignature flags/traits rather than by an external switch)*
* `DHCMethodRef.edition?` *(when illumination/coverage summaries are pinned to a method)*
* `EmitterPolicyRef` *(policy‑id/ref; identifies the chosen emitter policy under its governing definition, e.g., `C.19` when E/E‑LOG is used)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** QD/QD‑adjacent algorithm families and their parameterisations belong to `C.18 and C.19`; `G.1` only fixes the pins needed to make the VariantPool and Shortlist reproducible.



##### G.1:4.4.5 - GPatternExtension — `G.1:Ext.OpenEndedFamilyWiring`


**PatternScopeId:** `G.1:Ext.OpenEndedFamilyWiring`
**GPatternExtensionId:** `OpenEndedFamilyWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2` *(family semantics are governed by SoTA cards; this block only wires pins; selector-side wiring is governed by `G.5`.)*
**Uses:** `{G.2, G.5, C.19, C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyId[]`
* `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
* `EnvironmentValidityRegionRef?`
* `CoEvoCouplerRef[]?`
* `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (wiring‑only):** this block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in `G.1`; it should cite/align with the selector‑side wiring in `G.5:Ext.OpenEndedFamilyWiring`.



##### G.1:4.4.6 - GPatternExtension — `G.1:Ext.RefreshWiring`


**PatternScopeId:** `G.1:Ext.RefreshWiring`
**GPatternExtensionId:** `RefreshWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.11`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `RefreshReadinessCardId`
* `RSCRTestId[]`
* canonical `RSCRTriggerKindId[]` emitted/recorded (aliases only as labels, if any)

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.RefreshOrchestration}`
**Notes (wiring‑only):** M6 declares readiness and wiring; orchestration semantics (queueing, prioritisation, cadence) are governed by `G.11`.



##### G.1:4.4.7 - GPatternExtension — `G.1:Ext.ShippingWiring`


**PatternScopeId:** `G.1:Ext.ShippingWiring`
**GPatternExtensionId:** `ShippingWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.10`
**Uses:** `{G.10}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `CGFrameLibraryId`
* `SoTAPaletteDescriptionId`, `SoTA_SetId`
* `CHRPackId?`, `CALPackId?`, `SoS‑LOGBundleId?`, `ParityReportId?` *(as present in the library index)*
* `EvidenceGraphId?`, `BridgeMatrixId?`, `BridgeCalibrationTableId?` *(when cited by the shipped artefacts)*
* `UTSRowId[]?` *(when any public ids are minted/published)*
* `WorkPlanRef[]?` with local baseline locators *(when a planned baseline is cited by the shipment surface under `A.15.2`)*; include the governing declaration reference, member designator and plan-local filling-row locator when `A.15.3` applies

**Notes (wiring‑only):** this block does not define shipping; it only records the minimum wiring from the chassis/library index to `G.10` when shipping is performed.

### G.1:5 - Archetypal Grounding — Tell–Show–Show (informative)

**Tell.** Use the six‑card chassis to make a CG‑Frame authoring effort reproducible: a scoped SoTA set, a traceable candidate pool, a set‑return shortlist, a publishable library index, and refresh readiness—without redefining spec-legality/selection/refresh governing definitions.

**Show A (R&D multi‑criteria decisions; post‑2015 SoTA practice).**

* **M1:** define `CG‑FrameContext` for “R&D decision options”, pin `CNSpecRef/CGSpecRef` editions, and publish `entityOfConcern` + `ReferencePlane`.
* **M2:** build `SoTA_SetId` via `G.2` using a living‑review style funnel (e.g., PRISMA‑like trace + update cadence) and publish UTS stubs for reusable constructs.
* **M3:** emit a `VariantPoolId` where each candidate cites its emitter policy and provenance; if QD is used, wire `DescriptorMapRef.edition` and `DistanceDefRef.edition` via `G.1:Ext.NQD`.
* **M4:** produce `ShortlistId` as a selected-set / shortlist surface via `G.5`, with acceptance predicates sourced from `G.4`.
* **M5:** publish a `CGFrameLibraryId` indexing the chosen CHR/CAL/LOG bundles and UTS rows; register RSCR tests.
* **M6:** declare refresh readiness (telemetry pins + canonical RSCR trigger kinds) and wire to `G.11`.

**Show B (clinical operations; safety‑first acceptability).**

* **M1:** scope a CG‑Frame around dose adjustment decisions; pin legality and evidence minima explicitly.
* **M2:** harvest SoTA models and safety constraints as a reconstructible set (governed by `G.2`).
* **M3:** generate policy‑constrained candidate protocols; emitter trace and evidence pins are mandatory.
* **M4:** shortlist remains a set; “choose one” remains an explicit policy decision, not silently baked into the generator.
* **M5/M6:** publish and wire refresh (decay events, policy changes, and evidence updates retrigger along the P2W path).

### G.1:6 - Bias‑Annotation (informative)

* **Recency bias:** “newest paper wins” (mitigate with explicit inclusion criteria and update cadence in `G.2` wiring).
* **Novelty bias:** over‑rewarding novelty at the expense of legality/assurance (mitigate by making acceptance and assurance pins explicit and governed).
* **Algorithmic favoritism:** baking a preferred generator into “the chassis” (mitigate by keeping M3 method‑agnostic and putting method‑specific wiring into Extensions).
* **Scalarisation bias:** collapsing selected sets or partial orders into a single score (mitigate by set‑return discipline pinned through `G.Core`).
* **Hidden‑crossing bias:** implicit reuse across contexts (mitigate by explicit crossing pins and Bridge‑only routing via `G.Core`).

### G.1:7 - Conformance Checklist (normative)

| ConformanceId     | Statement   |
| ----------------- | ----------- |
| **CC‑G1‑CoreRef** | The pattern MUST satisfy the **effective** `CoreConformanceIds` implied by `G.1:4.1` (`GCoreConformanceProfileId` expansion + deltas), per `G.Core` expansion rules.   |
| CC‑G1‑01          | The reusable CG-Frame kit MUST include all six cards `M1…M6` with stable ids **and** a versioned kit manifest `CGKitId`, including at minimum: `{CGKitId, CG‑FrameContext, SoTAPaletteDescriptionId, SoTA_SetId, VariantPoolId, ShortlistId, CGFrameLibraryId, RefreshReadinessCardId}`.  |
| CC‑G1‑02          | `M1` MUST bind the kit to a single `CG‑FrameContext` and MUST expose the required pins from `GCorePinSetId.PartG.AuthoringMinimal` (including `entityOfConcern` and `CNSpecRef/CGSpecRef` editions). `M1` MUST also expose (or explicitly cite) a `ReferenceMap` surface and MUST NOT restate its semantics (cite `G.0:CG‑Spec.ReferenceMap`).  |
| CC‑G1‑03          | `M2` MUST be wired to `G.2` (or explicitly cite the `G.2` artefacts governed by cited patterns) and MUST be reconstructible as a scoped set, including `SoTAPaletteDescriptionId` + `SoTA_SetId` (not free‑floating prose). Provenance MUST be anchored via `A.10` for the emitted set.  |
| CC‑G1‑04          | `M3` MUST record emitter provenance as a wiring surface, including `EmitterPolicyRef` (policy‑id/ref), edition pins, and provenance anchors (via `A.10`). Any method‑specific fields MUST be introduced only via `GPatternExtension` blocks.   |
| CC‑G1‑05          | `M4` MUST be wired to `G.5` (or explicitly cite `G.5` artefacts governed by cited patterns) and MUST preserve set-result outcomes. `SCRId` MUST be present (or recoverable from an explicitly cited SCR record) so the G.5 audit references are addressable; assurance content is required only for an actual named assurance claim; `DRRId` SHOULD be present when a decision‑rationale artefact is minted.   |
| CC‑G1‑06          | `M5` MUST publish a library/index surface that points to referenced CHR/CAL/LOG artefacts and to any minted public ids (`UTSRowId[]`, Name Cards) via the canonical governing definitions (Part F), without introducing shadow specs (delegation target: `CC‑GCORE‑CN‑CG‑1` via `CC‑G1‑CoreRef`).    |
| CC‑G1‑07          | `M6` MUST publish `CGKitId` and expose refresh-readiness wiring: canonical `RSCRTriggerKindId[]` applicability, minimal payload pins and RSCR test ids. Planned baseline references MUST follow `G.1:4.2.6`, including the additional references required when `A.15.3` applies; orchestration semantics MUST be cited to `G.11`. |
| CC‑G1‑08          | Any method/discipline/generator specificity in `G.1` MUST be located in `G.1:4.4` as `GPatternExtension` blocks with `PatternScopeId`, `GPatternExtensionKind`, and `GoverningPatternId` (or `governing pattern not yet selected` only for Phase-3 seeds). If QD/illumination or Open‑Ended generator families are declared, the corresponding extension blocks MUST be present and MUST carry the edition and policy pins required by the governing pattern. |

### G.1:8 - Common Anti‑Patterns and How to Avoid Them (informative)

* **Anti‑pattern: “Shadow CN/CG spec inside the chassis.”**
  *Avoid:* keep CN/CG as cited governing spec refs; use pins and governing definition references only.

* **Anti‑pattern: “Chassis hard‑codes a favourite algorithm.”**
  *Avoid:* keep M3 core method‑agnostic; add algorithm families only via Extensions with explicit governing patterns and edition pins.

* **Anti‑pattern: “Shortlist = one winner.”**
  *Avoid:* preserve selected-set returns; any singleton choice must be an explicit downstream decision rule (policy‑bound).

* **Anti‑pattern: “Refresh plan described as prose triggers.”**
  *Avoid:* record canonical `RSCRTriggerKindId` and payload pins; aliases only as labels and only if docked.

* **Anti-pattern: “Packaging implies shipping governance.”**
  *Avoid:* treat M5 as a library index; treat M6 as readiness wiring; ship only via `G.10`.

### G.1:9 - Consequences (informative)

* **Repeatable authoring:** CG‑Frame work becomes reconstructible: what exists, what it depends on, and how it is refreshed.
* **Method pluralism with discipline:** multiple generator/selector families can coexist without turning the chassis into a shadow method spec.
* **Better reuse:** outputs land directly in published artefacts (UTS/Name/RSCR‑ready) rather than remaining local notes.
* **Lower refactor cost:** method-wiring changes localise to Extensions; core invariants remain stable under their governing definitions.

### G.1:10 - Rationale (informative)

* **Why six cards?** It matches the minimal decomposition needed to keep scope, harvesting, generation, selection, publication, and refresh **explicitly separable** (and thus auditable and evolvable).
* **Why “kit/index” rather than “pack”?** A CG‑Frame authoring effort must stay modular; shipping is a separate governing boundary (`G.10`).
* **Why put method-specific wiring into Extensions?** It prevents conflating (i) universal invariants, (ii) frame‑specific kit surfaces, and (iii) method/generator families.
* **Why working‑model first?** Many CG‑Frames fail due to premature formalism; a chassis with didactic micro‑examples improves correctness of pins, names, and boundaries before deep formalisation.

### G.1:11 - SoTA‑Echoing (informative)

This chassis is designed to stay compatible with modern (post‑2015) practice without confusing “SoTA” with “currently popular”:

* **Evidence synthesis:** living systematic review protocols (e.g., PRISMA‑style traceability and update cadence) map naturally to M2 wiring governed by `G.2`.
* **Quality‑Diversity and archives:** modern QD families (MAP‑Elites‑class, CMA‑ME‑class, and related archive‑based exploration) fit as M3/M4 extensions (`C.18`/`C.19`) because they require explicit descriptor/distance/insertion pins and preserve set‑valued outcomes.
* **Open‑ended exploration:** post‑2015 open‑endedness systems (POET‑class, paired/adversarial environment generation lines, and modern curriculum‑generation approaches) fit when treated as generator‑family wiring (governed elsewhere) rather than as chassis semantics.
* **Set‑valued decision outputs:** modern multi‑objective and set‑valued evaluation practices align with the `G.Core` set‑return discipline, preventing hidden scalarisation.
* **Governed traceability:** contemporary reproducibility and accountability norms (mechanism disclosure, provenance anchors, and audit trails) are supported via pinned policies/editions and explicit module boundaries, without introducing data‑governance machinery.

### G.1:12 - Relations

**Builds on:** `G.Core`, `E.8`, `E.10`, `E.19`.
**Uses:** `A.10 (Provenance Anchors)`, `A.15.2` (WorkPlan baselines), `A.15.3` (planned fillings of independently declared positions), `A.19.CN (CN‑Spec)`, `G.0 (CG‑Spec)`, `G.2 (SoTA Synthesis Pack)`, `G.3 (CHR Pack@CG‑Frame)`, `G.4 (CAL Pack@CG‑Frame)`, `G.5 (Selector & Dispatch)`, `G.10 (Shipping)`, `G.11 (Refresh Orchestration)`, and (via Extensions) `C.17, C.18, and C.19`.
**Publishes to / consumes from:** Part‑F publication surfaces (UTS, naming, RSCR tests, Role/Concept artefacts) as cited by their governing definitions.

### G.1:End

## G.2 - Harvest and Synthesize SoTA for a CG-Frame

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative *(unless explicitly marked informative)*
>
> **Purpose.** Provide a repeatable, auditable way to **discover**, **triage**, and **synthesize** state‑of‑the‑art (SoTA) across competing `Tradition` lineages *before* minting CHR/CAL/LOG assets for a `CG‑Frame`.
>
> **Start here.** Write the question the receiving CHR, CAL or selector work must answer. Before counting coverage, fix the source population and what counts as the same family. Distill the first source claims with their editions, evidence and limits, keeping competing lineages separate. The first useful result is a claim set that can answer part of that question and expose what is still missing. Use the manifest below when developing it into a conforming synthesis pack; a single-source fact lookup can return its source directly without creating such a pack.
> The primary output is a **`SoTA Synthesis Pack@CG‑Frame`** that feeds:
>
> * naming/publication (UTS),
> * CHR authoring (G.3),
> * CAL authoring (G.4),
> * method/generator registries and dispatch (G.5).
>
> **Scope note.** This pattern **governs** the harvesting + synthesis *generator* in Part G. Use **G.10** to ship the pack and **G.11** to orchestrate refresh.
>
> **Terminology note (normative).** In normative clauses below, **`Tradition`** refers to the *Tech* token `Tradition` (a plural lineage with internally coherent commitments). Plain “tradition” is allowed only as a 1:1 synonym.

### G.2:1 - Problem frame

A team extends FPF into a new `CG‑Frame`. The relevant literature is typically:

* **plural** (multiple `Tradition` lineages with incompatible commitments),
* **source- and use-sensitive** (results depend on the exact source and edition, claim region, EntityOfConcern, comparison basis, evidence, and receiving use),
* **method‑heterogeneous** (different evidence styles, operator sets, and validity regions),
* **time‑sensitive** (rapid drift post‑2015; frequent benchmark/protocol shifts).

Downstream Part-G work in CHR, CAL, selection, shipping, and refresh depends on citation-ready claims that keep each exact CG-frame, source edition, claim region, EntityOfConcern, comparison basis, evidence anchor, and actual cross-source relation recoverable.

### G.2:2 - Problem

How can we systematically assemble a SoTA view that is:

1. **pluralist but comparable** (plurality preserved; comparability is achieved only via explicit crossings),
2. **evidence‑addressable** (claims cite auditable evidence surfaces and anchors),
3. **actionable** (produces inventories and citable publication forms usable in G.3, G.4, and G.5 without treating a card as a meaning container or selector authority),
4. **refreshable** (editions/policies/windows are pinned so RSCR/refresh can re‑audit and re‑run without semantic drift)?

### G.2:3 - Forces

* **Pluralism vs. consolidation.** Consolidation is valuable, but unqualified fusion destroys meaning.
* **Breadth vs. load‑bearing depth.** Too broad becomes shallow; too deep misses rival lineages.
* **Recency vs. stability.** Freshness matters, yet durable “backbone” claims must be identified and kept visible.
* **Pedagogy vs. rigour.** Outputs must be teachable enough to support review, while remaining audit‑ready.
* **Authoring vs. operations.** This pattern governs authoring; use the applicable Work and decision patterns for operational runs and decisions.

### G.2:4 - Solution

#### G.2:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  CorePinSetIds := {GCorePinSetId.PartG.CrossingVisibilityPins}, // expands only for actual channel/receiving-use conditions under G.Core:4.2.3; no crossing means no crossing pins

  CorePinsRequired := {
    // Scope pins (G.2‑specific)
    CGFrameId, // identifies the exact CG-frame, which is the declared framing episteme; its cited ClaimGraph keeps source and edition, claim regions, EntityOfConcern, comparison basis, and intended use recoverable
    Tradition[],
    entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
    SoTA_SetId,
    SoTAPaletteDescriptionId,

    // Evidence / provenance pins (G.2‑specific)
    CorpusLedgerId,
    FlowRecordId,
    EvidenceAnchorRef[],
    EvidenceGraphId?,

    // Crossing / synthesis pins (delta beyond CorePinSetIds; only when used)
    GammaEpistSynthId[]?,

    // Edition / policy pins (only when used)
    HarvestPolicyRef?, // required when a coverage judgement is made
    CoverageJudgementRef?, // the pack judgement, required for a relied-on coverage result
    DistanceDefRef.edition?,
    InclusionCriteriaId?,
    ScreeningRubricId?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩
```

*(RSCR payload pins: `ClaimSheetId[]`, `SoTA_SetId`, `SoTAPaletteDescriptionId`, `BridgeMatrixId?`, `GammaEpistSynthId[]?`, `UTSRowId[]?`, `DistanceDefRef.edition?`, `HarvestPolicyRef?`, `InclusionCriteriaId?`, `ScreeningRubricId?`, `PathId/PathSliceId?` when path‑citable evidence or a stable freshness window is pinned.)*

**Pattern‑local default rules (governed by this pattern; not a Part‑G‑wide `DefaultId`).**

`FamilyCoverageFloorK := 3` *(unless explicitly overridden by `HarvestPolicyRef` and recorded in `FlowRecord`)*. This threshold supplies no counted population or same-family rule; those must be explicit before a coverage judgement. An undefined basis is unassessable, not a measured failure. Whenever coverage is judged, `HarvestPolicyRef` is required even when k uses this fallback; its applicability, receiving question, counted population/scope, grouping and same-family equivalence must be fixed before counting. An override changes k, not the unit or the independent pluralism duties.

**Counted-family basis.** The HarvestPolicy defines which candidates enter the counted population and when two entries represent the same family for this receiving question. Count equivalence classes under that rule. Repeated cards, aliases and source references for one family add zero. A combined method/generator population needs one receiving purpose and an overlap rule: a generator that is also a method is not counted twice unless the policy deliberately defines separate role-qualified units and justifies that interpretation. Freeze this basis before inspecting the count; changing it to turn a failure into three is not a repair of coverage.

The pack's coverage judgement carries the policy/edition, counted units, deduplication basis, count, k and pass/fail result, or the exact missing basis when unassessable. Give this existing pack component a local `CoverageJudgementRef` for citation. Evaluate lineage and materially distinct entry plurality separately. Cards and downstream consumers cite this same judgement instead of choosing their own unit. Compare counts across packs only when their bases match, or after an explicitly justified common-basis recount.

#### G.2:4.2 - Kit: `SoTA Synthesis Pack@CG‑Frame` (surface governed by this pattern)

A conforming `G.2` publication produces a **notation‑independent pack** whose internal organisation is free, but whose exported **named components and views** are stable and citable:

Each named component is addressable via a stable **pack‑local identifier** (e.g., `CorpusLedgerId`, `ClaimSheetId`, `FlowRecordId`) for citation and RSCR scoping. If any component is minted/evolved as a **public id**, it is published and cited via `UTSRowId[]` per `CC‑GCORE‑UTS‑1` (delegation).

0. **`SoTA_Set@CG‑Frame`** *(export view; “M2 output” consumed downstream)*
   A read‑optimised view over the harvested candidate set that downstream generator/selector work treats as the “harvester output set”.
   **Constraint (normative):** `SoTA_Set@CG‑Frame` **MUST** be reconstructible from pack components by id (no “hidden extra set”). Its coverage result cites the pack's `CoverageJudgementRef`, including its fixed HarvestPolicy basis; the export view does not redefine family membership.

1. **`G.2a CorpusLedger`**
   Ledger of candidate sources. Each row names the exact source and edition, claim region used, triage status (for example, include, park, or retire), evidence locator, and rationale for this CG-frame and receiving use.

2. **`G.2b ClaimSheets[Tradition]`**
   Typed Claim Sheets per `Tradition`, each with:

   * exact source and edition, claim region, effective ReferenceScheme where meaning matters, EntityOfConcern, and comparison basis for the stated use,
   * explicit evidence anchors/citations (A.10 and/or EvidenceGraph refs when available),
   * explicit freshness window notes and risk/trust cues *(cite `B.3` governing definitions when using trust/decay language)*.

3. **`G.2c OperatorAndObjectInventory`**
   Inventory of candidate CHR terms (characteristics/scales/coordinates) and candidate CAL operators/flows *as stubs* for downstream authoring.

4. **`G.2d BridgeMatrix`**
   A citable alignment/divergence surface across `Tradition`×`Tradition`, with explicit losses and row scopes.
   If any row asserts substitution or fusion across sources or across `Tradition` records, the pack **MUST** attach a `GammaEpistSynthId` record (alias: **`G.2‑F`**) per `G.2:Ext.GammaEpistSynthesis` (no silent fusion).

5. **`G.2e MicroExamples`**
   Worked micro-examples for load-bearing claims. Each names the exact source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its evidence carrier or A.10 evidence-provenance path; and annotates applicable assurance types (`TA`, `VA`, or `LA`). The example card is only a publication form for those claims.

6. **`G.2f UTSProposals`**
   Draft Name Cards + Minimal Definitional Sheets (MDS) + alias proposals (incl. concept‑set linkage where applicable), with the required publication pins.

7. **`G.2g entityOfConcern Map`**
   Map from key terms/claims/public ids to `GroundingHolon`, `ReferencePlane`, and minimal reference cues for later CHR/CAL authoring.

8. **`G.2h PRISMA Flow Record`**
   A screening/eligibility trail for how sources entered the pack (method‑profile is allowed; see Extensions).
   *(Name is historical; the artefact remains notation‑independent.)* The pack coverage judgement and its policy basis are recoverable here, separately from the lineage and material-entry pluralism results.

9. **`G.2i SoSIndicatorFamilies`**
   Indicator *families* as variants (windows/constraints/assumptions) **with explicit Acceptance branches per variant** (branch ids/labels only; threshold semantics belong to CAL governing definitions).

10. **`G.2j MethodFamilyCards`**
    Candidate method families with a shared signature and a plurality of implementations, each with validity regions, cost/complexity notes, and known failure modes.
    When the pack targets downstream registry/dispatch, MethodFamily cards **SHOULD** include the declared refs and pins `G.5` needs (eligibility predicate refs, assurance profile cues, and the pack ids that justify the family).

11. **`G.2k GeneratorFamilyCards`** *(if applicable)*
    Candidate generator families for environment/task generation with declared validity regions and transfer hooks.

12. **`G.2l Annexes`** *(optional; governing-definition-cited; see Extensions)*
    For example: QD/NQD annexes, discipline‑specific indicator annexes, interop forms.

**SoTAPaletteDescription** *(export view; required downstream)*
A view‑friendly description object (pack‑local `SoTAPaletteDescriptionId`) that binds together:

* the `SoTA_Set@CG‑Frame` view,
* `ClaimSheetId[]`, `OperatorAndObjectInventory`, `BridgeMatrixId?`,
* `SoSIndicatorFamilies` (with variant/branch structure),
* `MethodFamilyCards` / `GeneratorFamilyCards?`,
* `MicroExamples`, `UTSProposals`,
* and the `entityOfConcern Map` for citation and later CHR/CAL authoring.

**Note (normative intent):** this is the primary “consumable surface” for `G.3/G.4/G.5`; it prevents downstream patterns from scraping free prose.

**Editorial template: 1‑page “SoTA Sheet” per Tradition (informative).**
When authoring `ClaimSheets[Tradition]`, teams often benefit from a single‑page template: scope + claims + evidence anchors + validity region + failure modes + freshness window + cross‑Tradition reuse notes + pointers to micro‑examples.

#### G.2:4.3 - Harvester loop (conceptual choreography; pattern-governed)

A conforming `G.2` pack publication is built by iterating the following conceptual loop until the declared gates are satisfied:

1. **Declare scope and plurality.**
   Identify the exact CG-frame (the declared framing episteme), the initial `Tradition` set, each intended claim region and EntityOfConcern, the comparison basis, and the receiving use. Record the cited CG-frame and source editions and evidence anchors in the pack pins rather than hiding them in a generic context field. Before counting, fix the HarvestPolicy's receiving question, counted population, grouping and same-family equivalence, including overlap handling for a combined population.

2. **Discover and triage sources (ledger‑first).**
   Populate `CorpusLedger` via:

   * adding seed sources,
   * expansion via citation chaining and keyword family exploration,
   * pruning using load‑bearing relevance tests tied to the declared CG‑Frame scope.

3. **Distill claims per `Tradition`.**
   For each `Tradition`, author a Claim Sheet that preserves internal commitments and cites evidence anchors. Do not fuse cross‑`Tradition` claims at this stage.

4. **Inventory operators/objects for downstream authoring.**
   Extract candidate measurement terms and operator stubs for later CHR/CAL authoring (without asserting legality or thresholds locally).

5. **Build alignment/divergence surfaces.**
   Where reuse across `Tradition` is desired, record the obtaining correspondence and its exact basis in `BridgeMatrix`: F.9 for sense correspondence, C.3.3 for kind correspondence, or the direct rule for a plane relation, as actually used. State preserved distinctions and losses for the receiving question. Consolidation requires explicit alignment proof. Add bundle or gate anchors only for an independently applicable E.18 flow crossing or A.21 gate, under `CC‑GCORE‑CROSS‑1`.

6. **(Alias: G.2‑F) Produce Γ_epist synthesis records when fusion/substitution is asserted.**
   If a `G.2` pack publication asserts fusion or substitution across sources or across `Tradition` records (beyond mere “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records per `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit object alignment refs + assurance tuple refs), and it **MUST** keep penalties routed to `R_eff` only by delegation (`CC‑GCORE‑PEN‑1`).

7. **Publish teachable micro‑groundings.**
   Attach worked micro-examples to load-bearing claims, each tied to the exact source and edition, claim region, EntityOfConcern, comparison basis, intended use, and evidence carrier or A.10 evidence-provenance path.

8. **Apply gates and record repairs.**
   Apply that fixed HarvestPolicy basis and count its distinct units before comparing coverage with `FamilyCoverageFloorK` (and apply any optional diversity-by-distance gate under its own basis). Missing count semantics returns an unassessable result and the exact missing basis, not an instruction to search more. If a defined gate fails, the pack **MUST**:
   * record the failure and the repair iteration in `FlowRecord` and `CorpusLedger`,
   * pin the updated `HarvestPolicyRef` / criteria ids (if changed),
   * iterate the loop rather than silently weakening the gate.

9. **Emit hand‑off manifests and export views.**
   Produce explicit manifests to:

   * `G.3` (CHR authoring),
   * `G.4` (CAL authoring),
   * `G.5` (registry/dispatch),

   so that downstream work can cite pack components by id rather than re‑authoring them. Each relied-on coverage result carries the same `CoverageJudgementRef` and its policy basis; a downstream method-selection use cannot treat a combined method/generator count as a method-only count.
   The pack **MUST** also export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as the default downstream consumption surfaces (ids pinned).

#### G.2:4.4 - Interfaces (minimal I/O Standard)

| Interface         | Consumes                                                      | Produces                                                                    |
| ----------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- |
| **G.2-1 Harvest** | exact CG-frame (the declared framing episteme) identified by `CGFrameId`, initial `Tradition[]`, source edition and claim-region boundary, EntityOfConcern, comparison basis, receiving use, `HarvestPolicyRef` whenever coverage is judged | `SoTA Synthesis Pack@CG-Frame` (G.2a-G.2l) |
| **G.2‑2 Extend**  | existing Pack + new sources/anchors + updated policy pins     | updated Pack + RSCR‑relevant trigger emissions (canonical kinds)            |
| **G.2‑3 HandOff** | Pack                                                          | `CHR‑handoff` (to G.3), `CAL‑handoff` (to G.4), `Registry‑handoff` (to G.5) |

*Note:* Orchestration of re‑runs is governed by `G.11`; this pattern only defines what a conforming (re)harvest produces and what pins it must expose.

#### G.2:4.5 - Extensions (pattern‑scoped; non‑core)

`Extensions` are pattern‑scoped annexes. They do not introduce Part‑G‑wide norms; they declare the additional pins required when those semantics are active and cite the corresponding governing patterns.

##### G.2:4.5.1 - GPatternExtension: GammaEpistSynthesis

**PatternScopeId:** `G.2:Ext.GammaEpistSynthesis`
**GPatternExtensionId:** `GammaEpistSynthesis`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.2`
**Uses:** `{G.Core, B.3, F.9, G.6}` *(penalty routing + trust/decay cues + bridges/CL + evidence path citation when used)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GammaEpistSynthId[]` *(pack‑local ids of synthesis records; emitted iff fusion/substitution is asserted)*
* `EvidenceAnchorRef[]` *(provenance union; evidence carriers cited by A.10 evidence-provenance paths)*
* `BridgeMatrixId` and `BridgeCardId[]` *(explicit object alignment references when crossing is involved)*
* `CL/CL^plane` and `Φ/Ψ/Φ_plane policy-ids` when required by the cited crossing or actually used loss model *(semantics and penalties → `R_eff` remain governed by the cited definitions)*
* `PathId/PathSliceId?` *(only when citing via `G.6`)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.ReferencePlaneEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`

**Notes (normative intent; duplication‑avoidant):**
* The auditable synthesis record identified by `GammaEpistSynthId` binds: (i) provenance union, (ii) explicit object alignment refs, (iii) assurance tuple refs (via their governing definitions) for each asserted fusion/substitution. A B.1.3 `Γ_epist^synth` application and its returned episteme remain separate from this record.
* This extension cites the `Γ‑fold`, `Φ`, and penalty rules through `G.Core` and exposes the pins needed for replay. When B.3/C.2.2 supplies no justified common numerical score or loss calculation, retain the separate support, actual mapping limitations and bounded assurance conclusion; a synthesis record does not supply the missing model.

##### G.2:4.5.2 - GPatternExtension: HarvestProtocols

**PatternScopeId:** `G.2:Ext.HarvestProtocols`
**GPatternExtensionId:** `HarvestProtocols`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `G.2`
**Uses:** `{B.3, A.10}` *(for freshness/decay and provenance anchors, when protocol requires them explicitly)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `HarvestPolicyRef` *(declares the chosen protocol family and its parameters)*
* `FlowRecordId` *(protocol‑specific profile id or rubric id may be attached here)*
* `InclusionCriteriaId` / `ScreeningRubricId` *(ids only; semantics remain local to the protocol family)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension binds a declared protocol profile to the pack’s `FlowRecord` without redefining evidence semantics.

##### G.2:4.5.3 - GPatternExtension: DHCAlignmentHooks

**PatternScopeId:** `G.2:Ext.DHCAlignmentHooks`
**GPatternExtensionId:** `DHCAlignmentHooks`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `C.21` *(DHC semantics are governed by C.21)*
**Uses:** `{C.21, G.6, G.7}` *(DHC series + evidence path citations + bridge/CL regimes when alignment density is claimed)*
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DHCMethodRef.edition`
* `WindowRef?` *(if the DHC series is windowed)*
* exact F.17 `SchemeSenseCell` refs used by the DHC comparison set (use `SenseCellAddressRef` where a durable address is needed; cite `UTSRowId[]` only for independently public ids)
* `UTSRowId[]?` *(only if a cited cell or series id is independently minted or evolved as a public id)*
* `PathId[]` / `PathSliceId[]` *(when alignment summaries cite evidence paths via G.6)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TelemetryDelta}`

**Notes (extension discipline):**
* If DHC alignment summaries are emitted, this extension ensures the DHC method edition and the cited evidence paths are visible.
* AlignmentDensity uses C.21's Unit `obtaining_relations/100_compared_cells`: fix the exact compared F.17 cell set and count the exact obtaining directed F.9 relations, retaining each relation's orientation and admitted-use qualifier. Keep observed loss in its evidence account. A CL calibration label does not include or exclude a relation by itself. Any independently justified receiving-use filter must name its own policy and resulting population; it is not a C.21 CL threshold.
* For example, three obtaining directed relations in a fixed set of 100 compared cells give a density of 3 in that Unit. Changing a CL label while relation truth, population and admitted-use qualifier remain fixed leaves the density 3. A fourth calibration row labelled CL=2 with no obtaining relation adds nothing. If a use condition actually changes which relations qualify, restate that changed population before comparing densities.

##### G.2:4.5.4 - GPatternExtension: NQDAnnex

**PatternScopeId:** `G.2:Ext.NQDAnnex`
**GPatternExtensionId:** `NQDAnnex`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` *(NQD-CAL semantics are governed by C.18; explore/exploit logging is governed by C.19 when used)*
**Uses:** `{C.18, C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `InsertionPolicyRef` *(policy‑id/ref)*
* `EmitterPolicyRef` *(policy‑id/ref)*
* `TaskSignatureRef?` *(when QD mode is trait‑gated)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**Notes (extension discipline):**
* This extension only pins the required references for replayability; it does not redefine QD semantics, dominance, or acceptance rules.

##### G.2:4.5.5 - GPatternExtension: InteropForms

**PatternScopeId:** `G.2:Ext.InteropForms`
**GPatternExtensionId:** `InteropForms`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `MappingPolicyRef` *(policy‑id/ref)*
* `UTSRowId[]` *(for published external ids/aliases where relevant)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`

**Notes (extension discipline):**
* Interop affects only representation and citation routes; it must not introduce alternate legality gates or acceptance semantics.

#### G.2:4.6 - Palette first

- `SoTAPaletteDescription` is one plurality-preserving palette.
- It is not by itself one `Front`, one `Archive`, or one `Shortlist`.
- When that palette's members are traditions, `TraditionPalette` is the reader-facing tradition-only palette head over the same palette declaration, not one second governing definition. For methods, hypotheses, or other members, keep `SoTAPaletteDescription` or `Palette + SubjectKind` explicit instead.
- Traditions remain in the palette until a later surface declares comparison, retention, or choice semantics explicitly.
- `TraditionFront` is one derived view over the declared palette under one declared `Q`; the `Q` basis stays pinned separately and the view does not rename `Tradition` or `SoTAPaletteDescription`.
- `TraditionArchive` is one derived retention view over that same palette under one declared reachability or coverage rule; that rule stays pinned separately and the view does not turn the palette into one archive by default.
- When one derived tradition view is shown, keep the base palette recoverable at the same time.
- When comparison or retention needs richer geometry or atlas language, treat that as support for the derivation rather than as the default meaning of the palette.
- A reader should be able to say both `this is the palette` and `this is the derived tradition view currently being shown` without collapsing those two objects.

#### G.2:4.7 - Optional atlas interpretation of a declared palette

Use `TraditionAtlasView` only when the reader needs several derived views or interpretive qualifiers together to understand a grouping, omission risk or comparison boundary. Otherwise use the palette and its declared front, archive or shortlist, or the thinner `DeclaredSubstrateInterpretiveView`. A naming-only question belongs to F.18.

`TraditionAtlasView` specializes `DeclaredSubstrateAtlasView` under A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW and retains that declaration by value: the base palette, active source set or result, `TypedSetViews` when several declared views are combined, the space/map references and interpretive qualifiers actually used, and the reason the thinner view is insufficient. Cite `SearchSpaceRef` or `OutcomeSpaceRef` for the corresponding declared spaces. Add `SpaceMetricRef`, `TransitionRelationRef` and `BridgeDistortionNote` only for the comparison, reachability, transition or cross-scale claim that needs them. An `OutcomeMapRef` identifies a mapping from the stated result into an outcome/effect space; it does not turn the palette or result into that space. Their formal claims retain their own governing definitions.

If the interpretation changes the base source-to-outcome relation or its distortion, reopen the substrate declaration. Different atlas views may use different spaces, metrics, relations or mathematical traditions; one view does not settle those choices for every other view.

### G.2:5 - Archetypal Grounding (System / Episteme)

| Template element   | `U.System` illustration                                                                                                                                                                                                                                                  | `U.Episteme` illustration                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Tell** | A safety engineering team needs to choose a control stack across robust-control, learning-based, and formal-verification lineages. It identifies the exact CG-frame (the declared framing episteme), vehicle and operating-envelope EntityOfConcern, source editions, claim regions, test or comparison basis, evidence anchors, and intended decision use. | A research group synthesizes SoTA on decision quality across named causal, evidential, bounded-rationality, and active-inference lineages, keeping each source edition, local claim, evidence norm, comparison basis, and intended research use explicit. |
| **Show (failure)** | The team merges source-local terms, treats incompatible test protocols and populations as comparable, and collapses partially ordered trade-offs into one unqualified score. A later safety review cannot recover which source, claim region, basis, or evidence supported the choice. | The group publishes one “best” metric and retrofits definitions to it. Conflicting claims cannot be traced because source editions, evidence anchors, comparison bases, and any actual cross-source relation were never made explicit. |
| **Show (repair)** | Keep parallel Claim Sheets with exact sources, editions, claim regions, EntitiesOfConcern, comparison bases, and evidence. Cite an F.9 Bridge and loss only for an actual relation. Authors of CHR, CAL, and selection methods can then use the citable claims without attributing authority to a card. | Preserve plural claims, represent indicators as families or variants, and expose freshness and evidence. Any justified alignment names its exact cells and obtaining relation; the card or matrix merely represents that result. |

#### G.2:5.1 - Count one pack under a declared basis

Consider this illustrative control-stack pack, extending the System case above. These are stipulated source entries for a counting example, not a finding that a real corpus has adequate breadth.

| Entry and distinct claim region | Lineage | Declared family unit |
| --- | --- | --- |
| e1: robust controller's operating-envelope claim | robust control | method M-R |
| e2: that family's distinct disturbance-rejection claim | robust control | method M-R |
| e3: learned controller's adaptation claim | learning-based control | method M-L |
| e4: scenario generator's counterexample-generation claim | formal verification | generator G-S |

For the question “which control-method families can be selected?”, policy P-method counts method families only and equates entries exactly when they name the same declared method-family unit. The classes are {e1,e2} and {e3}: count 2, below k=3. Additional cards for e1 or citations for M-R leave the count at 2.

For the different question “which method and scenario-generator families can support building and evaluating this control stack?”, policy P-combined includes the three declared units M-R, M-L and G-S. Its overlap rule merges repeated references to one unit; these three units are stipulated distinct and G-S is not also M-R or M-L. Count 3 meets k=3 for that receiving purpose. This is not a passing method-only judgement and cannot be substituted after P-method fails. If one generator also qualified as a counted method, the overlap rule would have to resolve it before the count.

Four claim regions remain four material entries. The example independently has three lineages, so its two-lineage and three-material-entry pluralism duties pass under the stated facts in both policies. With no counted-family basis, family coverage is unassessable even though that pluralism result remains available. A justified k=2 override for P-method changes its threshold result while leaving its count at 2 and those independent duties unchanged.

G.1 M2 and the G.3–G.5 consumers cite the chosen pack judgement with its purpose and policy; they do not reconstruct a more convenient count from the cards.

### G.2:6 - Bias-Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: harvesting and synthesis for a `CG‑Frame`.

* **Selection bias (Gov/Onto).** Any harvesting protocol can over‑represent certain venues, languages, or evidence styles.
  *Mitigation:* pluralism floor + explicit `CorpusLedger` + explicit protocol pins.

* **Consolidation bias (Onto/Epist).** Pressure to “merge” lineages can erase incompatible commitments.
  *Mitigation:* keep Claim Sheets disjoint by default; require explicit alignment proof for fusion; preserve loss notes.

* **Recency bias (Prag).** Overweighting newest papers can hide durable backbone results; underweighting them misses SoTA drift.
  *Mitigation:* publish freshness windows and make them RSCR‑relevant.

* **Didactic bias (Did).** Micro‑examples can steer interpretation toward familiar domains.
  *Mitigation:* require heterogeneous substrates and explicit A.10 anchors.

### G.2:7 - Conformance Checklist (normative) — **CC‑G2**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                                                                                        | Purpose / Notes                                                                     |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **CC‑G2‑CoreRef**         | A conforming `G.2` artefact **MUST** satisfy the **effective** core obligations declared by the `GCoreLinkageManifest` in `G.2:4.1` (per `G.Core` Expansion rule).                                                                                                                                                                                 | Keeps core invariants governed by `G.Core`. |
| **CC-G2-Pluralism-1** | A conforming pack MUST include at least two `Tradition` lineages and at least three materially distinct entries, each identified by its source edition and claim region, with its EntityOfConcern, evidence norm, and comparison limits visible. | Prevents a single lineage or one renamed source cut from masquerading as synthesis. |
| **CC‑G2‑Ledger‑1**        | A conforming pack **MUST** include `G.2a CorpusLedger` with inclusion/triage status and explicit rationale hooks per entry.                                                                                                                                                                                                                        | Makes discovery/triage auditable.                                                   |
| **CC‑G2‑FlowRecord‑1**    | A conforming pack **MUST** include `G.2h FlowRecord` that traces identification → screening → eligibility → included at a minimum granularity sufficient to reproduce the corpus boundary.                                                                                                                                                         | Prevents “mystery inclusion” and supports refresh.                                  |
| **CC-G2-ClaimSheets-1** | For each included `Tradition`, the pack MUST include a `ClaimSheetId` naming exact sources and editions, claim regions, effective schemes where meaning matters, EntitiesOfConcern, comparison bases, evidence anchors, freshness notes, and intended use; it MUST NOT fuse cross-`Tradition` claims by default. | Keeps plurality and provenance explicit without a Context container. |
| **CC‑G2‑Palette‑1**       | A conforming pack **MUST** export `SoTA_Set@CG‑Frame` and `SoTAPaletteDescription` as citable views (via `SoTA_SetId`, `SoTAPaletteDescriptionId`) and ensure both are reconstructible from pack components by id (no hidden extra structure).                                                                                                      | Prevents downstream scraping of prose; keeps “M2 output” explicit.                  |
| **CC‑G2‑Palette‑2**       | If the pack exports one derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep `SoTAPaletteDescription` explicit as the default base palette, keep that derivation recoverable, and cite the declared `Q` or reachability/coverage rule that disciplined that view. Derived tradition views **MUST NOT** silently replace the palette's default meaning. | Keeps non-default tradition views recoverable without redefining palette-first semantics. |
| **CC‑G2‑AtlasInterpretation‑1** | If the pack exports `TraditionAtlasView`, it MUST satisfy §4.7 and the cited A.19 interpretive-view declaration by value, including the reason a thinner view is insufficient. | Keeps atlas use conditional and its interpretation recoverable. |
| **CC‑G2‑entityOfConcernMap‑1** | A conforming pack **MUST** include `G.2g entityOfConcern Map`, mapping (at minimum) each load‑bearing claim family and each minted/evolved public id to `entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩`, and citing the relevant `ClaimSheetId` and evidence anchors (A.10 and/or G.6 paths when used).                                         | Keeps plane/holon boundaries explicit and citable.                                  |
| **CC‑G2‑Alignment‑1** | Cross‑`Tradition` consolidation **SHALL** present either disjoint parallel claims with explicit divergence or an explicitly justified alignment proof. Reuse **MUST** cite the exact basis for every sense, kind or plane relation actually used and disclose its preservation and losses. Bundle/gate anchors **MUST** be supplied when an E.18 flow crossing or A.21 gate independently requires them, per `CC‑GCORE‑CROSS‑1`. | A kind correspondence alone requires neither an F.9 sense Bridge nor a flow-crossing bundle. |
| **CC‑G2‑GammaSynth‑1**    | If the pack asserts **fusion or substitution** across sources or across `Tradition` records (not merely “parallel divergent claims”), it **MUST** emit `GammaEpistSynthId` records satisfying `G.2:Ext.GammaEpistSynthesis` (provenance union + explicit alignment refs + assurance tuple refs). If no fusion or substitution is asserted, the pack **SHALL** state so explicitly. | Keeps the synthesis record (alias: `G.2‑F`) citable under its governing definitions. |
| **CC‑G2‑Inventory‑1**     | A conforming pack **MUST** include `G.2c OperatorAndObjectInventory`, sufficient for downstream CHR/CAL authoring to begin without re‑harvesting terms.                                                                                                                                                                                            | Ensures the pack is actionable.                                                     |
| **CC‑G2‑Inventory‑2**     | `G.2c OperatorAndObjectInventory` entries **MUST** be treated as **stubs** for downstream authoring: they **MUST NOT** embed acceptance thresholds or claim legality decisions locally. If an entry is not a citation of an already governed CHR/CAL artefact, it **MUST** be explicitly marked as `stub` (typing/lawfulness `TBD`) and **MUST NOT** be used as if lawful. Legality/threshold semantics are governed by `G.3` for CHR and `G.4` for CAL via explicit ids/pins. | Prevents “shadow CHR/CAL” and preserves lawfulness discipline without redefining it locally. |
| **CC‑G2‑MeasurementLawful‑1** | If any inventory entry is presented as **non‑stub** (i.e., already lawful/typed), the pack **MUST** cite the governing lawfulness discipline (e.g., `A.17–A.19/C.16` as applicable) and provide the minimal evidence anchors needed to justify that typing claim.                                                                                      | Prevents “quietly lawful” measurement claims inside the harvester pack.             |
| **CC-G2-MicroExamples-1** | For every load-bearing claim family, a conforming pack MUST include at least two worked micro-examples on heterogeneous substrates. Each names the source and edition, claim region, EntityOfConcern, comparison basis, and intended use; cites its evidence carrier or A.10 evidence-provenance path; and gives an applicable assurance tag. | Makes the synthesis teachable and inspectable; the example form supplies no meaning or authority. |
| **CC‑G2‑UTS‑1**           | If the pack proposes or evolves any public ids, it **MUST** publish UTS proposals *(Name Cards + MDS where applicable)* and cite them via `UTSRowId[]`, satisfying `CC‑GCORE‑UTS‑1` (delegation).                                                                                                                                               | Keeps naming and evolution disciplined.                                             |
| **CC‑G2‑Families‑1**      | SoS indicators and candidate evaluation constructs **SHALL** be represented as **families/variants** (windows/constraints/assumptions) **with explicit Acceptance branch structure per variant** (branch ids/labels only), not as single unqualified scalars; any scalar summary **MAY** be included only as report‑only unless explicitly promoted by governing patterns. *(Set-return discipline is delegated to `CC‑GCORE‑SET‑1`.)* | Prevents covert scalarization and keeps acceptance governed by downstream patterns.                |
| **CC‑G2‑HandOff‑1**       | A conforming pack **MUST** emit hand‑off manifests to `G.3`, `G.4`, and `G.5` that cite pack components by id and identify which families/operators are intended for downstream formalisation or registry entry.                                                                                                                                   | Prevents downstream re‑authoring and drift.                                         |
| **CC‑G2‑CoverageGate‑1**  | The pack **MUST** declare `FamilyCoverageFloorK` and enforce it as a harvesting gate. It **MUST** either (i) specify `k` explicitly in an explicit `HarvestPolicyRef`, or (ii) use the pattern‑local default rule governed by `CC‑G2‑CoverageGate‑1`. *Default threshold (pattern-local):* `k=3`. In both threshold branches, an explicit `HarvestPolicyRef` **MUST** fix the receiving question, population/scope, grouping, same-family equivalence and overlap rule before counting. The pack judgement cites that basis, its distinct units and result; all consumers reuse it. Missing basis returns unassessable. Duplicate references add zero, and a threshold override changes neither units nor independent pluralism duties. The independent CC-G2-Pluralism-1 duties remain. If the defined gate fails, the pack **MUST** (a) record the repair iteration in `FlowRecord`, and (b) broaden the search radius (new venues/corpora/contexts/traditions) rather than silently weakening the gate; if an exploration policy is used for this broadening, it **MUST** be pinned as a policy id/ref. | Makes “coverage floor” explicit and prevents “silent narrowing” under failure.      |
| **CC‑G2‑DistanceGate‑1**  | If a diversity‑by‑distance gate is used, the pack **MUST** pin `DistanceDefRef.edition` and the declared threshold (δ), and treat edits as RSCR‑relevant per `CC‑GCORE‑TRIG‑*` (delegation). If no such gate is used, the pack **SHALL** explicitly state that it is not used.                                                                     | Avoids implicit distance defaults and improves refreshability.                      |
| **CC‑G2‑RSCR‑1**          | A conforming pack **MUST** emit canonical `RSCRTriggerKindId` causes (not free text) for edits to evidence surfaces, name/tokenization surfaces (e.g., UTS proposals/aliases), crossings, planes, edition pins, and harvesting policy pins (`HarvestPolicyRef`), per `CC‑GCORE‑TRIG‑1…TRIG‑4` (delegation).                                                                                      | Keeps refresh reason codes stable and typed.                                        |
| **CC‑G2‑Ext‑GammaEpist‑1** | If `G.2:Ext.GammaEpistSynthesis` is used (i.e., any fusion/substitution is asserted), the pack **SHALL** expose the required pins listed in that extension and **SHALL NOT** redefine `Γ‑fold/Φ/penalty` semantics locally (cite governing definitions by delegation).                                                                                       | Keeps synthesis auditable without creating shadow specs.                            |
| **CC‑G2‑Ext‑HarvestProtocols‑1** | If `G.2:Ext.HarvestProtocols` is used, the pack **SHALL** expose the required pins/criteria ids listed in that extension and **SHALL NOT** redefine evidence/quality semantics outside the declared protocol profile.                                                                                                                            | Keeps protocol variation explicit and separately citable.                           |
| **CC-G2-Ext-DHC-1** | If `G.2:Ext.DHCAlignmentHooks` is used, expose the DHC method edition, exact compared F.17 cell population, counted obtaining directed F.9 relation refs with their orientation and admitted-use qualifiers, evidence paths, and C.21 Unit `obtaining_relations/100_compared_cells`. CL labels alone neither change that population nor impose a counting threshold. Cite any separate receiving-use policy under its own authority. | Keeps the quantity identical to the C.21/G.7 definition. |
| **CC‑G2‑Ext‑NQD‑1**       | If `G.2:Ext.NQDAnnex` is used, the pack **SHALL** expose the required pins/editions/policies listed in that extension and **SHALL NOT** redefine QD semantics locally.                                                                                                                                                                             | Keeps QD/OEE extension pins replayable and non‑shadowing.                          |
| **CC‑G2‑Ext‑Interop‑1**   | If `G.2:Ext.InteropForms` is used, the pack **SHALL** expose the required interop pins and **SHALL NOT** introduce alternative legality/acceptance semantics.                                                                                                                                                                                      | Prevents “foreign gate” shadowing.                                                  |

### G.2:8 - Common Anti‑Patterns and How to Avoid Them

* **AP‑G2‑1: “One true SoTA score.”**
  **Avoid:** selecting a single unqualified scalar metric as “the” SoTA.
  **Do instead:** represent evaluation constructs as families/variants; keep partial orders set‑returning (delegated).

* **AP‑G2‑2: Fusion without explicit alignment proof.**
  **Avoid:** merging rival `Tradition` claims into one statement “by common sense.”
  **Do instead:** preserve parallel Claim Sheets; if consolidation is required, publish explicit alignment proof or keep a divergence record.

* **AP‑G2‑3: Hidden protocol drift.**
  **Avoid:** changing the harvesting protocol (inclusion criteria, windowing, screening rubric) without pins.
  **Do instead:** pin harvesting policy/profile ids and treat changes as RSCR‑relevant.

* **AP‑G2‑4: Unanchored pedagogy.**
  **Avoid:** micro‑examples without carriers (they become folklore).
  **Do instead:** bind micro‑examples to A.10 anchors and declare `entityOfConcern`.

* **AP‑G2‑5: Atlas by default.**
  **Avoid:** writing as if every tradition comparison or NQD/OEE note needs `TraditionAtlasView`, or as if atlas wording renames the palette itself.
  **Do instead:** keep the base palette and derived front, archive, or shortlist explicit; use atlas form only when several declared views or interpretive qualifiers must be held together, and prefer thinner `DeclaredSubstrateInterpretiveView` when that is enough.

### G.2:9 - Consequences

* **Positive:** Downstream CHR/CAL/dispatch work becomes faster and less ambiguous because the pack is citable and structured.
* **Positive:** Plurality is preserved while still enabling disciplined comparability through explicit crossings.
* **Positive:** Refresh becomes tractable because pins and typed causes exist.
* **Negative:** Adds authoring overhead (ledger, flow record, micro‑examples, explicit pins).
* **Negative:** Requires governance discipline to prevent the pack from becoming an uncontrolled “everything bucket”.

### G.2:10 - Rationale

SoTA synthesis is a bottleneck for new `CG‑Frame` work: without a disciplined harvest, downstream formalization (CHR/CAL) and operational selection (G.5) either (i) inherit hidden semantic collisions, or (ii) re‑invent incompatible “mini‑standards.”
`G.2` resolves this by treating SoTA work as a **publishable kit**: explicit plurality, explicit crossings, explicit evidence anchors, and explicit hand‑offs.

### G.2:11 - SoTA-Echoing — keep a reusable synthesis current without restarting it

**Practice question.** How should several downstream authors reuse a synthesis when new sources can change a consequential, unsettled comparison? The selected line keeps a question-bound source ledger, separable claims and explicit update causes; a living protocol is chosen when continuing evidence surveillance is worth its cost. A serious alternative is a well-reported static review with an explicit search date and a separately commissioned update. That alternative is sufficient for a stable question or a one-time decision and avoids maintaining a continuing review service.

The [Cochrane Handbook, Chapter 22, §§22.2.3–4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-22) supplies the conditional living-review line and its resource trade-off: priority, uncertainty and likely new evidence can justify frequent updates, while additional searching needs resources. **Adapt** this conditional choice in `HarvestProtocols`; declare the search/update policy rather than treating every G.2 pack as perpetually living. The clinical-review guidance does not establish coverage or evidence adequacy for an arbitrary engineering CG-frame.

The [PRISMA 2020 reporting guidance](https://www.prisma-statement.org/prisma-2020) supplies the substantive static-review comparator and a shared reporting basis. Its [explanation of study selection](https://www.bmj.com/content/372/bmj.n160) distinguishes records, reports and included studies. **Adapt** the distinction to `CorpusLedger`, `FlowRecord` and the declared family units in §4.3: multiple source entries can concern one counted family. **Reject** treating a publication count or a completed flow diagram as proof of adequate family coverage. G.2's k threshold, lineage duties and FPF alignment rules remain local decisions, not PRISMA requirements.

The [2024 PRISMA-LSR extension](https://www.bmj.com/content/387/bmj-2024-079183) supplies the more specific reporting line for an actually selected living protocol: justify that mode, identify the version's trigger and changes, and plan when to retire it. **Adapt** that distinction to the policy pins, change causes and downstream handoffs in §4.3 and `G.2-2 Extend`; G.11 governs refresh orchestration. Source reporting guidance does not supply an automatic update schedule or establish that a newly added claim is sound.

The control-stack case in §5.1 makes the improvement concrete. If e1's operating-envelope claim is revised, the existing ledger identifies M-R and its consumers; re-examine that claim and the comparisons that depend on it. The new report does not add a family. The method-only count remains 2 until a distinct admitted method-family unit is found. A static review can also be updated correctly, but each separate consumer must recover the changed basis unless a shared update is published. For the same new source and receiving question, the selected pack reuses existing screening and claim relations; its added maintenance burden is justified only while repeated shared use and consequential change make that work useful.

Reopen the choice of protocol when the evidence rate, decision importance, uncertainty or maintenance resources change; retire living surveillance when its reason no longer holds. Reopen an individual synthesis when a new source changes a relied-on claim, coverage judgement or alignment. A source with a new date but no relevant content change does not by itself warrant reconstructing every downstream conclusion.

### G.2:12 - Relations

* **Builds on:**

  * `G.Core` (core invariants, typed RSCR causes, Default Governing Definition Index)
  * `E.8` (pattern template discipline)
  * `E.10` (lexical/ontological rules; strict distinction; kind‑suffix discipline)
  * `E.19` (conformance discipline)
  * `A.10` (evidence-provenance paths and cited source/carrier anchors)
  * `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` (generic interpretive-view and atlas discipline when `TraditionAtlasView` is used)
  * `A.6.P` (space/view/publication precision restoration when palette/support claims collapse)
  * `B.3` (trust, freshness/decay as cited governing patterns)
  * `F.9` (bridges and CL as cited governing patterns)
  * `F.17` (UTS publication discipline; via delegation)
  * `G.0` (CG‑Spec legality gate; cited when legality surfaces are referenced)
  * `G.6` (EvidenceGraph / path citation surfaces when used)

* **Used by:**

  * `G.1` (generator chassis consumes harvested SoTA sets)
  * `G.3` (CHR authoring consumes operator/object inventory and claim sheets)
  * `G.4` (CAL authoring consumes operator stubs, acceptance branch scaffolding)
  * `G.5` (registry/dispatch consumes MethodFamily/GeneratorFamily cards)
  * `G.10` (shipping cites the pack as payload)
  * `G.11` (refresh orchestration can re‑invoke harvest via typed causes)

* **Relates to:**

  * `G.13` (interop surfaces when external indices are used)
  * `F.18` (naming-side support wording when the question is label choice rather than synthesis geometry)

### G.2:End

---

## G.3 - CHR Authoring for a CG‑Frame: Characteristics, Scales, Levels, Coordinates

> **Status:** Stable

**Tag.** Architectural pattern (CHR kit; publishes lawful measurement primitives; constrains CAL authoring and selector/dispatch use)
**Stage.** *design‑time* (authoring & publication; enables admissible run-time consumption by `G.4` / `G.5`)
**Primary output.** `CHR Pack@CG‑Frame` — a notation‑independent, UTS‑published CHR bundle that provides: typed Characteristics/Scales/Levels/Coordinates, legality + guard surfaces, aggregation/comparison specs, RSCR hooks/tests, and provenance pins.
**Primary hooks.** `G.1` (declared CG-frame, which is the framing episteme), `G.2` (SoTA synthesis inputs), `A.19.CHR` (CHRMechanismSuite boundary + pins), `A.15.2` (WorkPlan baseline), `A.15.3` (planned filling of an independently declared position), `A.18/C.16` (MM-CHR legality), `F.0.1`, `F.1`, `F.9`, `F.17`, and `F.18` (source-local meaning, selected source editions, actual relations between local-sense cells, and naming settlement), `C.2.1` (bounded-use claims), `B.3` / `B.3.4` (trust, freshness/decay), `A.10` (evidence-provenance paths and cited carriers), `G.6` (EvidenceGraph/Path citation), optional `C.18 and C.19` (QD/OEE wiring), `G.11` (refresh orchestration).
**Non‑duplication note.** Universal Part‑G invariants (bridge‑only crossings, tri‑state semantics, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, linkage discipline) are governed by `G.Core`. This pattern cites them via `G.3:4.1` and delegates where needed.

### G.3:1 - Problem frame

A team is defining or evolving a `CG‑Frame` (via `G.1`) and has plural, competing SoTA traditions and constructs (via `G.2`). The team needs an *admissibility-ready CHR publication* that makes downstream work possible without hidden semantic drift:

* **CAL authoring (`G.4`)** needs typed, admissible operands and guard/legality surfaces to build admissibility and acceptance rules (thresholds and policy cut‑offs remain governed by CAL).
* **Selector/dispatch (`G.5`)** needs CHR‑typed quantities and explicit provenance pins so selection can remain set-returning and auditable under admissible orders.
* **Reuse beyond the defining source or use** must name the exact characteristic and scale editions, bearer, scope and validity window, reference plane, evidence, and intended downstream use. Cite an `F.9` relation only when it actually obtains between the named `F.17` cells; any claim that relies on the relation for this use remains a separate bounded-use claim under `C.2.1` and `F.9`; its evidence-bearing reliance follows `A.10` and any applicable `B.3` assurance requirement.

The resulting publication is a **CHR Pack** that is **CG‑Frame‑scoped**, **notation‑independent**, and **UTS‑published**, with explicit edition/policy pins sufficient for reproducibility and RSCR.

### G.3:2 - Problem

Without a disciplined CHR authoring layer, teams repeatedly produce “measurable slots” that are *numerically manipulable but semantically unlawful*:

* **Meaning leaks** when the same token is reused after its referent or sense, bearer, scope, validity window, evidence basis, or intended use has changed.
* **Illicit arithmetic** (e.g., averaging ordinals, mixing units, laundering polarity).
* **Hidden normalizations** that silently change scale type, polarity, or admissible transforms.
* **Unreproducible comparisons** (missing edition pins for methods/distances/policies; unclear reference plane).
* **Unscoped reuse** (the characteristic or scale lacks an exact edition, bearer, scope and validity window, reference plane, evidence basis, or intended downstream use; any relation needed for reuse is left unstated).
* **Un-auditable aggregation** (no explicit legality surface and guard surface; no proof hooks; unclear governing definition for the Γ‑fold).
* **Refresh chaos** (changes in names/editions/policies do not map to typed RSCR causes).

### G.3:3 - Forces

| Force                                             | Tension                                                                        |
| ------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Pluralism vs comparability**                    | Preserve tradition‑specific meaning ↔ enable admissible cross‑tradition use.       |
| **Expressiveness vs legality**                    | Model rich measurement semantics ↔ block illegal operations “by construction”. |
| **Portability vs honesty**                        | Encourage reuse ↔ forbid implicit crossings and hidden loss.                   |
| **Ease of authoring vs auditability**             | Keep authoring teachable ↔ require explicit pins, provenance, and tests.       |
| **Downstream flexibility vs upstream discipline** | Let CAL/selector choose policies ↔ keep thresholds/policy cut‑offs out of CHR. |

### G.3:4 - Solution — CHR authoring kit and publication surface

#### G.3:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**

```text
GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
},
CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

// Pins strengthened for CHR authoring (delta over PinSets)
CorePinsRequired := {
// NOTE: the frame pin inherited from `GCorePinSetId.PartG.AuthoringMinimal` denotes only the exact
// declared CG-frame, which is the framing episteme here; it supplies no universal setting, scope, or reuse authority.
// `entityOfConcern`, `CNSpecRef.edition`, and `CGSpecRef.edition` remain inherited; each card adds the exact use pins named below.
UTSRowId[],                      // required: CHR terms are public ids (Name Cards plus public-id continuity records)
PathId[]/PathSliceId[],          // required: worked examples/tests and refresh anchoring cite paths
ReferencePlane,                  // required: definitional claims are plane-scoped
Φ/Ψ/Φ_plane policy-ids?,         // when the applied loss/assurance model uses them or an applicable rule for the receiving use requires them (G.Core:4.2.3)
ΓFoldRef.edition?                // iff an explicit Γ-fold artefact is pinned (otherwise use DefaultId)
// NOTE: method-/discipline-specific pins (e.g., DescriptorMapRef/DistanceDefRef/DHCMethodRef/InsertionPolicyRef)
// are declared only inside Extensions (e.g., `G.3:Ext.QD_OEE_Wiring`) to keep core linkage universal.
},

// consumed iff any published `CHR.AggregationSpec` relies on default Γ-fold (no explicit override pinned)
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerKindIds := {
RSCRTriggerKindId.EvidenceSurfaceEdit,
RSCRTriggerKindId.TokenizationOrNameChange,
RSCRTriggerKindId.CrossingBundleEdit,
RSCRTriggerKindId.ReferencePlaneEdit,
RSCRTriggerKindId.EditionPinChange,
RSCRTriggerKindId.PolicyPinChange,
RSCRTriggerKindId.DefaultGoverningDefinitionChange,
RSCRTriggerKindId.FreshnessOrDecayEvent,
RSCRTriggerKindId.LegalitySurfaceEdit,
RSCRTriggerKindId.BaselineBindingEdit
}
⟩
```

*(Nil‑elision + expansion rule are per `G.Core:4.2`. This pattern does not redefine the semantics of core conformance ids, trigger kinds, or defaults; it only declares applicability and required pins.)*

#### G.3:4.2 - Output surface: `CHR Pack@CG‑Frame` (normative)

`CHR Pack@CG‑Frame` is the CHR kit payload that downstream patterns cite and pin (it is not a “shadow spec” for CN/CG).

**Minimum exported objects (kit surface):**

* `CHR.Characteristic[]`
* `CHR.Scale[]`
* `CHR.Level[]` *(when the scale type requires explicit level sets / order structure)*
* `CHR.Coordinate[]` *(encodings + legality annotations; never an implicit “upgrade” of measurement structure)*
* `CHR.Guards` *(guard macro surface; semantics governed by cited definitions; see `G.Core` and `A.18`)*
* `CHR.LegalityMatrix` *(admissible operations per scale type / unit / polarity regimes)*
* `CHR.AggregationSpecs` *(typed aggregators/comparators + proof hooks + edition pins where applicable)*
* `UTS` publication bundle: Name Cards (twin labels), public-id continuity notes, and (when applicable) bridge and loss notes
* RSCR artefacts: `RSCRTestId[]` + worked examples + provenance pins (ReferencePlane, Path/PathSlice, policy ids)

**Mandatory provenance pins (conceptual, notation‑independent):**

* `ReferencePlane`
* `PathId/PathSliceId` citations for worked examples/tests
* R‑anchors (conceptual; KD‑CAL lanes when used) realised via `PathId/PathSliceId` and, where applicable, `A.10` anchor/carrier refs
* policy pins used by crossings or plane moves (when exercised)
* edition pins for any referenced method or metric definitions that affect interpretation

#### G.3:4.3 - CHR authoring chassis (S1–S8)

**S1 — Charter the measurement scope (scope anchor).**
Identify the exact declared CG-frame (the framing episteme). For this CHR work, state the bearer or bearers and identify each as an `entityOfConcern`. Also state the scope, any applicable qualification and evaluation windows, `ReferencePlane`, evidence basis, intended downstream use, freshness or decay expectations, and any contested expression whose reuse may require an actual `F.9` relation. Output a design-time `MeasurementCharter` and `KindMap`.
If freshness/decay expectations are anything beyond an explicit “non‑decaying” declaration, wire them via
`G.3:Ext.DecayWiring` (governing pattern: `B.3.4`) rather than encoding decay semantics in CHR prose.
If assurance‑subtype lane tags are used (e.g., TA/VA/LA), declare the lane regime here so downstream evidence discipline can remain lane‑pure (taxonomy/semantics governed by `B.3`; evidence‑path representation & audit governed by `G.6`; this pattern only records wiring).
**Lane docking (wiring‑only; normative).**
If `EvidenceLanes` are used, the charter MUST:
* enumerate the lane tags used (e.g., TA/VA/LA) and cite their governing pattern taxonomy (governed by `B.3`), plus the upstream provenance for their use when available (e.g., `SoTAPaletteDescriptionId` via `G.3:Ext.SoTAPackInputs`);
* expose any lane‑dependent tolerances / proof requirements via explicit pins (policy‑id and/or edition‑pinned refs), not prose;
* treat lane tags as provenance metadata (not Contexts): they MUST NOT be “bridged away” or silently mixed;
* if any cross‑lane comparison/aggregation is claimed, it MUST be explicit and pinned to the governing acceptance/evidence policy (typically `G.4`) and auditable via evidence paths (`G.6`); otherwise downstream consumers treat it as illegal.
*Crossing semantics and penalty routing are cited via `G.Core` (do not restate).*

**S2 — Mint or reuse terms (UTS‑first).**
For each candidate characteristic, scale, level, or coordinate term: attempt reuse; otherwise mint via UTS Name Cards with twin labels and public-id continuity notes. When a term is imported across contexts, the import must be explicit and auditable (bridge and loss notes live with the crossing artefacts; CHR only cites them).

**S3 — Define `CharacteristicCard` (the per-characteristic publication unit).**
A CharacteristicCard is the minimum unit CHR publishes for downstream legality. It SHOULD include (field names are indicative; semantics governed by cited definitions):

```text
CharacteristicCard := ⟨
  UTSRowId,
  CharacteristicRef.edition,
  entityOfConcern,
  ClaimScope,
  ApplicableSliceRef[],
  QualificationWindow?,
  EvaluationWindow?,
  MeasurementMethodRef.edition?,
  MeasurementModelRef.edition?,
  EvidenceRef[],
  IntendedDownstreamUse,
  ReferencePlane,
  ObjectKind,
  Intent,
  Definition (typed),
  ObservableOf := ⟨instrument/protocol (provenance cited through A.10 paths), uncertainty model, validity window⟩,
  EvidenceLanes? (KD‑CAL lanes; wiring only; semantics governed by `G.4` / `G.6`),
  ScaleRef.edition,
  Polarity ∈ {↑, ↓, ⊥},
  Domain/Range,
  UnitSet,
  Bounds / zero semantics (as applicable),
  Freshness / half‑life (or explicit `NonDecayingDecl`; freshness/decay semantics governed by `B.3.4`),
  Missingness semantics (typed; include a classification/mapping when non‑trivial; downstream tri‑state handling is per G.Core),
  Stability/Reliability notes,
  RoleDecls? := RoleDecl[] (wiring‑only; each role declaration names its governing pattern + required pins; see `G.3:4.5`),
  QD.Role? ∈ {Q, D, QD-score} (interop alias for `RoleDecl` with `GoverningPatternId = C.18`; see `G.3:Ext.QD_OEE_Wiring`),
  Micro‑examples (R‑anchors: Path/PathSlice cited; lane tags where applicable)
⟩
```

`Polarity` gives the preferred direction for `IntendedDownstreamUse`: ↑ means higher-is-better, ↓ lower-is-better, and ⊥ no preferred direction assigned. Use ⊥ for a descriptive measurement. A target, range or other preference that has no single direction uses the applicable evaluation predicate and its Method; the Scale retains its measurement meaning under A.17/A.18.

Where `RoleDecl := ⟨ roleLabel, GoverningPatternId, EditionPins?, PolicyPins? ⟩` (wiring-only; the value of `GoverningPatternId` names the FPF pattern that governs the role declaration semantics).

Rules (CHR‑governed intent, semantics governed by cited definitions where indicated):

* Scale/unit/polarity legality obligations cite MM‑CHR governing definitions (`A.18` and `C.16`) and must be *checkable* by downstream patterns.
* Missingness must be typed so downstream can apply tri‑state outcomes without silent coercion (tri‑state semantics are governed by `G.Core`).
* If `EvidenceLanes` are recorded, they are only lane tags for downstream evidence discipline (taxonomy governed by `B.3`; audit surface: `G.6`; any cross‑lane policy is governed by `G.4`); this pattern does not introduce lane semantics or invent bridge‑like constructs.
* If `RoleDecls` are used, each declaration MUST cite the FPF pattern that governs the declaration, for example `C.18` or `C.19`, and surface the edition and policy pins required by that governing pattern; CHR does not define role semantics locally.
* **Role docking (normative, wiring-only):** if any `RoleDecl` is present with `GoverningPatternId = X`,
  then `G.3` MUST include (or explicitly cite) a corresponding `GPatternExtension` block whose governing definition is `X`
  (or whose `Uses` includes `X`) and that surfaces the required pins for that role family. Otherwise the role
  declaration is non-conformant (it is an undocked semantic fragment).
* **Freshness docking (normative, wiring-only):** if a characteristic’s freshness/half-life is defined via a named
  decay model/policy (rather than a pure local statement), the relevant policy/ref MUST be pinned and cited through `B.3.4`
  via `G.3:Ext.DecayWiring`.
* If a characteristic is intended to be *promoted into* `CG‑Spec`, the linkage is explicit and edition‑pinned (wiring lives in an Extension; semantics governed by `G.0`).

**S4 — Define `ScaleCard` and `LevelCard` (lawful measurement).**
Publish the scale type and admissible transforms, plus levels/orders when applicable. CHR does not invent new legality semantics; it cites MM‑CHR governing definitions and makes the legality surface concrete for the frame’s characteristics.

Typical distinctions that must be representable:

* **Nominal / categorical:** equality + counting; transforms are permutations.
* **Ordinal:** order‑preserving transforms; no arithmetic that presupposes intervals.
* **Interval:** affine transforms; differences meaningful; means may be lawful if justified.
* **Ratio:** positive scalar transforms; ratios meaningful; products/sums subject to unit discipline.
* **Count / rates:** explicit exposure/timebase requirements; rate conversions must be explicit.
* **Cyclic:** wrap‑around discipline + principal interval declaration.

**S5 — Define `CoordinatePolicy` (encodings without hidden cardinalization).**
When a numeric coordinate/embedding is used for convenience or tooling, CHR MUST publish:

* what invariants are preserved (order only / ratios / topology / wrap‑around),
* what remains illegal,
* what proof hooks are required if a structure with higher scale-type commitment is claimed.

A coordinate never silently upgrades a scale type; if an upgrade is claimed, the proof requirement is explicit and carried by MM-CHR governing definitions.

**S6 — Publish legality + guard surfaces (Guard Macros + LegalityMatrix).**
CHR publishes a `CHR.LegalityMatrix` and a `CHR.Guards` surface that downstream operators can reference.

Guard macro names are allowed as authoring ergonomics, but their semantics MUST cite governing definitions (no “shadow semantics” in this pattern). Examples of macro intents (governing definitions in parentheses):

* `CSLC_PROOF_REQUIRED(x)` (MM‑CHR legality governing definitions: `A.18/C.16`)
* `UNKNOWN_TRI_STATE(x)` (tri‑state semantics governed by `G.Core`)
* `UNIT_CHECK(x)` (MM‑CHR legality governing definitions)
* `RETURN_SET_FOR_PARTIAL_ORDERS()` (set‑return semantics governed by `G.Core`)
* `METRIC_EDITION_REF(...)` (edition‑pin discipline governed by `G.Core`; metric semantics governed by `C.18`/`C.21` as applicable)

**S7 — Publish `AggregationSpecs` (typed, admissible, reproducible).**
CHR may publish typed aggregation/comparison specs that are *safe by construction* and usable as building blocks by `G.4` and `G.5`. For any published spec:

* The legality regime is explicit (scale/unit/polarity constraints + required proof hooks).
* If a contributor folding policy (Γ‑fold) is used and not explicitly overridden, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`; do not restate the default here.
* If method‑role declarations imply metric‑driven comparisons (e.g., QD roles), the relevant edition/policy pins are surfaced (wiring lives in an Extension; semantics governed by the referenced patterns).

**S8 — Publish, test, and evolve (UTS + RSCR readiness).**
Publish the CHR pack and associated Name Cards to UTS. Attach:

* RSCR tests that check legality and guard coverage and reject illegal ops,
* worked examples with Path/PathSlice provenance,
* refresh/decay notes and deprecations with lexical continuity.

This step prepares the RSCR loop but does not govern orchestration (governing definition: `G.11`).

#### G.3:4.4 - Interfaces (normative)

| Interface                           | Consumes                                          | Produces                                                         |
| ----------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------- |
| **G.3-1 Charter_CHR** | exact declared CG-frame (the framing episteme), bearer or bearers identified as EntitiesOfConcern, scope and applicable windows, `ReferencePlane`, evidence basis, intended downstream use, and SoTA inputs (`G.2`) | `MeasurementCharter`, `KindMap` |
| **G.3-2 MintOrReuse_Terms** | candidate characteristic, scale, level, or coordinate expressions; their effective scheme, source-local sense, and intended CHR use; UTS registry | reused or minted ids and Name Cards where public ids are needed; exact `F.17` cell refs and `F.9` relation refs only when an actual relation between local meanings is required for the stated reuse and obtains |
| **G.3‑3 Define_Characteristic**     | `MeasurementCharter`, candidate semantics         | `CHR.Characteristic[]` (CharacteristicCards)                     |
| **G.3‑4 Define_ScaleLevel**         | CharacteristicCard + MM‑CHR rules                 | `CHR.Scale[]`, `CHR.Level[]`                                     |
| **G.3‑5 Define_CoordinatePolicy**   | Scale/Level + use‑case constraints                | `CHR.Coordinate[]` + legality annotations                        |
| **G.3‑6 Publish_GuardsAndLegality** | Scale/Level/Coordinate set                        | `CHR.Guards`, `CHR.LegalityMatrix`                               |
| **G.3‑7 Publish_AggregationSpecs**  | CHR set + legality hooks + (optional) metric refs | `CHR.AggregationSpecs` (+ proofs/refs + pins)                    |
| **G.3‑8 Publish_CHRPack**           | all CHR artefacts + tests/examples                | `CHR Pack@CG‑Frame` + UTS rows + RSCR tests                      |

#### G.3:4.5 - Extensions (pattern‑scoped; non‑core)

All blocks below are `GPatternExtension` modules (PatternScopeId-scoped; **not** new PatternIds). They store wiring only and cite governing patterns.

**GPatternExtension: SuiteBoundaryLinkage**

* **PatternScopeId:** `G.3:Ext.SuiteBoundaryLinkage`
* **GPatternExtensionId:** `SuiteBoundaryLinkage`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `A.19.CHR`
* **Uses:** `{A.19.CHR, A.15.2, A.15.3}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CHRMechanismSuiteDescriptionRef.edition?` *(when the suite description is cited as a reproducibility baseline)*
  * `WorkPlanRef` and local baseline locator *(when a planned baseline binds CHR artefacts into WorkPlanning under `A.15.2`)*
  * `CHRMechanismSuiteSlotFillingsPlanItem` in that WorkPlan *(when the plan fills an independently declared operation argument or relation position under `A.15.3`; cite the governing declaration and member designator, and locate the filling row within the plan)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring-only):** `A.19.CHR` governs suite semantics and membership; `A.19.CHR:4.1.2` distinguishes ordinary planned baselines from typed filling.

**GPatternExtension: SoTAPackInputs**

* **PatternScopeId:** `G.3:Ext.SoTAPackInputs`
* **GPatternExtensionId:** `SoTAPackInputs`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.2`
* **Uses:** `{G.2}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `ClaimSheetId[]` / operator & object inventory refs (as cited inputs)
  * `SoTAPaletteDescriptionId?` (when palette/traces are cited; used to dock contested‑term inventory and (if present) lane tags/tolerances)
  * `BridgeMatrixId?` (when terms/constructs are imported across traditions)
  * `UTSRowId[]` drafts/aliases from synthesis
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.TokenizationOrNameChange, RSCRTriggerKindId.CrossingBundleEdit}`
* **Notes (wiring‑only):** SoTA pluralism inputs are governed by `G.2`; this module only specifies which synthesis artefacts are cited while authoring CHR. When CHR authoring relies on pack coverage, cite the same `CoverageJudgementRef` and HarvestPolicy basis, retaining the counted population and receiving question. CHR terms or cards do not redefine the counted family unit; lineage plurality remains a separate result.

**GPatternExtension: CGSpecPromotionWiring**

* **PatternScopeId:** `G.3:Ext.CGSpecPromotionWiring`
* **GPatternExtensionId:** `CGSpecPromotionWiring`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.0`
* **Uses:** `{G.0}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `CGSpecRef.edition` *(when a characteristic is promoted/linked into `CG‑Spec`)*
  * `CHR.Characteristic.id` pointers included in `CG‑Spec.Characteristics := [...]` *(no shadow ids; CG‑Spec stores pointers, see `G.0`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
* **Notes (wiring‑only):** `G.0` governs promotion semantics and the legality gate; CHR only pins and cites.

**GPatternExtension: MMCHRLegalityWiring**

* **PatternScopeId:** `G.3:Ext.MMCHRLegalityWiring`
* **GPatternExtensionId:** `MMCHRLegalityWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `A.18`
* **Uses:** `{A.17, A.18, C.16}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * CSLC legality proof anchors/carriers (ids/refs as defined by MM‑CHR governing definitions; cite `A.18/C.16`)
  * Unit coherence references (where units exist)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.LegalitySurfaceEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (wiring‑only):** This module wires CHR artefacts to MM‑CHR legality proof obligations; legality semantics are governed by the referenced patterns.

**GPatternExtension: DecayWiring**

* **PatternScopeId:** `G.3:Ext.DecayWiring`
* **GPatternExtensionId:** `DecayWiring`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `B.3.4` *(freshness/decay semantics)*
* **Uses:** `{B.3.4, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `FreshnessWindowDeclRef` *(or equivalent window pin, as defined by the governing definition)*
  * `DecayPolicyIdRef?` *(policy-bound; if decay model is referenced by id)*
  * `PathSliceId[]` *(affected evidence carriers / examples that witness drift)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit}`
* **Notes (wiring‑only):** CHR does not define decay semantics; it only pins the window/policy defined by the governing pattern and ensures refresh can be triggered on decay events.

**GPatternExtension: QD_OEE_Wiring**

* **PatternScopeId:** `G.3:Ext.QD_OEE_Wiring`
* **GPatternExtensionId:** `QD_OEE_Wiring`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `DescriptorMapRef.edition` *(if any Characteristic declares descriptor roles)*
  * `DistanceDefRef.edition` *(if any Characteristic declares distance roles)*
  * `DHCMethodRef.edition?` *(when a C.21 discipline-health measurement definition is actually used; a Q / QD-score role alone does not select it)*
  * `InsertionPolicyRef?` *(when archive insertion semantics are declared for reproducibility)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** QD/OEE semantics are governed by `C.18 and C.19`. CHR only surfaces method‑role declarations
  (via `RoleDecls` or the interop alias `QD.Role`) and the edition/policy pins required for reproducible archive/front interpretation.

### G.3:5 - Archetypal Grounding

**AG‑1 — ML fairness auditing (post‑2015 selective and set‑valued practice).**
*System:* a CG‑Frame for evaluating deployed classifiers across cohorts with explicit abstention/defer behavior.
*CHR authoring:* publish `DemographicParityGap` and `EqualizedOddsGap` as Characteristics with:

* explicit ReferencePlane, with deployment population and sampling regime recorded separately as scope and protocol conditions,
* `ObservableOf` (audit protocol + uncertainty model + window),
* interval scale (bounded; zero semantics explicit),
* missingness semantics (cohort sparsity and label noise are typed),
* legality surfaces and guard surfaces that forbid illicit cohort mixing and require explicit proof hooks for aggregation across cohorts.

*Downstream:* CAL acceptance binds thresholds and failure behavior; selector remains set‑returning under partial orders and may treat “defer/abstain” as a first‑class outcome (tri‑state semantics pinned through `G.Core`).

**AG‑2 — Clinical diagnostics (post‑2015 evidence‑aware evaluation).**
*System:* a CG‑Frame for comparing diagnostic pipelines under evolving datasets and protocols.
*CHR authoring:* publish `Sensitivity` and `Specificity` as ratio‑scale, dimensionless Characteristics on `[0,1]`, with:

* explicit `ObservableOf` (trial protocol, inclusion criteria, uncertainty model),
* freshness/decay expectations (protocol drift is modelled as decay),
* legality surfaces that forbid averaging incompatible ordinal labels (e.g., severity grades) and require explicit unit/exposure constraints for any derived rate.

*Downstream:* CAL acceptance governs thresholds and guard‑bands; evidence wiring is cited via Path/PathSlice to make refresh triggers actionable.

**AG‑3 — Quality‑Diversity / Illumination (post‑2015 MAP‑Elites/CMA‑ME lineage).**
*System:* a CG‑Frame where selection returns archives/fronts rather than a single winner.
*CHR authoring:* declare which Characteristics play Q/D/QD‑score roles and pin the metric definitions (descriptor map, distance definition, method editions) so archives are reproducible across runs and refresh can be triggered on edition changes. CHR does not scalarize partial orders; set‑return semantics are pinned through `G.Core`.

### G.3:6 - Bias‑Annotation

CHR authoring is where many biases become “baked in” as measurement choices. Typical risks:

* **Proxy bias:** a convenient observable substitutes for the intended construct. Mitigation: require `ObservableOf` + ReferencePlane + micro‑examples; force explicit “what is being measured” rather than relying on labels.
* **Population and protocol shift:** a change in the sampling regime or protocol can change the interpretation or validity of a reported characteristic value, or change the characteristic’s meaning when that regime or protocol is part of its definition. Mitigation: explicit validity windows and freshness/decay expectations; edition pins for protocol definitions; RSCR triggers on freshness/decay events and evidence surface edits.
* **Ordinal misuse bias:** ordinal ratings treated as interval/ratio by convenience. Mitigation: publish scale type + admissible transforms; legality matrix + guard macros; reject coordinate upgrades without proof hooks.
* **Cross-tradition meaning bias:** an imported expression erases its source-local meaning or makes a changed bearer, scope, window, reference plane, evidence basis, or intended use disappear. Mitigation: name those values, cite exact `F.17` cells and an `F.9` relation only when it obtains, and keep any downstream bounded-use claim explicit under `C.2.1` and `F.9`, with evidence-bearing reliance governed by `A.10` and any applicable `B.3` assurance requirement. Loss remains visible through the applicable `G.Core` penalty rule rather than silently altering Part F or Part G semantics.
* **Metric gaming bias (QD and evaluation):** changing descriptors/distances changes what “diverse” means. Mitigation: edition‑pin metric definitions and make role declarations explicit (wiring via `C.18 and C.19`).

### G.3:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G3‑CoreRef** | `G.3` is conformant only if the applicable `G.Core` obligations declared in `G.3:4.1` are satisfied (effective expansion of profiles/sets + deltas; explicit pins; typed RSCR triggers; defaults with one governing definition).                       |
| CC‑G3‑01          | `CHR Pack@CG‑Frame` is published as a notation‑independent kit payload with the minimum exported objects listed in `G.3:4.2`.                                                                                                         |
| CC-G3-02 | Every `CHR.Characteristic` names its exact characteristic and scale editions, its bearer as the `entityOfConcern`, claim scope and applicable slices, any applicable qualification and evaluation windows, `ReferencePlane`, method or model edition when it affects interpretation, evidence refs, intended downstream use, and a filled `ObservableOf` field (instrument or protocol, uncertainty model, and validity window). |
| CC‑G3‑03          | Every `CHR.Characteristic` declares its `ScaleRef`, `Polarity`, and `UnitSet` (or an explicit “unitless” declaration), plus bounds/zero semantics where applicable.                                                                   |
| CC‑G3‑04          | Missingness is typed in the CHR artefacts such that downstream tri‑state handling is possible without silent coercion. *(Tri‑state semantics are governed by `G.Core`; the typing obligation is CHR‑local.)*                              |
| CC‑G3‑05          | `CHR.Scale` / `CHR.Level` artefacts encode the scale type and admissible transforms, and make illicit arithmetic checkable by downstream consumers.                                                                                   |
| CC‑G3‑06          | Any published `CHR.Coordinate` includes a `CoordinatePolicy` that states preserved invariants and explicit non‑entitlements; coordinates do not silently upgrade measurement structure.                                               |
| CC‑G3‑07          | `CHR.LegalityMatrix` and `CHR.Guards` exist and are referenced by downstream operator authoring; semantics are governed by cited definitions (MM‑CHR and `G.Core`), not duplicated locally.                                                        |
| CC‑G3‑08          | `CHR.AggregationSpecs` are typed and legality‑constrained; where Γ‑fold is required and no explicit override is pinned, cite `DefaultId.GammaFoldForR_eff` through `G.Core.DefaultGoverningDefinitionIndex`. |
| CC‑G3‑09          | If any characteristic is intended for promotion into `CG‑Spec`, the linkage is explicit and edition‑pinned (no shadow ids). *(Governing definition: `G.0`; wiring via `G.3:Ext.CGSpecPromotionWiring`.)*                                             |
| CC‑G3‑10          | UTS Name Cards exist for public ids minted or evolved by the CHR pack (twin labels plus public-id continuity notes). *(Delegation target: `CC‑GCORE‑UTS‑1` via `CC‑G3‑CoreRef`.)*                                                                      |
| CC‑G3‑11          | Worked examples and RSCR tests exist and cite `PathId/PathSliceId`; they cover illegal‑op refusal, unit and scale constraints, polarity invariants, and coordinate non‑entitlements.                                                      |
| CC‑G3‑12          | Thresholds/guard‑bands are not embedded in CHR artefacts; they remain governed by CAL acceptance clauses (`G.4`).                                                                                                                        |
| CC‑G3‑13          | When method‑role declarations are present (via `RoleDecls` and/or `QD.Role` alias), each declaration is **docked** to its governing pattern via a corresponding `G.3:Ext.*` module, and the edition and policy pins required by the governing pattern are surfaced to make downstream interpretation reproducible. *(QD/OEE governing patterns: `C.18` and `C.19`; wiring via `G.3:Ext.QD_OEE_Wiring`.)* |
| CC‑G3‑14          | **Evidence wired.** Each `CHR.Characteristic` links to R‑anchors via `PathId/PathSliceId` (and, where applicable, `A.10` anchor/carrier refs), so downstream evidence discipline (`G.6`) can audit legality and guard claims.            |
| CC‑G3‑15          | An `Archetypal Grounding` section exists with at least two domain‑distinct examples that demonstrate lawful CHR typing/legality and the CHR↔CAL separation (notably: no thresholds in CHR).                                          |
| CC‑G3‑16          | If `EvidenceLanes` are used, lane tags are declared with a citation to their governing pattern taxonomy (`B.3`), and any lane‑dependent tolerances/proof requirements are explicitly pinned (policy‑id / edition refs). Cross‑lane comparison/aggregation is **illegal by default** unless an explicit governing-pattern policy makes it lawful (typically `G.4`), and it must be auditable via evidence paths (`G.6`). |
| CC‑G3‑17          | When CHR outputs are bound into a planned baseline, identify the `A.15.2` WorkPlan and its local baseline locator. If the plan fills an independently declared operation argument or relation position under `A.15.3`, also use `CHRMechanismSuiteSlotFillingsPlanItem` with its governing declaration reference, member designator and plan-local filling-row locator, as governed by `A.19.CHR:4.1.2` (wiring via `G.3:Ext.SuiteBoundaryLinkage`). |
| CC‑G3‑18          | **Freshness is explicit.** Each `CHR.Characteristic` declares a validity window and either (i) an explicit `NonDecayingDecl` or (ii) a freshness/half‑life statement that is pinned to the governing pattern (`B.3.4`) when policy‑bound (`G.3:Ext.DecayWiring`). Changes in decay windows/policies participate in RSCR via canonical trigger kinds declared in `G.3:4.1`. |

### G.3:8 - Common Anti‑Patterns and How to Avoid Them

* **Hidden cardinalization.** Don’t treat ordinal encodings as interval/ratio; do publish coordinate policies that explicitly preserve order‑only invariants and forbid arithmetic upgrades.
* **Unit laundering.** Don’t add or average quantities with incompatible units; do force explicit unit discipline and legality checks via MM‑CHR governing definitions.
* **Polarity drift.** Don’t rely on “higher is better” implicitly; do publish polarity explicitly and make downstream use auditable.
* **Threshold leakage into CHR.** Don’t embed policy cut‑offs in CHR; do keep thresholds in CAL acceptance artefacts.
* **Unpinned semantics.** Don’t cite “the metric” or “the distance” without edition pins; do require edition‑pinned references when semantics affect interpretation.
* **Unscoped reuse.** Don’t reuse a characteristic or scale beyond its defining source and use on token continuity alone. Name the exact editions, bearer, scope and applicable window, reference plane, evidence, and intended downstream use; cite `F.9` only when an actual relation between the named local senses is needed and obtains.

### G.3:9 - Consequences

* **Legality becomes checkable.** Downstream patterns can reject illegal operations and rely on explicit legality surfaces rather than implicit conventions.
* **Comparability without semantic flattening.** Plural traditions remain representable because CHR preserves local meaning while making lawful relations explicit.
* **Reproducible downstream behavior.** Edition/policy pins make “why did this change?” answerable and RSCR actionable.
* **Authoring overhead.** The pattern shifts effort to up‑front authoring: explicit cards, pins, and tests are non‑optional when CHR becomes a public kit surface.

### G.3:10 - Rationale

CHR is the point where “numbers start moving” *only if* measurement semantics are stable enough to support lawful downstream reasoning. By making scale/unit/polarity explicit, publishing legality and guard surfaces, and requiring provenance pins, CHR authoring prevents downstream mechanisms from silently inventing their own legality assumptions.

Separating core invariants into `G.Core` prevents drift and ensures Part‑G‑wide properties (tri‑state, penalty routing, set‑return semantics, RSCR typing, Default Governing Definition Index) cite `G.Core` as their governing definition, while CHR remains responsible for CHR‑specific kit surfaces.

### G.3:11 - SoTA‑Echoing

This pattern aligns with post‑2015 best practice by:

* treating abstention/defer and set‑valued outcomes as first‑class design objects (consistent with modern selective prediction and set‑valued reporting practice),
* keeping multiobjective and archive‑based reasoning set‑returning rather than silently scalarizing (consistent with QD/illumination and open‑ended evaluation practice after 2015),
* making evaluation semantics reproducible through explicit edition/policy pinning (aligned with the modern emphasis on reproducibility and “specifying the evaluation surface” rather than only reporting metrics),
* modularizing method‑family specifics (QD/OEE, explore‑exploit) via explicit wiring and governing-definition assignment rather than embedding method semantics into universal measurement admissibility.

### G.3:12 - Relations

**Builds on:** `G.Core`, `G.1`, `G.2`, `G.6` (EvidenceGraph / Path citation), `A.19.CHR`, `A.15.2` (WorkPlan baselines), `A.15.3` (planned fillings of independently declared positions), `A.17–A.18/C.16` (MM-CHR), `F.0.1` (source-local meaning), `F.1` (source selection), `F.9` (actual relations between local-sense cells), `F.17` (scheme-sense cells), `F.18` (naming settlement), `C.2.1` (bounded-use claims), `B.3` / `B.3.4`, `A.10`, `E.10`, `E.5.1–E.5.3`.
**Uses (via Extensions):** `G.0` (promotion/linkage to `CG‑Spec`), optional `C.18 and C.19` (QD/OEE wiring).
**Publishes to:** `G.4` (admissible operators plus legality and guard macros and freshness pins), `G.5` (role declarations plus pins for reproducibility), `UTS` (Name Cards and public-id continuity notes), RSCR tests and hooks.
**Constrains:** any CAL/LOG/selector usage that consumes CHR (must treat CHR artefacts as typed/legal surfaces, not as prose hints).

### G.3:End

## G.4 - CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

> **Status:** Stable

**Use this when.** A team has typed characteristics and now needs to publish reusable operators, acceptance clauses, and legal compositions before any candidate is actually evaluated. The working object is one design-time `CAL Pack@CG-Frame`, not an evaluation run, verdict, selector outcome, assurance case, or decision.

**First move.** Write one plain acceptance statement for one task: “For subject `x` within `ClaimScope` `S` and evaluation window `W`, apply operator `O` to a C.16 measurement result for Characteristic `K` that argument declaration `R` admits. In the actual application, bind current result episteme `E`; the application of clause `A` returns `pass | fail | unknown` under threshold or policy `P` and its currentness rule.” Then turn only the reusable operator and clause definitions into stable CAL declarations. `E` belongs to the later application, not to reusable clause `A`.

**Smallest viable CAL pack.** Publish one charter for the exact CG frame, one typed operator card, one acceptance clause with `ClaimScope`, evaluation window, and unknown or failure behavior, one legal flow, one evidence and currentness profile, one proof-or-gap row, one worked declaration example, and a minimal editioned `TaskMap` that cites the exact charter, the C.22 `TaskSignatureRef`, and the declaration refs used by selection. Stop there when this pack answers the task; method-family extensions, archive surfaces, crossing records, and additional policy pins enter only when the case actually needs them.

**What changes in practice.** Thresholds and failure behavior stop hiding in code, illegal arithmetic becomes an authoring defect, and runtime workers can cite stable declarations without pretending that a card, flow, manifest, proof row, or stored evidence ref performed an evaluation.

**Not this pattern.** Use C.16 for the measurement result, A.19 for comparison or selection, A.13 and A.15.1 for each precise performer and independently admitted dated evaluation Work, F.6 only when exact assignment-bound attribution is current, A.6.1 for actual bindings, C.2.1 for the verdict episteme, A.10/G.6 for provenance, G.11 for currentness, B.3 for assurance, and C.11 for a decision. If the immediate question is whether a declared clause actually ran and what result obtained, go directly to the declaration-to-runtime boundary in §4.4a.

### G.4:1 - Problem frame

CAL authoring starts from:

* one exact `CG‑Frame` with its `EntityOfConcern`, `ReferencePlane`, task, and assumption envelope,
* a plurality of method traditions and claims (SoTA inputs), and
* CHR‑typed measurement constructs (`Characteristic/Scale/Coordinate` + legality guard macros).

Before any run‑time selection, comparison, aggregation, or selected-set formation is executed downstream, authors need an explicit, auditable **CAL Pack** that:

1. defines *what operators exist* and what they are allowed to do over CHR types,
2. externalizes *fit-for-purpose acceptance* as typed predicates whose use is bounded by an exact `ClaimScope`, evaluation window, and any separate qualification window that limits use, and
3. binds these choices to an evidence wiring surface (lanes, provenance anchors, policy pins, and refresh triggers) so that downstream selection, logging, parity, and shipping can cite *stable ids* rather than re‑inventing semantics.

This pattern provides the design‑time authoring kit and the publication surface for CAL artifacts, while delegating Part‑G‑wide invariants to `G.Core` and CN-Spec and CG-Spec legality to `CG‑Spec`/`CN‑Spec`.

### G.4:2 - Problem

Teams repeatedly face drift and ambiguity in the CAL Pack that sits between “typed measurements exist” and “a selector/dispatcher runs”:

* **Illicit operations** slip in (implicit cardinalization, unit laundering, ordinal arithmetic).
* **Acceptance is scattered** (thresholds embedded in code or in CHR prose; predicates not typed; unknown handling inconsistent).
* **Evidence wiring is underspecified** (which provenance anchors matter, what policy ids are in force, what is plane‑scoped, what changes must trigger refresh).
* **Cross-sense or cross-plane imports are silent** (hidden reuse across distinct source-local meanings, ReferencePlanes, or editions without the obtaining relation, required crossing records, and loss accounting).
* **Tooling artifacts become semantics** (vendor flags or implementation details substitute for a conceptual specification).

### G.4:3 - Forces

* **Expressiveness vs legality.** CAL must allow useful comparisons/aggregations while staying lawful under CHR typing and legality gates.
* **Pluralism vs comparability.** Multiple method traditions must coexist without forcing premature unification, yet remain cross‑citable and auditable.
* **Decision support vs auditability.** CAL must support selection and selected-set formation while preserving explicit, reviewable assumptions and proofs.
* **Exploration vs assurance.** CAL must support exploratory regimes (probing, novelty, open‑ended search) without letting un‑assured outputs silently become dominance claims.
* **Locality vs portability.** Each CAL clause stays bounded by its declared `ClaimScope`, window, source meanings, and ReferencePlane; reuse beyond that boundary requires the exact relation and crossing records that the changed value calls for.

### G.4:4 - Solution — author the smallest lawful CAL pack

#### G.4:4.0 - Practitioner authoring path C1–C9

Complete these actions in order; widen a step only when its stated input is needed by the current task.

1. **C1 — Charter the scope.** Name the exact `CG‑Frame`, `EntityOfConcern`, `ReferencePlane`, task, `CNSpecRef.edition`, and `CGSpecRef.edition`. State the assumption envelope in ordinary language.
2. **C2 — Declare one typed operator.** Give it a stable id, CHR-typed signature, preconditions, result kind, and failure behavior. This is an `A.6.1` operation declaration, not evidence of an application.
3. **C3 — Declare one acceptance clause.** Name the exact Characteristic and the A.6.1 argument declaration that admits the corresponding C.16 measurement-result episteme, then declare the predicate or threshold, `ClaimScope`, evaluation window, any separate qualification window that limits use, unknown handling, and the stated stop, degrade, or abstain behavior. Keep the exact current result episteme for the later application. If the clause claims statistical risk or coverage control, also name the loss, target, calibration population and window, sampling or exchangeability assumptions, declared treatment of shift, and the exact policy that states the guarantee.
4. **C4 — Compose only a legal flow.** Cite the operators and gating clauses, preserve the lawful result kind, and keep a selected set when no lawful scalarization exists. A declared DAG is possible composition, not performed work.
5. **C5 — Name the minimum evidence/currentness need.** Cite the exact A.10 source/provenance anchors and G.11 window needed to judge the clause. Do not turn an evidence profile, citation, or graph membership into a verdict or actual reliance.
6. **C6 — Add an extension only when the task needs one.** Select its current subject pattern first, then pin only the descriptor, distance, insertion, exploration, branch, or path records that change the present CAL action. Otherwise omit the extension.
7. **C7 — Record proof or an explicit gap.** For every operator, flow, or clause, cite the legality/monotonicity/boundedness justification actually required; when it is missing, publish the gap and the consequent degrade/abstain behavior.
8. **C8 — Exercise declaration behavior.** Provide one worked authoring example and focused conformance tests for illegal operations, `pass | fail | unknown`, freshness, and failure behavior. The example and test remain declarations/test records unless separately grounded dated work is named.
9. **C9 — Publish and hand off.** Mint stable ids and continuity notes, then emit the smallest immutable `TaskMap` edition. It cites the exact charter edition, the already constituted C.22 `TaskSignatureRef`, the task, and edition-bearing operator, flow, gating-clause, and evidence-profile refs; the cited evidence profiles carry the needed currentness pins. It neither constructs the TaskSignature nor copies clause thresholds. Use G.11 for change refs; G.4 defines no refresh rule or runtime occurrence or result.

The authoring path is complete when a cold reader can reconstruct the plain acceptance sentence from the published ids and can also say what still has to happen at runtime. The detailed manifests, schemas, interfaces, and optional extension blocks below make the same pack machine-citable; they do not add another practitioner sequence.

#### G.4:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).** Canonical shape, Nil‑elision, and the Expansion rule are defined in `G.Core`.

```text
GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
GCorePinSetId.PartG.CrossingVisibilityPins
},

CorePinsRequired := {
UTSRowId[],                 // CAL artefacts are public ids (Name Cards plus public-id continuity notes)
ΓFoldRef.edition?            // pin an actual numerical composition model/policy when used; otherwise cite the governing rule
},

// consumed iff no explicit `ΓFoldRef.edition` override is pinned
DefaultsConsumed := { DefaultId.GammaFoldForR_eff },

RSCRTriggerSetIds := { GCoreTriggerSetId.SoTAHarvestSynthesis },
RSCRTriggerKindIds := {      // deltas (Expansion rule applies)
  RSCRTriggerKindId.PenaltyPolicyEdit,
  RSCRTriggerKindId.DefaultGoverningDefinitionChange,
  RSCRTriggerKindId.BaselineBindingEdit
}
⟩
```

By the `G.Core` Expansion rule, the effective conformance ids / trigger kinds / pin obligations for `G.4` are the expansions of the referenced profiles/sets/pin‑sets plus the explicit deltas above.

Notes (normative intent, delegated semantics):

* The semantics of tri‑state outcomes, penalty routing, set‑return discipline, crossing visibility, P2W split, typed RSCR causes, and the Default Governing Definition Index are governed in `G.Core` and are not redefined here.
* EvidenceGraph/Path pins (when used) are declared only via **`G.4:Ext.EvidenceGraphWiring`** in **G.4:4.5** (so `G.Core linkage` stays minimal and does not “pull in” `G.6` by default).
* Method‑specific pins (e.g., QD descriptor/distance/insert policy pins; open‑ended transfer rules pins) MUST appear only in **Extensions** blocks (see **G.4:4.5**) and MUST NOT introduce competing defaults.

#### G.4:4.2 - `CAL Pack@CG-Frame` surface (kit governed by this pattern)

`CAL Pack@CG-Frame` is the CG‑Frame’s published CAL Pack. Minimally, it provides:

* `CAL.Charter` — identification and assumption basis for this CAL pack:

  * cites the exact `CGFrameId`, `EntityOfConcernRef`, and `ReferencePlane`,
  * cites the governance and legality records (`CNSpecRef`, `CGSpecRef`) by edition,
  * records the assumption envelope on which the acceptance predicates rely without minting another governance or legality record.
* `TaskMap` — the conditional G.4 handoff record to `G.5` when CAL gates are current; one exact edition names the task, cites the already constituted C.22 `TaskSignatureRef` and exact charter edition, and cites the acceptance-clause, operator, flow, and evidence-profile refs that selection actually consumes. It does not constitute the TaskSignature or contain threshold values.
* `CAL.Operator[]` — UTS‑published typed operation declarations governed by `A.6.1`; a card declares possible arguments, result kinds, and conditions but does not assert that an operation ran:

  * explicit signature over CHR types,
  * explicit preconditions/postconditions (incl. legality guard macros references),
  * explicit provenance/evidence hooks (by ids/pins, not by tool behavior).
* `CAL.Acceptance[]` — typed predicate declarations whose use is bounded by the declared `ClaimScope`, evaluation window, and any separate qualification window; a clause declares how an actual application is judged but is not itself a verdict:

  * binds to CHR characteristic ids and to exact A.6.1 argument declarations for admissible C.16 measurement-result epistemes (and, when inducing numeric comparison or aggregation, to `CG‑Spec.characteristic` ids),
  * keeps the exact current result episteme in the later application binding rather than in the reusable clause,
  * exposes unknown handling and failure behavior via policy pins.

Each `resultInputDeclarationRef` resolves an A.6.1 `ArgumentDeclaration` whose meaning names the C.16 measurement-result episteme expected by the clause, whose exact ValueKind and binding designation rule are explicit, and whose admissibility conditions require the named Characteristic and result shape. A deliberately one-off clause may also cite an already existing episteme in `fixedResultEpistemeRefs[]?`; mark that clause one-off instead of presenting it as reusable.
* `CAL.Flow[]` — legality‑checked declarations of possible operator composition; a declared DAG is not performed work:

  * declares result kind (scalar only when lawful; selected-set / set-result when partial orders remain partial orders),
  * records which acceptance clauses gate which flows.
* `CAL.EvidenceProfiles` — evidence wiring surface:

  * lane tags (`F/G/R`) / provenance anchors / policy pins needed for `SCR` and audit surfaces,
  * explicit freshness/decay hooks (freshness window + decay/Γ_time selectors) as pinned policies/refs (not prose).
  * explicit `ReferencePlane` and any used penalty-policy refs (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`); the ProofLedger supplies the receiving quantity, scale, input meanings, assumptions, and derivation or calibration. Monotonicity and boundedness alone do not justify a numerical loss.
* **Optional** `CAL.NQD[]` — QD/OEE‑related calculus surfaces when declared:

  * descriptor/distance/insertion artifacts are pinned by ids/editions,
  * semantics are governed by method‑specific governing definitions (e.g., `C.18`, `C.19`) and not redefined by CAL.
A CAL clause that consumes G.7 calibration states its exact receiving use and premises. A locally justified CL threshold is an additional policy condition; the ProofLedger and named authority must support that condition. It does not replace the bounded-use claim, target classification or reliance result. A policy waiver changes only the authorized policy condition.

* `CAL.ProofLedger` — a proof/justification ledger:

  * links operator/flow/clause ids to their needed legality and soundness results; a numerical support fold includes the B.3/C.2.2 receiving model, compatible scales and inputs, dependence assumptions, and boundary behavior.
* Publication artifacts:

  * UTS Name Cards (twin labels) for all public ids,
  * RSCR tests ids and Worked‑Examples ids,
  * deprecation notices and edition bump notes as public-id continuity records.

Boundary discipline (normative):

* **No shadow specs**: CAL artefacts cite `CN‑Spec`/`CG‑Spec` and do not introduce competing “local specs” (delegated; see `CC‑GCORE‑CN‑CG‑1` via **CC‑G4‑CoreRef**).
* **Shipping boundary:** `G.10` governs shipping; see `CC-GCORE-SKP-1` via **CC-G4-CoreRef**.
* **Refresh boundary:** CAL publishes pins/payload for refresh; `G.11` governs refresh orchestration.

**Minimal schema fragments (notation‑independent; fields for citation, not an implementation schema):**

```
CAL.Charter :=
  ⟨ charterId, charterEdition, cgFrameId, entityOfConcernRef, referencePlaneRef,
    CNSpecRef.edition, CGSpecRef.edition, assumptionEnvelope ⟩
CALCharterRef := <charterId, charterEdition>

TaskMap :=
  ⟨ taskMapId, taskMapEdition, charterRef := CALCharterRef,
    taskRef, taskSignatureRef := TaskSignatureRef,
    acceptanceClauseRefs[], operatorRefs[], flowRefs[], evidenceProfileRefs[] ⟩
TaskMapRef := <taskMapId, taskMapEdition>

CAL.Pack@CG-Frame :=
 ⟨ calPackId, charterRef, taskMapRef, operatorIds[], acceptanceClauseIds[], flowIds[],
 evidenceProfileIds[], proofLedgerId, nqdIds[]?,
    utsRowIds[], workedExampleIds[], rscrTestIds[], publicIdContinuityNoteIds[] ⟩

CAL.Operator :=
  ⟨ operatorId(UTS), signature(CHR-typed), preconditions[], postconditions[],
  evidenceProfileRefs[]?, failureBehaviorRef?, crossingRefs[]? ⟩

CAL.Acceptance :=
  ⟨ clauseId(UTS), characteristicRefs[], resultInputDeclarationRefs[],
    fixedResultEpistemeRefs[]?,              // deliberately one-off clause only
    cgSpecCharacteristicRefs[]?, predicateRef, claimScopeRef,
    evaluationWindow, qualificationWindow?, unknownHandlingRef,
    failureBehaviorRef, evidenceProfileRefs[]?, crossingRefs[]? ⟩

CAL.Flow :=
  ⟨ flowId(UTS), dag(operatorIds, edges), gateClauses(acceptanceClauseIds),
    resultKind, decisionAidPolicyRef? ⟩

CAL.EvidenceProfile :=
  ⟨ evidenceProfileId(UTS), lanes(F/G/R), anchors(A.10)[],
    freshnessPolicyPins[]?, penaltyPolicyPins[]?, ΓFoldRef.edition? ⟩
```

`CALCharterRef` and `TaskMapRef` each resolve one immutable edition. A changed charter, task, TaskSignature edition, clause, operator, flow, evidence profile, or edition-bearing cited list creates a new `taskMapEdition`; an old `TaskMapRef` continues to resolve its old values. The C.22 TaskSignature remains a separately constituted episteme. The map relates that exact signature to the CAL declarations used by selection but neither derives the signature nor duplicates their thresholds.

When CAL authoring relies on SoTA coverage, consume G.2's pack `CoverageJudgementRef` with its HarvestPolicy basis and receiving question. Preserve the distinction between family coverage and lineage/material-entry plurality. A CAL clause does not turn a combined method/generator count into method-only coverage.

#### G.4:4.4 - Interfaces (minimal I/O surface)

| Interface                 | Consumes                                            | Produces                                                                                  |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `G.4-1 Charter`           | exact `CGFrameId`, `EntityOfConcernRef`, `ReferencePlane`, `CNSpecRef.edition`, `CGSpecRef.edition`, assumption envelope, SoTA inputs, `CHR Pack@CG-Frame` | one immutable `CAL.Charter` edition and its `CALCharterRef` |
| `G.4-2 Operators`         | CHR typing + SoTA operator inventory                | `CAL.Operator[]` (UTS ids; typed signatures; refs to evidence profiles & guards)  |
| `G.4-3 Acceptance`        | task intent, exact Characteristic and A.6.1 result-input argument declarations, `ClaimScope`, evaluation window, any separate qualification window that limits use, policy pins, and CHR characteristics; exact result-episteme refs only for a clause explicitly marked one-off | `CAL.Acceptance[]` (typed predicate or threshold; admissible result-input declarations; scope; evaluation and applicable qualification windows; freshness pins; unknown and failure behavior refs) |
| `G.4-4 Flows`             | Operator cards + admissible aggregators             | `CAL.Flow[]` (legality‑checked compositions; declared result kind)                        |
| `G.4-5 NQD Surface`       | Task intent + policy pins + (optional) QD/OEE inputs | `CAL.NQD[]` (descriptor/distance/insertion refs + edition pins; optional)  |
| `G.4-6 Publish`           | all above, exact task, C.22 `TaskSignatureRef`, proofs, and examples | versioned `CAL Pack@CG-Frame`, exact `CALCharterRef`, and the smallest immutable `TaskMap` edition plus `TaskMapRef`, citing the task, matching TaskSignature, and acceptance-clause, operator, flow, and evidence-profile refs; also UTS entries, RSCR tests, Worked-Examples, and public-id continuity notes |

#### G.4:4.4a - Declaration-to-runtime evaluation boundary (normative)

A CAL pack is a reusable design-time declaration. A stored operator card, clause, flow, `TaskMap`, proof-ledger row, test, or evidence-profile reference establishes neither an actual participant nor performed evaluation. When a CAL declaration is applied, recover the runtime chain explicitly:

1. Name one exact `EvaluationMethod` (`U.Method`). Its `U.MethodDescription` may state generic participants, parameters, effects, and evaluation conditions, but it carries no actual-participant slots and no intrinsic claim that a test, proof, or acceptance event occurred.
2. Cite the exact `CAL.Operator`, `CAL.Flow`, and `CAL.Acceptance` declarations as `A.6.1` operation semantics. Resolve the clause's `resultInputDeclarationRef`, then bind the exact current C.16 measurement-result episteme in this application and test it against the declaration's Characteristic and admissible result shape. Use the exact `A.6.1` declaration and application bindings; do not infer them from a compatible signature, `TaskMap`, or stored reference.
3. First recover every precise performer's A.13 core for the exact evaluation action, scope, working situation, and window, including the same obtaining assignment later used by any attribution. A.15.1 then independently admits one dated `EvaluationWork : U.Work` from its performance history, enacted Method, extent, and containing-System relation. Add F.6 afterward only when the receiving claim needs exact assignment-bound attribution through that same assignment. Recover the evaluated or affected referent, actual resources, and every concrete participant through its direct subject relation or an `A.6.1` application binding. A compact attribution account may omit only an assignment identifier unused by its receiving claim; it omits no consumed fact. Ordinary activity not claimed as `U.Work` does not enter this branch.
4. State the local result under its direct predicate and pattern. A `CAL.Acceptance` application yields its exact `pass | fail | unknown` verdict; use A.19 for comparison and selection results, C.16 for measurement results, and C.11 for a decision result. No generic evaluation-result or work-result field substitutes for these objects.
5. When a durable assertion is needed, constitute one `C.2.1` result episteme whose ClaimGraph states that local result, evaluated subject, interpretation basis, polarity or domain status, and uncertainty when current. The episteme is not the domain result and does not create it.
6. Attach source recovery and provenance through A.10/G.6 and currentness through G.11. State the A.10 evidence-provenance account and local `RelianceDisposition` for the bounded use, citing the direct rule for any reliance relation. Enter B.3 when an actual named assurance claim is current; a consequential use without one retains its direct governing rule. A citation, ledger edge, evidence profile, disposition, or assurance record does not establish the work, participant, application, or local result it describes.
7. A later selector, acceptance action, or decision is another governed occurrence. It relies on the result episteme through an exact premise, reference, decision-use, or operation-argument relation; mere storage, citation, or graph membership does not establish actual use.

This chain keeps declaration, execution, local result, result episteme, provenance, bounded reliance, currentness, acceptance, and decision independently recoverable.

#### G.4:4.5 - Extensions (pattern‑scoped; non‑core)

`G.4` supports method‑family and discipline‑specific calculus variations exclusively via pattern‑scoped extensions.

**GPatternExtension block: `G.4:Ext.EvidenceGraphWiring`**
- **PatternScopeId:** `G.4:Ext.EvidenceGraphWiring`
- **GPatternExtensionId:** `EvidenceGraphWiring`
- **GPatternExtensionKind:** `InteropSpecific`
- **GoverningPatternId:** `G.6`
- **Entry:** use only when this CAL pack must cite a shared, addressable G.6 path or slice across more than one downstream consumer.
- **Stop:** omit the block when a local A.10 source-to-use account is sufficient; remove it when no current clause, proof, or example cites the path.
- **Uses:** `{G.6}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `EvidenceGraphId?`
  - `PathId[]/PathSliceId[]`
  - `UTSRowId[]` (for cited artifacts)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
- **Notes (wiring‑only):** This block does not define EvidenceGraph semantics; it only fixes that CAL proofs/examples may cite evidence by Path ids.

**GPatternExtension block: `G.4:Ext.NQD`**
- **PatternScopeId:** `G.4:Ext.NQD`
- **GPatternExtensionId:** `NQD`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.18`
- **Entry:** use only when the current task applies a C.18 quality-diversity/archive method and its descriptor, distance, insertion, or archive policy must be pinned for CAL use.
- **Stop:** omit or retire the block when the task has no current archive/QD clause or when those refs no longer change a CAL action.
- **Uses:** `{C.18}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `DescriptorMapRef.edition`
  - `DistanceDefRef.edition`
  - `InsertionPolicyRef`
  - `ArchiveRef?`
  - `TaskSignatureRef?` (if activation is TaskSignature‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
- **Notes (wiring‑only):** CAL does not redefine QD semantics; it only pins the descriptor, distance, and insertion records needed for reproducible archive behavior. Any archive/illumination summaries (e.g., coverage / QD‑score / occupancyEntropy / filledCells) are published as report‑only outputs unless an explicit CAL acceptance clause/policy authorizes promotion.

**GPatternExtension block: `G.4:Ext.EELog`**
- **PatternScopeId:** `G.4:Ext.EELog`
- **GPatternExtensionId:** `EELog`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.19`
- **Entry:** use only when the current task has a C.19-governed exploration/exploitation budget or probe-accounting rule that changes a CAL clause or failure branch.
- **Stop:** omit or retire the block when no current CAL action consumes those C.19 refs.
- **Uses:** `{C.19}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `ExploreExploitBudgetPolicyRef`
  - `ProbeAccountingRef?`
  - `FailureBehaviorRef?` (if probe/sandbox is policy‑bound)
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`

**GPatternExtension block: `G.4:Ext.SoSLogBranches`**
- **PatternScopeId:** `G.4:Ext.SoSLogBranches`
- **GPatternExtensionId:** `SoSLogBranches`
- **GPatternExtensionKind:** `MethodSpecific`
- **GoverningPatternId:** `C.23`
- **Entry:** use only when C.23-governed SoS-LOG branches currently explain a CAL degrade/abstain path.
- **Stop:** omit or retire the block when those branch/rule ids no longer change a current CAL clause, flow, or explanation.
- **Uses:** `{C.23}`
- **⊑/⊑⁺:** `∅`
- **RequiredPins/EditionPins/PolicyPins (minimum):**
  - `SoSLogRuleId[]`
  - `SoSLogBranchId[]`
  - `FailureBehaviorPolicyId`
- **RSCRTriggerSetIds:** `∅`
- **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
- **Notes (wiring‑only):** This block only pins branch/rule ids for degrade/abstain explanation; it does not redefine rule semantics.

### G.4:5 - Archetypal Grounding

**Tell.** A team working within a CG‑Frame must choose and justify a set of candidate methods (possibly a selected set or a set retained in an archive) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement basis; CAL declares auditable predicates and flows that separately grounded runtime work may apply.

**Show 1 (bounded CAL pack skeleton).**
Use: R&D selected-set choice. The pack names the exact CG frame and EntityOfConcern, candidate-set `ClaimScope`, ReferencePlane, and evaluation window. CHR defines `SafetyClass(ord↑)`, `CostUSD_2026(ratio↓)`, `Readiness(nominal)`.

* `CAL.Operator: DominatesPareto`
  Signature over CHR types, precondition references CHR guard macros.
* `CAL.AcceptanceClause: AC_SafetyGate`
  Reusable typed predicate for `SafetyClass` (and its levels), citing `SafetyResultArgument-D1`, the A.6.1 argument declaration that admits a C.16 measurement-result episteme for that Characteristic. Thresholds are valid for the stated `ClaimScope` and evaluation window; unknown handling uses tri-state pins. The clause names no current measurement-result episteme.
* `CAL.Flow: Flow_ParetoPortfolio`
  Declares a selected-set result kind; gated by `AC_SafetyGate` and `AC_Budget`.
* `CAL.EvidenceProfile: EP_SafetyEvidence`
  Declares anchor ids and freshness policy pins required for `SCR`.

When this CAL pack supplies selector gates, it publishes `TaskMapRef=<SafetySelectionMap, E3>`. That map cites `CALCharterRef=<SafetyCALCharter, E2>`, C.22 `TaskSignatureRef=SafetyPortfolioTaskSignature-E4`, the exact task, and edition-bearing refs `AC_SafetyGate-E2`, `Flow_ParetoPortfolio-E1`, `DominatesPareto-E3`, and `EP_SafetyEvidence-E4`; it contains no threshold values. Downstream G.5 consumes the exact TaskSignatureRef and this TaskMapRef together, verifies that the map cites the same signature, and resolves the charter and declarations through their refs. If the charter or a cited clause changes, G.4 publishes another TaskMap edition; selectors that still cite `<SafetySelectionMap, E3>` continue to replay the old boundary.

**Show 2 (explicit cross-sense or ReferencePlane import).**
A `SafetyClass` result uses an expression with a different F.17 source-local meaning or comes from another ReferencePlane. CAL may author a clause using it only after the exact F.17 cells and obtaining F.9 relation are cited when meanings differ, and the applicable plane or edition crossing records are cited when those values differ. The clause keeps its declared `ClaimScope` and window; the import does not silently widen either.

**Show 3 (one performed acceptance evaluation).**

Before the candidate action is admitted as Work, A.13 recovers `SafetyEvaluatorSystem-17 : U.System` for exact action `SafetyAcceptanceEvaluationAction-17`. Its admitted `SafetyEvaluatorBoundary-17` contains the evaluation controller, its active decision state, and the input/output channels through which it applies the clause; it excludes the CAL declarations, measurement-result episteme, candidate, assignment, and containing team System. The action's scope is `SafetyAcceptanceClaimScope-17`, its working situation is `SafetyGateEvaluationSituation-17`, and its window is `2026-07-30T09:00:00Z` through `2026-07-30T09:20:00Z`. It is directed by `SafetyAcceptanceDecisionNorm-17`: apply the current clause to admissible current inputs, return `unknown` rather than force a threshold verdict when uncertainty crosses the boundary, and reject an input whose declared result shape is incompatible. The relevant conditions are clause edition, result-shape admissibility, measurement currentness, and uncertainty relative to the threshold.

The local kind `SafetyAcceptanceEvaluatorSystemRole` is declared under A.2. Its membership criterion requires the stable work-facing contribution of safety-acceptance evaluation and goal-directed, condition-sensitive regulation under `SafetyAcceptanceDecisionNorm-17`: the holder must bind admissible inputs, choose the clause-defined verdict, and abstain or return `unknown` when the declared conditions require it. `SafetyEvaluatorDecisionTrace-17` shows `SafetyEvaluatorSystem-17` rejecting an incompatible result shape and returning `unknown` when the admissible uncertainty interval crosses the threshold; the system-boundary and runtime records show that those actions occurred within `SafetyEvaluatorBoundary-17`. The cited decision-trace, system-boundary and runtime records support the criterion facts under A.2's membership rule; A.10 makes that source-to-use account recoverable. The case independently classifies `SafetyEvaluatorSystem-17` under `SafetyAcceptanceEvaluatorSystemRole`. Neither the candidate Work nor the assignment supplies that classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed here.

The same A.13 core uses `SafetyAcceptanceEvaluationAssignment`, a directly declared `U.SystemRoleAssignment` species under A.2.1. The species defines holder, assigned-kind, and evaluation-candidate participant meanings; its predicate appoints the holder to evaluate that candidate under the applicable clause for the stated scope, situation, and window. `SafetyAcceptanceEvaluationAssignment-17` obtains with `SafetyEvaluatorSystem-17` as holder, `SafetyAcceptanceEvaluatorSystemRole` as assigned-kind value, and `C-17` as evaluation candidate. Its maximal uninterrupted predicate-true interval covers the full stated window.

Only after that A.13 core is established does A.15.1 independently admit `EvalWork-2026-07-30-17 : U.Work` from its exact performance history, enacted `SafetyAcceptanceMethod`, temporal extent, and obtaining containing-System relation to independently admitted `SafetyEvaluationTeamSystem-17`. The actual A.6.1 application `SafetyAcceptanceApplication-17` binds candidate `C-17` separately from its binding of current C.16 measurement-result episteme `SafetyMeasureResult-E17` to `SafetyResultArgument-D1` while using unchanged reusable clause `AC_SafetyGate`. Neither the assignment nor an F.6 conclusion is an A.15.1 admission premise.

Because this worked case explicitly says that the Work was performed under an assignment, F.6 afterward establishes `performedUnderAssignment(EvalWork-2026-07-30-17, SafetyAcceptanceEvaluationAssignment-17)` through the same obtaining A.13 assignment. The direct case fact links that exact pair, holder equality holds, and the assignment interval covers the Work. A different overlapping assignment held by the same performer would not establish this attribution.

`SafetyMeasureResult-E17` states the measured safety characteristic, scale, attributed value, uncertainty, model, calibration, and measurement Work; it is neither the raw detector output nor the acceptance verdict. The clause application obtains `unknown` because the uncertainty interval crosses the threshold. A later `SafetyMeasureResult-E18` can bind through separately identified `SafetyAcceptanceApplication-18` while `AC_SafetyGate` remains unchanged. A C.16 result for `CostUSD_2026`, a result with an incompatible declared shape, or raw detector output fails `SafetyResultArgument-D1` before the predicate runs; it does not cause a new reusable clause edition. A separate C.2.1 episteme asserts that exact verdict and cites its provenance under A.10 and, when the EvidenceGraph extension is present, G.6; G.11 supplies currentness. A later C.11 result may record `defer`, and its claim uses the verdict episteme through an exact premise or decision-use relation. Any decision-making Work remains separate. The clause card, proof-ledger row, evidence edge, and decision record do not retroactively establish the measurement Work or the evaluation occurrence.

**Show 4 (a support model and its separate acceptance threshold).**

For the pump-triage use in G.5 §0.5, consider a separately declared gated variant. `AC_InputConditionGate-E1` accepts a declared probability of at least 0.85 that both the measurement series is valid (event A) and its time alignment is valid (event B) for the same 24-hour input. Its scope, evaluation window, result-input declaration, and `unknown` behavior belong to this G.4 clause, not to the default composition rule. `PumpInputEvidence-E1` supplies the receiving model and provenance for those event meanings and probabilities. An applicable `TaskMapRef` binds that clause, profile, and the matching C.22 task signature.

Suppose the application inputs establish P(A)=0.9 and P(B)=0.9 and the profile's model establishes independence. The model gives P(A ∩ B)=0.81, so the clause returns `fail`. Minimum 0.9 would incorrectly pass. If independence or a justified conditional alternative is unavailable, the missing joint probability yields the clause's `unknown` result, with the declared downstream degrade/abstain behavior; a high F or formal line tag cannot replace it.

For a different receiving question that asks only for a qualified comparison on existing heterogeneous support, the profile retains the proof, empirical contributions, shared-bias limitations, and contrary evidence under B.1.3/C.2.2. It does not invent a probability or apply `AC_InputConditionGate-E1` to that different question. The ordinary G.5 shortlist remains available without an additional assurance calculation.

### G.4:6 - Bias-Annotation

CAL is where “what counts as acceptable” is encoded. Typical bias vectors include:

* threshold‑selection bias (arbitrary floors masquerading as natural laws),
* measurement bias amplified by illegitimate arithmetic or hidden scalarization,
* survivorship bias in Worked‑Examples and probe telemetry,
* Goodhart pressures when report‑only telemetry is accidentally treated as dominance.

The pattern mitigates these by requiring typed acceptance clauses, explicit policy pins, and an auditable ledger of proofs and justifications, while keeping cross-sense and ReferencePlane reuse explicit and placing penalties only in the explicit assurance lane.

### G.4:7 - Conformance Checklist (normative)

| ConformanceId     | Statement                                                                                                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G4‑CoreRef** | Conformance with `G.4` requires satisfying the effective `G.Core` obligations referenced by the `GCoreLinkageManifest` in **G.4:4.1** (profiles, pin sets, consumed defaults, and trigger kinds).                                                                                                              |
| **CC‑G4‑01**      | `CAL Pack@CG-Frame` is published as a notation-independent object with stable UTS ids (Name Cards with twin labels) for `CAL.Charter`, `TaskMap`, all operator, acceptance-clause, flow, and evidence-profile declarations, Worked-Examples, and public-id continuity notes, including deprecations and lexical-continuity notes. Tooling/vendor details remain non-normative. |
| **CC‑G4‑02**      | Each exact `CALCharterRef = <charterId, charterEdition>` resolves one immutable charter edition naming the exact `CGFrameId`, `EntityOfConcernRef`, `ReferencePlane`, `CNSpecRef.edition`, `CGSpecRef.edition`, and assumption envelope on which the pack relies. |
| **CC‑G4‑03**      | Every `CAL.Operator` has an explicit CHR‑typed signature and explicit preconditions; any legality guard macros referenced are cited by id (no “implicit legality”).                                                                                                                                             |
| **CC‑G4‑04** | Every reusable `CAL.Acceptance` binds the exact Characteristic and exact A.6.1 `resultInputDeclarationRef` values that declare the admissible C.16 measurement-result episteme inputs; the exact current result episteme is bound only in an actual application. A clause marked one-off may additionally cite `fixedResultEpistemeRefs[]?`. Every clause also declares its predicate or threshold, `ClaimScope`, evaluation window, any separate qualification window that limits use, unknown handling, and failure behavior. A statistically risk-controlled clause also names its loss, target, calibration population and window, sampling or exchangeability assumptions, declared treatment of shift, and the exact policy that states or defines the guarantee. Inputs with distinct source-local meanings cite the exact F.17 cells and obtaining F.9 relation; cross-plane or cross-edition inputs cite their applicable crossing records. None of these declarations establishes performed evaluation or a verdict. |
| **CC‑G4‑05**      | If an acceptance clause, operator, or flow induces numeric comparison or aggregation, it cites the relevant `CG‑Spec.characteristic` ids and links to legality proof refs (CSLC) in the ProofLedger; otherwise it must be authored so that downstream can degrade or abstain rather than perform illegal operations. |
| **CC‑G4‑06**      | Every `CAL.Flow` declares its result kind and the set of gating acceptance clauses; any thinning/selection‑aid policies (e.g., ε‑front selection) are explicitly policy‑bound and do not silently replace the underlying result kind.                                                                      |
| **CC‑G4‑07** | Every `CAL.EvidenceProfile` declares the provenance anchors, evidence lanes, and currentness or loss-policy pins its use needs. It cites `DefaultId.GammaFoldForR_eff` for B.3/C.2.2 support-model discipline and pins any numerical Γ-fold actually used. That calculation must preserve input meanings, scales, dependencies, formal/empirical distinctions, and mapping limits; absent a common model, retain separate support and a bounded synthesis. Losses affect R only and do not define dominance or an acceptance threshold. |
| **CC‑G4‑08** | `CAL.ProofLedger` links each operator, flow, or clause to its required proof or justification and explicit failure behavior. A numerical Γ-fold or loss includes its receiving quantity, input scales, dependency model, derivation or calibration, assumptions, and boundary behavior; monotonicity and boundedness alone are insufficient. A missing required model cannot be repaired by F-to-R conversion or an invented default score. |
| **CC‑G4‑09**      | CAL publication includes RSCR tests and Worked‑Examples sufficient to detect illegality (incl. unit laundering / ordinal arithmetic), to exercise authored acceptance/flow behavior, and to validate the authored freshness envelope when it is part of admissibility; missing tests/examples are treated as an auditable gap, not as “assumed OK”. |
| **CC‑G4‑10**      | Each `TaskMapRef = <taskMapId, taskMapEdition>` resolves one immutable map edition containing the exact `CALCharterRef`, task, C.22 `TaskSignatureRef`, and edition-bearing acceptance-clause, operator, flow, and evidence-profile refs used by selection. Changing the charter, task, signature edition, or a cited component creates a new map edition. When G.4 gates are current, G.5 consumes this exact map alongside the same `TaskSignatureRef`; a mismatch or unresolved ref blocks that gated selector use. The map neither constructs the TaskSignature nor embeds thresholds or duplicates acceptance semantics. |
| **CC‑G4‑11**      | Any method/discipline specifics are placed under `G.4:4.5 Extensions` as `GPatternExtension` blocks (stable `PatternScopeId`, explicit governing definition, pins, and RSCR triggers); no extension introduces competing defaults or replaces `G.Core` invariants. |
| **CC‑G4‑12**      | `CAL Pack@CG-Frame` includes public-id continuity records for public ids: deprecations, edition bumps, and lexical-continuity notes. It exposes refresh payload pins, including editions, policies, UTS ids, and, when present, `PathId` and `PathSliceId`, sufficient for `G.11` to plan RSCR without inferring semantics from prose. |
| **CC‑G4‑13**      | When `G.4:Ext.NQD` is present, `CAL.NQD[]` is present and is wired only via the declared subject pattern (`C.18`): at minimum it pins `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `InsertionPolicyRef`, and it treats archive/illumination summaries as report‑only unless explicitly promoted by a CAL acceptance clause/policy. |
| **CC‑G4‑14** | CAL does not mint new universal types to encode “strategy/policy”. Strategy is expressed as authored flows + acceptance clauses + policy/task pins (and downstream registry/composition in `G.5`); any specialization is introduced only via `GPatternExtension` wiring blocks or cited subject patterns. |
| **CC‑G4‑15** | Every runtime example keeps the reusable Method, MethodDescription, A.6.1 declaration, each precise performer's A.13 core, independently A.15.1-admitted dated `U.Work`, optional later F.6 assignment-bound attribution, actual bindings and direct participants, local result, and C.2.1 result episteme distinct. Any F.6 relation uses the same obtaining A.13 assignment. A compact account may omit only an unused assignment identifier and no consumed fact; ordinary activity outside `U.Work` does not enter this rule. |
| **CC‑G4‑16** | Each performed acceptance or decision path names its exact local result, applies the relevant result pattern, and states the exact later-use relation. Provenance stays with A.10/G.6, currentness with G.11, assurance with B.3, and decisions with C.11; no universal evaluation-result, work-result, evidence-use, or criterion-participant relation is introduced. |

### G.4:8 - Common Anti-Patterns and How to Avoid Them

* **Hidden thresholds.**
  Avoid: embedding cutoffs in CHR prose or in operator descriptions.
  Prefer: `CAL.AcceptanceClause` with explicit ids and pins.

* **Untyped “score(x)”.**
  Avoid: operators with implicit units and untracked legality assumptions.
  Prefer: explicit CHR‑typed operator signatures + cited legality checks.

* **Silent cross-sense or cross-plane reuse.**
  Avoid: importing expressions with distinct source-local meanings, or values across ReferencePlanes or editions, without the obtaining relation and required crossing records.
  Prefer: cite the exact F.17 cells and F.9 relation when meanings differ, cite the applicable plane or edition crossing records, and keep each clause bounded by its stated `ClaimScope` and window.

* **Acceptance as implementation detail.**
  Avoid: acceptance embedded in tool logic.
  Prefer: publish acceptance as citable CAL artifacts; downstream consumes ids.

* **Exploratory telemetry treated as dominance.**
  Avoid: letting probe/illumination telemetry quietly become a dispatch criterion.
  Prefer: keep it report‑only unless an explicit policy‑bound acceptance clause authorizes promotion.

* **Declaration mistaken for execution.**
  Avoid: treating a CAL card, `TaskMap`, proof-ledger row, worked example, or evidence edge as proof that an operator ran or a verdict obtained.
  Prefer: recover every precise performer's A.13 core, let A.15.1 independently admit the dated Work, and add F.6 only when exact assignment-bound attribution through the same obtaining assignment is current; recover actual direct bindings separately. Compact wording may omit only an unused assignment identifier and no consumed fact. Keep the domain-local result and any result episteme separate from both.

### G.4:9 - Consequences

* CAL operator/acceptance semantics become stable, citable CAL Pack content rather than tacit code behavior.
* Legality failures are surfaced as authoring defects (RSCR‑testable) rather than run‑time surprises.
* Downstream patterns (`G.5`, `G.8`, `G.9`, `G.10`, `G.11`) can reference stable ids/pins without redefining acceptance or operator semantics.
* Method pluralism is supported: multiple calculi can coexist as separate operator/flow/acceptance families, wired via Extensions rather than mixed into the core kit.

### G.4:10 - Rationale

CAL sits at the boundary where typed measurement becomes actionable choice. Publishing typed and testable CAL declarations reduces semantic drift and prevents “shadow legality gates” from emerging in tools or in downstream prose.

The design separates concerns:

* CHR governs measurement typing and legality guard macros,
* CG‑Spec and CN‑Spec govern the legality gate and governance card, respectively,
* `G.Core` governs Part‑G invariants and trigger/default discipline,
* `G.4` governs the CAL kit: authoring objects, publication surface, and handoff manifest.

This yields modularity (one governing definition per invariant or default), auditability (pins/ids and proof refs), and extensibility (method families attach through explicit extension modules).

### G.4:11 - SoTA-Echoing

The qualification period for the source-use decisions below starts on 2026-07-30. The source identities below are immutable publications; the G.4 adoption decisions remain qualified through 2027-07-30 unless a governing neighbour adopts a successor earlier or a new result contradicts the named assumption boundary.

| Exact source and source-use decision | Visible G.4 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| Angelopoulos, Bates, Fisch, Lei, and Schuster, [*Conformal Risk Control*, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f3549ef9b5ff520a7e41ff3cc306ab2b-Abstract-Conference.html) — **adapt** bounded monotone-loss risk control only for a CAL clause whose statistical assumptions are explicit. | C3 and `CC-G4-04` require loss, risk/coverage target, calibration population/window, exchangeability or declared shift treatment, and failure/abstain behavior before such a clause is published. Only an actual application under §4.4a supplies the required binding and verdict. | “Conformal”, a calibration set, or a coverage target does not make a universal acceptance guarantee, authorize deployment, or establish that evaluation occurred. | Reopen only C3, `CC-G4-04`, and the one worked clause/test that claims this guarantee when its assumptions or guarantee change. |
| Fontaine, Togelius, Nikolaidis, and Hoover, [*Covariance Matrix Adaptation for the Rapid Illumination of Behavior Space*, GECCO 2020](https://doi.org/10.1145/3377930.3390232) — **adapt** only the need to pin descriptor, distance, insertion, archive, and reporting policy when `G.4:Ext.NQD` is actually used. | C6, `G.4:Ext.NQD`, and `CC-G4-13` keep QD method semantics in C.18 while making the CAL wiring reproducible. | Archive occupancy, coverage, QD-score, or the presence of CMA-ME wiring is not dominance, acceptance, selection, or a runtime result. | Reopen only C6, `G.4:Ext.NQD`, `CC-G4-13`, and its one NQD example/test if the adopted descriptor/archive contract changes. |
| Wang et al., [*Enhanced POET: Open-ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions*, ICML/PMLR 119 (2020)](https://proceedings.mlr.press/v119/wang20l.html) — **reject as a source of G.4 core or acceptance semantics**; retain it only as an exact lineage reference for optional exploration wiring under the applicable pattern. | C6 and `CC-G4-11` require an exact current pattern and present-task entry and stop condition before any exploration extension is admitted; no POET-specific rule enters the CAL core. | Open-ended generation, transfer, or progress telemetry does not become a CAL acceptance rule, task authority, or selected governor by citation. | Reopen only C6, `CC-G4-11`, and the exact C.19/C.23 extension block if the applicable pattern explicitly adopts a changed POET-family rule set. |

Distributionally robust and broad multi-objective families are discovery leads, not G.4 decision sources. Current comparison, partial-order, and selected-set law stays with A.18/A.19; a future external source enters this table only after it changes a present C1–C9 action, worked case, or conformance row. Source refresh is local to the row's named rule, example, and check.

#### G.4:11.1 - CAL architecture and publication inventory

G.4 is a design-time authoring pattern. It publishes a notation-independent `CAL Pack@CG-Frame` with a charter for the exact CG frame, EntityOfConcern, ReferencePlane, specification editions, and assumption envelope; stable operator, clause, and flow ids; evidence and currentness refs; proof-or-gap records; worked examples and tests; continuity notes; and a minimal `TaskMap`. It uses G.Core, G.0, and G.1–G.3 for Part-G, CG-frame, SoTA, CHR, and legality disciplines; A.6.1 for declarations and actual bindings; A.13 and A.15.1 for precise performers and independently admitted runtime Work; F.6 only for a current assignment-bound attribution through the same obtaining assignment; C.2.1 for result epistemes; and A.10, G.11, B.3, and C.11 for provenance, currentness, assurance, and decisions. G.6 is used only when `G.4:Ext.EvidenceGraphWiring` is present. Method-specific semantics remain in the applicable extension pattern. The detailed manifests, schemas, and interfaces above are citation surfaces for CAL authors and consumers within this one practitioner path, not a second workflow.

### G.4:12 - Relations

**Builds on:** `G.Core` (and the pattern template discipline in `E.8`).

**Uses:** `G.1` (CG‑Frame Card), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.0` (CG‑Spec legality gate), `A.19` (CN‑Spec plus direct comparison and selection patterns), `A.18` (CSLC), `A.2.6` (`U.ClaimScope`), `A.6.1` (declarations and actual bindings), `A.13` (precise performer core), `A.15.1` (independent Work admission), `A.2.1` (assignment species and occurrences), and `F.6` only for exact assignment-bound attribution through the same obtaining assignment, `C.2.1` (result epistemes), `C.11` (decision results), `A.10` (provenance and bounded reliance), `B.3` (assurance), `G.11` (currentness), and `E.18` (transformation-flow structure and GateCrossing), `A.21` (gate decisions from independent check results), `F.9` (actual relations between source-local meanings), `F.17` (SchemeSenseCells), and `E.17` (multi-view publication).

**Uses (via Extensions):** `G.6` (EvidenceGraph/Path citation; when `G.4:Ext.EvidenceGraphWiring` is present), `C.18` (NQD), `C.19` (E/E‑LOG), `C.23` (SoS‑LOG).

**Used by:** `G.5` (selector/dispatcher), `G.8` (SoS‑LOG bundles), `G.9` (parity), `G.10` (shipping), `G.11` (refresh orchestration).
**Publishes to:** UTS (public ids and public-id continuity records), RSCR (tests and trigger emissions), `G.5` (handoff manifest), and, as cited payload, shipped packs governed by `G.10`.

**Constrains:** any run‑time LOG implementation that executes CAL operators/flows must treat CAL artifacts as citable specifications and must not re‑invent acceptance semantics.

### G.4:End

## G.5 - Method-Family Registry, Dispatch and Selected-Set Result Declaration

> **Type:** General (G)
> **Status:** Stable
> **Normativity:** Normative

**Intent.** Help an engineer use a dispatcher and registry for rival method families and state selector-facing set outcomes. The outcome distinction covers retained alternatives and members jointly included for one named use without collapsing plurality into one hidden scalar winner.

**Primary working reader and object.** An engineer or framework author who already has a set of identified candidates or members and must state the selector-facing result—outcome kind, members, ordering, named use when required, and basis pins—for a named downstream use, without also claiming a choice, Work, or publication occurrence that has not happened.

### G.5:0 - Use this when
When loop-engineering work retains several already identified candidates for downstream use—for example, loop candidates, harness variants, method families, workflow-store entries, or DPF framework candidates—or when several already identified values are all included for one named use, use `G.5` only when the live claim is the selector-facing declaration of that set result. The declared result states the outcome kind, members or keyed member entries, ordering status, named use when applicable, and basis pins. It does not prove that any member improved, that work occurred, that a local choice has been made, or that the result is available to an audience.

Use `Shortlist` or `RankedShortlist` for alternatives retained for later choice. Use `JointUseSet` only when every named member is included for one bounded use. This joint-use branch consumes exact member identities under their own rules; it does not require `MethodRef`, a method-family registry row, or Method classification for framework editions or other non-Method values.

When an earlier choice or other current inclusion basis has already fixed the exact members, use `G.5-6 DeclareSetResult` with those member refs, the named use, inclusion conditions, ordering, and sufficient basis pins. This branch declares selector-facing result content without running method-family registration or `G.5-3 Select`; non-Method members never enter those method-family operations.

For ordinary method-family dispatch, open `G.5` when two or more already admitted Methods are live under grounded selector rows for the same declared task and the current question is the selector-facing set result: which candidates remain admissible, whether the emitted result may truthfully order them, or whether it must be a shortlist, narrowed handoff, abstain, or escalation. If the live question is still one local choice among available options, first constitute the exact C.11 choice assertion under its predicate. Reuse already grounded method-family rows when they exist; do not rebuild a registry on every run. Create a new reusable row only when the grouping itself must recur, carry family-level policy, be versioned, or be published. Crossing, evidence/reliance, assurance, stable public identity, and actual publication are conditional branches, not an entry fee.


For Method dispatch, resolve each exact A.3.1 Method and the row's independent grouping basis under S1 (§4.2). An unresolved member or grouping basis blocks that row. If the claim concerns actual selection, use S3's application and Work-admission conditions; a result declaration alone supplies no such occurrence. S5 governs any separately needed result episteme, public identity and publication claim.

Typical selector situations include:

- Methods or generators from several families are admissible for the same declared task family or work target
- you need one selector to return a `Shortlist`, `RankedShortlist`, `JointUseSet`, one `SpecialistHandoff`, one other narrowed handoff plan, or one abstain outcome without pretending that there is always one scalar winner or that all set results are alternatives
- the declared result must carry enough basis pins for its named downstream use—for example, later comparison, handoff, or escalation—without changing its declared outcome kind or any applicable public selected-set label

#### G.5:0.1 - What goes wrong if missed

- rival families are compared under silent comparator drift, hidden baseline changes, or unspoken crossing costs
- the selector hides one dogmatic winner even when only a partial order is admissible
- selector-facing result content stays hidden inside `C.11`, `C.19`, or `C.24`, so the G.5 result no longer states which upstream choice, pool treatment, or enactment result it consumes and what set result it declares
- exploration, open-ended, or specialization pressure leaks in as one architecture convenience rather than one explicit policy-bound choice

#### G.5:0.2 - What this buys

- one registry that keeps rival method families disjoint but dispatchable
- one selector result form that uses the closed `SelectorOutcomeKind` rules in §4.4b and the closed `SetResultFamily` set when the result is set-shaped
- one trace addressable by DRR and SCR records with explicit basis pins instead of one hidden selector rationale
- one explicit selected-set result that states the outcome kind, applicable public label, retained members or keyed joint-use entries, ordering, named use where required, handoff content, and basis pins instead of leaving them implicit upstream

Registry and dispatch remain the primary selector question here; the explicit selected-set result closes that question without replacing registry or dispatch.

#### G.5:0.3 - First-minute questions

- Which exact members and grouping or inclusion basis are already established?
- Are they alternatives for later choice or members all included for one named use?
- Does the declared comparison justify ordering them?
- Which eligibility, evidence or other receiving-use conditions actually apply?
- What result can be handed over, and what prevents a complete result?
- Does the current question additionally claim actual selection, composition, a relation between meanings, public identity or publication? Open only the applicable branch in §4.2.

#### G.5:0.4 - First output

State one `SelectorOutcome` under §4.4b: its kind, applicable members or keyed entries, ordering, named use and inclusion conditions where required, handoff or blocking content, and sufficient basis pins. Use the quick card in §4.4c. For an ordinary result over grounded rows, direct refs to the grouping, eligibility and comparison basis plus the S3 audit refs suffice; the same compact record can carry them.

A prior C.11 choice, C.19 pool-policy result, C.24 next action or another governed inclusion basis can supply the inputs. G.5 states the resulting membership or handoff. Exact framework editions retain their own identities and use `G.5-6 DeclareSetResult`; E.4.PFR governs their dependency or compatibility claims. Add a stable public identity only when needed. For audience availability, use E.17's source-backed face and E.24.PUB's publication conditions through S5.

#### G.5:0.5 - Minimum ordinary slice and bounded non-use

**Situation.** A pump-maintenance team has two already admitted A.3.1 Methods, `ThresholdTrendReviewMethod-E2` and `SpectralResidualReviewMethod-E1`, behind the exact project-local selector rows `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>`. These are `MethodFamilyRowRef` values: each fixes its row edition, exact `MethodRef[]`, and declared grouping basis `PumpTriageCandidateGrouping-E1`. The same `TaskSignatureRef=PumpVibrationTriage-T1` and effective reference scheme apply to both. The task signature requires a 24-hour series input and a 30-minute review budget, and both declared Method interfaces meet those constraints. No G.4 CAL gate is current in this ordinary case, so `TaskMapRef` is absent. No admitted comparator justifies ordering one above the other. The live `G.5` question is now how to surface that admissible set, not which pump action a decision-maker should choose.


The minimum truthful result is:

```text
GroundedCandidateRows = [
  { methodFamilyRowRef = <ThresholdTrendReview-local, R3>,
    MethodRef = [ThresholdTrendReviewMethod-E2],
    groupingBasis = PumpTriageCandidateGrouping-E1 },
  { methodFamilyRowRef = <SpectralResidualReview-local, R2>,
    MethodRef = [SpectralResidualReviewMethod-E1],
    groupingBasis = PumpTriageCandidateGrouping-E1 }
]

SelectorOutcome(

  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [<ThresholdTrendReview-local, R3>, <SpectralResidualReview-local, R2>],
  ordering = unordered,
  basisPins = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>,
               PumpTriageEligibility-E1],
  auditRefs = [DRR-PumpTriage-01, SCR-PumpTriage-01],

  nextUse = maintenance_method_handoff

)
```

**What changes in practice.** The team stops leaving the retained pair implicit in a comparison note and stops saying “the spectral method is best.” It emits one unordered `Shortlist` that another receiver can cite, with the exact survivors and basis visible, while making no local-choice, actual-use, or winning-method claim. A later receiver can request one missing comparator, use the bounded handoff, or open its separately governed decision question without rewriting either Method or inventing a winner.


**Near misses and non-use.** Do not use `G.5` merely because several names appear in one list.

- If the Method-dispatch candidates are only labels, descriptions, cards, or unresolved references, require A.3.1 and C.2.1 before dispatch.
- If the current question is one local choice among already available options, use `C.11`; if it is the policy for retaining or retiring live candidate lines, use `C.19`; if it is enactment planning after choice, use `C.24` for the plan and the applicable A.15/A.6 patterns for actual Work and operation applications.
- If the current object is only a composition sketch, keep the S4 template; use B.1.5 only for a qualified composite Method and A.22 only for an independently selected Structure.
- If no rival candidate set, selector result, narrowed handoff, abstain, or escalation is current, do not open `G.5`.
- Open F.9, A.10, B.3, stable registry or UTS identity, and E.24.PUB only for an actual crossing, relied-on evidence, assurance claim, reusable identity, or audience-availability claim respectively; their absence does not invalidate the smaller same-scheme selector result.

#### G.5:0.6 - Reuse a local grouping, then register it publicly when needed

The pump team in §0.5 already dispatches through R3 and R2. That unordered shortlist requires no new row. If the grouping of both Methods must recur across triage runs, the team can define:

```text
MethodFamilyRowRef = <PumpReviewCandidates-local, R1>
MethodRef[] = [ThresholdTrendReviewMethod-E2, SpectralResidualReviewMethod-E1]
GroupingBasis = PumpTriageCandidateGrouping-E1
EligibilityBasis = PumpTriageEligibility-E1
TaskSignatureRef = PumpVibrationTriage-T1
ComparisonBasis = no admitted ordering; retain admissible alternatives unordered
```

The grouping criterion is “these admitted review Methods are candidates for pump vibration triage using the stated 24-hour input and 30-minute budget.” This project-local row fixes those exact members and basis; changed membership or an action-changing policy makes R2. It requires neither a UTS row nor an AssuranceProfile when this ordinary use has no assurance gate. A later real gate still consumes its required evidence and follows its unknown/fail behavior.

If the team instead intends a stable public registry entry, its proposed public continuation can be `<PumpReviewCandidates, P1>`, linked by an explicit naming/continuity mapping to the local R1 grouping. P1 retains the same exact Method refs and grouping criterion, adds the typed `EligibilityStandardRef` for the pump task and an `AssuranceProfileRef` stating expectations for its declared uses, and satisfies UTS naming/publication requirements under S1 and CC-G5.6. Registration is complete only when those public-contract obligations are met. For this P1 example, `PumpTriageEligibilityStandard-E1` states the two Methods' required 24-hour series and 30-minute budget, with unknown when a required input cannot be determined. `PumpTriageAssuranceProfile-E1` names the evidence expectations and failure behavior for the declared triage uses; `UTS-PumpReviewCandidates-P1` supplies the public name and continuity mapping to R1. P1 registration consumes these completed declarations and that UTS entry alongside the unchanged exact member/grouping basis. A missing one leaves public registration incomplete. The assurance profile supplies no B.3 result.

R1 itself completes through RegisterFamily with the six values shown above: neither AuthoringBase nor AuthoringMinimal is activated because this local grouping has no CG-Frame use. P1 adds the three public references just described and activates UTSWhenPublicIdsMinted. Now suppose a later G.5-3 Select use is governed by `PumpTriage-CG-E1`, whose MinimalEvidence clause requires a valid sensor calibration for the cited vibration series. Its CN/CG editions and frame pins are required. If the calibration input is missing, the evidence predicate is unknown and this example's gate rule returns abstain; neither successful local R1 registration nor completed public P1 registration makes that selection pass.

Making local R1 available to the project audience may itself be an E.24.PUB publication occurrence when that pattern's conditions obtain. Conversely, the intention or declaration of P1 establishes no availability. Neither branch creates a Method or an ontic family relation. Non-Method joint-use members continue through `DeclareSetResult` with their existing identities and inclusion basis.

### G.5:1 - Problem frame


The exact `CG‑Frame` card from **G.1** and `SoTA Synthesis Pack@CG‑Frame` from **G.2** name the frame, `EntityOfConcernRef`, ReferencePlane, source rows, and rival internally coherent **method families** (and sometimes **generator families**) that may address the same declared task. If their breadth is used as a premise, cite G.2's pack `CoverageJudgementRef` and its HarvestPolicy basis. Registration does not recount cards as families; a combined method/generator coverage result does not establish method-only coverage for dispatch.

At the same time, the scale and coordinate definitions from **G.3** and the typed operator-argument and result declarations from **G.4** make admissible calculi and acceptance clauses explicit - enough to formulate *eligibility*, *assurance*, and *admissibility* constraints, but not enough to pick "the method" without collapsing plurality.

You need a **notation‑independent** way to:

1. register method families and generator families as *auditable, versioned* entries,
2. select, compose, or fall back among them at run time for a concrete task instance,
3. declare stable selected-set results, including retained-alternative and all-member results, and publish stable identities to UTS when required, and
4. emit RSCR‑relevant triggers and pins without inventing new “shadow specs”.

### G.5:2 - Problem

How to design a **general, auditable dispatcher** that:

* preserves **pluralism** (families from competing Traditions stay disjoint) while remaining **dispatchable** (selection is possible and explainable);
* does **not embed algorithmic dogma** in the core selector kernel;
* when expressions carry distinct F.17 source-local meanings, requires the complete crossing path—exact local senses, an obtaining F.9 Bridge, a separate bounded-use proposition, and the appropriate reliance or assurance branch—while treating pins as audit references rather than as the crossing facts;

* produces **set-valued outcomes** when only partial orders are admissible or when every named member is included for one bounded use, without confusing those meanings; when exact non-Method members already have a current inclusion basis, it declares that result without routing them through method-family selection;
* cleanly separates:

  * **selector object set and components** (registry, selector boundary, and result-declaration records),
  * **universal Part‑G invariants** (carried by `G.Core`),
  * **method-specific and generator-specific semantics** (carried only through `Extensions` blocks).

### G.5:3 - Forces

* **Pluralism vs. forced totalisation.** Many selection regimes are inherently partial-order; forcing a scalar winner often creates inadmissible semantics.
* **Evidence realism vs. hard gates.** Eligibility and acceptance frequently depend on incomplete evidence; selection must remain auditable under tri-state unknowns.
* **Reuse vs. leakage.** Reuse across distinct source-local meanings remains valuable, but it starts from exact F.17 cells and an obtaining F.9 Bridge, then keeps the proposed use, direction, rule, tolerated loss, reliance or assurance, and actual selector use separate. Bridge, CL, loss, registry, bundle, or policy pins cannot silently re-ground semantics.

* **Exploration vs. exploitation.** Dispatch sometimes must probe alternatives under explicit policy envelopes and risk envelopes, but probing must not become an implicit fourth status.
* **Evolvability vs. churn.** Registries evolve (new families, deprecations, edition bumps); continuity must not be broken by “rename by meaning”.

### G.5:4 - Solution
#### G.5:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (normative; size-controlled via profiles and sets).**
For the operation in use, expand the applicable profile and set ids by union with its explicit deltas (per `G.Core:4.2.1`). The activation conditions below select those ids before expansion; `Nil‑elision` does not waive an activated obligation. `Select` retains its exact task, row editions and DRR/SCR-addressable audit result. `DeclareSetResult` instead consumes its exact result family, identified members, inclusion basis, ordering and named use where required; it acquires no TaskSignature, Method or registry row merely by declaring that set.

Select profile activation before expanding the G.Core sets. RegisterFamily always retains S1's immutable row edition, exact admitted members, grouping criterion and applicable eligibility/comparison basis. A project-local row without a CG-Frame activates neither AuthoringBase nor AuthoringMinimal; it still satisfies those S1 obligations. Intentional public registration adds EligibilityStandardRef, AssuranceProfileRef and UTS obligations even when no CG gate is in use. When a real CG-Frame registry or Select use is current, both authoring sets apply in full; omitting their required CN/CG pins is a failure, not nil-elision.

For crossing-aware selection, `CorePinsRequired` below lists the crossing pins individually. Each conditional pin is mandatory when its stated condition holds. When consuming `G.7` calibration records or a named `B.3` assurance account, retain all pins, editions, and evidence required by that account, including `CC‑G7‑SCRLinkage‑1` for cited calibration evidence.

* `CoreConformanceProfileIds :=`

  * `GCoreConformanceProfileId.PartG.AuthoringBase` *(when the current operation authors a registry in an actually selected CG-Frame or performs G.5-3 Select within that frame)*
  * `GCoreConformanceProfileId.PartG.TriStateGuard` *(when evaluating eligibility or acceptance predicates)*
  * `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted` *(when public identities are minted or evolved, including intentional public registration under S1/S1′ and CC-G5.6; a reusable project-local row alone does not activate this profile)*
  * `GCoreConformanceProfileId.PartG.ShippingBoundary` *(when an output is shipped)*
* `CorePinSetIds :=`

  * `GCorePinSetId.PartG.AuthoringMinimal` *(for the same actual CG-Frame registry-authoring or G.5-3 Select use; local registration or a set declaration alone does not activate it)*
* `CorePinsRequired :=` *(delta over PinSets; pins and refs are id-only; prefer strengthening optional-to-required over restating pins already covered by PinSets)*

  * `TaskSignatureRef` *(the C.22 TaskSignature edition for `Select`; see `G.5:4.2`, S2)*
  * `TaskMapRef?` *(exact G.4 map edition, only when this selection uses G.4 CAL gates)*
  * `MethodFamilyRowRef[]` *(exact `<MethodFamilyId, rowEdition>` values when method-family rows are consumed or registered)*
  * `MethodRef[]` *(exact A.3.1 Methods resolved from every method-bearing registry row consumed or registered)*
  * `SelectedStructureRef[]?` *(exact independently selected A.22 Structures consumed only when their organization changes this selector use)*

  * `GeneratorFamilyRowRef[]?` *(exact `<GeneratorFamilyId, rowEdition>` values when generator families are in scope)*
  * `PathId[]?`, `PathSliceId[]?` *(when audit or evidence citations use a G.6 graph, or an independently applicable gate or shipping contract requires those citations)*
  * `UTSRowId[]?` *(when the operation mints, evolves or consumes a public identity; intentional public registration activates S1/S1′ and CC-G5.6 obligations)*
  * `FailureBehaviorPolicyId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `SoSLogBranchId?` *(only when degrade or abstain behavior is explicitly policy‑bound)*
  * `BridgeId/BridgeCardId?` *(the obtaining Bridge actually used by this selection; a Bridge Card is cited only when that Card is relied on)*
  * `BridgeMatrixId?` *(when this selection uses a BridgeMatrix)*
  * `CL/CL^k/CL^plane?` *(the applicable values when cited or required by the consumed calibration or named assurance account)*
  * `Φ/Ψ/Φ_plane policy-ids?` *(the applicable policy ids and editions when required by the consumed calibration or named assurance account, or when crossing or plane penalties are applied)*
  * `CrossingBundleId?` *(when the selector cites a CrossingBundle or its named downstream use requires one under `E.18` or `CC‑G5.27`)*
* `DefaultsConsumed :=`

  * `DefaultId.GammaFoldForR_eff`
  * `DefaultId.PortfolioMode`
  * `DefaultId.DominanceRegime`
* `RSCRTriggerSetIds :=`

  * `GCoreTriggerSetId.RefreshOrchestration`
    *(payload: exact changed source and affected-use scope; `SCRId`, `DRRId`; `TaskSignatureRef`, `MethodFamilyRowRef[]`, `CGSpecRef.edition` and `CNSpecRef.edition` for a `Select` result; and the actually applicable `TaskMapRef?`, `GeneratorFamilyRowRef[]?`, `AcceptanceClauseId[]?`, `SoSLogBranchId?`, `FailureBehaviorPolicyId?`, `DescriptorMapRef.edition?`, `DistanceDefRef.edition?`, `TransferRulesRef.edition?`, `InsertionPolicyRef?`, `PathId[]?`, `PathSliceId[]?`, `RSCRTestId[]?`. Nongraph scope uses the existing G.Core `PatternScopeId` branch.)*

#### G.5:4.2 - Dispatcher and Registry object set (notation‑independent)

G.5 defines the **object-set components** below. Their purpose is to make dispatch **possible and auditable** without embedding any method-family semantics in the selector kernel.

**S1 — `MethodFamily Registry` (design-time; project-local or within a selected CG-Frame).**
A reusable row represents one declared grouping. Choose its registry-identity contract: project-local reuse, or intentional registration under a stable public registry identity. This distinction concerns the identity contract, not who can see the row. Both branches fix these replayable values:

* `Identity and continuity`: `MethodFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `MethodFamilyRowRef := <MethodFamilyId, rowEdition>` designates that edition. Lineage and Tradition notes and `UTSRowId` remain descriptive or publication values.
* `Exact method members`: non-empty `MethodRef[]`, each resolving to one `U.Method` already admitted under A.3.1.
* `Grouping basis`: exact claim, criterion, or direct relation reference that justifies this row's grouping for the current selector use; if no ontic family or membership relation is directly governed, the basis is explicitly project-local and creates none.

One exact row edition fixes its method members, grouping basis, and every selection-changing pin. Changing any of those values creates a new `rowEdition`; retain the `MethodFamilyId` only while the declared grouping remains the same continuing row lineage. Old `MethodFamilyRowRef` values continue to resolve their old editions. Add task, eligibility, policy, scheme, source, `ClaimScope`, validity, or intended-use pins only when they change selection or a named receiver needs them; none replaces the members or grouping basis.

* `Eligibility and comparison basis`: the actual rule and applicable editions used for this selection, including whether any comparison justifies ordering. A local row may cite its existing project rule; it need not manufacture a public eligibility artifact.
* `Assurance expectations`, only when the local use requires them, with the applicable evidence, unknown and failure rules. A real assurance or minimal-evidence gate keeps every input required by its governing clause.

**Public-registry continuation.** Intentional registration under a stable public identity additionally requires `EligibilityStandardRef` as a typed predicate record (tri-state per G.Core, using CHR/CAL terms and applicable edition pins), `AssuranceProfileRef` for declared evidence-lane expectations and assurance-lane pins, and the UTS naming/continuity obligations of CC-G5.6. The AssuranceProfile states expectations; it is not a B.3 assurance result. The public contract retains the same immutable members and grouping basis. The remaining fields below apply when their subject conditions hold in either branch.
* `AdmissibilityBindings`: when the row is authored for an actual CG-Frame or consumed by its gate, cite its single governance card and gate (`CNSpecRef`, `CGSpecRef`) and every required admissibility constraint, such as scale/unit conditions for a measurement use. An ordinary local grouping with no such use adds no CN/CG reference.
* `EvidencePins`: the source and evidence citations supporting asserted claims or guarantees. Cite `G.6` `PathId` or `PathSliceId` values when that support is represented in a graph or an independently applicable receiving contract requires those citations.
* `CrossingAllowance`: references to the exact F.17 endpoint senses, one obtaining F.9 Bridge, the separate C.2.1 bounded-use proposition, and the current A.10 or B.3 reliance basis, plus CL or observed-loss evidence when material, **only** when expressions with distinct recovered source-local meanings are actually related for this selector use. These are audit references; the field makes none of the referenced facts obtain.

For an actual crossing, first resolve both exact F.17 `SchemeSenseCell` endpoints and establish the two-participant F.9 Bridge under its own predicate profile. Then identify a separate C.2.1 episteme whose exact `EntityOfConcern` is that Bridge and whose ClaimGraph states the proposed use `u`, direction `d`, use-specific rule `r`, tolerated loss `t`, and polarity. For ordinary reliance require the matching current A.10 evidence-provenance path and local `RelianceDisposition`; when an actual named assurance claim is current, use B.3's separate assurance branch. A consequential use without one retains its direct governing rule. Observed loss and CL are evidence, defeater or assurance-policy material, not Bridge participants or permission. Authorization and the actual `Select` application remain with their subject patterns. A Bridge id, `CrossingAllowance`, registry row, policy pin, `CrossingBundle`, DRR or SCR entry cannot substitute for any step.

* `PolicyHooksRef?`: optional pointers to policy records (not defined here; wired via Extensions).

Here “a registry row represents a family” means that the row is the auditable selector-facing record for one declared grouping. The family id preserves that row lineage; the row ref selects one immutable edition for replay. Neither value identifies the grouped Methods, makes a membership relation obtain, or turns a common label, shared description, lineage note, eligibility rule, maturity card, evidence record, or policy into a method-family fact. Changing a row edition changes the registry artifact; it changes a Method or a separate family relation only when that object's direct identity rule or the relation's predicate independently says so.


**S1′ — `GeneratorFamily Registry` (design‑time; optional; per CG‑Frame).**
A reusable row groups generators of tasks and environments, which may co-evolve solver families. It uses the same local/public identity-contract distinction as S1 while retaining its own generator member and signature rules:

* `Identity and continuity`: `GeneratorFamilyId` names the continuing row lineage; `rowEdition` names one immutable edition; `GeneratorFamilyRowRef := <GeneratorFamilyId, rowEdition>` designates that edition. `UTSRowId` is required by intentional public registration; project-local reuse does not require it.
* `Exact generator members`: non-empty references, each resolving to a generator already identified under its subject pattern.
* `Grouping basis`: the independently established classification, membership relation, or explicit project-local criterion that groups those generators for this selector.
* `GeneratorSignatureRef`: conceptual input and output semantics plus budget semantics.
* `EnvironmentValidityRegionRef?`: pinned constraints for generated environments or tasks.
* `TransferRulesRef.edition?`: required when the Open-Ended mode is enabled (semantics come from the cited extension refs).
* `CouplerRefs?`: exact `MethodFamilyRowRef[]` values that may be coupled with this generator-row edition.

Both branches also fix the applicable eligibility/comparison basis and every selection-changing source or policy pin; assurance expectations are conditional on the use. Changing generator members, grouping basis, or another selection-changing pin creates a new generator `rowEdition`; old `GeneratorFamilyRowRef` values continue to resolve their old editions. Intentional public registration activates CC-G5.6 naming, continuity and UTS obligations, with the applicable generator signature and use contracts. It does not import A.3.1 Method membership into generator rows.

**S2 — C.22 `TaskSignature` input and conditional G.4 map.**
C.22 constitutes the `TaskSignature` episteme and defines its edition rule. G.5 consumes its `TaskSignatureRef` and does not reconstruct it from a task, CAL pack, or map. Its function here is pinning and auditability, not over-specification.

When this selector actually uses G.4 CAL gates, it also consumes one exact `TaskMapRef`. Resolve that immutable map edition, require its `taskSignatureRef` to equal the C.22 `TaskSignatureRef` supplied to this selector, and follow its exact `CALCharterRef` and edition-bearing clause, operator, flow, and evidence-profile refs. The map supplies no TaskSignature field and no threshold value. If no G.4 gate is current, omit `TaskMapRef`; an ordinary selector does not need a CAL pack merely to return a truthful bounded result.

For the G.4 safety example, G.5 receives `TaskSignatureRef=SafetyPortfolioTaskSignature-E4` and `TaskMapRef=<SafetySelectionMap, E3>`. The map resolves `CALCharterRef=<SafetyCALCharter, E2>` and the cited gate declarations. A different signature ref or an unresolved charter or component blocks only that gated selector use.

**S3 — `Selection kernel boundary` (run‑time; policy‑governed).**
A notation‑independent selector that:

* consumes `TaskSignatureRef`, exact method- or generator-family row refs, pinned spec refs, and an exact matching `TaskMapRef` only when G.4 CAL gates are current,
* applies the declared eligibility conditions and any assurance gates actually required for this use (tri-state),
* computes an admissible (possibly partial) order,
* returns one declared selector outcome over the exact Method candidates admitted through this kernel: most often `Shortlist` or `RankedShortlist`, and `JointUseSet` only when every returned Method candidate is included for one named use; otherwise it returns one `SpecialistHandoff`, one other narrowed handoff, one abstain outcome, or one escalation outcome (per `DefaultId.PortfolioMode` and explicit overrides),
* emits audit records with pins addressable by DRR and SCR records.

When `TaskMapRef` is present, resolve its exact immutable G.4 map edition before applying any cited gate. Its `taskSignatureRef` must match this selector's C.22 `TaskSignatureRef`; its `CALCharterRef` must recover the CG frame, EntityOfConcern, ReferencePlane, specification editions, and assumption envelope; and each cited clause, operator, flow, and evidence profile must resolve at its exact edition. Carry the exact map ref among the result basis and refresh pins. Do not copy thresholds or acceptance semantics into G.5.

If a cited gate consumes R, resolve the quantity and support model under `CC‑G5.4` before evaluating its threshold. Keep formal and empirical inputs, required premises, complementary support, dependence, scope, and counterevidence distinguishable. No common model means no invented aggregate: retain a qualified synthesis, and apply the clause's unknown behavior only where that missing quantity is actually required. The ordinary selector result in §0.4 is not an assurance claim and needs no new R calculation.

For every `MethodFamilyRowRef` consumed here, resolve the exact immutable row edition and then its A.3.1 `MethodRef[]`, grouping basis, and selection-changing pins before admitting the candidate. Apply the same rule to `GeneratorFamilyRowRef`. The selector may compare or return exact row refs as auditable selector-facing addresses, but row selection neither creates its members nor proves that every listed member belongs, is admissible, is selected, or will be enacted. An unresolved Method reference or missing grouping basis blocks that row's method-bearing use; it is not repaired by a label, description, UTS identity, policy, or evidence pin.

When a selector consumes an organization among Methods, cite an exact `SelectedStructureRef` only after A.22 has independently identified the `U.Structure` from exact constituents, exact already-obtaining relation occurrences, applied constraints, and one named use frame. G.5 neither supplies those discriminators nor selects the Structure by listing it. If the organization instead constitutes one composite Method, consume the exact A.3.1 Method only after B.1.5 has qualified that candidate from its independent parts and whole-forming basis.

S3 states reusable selector behavior. It does not itself perform selection. For an actual selector use, first recover every precise performer's A.13 core for the exact selection action, scope, working situation, and window, including the same obtaining assignment later used by any exact attribution. A.15.1 then independently admits the dated selector Work from its exact performance history, enacted Method, temporal extent, and containing-System relation. State the actual A.6.1 `Select` application, its effective argument bindings, and the A.19 `SelectionSlot` binding for any selected set returned by value. Add F.6 afterward only when the receiving claim needs exact assignment-bound attribution through the same obtaining A.13 assignment. The declaration, planned pins, registry rows, policy, assignment, F.6 relation, and `CandidateSet` type create none of the A.13, Work-admission, application, or result facts.

A compact selector account may omit only an assignment identifier unused by its receiving claim; it omits no criterion, classification, assignment, Work-admission, or attribution fact that the claim consumes. A root-family reference, the same holder, overlapping times, or silence in the receiving text establishes or removes neither the assignment nor F.6 attribution. Ordinary selector discussion not admitted as `U.Work` does not enter this branch.

In this actual-selector branch, the independently admitted dated selector Work and its actual Select application are required. Replay the upstream CPM applications through their own declaration-local bindings; separately admitted comparison Work is required only if the account asserts it. Evidence use, A.10 reliance/provenance, G.11 currentness and a C.2.1 result episteme retain their complete independent grounds when asserted or consumed by the receiving use. A bounded selection that consumes none of these additional claims requires no such additional object.

**S3.A — `TaskFamilySpecializationProfile@Context` (run‑time; conditional).**
When the real selector question is acquisition of usable specialization on a declared task family, the selector may emit one `TaskFamilySpecializationProfile@Context` for each candidate, one `SpecialistHandoff`, or one narrowed handoff plan. Here `profile` means one selector-time comparison record for bounded specialization, not a new U-kind and not a generic narrative profile. `G.5` carries this selector-time specialization question here; it does not redefine the adaptation-signature field vocabulary from `C.22.1`.

The profile should therefore cite one `AdaptationSignatureRef` or equivalent pinned field set carrying the declared `TaskFamilyRef` or `TaskSignature`, the work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, any declared transfer or retention claim, any downside cost or downside on adjacent tasks, and any specialization-entry baseline, specialization-entry evidence, or stepping-stone evidence item that materially affects comparison.

Admission rule for `SpecialistHandoff`: use that handoff kind only when the truthful declared result is one heterogeneous handoff bundle whose members occupy different specialization positions that still need to travel together. Do not use it when a `SetResultOutcome` with `Shortlist`, `RankedShortlist`, or `JointUseSet`, or a `HandoffOutcome` with another admitted handoff kind, already states the result more precisely.

When the declared task family is heterogeneous, the selector may return one `SpecialistHandoff`, one other narrowed handoff plan, or one `SetResultOutcome` with an admitted `SetResultFamily` that preserves rival specialists rather than collapsing them into a fake single winner. Low-human-overlap candidates remain admissible only when the profile, evidence basis, and policy constraints are explicit.

**S4 — `Composition and fallbacks` templates (design‑time).**
A library of composition shapes—`preconditioner -> solver -> verifier`, cascades, and meta-selectors—remains available **as design-time templates**, admissibility-checked and pinned. A template is a description or policy-bound arrangement for possible composition; its existence, diagram order, registry placement, or selection does not create a Method, `methodPartOf` occurrence, obtaining relation, or selected Structure.

If exact A.3.1 Methods, exact B.1.5 `methodPartOf` occurrences, all other required whole-forming claims and constraints, whole semantics, interface boundary, and reidentification rule qualify one already identified candidate as a composite `U.Method`, consume that exact Method through the B.1.5 branch. If independently identified Methods and already-obtaining relations are instead organized for one use without constituting one Method, consume an independently selected A.22 `U.Structure` only after its exact constituents, selected obtaining relation occurrences, applied constraints, and named selection-use frame are present. `MethodRelationStructure` may remain a local readable designator for that actually selected Structure; it is not a U-kind, relation kind, Method holon, registry-row identity, or generic `@BoundedContext` object.

A C.2.1 episteme may describe either governed object. A.3.2 applies only when the episteme's exact `EntityOfConcern` is one already admitted Method and its claims substantively describe that Method; an episteme whose exact concern is the selected Structure is not thereby a `U.MethodDescription`. Concrete strategy semantics stay in the referenced method families; G.5 only carries the composition template, selector relation, registry row, exact consumed Method or Structure reference, or selected-set result. None of those G.5 artifacts supplies the B.1.5 or A.22 construction facts.

Algebraic, graph, matrix, embedding, or neural selector notation remains a mathematical or representation lens when that representation is current; use C.29 for its correspondence and preserved-or-lost structure rather than reading notation as composition or selection.


**S5 — `Result, public identity, and telemetry` record boundary (run-time).**
Declare the following S5 outputs:

* `DRR` (decision rationale) and `SCR` (evidence and confidence citation) with explicit pins,
* declared selector and selected-set records produced either by method-family `G.5-3 Select` or by the already-grounded-member `G.5-6 DeclareSetResult` branch,
* telemetry pins to refresh orchestration (`G.11`), without governing orchestration.

S5 governs the selector-facing record boundary, not truth or actuality by record existence. A DRR, SCR, selected-set record, shortlist id, telemetry event, refresh cue, policy pin, or result label does not create dated Work, an actual operation application, the selected-set binding, a domain result, an evidence-provenance relation, assurance, authorization, or publication availability. Persist a selector-result claim as its own C.2.1 episteme when another use must rely on it; connect evidence through A.10, assurance through B.3, authorization through its direct governor, and actual availability through E.24.PUB only when each claim has its independently established basis.


Use §4.4b for outcome kinds and §4.4c for conditional public-identity fields.

**S6 — `Governance and evolution` declaration boundary (design-time).**
Versioning, deprecation, and registry evolution discipline (UTS publication; continuity), without minting new Part‑G‑wide types.

#### G.5:4.3 - Selector head and narrower selector families

Selection and dispatch stay one generic selector head. Narrower selector families may refine it, but they do not redefine the universal invariants pinned through `G.Core`, do not add new mandatory inputs to inherited `Select`, and do not mutate inherited SlotKinds. Required policy and edition refs use the declared input meanings.

Method- and generator-specific pressures such as `QD` archives, open-ended declared sets, explore and exploit lenses, or preference comparators do not become part of the selector head. They arrive only through explicit extension declarations and the pins those extensions require.

#### G.5:4.4 - Selector Relation Fields

| Selector relation                 | Consumes                                                                                                                                                     | Produces                                                                                                                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **G.5-1 RegisterFamily** | declared local or public registry-identity contract; continuing MethodFamilyId and new immutable row edition; nonempty exact admitted A.3.1 MethodRef[]; obtaining grouping relation or explicit grouping criterion; eligibility/comparison basis; selection-changing source, policy and CHR/CAL/CN/CG pins as applicable; public-continuation fields when selected | One immutable MethodFamilyRowRef = <MethodFamilyId, rowEdition>, resolving the members, grouping, eligibility/comparison basis and applicable pins. Public registration additionally fixes EligibilityStandardRef, AssuranceProfileRef and UTSRowId under S1/CC-G5.6. A local row retains conditional assurance expectations without requiring a public UTS entry. Neither branch creates Methods or grouping facts. |
| **G.5-2 RegisterGeneratorFamily** | declared local or public registry-identity contract; continuing GeneratorFamilyId and immutable row edition; nonempty exact generator refs under their subject patterns; grouping basis; GeneratorSignatureRef; applicable eligibility/comparison, source and policy pins, including TransferRulesRef.edition when required | One immutable GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>, resolving those members, basis, signature and applicable pins. Intentional public registration additionally meets S1′/CC-G5.6 naming, continuity and UTS requirements. Local reuse retains the same replayable member/basis core; neither branch creates generator identity or membership. |
| **G.5-3 Select**                  | `TaskSignatureRef`; exact matching `TaskMapRef` when G.4 CAL gates are current; exact `MethodFamilyRowRef[]` in scope whose immutable editions resolve to non-empty exact A.3.1 `MethodRef[]` and exact grouping bases; optional exact `GeneratorFamilyRowRef[]`; pinned `CNSpecRef` and `CGSpecRef` editions; policy refs if any; sufficient audit basis refs, with `PathId` or `PathSliceId` only for actual graph citations or an independently applicable gate or shipping contract | `CandidateSet` (set-returning), declared selector result with `PortfolioMode` recorded, exact row refs and any current `TaskMapRef` among the result basis pins, and `DRR` and `SCR` pins; if no admissible candidate exists: return `CandidateSet = EMPTY` plus an escalation hint (`ActionHint`) and the pins required to plan next steps (P2W split applies) |
| **G.5-4 Compose**                 | `CandidateSet`, composition template refs, pinned admissibility constraints                                                                                       | Composite strategy template (template-level; admissibility-checked; pinned)                                                                                                                                                                                      |
| **G.5-5 Telemetry**               | run outcomes, citations, and policy or edition pins                                                                                                               | refresh cues (typed RSCR causes and payload pins), parity deltas (if parity harness is in use), telemetry pins (selector-side; orchestration governing definition is `G.11`)                                                                                              |
| **G.5-6 DeclareSetResult**        | one exact `SetResultFamily`; exact already identified `memberRef[]`; `namedUse` for `JointUseSet`; ordering; inclusion or selection conditions; and sufficient `basisPins` to the already current choice, pool treatment, accepted decision, or other governed inclusion basis | one `SelectorOutcome` with `SelectorOutcomeKind = SetResultOutcome` and the exact membership form required by that family. For `JointUseSet`, it emits keyed unique `memberEntries`, `ordering = unordered`, the named use, inclusion conditions, and basis pins without a method-family row or `Select` pass. |

`RegisterFamily` produces only the local or public registry row selected under S1. It does not produce any A.3.1 Method or independently governed membership fact. `Select` may address candidates through those rows only after their exact Methods and grouping bases resolve; its returned candidate or selected-set value does not retroactively ground a row member.

`Compose` produces only the pinned template named in its output column. It neither qualifies one composite Method under B.1.5 nor selects one A.22 Structure. When a later selector use consumes either governed object, the exact Method or Structure reference is an independently grounded input rather than a result inferred from this template.

`DeclareSetResult` begins only after its exact members and inclusion or selection basis are current. An upstream C.11 `ChoiceResult`, C.19 pool treatment, accepted decision, or another governed basis may appear among `basisPins`; the G.5 branch does not repeat or perform that decision. It declares the selector-facing set-result content and stops. It creates no member identity or relation, method-family row, `Select` application, dated selection Work, persisted C.2.1 result episteme, assurance or authority claim, or E.24.PUB availability occurrence.

#### G.5:4.4a - Worked selector slice

- A catalyst-search team is choosing among three method families for the same declared `TaskSignature` and `C.22.1` adaptation signature.
- The shared profile pins one work-measure threshold target, one freshness window, one prior-exposure declaration, and one adaptation budget. One family reaches threshold quickly but carries high downside on adjacent tasks. One family is slower but transfers cleanly. One family never clears `MinimalEvidence` and must receive an abstain verdict.
- The `G.5` result in this slice therefore declares one unordered `Shortlist` retaining the first two families, with DRR and SCR records citing why the third family was excluded and why the first two remain non-dominated. The selector does not invent one scalar winner and does not hide the specialization profile in auxiliary side notes.
- If the project also claims that this selection actually occurred, A.13 first recovers `CatalystSelectorSystem-17 : U.System` for exact action `CatalystFamilySelectionAction-17`. `CatalystSelectorBoundary-17` contains the deployed selector runtime, its effective policy state, and its registry/evidence interfaces; it excludes the method-family rows, `TaskMap`, result records, assignment, and containing team System. The action applies the effective selector to the three candidate families and returns the retained set. Its scope is `CatalystFamilySelectionClaimScope-17`, its working situation is `CatalystSearchSelectionSituation-17`, and its window is `2026-07-30T10:00:00Z` through `2026-07-30T10:08:00Z`. `CatalystSelectionAdmissibilityNorm-17` directs the selector to exclude candidates that fail `MinimalEvidence`, preserve admissible non-dominated alternatives, and abstain rather than manufacture a scalar winner. Relevant conditions include the exact `CatalystTaskSignature-17`, current row and map editions, eligibility evidence, comparison policy, and adaptation-signature values.
- A.2 declares local agential kind `CatalystMethodSelectorSystemRole`. Its membership criterion requires the stable work-facing contribution of method-family selection and goal-directed, condition-sensitive regulation under `CatalystSelectionAdmissibilityNorm-17`: the holder must apply the current gates, preserve the admissible set-return semantics, and abstain or escalate when no candidate qualifies. `CatalystSelectorDecisionTrace-17` shows `CatalystSelectorSystem-17` excluding the third family for failed `MinimalEvidence`, retaining the first two as non-dominated, and emitting no scalar winner. The trace and boundary/runtime records support the criterion facts under A.2's membership rule; A.10 makes that source-to-use account recoverable. The case independently classifies `CatalystSelectorSystem-17` under `CatalystMethodSelectorSystemRole`; neither the assignment nor the candidate Work supplies the classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed.
- The same A.13 core uses `CatalystSelectorAssignment`, a directly declared species under `U.SystemRoleAssignment`. The species declares holder, assigned-kind, and task-signature participant meanings and the assignment predicate. `CatalystSelectorAssignment-17` obtains with `CatalystSelectorSystem-17`, `CatalystMethodSelectorSystemRole`, and `CatalystTaskSignature-17` as its exact participant values; its maximal uninterrupted predicate-true interval covers the stated scope, situation, and window.
- Only after that core is established does A.15.1 independently admit `CatalystSelectionWork-17 : U.Work` from the exact selection-action history, enacted `CatalystFamilySelectionMethod`, temporal extent, and obtaining containing-System relation to independently admitted `CatalystSearchTeamSystem`. Actual application `CatalystSelectApplication-17` separately carries its effective candidate, criteria, and A.19 `SelectionSlot` bindings. Neither the assignment nor F.6 is an A.15.1 admission premise.
- Because this account explicitly attributes the Work under `CatalystSelectorAssignment-17`, F.6 afterward establishes `performedUnderAssignment(CatalystSelectionWork-17, CatalystSelectorAssignment-17)` through that same obtaining A.13 assignment. The direct case fact links the exact pair, holder equality holds, and the assignment interval covers the Work. A different overlapping assignment held by the same System would not establish this attribution. A short result may omit the assignment identifier only after every fact consumed by the attribution remains recoverable.
- A persisted shortlist assertion is a separate C.2.1 episteme; its DRR or SCR references do not by themselves prove the exclusion facts, warrant the result, authorize downstream action, or make that episteme available to an audience.

- When one upstream `C.19` pass has already narrowed the live pool to one internal retained subset over registered families, `G.5-6 DeclareSetResult` may declare that result as one `Shortlist` with one `ShortlistId` and explicit basis pins only when selector-facing result declaration is now the question. Until that declaration occurs, the internal retained subset is not yet one G.5 shortlist result.
- When one upstream `C.11` pass has already fixed one local choice over one declared source set, `C.19` has fixed one retained pool treatment, an accepted decision has fixed all-member inclusion, or `C.24` has produced one enactment-facing narrowed handoff, use `G.5-6 DeclareSetResult` when selector-facing set-result content is now the question. Until that declaration occurs, the `ChoiceResult`, `PoolPolicyResult`, accepted inclusion basis, `CallPlan`, or `CheckpointReturn` is not itself that G.5 result. Non-Method members do not pass through `RegisterFamily` or `G.5-3 Select`.

#### G.5:4.4b - Declared selected-set result and closure rule

When the current question is selector-facing result declaration, state one explicit selected-set result rather than leave it implicit in a selector trace, comparison note, or local choice.

For method dispatch, that result closes selector work over grounded rows. For a `JointUseSet`, it records already identified members that are all included for one named use. It does not replace registry maintenance, comparison rules, the upstream choice or inclusion basis, or the patterns that identify the members and their relations.

The admissible selector outcome families here are:

- `SelectorOutcomeKind = SetResultOutcome`, whose closed `SetResultFamily` value set is `Shortlist` when alternatives are retained for later choice and the result does not order them, `RankedShortlist` when the result orders those retained alternatives, and `JointUseSet` when every named member is included for one named use;
- `SelectorOutcomeKind = HandoffOutcome`, with `HandoffKind = SpecialistHandoff` or one other narrowed handoff plan when heterogeneity is the truthful downstream result;
- `SelectorOutcomeKind = AbstainOutcome` when no admissible candidate exists and the truthful result is one abstain; and
- `SelectorOutcomeKind = EscalationOutcome` when no admissible candidate exists and the truthful result is one escalation.

`G.5-3 Select` may emit one of these outcome kinds only over the exact Method candidates admitted through its kernel; `G.5-6 DeclareSetResult` emits `SetResultOutcome` from exact already identified members and a current inclusion basis. Neither branch performs an upstream choice, makes a member relation obtain, or proves actual selection Work.

A `JointUseSet` uses this bounded representation:

- `namedUse` states the one joint use;
- `memberEntries` contains one keyed entry per included member;
- every entry has one exact `memberRef`; the membership result adds no per-member contribution or basis field;
- each exact `memberRef` occurs at most once, and entry order has no semantic effect;
- if a serialization also emits top-level `members`, it is only the unique set projection of `memberRef` values from `memberEntries`, never a second maintained list;
- `ordering`, inclusion conditions, and sufficient top-level `basisPins` remain explicit; and
- candidate-pool membership and excluded candidates stay separate from emitted joint-use membership.

Exact content, claims about a member's use or contribution, and direct relations keep their own governed records. When one supports the membership result, cite that existing record among `basisPins`; `memberEntries` creates neither the cited content nor a new contribution relation.

For framework use, `memberRef` may name an exact already identified edition under its existing identity rules. Do not populate `MethodRef`, create a registry row, or classify that edition as a Method merely to emit the result.

Every outcome still states its `SelectorOutcomeKind`, public result kind when applicable, members, keyed entries, handoff content, or blocking condition, ordering, and sufficient basis pins. A handoff also states its next downstream use boundary.

A compact retained-alternative result may look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = Shortlist,
  members = [family_A, family_C],
  shortlistId = shortlist_17,
  ordering = unordered,
  basisPins = [pathSlice_41, scr_22],
  nextUse = downstream_comparison
)
```

A compact joint-use result may look like:

```text
SelectorOutcome(
  selectorOutcomeKind = SetResultOutcome,
  setResultFamily = JointUseSet,
  namedUse = cohort_review,
  memberEntries = [
    { memberRef = FPF@C },
    { memberRef = Domain@D },
    { memberRef = Local@L }
  ],
  ordering = unordered,
  inclusionConditions = [all_three_editions_required_for_cohort_review],
  basisPins = [choice_result_12, edition_basis_7]
)
```
Close with `Shortlist` or `RankedShortlist` when the result retains alternatives. Close with `JointUseSet` only when every member is included for the named use and its keyed membership can be stated truthfully. Close with a handoff, abstain, or escalation outcome when that is the actual result. If the result omits its result family, members or member entries, ordering, named use where required, or basis pins, it is not a complete `G.5` result.

#### G.5:4.4bb - Public labels over archive, front, and style source sets

When a selector consumes a declared `ExplorationArchive`, `Archive`, `Front`, or `Q-front`, keep that object as a source-set family or source-set reference; it is not the emitted G.5 outcome. The emitted result states one admitted `SelectorOutcomeKind` and, for a set result, one admitted `SetResultFamily`. `StyleShortlist` and `TraditionShortlist` may be public domain labels over an admitted set-result family after their term bridges and cultural meaning are clear; they do not extend either closed set.

```text
SelectedSetResultLabelLine@Context:
  selectorOutcomeKind:
  setResultFamily?:
  sourceSetFamily:
  publicSelectedSetLabel?:
  namedUse?:
  memberEntries?:
  membersOrHandoff?:
  derivedViewKind?:
  basePaletteOrArchiveRef?:
  ordering:
  basisPins:
  nextUse:
```

Earlier records may keep `membersOrHandoff`. Read it as `members` for `Shortlist` or `RankedShortlist` and as `handoffContent` for a `HandoffOutcome`. It cannot replace keyed `memberEntries` in a `JointUseSet`; if it also lists joint-use members for compatibility, that list is only the unique set projection of the entry keys.

`sourceSetFamily` may name a declared `Front`, `Q-front`, `ExplorationArchive`, `Archive`, current pool subset, or derived tradition view. For retained alternatives, `publicSelectedSetLabel` normally names `Shortlist` or `RankedShortlist` and may use a domain label such as `StyleShortlist` or `TraditionShortlist` only when the term bridge is already clear. `JointUseSet` is not a shortlist label: it names an all-member result and therefore uses `namedUse` plus keyed `memberEntries`. G.5 does not create the archive, compute the comparison, govern the pool policy, decide the cultural-evolution case, establish member identity or relations, or repair the term bridge. Use `C.18` for archive formation, `A.19.CPM` for comparison, `C.19` for pool policy, `C.36` for cultural-evolution claims, each member's own identity and relation patterns for those facts, and `F.17`/`F.18`/`F.9` for local meanings, naming settlement, and any obtaining term Bridge.

#### G.5:4.4c - Result-declaration quick card

Use the outcome definitions in §4.4b and fill only the applicable fields:

| Field | When and what to state |
| --- | --- |
| `selectorOutcomeKind` | Every result: the admitted set, handoff, abstain or escalation kind. |
| `setResultFamily`, `members` | For retained alternatives: the admitted shortlist family and exact surviving refs; preserve a justified order for `RankedShortlist`. |
| `setResultFamily`, `namedUse`, `memberEntries`, `inclusionConditions` | For joint inclusion: `JointUseSet` and its §4.4b keyed membership declaration. |
| `handoffKind`, `handoffContent` | For a handoff: `SpecialistHandoff` or another admitted narrowed handoff and the content the next receiver needs. |
| `blockingPins` | For abstain or escalation: the actual blocking conditions. |
| `ordering` | Ranked, unordered or not applicable, as the outcome permits. |
| `basisPins`, `nextUse` | The supporting basis and next use boundary; `none` when there is no next use. |
| `publicId` | Only when stable public identity is needed; `ShortlistId` is specific to a shortlist. |

The pump result in §0.5 and the joint-use declaration in §4.4b show complete filled forms. A missing required value leaves the result incomplete.

#### G.5:4.4ca - Derived tradition-view result stays derived over one declared palette

When the source is `TraditionFront` or `TraditionArchive`, keep its base `SoTAPaletteDescription` recoverable. State `SourceSetFamily`; add `DerivedViewKind` when it changes interpretation or later publication and `SourceSetComposition` only when several source-set families were actually composed. Cite the derivation's declared Q, reachability or coverage rule among the DRR/SCR or equivalent basis pins. The view qualifies the source; §4.4b still defines the emitted outcome.

#### G.5:4.4d - Worked result-declaration closure slice

| Receiving situation | Complete result and changed action |
| --- | --- |
| The two pump Methods in §0.5 survive, with no admitted ordering. | Emit its unordered `Shortlist`; the receiver still has a choice to make. |
| A declared comparator orders family_B before family_A for the specialist handoff. | Emit a `RankedShortlist` with `[family_B, family_A]`, the comparator and supporting basis pins, and the handoff use. A request for an order alone supplies no comparator. |
| The cohort decision includes `FPF@C`, `Domain@D` and `Local@L` together. | Emit the §4.4b `JointUseSet`; the receiver uses all three exact editions under the inclusion conditions. |
| No candidate clears the applicable admissibility/evidence gates. | Emit `AbstainOutcome` or `EscalationOutcome`, naming the blocking pins, basis and next use; an empty shortlist leaves the stop unexplained. |

The following extensions apply only when their corresponding mode is active. Their declared `Uses` and pins cite the governing semantics.

**GPatternExtension block: `G.5:Ext.EELog`**

* `PatternScopeId`: `G.5:Ext.EELog`
* `GPatternExtensionId`: `EELog`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.19`
* `Uses`: `{C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `EELensPolicyRef` *(or equivalent lens or policy id carried by `C.19`)*
  * `RiskBudgetRef?`
  * `ProbeAccountingRef?`
  * `FailureBehaviorPolicyId?` *(if degrade behavior is governed by policy)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block activates exploration and exploitation-governed dispatch.
  * Post‑2015 examples that typically land here: modern bandit‑style or Bayesian selection under explicit risk budgets; adaptive evaluation and probing regimes; safe‑exploration variants where “abstain” or “degrade” is policy-bound.

**GPatternExtension block: `G.5:Ext.SoSLOG`**

* `PatternScopeId`: `G.5:Ext.SoSLOG`
* `GPatternExtensionId`: `SoSLOG`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.23`
* `Uses`: `{C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `SoSLogRuleId[]`
  * `SoSLogBranchId[]` *(including escalation branches, if used)*
  * `FailureBehaviorPolicyId` *(if degrade behavior is made explicit)*
  * `MaturityRungId[]?` *(when maturity ladders are used as gates; semantics come from `C.23`)*
  * `AdmissibilityLedgerRef?` *(when selector consumes admissibility rows rather than recomputing thresholds)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* `Notes (extension discipline; semantics cited):`

  * This block pins dispatch decisions to explicit rule and branch ids, enabling auditable “why” without inventing a fourth acceptance status.

**GPatternExtension block: `G.5:Ext.NQD`**

* `PatternScopeId`: `G.5:Ext.NQD`
* `GPatternExtensionId`: `NQD`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* `Uses`: `{C.18, C.19}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef`
  * `TaskSignatureRef` *(when QD is enabled via TaskSignature flags or traits)*
  * active fields from C.21's DHC replay basis *(only when this telemetry consumes a C.21 DHC coordinate; carry exactly the fields that coordinate used)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * G.5 core remains QD‑agnostic; QD semantics are governed by `C.18`.
  * Post-2015 families that typically use this extension declaration: MAP-Elites-class QD including later archive-centric refinements, CMA-ME-class hybrids, modern illumination and coverage telemetry regimes where admissibility and edition pinning matter.

**GPatternExtension block: `G.5:Ext.OpenEndedFamilyWiring`**

* `PatternScopeId`: `G.5:Ext.OpenEndedFamilyWiring`
* `GPatternExtensionId`: `OpenEndedFamilyWiring`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `G.2`
* `Uses`: `{G.2, C.19, C.23}`
* `⊑` and `⊑⁺`: `∅`
* Required pins, edition pins, and policy pins (minimum):

  * `GeneratorFamilyRowRef[]`
  * `TransferRulesRef.edition` *(mandatory when Open‑Ended is enabled)*
  * `EnvironmentValidityRegionRef?`
  * `CoEvoCouplerRef[]?`
  * `SoSLogBranchId[]?` *(when validity of generated tasks is gated by explicit branches)*
* `RSCRTriggerKindIds`: `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* `Notes (extension discipline; semantics cited):`

  * This block enables declared sets of `{Environment, MethodFamily}` pairs without redefining generator semantics in G.5.
  * Post‑2015 examples typically referenced via `G.2` family cards: POET‑class and later open‑ended and co‑evolutionary regimes, including enhanced variants where transfer policies and validity gates must be edition‑pinned.


#### G.5:4.4e - Source sets, operating modes and comparison policy

Use §4.4b for the emitted outcome and §4.4bb–ca for its source and public-label interpretation. An actual `SelectionSlot` binding carries the by-value selected candidate set; it is separate from G.5's declared `SelectorOutcome`. `ChoiceSet` remains an ordinary mathematical set gloss, not an additional public result kind.

| Declaration | Meaning and applicable condition |
| --- | --- |
| `Front` | The non-dominated source set under the declared `DominanceSet`. |
| `Archive` | The exploration set retained under its policy. |
| `PortfolioMode` | How the selector operated. The default `Archive` retains exploration evidence; it establishes neither an emitted Archive nor a different result family or DominanceSet. |
| `SourceSetFamily`, `SourceSetComposition` | State the immediate source family; use composition only when several source families were actually consumed, for example a front and an archive. |
| `DerivedViewKind`, `BasePaletteRef` | Qualify an actual derived view under §4.4ca; the latter is a reference, not a kind. |
| `PromotionPolicy` | Required when tie-break or telemetry signals are promoted into dominance. |
| `SubjectKind`, `RetentionIntent=steppingStone` | Qualify the relevant declaration or retention policy; neither names another emitted set result. |

Use controlled tokens, cited ids or already declared head labels for these fields. CostToProbe, ValueOfInformation, ValueOfComputation, explore_share, graduation conditions and sequencing pressure belong to the surrounding choice doctrine when they affect the decision; a result field does not establish them. All-member membership and candidate/exclusion records retain the separation in §4.4b.

#### G.5:4.6a - Causal method dispatch declarations

When method dispatch compares causal uses, each compared Method declares its causal question/rung and whether it is being used as an observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only Method.

```text
MethodFamily.causalUseDispatchSpec?:
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalSupportComponentRefs?: CausalSupportComponentRefs
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalMethodUseClassification:
    observationalPredictor |
    interventionOptimizer |
    counterfactualStrategy |
    causalFairnessEstimator |
    causalRLPolicy |
    simulationOnlyMethod
  supportedUse
  unsupportedUse
```

`CausalUseQuestionRef` identifies the question content used by C.28; it is not a durable root U-kind. `causalMethodUseClassification` describes the Method's proposed selector-facing use and supplies no system-role assignment, responsibility, authority, or causal certification.

A simulation-only Method cites `simulationResultRef` inside its support components and states bounded model use plus unsupported realized/interventional use. G.5 declares the dispatch result; C.28 supplies the causal-support result. A selector may still abstain even when a C.28 result is supported.

### G.5:5 - Archetypal Grounding

**Tell (archetype).**
The selector-bearing **System** must choose among rival families without lying about measurement admissibility, crossings, or evidence. The result **Episteme** keeps the comparison basis, audit pins, and refresh conditions recoverable. When the current result instead includes several already identified members together, the same result-content boundary must not disguise that all-member meaning as retained alternatives.

**Show 1 (multi-Tradition dispatch; unordered shortlist).**
A `CG-Frame` includes multiple decision-theoretic families with different admissibility assumptions. Evidence for some CHR traits is incomplete.
System registers families (S1), then runs `Select` (S3) on a pinned `TaskSignatureRef`. Eligibility is tri-state; some families **receive abstain** due to missing minimal-evidence pins. Among remaining candidates, only a partial order is admissible, so the selector emits one `Shortlist` with explicit `basisPins` instead of inventing one scalar winner. No shadow acceptance logic appears in the selector; it consumes pinned acceptance and admissibility records.

**Show 2 (specialist handoff; ranked result).**
A bounded-specialization comparison keeps two method families live under a pinned admissible comparator that orders them, and downstream handoff needs that ordering.
Declare one `RankedShortlist` with that ordering and comparator among its basis pins, `ShortlistId` when public identity is needed, and handoff-facing `nextUse`. If no admissible comparator supplies an order, retain an unordered `Shortlist`; the request for a ranked handoff does not establish one.

**Show 3 (no admissible survivor; abstain or escalation).**
In this frame, one admissibility gate and one minimal-evidence gate fail at the same time.
The truthful `G.5` result is one abstain or escalation result that names the blocking pins and the next downstream use boundary, not one empty shortlist that leaves downstream users unsure whether selection silently failed or admissibly stopped.

**Show 4 (complementary framework editions; unordered joint use).**
A training cohort needs `FPF@C`, `Domain@D`, and `Local@L` together. The editions are already identified under their own edition rules; they are not Method candidates or registry rows. An accepted cohort decision supplies the exact members and basis. `G.5-6 DeclareSetResult` emits one unordered `JointUseSet` with one keyed entry per edition, the named cohort-review use, inclusion conditions, and sufficient top-level basis pins. Direct dependencies and pairwise compatibility claims remain with E.4.PFR; publication and access remain with E.17/E.24.PUB and the applicable access-carrier pattern. The G.5 result declares membership but does not perform the choice, make those neighboring claims obtain, or create a contribution relation.

**Show 5 (support-sensitive Method eligibility).**

Keep the exact admitted Methods, row editions, and grouping basis from §0.5. In a gated variant, the matching G.4 task map makes `AC_InputConditionGate-E1` from G.4 §5 applicable to `ThresholdTrendReviewMethod-E2`. Consume that clause's value and threshold rather than define either in G.5. For the two-condition case there, the returned `fail` excludes that row from the assurance-gated set. Replacing its joint probability with minimum would wrongly retain it. An otherwise admissible row stays in the set under its own declared eligibility basis; if none survives, return the existing abstain or escalation outcome.

If the dependence model is missing, use the clause's `unknown` branch rather than pass by a high F. In the ordinary, non-assurance question of §0.5, both grounded rows still form the unordered `Shortlist`. A formal proof, a limited complementary study, and an overlapping contrary result can remain separate support with their limitations; neither weak additional evidence nor the absence of an unjustified common score automatically removes a Method. A defeated necessary premise still changes the eligibility that actually relies on it.

**Show 6 (one calibrated correspondence, two receiving uses).**

Use G.7 §4.5's `VehicleTransportOrder` row from C.3.3 to select among independently admitted Methods for a transport review. The task's applicability comparison uses only the preserved transport/passenger order and explicitly ignores propulsion. When receiving admissibility, fresh target classification of the subject vehicles, the bounded comparison conditions and matching reliance pass, that row can support Method eligibility under the task's other rules. Keep those premises with the result.

For a second task that requires battery-health evidence, the same CL^k=2 row loses the necessary EV distinction and cannot support that criterion. Return the missing battery premise through the existing unknown/abstain or evidence-request branch. Raising a scalar summary or citing a waiver does not restore that distinction. G.7 reports the correspondence; the exact TaskSignature and receiving rules decide each selection use.

### G.5:6 - Bias-Annotation

Potential biases and failure modes this pattern explicitly guards against:

* **Monoculture bias (single Tradition dominance by default).** Mitigation: rows retain an explicit eligibility basis and conditional assurance expectations; public registration adds its stronger records; selection is set‑returning under partial orders; method‑specific policies stay explicit pins rather than hard-coded defaults.
* **Hidden scalarisation bias.** Mitigation: set-return semantics is pinned through `G.Core`; dominance regimes are explicit and each default cites one declared governing definition.
* **“Tool equals method” bias.** Mitigation: notation independence and prohibition of tool keywords in core registry and eligibility fields; tool choices are outside the core.
* **Cross-sense leakage bias.** Mitigation: when expressions have distinct source-local meanings, require exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition, and the matching A.10 or B.3 reliance branch; keep loss and CL visible where material. Crossing pins and bundles remain audit or publication references and cannot make an implicit crossing admissible.

* **Survivorship bias in refresh.** Mitigation: RSCR triggers are typed and id-based; freshness, decay, and telemetry deltas are first‑class causes with canonical ids.

### G.5:7 - Conformance Checklist (normative)

| ConformanceId   | Statement |
| --------------- | ----------|
| `CC‑G5‑CoreRef` | **Core conformance bridge.** `G.5` is conformant only if the **effective** `G.Core` obligations referenced by `G.5:4.1 (GCoreLinkageManifest)` are satisfied (after profile and set expansion plus explicit deltas). |
| `CC‑G5.0`       | Core standards **SHALL** remain notation‑independent; vendor or tool keywords are forbidden in registry, eligibility, assurance, or selector‑kernel obligations (`E.5.*`). |
| `CC‑G5.1` | Every reusable MethodFamily row **SHALL** fix its exact members, grouping basis, eligibility/comparison basis and selection-changing pins in one immutable edition. Intentional public registration additionally declares EligibilityStandardRef using CHR/CAL terms and applicable edition pins. Both branches remain notation-independent. |
| `CC-G5.2`       | Selection **SHALL** be a pure function of `TaskSignatureRef`, exact method- and generator-family row refs, any conditionally current exact `TaskMapRef`, and pinned policy or edition refs; side effects are limited to emitting DRR and SCR pins, telemetry triggers, and RSCR triggers (no hidden mutation of constraint-bearing spec refs). |
| `CC‑G5.3`       | **Delegated (ID‑continuity) plus F.9 use boundary.** When a selector use relates expressions with distinct F.17 source-local meanings, it **MUST** resolve the exact cells, an obtaining F.9 Bridge, a separate C.2.1 `<u,d,r,t,polarity>` proposition, and the matching A.10 or B.3 reliance branch. G.Core crossing visibility and penalty-assignment semantics still apply. **Delegation targets:** `CC‑GCORE‑CROSS‑1`, `CC‑GCORE‑PEN‑1`. Pins alone **MUST NOT** establish the Bridge, use, reliance, or actual selector application. |
| `CC‑G5.4` | **Governing rule for** `DefaultId.GammaFoldForR_eff`. An R or R_eff composition **MUST** use a justified receiving quantity, input meanings and scales, dependency model and operation under B.3/C.2.2; cite contributors and pin the actual model/policy. Neither a universal minimum/maximum or best-source cap, an ungrounded F-to-R conversion, nor monotonicity and boundedness alone supplies that model. Without a justified common model, retain separate support and a bounded synthesis. If an actual G.4 gate requires the missing quantity, follow that clause's unknown behavior; a calculated threshold failure remains a failure. G.4 owns acceptance conditions and thresholds. Ordinary selection with no assurance condition remains usable without a new R calculation. |
| `CC-G5.5`       | Ordinal scales **MUST NOT** be averaged or subtracted; any aggregation or comparison must respect CHR scale typing and admissibility constraints, including CSLC where applicable. |
| `CC‑G5.6` | **Public registration.** Intentional registration of a MethodFamily or GeneratorFamily under a stable public registry identity **SHALL** publish that identity to UTS with the applicable naming and lexical-continuity discipline. Project-local reusable rows keep the immutable member/basis contract of S1/S1′ without this added duty. Visibility alone does not select the public identity contract; actual audience availability is a separate E.24.PUB occurrence. |
| `CC‑G5.7`       | **Conditional.** If `G.5:Ext.EELog` is present, exploration **MUST** be budgeted under the pinned exploration and exploitation log policy; probe outcomes **MUST** feed refresh through canonical RSCR trigger kinds. |
| `CC‑G5.8` | **Actual CG-Frame gate enforced.** When selection uses a CG-Frame gate, retain its pinned CG-Spec.MinimalEvidence requirements for the cited characteristics. Failed requirements reject or abstain under that gate's rule; missing required input remains unknown/abstain and cannot pass. Registering a local grouping without this selection/gate use does not activate that gate. |
| `CC-G5.9`       | **Delegated (ID-continuity).** Set-return semantics are pinned through `G.Core`. **Delegation target:** `CC-GCORE-SET-1`. Candidate ordering **MUST** be admissible over typed traits and admissibility constraints. If only a partial order is available, selection **MUST** return one declared selector outcome, for example one `SetResultOutcome` with `Shortlist` or `RankedShortlist`, one `HandoffOutcome` with `SpecialistHandoff`, or another pinned outcome result, with no forced totalisation via inadmissible scalarisation. |
| `CC-G5.10`      | **SCR completeness.** SCR **MUST** enumerate Gamma-fold contributors when used, referenced constraint-bearing spec editions, the source and evidence citations used in gating and rationale (`PathId` or `PathSliceId` when graph citations are used or independently required), and `MinimalEvidence` gating verdicts by lane and carrier when such gating is relied upon. |
| `CC‑G5.11`      | **Delegated (ID‑continuity).** Tri‑state eligibility and acceptance semantics plus unknown handling are pinned through `G.Core`. **Delegation target:** `CC‑GCORE‑GUARD‑1`. *(Includes the rule that `degrade(...)` is expressed through a pinned FailureBehavior or SoS‑LOG branch id, not as a fourth status.)* |
| `CC-G5.12`      | **Applicability of a selected method set.** A selected method-set result **MUST** state the exact task, exact row refs or other exact members, grouping and selection basis, truthful outcome kind, ordering, selection or inclusion conditions, and the named next use. Add `ClaimScope`, selected A.2.6 slices, a validity or evaluation window, source or scheme editions, intended-use restrictions, counterexamples, evidence pins, and transfer or change conditions only when they change eligibility, selection, applicability, or a receiver's justified reliance. Omitting any such action-changing value fails this check and reopens the affected result; values that change no current action stay out. Coverage, descriptors, and distance may guide a named search for omissions but **MUST NOT** establish broader applicability. Apply `E.24.UK` or `A.8` only to a separate claim about a durable kind or kernel placement; neither claim widens the selected set's applicability. |
| `CC‑G5.13`      | **Conditional.** If the selector consumes admissibility or maturity records (e.g., through `G.5:Ext.SoSLOG`), it **MUST NOT** recompute thresholds; it consumes pinned admissibility ledger rows and cites clause and rung ids in audit pins. |
| `CC‑G5.14`      | **Φ(CL) and Φ_plane discipline.** If crossing or plane penalties are applied, the active penalty policy ids (e.g., `Φ(CL)`, `Φ_plane`) **MUST** be explicit in audit pins, and the pinned policies **MUST** satisfy the monotone and bounded requirements asserted by their cited constraint-bearing spec refs and be published through those same cited spec refs (e.g., `CG‑Spec`). SCR **MUST** record the policy id in use; penalty assignment semantics remain pinned through `G.Core`. |
| `CC-G5.15`      | Unit and scale admissibility **MUST** be established via CSLC (A.18) before any aggregation or Gamma-fold; unit and scale mismatches are a fail-fast defect. |
| `CC‑G5.16`      | Hidden thresholds are forbidden. Thresholds live in explicitly pinned acceptance or eligibility policy records, not in selector prose, LOG shells, or code.  |
| `CC‑G5.17`      | ReferencePlane **MUST** be declared (pinned) for any claim that is used in dispatch, and the selector’s audit records must cite it (including plane‑crossing pins when applicable). |
| `CC-G5.18`      | Numeric comparisons and aggregations used by dispatch **MUST** cite an admissible, edition-pinned comparator or spec publication (as provided by the constraint-bearing spec refs); inadmissible mixes of scale types are forbidden. |
| `CC-G5.19`      | **Conditional (QD).** If `G.5:Ext.NQD` is present, the required QD telemetry triple (quality, diversity, and QD summary) **MUST** be computable and ready for emission under the pinned descriptor and distance definitions and archive policy, without redefining their semantics in G.5. If actual publication is current, use E.17 for a source-backed face and return to source and E.24.PUB for the publication occurrence and audience availability. |
| `CC‑G5.20`      | **Conditional (QD).** QD and illumination summaries are treated as telemetry unless explicitly promoted by a pinned acceptance or policy record; the selector must record the promoting policy id in audit pins. |
| `CC-G5.21`      | **Conditional (Archive and QD).** Any use of archives **MUST** declare `InsertionPolicyRef` and pin the required editions for reproducibility, including descriptor and distance definitions and any method editions they depend on. |
| `CC‑G5.22`      | **Conditional (QD).** Twin‑naming discipline for descriptor vs plain space (if used) must be respected (distinct objects; no aliasing).  |
| `CC-G5.23`      | **Default rule for** `DefaultId.PortfolioMode`. The selector **MUST** expose `PortfolioMode` with values `Pareto` or `Archive`, with **default = `Archive`**, and echo it in DRR and SCR records and declared selector results when not explicitly overridden by pinned policy or TaskSignature. The default is a retention and evidence-preservation policy, not a public selected-set label, not a dominance default, and not a substitute for `SetResultFamily`. Epsilon-fronts are allowed as *local* decision aids under `CG-Spec` when explicitly pinned. |
| `CC-G5.23a`     | **Parity-run publication.** If parity harness is in use, a selector or generator **MUST** publish a parity run and `ParityCard` to **UTS** (see `G.9`). This obligation remains mandatory irrespective of dominance policy or `PortfolioMode` policy. |
| `CC‑G5.24`      | **Conditional (Open‑Ended).** If `G.5:Ext.OpenEndedFamilyWiring` is present, the selector **MUST** return declared sets of `{Environment, MethodFamily}` pairs as set‑valued outcomes under explicit pins. |
| `CC‑G5.25`      | **Conditional (Open‑Ended).** In Open‑Ended mode, `TransferRulesRef.edition` is mandatory and **MUST** be visible to telemetry and RSCR triggers.  |
| `CC-G5.26`      | **Conditional (Archive and QD).** Within any archive niche or cell, ordering and tie-breaks **MUST** remain admissible over compatible scales; inadmissible mixed-scale weighted sums are forbidden. |
| `CC‑G5.27`      | If the selector cites any `GateCrossing`, the corresponding `CrossingBundle` publication **MUST** be present and conformant; missing or non‑conformant `CrossingBundle` blocks downstream consumption. The bundle packages already governed crossing evidence for that named use; it **MUST NOT** create the F.17 endpoints, F.9 Bridge, bounded-use proposition, A.10/B.3 reliance, gate decision, authorization, or actual selector use. |
| `CC‑G5.28`      | **Default rule for** `DefaultId.DominanceRegime`. `DominanceRegime` **SHALL** default to `ParetoOnly`. Any inclusion of additional telemetry dimensions into dominance (e.g., illumination) requires an explicitly pinned acceptance or policy record and must be recorded in audit pins. **Parity‑run publication (CC‑G5.23a) remains mandatory** irrespective of dominance policy. |
| `CC-G5.29`      | **Conditional (QD and Open-Ended).** Any telemetry event that materially changes an archive state or retained-set state **MUST** identify the exact changed state and affected-use scope, log `PathSliceId` when graph-scoped or independently required by the receiving contract, and retain the active policy id and active editions of the relevant definition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `TransferRulesRef.edition` when applicable) and expose them to RSCR triggers. |
| `CC‑G5.30`      | **No Strategy minting.** Within `G.5`, “strategy” is a policy‑bound composition template; the pattern **SHALL NOT** mint a durable U-kind named `Strategy` (E.10 and E.24.UK discipline). If a stable reference is needed, publish composition and policy ids (e.g., UTS entries) rather than minting a universal kind. |
| `CC-G5.31`      | **Strategy hint on non-admissible sets.** If selection yields `CandidateSet = EMPTY`, the selector **SHALL** emit an explicit escalation hint (`ActionHint`) that is compatible with DRR and SCR records and auditable: include the top three actual blocking constraints as cited ids and pins, or all actual blockers when fewer than three exist, and where applicable include the relevant edition pins, for example `TransferRulesRef.edition` in Open-Ended mode, to guide exploration under explicitly pinned lenses such as the exploration and exploitation log policy. |
| `CC‑G5.32`      | **Parity‑run publication and admissible roll-ups.** If parity harness is in use, parity publication is required per `CC‑G5.23a` (ID‑continuity). Any scalar roll-up or summary view **MUST** be admissible under **CG‑Spec** (no mixed‑scale sums), and published views must preserve set‑return semantics (no single‑score leaderboards as authoritative outputs without an explicit, admissible comparator publication). |
| `CC‑G5.33`      | **Conditional (bounded specialization).** When the selection question is acquisition of usable specialization on a declared `TaskFamilyRef` or `TaskSignature`, selector outputs **SHALL** either emit `TaskFamilySpecializationProfile@Context` or cite equivalent pins carrying the `C.22.1` adaptation-signature fields needed for comparison: work-measure threshold target, prior exposure declaration, time-to-threshold, budget-to-threshold, post-threshold efficiency when relevant, and any declared transfer, retention, downside, or specialization-entry notes. |
| `CC‑G5.34`      | **Selected-set result kind.** When `SelectorOutcomeKind = SetResultOutcome`, the public result kind **MUST** be explicit. Use `Shortlist` for unordered alternatives retained for later choice, `RankedShortlist` only when the result orders those alternatives, and `JointUseSet` only when every named member is included for one named use. `ChoiceSet` **MUST NOT** silently replace the public result kind. |
| `CC‑G5.34a`     | **Selector outcome typing.** Declared selector results **MUST** state `SelectorOutcomeKind`. `SetResultFamily` is required only when `SelectorOutcomeKind = SetResultOutcome`; `HandoffKind` is required only when `SelectorOutcomeKind = HandoffOutcome`. Non-set outcomes **MUST NOT** masquerade as one public selected-set label. |
| `CC‑G5.35`      | **Result-content closure.** Any declared selector result **MUST** state the `SelectorOutcomeKind`, applicable public result kind, retained members or keyed joint-use entries, ordering, named use and inclusion conditions when required, and basis pins directly in the emitted result rather than relying on upstream `C.11`, `C.19`, or `C.24` notes. |
| `CC‑G5.36`      | **Neighboring-pattern boundary.** If the current question is still local choice among already-available options, pool policy over still-live candidate lines, or enactment planning after choice, a `G.5` use **MUST** consume the result produced by applying `C.11`, `C.19`, or `C.24` rather than restating those patterns as if declaring selector-facing content decided the upstream matter. |
| `CC‑G5.37`      | **Derived tradition-view result discipline.** If the selector emits one result through a derived tradition view such as `TraditionFront` or `TraditionArchive`, it **MUST** keep the declared base `SourceSetFamily` explicit, keep `SoTAPaletteDescription` recoverable through `BasePaletteRef`, and **MUST NOT** let the derived view become the default meaning of `Tradition`, `TraditionPalette`, or the base palette. |
| `CC‑G5.38`      | **Causal method dispatch declarations.** If method selection involves causal methods, each compared method **MUST** declare `causalMethodUseClassification` as observational predictor, intervention optimizer, counterfactual strategy, causal fairness estimator, causal-RL policy, or simulation-only method, and **MUST** carry `causalUseSupportResultRef` and the cited result's verdict when it consumes `C.28` causal-use support rather than treating method dispatch as causal certification. |
| `CC-G5.39`      | **Registry grounding, edition, and grouping boundary.** Every consumed method-family row **MUST** be addressed by one exact `MethodFamilyRowRef` whose immutable edition resolves its non-empty `MethodRef[]` to exact A.3.1 Methods; every consumed generator-family row **MUST** use one exact `GeneratorFamilyRowRef` and resolve non-empty exact generator refs under their subject patterns. Each row edition cites the independently established classification, membership relation, or explicit project-local grouping criterion used by this selector. A row, id, label, description, family card, eligibility or maturity record, policy, evidence pin, shortlist, or publication **MUST NOT** create a member or membership fact. Missing grounding or an unresolved row edition blocks that row's family use. |
| `CC-G5.40`      | **Composition and selected-structure boundary.** A composition shape **MUST** remain a template unless one already identified A.3.1 Method separately passes B.1.5's complete composite-method qualification. An organization that does not constitute one Method **MUST** be consumed as an A.22 `U.Structure` only after all four A.22 identity discriminators are present. A template, A.3.2 description, registry row, selector outcome, diagram, label, or notation **MUST NOT** create either governed object or its underlying relations. |
| `CC-G5.41`      | **Declaration, actuality, performer, result and publication boundary.** A registry, selector, policy, template, shortlist, DRR, SCR, telemetry or publication-content declaration **MUST NOT** be treated as an A.13 performer core, dated Work, F.6 attribution, actual A.6.1 `Select` application or binding, domain-result truth, C.2.1 result episteme, A.10 evidence-provenance path, B.3 assurance claim, authorization, or E.24.PUB publication occurrence. Every claimed precise performer **MUST** first have the A.13 core; A.15.1 **MUST** admit the Work independently; F.6 enters only for a current exact assignment-bound attribution through the same obtaining assignment. Every other claimed actual object or relation **MUST** be recovered under its subject pattern; missing actuality blocks only that stronger claim. |
| `CC-G5.42`      | **Crossing completeness.** A selector use that relates expressions with distinct source-local meanings **MUST NOT** proceed from Bridge, CL, loss, registry, policy, `CrossingAllowance`, `GateCrossing`, `CrossingBundle`, DRR, or SCR pins alone. It requires exact F.17 endpoint senses, an obtaining F.9 Bridge, a separate C.2.1 bounded-use proposition, and the matching A.10 reliance disposition or B.3 assurance branch; authorization and the actual selector application remain separate. |
| `CC-G5.43`      | **Ordinary-use proportionality.** A bounded selector run over already grounded rows **MUST** be usable from the exact task, immutable row-edition refs, Methods and grouping bases, declared eligibility or comparison basis, truthful outcome, members, ordering status, basis refs and next use. It **MUST NOT** demand a fresh registry build, crossing branch, A.10 reliance claim, B.3 assurance claim, stable public identity, or E.24.PUB occurrence unless that stronger object or claim is current. The dated selector Work required by S3 remains independently admitted; upstream mathematical comparisons need their actual application bindings, with separate comparison Work only when asserted. Missing conditional apparatus blocks only the stronger claim. |
| `CC-G5.44`      | **Joint-use membership integrity.** A declared selector-result record with `SetResultFamily = JointUseSet` **MUST** name one bounded use, set `ordering = unordered`, and use keyed `memberEntries` with each exact `memberRef` present at most once. Entry order has no semantic effect; the result **MUST NOT** add an undefined per-member contribution or basis field; and any top-level `members` **MUST** be only the unique set projection of the entry keys, never an independently maintained list. Exact supporting content or claims remain in their own records and may be cited only among sufficient top-level `basisPins`. |
| `CC-G5.45`      | **Joint-use ontic and actuality boundary.** A declared selector-result record with `SetResultFamily = JointUseSet` is well formed only if every exact framework-edition or other non-Method `memberRef` resolves under its existing identity and the record adds no `MethodRef` value or registry row merely for membership. Candidate-pool and excluded-candidate records, direct member relations, local choice, actual selection Work, publication availability, and access remain separate. |
| `CC-G5.46`      | **Operation-path integrity.** A `JointUseSet` over non-Method members **MUST** be emitted through `G.5-6 DeclareSetResult` from exact already identified `memberRef` values and a current inclusion basis; it **MUST NOT** use `RegisterFamily` or `G.5-3 Select`. `DeclareSetResult` **MUST NOT** be treated as the upstream choice, an actual `Select` application, dated Work, persisted result episteme, or E.24.PUB availability occurrence. |
| `CC-G5.47`      | **G.4 TaskMap receiving boundary.** `TaskMapRef` is required only when this selector uses G.4 CAL gates. Its immutable map edition **MUST** cite the same C.22 `TaskSignatureRef` supplied to selection, resolve one exact `CALCharterRef` and every cited clause, operator, flow, and evidence profile at its exact edition, and travel in result-basis and refresh pins. A mismatch or unresolved ref blocks that gated use. The map **MUST NOT** construct the TaskSignature, copy thresholds, duplicate acceptance semantics, or become mandatory for an ordinary selector with no G.4 gate. |

### G.5:8 - Common Anti-Patterns and How to Avoid Them

* **Anti‑pattern: “Selector as a shadow spec.”**
  *Symptom:* local acceptance or admissibility rules appear in selector prose or code, diverging from CN, CG, and CAL.
  *Avoid:* govern constraint semantics through `CNSpecRef` and `CGSpecRef` plus pinned CAL records; keep G.5 core as a boundary.

* **Anti‑pattern: “Implicit crossings.”**
  *Symptom:* reuse across distinct source-local meanings is claimed from a shared label, Bridge or CL pin, registry row, policy, DRR or SCR line, `GateCrossing`, or `CrossingBundle` without the required relation, use, and reliance facts.
  *Avoid:* resolve the exact F.17 endpoint senses; establish the F.9 Bridge; state the separate C.2.1 `<u,d,r,t,polarity>` claim; require the matching A.10 disposition or B.3 assurance branch; and keep authorization and actual selector use separate. Materialize or cite a bundle only when its named downstream use requires that durable package.


* **Anti‑pattern: “Hidden scalarisation.”**
  *Symptom:* partial orders are flattened into single winners “for convenience”.
  *Avoid:* return declared sets; make dominance regimes explicit; keep telemetry report‑only unless promoted by explicit policy.

* **Anti‑pattern: “Method specifics in the selector head.”**
  *Symptom:* QD, OEE, or preference models become mandatory for basic dispatch.
  *Avoid:* keep them in `G.5:Ext.*` blocks with explicit pins and `Uses`.

* **Anti‑pattern: “Churn by meaning.”**
  *Symptom:* a continuing family id silently resolves different members, grouping basis, or selection pins after a row changes.
  *Avoid:* keep the lineage id only for the continuing declared grouping, publish a new immutable row edition, and carry its exact row ref through selection, result basis, refresh, and deprecation notices.

* **Anti‑pattern: “Result declaration hidden in upstream reasoning.”**
  *Symptom:* the retained alternatives or all-member result exist only as one implication inside `C.11`, `C.19`, or `C.24`, while `G.5` never names the declared result kind.
  *Avoid:* declare the selected-set result directly, with its result kind, applicable members or keyed entries, ordering, named use where required, and basis pins instead of leaving it implicit upstream.

* **Anti-pattern: “Shortlist used for complementary members.”**
  *Symptom:* every named member is needed for one use, but the result calls them alternatives in a `Shortlist`.
  *Avoid:* use `JointUseSet`, name the joint use, and key one entry per exact member; keep direct member relations and actual selection separate.

* **Anti‑pattern: “Declared result missing required content.”**
  *Symptom:* a `Shortlist`, `JointUseSet`, narrowed handoff, or abstain result is named, but the emitted result still omits its members or keyed member entries, ordering, named use where required, or basis pins.
  *Avoid:* state the result kind, retained members or keyed joint-use entries, ordering, named use where required, abstain or escalation condition, and basis pins directly in `G.5`.

### G.5:9 - Consequences

* **Auditable plurality.** Multiple Traditions can co-exist without forced semantic flattening; dispatch remains explainable and evidence-pinned.
* **Core stability.** Universal invariants are pinned through `G.Core`; method innovation and generator innovation do not churn the selector head.
* **Evolvability.** Registries allow growth, retirement, and refresh with typed RSCR causes and explicit payload pins.
* **Composability.** Strategy templates and fallbacks remain admissibility-checked and portable across implementations.
* **Recoverable result content.** Selected-set results can travel downstream as explicit shortlist-family, joint-use, handoff, abstain, or escalation results rather than one hidden implication inside upstream reasoning.

### G.5:10 - Rationale

* **Why registries?** Reusable method-family dispatch requires stable, auditable row editions with explicit eligibility and assurance records, so later uses can recover the grouping and its dispatch basis.
* **Why separation via Extensions?** QD, OEE, preference-learning, and similar families are fast-moving and method-specific; making them part of the selector head would force a universal semantics and violate strict distinction.
* **Why set-return?** Partial orders are common and often the only admissible representation under heterogeneous scales; set-return preserves semantics and makes tie criteria explicit.
* **Why explicit defaults with one declared source?** Defaults are unavoidable; single-source indexing prevents competing defaults from silently diverging across patterns.
* **Why selected-set result declaration here?** Once the current question is to state retained alternatives or an all-member result for downstream use, the selector should declare that result directly instead of leaving it implicit in local choice, pool-policy, or enactment notes written for other purposes.
* **Why `JointUseSet`?** A shortlist preserves alternatives for later choice; an all-member result says that removing one member changes the result for the named use. G.5 mints `JointUseSet` only as a local `SetResultFamily` value and reuses the existing outcome schema and member identities. `G.5-3 Select` may emit it only over exact Method candidates admitted through that kernel; `G.5-6 DeclareSetResult` covers exact already grounded members without retyping them as Methods. Neither branch mints a new U-kind, Method kind, relation kind, or registry kind. `CoUseSet` is less plain, `ComplementarySet` would imply a relation among the members, and `Bundle` would misname a package form.

### G.5:11 - SoTA-Echoing — return what the receiving use can actually select

**Practice question.** What should a dispatcher hand over when several candidates remain useful but the declared comparison does not justify one winner? The selected line returns the admissible alternatives with their ordering status and basis. A serious default chooses one best candidate under a declared objective and returns it ready for use. That default is efficient when the objective settles the choice; it loses a needed alternative when an undeclared scalar objective is substituted for an unresolved trade-off.

The [scikit-learn GridSearchCV documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html), `refit` and `best_estimator_`, supplies the concrete default. It can choose one estimator by a scorer or a custom rule over the evaluation results; multi-metric evaluation still needs a specified refit choice. **Adopt** that explicit-choice requirement when G.5 emits an ordered result. **Reject** reading a single best-estimator interface as a warrant to invent the missing comparator. The library supports custom choices and exposes other candidate results; it does not require G.5 to discard them.

[PS-AAS, Kostovska et al. (2023)](https://proceedings.mlr.press/v224/kostovska23a.html) supplies a substantive alternative-selection line: form a complementary portfolio for later algorithm selection, balancing coverage with the cost of a larger choice problem. Its experiments concern specified CMA-ES variants and BBOB tasks, not arbitrary Methods. **Adapt** the distinction between forming an eligible pool and selecting a member to `Shortlist` and `RankedShortlist` in §4.4b, S3 and the pump case in §0.5. The selected line here is this result discipline, not a claim that PS-AAS is the best portfolio algorithm for every task.

A different receiving use combines members. [Split-Ensemble, Chen et al. (2024)](https://proceedings.mlr.press/v235/chen24aw.html) supplies a concrete counterexample to treating every retained set as alternatives: its submodels serve complementary subtasks in one ensemble. **Adapt** that use distinction to `JointUseSet` and `G.5-6 DeclareSetResult`. G.5 states all-member inclusion; the paper's trained ensemble does not establish compatibility or effective combined use for an arbitrary set of framework editions. Show 4 therefore keeps those claims with their own patterns.

In §0.5 both grounded pump Methods meet the task constraints, but no admitted comparator orders them. With the same candidate evidence, returning the pair as an unordered `Shortlist` preserves the receiving choice at the cost of one further decision. Naming the spectral Method “best” would require an additional criterion and its supporting comparison. If that criterion is supplied and actually orders the candidates, a ranked result is available. If the receiving use includes every exact member, declare that different membership meaning; a ranking does not establish it. These distinctions govern the outcome declarations and the positive, ranked, no-survivor and joint-use cases in §5.

Reopen when new evidence changes eligibility, a comparator supplies or defeats an ordering, the downstream use changes from alternatives to joint inclusion, or keeping the retained set costs more than the receiving decision can bear. A bounded handoff or abstain outcome remains available. None of these sources establishes actual selection Work, a Method's identity, public availability or assurance merely from the emitted result.

### G.5:12 - Relations

**Builds on (normative):** `G.Core` (core invariants + linkage discipline).

**Uses (conceptual dependencies; cited via pins and ids):**

* Specification refs required by this result: `A.19.CN (CN‑Spec)`, `G.0 (CG‑Spec)`. Use `A.2.6` only when a `U.ClaimScope` or selected `U.ContextSlice` changes selection, applicability, or a receiver's justified reliance; validity and evaluation windows and intended-use restrictions follow the same conditional boundary.
* Method identity and family grouping: `A.3.1` for every exact selectable `U.Method`; `A.3.2` only for the same C.2.1 episteme that substantively describes one already admitted Method; and C.2.1 or the defining declaration or pattern for the family relation cited by a registry row. G.5 creates none of those source facts.
* Method composition and selected organization: `B.1.5` for the complete composite-Method qualification, `A.22` for an independently selected organization that does not constitute one Method, and `C.29` for algebraic, graph, matrix, embedding, neural, or other representation-lens use. G.5 consumes exact resulting references and does not construct them.


* Upstream object sets: `G.1 (CG‑Frame Card)`, `G.2 (SoTA Pack)`, `G.3 (CHR Pack)`, and `G.4 (CAL Pack)`. C.22 alone constitutes the TaskSignature. When G.4 CAL gates are current, G.5 additionally consumes the exact `TaskMapRef` that relates that same `TaskSignatureRef` to one exact charter and the cited CAL declarations; otherwise the map is absent.
* Evidence and crossings: `G.6` for EvidenceGraph citations; `F.17` for exact local senses; `F.9` for the direct Bridge; C.2.1 for the separate bounded-use proposition; and `A.10` or `B.3` for reliance or assurance. Add a `CrossingBundle` under `E.18` or a GateCheck under `A.21` only when that named downstream use requires one. A G.7 calibration artifact remains a cited policy or evidence input; it does not define the Bridge, bounded use, reliance, or selector actuality.

* Planning and enactment boundary: `A.15.2` identifies the `U.WorkPlan` used as `plannedBaselineRef`; A.15.3 defines any planned-filling rows kept inside that WorkPlan. G.5 does not redefine them.
* Actual selector use and result availability: `A.19.SelectorMechanism` and A.6.1 for the actual `Select` application and bindings; A.13 for every precise performer's local-kind criterion, classification, same obtaining assignment, scope, situation, window, and evidence; A.15.1 for independent Work admission; A.2.1 for the assignment species and occurrence; and F.6 only for a current exact assignment-bound attribution. When asserted by the account or consumed by its receiving use, A.2.4 governs evidence use, A.10 governs reliance and provenance, G.11 governs currentness, C.2.1 governs a persisted result episteme, B.3 governs assurance, the direct authority pattern governs authorization, and E.24.PUB governs publication. Upstream CPM applications retain their local bindings without requiring separately admitted comparison Work unless that Work is asserted. A root-family assignment reference, temporal overlap, or omission from short wording supplies no attribution and removes no world-side fact. G.5 declarations and records create none of those neighboring facts.
* Joint-use members outside Method dispatch: the direct identity pattern identifies every `memberRef`; `C.11` supplies a local choice result when one is current; another accepted decision or governed inclusion basis may establish all-member inclusion; E.4.PFR states framework-edition dependency or pairwise compatibility separately; `G.11` supplies currentness; and E.17/E.24.PUB plus the applicable access-carrier pattern supply exposure and source return. `G.5-6 DeclareSetResult` consumes the exact members and sufficient basis pins and emits only the selector-facing membership result.

* Causal-use method dispatch: `C.28` when method selection involves causal effect, counterfactual comparison, causal fairness, causal policy, causal RL, or simulation-only causal-use claims.
* Optional Method or generator extensions through `G.5:Ext.*`: `C.18`, `C.19`, `C.23`, plus extension-bearing patterns whose exact Part G admission relation is established when they add extra selector pins.
* Mathematical-lens use: apply `C.29` when a selector input depends on a mathematical object or mapping whose use is not yet recoverable—for example, a comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, QD archive descriptor, model-family label, or model-selection basis. For claim-bearing lens use, recover that object's mapping mode, preserved or lost structure, and stop condition. A `LensCandidateNote` may instead retain the recognition and next-action account while `CandidateMathObject?` remains unresolved. The recorded result is a C.29 lens-use result; non-exhaustive examples include no lens use, a lens-candidate note, a one-line note, a mini-card, a full card, or a note naming the applicable pattern for the stated selector use. That result does not declare a selector result or its supporting records, such as the selected set, selector policy, registry row, shortlist, ranked shortlist, or selector evidence pins; use `G.5` for those objects and cite the exact references used.

**Provides to:** downstream uses such as `G.6` audit citations, RSCR emission records with typed triggers and payload pins, and packs shipped through `G.10`. When a named use needs stable public identity, publish the required family ids, selector policy records, or selected-set identities—such as `ShortlistId`—to `UTS` under the applicable identity rule.

**Coordinates with:** `C.11` for local choice results; E.4.PFR for direct framework-edition dependency and pairwise compatibility claims; G.11 for edition currentness; E.17 for a source-backed publication face and return to source; E.24.PUB for a publication occurrence and audience availability; `C.19` for pool-policy records; `C.32.P2S` when a selected-set result declaration feeds architecture problem-to-structure carry-through; `C.35` when a generated or discovered structure-bearing output is not yet a selector-facing result; `C.24` for enactment-facing next-action records; and `C.18` when a `Front` or `Q-front` is the source set for a G.5 use.

A `Q-front` stays a C.18 source set; it is not the emitted G.5 outcome or a `SetResultFamily`. The G.5 result states one admitted `SelectorOutcomeKind`; a set result also states `Shortlist`, `RankedShortlist`, or `JointUseSet`, and any public selected-set label resolves to that family.

Architecture discovery boundary: when a generated or discovered structure-bearing output is only a representation or carrier—for example, a description, query result, graph, cluster, or search trace—use `C.35` before G.5. Use G.5 only when the live claim is declaration of selected-set result content with selector-policy and selected-set identity; stable public identity and actual publication remain conditional neighboring branches.

### G.5:End

## G.6 - Evidence Graph and Provenance Ledger: Citable Evidence-Provenance Paths

> **Type:** Evidence and provenance pattern
> **Status:** Stable
> **Normativity:** Normative where conformance rows say so; examples and SoTA rows are informative guidance.

### G.6:1 - Problem Frame

Use this pattern when a later user must cite, replay, audit, or refresh a path through several already established objects and relations rather than repeat their complete source account.

Use it when the working question is:

* which admitted dated Work occurrences and A.13-qualified actual performer Systems must remain addressable, together with already-established F.6 attribution refs only when the selected path expressly consumes precise assignment-bound attribution, and any local system-role kind or assignment identifier that the path separately uses;
* which direct participation or binding facts, produced entities, domain results, result epistemes, outcomes, source publications, carriers, and provenance relations must remain addressable;
* which exact direct relations connect those objects, which pattern defines or constrains each relation, and whether each relation is already established as obtaining;
* which bounded context, reference plane, time window, bridge, edition, policy, source-currentness result, or reliance boundary limits the cited path;
* which downstream work and exact use relation may cite the path; and
* what stronger conclusion, assurance, permission, acceptance, gate passage, or decision the path does not carry.

**Primary EntityOfConcern.** The primary `EntityOfConcern` is an addressable provenance representation: one `EvidenceGraph`, its `PathId` or `PathSliceId`, and any ledger entry that makes the path replayable. G.6 governs path identity, slicing, citation, and local refresh. It does not create the represented work, participation, production, result, episteme, outcome, source, currentness, reliance, or representation correspondence.

**First useful move.** Name the relied-on claim or bounded use, then list the exact object refs and direct relation refs needed to replay it. For every relation record its direct governor and obtaining claim. Only then draw the path. Keep an unresolved relation as a gap; do not turn it into a graph edge asserted as obtaining.

**What goes wrong if missed.** A tidy graph makes an unperformed method look like Work, a co-listed System or entity look like a participant or Work performer, a carrier look like a produced result, a measurement or verdict look like generic evidence, or a provenance edge look like the world-side relation itself.

**What this buys.** Downstream work can cite one stable path while a reviewer can still recover the exact work, participants, products, subject results, result epistemes, sources, direct relations, currentness, and bounded use that the path represents.

**Not this pattern when.** Use `A.2.4` for the first evidence-use or status-use classification, `A.10` for source recovery and bounded reliance, `A.15.1` and `F.6` for performed Work and its attribution, `A.2.1` only when an assignment occurrence itself is current, `A.6.1` for actual operation bindings, `A.15.PROD` when production or inception is current, the exact domain pattern for its local result, `C.2.1` for the result episteme, `G.11` for currentness, `C.29` for representation correspondence, and `B.3` for assurance. If only one local source-to-use statement is needed, stay in A.10.

Here `path` means a path in a descriptive provenance graph. It is not an action route, method, workflow, transformation flow, universal evidence relation, or generic work-result relation.

### G.6:2 - Problem

Large projects often need to cite a chain that crosses measurement, evaluation, aggregation, production, publication, and later use. The chain becomes unsafe when the graph is allowed to supply facts missing from the governed objects.

The common failures are:

1. **Edge-to-fact inversion.** A drawn edge is treated as proof that work, participation, production, measurement, evaluation, or use occurred.
2. **Generic relation fallback.** Labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` replace the exact direct relation and its governor.
3. **Result collapse.** Subject result, result episteme, carrier, outcome, assurance, and later decision become one generic result node.
4. **Declaration-to-runtime collapse.** A `MethodDescription`, operation signature, policy, clause, or plan is read as an actual run and its bindings.
5. **Hidden crossing.** A path silently crosses context, reference plane, edition, source order, or currentness window.
6. **Refresh fanout.** One changed source or relation forces a global rerun because the smallest affected path slice cannot be found.

### G.6:3 - Forces

| Force | Tension this pattern resolves |
| --- | --- |
| Compact citation versus the represented facts' governing rules | One path is easy to cite, but each represented fact and relation must remain with its exact governor. |
| Graph readability versus ontic force | Nodes and edges make a chain legible; their presence cannot make any represented relation obtain. |
| Result continuity versus result collapse | A path may connect measurement, evaluation, aggregation, and decision while preserving every local result and result episteme. |
| Reusable declaration versus performed occurrence | Methods, descriptions, policies, and clauses may be cited, but dated work and actual bindings remain separate. |
| Cross-context reuse versus hidden loss | Bridges, editions, time windows, source order, and currentness remain visible at the path slice that depends on them. |
| Refresh locality versus stale reliance | Stable addresses let one changed object or direct relation reopen only the affected path or slice. |

### G.6:4 - Solution — cite independently governed objects and relations

Create an `EvidenceGraph` only after the relied-on claim or bounded use and its supporting objects have been recovered. The graph is a declarative, addressable representation. Each node record cites one independently governed object; each asserted edge record cites one independently established direct relation. `PathId`, `PathSliceId`, and the provenance ledger add citation and refresh locality, not world-side facts.

#### G.6:4.1 - Subject-pattern map

| Represented claim or object | Subject pattern before G.6 represents it |
| --- | --- |
| Reusable method, generic participants, parameters, effects, and conditions | `A.3.1` for the exact `U.Method`; `A.3.2` for its `U.MethodDescription` |
| Independently admitted dated Work and its exact actual performer refs; optional obtaining F.6 relation and assignment occurrence refs when the path expressly consumes attribution; enactment, resources, and direct participation or binding facts | `A.13` for each exact actual performer and `A.15.1` for independent Work admission; `F.6` and `A.2.1` only when the path represents precise assignment-bound attribution; the exact direct participation or resource relation; and `A.6.1` for operation-application bindings |
| Production or inception of an entity or episteme | one exact local A.15.PROD claim when its entry condition is met, or a direct subject predicate under its own pattern |
| Measurement result and its measurement-specific basis | `C.16` |
| Acceptance-clause application or other runtime evaluation result | `G.4` or the exact formal, conformance, diagnostic, causal, comparison, selection, gate, or decision governor |
| Work-resource aggregation result | `B.1.6` |
| Durable episteme that states a local result | `C.2.1`; it remains distinct from the domain result |
| Outcome, later action, acceptance, gate passage, permission, or decision | its exact work and domain governor, including `C.11` or `A.21` when applicable |
| Source publication, carrier, copy, extraction, or publication occurrence | `E.17` for a source-backed face and source return; `E.24.PUB` for an obtaining publication occurrence; the direct rule for each copy, extraction or source relation |
| Representation correspondence | `C.29` |
| Bridge, congruence, loss, or cross-context transfer | `F.9` |
| Transformation-flow structure distinct from performed work | `E.18` and `E.18.2` |
| First evidence/status use, provenance and bounded reliance, currentness, or assurance | `A.2.4`, `A.10`, `G.11`, or `B.3` respectively |

G.6 does not substitute for any row. If the subject pattern or relation cannot be recovered, the path records an unresolved gap and cannot present that edge as obtaining.

Do not add a local `U.EvidenceRole` or turn proof, measurement, benchmark, source, or status labels into system-role kinds. For any claim that a producer, verifier, laboratory, issuer, or maintainer participates, recover the exact direct relation, the participants it declares, and the place each actual participant fills. Other nearby facts—for example, a local system-role kind, assignment, Work occurrence, responsibility, authority, or permission—are separate and may be cited only when they independently obtain; none establishes participation. Do not infer that a passive laboratory or produced entity performs Work merely because the path cites it.

**Work recovery and compact citation.** Before G.6 represents dated `U.Work`, its subject account must already recover each exact actual performer through A.13 and admit that Work independently under `A.15.1`. Include an assignment occurrence and obtaining F.6 relation only when the graph path or receiving use expressly consumes precise assignment-bound attribution; any present attribution must use the same obtaining A.13 assignment. If a required Work or performer ref is absent, record a Work gap. If an expressly consumed F.6 ref is absent or unresolved, retain the Work node and record an attribution gap rather than suppressing the Work. G.6 neither re-admits the Work nor retests assignment species, occurrence identity, holder, classification, predicate duration, or interval coverage. Merely listing an assignment beside Work establishes no relation between them.

#### G.6:4.2 - EvidenceGraph as a representation

An `EvidenceGraph` is a typed directed graph used for provenance citation and replay. It may project a dependency-closed slice of independently governed objects and relations. It is not a holarchy, work plan, method, transformation flow, result algebra, or proof that its contents obtain.

Minimal graph fields:

```text
EvidenceGraph:
  EvidenceGraphId
  ReliedOnClaimOrBoundedUseRef
  BoundedContext
  ReferencePlane
  RepresentedNodeRecords
  RepresentedRelationEdgeRecords
  TimeWindowOrPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  GraphPathAddressingRule
  C29RepresentationRefs
```

A node record is a projection, not a new universal object kind:

```text
RepresentedNodeRecord:
  GraphNodeId
  RepresentedObjectRef
  ObjectKindAsGoverned
  SubjectPatternLocator
  ContextEditionOrTimeQualification?
  RepresentationRef
```

The node set may cite exact Work occurrences and their A.13-qualified actual performer Systems. It may also cite local system-role kinds, assignment occurrences whose identities the path uses, obtaining F.6 relations when precise attribution is expressly consumed, direct participation and binding facts, produced entities, subject results, result epistemes, outcomes, sources, carriers, currentness results, reliance dispositions, and later Work. Every cited Work occurrence uses the independently established performer and A.15.1 Work refs described in §4.1; F.6 refs are optional and never discover the performer. Co-listing creates no relation among these objects.

An asserted edge is also a projection:

```text
RepresentedRelationEdgeRecord:
  GraphEdgeId
  DirectRelationRef
  DirectRelationKindRef
  ActualParticipantRefs
  SubjectPatternLocator
  ObtainingClaimRef
  ContextEditionOrTimeQualification?
  RepresentationRef
```

Before the edge enters a relied-on path, the exact direct relation must already be established under its governor. The participant refs in the edge must match that relation; adjacency, direction, shared identifiers, timestamps, source order, or visual layout cannot supply them. `RepresentationRef` points outward to the applicable C.29 correspondence when that correspondence is current.

G.6 defines no fallback core edge vocabulary. Legacy or display labels such as `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, `derivedFrom`, `usesMethodDescription`, `citesSource`, or `evidences` are navigation prompts only. Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, premise, reference, argument, or other direct relation before asserting the edge as obtaining.

#### G.6:4.3 - PathId and PathSliceId

A `PathId` identifies one claim-local path inside an `EvidenceGraph`. A `PathSliceId` identifies the same path under a declared time window, reference plane, bounded context, edition, bridge, policy, or selected object/relation subset.

Use this compact record:

```text
PathCitationRecord:
  ReliedOnClaimOrBoundedUseRef
  EvidenceGraphRef
  PathId
  PathSliceId
  BoundedContext
  ReferencePlane
  RepresentedObjectRefs
  RepresentedDirectRelationRefs
  SubjectPatternLocators
  SourcePublicationAndCarrierRefs
  C29RepresentationRefs
  TimeWindowOrFreshnessPolicy
  SourceCurrentnessRefs
  BridgeOrLossRefs
  EditionOrPolicyRefs
  DownstreamWorkRef?
  ExactDownstreamUseRelationRef?
  A10RelianceDispositionRef?
  NotCarried
  UnresolvedRelationGaps
  ReopenTrigger
```

`NotCarried` names the stronger claim or use at issue that the path does not establish. Recover the exact premise, reference, operation-argument, decision-use, or other direct relation for actual downstream use. If the use asserts dated `U.Work`, cite its independently admitted A.15.1 Work ref and A.13-qualified performer refs. Add attribution refs only when the use expressly consumes precise assignment-bound attribution. Path availability or citation alone does not establish that use.

#### G.6:4.4 - Provenance ledger

A `ProvenanceLedger` is a citable replay index over `PathCitationRecord` entries. It is not a work-progress log, result registry, review-comment log, process-status log, or ontic source.

```text
ProvenanceLedger:
  LedgerId
  EvidenceGraphRef
  PathCitationRecords
  RepresentedObjectIndex
  RepresentedDirectRelationIndex
  SourceOrderPolicy
  CurrentnessPolicy
  PrivacyOrDisclosureBoundary
  RefreshScopeRule
```

The ledger may cite work, participants, produced entities, domain results, result epistemes, outcomes, sources, transformations, representation correspondences, provenance, and later uses. A row establishes none of them. Use a ledger when several downstream consumers need the same path family; do not create one merely because a local A.10 account is easy to write.

#### G.6:4.5 - Refresh and source return

Reopen the smallest affected `PathId`, `PathSliceId`, node projection, or relation-edge projection when any cited object, direct relation, governor, source, bridge, representation correspondence, edition, policy, time window, currentness result, or reliance boundary changes.

If the direct relation no longer obtains or its proof becomes unavailable, remove it from the relied-on path or mark the exact unresolved gap. Do not preserve the edge from graph history, infer a replacement relation, rerun unrelated paths, or certify a new downstream result through refresh alone.

#### G.6:4.6 - Declarative representation discipline

`EvidenceGraph`, `PathId`, `PathSliceId`, and `ProvenanceLedger` tell a reader which already governed account is being cited. They do not tell a worker what to do and they do not reconstruct missing world-side facts.

| Current phrase or artifact | Required recovery before G.6 representation |
| --- | --- |
| method, protocol, algorithm, clause, or policy | exact reusable declaration; when the path cites dated Work, recover it separately under §4.1; when it cites actual operation bindings, recover them under A.6.1 |
| work trace, run, test, audit, measurement, or evaluation | independently admitted dated Work ref and A.13-qualified actual performer refs under §4.1; enacted Method, resources, exact direct participation facts, and A.6.1 binding facts remain separate; expose an assignment occurrence and obtaining F.6 relation only when the path expressly consumes precise assignment-bound attribution |
| produced carrier, model, report, or episteme | exact produced entity and either its subject-specific direct production relation, when the subject pattern declares one, or the one local A.15.PROD production-work or inception claim that the current use needs |
| reading, score, verdict, estimate, aggregate, diagnosis, or outcome | exact domain result and direct governor; distinct C.2.1 episteme when durably stated |
| publication, view, export, or graph rendering | exact source relation, E.17 source-backed face, E.24.PUB publication occurrence, and C.29 representation correspondence when each is current |
| evidence, provenance, currentness, reliance, or assurance | A.2.4/A.10, G.11, and B.3 under their separate entry conditions |
| later acceptance, gate, release, or decision | its local result and exact later-use relation under their direct rules; dated Work admitted under §4.1 when that occurrence is asserted |

#### G.6:4.7 - Extension wiring without core drift

Selector, benchmark, assurance, refresh, or telemetry patterns may require additional pins in `PathCitationRecord`. They may cite `PathId` or `PathSliceId`, but they do not mint a universal edge, result, evidence, or criterion-participant relation. Any added graph record still names the exact represented object or direct relation and its governor.

`G.5` may cite a path for selector explanation, `G.9` for benchmark replication, `G.11` for local refresh, and B.3 for an assurance input. Their selection, benchmark, currentness, and assurance results remain their own.

### G.6:5 - Archetypal Grounding

#### G.6:5.1 - Measurement, acceptance, and decision

C.16 dated measurement work binds the pressure measurand, detector, calibration, model, input quantities, and uncertainty propagation and obtains a pressure measurement result. A distinct C.2.1 episteme states that result. Later G.4 `EvaluationWork` applies one declared acceptance clause through exact A.6.1 bindings and obtains `unknown`; another C.2.1 episteme states that verdict. Later C.11 decision work uses the verdict episteme through an exact premise relation and defers.

G.6 may give this chain one `PathId` only after the measurement, work, binding, result, episteme, clause-application, premise, and decision relations are independently established. Its nodes keep raw detector output, indication, actual pressure, measurement result, verdict, and decision distinct. Its edges cite the exact relations; none produces the work, verdict, or decision.

#### G.6:5.2 - Resource aggregation

An engine programme has several C.16 resource measurements, dated test-run work occurrences, exact phase and overlap relations, and a shared warm-up allocation rule. B.1.6 dated aggregation work applies `ProgrammeResourcePolicy-v3` and obtains a typed resource vector with propagated uncertainty; a distinct C.2.1 episteme states it.

The G.6 path cites every measurement result and episteme, the work-set and overlap relations, the edition-pinned policy, aggregation work, aggregation result, sources, and representation refs. Epoch labels alone do not establish work-part relations. Warm-up energy allocation and uncertainty propagation are performed in the aggregation work; an emissions verdict remains a separate result.

#### G.6:5.3 - Produced model and benchmark use

Dated training work has exact actual bindings and, when an inception or completion claim is current, one local A.15.PROD claim. Separate benchmark-evaluation work applies its declared method and dataset edition and obtains a result under the benchmark's direct governor; a C.2.1 episteme states that result. E.17 governs the model card's source-backed face and return to the selected claims, E.24.PUB their actual audience availability, and C.29 any consumed representation correspondence. G.11 supplies currentness when later use depends on edition or freshness.

A G.6 `PathSliceId` may cite that dependency chain for replication. The graph does not infer training from the model's presence, participation from a roster, evaluation from the protocol, superiority from the score, or deployment permission from the model card.

#### G.6:5.4 - Dashboard status cue

A dashboard cell shows `Ready`. F.10 governs the status-use classification; A.10 recovers the source and provenance for bounded reliance, with query Work, currentness, and a live rival explanation when those facts affect the claim. G.6 is entered only when a downstream audit or release package needs a stable path through those already established relations. The visible cue, graph path, and ledger row establish neither gate passage nor release.

### G.6:6 - Bias-Annotation

| Bias | Guard |
| --- | --- |
| Graph-authority bias | A node or edge represents an object or direct relation only after that object or obtaining relation has been independently established under its governing rule. |
| Generic-edge bias | Reject fallback `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, and `evidences` relations; recover the exact direct relation. |
| Result-node bias | Keep subject result, result episteme, carrier, outcome, assurance, and later action distinct. |
| Declaration-runtime bias | A method, description, policy, clause, signature, or plan establishes no occurrence or actual binding. |
| Provenance-as-truth bias | Origin and history support only their named bounded claim; provenance is not truth, safety, approval, or assurance. |
| Path-as-workflow bias | Graph path identity supports citation and refresh; actual work and transformation flow retain their subject patterns. |
| Ledger-process bias | The ledger contains replayable provenance records, not campaign status, review proof, or work-progress notes. |

### G.6:7 - Conformance Checklist

| ID | Check | Repair if missing |
| --- | --- | --- |
| `CC-G6-01` Exact use | Is one relied-on claim or bounded downstream use named? | Name it, or stay in local A.10 source recovery. |
| `CC-G6-02` Object projection | Does every node cite an exact independently governed object, kind, governor, qualification, and representation ref? | Recover the object or record an unresolved gap; do not mint a graph-only world object. |
| `CC-G6-03` Relation prerequisite | Does every asserted edge cite one exact direct relation, its actual participants, governor, obtaining claim, and context? | Establish the direct relation first or remove the edge from the relied-on path. |
| `CC-G6-04` No fallback edge | Are legacy or display labels prevented from acting as universal relations? | Replace each with the exact formal, measurement, work, production, publication, representation, provenance, temporal, status-use, or later-use relation. |
| `CC-G6-05` Work boundary | Does each represented Work cite one independently admitted A.15.1 Work ref and its A.13-qualified actual performer refs? Are assignment occurrence and F.6 refs included only when the path expressly consumes precise assignment-bound attribution, with a missing attribution recorded as a gap rather than loss of the Work node? Are Method, MethodDescription, resources, direct participation, and A.6.1 bindings still separate? | Use A.13 and A.15.1 for the already-established performer and Work. Cite A.2.1/F.6 only for an expressly consumed attribution, A.6.1 for actual operation bindings, and the exact direct relation for every other participant claim. |
| `CC-G6-06` Result boundary | Are produced entity, subject result, result episteme, carrier, outcome, assurance, and later action distinct and independently identified under exact predicates? | Handle each through the exact predicates and assertions located in A.15.PROD, the domain result pattern, C.2.1, E.17/E.24.PUB/C.29, B.3, or the later-action source. |
| `CC-G6-07` Source and representation | Are source publication, carrier, copy/transform chain, and C.29 correspondence explicit when current? | Recover those relations before treating the graph rendering as source truth. |
| `CC-G6-08` Time and crossing | Are bounded context, plane, window, bridge/loss, edition, policy, source order, and G.11 currentness visible where they limit use? | Add the exact refs or narrow/block the path slice. |
| `CC-G6-09` Provenance and use | Are A.2.4/A.10 evidence/status use, A.10 provenance/reliance, downstream work, and exact use relation separate? | Recover the direct use; path citation or membership is not actual reliance. |
| `CC-G6-10` Ledger boundary | Does the ledger merely index already established objects and relations, with `NotCarried`, gaps, and local reopen triggers? | Remove process status, generic result fields, and fact-creating language. |

### G.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Edge as fact | Drawing or storing an edge is mistaken for an obtaining relation. | Establish the exact direct relation under its governor, then cite it through a representation record. |
| Universal evidence edge | `verifiedBy`, `validatedBy`, `measuredBy`, `producedByWork`, or `evidences` absorbs several relation families. | Replace the label with the exact formal, measurement, work, production, source, use, or other direct relation. |
| MethodDescription as run trace | Generic declarations acquire actual participants, time, or results by graph membership. | Cite one independently admitted dated Work ref and its A.13-qualified actual performer refs through §4.1. Keep Method enactment, resources, direct participation, and A.6.1 bindings separate; expose an assignment occurrence and F.6 relation only when the path expressly consumes precise assignment-bound attribution. |
| Generic result node | Measurement, evaluation, aggregation, episteme, outcome, and decision collapse. | Keep each local result under its domain governor and each durable assertion under C.2.1. |
| Provenance as result or assurance | A path or ledger row is read as truth, currentness, safety, permission, or acceptance. | Use A.10, G.11, and B.3 under their entry conditions, and state the exact local result under its applicable predicate and pattern. |
| Citation as actual use | A downstream record cites a path and is assumed to have used it. | Establish the exact premise, reference, argument, or decision-use relation; recover dated Work separately under §4.1 when the claim asserts that occurrence. |
| Workflow overread | A declarative path becomes a method or action route. | Handle Work under A.15.1 and transformation-flow structure under E.18; limit G.6 to representation and citation. |
| Global refresh | One changed source or relation reopens every graph. | Reopen only the affected path, slice, node projection, or relation-edge projection. |

### G.6:9 - Consequences

Benefits:

* downstream records cite evidence-provenance paths without copying evidence tables;
* source, bridge, policy, edition, and time changes reopen the smallest path slice;
* evidence, assurance, causal use, status, gate, work, and publication claims stay in their subject patterns;
* provenance becomes replayable and privacy-minimizable through scoped refs.

Costs:

* path identity, node typing, and source-currentness refs add overhead;
* graph paths can look like routes unless declarative representation discipline is kept visible;
* users must resist treating one complete path as a complete downstream decision.

### G.6:10 - Rationale

A.10 recovers one relied-on claim, its source/provenance account, and bounded reliance. G.6 adds stable graph-path identity, slicing, shared citation, and path-local refresh when several downstream consumers need the same dependency-closed representation.

That representational gain does not justify a second ontology of evidence edges. Work, participants, products, subject results, result epistemes, outcomes, sources, provenance, currentness, and later uses already have direct governors. G.6 therefore projects their exact refs and direct relations, and C.29 governs the representation correspondence when current. This makes a complex chain readable without allowing graph topology to create facts.

The ledger is likewise an index over established provenance, not a result store or process log. Missing relation evidence remains a visible gap; it is never repaired by drawing a more persuasive path.

### G.6:11 - SoTA-Echoing

The source-use decisions below are based on the publishers' source versions current on 2026-07-30. These decisions remain qualified through 2027-07-30 unless a new Recommendation, specification edition, maintenance status, or replacement changes the adopted contract earlier. Internal FPF neighbour authority stays in Relations; it is not presented as an external source decision.

| Exact source and source-use decision | Visible G.6 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [W3C PROV-O, Recommendation 30 April 2013](https://www.w3.org/TR/prov-o/) — **adapt** qualified provenance descriptions and stable entity/activity/agent references only as a representation discipline for exact FPF objects and direct relations. | `RepresentedNodeRecord`, `RepresentedRelationEdgeRecord`, the measurement-to-decision case, and `CC-G6-02/03` require every node and edge to cite an independently governed object or obtaining relation with its governor and qualification. | A PROV-shaped class, activity, agent, qualified association, or derivation does not establish FPF work, participation, production, result, truth, currentness, or later use. | Reopen only §4.2's node/edge rules, the measurement-to-decision path, and `CC-G6-02/03` if PROV-O's qualified-relation contract changes. |
| [C2PA Content Credentials Technical Specification 2.4, April 2026](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) — **adapt** asset/manifest identity, claim generator, assertions, ingredients/actions, signature validation, trust policy, and specification version for claim-bound content provenance. | `PathCitationRecord` carries source publication/carrier, C.29 representation, edition/policy, currentness, and `NotCarried`; the produced-model case and `CC-G6-07/08` retain the exact content carrier, transform chain, trust regime, and version. | A valid manifest, visible Content Credential, ingredient chain, or authenticity mark does not establish truth of the represented world state, authorship beyond its exact assertion, work, safety, permission, or adequacy. | Reopen only those `PathCitationRecord` source/version fields, the produced-model carrier slice, and `CC-G6-07/08` when C2PA changes manifest/assertion identity, validation, trust, or version semantics. |
| [SLSA specification v1.2](https://slsa.dev/spec/v1.2/) with [in-toto Attestation Framework v1.2 and `Statement/v1`](https://github.com/in-toto/attestation/blob/main/spec/README.md) — **adapt** artifact subject, predicate type, producing context, inputs, authenticated envelope, verifier expectation, and versioned attestation separation. | The produced-model/benchmark path names training work, produced model edition, dataset/method edition, benchmark work/result, source inputs, publication/carrier, verifier context, and currentness; `CC-G6-07/08` keep those refs replayable without one generic attestation edge. | A signed statement, provenance predicate, SLSA level, or verification summary does not prove an uncited build/work/result relation, benchmark superiority, runtime safety, release approval, gate passage, or assurance. | Reopen only the attestation-bearing fields of that path slice, the produced-model/benchmark case, and `CC-G6-07/08` when the adopted SLSA provenance/verification contract or in-toto `Statement/v1` semantics change. |
| [W3C Verifiable Credentials Data Model 2.0, Recommendation 15 May 2025](https://www.w3.org/TR/vc-data-model-2.0/) — **adapt** credential subject, issuer, holder, verifier, status, context, and validity separation for a path that cites an independently governed credential/status use. | `PathCitationRecord` separates source/carrier/currentness refs, downstream work, exact use relation, A.10 reliance disposition, and `NotCarried`; the dashboard-status case and `CC-G6-09` require the status cue, query/use work, verifier or relying context, and actual reliance to remain distinct. | A valid credential, successful proof check, holder presentation, status value, or graph membership does not become claim truth, authorization, permission, gate passage, release, actual reliance, or assurance. | Reopen only those credential/status/use fields, the dashboard-status path, and `CC-G6-09` if VC 2.0 or its adopted status/validity contract changes. |
| Pineau et al., [*Improving Reproducibility in Machine Learning Research*, JMLR 22(164), 2021](https://jmlr.org/papers/v22/20-303.html), and Mitchell et al., [*Model Cards for Model Reporting*, FAT* 2019](https://doi.org/10.1145/3287560.3287596) — **adapt** exact method, dataset, metric, evaluation condition, version, limitation, and run-evidence disclosure as inputs to a replayable benchmark path. | The produced-model/benchmark case, dependency-closed `PathSliceId`, and `CC-G6-02/07/08` keep model edition, training/evaluation work, dataset and method editions, local result, result episteme, source carrier, limitations, and currentness separately addressable. | A reproducibility checklist, model card, disclosed score, or limitation does not establish that training or evaluation occurred, that the reported result is current, that one model is superior, or that deployment is permitted. | Reopen only the model/benchmark slice fields, that worked case, and `CC-G6-02/07/08` if the adopted reproducibility or reporting contract changes. |
| [ISO/IEC/IEEE 15026-2:2022, *Systems and software assurance — Part 2: Assurance case*](https://www.iso.org/standard/80625.html) — **adapt** the separation between cited evidence and the structure, maintenance, and evaluation of an assurance case. | `NotCarried` names assurance explicitly, the subject-pattern map and §4.7 handle assurance under B.3, and `CC-G6-10` permits the ledger to index evidence paths without becoming an assurance result. | A complete-looking evidence path, ledger entry, confidence label, or signed carrier is not an assurance claim, safety result, readiness result, compliance result, or release confidence. | Reopen only `NotCarried`, the B.3 extension boundary, one assurance-input path, and `CC-G6-10` if the adopted assurance-case evidence or maintenance boundary changes. |

Source refresh is local: replay the changed row's named record fields, rule or case, and checklist rows first. Widen only when that replay contradicts another current G.6 locus; a changed source cannot by itself create a represented object, obtaining relation, work occurrence, result, currentness, reliance, assurance, permission, or decision.

### G.6:12 - Relations

* **Builds on:** `A.10` for source recovery, provenance, bounded reliance, and graph-edge discipline; `A.2.4` for first-use evidence/status classification; `C.2.1` for claim and result epistemes; `C.29` for representation correspondence.
* **Coordinates with:** `A.13` and `A.15.1` for already-established exact actual performers and Work; `F.6` and `A.2.1` only when the receiving path expressly consumes precise assignment-bound attribution; `A.6.1` for actual operation bindings; the exact pattern for each participation relation; `A.15.PROD` for production or inception when current; `C.16` for measurement results; `G.4` for runtime evaluation results; `B.1.6` for work-resource aggregation results; `C.28` for causal use; `F.10` for status use; `F.9` for bridge and loss; `E.18` and `E.18.2` for transformation-flow structure; `G.11` for currentness; `B.3` for assurance; `E.17` for source-backed faces and return to source; `E.24.PUB` for obtaining publication occurrences; and the pattern that defines each exact formal, diagnostic, conformance, comparison, selection, acceptance, gate, permission, commitment, or decision claim cited by a path.
* **Used by:** selector, benchmark, replication, audit, refresh, assurance, maturity, and release patterns that need stable provenance-path citation, including `G.5`, `G.9`, and `G.11`.
* **Does not govern:** any represented work occurrence, participation, production, local result, result episteme, outcome, source publication, representation correspondence, currentness result, assurance, later use, or stronger conclusion named in `NotCarried`.

### G.6:End

## G.7 - Cross‑Tradition Bridge Calibration Kit (BridgeMatrix → BridgeCards + BCT/Sentinels)

> **Status:** Stable

**Tag.** Architectural pattern
**Stage.** design‑time (calibration + publication) + run‑time (sentinel‑driven telemetry emission; orchestration governed by **G.11**)
**Start here.** Name the correspondence to be calibrated and the question of the receiving use, if one is already known. Recover its exact endpoints and governing relation, then state the evidence, preserved distinctions and losses. The first useful result is a bounded calibration statement; its suitability for a receiving use requires that use’s own rule, loss tolerance and reliance. Add the kit fields below when calibrated values or published, refreshable calibration records are needed. For a bounded reuse needing neither, follow the correspondence’s direct rule instead (F.9 for senses, C.3.3 for kinds, or the named plane rule).
**Primary output.** A calibration kit with a `BridgeCalibrationTable (BCT)`, `CalibrationLedger`, `RegressionSet` and `SentinelSet`. Each row cites the actual sense, kind or plane correspondence being calibrated. F.9 rows carry BridgeCards; public naming and real flow/gate crossings add their required UTS or bundle anchors. Sentinel triggers carry the affected references and live scope.
**Primary hooks.** `G.Core` (Part‑G invariants + RSCR trigger catalogue + Default Governing Definition Index), **G.2** (BridgeMatrix), **F.9** (BridgeCard + CL), **C.3.3** (KindBridge + CL^k when the kind channel is used), **F.3** (source-local sense clustering), **F.17** (SenseCell anchoring), **F.7** (source-local comparison display), **E.18/A.21** (GateCrossing + CrossingBundle checks), **G.6** (PathId/PathSliceId citation surface), **G.5** (downstream consumer for eligibility/selection), **G.11** (refresh orchestration consumer), **B.3** (assurance lanes + penalty policies), **C.21** (DHC accounts such as AlignmentDensity), **C.18 and C.19** (QD/OEE pins when relevant), **C.23** (SoS‑LOG clauses as explainability gates for cross‑Tradition choices), **G.4** (Acceptance hooks/thresholds when bridges are used as selector gates), **E.10** (LEX / strict distinction discipline).
**Working‑Model first.** Prefer a minimal, auditable calibration procedure and worked micro‑cases; escalate to heavier harnesses only where risk warrants (per **E.8**).
**Non‑duplication note.** Universal Part‑G invariants (no shadow specs; Bridge‑only crossings; penalty routing to `R_eff` only; P2W split; typed/id‑based RSCR causes; defaults with one governing definition; Δ‑discipline) are governed by `G.Core` and are *cited* via `CC‑GCORE‑*`. This pattern defines only the *bridge calibration kit* and its surfaces.

### G.7:1 - Problem frame

SoTA synthesis (**G.2**) can legitimately preserve pluralism by exporting a **BridgeMatrix**: a Tradition×Tradition inventory of “comparable constructs” with preliminary notes (candidate correspondences, likely losses, tentative levels). When the receiving use requires calibrated cross‑Context reuse, downstream patterns (CHR/CAL/selector/logging/shipping) must ensure that the reuse is:

* **recoverable** through the actual correspondence and its source basis, including BridgeCards for F.9 rows,
* **calibrated** with a small, auditable procedure (so CL/CL^k/plane routing is not a narrative),
* **published** with the anchors required by the receiving use; UTS and E.18/A.21 harnesses apply to their actual public names and flow/gate crossings,
* **refreshable** in a *targeted* way (path‑scoped RSCR rather than whole‑pack reruns).

`G.7` packages this into a kit: `BCT` + applicable correspondence references + `RegressionSet`/`SentinelSet` wiring, so that later patterns can satisfy core invariants without re‑inventing cross‑Tradition machinery.

### G.7:2 - Problem

1. Cross‑Tradition comparisons are frequently attempted via informal “synonymy” or ad‑hoc mappings, causing silent meaning drift and hidden crossings.
2. Plane mismatches (world ↔ concept ↔ episteme, or other `ReferencePlane` shifts) are often ignored, or conflated with “semantic sameness”, causing wrong downstream confidence.
3. Calibration changes (CL/CL^k/plane or their policy pins) must trigger **targeted** re‑checks; pack‑wide reweaves are too costly and too slow.
4. If bridges are involved in QD/illumination or other edition‑sensitive telemetry, **edition pins** must be tracked (otherwise comparisons become irreproducible after a map/distance/policy update).
5. Row‑level summaries (for matrix rows / comparable construct groups) tend to be averaged or “smoothed”, which is incompatible with bottleneck semantics and loss honesty.

### G.7:3 - Forces

| Force                                    | Tension                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Comparability vs local authority**     | Enable comparisons across Traditions ↔ avoid overriding Context‑local meaning.                                                                                            |
| **Auditability vs authoring throughput** | Require explicit artefacts, losses, and pins ↔ keep the calibration procedure light enough to be used.                                                                    |
| **Targeted refresh vs safety**           | Emit path‑local RSCR triggers ↔ ensure triggers are typed and carry enough payload pins for audit and rerun planning.                                                     |
| **Plane awareness vs “one story”**       | Explicitly surface `ReferencePlane` and plane penalties ↔ avoid turning plane discussion into a second semantics of “sameness”.                                           |
| **QD comparability vs metric drift**     | Enable cross‑context reporting of archive/illumination telemetry ↔ enforce edition‑aware pins for descriptor/distance/policies only when those modes are actually in use. |

### G.7:4 - Solution — Bridge calibration kit (BCT + BridgeCards + RegressionSet/Sentinels)

#### G.7:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative).**

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted
  },
  RSCRTriggerSetIds := { GCoreTriggerSetId.BridgeCalibrationKit },
  CorePinSetIds := { GCorePinSetId.PartG.CrossingVisibilityPins },
  CorePinsRequired := {
    BridgeCalibrationTableId (BCT.id),
    RegressionSetId,
    SentinelSetId,
    FreshnessWindowRef,
    CalibrationLedgerId,
    RowScopeId,
    ReferencePlane(src)?,
    ReferencePlane(tgt)?,
    UTSRowId[]?,
    PathId[]?/PathSliceId[]?
  },
  DefaultsConsumed := ∅,
  TriggerAliasMapRef := ∅
⟩`

* **Expansion rule.** Effective `CoreConformanceIds`, `RSCRTriggerKindIds`, and `CorePinsRequired` are obtained by expanding the cited profile/set ids and unioning with the explicit ids above (see `G.Core` nil‑elision + expansion rule).
* **Conditional pins.**
  * Relation, calibration and policy pins follow the channel/use conditions in G.Core:4.2.3. Source/target planes are required for an actual plane claim or another rule that consumes them; UTS and Path pins follow actual public-name and path uses.
  * `BridgeCardRef.edition` is required iff an F.9 BridgeCard is published as an editioned artefact.
  * Sentinel scopes MAY be recorded as `PatternScopeId[]` when path surfaces are not available (and SHALL then be present in sentinel records and emitted trigger payload pins).
* **CN/CG note.** `CC‑GCORE‑CN‑CG‑1` is included via `GCoreConformanceProfileId.PartG.AuthoringBase` and is exercised only when the governance card and legality gate (e.g., `CNSpecRef.edition` / `CGSpecRef.edition`) are explicitly pinned; penalty/guard policy ids (`Φ(CL)`, `Ψ(CL^k)`, `Φ_plane`) are policy pins, not governance cards or legality gates.

*(payload pins, minimum: affected members of the effective `CorePinsRequired` (after expansion) plus any pins introduced by active extensions (e.g., QD parity pins), scoped to the watched `PathSliceId[]`/`PathId[]`/`PatternScopeId[]`.)*

#### G.7:4.2 - Kit objects (surface governed by this pattern)

This pattern defines the *bridge calibration kit* as a set of minimal, checkable surfaces. **F.9** governs `BridgeCard` and CL meaning; **C.3.3** governs `KindBridge` and `CL^k` when the kind channel is used. G.7 adds calibration records and publication/wiring surfaces.

**(A) BridgeCalibrationTable (BCT) — object.**
A `BridgeCalibrationTable` is a per‑Tradition‑pair registry of calibrated bridge entries.

Minimal fields (conceptual):

`BridgeCalibrationTable := ⟨
BCT.id, TradPairId, FreshnessWindowRef,
RowEntries[]
⟩`

**Source provenance (when sourced from `G.2`).** If the BCT is derived from a `G.2` BridgeMatrix, publish `BridgeMatrixId` (+ `BridgeMatrixRef.edition` when editioned) and row‑level linkage via `G.7:Ext.MatrixIntake` (wiring‑only), rather than duplicating G.2 semantics in core.

Where each `RowEntry` minimally binds:

`RowEntry := ⟨
RowEntryId, ComparableConstructId, RowScopeId,
BridgeCardId[]?, KindBridgeAssertionRef[]?, PlaneRelationRef[]?,
RowCL_min?, RowCL_k_min?, RowCL_plane_min?, CalibrationBasisRef,
LossNoteRef[]?, CounterExampleRef[]?, CounterExampleAbsenceRef?, ReceivingUseClaimRef[]?, ReceivingPolicyRef[]?, WaiverRef[]?,
RegressionSetId, SentinelSetId,
PolicyPins?: { Φ(CL)?, Ψ(CL^k)?, Φ_plane? },
PlanePins?: { ReferencePlane(src), ReferencePlane(tgt) },
ExtensionPins?: { [GPatternExtensionId]: { …ids… } }
⟩`

**(B) CalibrationLedger — object.**
A `CalibrationLedger` is the auditable “row narrative” that remains *pin‑first*: it records what was calibrated, what was lost, and which artefacts/policies witness that.

Minimal fields:

`CalibrationLedger := ⟨
LedgerId, TradPairId,
Entries[]  // cite RowEntryId, relation/card refs, calibration basis and supported summaries, losses, counterexamples or search disclosure, UTS rows and any regression-run/delta refs; keep receiving-use/policy claims and a policy exception distinct
⟩`

**(C) RegressionSet — object.**
A `RegressionSet` is a small set of regression probes/checks that are runnable against the BCT row entries. It exists to detect drift (bridge edits, policy edits, plane edits, edition pin changes) and to provide the evidential payload for RSCR triggers.

Minimal fields:

`RegressionSet := ⟨ RegressionSetId, TradPairId, TestCaseId[], ExpectedOutcomesRef?, RegressionRunRef? ⟩`

##### G.7:4.2.1 - Interpret calibration and assess a receiving use separately

**Calibration question.** State which correspondence, direction, scope, source editions and evidence the row assesses. Keep an F.9 sense correspondence, a C.3.3 kind correspondence and an applicable plane relation under their separate predicates. A record or favourable summary makes none of them obtain.

For a stated F.9 correspondence, optional CL shorthand means: `0` contradicted, `1` weakly comparable, `2` bounded support with explicit counterexamples, and `3` matched stated invariants with no current material counterexample. Cite the actual calibration basis. A kind-channel value follows C.3.3; a plane-channel value requires its own declared calibration rule. One channel cannot raise or replace another.

**Summary meaning.** Use `RowCL_min` only when a non-empty set of cells shares the declared ordinal scale and calibration question and the receiving report needs its weakest calibrated level. Cite that cell set and keep each loss recoverable. Apply the same condition independently to kind or plane summaries. An empty, mixed or unresolved basis has no such minimum; publish the separate results or the precise gap. A minimum is a calibration summary, not an admissibility result, and ordinal values are not averaged.

**Evidence honesty.** Preserve actual counterexamples and losses. Level 2 needs its cited bounded-support counterexample; level 0 identifies the contradiction. Weak or incomplete evidence must be disclosed rather than dressed as a discovered counterexample. At level 3, when none is cited, supply a citable search/absence account stating what was examined and that none was found or is currently known. This reports the search basis, not universal absence. A loss-noted row cannot be presented as free substitution.

**Receiving use.** For an F.9 use, state the separate claim with its use, direction, correspondence rule, loss tolerance and polarity; obtain matching A.10 reliance, or the B.3 result when an actual named assurance claim is current. A C.3.3 use separately checks receiving admissibility and target classification. Missing classification evidence remains unknown. Authorization, when required, follows its own rule. No CL level supplies these results.

A receiving policy may impose an additional threshold for one named use. Cite that use, the policy's justification and authority, and its other necessary premises. The threshold is an additional policy condition, not F.9's general law. A `WaiverRef` identifies an authorized exception to that policy only: it supplies no missing correspondence, target fact, suitable-use claim or evidence. Preserve any narrower allowed use and its independently supported conditions.

**Plane and loss policies.** When a receiving use relies on a plane relation, name the source and target planes, its predicate, calibration basis and applicable policy. Missing required plane information leaves that use unresolved. Keep any downstream `abstain` or policy-bound `degrade` under its receiving guard. Plane evidence does not rewrite CL or CL^k; a numerical loss requires its own receiving model and policy, with the consequence in R only.

**(D) SentinelSet & BridgeSentinel — object.**
A `SentinelSet` is a watch‑list that connects bridge calibration changes to RSCR‑ready triggers scoped to downstream consumption.

Minimal fields:

`BridgeSentinel := ⟨
SentinelId,
watchedRowEntryIds: RowEntryId[],
watchedRelationRefs: exact references to the correspondences assessed by those rows,
watchedScope: PathSliceId[] | PathId[] | PatternScopeId[],
payloadPins: { BCT.id, RegressionSetId, FreshnessWindowRef, affected RowEntryId[], watchedRelationRefs, PolicyPins?, PlanePins?, UTSRowId[]? }
⟩`

`SentinelSet := ⟨ SentinelSetId, BridgeSentinel[] ⟩`

#### G.7:4.3 - Minimal calibration procedure (auditable; table‑backed; bridge‑first)

For each Tradition‑pair and each comparable construct row from **G.2**:

1. **Recover the correspondence being calibrated.** For an F.9 row, resolve the exact F.17 sense cells and profile, then produce or reuse its BridgeCard. A kind-channel row cites the C.3.3 kind endpoints and assertion; a plane row cites its own relation and rule. A coarser source label must be resolved to those actual endpoints before calibration.
2. **Record row scope and losses.** Author a `RowScopeId` and record loss notes as first‑class citations (e.g., `LossNoteRef[]`), not as informal footnotes.
   Record the calibration basis and any meaningful channel summary under §4.2.1. If a receiving use is named, cite its separate suitability/classification and reliance results. Cite a waiver only for its exact authorized policy exception; it does not repair missing evidence.
3. **Resolve any plane claim.** If the row or receiving use consumes a plane relation, record its exact reference, source and target planes, governing rule and any plane policy actually applied. A kind-only or sense-only row creates no plane claim.
4. **Expose policies actually used.** Record policy and model references for a named threshold, exception, numerical loss or assurance calculation. Calibration without such a receiving use needs no invented Φ/Ψ/Φ_plane policy. Applied penalties retain G.Core's R/R_eff-only rule.
5. **Summarize only a common calibration basis.** Use the minimum only under §4.2.1's shared-scale and shared-question conditions. Retain each actual loss and counterexample; otherwise report the separate cell results or the unresolved basis.
6. **Regression and sentinel wiring.** Create/update the `RegressionSet` and `SentinelSet`. Any calibration change that can affect downstream audit (CL/CL^k/plane pins, relevant policy ids, edition pins for involved telemetry surfaces, freshness window) emits typed RSCR triggers (canonical ids; scope + payload pins).
   If the regression harness is run, record a citable `RegressionRunRef` (or equivalent run/delta reference) and attach it to the relevant ledger entries (pin‑first; no narrative-only deltas).

#### G.7:4.4 - Publication surfaces (UTS + GateCrossing harness)

A conformant G.7 publication:

* publishes the exact correspondence references for each row, including BridgeCards for F.9 rows and UTS identifiers when the naming/publication rule requires them,
* makes an independently governed E.18 crossing or A.21 gate checkable through its applicable harness, preserving lexical, lane and required-pin constraints,
* emits RSCR triggers using canonical `RSCRTriggerKindId` and attaches the minimum payload pins listed in §4.1.
* keeps SCR/Evidence citations complete for their actual use: include the row locator, exact correspondence basis and `{BCT.id, RegressionSetId}`, plus the policy/model pins actually consumed by the reliance or assurance claim. Representation follows G.6/SCR when that surface is used.

#### G.7:4.5 - Worked mini‑examples (informative; post‑2015; row scopes + loss notes)

> These worked rows use illustrative calibration values and source scopes. Actual calibration needs its stated evidence. Each receiving use still has a separate rule and loss tolerance.

1. **Preference‑learning objective (Method; RowScope = “training‑objective‑intent”).**
   *Cells:* `RLHF@Context‑A` ↔ `DPO@Context‑B` ↔ `IPO@Context‑C`
   *RowCL_min:* 2 (calibrated bounded support in this worked case)
   *Loss notes:* different inductive biases (reward model vs direct preference likelihood; sensitivity to preference noise model; implicit regularisation forms).
   *Proposed use:* a didactic comparison of objective intent. Its separate claim must limit the comparison to that intent and retain the listed differences; method eligibility and acceptance require their own rule.

2. **Robustness evaluation (Measurement; RowScope = “metric‑family‑intent”).**
   *Cells:* `Accuracy@IID` ↔ `Robustness@ShiftBench` (e.g., distribution‑shift benchmarks common in post‑2019 practice)
   *RowCL_min:* 2
   *Loss notes:* shift taxonomy differs; comparability depends on pinned protocol editions and window selection; “robustness” is not a scalar substitute for accuracy.

3. **Quality‑Diversity archive comparability (Measurement; RowScope = “DescriptorMap‑only”).**
   *Cells:* `MAP‑Elites grid indices` ↔ `CVT‑MAP‑Elites centroids` ↔ `CMA‑ME archive`
   *RowCL_min:* 2
   *Loss notes:* discretisation vs centroidal tessellation; archive pressure differs; drift occurs if `DistanceDef` or insertion policy changes.
   *Proposed use:* cross-reporting only the named descriptor-map relation under explicit edition pins and an affirmative bounded-use claim with passing reliance. Edition pins alone do not make the telemetry comparable.

4. **Open‑ended transfer semantics (Method; RowScope = “transfer‑rule intent”).**
   *Cells:* `POET‑class transfer rule` ↔ `Enhanced‑POET‑class transfer rule` ↔ “modern open‑ended transfer variants”
   *RowCL_min:* 2
   *Loss notes:* environment validity region differs; transfer timing and selection pressures differ; pinning transfer rule editions is mandatory for audit.

**Paired receiving case — Vehicle to TransportUnit.** Use C.3.3 §9.1's exact source and target kind declarations, pinned scheme editions, `registryAPI v1.4` and selected time window. In row `VehicleTransportOrder`, record the obtaining KindBridge, preserved PassengerCar/Vehicle subkind order and collapsed EV distinction, with the reported `CL^k=2` and battery-health loss. This is the kind channel; an F.9 sense Bridge is added only if the receiving claim separately relies on one.

For a G.5 shortlist of independently admitted Methods for a transport review, suppose the applicability criterion uses only the preserved transport/passenger order and explicitly ignores propulsion. The row can support that narrow applicability comparison after receiving admissibility, fresh target classification of the subject vehicles and the matching evidence-reliance result pass. The Methods' other eligibility criteria remain applicable. For a battery-health review whose Method-selection rule needs EV/battery information, the same correspondence fails that use because the required distinction is lost. A favourable CL value or a waiver cannot supply the battery premise. The correspondence and calibration can stay unchanged while these two use conclusions differ. Use these two questions as a paired RegressionSet probe when this row is reused: recover the transport-order premise for the first and expose the missing battery premise for the second. Recheck the affected use after its criterion or the row's preservation/loss basis changes.

In C.3.3 §9.3's AdultPatient/AdultPerson_Y case, the age-boundary loss and `CL^k=1` remain evidence about the kind correspondence. An authorized policy exception does not supply an unresolved date of birth; the receiving classification stays unknown.

**Choose pins for the actual use.** These cases apply the same conditions to a compact result and to the fuller kit:

| Use | What the result must retain |
| --- | --- |
| VehicleTransportOrder kind-only calibration | its C.3.3 kind endpoints, assertion, CL^k calibration basis, battery-health loss, row/freshness and kit references; a live sentinel can use PatternScopeId. No sense Bridge, plane relation or loss policy follows from this row. |
| F.9 sense-only calibration | exact F.17 sense endpoints, obtaining Bridge, BridgeCard and any reported CL basis; add neither a kind correspondence nor a plane claim without its own basis. |
| Plane-only calibration | the independently governed plane relation, planes and calibration rule/basis; add a numerical loss policy only if that receiving model is used. Plane change alone supplies no F.9 Bridge. |
| A G.2 harvest with no crossing, or a suite contract reused on another entity of the same kind | ordinary source/edition and applicability information; no crossing pin set is instantiated merely from the harvest, entity change or a new declaration edition. |
| A use relying on both a sense and kind correspondence | both independently established relations and their receiving conditions; neither channel replaces the other. |
| A safety-assurance comparison using an F.9 calibration, a defined plane-loss model and an A.21 gate | the exact Bridge/Card and row, BCT/regression/freshness evidence, actual plane relation and model/policy pins, matching A.10/B.3 reliance and assurance grounds, and every required gate anchor. A required missing pin leaves that use unresolved; favourable calibration alone grants no permission. |

#### G.7:4.6 - Extensions (pattern‑scoped; non‑core)

> Extensions carry *wiring only* (pins/editions/policy‑ids + which governing patterns are applied). They MUST NOT redefine core invariants or defaults.

**GPatternExtension: MatrixIntake**

* **PatternScopeId:** `G.7:Ext.MatrixIntake`
* **GPatternExtensionId:** `MatrixIntake`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `G.2` *(BridgeMatrix semantics and comparable-construct inventory)*
* **Uses:** `{G.2, F.9}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum):**

  * `BridgeMatrixId` (and, if editioned: `BridgeMatrixRef.edition`)
  * `BridgeMatrixRowRef[]` *(row‑level anchors for intake; defined by the governing pattern; e.g., `PatternScopeId` / `UTSRowId` / row ids)*
  * `ComparableConstructId[]` *(row keys; if the source does not supply a stable id, `G.7` mints one while preserving `BridgeMatrixRowRef` as the provenance anchor)*
  * `LossNoteRef[]?` *(if exported by `G.2`; otherwise authored in `G.7` and cited from the `CalibrationLedger`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):** This module binds “row candidates” from G.2 to the BCT/Ledger intake without copying G.2 semantics into G.7.

**GPatternExtension: DHCAccounting**

* **PatternScopeId:** `G.7:Ext.DHCAccounting`
* **GPatternExtensionId:** `DHCAccounting`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `C.21` *(DHC metric semantics, including AlignmentDensity)*
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `AlignmentDensityMethodRef.edition?`
  * `DeclaredUnitsRef?` *(the C.21 Unit for the reported quantity; AlignmentDensity uses `obtaining_relations/100_compared_cells`)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EditionPinChange}`
* **Notes (wiring‑only):**
  * G.7 stores the *counts and declared units* as a surface; C.21 governs the meaning and legality constraints.
  * When reporting AlignmentDensity, follow C.21's declared F.17 cell set and count only exact obtaining directed F.9 relations. Preserve each counted relation's orientation and admitted-use qualifier, and keep observed loss in its evidence account. CL values neither change that count definition nor grant substitution; `CC‑G7‑DHC‑Units‑1` checks the report's units and cited method.

**GPatternExtension: QDParityPins**

* **PatternScopeId:** `G.7:Ext.QDParityPins`
* **GPatternExtensionId:** `QDParityPins`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `C.18` *(QD artefact semantics; uses C.19 for exploration/logging pins as needed)*
* **Uses:** `{C.18, C.19}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**

  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `InsertionPolicyRef` *(policy id or pinned policy ref, per governing definition semantics)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent}`
* **Notes (wiring‑only):** Enforces reproducibility of cross‑Context archive/illumination comparisons without pulling QD semantics into the core bridge kit.
  The pins from this module should be attached via `RowEntry.ExtensionPins[QDParityPins]` (or an equivalent extension‑pin map) and included in `BridgeSentinel.payloadPins` whenever the watched scope consumes QD telemetry.

**GPatternExtension: SoSLogClauses**

* **PatternScopeId:** `G.7:Ext.SoSLogClauses`
* **GPatternExtensionId:** `SoSLogClauses`
* **GPatternExtensionKind:** `InteropSpecific`
* **GoverningPatternId:** `C.23` *(SoS‑LOG rule and branch semantics; G.7 does not redefine meaning)*
* **Uses:** `{C.23, G.6}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` *(or governing definition‑equivalent ids)*
  * `FailureBehaviorPolicyId?` *(policy id, when degrade behavior is bound)*
  * `PathId/PathSliceId` citations for explainability (via `G.6`)
  * `BridgeCardId[]` (bridges whose reuse is being justified)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.MaturityRungChange}`
* **Notes (wiring‑only):** Ensures cross‑Tradition bridge reuse decisions can be justified by citing SoS‑LOG clauses and evidence paths, without embedding SoS‑LOG semantics into G.7.

**GPatternExtension: AcceptanceHooks**

* **PatternScopeId:** `G.7:Ext.AcceptanceHooks`
* **GPatternExtensionId:** `AcceptanceHooks`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `G.4` *(Acceptance/threshold/unknown handling; G.7 does not define thresholds)*
* **Uses:** `{G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `AcceptanceClauseId[]` *(or governing definition‑equivalent ids)*
  * `AcceptancePolicyId?` *(policy id when acceptance behavior is pinned)*
  * `BridgeCardId[]` (bridges whose calibrated status is being used as a gate input)
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.BaselineBindingEdit, RSCRTriggerKindId.LegalitySurfaceEdit}`
* **Notes (wiring‑only):** When bridges are used as selector gates, thresholds and unknown-handling remain governed by Acceptance; this module only pins the linkage and refresh relevance.

**GPatternExtension: AdvancedCalibrationProcedures (Phase‑3 seed)**

* **PatternScopeId:** `G.7:Ext.AdvancedCalibrationProcedures`
* **GPatternExtensionId:** `AdvancedCalibrationProcedures`
* **GPatternExtensionKind:** `Phase3Seed`
* **GoverningPatternId:** `governing pattern not yet selected`
* **Uses:** `{ }`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins:** `pending governing-pattern selection`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.ReferencePlaneEdit}`
* **Notes (seed; non‑normative):** Placeholder for domain‑specific / statistical calibration families beyond the minimal auditable procedure (e.g., uncertainty‑aware calibration, probabilistic mapping). No Part‑G‑wide norms are introduced.

### G.7:5 - Archetypal Grounding (System / Episteme)

**System case:** *Cross-standard comparison of safety claims about one physical system (bridge-first).*
A team must compare a safety assurance claim across two regulatory Traditions (e.g., a “functional safety case” tradition and a “ML system testing” tradition) for the *same physical system scope*. `G.7` forces explicit SenseCell‑level bridges (what exactly is the “hazard”, what is the “evidence carrier”, what is the “pass criterion”), records losses, pins planes, and provides sentinels so that changes in the safety evidence protocol editions trigger path‑local RSCR rather than re‑authoring the entire safety case.

**Episteme case:** *Benchmark protocol pluralism (post-2015 evaluation practice).*
A research group wants to compare “state‑of‑the‑art” across multiple evaluation Traditions (IID performance, shift robustness, preference‑based evaluation). `G.7` turns “these are comparable” into explicit BridgeCards with declared row scope, pins the evaluation protocol editions, and registers sentinels so that when a benchmark protocol or policy pin changes, downstream selector decisions can be re‑audited by replaying the affected PathSlice‑scoped evidence.

### G.7:6 - Bias‑Annotation

Bias lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the bridge calibration kit; any method‑family or discipline‑specific calibration technique is modularized as `GPatternExtension` and cited to its governing patterns.

### G.7:7 - Conformance Checklist (normative) — **CC‑G7**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                               | Purpose                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CC‑G7‑CoreRef**         | `G.7` is conformant only if it satisfies the effective `G.Core` obligations declared by the `GCoreLinkageManifest` in **§4.1** (after nil‑elision and expansion of profile/set/pinset ids), including any explicit deltas listed there. | Make universal invariants one governing definition and enforce citation‑based reuse.       |
| **CC‑G7‑BCT‑1** | An active calibration kit has a BCT with its freshness basis, exact row scope, relation/card references, calibration basis and applicable evidence, regression and sentinel references. Channel summaries and policy/plane pins are present only under their declared calibration or receiving-use conditions. | Make the calibration and its use independently recoverable. |
| **CC‑G7‑BridgeCard‑1** | An F.9 BridgeCard resolves its exact F.17 endpoint senses and relation profile. A kind-channel assertion follows C.3.3 and cites its exact kind endpoints; a plane claim cites its own governor. Keep the channels distinct. | Preserve the subject of each correspondence. |
| **CC‑G7‑UTS‑1** | When G.7 mints or publishes a public identifier, apply CC-GCORE-UTS-1 and expose the resulting UTS rows in the consuming BCT/Ledger or crossing bundle. Include a BridgeCard or GateCrossing row only when that actual object is used; a kind-only calibration creates no F.9 BridgeCard. | Make public names citable without inventing relations. |
| **CC‑G7‑RowScope‑1**      | Every BCT row **MUST** declare its `RowScopeId` (which correspondence or difference is being calibrated), and any loss notes **MUST** be recorded as citable artefacts (refs/ids), not only narrative text.                                                                                                 | Keep reuse honest and locally bounded.                                         |
| **CC‑G7‑CLRegime‑1** | Every reported CL summary satisfies §4.2.1's calibration meaning and aggregation conditions. Actual losses, counterexamples and required search/absence disclosures remain citable. The receiving use has its own rule, tolerance and reliance; a threshold or waiver cites its policy use, justification, authority and additional premises. | Calibration evidence supplies no automatic permission or receiving classification. |
| **CC‑G7‑SCRLinkage‑1** | A calibration cited in SCR/Evidence surfaces MUST identify its exact sense, kind or plane correspondence, row locator and `{BCT.id, RegressionSetId}`. Add BridgeCard/UTS anchors for the actual F.9/public-name use and policy/model pins for the actual reliance, numerical loss or assurance calculation. | Preserve the evidence consumed by the claim without fabricating another channel. |
| **CC‑G7‑SoSLOG‑Pins‑1**   | When `G.7:Ext.SoSLogClauses` is in use, G.7 outputs **MUST** expose the cited SoS‑LOG rule ids and the relevant `PathId/PathSliceId` evidence citations; any change in those pins **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                               | Keep cross‑Tradition reuse explainable without embedding C.23 semantics.        |
| **CC‑G7‑Acceptance‑1**    | When `G.7:Ext.AcceptanceHooks` is in use, G.7 outputs **MUST** expose the Acceptance clause ids/policy ids used as gates; thresholds/unknown handling remain governed by Acceptance; any change **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                           | Keep thresholds and unknowns out of bridges while preserving auditability.     |
| **CC‑G7‑RowBottleneck‑1** | A minimum summarizes only a non-empty cell set sharing the declared ordinal scale and calibration question. Keep the constituent evidence and losses; otherwise report separate results or the gap. | Avoid averaging ordinal evidence or treating its minimum as a use decision. |
| **CC‑G7‑PolicyPins‑1**    | G.7 outputs **MUST** publish the *policy id pins* required to audit penalty routing and plane effects (ids only), as required by `CC‑GCORE‑LINK‑1/2` and `CC‑GCORE‑PEN‑1`. G.7 MUST NOT duplicate policy tables or redefine penalty semantics.                                           | Keep penalty routing auditable while preserving single‑governing-pattern policy semantics. |
| **CC‑G7‑GateCrossing‑1** | An independently governed E.18 flow crossing or A.21 gate that consumes calibration MUST retain its required harness, pins, lexical constraints and lane checks. A calibration relation alone is not that flow crossing or gate. | Make actual crossings and gates checkable. |
| **CC‑G7‑Sentinels‑1**     | G.7 **MUST** register `BridgeSentinel` entries for bridges used by live scopes and **MUST** emit typed RSCR triggers (canonical `RSCRTriggerKindId`; see `CC‑GCORE‑TRIG‑1…TRIG‑4`) on calibration‑relevant edits, scoped to the watched `PathSliceId[]` or `PatternScopeId[]`, with the minimum payload pins from §4.1. | Enable targeted refresh rather than pack‑wide reruns.                          |
| **CC‑G7‑QD‑Pins‑1**       | When `G.7:Ext.QDParityPins` is in use, G.7 outputs **MUST** include `{DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef}` and treat any change to those pins as RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                                          | Prevent silent QD telemetry drift.                                             |
| **CC‑G7‑DHC‑Units‑1** | When AlignmentDensity is reported, G.7 outputs **MUST** count the exact obtaining directed F.9 relations in the declared F.17 cell set under C.21, include the declared units, and cite the active DHC method and replay basis. Related DHC accounts use their own exact C.21 definitions. CL labels grant no substitution and do not redefine the counted relation set; G.7 MUST NOT invent arithmetic over ordinal or otherwise inadmissible surfaces. | Keep dashboards and discipline-health readings faithful to their measurement definitions and bounded-use claims. |

### G.7:8 - Common Anti-Patterns and How to Avoid Them

* **Bridge‑by‑prose (“they have the same sense”).**
  **Avoid:** publish BCT rows + BridgeCards + UTS rows; require SenseCell anchoring and row scopes.
* **Scope or sense relation used as a kind bridge.**
  **Avoid:** state the channel in `RowScopeId` and use its direct governor. A C.3.3 correspondence needs its kind endpoints and separate receiving classification; cite CL^k and any loss policy only when that calibration or reliance account uses them.
* **Plane blindness (“concept = world”).**
  **Avoid:** record plane pins and policy id pins; keep plane effects auditable and separable from CL/CL^k semantics.
* **CL smoothing / averaging.**
  **Avoid:** establish the common scale and calibration question before taking a minimum; retain actual counterexamples and losses, and keep the receiving decision separate.
* **Pack‑wide refresh on a local bridge edit.**
  **Avoid:** register sentinels scoped to `PathSliceId` and emit typed RSCR triggers with minimal payload pins.
* **QD metric drift by unpinned artefacts.**
  **Avoid:** enable `G.7:Ext.QDParityPins` only when needed and require edition/policy pins when enabled.

### G.7:9 - Consequences

* **Auditable pluralism.** Cross‑Tradition reuse becomes explicit, loss‑aware, and checkable.
* **Targeted, edition‑aware refresh.** Calibration drift triggers path‑scoped RSCR rather than expensive global reruns.
* **Downstream cleanliness.** Selectors/logging/shipping can cite bridges and policy pins without inventing local crossing rules or shadow specs.

### G.7:10 - Rationale

* **Why a kit (not a new governance card or legality gate)?** Bridge calibration must support many downstream consumers without becoming a competing legality gate; governing-spec semantics remain governed by `CG‑Spec`/`CN‑Spec`.
* **Why BCT + RegressionSet + SentinelSet?** Regression tests make calibration drift detectable; sentinels identify the downstream scopes to refresh.
* **Why row scopes?** Because “comparable” is not one thing; scope must be explicit to avoid accidental substitution.

### G.7:11 - SoTA-Echoing — calibrate a correspondence for its receiving use

**Practice question.** When a correspondence has a favourable calibration, what must an engineer check before reusing it for a different task? The selected best-known line for this question keeps the exact relation, its justification and source versions recoverable, then tests the receiving task's required distinctions. The serious alternative is to select an alignment by its reference-benchmark score and carry that favourable score into downstream use.

[SSSOM 1.0's mapping model](https://mapping-commons.github.io/sssom/1.0/spec-model/) supplies the first line's concrete separation of endpoints, relation predicate and justification. Its [mapping FAQ](https://mapping-commons.github.io/sssom/1.0/faq/) distinguishes relation precision from confidence and explains why source versions and justification matter. **Adopt** that separation for the BCT row's exact correspondence and calibration basis in §4.2. These sources address exchangeable ontology mappings; they do not establish an F.9 Bridge, a C.3.3 classification or permission for an FPF receiving use.

The [OAEI 2025 Conference evaluation](https://oaei.ontologymatching.org/2025/results/conference/eval.html) is the serious benchmark comparator: its precision/recall measures assess generated correspondences against stated reference alignments and populations. That is useful for choosing a matcher on that question. **Reject** carrying its aggregate success, or one CL value, as a substitute for a different task's premises. This is a limit of the inference, not a claim that OAEI promises such transfer.

**Adapt** the mapping-and-justification line in §4.2.1 and procedure steps 2/6: retain direction, scope and losses, and use a small regression pair whose required distinction changes. In §4.5, VehicleTransportOrder can retain passenger/transport order while losing battery information. The same calibrated relation can therefore support the stated transport comparison and fail the battery-health question. Keeping that distinction prevents a concrete erroneous use that a single favourable summary cannot detect.

At comparable effort, both alternatives start with the same relation row and existing calibration evidence. The selected line adds one named use condition and the smallest counterexample or regression pair that can change the answer. That is extra effort deliberately accepted for reuse across task boundaries; ordinary one-off correspondence handling remains with F.9 when a calibration kit adds no value. SSSOM and OAEI provide the compared technical approaches, not empirical validation of this kit. Reopen when a new receiver needs a distinction outside the row's stated preservation/loss basis, or when a cheaper rule can distinguish those same allowed and failed uses with equivalent support.

### G.7:12 - Relations

**Builds on:** `G.Core`, `G.2`, `F.3`, `F.7`, `F.9`, `F.17`, `B.3`, `E.10`, `E.18`, `A.21`, `G.6`, `C.21`; `C.3.3` when the kind channel is used.
**Optionally uses via Extensions:** **G.4** (Acceptance hooks), **C.23** (SoS‑LOG clauses), **C.18 and C.19** (QD/OEE pins).
**Used by / prerequisite for:** In uses that consume this kit's calibration, **G.5** (cross‑Tradition eligibility/selection), **G.11** (refresh orchestration), **G.9** (parity across Traditions where bridges are required), **G.10** (shipping surfaces that must cite bridge calibration ids), **G.12** (DHC dashboards when bridge counts/units are surfaced).
**Publishes to:** **UTS** (bridge and crossing rows; twin labels as applicable) and emits RSCR‑ready telemetry/trigger payloads for **G.11**.
**Constrains:** Any downstream consumer that relies on this kit's calibration claims or records must use the corresponding calibrated bridge artefacts/pins surfaced by this kit (governing G.Core crossing invariants apply).

### G.7:End

## G.8 - Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)

> **Status:** Stable

**Tag.** Architectural pattern (packaging kit).
**Stage.** Design‑time packaging (authoring & publication) with a run‑time consumption facade for `G.5` (selector/registry).
**Primary hooks:** `G.Core` (Part‑G invariants), `C.23` (SoS‑LOG semantics), `C.22` (TaskSignature), `G.4` (Acceptance & EvidenceProfiles), `G.6` (EvidenceGraph & `PathId/PathSliceId`), `G.5` (registry/selector), `G.11` (refresh orchestration), `G.10` (shipping boundary), `F.9` (cross-semantic relations and bounded-use claims), `F.17` (UTS), `E.17` (publication faces), `G.7` (bridge calibration & Φ/Ψ/Φ_plane), `F.8` (Policy pins: `PolicySpecRef`/`MintDecisionRef` resolvability), `A.10` (anchors), `E.10` (LEX twin registers), `E.5.2` (notational independence), `E.18` (crossing visibility when a selected transformation-flow structure is in use), `A.21` (gate decisions under an applicable profile).

**Part‑G linkage.** This pattern defines **kit-governed packaging surfaces** for SoS‑LOG bundles and maturity ladders. **Part‑G‑wide invariants** are governed by `G.Core`; the linkage manifest in §4.1 names the applicable obligations.

**Modularity note (policy‑id pins are reference‑only).** This kit may pin/cite policy ids (e.g., `Φ/Ψ/Φ_plane` policies, `FailureBehaviorPolicyId`, illumination‑promotion policy ids, and E/E‑LOG policy ids) **as references only**. Conformance relies on the policy‑pin resolvability discipline of `F.8:8.1` (i.e., policy ids are not “inlined”; and when newly minted, they are backed by resolvable `PolicySpecRef` + `MintDecisionRef`). `G.8` does not define policy semantics and MUST NOT silently mint policy ids.

### G.8:1 - Problem frame

Method families compete within a `CG‑Frame`, but dispatch is only lawful if (i) admissibility decisions remain **tri‑state** and auditable, (ii) evidence and crossings are **explicitly citable** (by ids, not prose), and (iii) selection preserves **set-return semantics** under partial orders. In practice, SoS‑LOG rules (`C.23`) and “maturity stories” are often distributed across prose, dashboards, and ad‑hoc checklists, with thresholds embedded where they do not belong and with missing pins for evidence paths, crossings, and editions.

This pattern provides the missing packaging kit: a **selector‑facing, UTS‑citable bundle** that binds **(a)** rule ids (semantics governed by `C.23`), **(b)** an ordinal/poset maturity ladder (published as a citable card), and **(c)** explicit wiring to Acceptance (`G.4`), EvidenceGraph (`G.6`), selection/registry (`G.5`), and refresh (`G.11`)—without creating any shadow governing spec refs.

### G.8:2 - Problem

1. **Selector needs a stable input artefact.** `G.5` cannot consume “maturity narratives” and scattered SoS‑LOG snippets without re‑authoring semantics or inventing implicit defaults.
2. **Thresholds leak into LOG.** Numeric gates are often embedded directly into rule text or ladder rungs, blurring the boundary between LOG decisions (`C.23`) and Acceptance thresholds (`G.4`).
3. **Auditability is brittle.** Decisions (`pass/degrade/abstain`) lack stable, citable links to evidence paths (`G.6`) and crossing pins (Bridge/CL/Φ policy ids as required for the stated use), so later re‑checks and RSCR become ad‑hoc.
4. **Telemetry contaminates decision semantics.** QD/OEE/illumination signals are frequently treated as dominance inputs without explicit policy pins; edition drift then silently changes outcomes.
5. **Refresh is under‑specified.** Bundle evolution (rules, ladders, pins, policies, editions) must be RSCR‑addressable via typed trigger kinds, not by free‑text “reasons”.

### G.8:3 - Forces

| Force                                        | Tension                                                                                                      |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Pluralism vs. dispatchability**            | Preserve multiple method families and partial orders ↔ still provide a consumable artefact for `G.5`.        |
| **Auditability vs. authoring friction**      | Fine‑grained pins and citations ↔ keeping authoring lightweight and notation‑independent.                    |
| **Maturity as poset vs. scalar ranking**     | Maturity is inherently non‑scalar ↔ teams want a “single readiness number”.                                  |
| **Telemetry richness vs. decision hygiene**  | Rich QD/OEE telemetry ↔ avoid illegitimate promotion into dominance without explicit policy.                 |
| **Design‑time packaging vs. run‑time trace** | Authoring produces stable bundles ↔ run‑time produces branch‑specific path traces and admissibility ledgers. |
| **Interoperability vs. crossing discipline** | Reuse across contexts or planes ↔ prevent implicit crossings (Bridge‑only + visible).                           |

### G.8:4 - Solution — Publish SoS‑LOG bundles and maturity cards as UTS‑citable kit

#### G.8:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; citation/delegation hub)

**GCoreLinkageManifest (normative; size‑controlled).**
*(Canonical shape, Nil‑elision, and Expansion rule are per `G.Core:4.2`.)*

**Separation rule.** Method‑/generator‑specific pins are **normatively specified** only inside `Extensions` as `GPatternExtension` modules (see `G.8:5.*`). The bundle/ledger schema may mention such fields only as **extension‑gated optionals**, with the authoritative pin/edition/policy requirements stated in the corresponding extension block. The core linkage manifest lists only base‑kit pins and Part‑G‑wide linkage.

`GCoreLinkageManifest := ⟨
CoreConformanceProfileIds := {
GCoreConformanceProfileId.PartG.AuthoringBase,
GCoreConformanceProfileId.PartG.TriStateGuard,
GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
GCoreConformanceProfileId.PartG.ShippingBoundary
},

RSCRTriggerSetIds := { GCoreTriggerSetId.EvidenceGraphKit },

CorePinSetIds := {
GCorePinSetId.PartG.AuthoringMinimal,
},

CorePinsRequired := {
  // Public ids governed by this pattern (strengthen conditional pins where G.8 publishes UTS publication units)
  UTSRowId[],                    // bundle/ledger/card rows + any referenced UTS rows
  SoS‑LOGBundleRef,
  SoSLogRuleId[],
  MethodFamilyRowRef,             // exact G.5 <MethodFamilyId, rowEdition>
  RegistrationContext,

  // Closed value sets (ids only; UTS-registered)
  DegradeModeEnum,
  MaturityRungs,

  // Maturity ladder pins
  MaturityCardRef,               // required; recommended: published as separate UTS artefact
  MaturityRungId?,               // iff a specific rung is asserted at packaging/run-time

  // Evidence / provenance pins
  A10EvidenceGraphRef?[],        // packaging-time A.10 carriers (when PathId/PathSliceId not yet available)
  EvidenceGraphId?,              // iff resolvable to G.6 EvidenceGraph
  PathId[]/PathSliceId[]?,       // run-time ledgers typically have them

  // Authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[],  // edition-pinned method-description refs
},

DefaultsConsumed := {
DefaultId.PortfolioMode,
DefaultId.DominanceRegime,
DefaultId.GammaFoldForR_eff
},
⟩`

*(RSCR payload pins typically include: `SoS‑LOGBundleRef`, `SoSLogRuleId[]`, `MaturityRungId?`, and `EvidenceGraphId/PathId/PathSliceId?`.
Crossing payload pins (Bridge/CL/Φ/Ψ/Φ_plane) are introduced **only when reuse is asserted**, via `G.8:Ext.BridgeReuseWiring`. CL and loss-policy pins are required only by the actual calibration or separate named assurance use.
Method-/generator‑specific payload pins are listed only inside the relevant `GPatternExtension` blocks in `G.8:5`.)*

*(Conditionality note for defaults.)* Include `DefaultId.GammaFoldForR_eff` in `DefaultsConsumed` **only if** the bundle/ledger exports aggregated `R_eff` summaries (otherwise Nil‑elide it).

#### G.8:4.2 - Kit: objects and naming discipline (LEX heads; twin‑register safe)

**Objects / surfaces (pattern-governed).**

* **`SoS‑LOG.Rule`**
  An executable tri‑state decision schema `{pass | degrade(mode) | abstain}` for `(TaskSignature, MethodFamily)`, cited by a rule id. *(“pass” may be described as “admit” in prose, but the normative tri‑state vocabulary is `G.Core`’s `{pass|degrade|abstain}`.)*
  **Semantics are governed by `C.23`.** `G.8` only packages rule ids and binding pins.

* **`SoS‑LOGBundle@Context`**
  A selector‑facing, notation‑independent packaging object published to UTS.

* **`AdmissibilityLedger@Context`**
  A run‑time ledger view that records admissibility outcomes, cited evidence paths, branch tokens, and the pins required for audit/refresh.

* **`MethodFamily.MaturityCardDescription@Context`**
  A maturity ladder description published as a citable artefact: **ordinal/poset**, closed rungs, `ReferencePlane` declared; no thresholds inside.

**Naming discipline (E.10 + “Spaces ≠ Maps”).**

* Technical heads are normative; Plain twins are didactic only and MUST NOT cross kinds.
* Do **not** alias `CharacteristicSpace` and `DescriptorMap`.

  * `DescriptorMapRef` is a **map‑reference** (typically used with QD archives).
  * `CharacteristicSpaceRef` is a **space‑reference** (grid/cell semantics, if used).
* Editions are pinned on `…Ref.edition` fields (not on informal names).

#### G.8:4.3 - `SoS‑LOGBundle@Context` schema (conceptual; notation‑independent)

A conforming bundle is a UTS‑published object whose internal representation is free, but whose **field meanings** are stable:

```
SoS-LOGBundle@Context :=
⟨
  UTS.id := SoS‑LOGBundleRef,
  Edition,

  // Scope + spec pins (from GCorePinSetId.PartG.AuthoringMinimal)
  CG-FrameContext,
  entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
  CNSpecRef.edition,
  CGSpecRef.edition,

  MethodFamilyRowRef,             // exact G.5 <MethodFamilyId, rowEdition>
  RegistrationContext,

  SoSLogRuleId[] ,               // ids only; semantics governed by C.23
  ClosedEnums: {DegradeModeEnum, MaturityRungs},  // ids only; UTS-registered closed value sets
  A10EvidenceGraphRef?[] ,        // packaging-time evidence carriers (A.10 anchors) when paths are not yet stable
  MaturityCardRef ,               // UTS ref to maturity card (required; may be embedded but MUST be citable)
  MaturityRungId? ,               // if a specific rung is asserted at packaging time

  // Optional: Acceptance wiring (thresholds remain governed by G.4)
  AcceptanceClauseId[]? ,

  // Optional: Evidence wiring (for later audit & rung transition justification)
  EvidenceGraphId? ,
  PathId[]/PathSliceId[]? ,

  // Optional: cross-context or cross-plane wiring (only when reuse is asserted)
  BridgeId/BridgeCardId? ,
  CL/CL^k/CL^plane? ,
  Φ/Ψ/Φ_plane policy-ids? ,

  // Optional: selector semantics pins (explicit value or resolved via DefaultGoverningDefinitionIndex)
  PortfolioMode? ,
  DominanceRegime? ,

  // Optional: QD / OEE pins (only when those surfaces are declared)
  CharacteristicSpaceRef.edition? ,
  DescriptorMapRef.edition? ,
  DistanceDefRef.edition? ,
  EmitterPolicyRef? ,
  InsertionPolicyRef? ,
  // Optional: Open-ended pins (only when those surfaces are declared)
  GeneratorFamilyRowRef? ,       // exact G.5 <GeneratorFamilyId, rowEdition>
  EnvironmentValidityRegionId? ,
  CouplerPolicyId? ,
  TransferRulesRef.edition? ,

  // Optional: branch/failure wiring (policy-bound)
  FailureBehaviorPolicyId? ,
  SoSLogBranchId[]? ,

  // Optional: authoring traceability (SoTA-of-description)
  AuthoringMethodDescriptionRefs?[] ,

  Notes
⟩
```

**Bundle discipline (normative intent; semantics delegated):**

* `SoS‑LOGBundle@Context` **does not introduce** new legality or normalization rules; it cites the pinned references above.
* Thresholds and numeric gates are cited by id from `G.4` Acceptance (no embedding inside the bundle).
* If cross-context or cross-plane reuse is asserted, crossing pins are made explicit (Bridge/CL/Φ policy ids as required for that use by `G.8:Ext.BridgeReuseWiring`), and evidence paths are citable when available.

**Binding obligations B1–B5 (packaging‑only; wiring‑only; semantics delegated):**

* **B1 — Evidence wiring.** At packaging time the bundle SHOULD provide resolvable evidence refs (typically `A10EvidenceGraphRef?[]` and/or `EvidenceGraphId?`). At run time, admissibility outcomes SHOULD cite `PathId/PathSliceId` when available (`G.6`), so rung transitions and `degrade/abstain` traces are audit‑stable.
* **B2 — CL/plane routing pins.** When reuse across Context or plane is asserted, the bundle/ledger MUST cite the obtaining relation and its separate bounded-use claim and reliance basis. It MUST pin the relevant Bridge/CL/Φ/Ψ/Φ_plane policy ids required for that use by `G.8:Ext.BridgeReuseWiring` (reference‑only; resolvable per `F.8:8.1`). CL and loss-policy pins are mandatory only when required by the actual calibration or separate named assurance account. Any supported penalty MUST follow that assurance policy's declared rule and respect the core penalty routing (penalties affect `R_eff` only; `F/G` invariance via `G.Core`).
* **B3 — `PortfolioMode`/QD fields.** If the bundle/ledger exposes `PortfolioMode`/QD fields (e.g., `PortfolioMode=Archive`), it MUST pin the descriptor/distance/insertion/emitter artefacts (editions/policies as applicable). Illumination remains **report‑only** unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.
* **B4 — Open‑ended fields.** If the bundle binds an open‑ended generator family, it MUST pin `GeneratorFamilyRowRef` and `TransferRulesRef.edition` (and any validity region/coupler policy ids when used). Unknown transfer validity MUST be recorded as `degrade`/branching, not as an ad‑hoc fourth status.
* **B5 — Telemetry hooks.** On any material telemetry event (illumination increase, archive insertion, probe accounting update, open‑ended coverage/regret proxy update), the emitted telemetry pins SHOULD include the controlling policy ids plus the relevant edition pins (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `TransferRulesRef.edition`) and, when available, `PathSliceId` to keep RSCR planning auditable.

#### G.8:4.4 - `AdmissibilityLedger@Context` (run‑time view; selector‑facing)

A conforming ledger is a UTS‑published view (or a view‑projection of a Work/Audit artefact) with rows of the form:

`⟨ MethodFamilyRowRef, TaskSignatureRef, SoSLogRuleId, RuleEdition, EvidenceProfileRef, ClaimScope, QualificationWindow, IntendedAdmissionUse, EligibilityVerdict, CGSpecVerdict, AcceptanceVerdictRefs?, PolicyEditionRefs[], GuardDecision ∈ {pass|degrade|abstain}, DegradeMode?/SoSLogBranchId[]?, MaturityRungId?, AcceptanceClauseId[]?, EvidencePathRefs?, CrossingPins?, PortfolioMode?, DominanceRegime?, Edition ⟩`

The bundle, maturity card, and ledger bind one exact G.5 `MethodFamilyRowRef = <MethodFamilyId, rowEdition>`; an open-ended generator use also binds `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>`. Their own publication `Edition` does not replace either registry-row edition. Preserve the rule edition and the C.23 admission basis: evidence profile, claim scope, qualification window, intended use, consulted verdicts, and policy editions. An unresolved required reference blocks only the result that depends on it; never resolve an old result against the current row by default.

Where `EvidencePathRefs` are typically `PathId[]/PathSliceId[]` when `G.6` is in use (or resolvable), and “CrossingPins” are the explicit Bridge/CL/Φ policy pins required for the stated reuse by `G.8:Ext.BridgeReuseWiring`, together with citable references to its separate bounded-use claim and reliance basis.

#### G.8:4.5 - Maturity ladder as a citable poset (published card)

`MethodFamily.MaturityCardDescription@Context` names the exact `MethodFamilyRowRef`, evidence profile, claim scope and selected slices, qualification window, and intended admission use required by C.23. It is published with:

* closed rungs (UTS‑registered identifiers),
* `Scale kind = ordinal` and a declared `ReferencePlane`,
* (optional) explicit poset edges / precedence constraints,
* rung transition justifications that cite evidence paths (typically `G.6` paths).

This card is a **description** suitable for dispatch/audit and refresh; it is not a competing governing spec ref.

#### G.8:4.6 - Interfaces (minimal I/O standard; conceptual)

| Interface                               | Consumes                                                                                   | Produces                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **G.8‑1 `Publish_LOGBundle`**           | `MethodFamilyRowRef`, `SoSLogRuleId[]` with rule editions (C.23), pins to Acceptance/Evidence/Crossings (as applicable) | `SoS‑LOGBundle@Context` (UTS row)                                                     |
| **G.8‑2 `Publish_AdmissibilityLedger`** | Bundle + run‑time branch outcomes + evidence path refs (when available)                    | `AdmissibilityLedger@Context` (UTS row or UTS‑citable view)                           |
| **G.8‑3 `Publish_MaturityCard`**        | Ladder description + (optional) evidence path refs for rung transitions                    | `MaturityCardDescription@Context` (UTS row; editioned)                                |
| **G.8‑4 `Expose_TelemetryHooks`**       | QD/OEE/archive/open‑ended telemetry signals (when declared)                                | telemetry pins for refresh (`…Ref.edition`, policy‑ids, `PathSliceId` when available) |

### G.8:5 - Extensions (pattern‑scoped; non‑core)

`G.8` keeps method/generator specificity out of the core kit. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s.

#### G.8:5.1 - `G.8:Ext.SoSLOGWiring`

**PatternScopeId:** `G.8:Ext.SoSLOGWiring`
**GPatternExtensionId:** `SoSLOGWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.23`
**Uses:** `{C.23}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoSLogRuleId[]`
* `SoSLogBranchId[]?`
* `FailureBehaviorPolicyId?` *(when degrade behaviour is policy‑bound)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.8:4.1`)*
**Notes (wiring‑only):**
* Rule meaning, branch taxonomy, and “probe/sandbox” semantics are governed by `C.23`; this module only binds ids and pins.

#### G.8:5.2 - `G.8:Ext.AcceptanceWiring`

**PatternScopeId:** `G.8:Ext.AcceptanceWiring`
**GPatternExtensionId:** `AcceptanceWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.4`
**Uses:** `{G.4}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `AcceptanceClauseId[]`
* `EvidenceProfileId[]?` *(if the ledger/bundle cites evidence profile ids rather than only paths)*
* `PromotionPolicyId?` *(only if telemetry may be promoted into dominance by explicit CAL policy)*

**RSCRTriggerKindIds (optional delta):** `{RSCRTriggerKindId.PolicyPinChange}` *(only if acceptance policies are pinned as ids in the bundle/ledger)*
**Notes (wiring‑only):**
* Thresholds remain governed by `G.4` Acceptance; this module carries only clause ids and policy pins.

#### G.8:5.3 - `G.8:Ext.BridgeReuseWiring`

**PatternScopeId:** `G.8:Ext.BridgeReuseWiring`
**GPatternExtensionId:** `BridgeReuseWiring`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.7`
**Uses:** `{G.7, F.9, A.10, B.3}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum; conditional on the stated use):**

* `BridgeId/BridgeCardId` *(the obtaining Bridge actually used; a `BridgeCardId` is needed only when that Card is relied on)*
* `CL/CL^k/CL^plane` *(when cited; the applicable values are mandatory when required by the `G.7` calibration or named `B.3` assurance account)*
* `Φ/Ψ/Φ_plane policy-ids` *(only the policy ids and editions required by the actual `G.7` calibration or named `B.3` assurance account; reference‑only and resolvable per `F.8:8.1`)*
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(both required when calibration evidence is cited, together with the row locator and active policy pins required by `G.7` `CC‑G7‑SCRLinkage‑1`)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration records by id)*
**Notes (wiring‑only):**
* Present only when `SoS‑LOGBundle@Context` asserts cross-Context or cross-plane reuse. No additional crossing semantics are defined here.
* The wiring MUST keep the obtaining Bridge reference, the separate bounded-use claim (use, direction, rule, and tolerated loss), and the `A.10` reliance basis citable. A separate named assurance use also cites its exact target claim, receiving use, and `B.3` assurance basis/result. Required CL values, policy editions, and evidence remain mandatory for that account; a supported loss penalty is applied only under the assurance policy's declared rule, to `R_eff` only. Ordinary supported reuse does not require a CL shorthand, calibration record, loss-policy id, or assurance claim merely to fill the package.

#### G.8:5.4 - `G.8:Ext.QDArchiveTelemetry`

**PatternScopeId:** `G.8:Ext.QDArchiveTelemetry`
**GPatternExtensionId:** `QDArchiveTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `EmitterPolicyRef`
* `InsertionPolicyRef`
* `CharacteristicSpaceRef.edition?` *(required iff cell boundaries / de‑dup / parity depend on the space definition)*

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* Archive/illumination signals are telemetry; promotion into dominance is only via explicit `G.4` policy pins.

#### G.8:5.5 - `G.8:Ext.ExploreExploitTelemetry`

**PatternScopeId:** `G.8:Ext.ExploreExploitTelemetry`
**GPatternExtensionId:** `ExploreExploitTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19`
**Uses:** `{C.19}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExploreExploitBudgetPolicyId?`
* `ProbeAccountingId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring‑only):**
* When “probe/sandbox” is used, the controlling policy ids are pinned and recorded in the ledger/bundle trace.

#### G.8:5.6 - `G.8:Ext.OpenEndedWiring`

**PatternScopeId:** `G.8:Ext.OpenEndedWiring`
**GPatternExtensionId:** `OpenEndedWiring`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5` *(generator family registry surface; algorithm semantics remain external to Part‑G core)*
**Uses:** `{G.5}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `GeneratorFamilyRowRef`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by a governing-pattern policy.

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle cites `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`) and cites `AcceptanceClauseId[]` for any floors (governed by `G.4`). The run‑time `AdmissibilityLedger` cites `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.

**Show‑B — QD archive dispatch with edition‑pinned descriptors (post‑2015 QD families).**
A method family uses a modern QD line (e.g., CMA‑ES‑driven archives, differentiable QD variants, and large‑scale JAX‑style QD toolchains). The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show‑C — Open‑ended environment–method co‑evolution (post‑2018 open‑ended families).**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

### G.8:7 - Bias‑Annotation

Scope: packaging kit only. Rule semantics remain governed by `C.23`; thresholds remain governed by `G.4`; evidence path semantics remain governed by `G.6`; selection semantics remain governed by `G.5`.

### G.8:8 - Conformance Checklist (CC‑G8)

* **CC‑G8‑CoreRef (G.Core conformance bridge).**
  A conforming `G.8` SHALL satisfy the **effective** set of `CC‑GCORE‑*` obligations implied by `G.8:4.1` (expanded per `G.Core:4.2`), including required pins, trigger sets, and Default Governing Definition Index citation.

* **CC‑G8‑1 (No thresholds in LOG).**
  Any numeric gate, maturity floor, or threshold SHALL be authored as a `G.4` Acceptance artefact and cited by id; the LOG bundle/ladder SHALL NOT embed thresholds.

* **CC‑G8‑2 (Tri‑state discipline; delegated).**
  Guard outcomes SHALL obey the tri‑state domain and unknown handling defined in `G.Core` (delegation to `CC‑GCORE‑GUARD‑1`).
  Any sandbox/probe‑only behaviour SHALL be represented as an explicit `C.23` branch and MUST pin (and record) the controlling policy id (typically an E/E‑LOG policy id via `C.19`), rather than inventing a fourth status or silently coercing unknowns.

* **CC‑G8‑3 (Path citation when evidence is path‑addressable).**
  When `G.6` is in use (or resolvable), every recorded `pass/degrade/abstain` outcome in the `AdmissibilityLedger` MUST cite `PathId/PathSliceId` (run‑time). At packaging time, the bundle/ledger SHALL at minimum provide resolvable evidence refs (e.g., `EvidenceGraphId?` + anchor refs).

* **CC‑G8‑4 (Crossing visibility and penalty routing; delegated).**
  Any cross-Context or cross-plane reuse asserted by the bundle/ledger SHALL satisfy the core crossing visibility and penalty routing invariants (delegation to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`).

* **CC‑G8‑5 (PortfolioMode/dominance hygiene; delegated).**
  The bundle/ledger SHALL treat `PortfolioMode` and dominance fields as pinned inputs and SHALL cite the governing definition for each omitted default through `G.Core.DefaultGoverningDefinitionIndex` (delegation to `CC‑GCORE‑DEF‑1` and `CC‑GCORE‑SET‑1`; governing definitions include `CC‑G5.23` for `DefaultId.PortfolioMode` and `CC‑G5.28` for `DefaultId.DominanceRegime`). It MUST NOT restate default values locally.
  If the bundle/ledger records telemetry that could influence dispatch (e.g., illumination/QD/OEE/open‑ended proxies), such telemetry SHALL remain report‑only unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.

* **CC‑G8‑6 (QD/OEE edition discipline).**
  When QD/OEE surfaces are declared, the bundle/ledger MUST pin the relevant editions and policies (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies, and `TransferRulesRef.edition` when applicable).
  `CharacteristicSpaceRef.edition` is **required iff** cell boundaries / de‑dup rules / parity depend on the space definition, and MUST NOT be used as a substitute for `DescriptorMapRef.edition`.

* **CC‑G8‑7 (Maturity is ordinal/poset).**
  Maturity ladders SHALL be authored as ordinal/poset descriptions with **closed** rung ids (`MaturityRungs`, UTS‑registered) and a declared `ReferencePlane`, and SHALL be published as a citable UTS artefact (editioned; twin‑register safe).
  Rung transitions, when asserted, MUST be justifiable by citable evidence paths (when available).

* **CC‑G8‑8 (Spaces ≠ Maps).**
  `CharacteristicSpace` and `DescriptorMap` SHALL remain strictly distinct kinds; naming and twin‑register discipline must be respected.

* **CC‑G8‑9 (Notational independence).**
  The bundle, ledger, and maturity card SHALL remain notation‑independent (per `E.5.2`); any serialization choice is non‑normative and belongs outside Part‑G core.

* **CC‑G8‑10 (MOO cross‑reference).**
  When a LOG bundle is used to drive or justify a produced selected-set outcome, the record of the producing Work, or the audit artefact, SHOULD cite the controlling mechanism ids (e.g., parity/shipping/refresh artefact ids) and relevant policy pins; no “black box” provenance.

* **CC‑G8‑11 (SoTA‑of‑description trace).**
  If authoring methods (e.g., discovery, clustering, summarisation) materially shaped rule text or rung definitions, the bundle/card SHOULD cite their method description refs (edition‑pinned) to support cross‑stance traceability.

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by a governing-pattern policy pin.

* **Anti‑pattern:** Publishing a bundle that “implies” cross‑context reuse without its required relation/use/reliance pins, or omits CL/Φ pins required by the actual calibration or named assurance use.
  **Avoid:** if reuse is asserted, publish the crossing pins required by `G.8:Ext.BridgeReuseWiring` for that use; otherwise downstream must abstain from reuse.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

### G.8:10 - Consequences

* **Positive:** `G.5` receives a stable, citable, selector‑facing artefact without importing rule semantics or threshold logic.
* **Positive:** Audit and refresh become tractable: pins, crossings, evidence paths, and trigger kinds are explicit.
* **Positive:** Maturity remains non‑scalar, reducing illegitimate aggregation and “readiness theater”.
* **Negative:** Requires stricter authoring discipline (UTS publication, pin completeness, explicit wiring).
* **Negative:** Without maintained G.6 paths, a later reader may need more work to recover the cited evidence. Evaluate the resolvable A.10 anchors and their support for the stated use; absence of a graph alone does not lower evidence-support class. If a required basis cannot be recovered, abstain from the dependent use.

### G.8:11 - Rationale

`C.23` governs **rule semantics**, `G.4` governs **thresholding/acceptance**, `G.6` governs **path‑addressable provenance**, and `G.5` governs **selection/registry semantics**. A dedicated packaging kit lets projects cite those sources in one auditable dispatch surface instead of duplicating semantics inside ad‑hoc “decision bundles” (creating shadow specs). `G.8` keeps these boundaries strict while providing a single, consumable surface.

### G.8:12 - SoTA‑Echoing (informative; post‑2015 practice alignment)

This pattern’s separation of **decision rules**, **acceptance thresholds**, **provenance paths**, and **set‑valued outputs** echoes post‑2015 practice in:

* **Set‑valued / set-returning selection** (multi‑objective and uncertainty‑aware regimes; avoiding forced scalar winners).
* **Quality‑Diversity and archive‑based evaluation** (post‑2015 QD variants emphasize edition‑pinned descriptors/distances and telemetry‑driven refresh).
* **Open‑endedness / curriculum generation** (post‑2018 lines emphasize explicit transfer rules, safe degrade branches, and telemetry‑driven orchestration rather than hidden gates).
* **Reproducibility‑aware publishing** (explicit identifiers, pinned editions/policies, citable traces rather than prose‑only decision rationales).

*(Examples are illustrative; they do not introduce new Part‑G‑wide norms.)*

### G.8:13 - Relations

**Builds on:** `G.Core`, `C.23`, `G.4`, `G.6`, `G.5`, `C.22`
**Uses:** `A.10` (anchors), `F.8` (policy-id resolvability), `F.9` (cross-semantic relation and bounded-use claims), `F.17`/`E.17` (crossing publication surfaces), `G.7` (when calibration is used), `B.3` (when a separate named assurance use is made), `G.11` (refresh planning/trigger consumption), `G.10` (shipping boundary; if bundled artefacts are shipped), `E.10` (LEX twin registers), `E.5.2` (notation independence), `E.18` (crossing visibility when a selected transformation-flow structure is in use), `A.21` (gate decisions under an applicable profile); optional `C.18` (QD) / `C.19` (E/E‑LOG) when those surfaces are declared.
**Publishes to:** `UTS` (bundle/ledger/card), `G.5` (selector/registry consumption), `G.11` (refresh via typed triggers and pinned telemetry)
**Constrains:** any SoS‑LOG packaging that claims FPF conformance for selector‑facing dispatch across method families.

### G.8:14 - Author’s quick checklist (informative)

* [ ] `SoSLogRuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Any cross-Context or cross-plane reuse is explicit: `BridgeId/BridgeCardId` and the separate bounded-use claim and reliance basis are citable. `CL/CL^k/CL^plane` and `Φ/Ψ/Φ_plane` policy ids and editions are pinned when required by the actual calibration or named assurance account, per `G.8:Ext.BridgeReuseWiring` (policy ids resolvable per `F.8:8.1`).
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] QD pins are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de‑dup/parity depend on it; **Spaces ≠ Maps**.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyRowRef`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity is recorded as `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

### G.8:End

## G.9 — Parity and Benchmark Harness

> **Status:** Stable

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

#### G.9:0.1 — What goes wrong if missed

- benchmark reports present numbers from different windows, baselines, or comparator editions as comparable
- reuse across distinct source-local meanings, a reference-plane crossing, or a normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

#### G.9:0.2 — What this buys

- one exact `ParityPlanRef` that fixes the plan edition, baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport` that cites that exact plan and echoes its active baseline binding, pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs for one explicit subject—either one `EntityOfConcernRef` or target refs under their existing subject patterns—with a `ReferencePlane`, scope, window, applicable rules, CSLC comparability and admissibility references, comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`), and reproducibility pins for editions and policy ids;
* executes parity in a way that **G.5** can consume, with selected-set outcomes and a DRR and SCR evidence trace;
* publishes an edition-pinned **ParityReport** suitable for downstream consumption, shipping, refresh wiring, and RSCR.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window and freshness regime,
* comparator semantics, including any normalization or comparability mapping,
* the active C.21 replay basis when DHC coordinates are compared, including the exact Characteristic, Scale, measurement definition, Method, MethodDescription or model, and time or population basis,
* reuse across distinct F.17 source-local meanings or ReferencePlanes (the obtaining relation, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9 makes these comparison inputs and outcomes recoverable through published pins as part of its *method-of-obtaining-outputs* (MOO) disclosure, without introducing new governing spec refs.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement and comparator definitions. When DHC, QD, or OEE modes are used, the required definition pins are introduced only through the corresponding `Extensions` blocks; omit them when unused.
* **Telemetry versus objectives.** `IlluminationSummary`, coverage, and regret are report-only telemetry by default. A dominance change needs an explicit CAL policy id recorded in the audit pins.
* **Crossing visibility.** Every crossing used by parity must be visible and auditable through its `CrossingBundle` and `GateCrossing` checks; failure blocks publication or use of the parity result.
* **Cross-sense and reference-plane reuse.** When expressions have distinct F.17 source-local meanings, recover both cells and establish the required F.9 relation; a ReferencePlane crossing follows its own declared crossing basis. Each actual crossing carries explicit pins, its audit evidence relation, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

### G.9:4 — Solution
#### G.9:4.0 — G.Core linkage (normative)

This pattern binds to **G.Core** through the following manifest.

**GCoreLinkageManifest (G.9)** *(normative; expands per `G.Core:4.2`)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`
  }

* `RSCRTriggerSetIds` := {
  `GCoreTriggerSetId.CGSpecGate`
  }
* `RSCRTriggerKindIds` := {
  `RSCRTriggerKindId.EvidenceSurfaceEdit`,
  `RSCRTriggerKindId.PenaltyPolicyEdit`,
  `RSCRTriggerKindId.BaselineBindingEdit`,
  `RSCRTriggerKindId.TelemetryDelta`
  }
  *(Pattern-local deltas; cross-tradition or Bridge-calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over-trigger parity runs that use one already recovered meaning and ReferencePlane.)*

* `DefaultsConsumed` := {
  `DefaultId.DominanceRegime`,
  `DefaultId.PortfolioMode`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Defaults are cited through `G.Core.DefaultGoverningDefinitionIndex` (not restated here); the expected default governing definitions are `CC‑G5.28`, `CC‑G5.23`, and `CC‑G5.4` respectively.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `ComparatorSpecRef.edition`,
  `TaskSignatureRef?`, `TaskMapRef?`, *(when a selector consumes the parity result; TaskMapRef only when its G.4 CAL gates are current)*
  `entityOfConcernRef?`, `targetRefs[]?`, *(exactly one subject branch)*
  `ClaimScope`, `EvaluationWindow`, `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlannedFillingRows[]?`,
  `EvidenceGraphId`,
  `Budgeting?`,
  `EpsilonDominance?`,
  `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`,
  `SCPRef.edition?`, `MinimalEvidenceRef.edition?`
  }
*(Nil‑elision applies; mode‑specific definition pins are introduced only by the corresponding `GPatternExtension` blocks.)*

* `TriggerAliasMapRef` := `∅`

#### G.9:4.1 — Objects and publication records

All objects below are **notation‑independent**; serialisations (if any) are handled in shipping and interop publication forms, not here.

**(1) `ParityPlan`** *(one exact `U.WorkPlan` episteme; `ParityPlan` is the local application name)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan := ⟨
  ParityPlanId(UTS),                       // continuing plan lineage
  planEdition,                            // one immutable edition
  CGFrameId?,                              // exact cited CG frame when the plan depends on one
  TaskSignatureRef?, TaskMapRef?,           // conditional G.5 input; TaskMap only for current G.4 CAL gates
  entityOfConcernRef? := EntityOfConcernRef, // one-EntityOfConcern branch only
  targetRefs[]?,                            // exact-target branch only; existing kinds and editions
  groundingHolonRef := GroundingHolonRef,
  referencePlaneRef := ReferencePlane,
  claimScopeRef := ClaimScope,
  EvaluationWindow,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  BaselineSet,                            // exact method-family or generator-family targets (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  EvidenceGraphId, PathId[], PathSliceId?,
  PlannedFillingRows[]?                    // declaration-local A.15.3 content inside this WorkPlan; no independent row refs
⟩`

`ParityPlanRef := <ParityPlanId, planEdition>` designates one immutable plan edition. Changing its subject, baseline binding, comparator edition, or another active value that can change the run or its interpretation creates a new `planEdition`. When a G.5 selector consumes this comparison, pin its exact `TaskSignatureRef` in the plan. If that selector uses G.4 CAL gates, also pin its exact `TaskMapRef` and require the map's task-signature reference to match. Omit these selector inputs from a parity run that needs no selector. The lineage id may remain only while this is still the same continuing plan; old `ParityPlanRef` values continue to resolve their old editions.

Exactly one subject branch is present. Use `entityOfConcernRef` when the report compares results about one EntityOfConcern. Use `targetRefs[]` when the targets themselves are compared; each ref keeps the kind and edition defined by its existing subject pattern. In particular, a G.5 method-family target is an exact `MethodFamilyRowRef`, and a generator-family target is an exact `GeneratorFamilyRowRef`.

For example, a direct comparison of `<ThresholdTrendReview-local, R3>` and `<SpectralResidualReview-local, R2>` puts those two exact row refs in `targetRefs[]`; the plan may explicitly use the same two refs as its `BaselineSet`. A comparison of their results for `Pump-P17` instead puts `Pump-P17` in `entityOfConcernRef`, leaves `targetRefs[]` absent, and uses `BaselineBindingRef` to say how the two method rows supply results about that pump.

`BaselineSet` names the alternatives treated as the comparison baseline; it supplies `targetRefs[]` only when the plan explicitly says that the same exact refs serve both purposes. Otherwise the subject and baseline remain separate, and `BaselineBindingRef` records how that baseline applies to the named subject. These exact values determine what is compared and when the parity claim is usable; do not add `ParityContextId`. If the plan relates expressions with distinct source-local meanings, first recover the exact F.17 cells and establish the required F.9 relation. A shared label, source note, or generic context identifier does not establish comparability.

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by a parity run under one exact `ParityPlanRef`. Work or audit occurrence claims use `A.15`/`A.15.1`; evidence-path claims use `A.10`/`G.6`; a separate named assurance claim uses `B.3`; and a gate decision uses `A.21` under its applicable profile. Keep each such occurrence, path, or result distinct from the report.

`ParityReport := ⟨
  ParityReportId(UTS),
  parityPlanRef := ParityPlanRef,
  entityOfConcernRef?, targetRefs[]?,        // exactly one subject branch is present
  TaskSignatureRef?, TaskMapRef?,           // echoed when the selector branch is used
  groundingHolonRef, referencePlaneRef,
  claimScopeRef, EvaluationWindow,
  BaselineSet, BaselineBindingRef, FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // parity/comparison results; G.5 output refs only when selection is current
  EpsilonDominance?,                        // echoed when used
  AbstainReasons[]?,                        // ids/labels (policy-bound) for abstain/degrade; refusal paths included
  TelemetrySummary? := ⟨IlluminationSummary?, coverage?, regret?⟩,  // report-only by default; promotion requires CAL policy-id pins
  GuardOutcomeTraceRef?,                    // pass/degrade/abstain trace + cited reasons (policy-bound)
  EvidenceTrace := ⟨EvidenceGraphId, PathId[], PathSliceId?⟩,
  CrossingPins?,                            // Bridge/CL/Φ/Ψ/Φ_plane pins, when crossings are invoked
  EditionPinsDelta?,                        // explicit list of edition pins actually active during the run
  PolicyPinsDelta?,                         // explicit list of policy-ids actually active during the run
  RSCRRefs[]                                // parity RSCR test ids / trigger emissions
⟩`

The report carries the exact `ParityPlanRef` and echoes the `BaselineBindingRef` used in that edition. For example, if `<PumpParityPlan, E4>` used `PumpBaselineBinding-E7` and a later `E5` changes the binding or comparator, an old report still resolves `E4` and `PumpBaselineBinding-E7`. A missing historical plan edition or binding is an unresolved required input; it is never replaced with the current value.

**Naming discipline.**

* Head names follow the existing kind definitions and LEX discipline.
* The older labels `ParityPlan@Context` and `ParityReport@Context` are retired. The suffix named neither identity nor comparison basis; current records are `ParityPlan` and `ParityReport`, with all operative conditions carried in explicit fields and exact refs.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (one exact `U.WorkPlan`)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the exact `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) used as the comparison baseline. When SoS-log or source-maturity values change baseline eligibility or interpretation, cite `SoS‑LOGBundleId?` and the source-maturity ids by reference; acceptance-gate thresholds remain in `G.4` Acceptance.
2. **Bind subject, scope, and evaluation window.** Choose exactly one subject branch: one `entityOfConcernRef`, or exact `targetRefs[]` under their existing kinds and editions. For G.5 families, use `MethodFamilyRowRef` or `GeneratorFamilyRowRef`, not a bare lineage id. Then fix `groundingHolonRef`, `referencePlaneRef = ReferencePlane`, one exact `ClaimScope`, and `EvaluationWindow`; record them without silent widening, narrowing, collapse of an EntityOfConcern into the grounding holon, or window drift.
3. **Define baseline-set reference.** Declare what counts as the baseline and how it applies to the selected subject in `BaselineBindingRef` (for example, through an EvidenceGraph path slice or an upstream shipped package or publication-record id). If `BaselineSet` also supplies the exact compared targets, say so and use the same refs by value; otherwise keep baseline and subject refs distinct.
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

   When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned fillings when applicable.** If parity depends on planned slot fillings, this WorkPlan contains the relevant A.15.3 rows in `PlannedFillingRows[]`; each row points to a declaration member defined by its own pattern and has no independent reference or identity. Omit the field when no such row is needed.
10. **Publish the relation and its receiving use (when invoked).** For distinct recovered F.17 meanings, establish the F.9 relation and the separate bounded-use claim and matching reliance. Cite G.7 calibration, CL and policy pins when that account uses them; its summary does not decide parity admissibility. Kind correspondence also requires receiving admissibility and fresh target classification under C.3.3. A plane relation keeps its own basis. Supported penalties affect R only under the receiving model.

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; apply the eligibility or acceptance checks required by the pinned comparison and refuse or abstain on non-admissible operations. When the G.5 branch is current, use the exact planned `TaskSignatureRef` and the matching `TaskMapRef` when G.4 CAL gates apply; record the branch trace under its own result vocabulary. If a live `A.21` gate consumes this check, cite its exact `GateDecisionResult`; cite a `DecisionLog` only when that optional audit or reuse record is needed. The profile application and its action consequence remain governed by A.21; do not create a `G.9`-local CSLC gate.
2. **Run the comparison and any required selection.** Apply the pinned comparator to the admissible comparison inputs and retain its lawful result shape in `ParityReport`. If a selector-facing result is required, apply **G.5** under the plan's exact task and conditional map refs and publish its declared outcome. An ordinary parity or benchmark report ends without G.5 when no selector result is needed.

   When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record the comparability mapping when used.** If `UNM_id?`, `NormalizationMethodId[]?`, or `NormalizationMethodInstanceId[]?` was declared, echo it in `ParityReport` or its explicit pins delta. Record the ids and any scoped notes required by the cited specification in the audit pins and SCR; cite the applicable `PathId` values.
4. **Publish trace.** Emit `ParityReport` with the exact `ParityPlanRef`, its `BaselineBindingRef`, conditional selector input refs, EvidenceGraph citations, and all active edition and policy-id pins, so the run can be checked and run again.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

**Ordinary case: compare two pump-triage method rows.** The team from the G.5 example wants a reproducible comparison of the two exact selector-row editions, not a claim that one Method is universally better. Both rows use the same scheme, units, and ReferencePlane, so no normalization or crossing branch is needed.

```text
ParityPlanRef = <PumpTriageParity, E1>
targetRefs = [<ThresholdTrendReview-local, R3>,
              <SpectralResidualReview-local, R2>]
entityOfConcernRef = absent
groundingHolonRef = PumpMaintenanceProgram-H1
referencePlaneRef = PumpVibrationTriage-RP1
claimScopeRef = PumpFleet-F7-VibrationTriageClaims-E1
EvaluationWindow = 2026-08-01T00:00Z .. 2026-08-07T23:59Z
BaselineSet = [<ThresholdTrendReview-local, R3>,
               <SpectralResidualReview-local, R2>]
BaselineBindingRef = PumpTriageBaselineBinding-E1
FreshnessWindows = { sensorSeries: at-most-24h-old-at-run,
                     evidencePath: at-most-72h-old-at-run }
CNSpecRef.edition = PumpCN-E2
CGSpecRef.edition = PumpCG-E4
ComparatorSpecRef.edition = PumpTriageComparator-E3
TaskSignatureRef = PumpVibrationTriage-T1
TaskMapRef = absent                         // this G.5 case uses no G.4 CAL gate
ParityPinSet = [PumpCN-E2, PumpCG-E4, PumpTriageComparator-E3, PumpVibrationMeasureSpec-E2]
EvidenceGraphId = PumpTriageEvidence-E5
PathId[] = [PumpReadings-P7, ComparatorRun-P3]
PathSliceId = PumpParitySlice-S2
expected selector result = unordered Shortlist
```

The plan explicitly says that `BaselineSet` and `targetRefs[]` contain the same two row refs. `EvaluationWindow` bounds the observations and results included in the comparison. `FreshnessWindows` asks a different question at run or reuse time: whether each required input and evidence path is still recent enough to rely on. A report from this run carries `parityPlanRef=<PumpTriageParity, E1>`, `BaselineBindingRef=PumpTriageBaselineBinding-E1`, the same evidence path, and the unordered `Shortlist`; it does not invent a scalar winner.

**Conditional specialization case.** Loop-engineering parity may add further pins after the ordinary comparison boundary above is complete. An evaluation program, benchmark script, or dashboard is part of the evaluation or comparison procedure; it is not the Characteristic being improved.

- Two agentic search setups both claim bounded specialization on the same declared task family.
- Their `ParityPlan` also pins the same threshold target, adaptation budget, prior-exposure declaration, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- Their CSLC-admissible `ParityReport` states what was held constant, which signals remained telemetry, and why the outcome stays a selected set or partial order rather than collapsing into a scalar winner. These specialization values extend the complete comparison boundary; they do not replace its subject, scope, windows, baseline binding, comparator editions, or evidence.

#### G.9:4.3b — Conditional causal method rung parity

Use this extension only when a parity report compares causal methods or causal-use claims. Start with a cheap screen and stop at degraded parity or abstention when the methods answer different questions.

```text
CausalRungParityScreen:
  comparedMethodsRef
  targetCausalityLadderRungSet
  causalSupportComponentTypeSet
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  sameTransportEndpoints: yes | no | unclear
  cheapParityStop:
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportComponentsDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    differentEndpointsAbstain |
    returnToC28
```

`causalSupportComponentTypeSet` records which methods rely on evidence paths/data regimes, identification, estimates, direct counterfactual sampling, simulation, or transport. Difference is not an automatic ban, but it must be exposed and bridged; one label cannot make unlike components equivalent.

Open the full record only when comparison remains meaningful:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  causalEstimandRef: CausalEstimandRef
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalSupportComponentRefs: CausalSupportComponentRefs
  declaredCausalSupportLossRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  sourceDomainRef?
  targetDomainRef?
  sourceEnvironmentRef?
  targetEnvironmentRef?
  sourceDataGeneratingRegimeRef?
  targetDataGeneratingRegimeRef?
  transportabilityResultRef?
  estimateResultRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

The record names every changed transport endpoint that matters; population and semantic scheme do not substitute for domain, environment, or data-generating regime. Different rungs, estimands, windows, endpoints, or support components require a bridge/loss, degraded parity, or abstention. G.9 makes the parity conclusion; C.28 supplies the cited causal-support result and does not authorize the benchmark conclusion.

#### G.9:4.9 — Extensions (pattern‑scoped; non‑core)

Most working readers can stop after `G.9:4.3a`. The blocks below are binding-only wiring records used only when the corresponding parity mode is actually active.

The following blocks store **wiring only** (pins/refs/policy‑ids, relevant triggers, and `Uses`), while semantics remains defined in the referenced patterns.

**GPatternExtension block: `G.9:Ext.CrossTraditionParity`**
**GPatternExtension: CrossTraditionParity**
* **PatternScopeId:** `G.9:Ext.CrossTraditionParity`
* **GPatternExtensionId:** `CrossTraditionParity`
* **GPatternExtensionKind:** `DisciplineSpecific`
* **GoverningPatternId:** `G.7`
* **Uses:** `{G.7, F.9, E.18, A.21}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `BridgeId/BridgeCardId[]`
  * `BridgeMatrixId?`
  * `CalibrationLedgerId?` / `BCT.id?`
  * `RegressionSetId?` / `SentinelId[]?` *(when sentinel wiring is used)*
  * `CL/CL^k/CL^plane`
  * `Φ(CL) policy-id`, `Φ_plane policy-id`, `Ψ(CL^k) policy-id?`
  * `CrossingBundleId?`
* **RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(preferred; expands in `G.Core`)*
* **RSCRTriggerKindIds (delta, if any):** `∅`
* **Notes (wiring-only):** This block does not define CL/Φ/Ψ semantics; it only requires the pins needed to cite calibration records and crossing visibility bundles.

**GPatternExtension block: `G.9:Ext.SoSLogGuardNarration`**
**GPatternExtension: SoSLogGuardNarration**
* **PatternScopeId:** `G.9:Ext.SoSLogGuardNarration`
* **GPatternExtensionId:** `SoSLogGuardNarration`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.23`
* **Uses:** `{C.23, G.6, G.4}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `SoSLogRuleId[]` / `BranchId[]` *(ids as cited labels; semantics come from `C.23`)*
  * `FailureBehaviorPolicyId/SoSLogBranchId`
  * `EvidenceTrace.PathId[]` / `PathSliceId?`
  * `AcceptanceClauseId[]` *(when referenced)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Explains **why** a parity run degraded/abstained by citing SoS‑LOG ids and evidence paths; does not redefine guard semantics.

**GPatternExtension block: `G.9:Ext.DHCParityPins`**
**GPatternExtension: DHCParityPins**
* **PatternScopeId:** `G.9:Ext.DHCParityPins`
* **GPatternExtensionId:** `DHCParityPins`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.21`
* **Uses:** `{C.21}`
* **⊑/⊑⁺:** `∅`
* **Required replay values and pins (minimum; conditional on DHC parity):**
  * `DisciplineRef`
  * `IntendedUse`
  * `ClaimScopeRef`
  * `ComparisonBasis`
  * `CharacteristicRef.edition`
  * `ScaleRef.edition`
  * `UnitRef.edition?`
  * `DHCMethodRef.edition`
  * `MethodRef`
  * `MethodDescriptionRef.edition?`
  * `MeasurementModelRef.edition?`
  * `CalibrationBasisRef?`
  * `TimeOrPopulationBasis`
  * `DHCDefinitionSetRef.edition?`
  * `TargetSliceRef?`
  * `DistanceDefRef.edition?`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* **Notes (wiring-only):** Carry exactly the active fields of the C.21 replay basis. `TargetSliceRef` appears only when the parity computation consumes that A.2.6 selection and states its relation to `ClaimScopeRef`. Compatible same-semantics readings use the admitted C.16 comparison basis directly; actual distinct-local-sense use also cites the obtaining F.9 relation, direction, admitted use, and loss. C.21 defines the DHC semantics.

**GPatternExtension block: `G.9:Ext.QDArchiveParity`**
**GPatternExtension: QDArchiveParity**
* **PatternScopeId:** `G.9:Ext.QDArchiveParity`
* **GPatternExtensionId:** `QDArchiveParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.18`
* **Uses:** `{C.18, C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DescriptorMapRef.edition`
  * `DistanceDefRef.edition`
  * `CharacteristicSpaceRef.edition?` *(when discretisation/topology is referenced)*
  * `EmitterPolicyRef`
  * `InsertionPolicyRef`
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Post‑2015 QD families are referenced here only as wiring + edition/policy pin obligations (semantics come from `C.18`/`C.19`/`G.5`).

**GPatternExtension block: `G.9:Ext.OEEParity`**
**GPatternExtension: OEEParity**
* **PatternScopeId:** `G.9:Ext.OEEParity`
* **GPatternExtensionId:** `OEEParity`
* **GPatternExtensionKind:** `MethodSpecific`
* **GoverningPatternId:** `C.19`
* **Uses:** `{C.19, G.5}`
* **⊑/⊑⁺:** `∅`
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `TransferRulesRef.edition`
  * `EnvironmentValidityRegionId`
  * `ExplorationBudgetPolicyId?`
  * `EvidenceTrace.PathSliceId?` *(for transfer‑keyed events)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
* **Notes (wiring-only):** Open‑ended parity is expressed as policy/edition pins + telemetry wiring, not as new core norms.

### G.9:5 — Interfaces (minimal I/O; conceptual)

| Interface                          | Consumes                                                                                                                                         | Produces                                                                                        |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **G.9‑1 `Plan_Parity`**            | exactly one subject branch—one `EntityOfConcernRef` or exact `targetRefs[]` under their existing kinds and editions—plus `GroundingHolonRef`, `ReferencePlane`, `ClaimScope`, `EvaluationWindow`, `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, mode-specific measurement or normalization editions when used, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `EvidenceGraphId`, `PathId[]`, `PathSliceId?`, `PlannedFillingRows[]?` | one immutable `ParityPlan` WorkPlan edition and its exact `ParityPlanRef` |
| **G.9‑2 `Run_Parity`**             | exact `ParityPlanRef` and comparison inputs; **G.5‑3 Select** only for a selector-facing result, using the plan's exact `TaskSignatureRef` and conditional matching `TaskMapRef` | parity/comparison result refs and, when selected, G.5 outcome refs; DRR and SCR pins with `PathId[]` and, when needed, `PathSliceId` |
| **G.9‑3 `Publish_ParityReport`**   | exact `ParityPlanRef`, parity-run trace refs, and active pins                                                                                   | `ParityReport` carrying the same exact plan ref and baseline binding (UTS publication record; emits canonical RSCR ids) |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, Default Governing Definition Index links, and P2W split).

1. **CC‑G9.1 — Exact comparison boundary, equal windows (and budgets), and pinned spec editions (local).**
   A `ParityPlanRef = <ParityPlanId, planEdition>` **SHALL** resolve one immutable plan edition. That ParityPlan **SHALL** choose exactly one subject branch: one `EntityOfConcernRef`, or `targetRefs[]` under their existing kinds and editions. It **SHALL** also name `GroundingHolonRef`, `ReferencePlane`, `ClaimScope`, `EvaluationWindow`, baseline set and binding, and evidence refs, and **SHALL** declare a single `FreshnessWindows` shared across baselines. `BaselineSet` supplies the target refs only when the plan explicitly identifies the same refs in both places; otherwise `BaselineBindingRef` relates the separate baseline to the named subject. If `Budgeting` is used and pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the editions required by the referenced specification, comparator, and any measurement or normalization method in use (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings, its exact `ParityPlan` WorkPlan **SHALL** carry the relevant declaration-local A.15.3 rows in `PlannedFillingRows[]` (nil-elision when not applicable). Each row resolves only inside that WorkPlan and has no independent reference, kind, or edition.

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific definition records beyond the pinned governing spec refs (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — CSLC-admissible orders and arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 `PortfolioMode` / selected-set semantics). Additionally: any numeric comparison or aggregation invoked by parity **SHALL** be CSLC-admissible and cite the corresponding CG‑Spec entry; non-admissible operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (citation only; arithmetic admissibility comes from `CG‑Spec`/`MM‑CHR`).

4. **CC‑G9.4 — Normalization discipline (local citation only).**
   If Characteristics differ by unit, scale, or space, the ParityPlan **SHALL** cite the CSLC-admissible comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible and auditable without unrecorded information.
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/PortfolioMode interpretation & telemetry separation (local).**
   `ParityPlan` and `ParityReport` **SHALL** either pin the applicable dominance regime and portfolio mode through explicit references and policy ids, or cite their corresponding defaults in `G.Core.DefaultGoverningDefinitionIndex`. Any non-default promotion behaviour must be bound to a policy and recorded through its policy-id pin.
   `IlluminationSummary`, coverage, and regret **SHALL** be treated as telemetry (report-only by default); any promotion into dominance is an explicitly pinned CAL policy and **MUST** be recorded in the audit pins and SCR.

   5a. **CC‑G9.5a — Adaptation parity disclosure (local; conditional).**
   When the parity claim concerns bounded specialization, the ParityPlan and ParityReport **SHALL** pin the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and any transfer, retention, downstream exploitation efficiency, downside field, or corridor-entry baseline/evidence note that materially affects comparison.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing visibility (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge and reference-plane crossing visibility plus R-channel penalty placement discipline.

8. **CC‑G9.8 — Report replay and evidence trace completeness (local).**
   A ParityReport **SHALL** carry the exact `ParityPlanRef` and `BaselineBindingRef` used for the run, echo `TaskSignatureRef` and any required `TaskMapRef` when the selector branch was used, and include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering inclusions, refusals, abstentions, and degradations. If the historical plan edition or binding cannot be resolved, return that unresolved input instead of substituting a current edition.

9. **CC‑G9.9 — Telemetry hooks are emitted with pins (local).**
   When parity emits telemetry for refresh, emitted telemetry **SHALL** carry the active edition pins and policy‑ids needed to re‑run parity (including the active subset of `ParityPinSet` relevant to the emitted event).
   In particular, telemetry items SHOULD cite `PathSliceId` when available, and **SHALL** include the policy id governing the telemetry interpretation.
   Mode‑specific definition pins **SHALL** be included as declared by the active `Extensions` blocks (e.g., `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`, including `EnvironmentValidityRegionId` when OEE parity is in scope).

10. **CC‑G9.10 — RSCR parity tests are published (local).**
    Parity publication **SHALL** include RSCR parity tests (via `F.15` harness refs) that cover negative/refusal paths relevant to this plan (missing pins, edition drift, missing bridge calibration refs, etc.).

11. **CC‑G9.11 — GateCrossing visibility (delegation point).**
    Delegated to `CC‑GCORE‑CROSS‑1` and the applicable GateCrossing/CrossingBundle harness checks (`E.18`, `A.21`, `F.9`, and relevant Part G bridge or crossing wiring). This remains a stable delegation point.

12. **CC‑G9.12 — Tech‑register lexical discipline (local).**
    Tech prose and heads **SHALL** follow E.10: do not introduce drift‑prone primitives (e.g., “metric” as a Tech primitive); reference the source pattern's canonical terms and pinned refs.

13. **CC‑G9.13 — MOO disclosure for parity (local).**
    `Run_Parity` / `Publish_ParityReport` **SHALL** record the ParityHarness identity (UTS ids) and the active pins required to interpret the outcome (editions + policy‑ids), so the reader can recover the harness and pins from the parity record itself.

14. **CC-G9-CLP-1 - Causal method rung parity.** If a parity report compares causal methods, it SHALL first run `CausalRungParityScreen`; when full parity remains plausible, it SHALL declare target causality-ladder rung, causal-use claim kind, `causalEstimandRef`, interventional-action basis, causal support-component refs, exact transport endpoints and transportability result when needed, estimate result when needed, bridge and loss where rungs differ, and `causalUseSupportResultRef` when relevant C.28 support is consumed, and degraded parity or abstain result where parity cannot be established.

### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross-sense or reference-plane reuse without its obtaining relation and visible pins.** Remedy: recover the exact F.17 cells and cite the obtaining F.9 relation when local meanings differ; cite the exact reference-plane crossing basis and visibility records when planes differ (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve CSLC-admissible outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by the governing policy pattern.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: name the exact `CharacteristicRef`, `ScaleRef`, `UnitRef` when applicable, `DHCMethodRef`, `MethodRef`, and `U.Measure` or result episteme; add `DistanceDefRef` only when used. “Metric” may appear only in Plain with a pointer to those canonical objects.
* **AP‑7 Hidden DHC replay drift.** Remedy: carry every active field of the C.21 replay basis and refuse parity reuse when a required field is unresolved or differs across the compared readings. Register refresh tests only for a named receiver that consumes those changes.

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a selected-set outcome plus the evidence trace. Family labels such as preference-learning comparators, causal decision pipelines, offline-RL evaluation pipelines, and robust BO-style selectors remain illustrative until a `G.2` SoTA pack or named current source pins the exact family being compared; the parity report still must preserve the selected set or partial order rather than collapse everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage; CMA-MAE `arXiv:2205.10752`; DQD `arXiv:2106.03894`; QDax `arXiv:2308.03665`; QDHF or QDAIF refs only when a feedback-guided QD claim is live).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET `arXiv:1901.01753` as lineage; AlphaEvolve `arXiv:2506.13131` when the live generator-family claim is coding-agent discovery; other current generator-family claims require a named `G.2` SoTA pack or exact current source).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes selected-set outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

**Show-D — Causal method rung parity.**
A team compares an observational predictor, an intervention optimizer, and a counterfactual policy strategy under one "best causal method" headline. `G.9` first runs `CausalRungParityScreen`: if rungs, support components, estimands, endpoints, or outcome windows differ, the screen returns degraded parity or abstain before a full record is fabricated. When full parity remains plausible, `G.9` requires `CausalMethodRungParityRecord`: each method declares `targetCausalUseClaimKind`, target `CausalityLadderRung`, `causalEstimandRef`, interventional-action basis, the support components actually consumed, relevant C.28 support result, follow-up window, outcome measure, changed transport endpoints, and estimate-result basis. If those fields differ, the parity report names `declaredCausalityLadderBridgeOrLossRef`, transportability or estimation refs where available, and degraded parity or abstain result. The admissible output may be a selected set by comparable rung, not one scalar winner.

### G.9:9 — Cited Records (what this pattern publishes)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan` and its exact `ParityPlanRef` (one `U.WorkPlan` episteme and immutable edition reference; any planned-filling rows remain declaration-local content)
* `ParityReport` (UTS publication record carrying the exact plan and baseline-binding refs; work-result or audit-facing publication record only when the neighboring source relation is live)
* DRR and SCR refs by id and, when applicable, `PortfolioPackRef?` and selector-output refs by id, for downstream consumption.
* Telemetry pins and events by id, for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

### G.9:10 — Relations

**C.27 temporal-claim relation.**

- C.27 may flag: dynamic parity when a benchmark actually compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome.
- This pattern keeps: baseline, freshness, comparator edition, effort/budget parity, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: faster improvement is not benchmark superiority, and `dyn2BenchmarkParityBlock?` is a benchmark input declaration, not a benchmark harness.
- Exit: when live, recover `dynOrderCompared`, baseline window, adaptation or intervention window, effort or budget parity reference, rate or rate-change measure, `G9ParityPlanRef`, and optional `G9ParityReportRef`; G.5 is relevant only if a selector-facing result declaration consumes such a benchmark result.

**C.29 mathematical-lens use relation.**

- C.29 may flag: parity or benchmark input whose comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, parity measure, model-family label, or model-selection basis depends on a mathematical lens that changes the parity claim and is missing, under-specified, or overread.
- This pattern keeps: baseline set, freshness, comparator edition, normalization ids, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- The `C.29` mathematical-lens account is a cited input to parity. `G.9` governs the benchmark report and conclusion, and `G.5` governs any selector-facing output declaration. Parity-measure admissibility comes from the cited `CG‑Spec`/`MM‑CHR`.
- C.29 application: for an under-lensed or overread parity input, cite the applicable `C.29` output for the stated use: `NoMathLensUseNeeded`, `MathLensUse.LensCandidateNote`, `MathLensUse.OneLine`, `MathLensUse.MiniCard`, `MathLensUse.FullCard`, or `NeighborGoverningPatternNote`. Use the cheap output that changes the next admissible parity use; full-card work is only required when the live parity or benchmark claim needs it.

**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.17`, `E.18`, `A.21`, `F.17`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping publication form; parity records are cited records).
**Uses:** **G.0**, **A.19**, `A.2.6` for exact `U.ClaimScope`, **F.9**, and `C.28` when parity compares causal methods or causal-use claims.
**Uses (optional, via Extensions):** **G.7**, **C.18 and C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

### G.9:11 — Working reading checks

- If two baselines are being compared under different freshness windows, comparator editions, or silent normalization rules, this pattern has not yet been satisfied.
- If parity cannot tell the reader what was held constant, what remained telemetry, and what crossings or penalties were active, the report is not yet usable.
- If a scalar winner is being claimed where only a selected set or partial order is CSLC-admissible, parity is overclaiming and should publish the CSLC-admissible outcome shape instead.

### G.9:End

## G.10 - SoTA Pack Shipping

> **Status:** Stable

**Tag:** Architectural pattern (conceptual; notation‑independent; pack‑boundary governing definition)
**Stage:** release‑time composition and publication; edition‑aware. For an independently applicable `E.18` flow crossing or `A.21` gate, carry its required CrossingBundle or gate anchors into the shipped pack.
**Builds on:** `G.Core` (Part‑G core invariants and delegation); upstream pack/kit governing definitions as cited publications or records (not redefined here).
**Governs (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing selection/parity roster, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not govern:** governing spec refs (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their governing definitions and are **cited**).

### G.10:1 - Problem frame — Shipping without smuggling semantics

Part G produces many **kit-governed** and **suite-governed** publications or records (harvest packs, CHR/CAL packs, evidence graphs, bridge calibration records, log bundles, parity reports). Without an explicit **pack-boundary governing definition**, “shipping” tends to become:

* an ad‑hoc folder/export ritual (tool‑locked, not citable), or
* a silent re-specification step (shipping accidentally redefines legality, defaults, or selection semantics), or
* a brittle hand‑off that cannot support RSCR/refresh (no actionable pins/editions/policies attached).

`G.10` fixes the pack boundary: it defines the **single, normative shipping surface** for Part‑G outputs — **`SoTA‑Pack(Core)`** — and a minimal choreography for making shipped artefacts **selector‑ready** and **audit‑citable**, while delegating all Part‑G‑wide invariants to `G.Core` (citation/delegation, not restatement).

### G.10:2 - Problem — Why naive shipping breaks reuse, legality, and refresh

Naive shipping fails (conceptually) when any of the following occurs:

1. **Format-as-governing-spec.** A concrete export format is treated as “the pack,” turning a tool choice into a governing pack definition.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Pack smuggles semantics.** Shipping reintroduces “convenience” rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the governing spec ref.
4. **Invisible crossings.** Cross-context or cross-plane reuse is present, but the pack does not expose the crossing bundles and penalty policy pins needed for audit and refresh planning.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which methods, mechanisms, and policies were used, at which editions, to obtain them*.
6. **Refresh orphaning.** Telemetry and decay signals exist, but the shipped artefact provides no stable scope keys (`PathId` / `PathSliceId`) and no payload pins for RSCR triggers.

### G.10:3 - Forces

| Force                                              | Tension                                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Notation independence**                          | Make packs portable across tools ↔ still make them concrete enough to be used.                   |
| **Completeness vs minimality**                     | Ship enough to be selector‑ready ↔ avoid duplicating governing definition semantics.                            |
| **Continuity vs evolvability**                     | Preserve public IDs across edition bumps ↔ allow legitimate upgrades and deprecations.           |
| **Cross‑context reuse vs honesty**                 | Enable reuse across Traditions/contexts ↔ keep crossings explicit and auditable.                 |
| **Telemetry usefulness vs semantic contamination** | Export useful signals ↔ avoid turning telemetry into dominance/acceptance without pinned policy. |
| **Fast shipping vs refreshability**                | Ship quickly ↔ ensure RSCR triggers can be planned and scoped (P2W‑path aware).                  |

### G.10:4 - Solution — `SoTA‑Pack(Core)` as the shipping object and publication kit

`G.10` defines a **pack-governed** shipping surface: a notation‑independent object that **cites** all upstream artefacts by stable ids/refs and exposes the minimum pins required to (a) consume the result via selection, (b) audit it via path citations and crossing bundles, and (c) refresh it via typed RSCR triggers.

#### G.10:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core` (Part‑G core invariants; Default Governing Definition Index citation)

**GCoreLinkageManifest (G.10)** *(normative; expands per `G.Core:4.2`; `Nil‑elision` applies)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := { `GCoreTriggerSetId.RefreshOrchestration` }
  *(payload pins: `PackId(UTS)`, `publicationScopeId`, `CNSpecRef.edition`, `CGSpecRef.edition`, `PlanItemRefs := ⟨WorkPlanRef, planLocalContentLocator⟩[]`, `AuditPins`, `UTSRowId[]`, `PathId/PathSliceId`, crossing policy pins, `TelemetryPinIds`, relevant upstream artefact ids)*

* `DefaultsConsumed` := {
  `DefaultId.PortfolioMode`,
  `DefaultId.DominanceRegime`,
  `DefaultId.GammaFoldForR_eff`
  }
  *(Governing definitions are resolved through `G.Core.DefaultGoverningDefinitionIndex` and are not restated here.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; id‑valued unless noted)* := {
  `PackId(UTS)`,
  `publicationScopeId`,
  `contextSliceId?`,

  `PlanItemRefs := ⟨WorkPlanRef, planLocalContentLocator⟩[]?` *(WorkPlanning planned baseline refs)*,
  `AuditPins` *(pack‑level pin bundle: edition pins (only on `…Ref.edition`), policy‑ids, UTS/Path pins; ids only)*,

  `UTSRowId[]`,
  `PathId[]?`, `PathSliceId[]?`,
  `CrossingBundleIds := CrossingBundleId[]?`,
  `TelemetryPinIds := TelemetryPinId[]?`,
  `PortfolioRosterId?`,

  `MOOManifestId?` *(method‑of‑obtaining‑output disclosure; conceptual object id)*
  }
  *(Optional pins from `CrossingVisibilityPins` MAY be strengthened to unconditional by listing them above; `G.10` typically strengthens `UTSRowId[]` and path/crossing bundles when the pack is publicly shipped.)*

* `TriggerAliasMapRef` := `∅` *(canonical trigger ids are used directly)*

> **Mode‑specific definition pins.** Any additional pins required for QD/OEE/interop shipping are introduced only by `GPatternExtension` blocks in `G.10:4.6` (never smuggled into the core linkage).

#### G.10:4.2 - `SoTA‑Pack(Core)` object model (normative; notation‑independent)

`SoTA‑Pack(Core)` is a **shipment object** (a *pack*, not a kit and not a suite) that **cites** upstream artefacts and exposes pack‑level pins required for downstream use.

```
SoTA‑Pack(Core) :=
⟨
  PackId(UTS),
  publicationScopeId,
  contextSliceId?,
  CG-FrameContext,
  entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,

  // Governing spec refs (refs + edition pins; semantics governed by their patterns)
  CNSpecRef := ⟨A.19 ref, CNSpecRef.edition⟩,
  CGSpecRef := ⟨G.0 ref,  CGSpecRef.edition⟩,

  // Selector-facing selection/parity roster token (conceptual; no formats mandated)
  PortfolioRosterId?,        // produced by `G.10‑1` as part of composition; may cite ε and the applicable pinned regime/mode refs

  // Cited payload packs/kits (ids only; semantics governed by the cited governing patterns)
  SoTAHarvestPackId?          // e.g., G.2 output id
  CHRPackId?                  // G.3 output id
  CALPackId?                  // G.4 output id
  EvidenceGraphId?            // G.6 output id
  BridgeMatrixId?             // G.2/G.7 cited id
  BridgeCalibrationTableId?   // G.7 output id
  SoSLOGBundleId?             // G.8 output id
  ParityReportId?             // G.9 output id
  DashboardSliceId?           // G.12 output id (optional)
  InteropSurfaceId?           // G.13 output id (optional)

  // Path citation surface (ids only; semantics governed by A.10/G.6)
  PathIds := PathId[]?,
  PathSliceIds := PathSliceId[]?,

  // Planned baseline + audit pins (P2W-aware; ids only)
  PlanItemRefs := ⟨WorkPlanRef, planLocalContentLocator⟩[]?,
  AuditPins := { id pins… },                 // editions only on `…Ref.edition`; includes policies, UTS/Path pins, crossing pins

  // Crossing visibility surface (per GateCrossing; ids only)
  CrossingBundleIds := CrossingBundleId[]?,

  // Telemetry hooks for refresh planning (ids only; PathSlice-keyed; policy-id pinned)
  TelemetryPinIds := TelemetryPinId[]?,

  // Method-of-obtaining-output (MOO) disclosure (conceptual; ids only)
  MOOManifestId?,

  Notes?
⟩
```

`PlanItemRefs`, when present, resolve the exact U.WorkPlan episteme and locate the baseline content inside it. For A.15.3 content, the locator uses that WorkPlan's `planItemDesignator` and any needed `rowDesignator`; it gives the item or row no independent identity or edition. An ordinary A.15.2 baseline stays ordinary plan content when it reuses no declaration member. A changed plan must not silently replace the earlier reference carried by the shipped pack.

##### G.10:4.2.1 - Portfolio roster (normative; pack-governed; governing-definition delegating)

`PortfolioRosterId` identifies the **selector‑facing** pack roster token. The corresponding `PortfolioRoster@Context` is one citation-and-binding roster record inside the shipped publication form, not a publication face kind, publication form kind, interop publication form kind, or carrier kind:
it MUST NOT redefine selection / selected-set semantics (governed by `G.5`) or parity semantics (governed by `G.9`).
Mode‑specific definition pins (QD/OEE/interop) are introduced only via `G.10:Ext.*` blocks.

```
PortfolioRoster@Context :=
⟨
  PortfolioRosterId,
  PackId(UTS),
  CG-FrameContext,
  entityOfConcern,

  // Selector operation and default-resolution support
  portfolioMode?,
  dominanceRegime?,
  ε?,

  // Published selector outcome and set-result declaration (metadata fields, not local semantics)
  selectorOutcomeKind?,
  setResultFamily?,
  handoffKind?,
  subjectKind?,
  sourceSetFamily?,
  derivedViewKind?,
  sourceSetComposition?,
  basePaletteRef?,
  lensId?,
  shortlistId?,
  promotionPolicyRef?,
  retentionIntent?,

  // Selector-facing roster + provenance hooks (ids only)
  MethodFamilyRowRefs := MethodFamilyRowRef[]?,
  GeneratorFamilyRowRefs := GeneratorFamilyRowRef[]?,
  ParityReportId?,
  SCRId[]?, DRRId[]?,

  // Pin reuse: prefer referencing the enclosing pack’s AuditPins bundle
  AuditPins?,
  Notes?
⟩
```

The roster cites exact G.5 `MethodFamilyRowRef = <MethodFamilyId, rowEdition>` and `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>` values. A lineage id alone cannot replay the selected membership or grouping basis; each row ref resolves its immutable source edition. Shipping these references neither admits the members nor creates their grouping. Preserve the row's G.5 local or public registry-identity contract. A visible project-local row is not automatically a public registry entry; intentional public registration adds S1/S1′ naming and UTS duties. G.10's independently applicable pack-shipping requirements and E.24.PUB availability conditions still apply.

*Presence rule:* `PortfolioRosterId` MAY be omitted only when the shipped pack is *inputs‑only*
(e.g., shipping CHR/CAL/evidence without any selector‑consumable selected-set/shortlist output).

The `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `sourceSetFamily`, `sourceSetComposition`, `derivedViewKind`, `basePaletteRef`, `lensId`, and `shortlistId` fields in this roster are payload metadata fields or refs inside the shipped publication form. They do not define publication face kinds, publication form kinds, interop publication form kinds, or carrier kinds, and they do not let `G.10` re-govern `G.5`, `C.18`, `C.19`, or `G.2` semantics.

**Interpretation constraints (normative by delegation).** Any universal invariants governing (i) CN/CG spec-ref governing-definition assignment, (ii) crossing visibility and penalty routing, (iii) tri‑state guards, (iv) set‑return semantics, (v) P2W split, (vi) defaults, and (vii) RSCR trigger typing are **not restated here** and are enforced via `G.Core` conformance (see `CC‑G10‑CoreRef`).

#### G.10:4.3 - Shipping choreography (normative; governing-definition delegating)

`G.10` prescribes a minimal, governing-definition delegating sequence for composing a shipped pack:

1. **S‑1 — Gather & pin.** Collect upstream artefact ids and verify the **required pins** implied by the linkage manifest (edition pins, policy pins, UTS/Path pins).
2. **S‑2 — Compose `SoTA‑Pack(Core)` + MOO disclosure.** Assemble the pack object and attach a **`MOOManifest`** that lists the referenced methods, mechanisms, and policies used, at their exact editions, to obtain the shipped outcomes (ids only; semantics stay with governing definitions).
3. **S‑3 — Publish selection/parity roster (selector‑facing).** Except when the inputs-only presence-rule exception in §4.2.1 is used, produce a selector‑readable `PortfolioRosterId` with the parity/definition pins required for reproducibility; do not mandate formats.
4. **S‑4 — Anchor and publish path citations.** Ensure A.10 anchors exist and publish/record `PathId/PathSliceId` citations required for downstream explainability (e.g., the `C.23` W2 `AdmissibilityLedger`) and maturity rung changes.
5. **S‑5 — Expose CrossingBundle.** For each GateCrossing relevant to the shipped artefacts, expose the required `CrossingBundle` references (fail fast on missing or non‑conformant bundles when required).
6. **S‑6 — Emit telemetry pins for refresh planning.** Whenever illumination increases or archive/OEE pin state changes, emit PathSlice‑keyed telemetry with policy‑id and the active `…Ref.edition` pins (and QD `EmitterPolicyRef`/`InsertionPolicyRef` when applicable).
7. **S‑7 — Publish to UTS (twin labels).** Mint/refresh UTS Name Cards needed to cite the pack and shipped heads (Tech/Plain twins when required); a claimed cross-context semantic correspondence cites its F.9 relation, separate bounded-use claim and reliance. G.7 calibration and loss notes remain evidence for that use, not identity or permission.
8. **S‑8 — Optional: ingest interop surface.** If `G.13` interop is in use, ingest/cite `InteropSurface@Context` as annotation-only notes, pinning external index editions; do not redefine interop semantics.

#### G.10:4.4 - Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | `G.*` outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas     | `SoTA‑Pack(Core)` (UTS row + surfaces) + `AuditPins` (+ `MOOManifestId?`) (+ `PortfolioRosterId?`) |
| **G.10‑2** | `Publish_UTS`              | `PackId(UTS)`, `UTSRowId[]`, deprecation/edition‑bump notes       | UTS rows/Name Cards for the pack and shipped heads (incl. twins when required) |
| **G.10‑3** | `Expose_CrossingHooks`     | GateCrossings, lanes/planes/contexts                              | **CrossingBundle** (**E.18:CrossingBundle**) per GateCrossing; **fail** on missing/non‑conformant bundles |
| **G.10‑4** | `Pack_MOO`                 | referenced method/mechanism/policy/edition ids                           | `MOOManifestId` (ids only; governing-definition delegating) |
| **G.10‑5** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition` (+ QD/OEE pins when applicable) |
| **G.10‑6** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for the `C.23` W2 `AdmissibilityLedger` & rung changes |
| **G.10‑7** | `Ingest_InteropSurface?`   | (optional) `G.13 InteropSurface@Context`                          | Annotated pack notes citing external‑index editions     |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

> **Note.** Any concrete serialisation/export is *not* part of this interface set. Serialisation belongs to interop/annex governing-definition assignment and must not become the governing definition.

#### G.10:4.5 - Consequence of governing-definition assignment (normative boundary statement)

`G.10` is the **one governing definition** of “shipping” in Part G *(by delegation to `CC‑GCORE‑SKP‑1`)*.
Other `G.x` patterns may produce artefacts that are shipped, but they must not embed shipping obligations; they cite `G.10` shipping surfaces instead.

#### G.10:4.6 - Extensions (pattern‑scoped; non‑core)

All method‑/generator‑/interop‑specific shipping extension declarations live here as `GPatternExtension` blocks.



##### G.10:4.6.1 - GPatternExtension — `G.10:Ext.QDArchiveShippingPins`


**PatternScopeId:** `G.10:Ext.QDArchiveShippingPins`
**GPatternExtensionId:** `QDArchiveShippingPins`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, C.21, G.5, G.8, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* active fields from C.21's DHC replay basis *(only when shipped archive telemetry consumes a C.21 DHC coordinate; carry exactly the fields used rather than a generic method-spec or metric-edition pin)*
* `EmitterPolicyRef` *(policy‑id / ref)*
* `InsertionPolicyRef` *(policy‑id / ref)*
* `CharacteristicSpaceRef` *(id/ref; iff archive partitioning is declared)*
* `CharacteristicSpaceRef.edition?` *(iff partitioning depends on an editioned space definition)*
* `PathSliceId[]` *(to bind telemetry/refresh scope when archive behaviour is present)*
**RSCRTriggerSetIds:** `∅` *(covered by `G.10` core linkage via `GCoreTriggerSetId.RefreshOrchestration`)*
**Notes (shipping-pin discipline):**
* This block never redefines archive semantics; it only states which pins must be present in the shipped pack when QD archive fields are present.



##### G.10:4.6.2 - GPatternExtension — `G.10:Ext.OEEShippingPins`


**PatternScopeId:** `G.10:Ext.OEEShippingPins`
**GPatternExtensionId:** `OEEShippingPins`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `G.5`
**Uses:** `{G.5, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition`
* `EnvironmentValidityRegion?` *(id/ref; iff an explicit region is declared as part of generator-family support)*
* `PathSliceId[]` *(scope key for refreshable generator telemetry when present)*

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* “Open‑endedness” semantics remain defined by the governing pattern; the pack only carries the pins required to make the shipped claim replayable/auditable.



##### G.10:4.6.3 - GPatternExtension — `G.10:Ext.InteropCitation`


**PatternScopeId:** `G.10:Ext.InteropCitation`
**GPatternExtensionId:** `InteropCitation`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.13`
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `InteropSurfaceId`
* `ExternalIndexRef.edition`
* `ClaimMapperRef.edition`
* `PlaneMapRef.edition?`
* `MappingPolicyRef`

**RSCRTriggerSetIds:** `∅` *(covered by the core trigger set)*
**Notes (shipping-pin discipline):**
* This block only records that an interop surface contributed to the shipped pack’s provenance; it does not redefine any crosswalk semantics.

#### G.10:4.7 - Published surfaces must ship kind, source, derivation, lens, and shortlist token

- Published surfaces should carry the subject kind, source set kind, and relevant declared surface pins. When a selector outcome is shipped, they should also carry its outcome kind and, when applicable, the set-result kind or handoff kind.
- These are publication payload metadata fields inside `SoTA-Pack(Core)`, not publication face kinds, publication form kinds, interop publication form kinds, or carrier kinds.
- Good publication fields include `selectorOutcomeKind`, `setResultFamily`, `handoffKind`, `subjectKind`, `sourceSetFamily`, `sourceSetComposition`, `dominanceRegime`, `lensId`, `shortlistId`, and any declared archive or promotion-policy ids that the reader needs to interpret the visible set.
- Those payload fields should use controlled tokens, cited ids, or already-declared head labels rather than shipping-local prose values.
- When the visible surface or the shortlisted source is one derived tradition view, also publish the derivation explicitly.
- Useful additional fields there include `derivedViewKind`, `basePaletteRef`, and the declared `qId` or reachability rule id that disciplined that derivation.
- `portfolioMode` may remain as one support field about selector operation, but it should not stand in for the public set label.
- A published surface should mirror semantics that are already declared in the governing palette, front, archive, or shortlist language.
- It should not redefine that semantics locally.
- When one shipped surface still needs a plain-language label, use the declared set-result kind and source set rather than falling back to `portfolioMode`.

##### G.10:4.7.1 - Worked publication slice

- If the visible surface is one tradition front under the declared `Q`, publish `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, and keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable instead of pretending that the palette itself already was that front. Publish `selectorOutcomeKind` only when a G.5 selector outcome is also shipped, and `setResultFamily` only for its `SetResultOutcome` branch.
- If one shortlist is emitted from that derived tradition front, publish `selectorOutcomeKind=SetResultOutcome`, `setResultFamily=Shortlist`, `sourceSetFamily=Front`, `derivedViewKind=TraditionFront`, `basePaletteRef=SoTAPaletteDescriptionId`, and the named `lensId` together.
- If that same shortlisted surface is emitted as one stable public object, also publish `shortlistId=<...>` and keep it recoverable that the token names that shortlist rather than replacing it.
- If one retained tradition archive view is shown, publish `sourceSetFamily=Archive`, `derivedViewKind=TraditionArchive`, and keep the same `basePaletteRef` recoverable. A G.5 selector outcome, when also shipped, carries its admitted outcome kind and, only for a `SetResultOutcome`, its set-result kind.
- If the shortlist is later ordered, publish `setResultFamily=RankedShortlist` and keep the declared source set visible.
- Use `ChoiceSet` only as a mathematical gloss when the shipped object is explicitly one mathematical analysis artifact rather than the public selected set; it is not a `setResultFamily` value.
- Do not publish `sourceSetFamily=TraditionPalette` alone when the visible object is already one derived tradition view; readers need to know which view is on the surface and which base palette it depends on.
- Do not publish `TraditionFront` or `TraditionArchive` as if they were the default meaning of `Tradition`.
- Do not ask `portfolioMode` to tell the reader whether they are seeing one palette, one front, one archive, or one shortlist.

### G.10:5 - Consequences

**Benefits**

* A shipped result becomes **selector‑ready** and **audit‑citable** without turning file formats into governing specifications.
* Shipping is no longer a semantic “backdoor”: pack‑level semantics remain governing-definition delegated.
* RSCR/refresh becomes operationally viable because pack‑level scope keys and payload pins are present.

**Costs / trade‑offs**

* Shipping becomes more explicit (more pins and explicit surfaces), which raises authoring overhead.
* If upstream governing definitions fail to provide citable ids/pins, `G.10` cannot paper over the gap; shipping will block or ship a visibly incomplete pack (depending on policy‑bound failure behaviour, governed by cited definitions).

### G.10:6 - Bias‑Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Format bias (Arch/Prag).** A popular export format is tempting to treat as “the pack”.
  *Mitigation:* keep Core surfaces conceptual (E.5.2); move serialisation recipes to Annex/Interop; keep conformance on semantics.
* **Centralisation bias (Gov).** A single pattern governing shipping semantics can become a bottleneck.
  *Mitigation:* keep shipping as one explicit governing-pattern responsibility, but push mode/method specifics into explicit `G.10:Ext.*` extension blocks and cite governing patterns.
* **Telemetry→dominance bias (Onto/Prag).** Shipping pipelines often “promote” telemetry proxies (illumination/coverage) into ranking.
  *Mitigation:* preserve the telemetry/order separation and require explicit CAL policy‑id for any promotion; record the policy‑id in audit pins/telemetry.
* **Interop authority bias (Onto/Epist).** External indexes can silently override local legality/typing.
  *Mitigation:* `G.10‑7` ingests interop only as cited notes (editions + mapping policy refs), never as a replacement governing spec ref.

### G.10:7 - Archetypal grounding (informative; post‑2015 method families)

**World‑plane (benchmark shipping).**
A team working within a CG‑Frame ships a selected set that includes a QD archive (e.g., MAP‑Elites‑class / CMA‑ME‑class families) and a generator family (e.g., POET‑class environment generation). The shipped `SoTA‑Pack(Core)` cites the CHR/CAL packs and records the QD/OEE extension-required pins through the extension blocks so that downstream parity and refresh can be scoped to the affected `PathSliceId`s rather than forcing a global rebuild.

**Episteme‑plane (synthesis shipping).**
A team working within a CG‑Frame ships a pluralistic set of admissible methods gathered from post‑2015 literature streams (living review + synthesis pack). The shipped pack carries explicit CN/CG spec refs, evidence path citations, and method‑of‑obtaining‑output disclosure; downstream selection uses set‑valued outcomes, and refresh can be scheduled when the synthesis pack or key pins change.

### G.10:8 - Conformance checklist (CC‑G10)

This pattern inherits order/illumination, evidence, and bridge/penalty legality from the cited governing patterns (not restated here). Shipping‑specific requirements:

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD/OEE fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and (OEE) `TransferRulesRef.edition`; when a shipped field actually consumes a C.21 DHC coordinate, carry every active field of that coordinate's `DHCReplayBasis` instead of a generic method-spec or metric-edition pin. Include `CharacteristicSpaceRef` (+ `CharacteristicSpaceRef.edition` when it affects partitioning reproducibility); for QD archive semantics also pin `EmitterPolicyRef` and `InsertionPolicyRef`. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active editions of the pinned `…Ref` fields (incl. OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels optional only). |
| **CC‑G10.4 (UTS publication & twins).** | Shipped heads use UTS Tech/Plain twins under the delegated publication rule. A shipped cross-context semantic-use claim cites its obtaining relation, separate bounded-use proposition and matching reliance; calibration summaries keep their evidence role. Kind and plane claims retain their own governors. | Verify the published names and exact relation/use evidence; a visible CL or policy pin alone is insufficient. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For every declared selector set-result or archive published, the pack SHALL list the applicable generation/parity method and mechanism ids (e.g., QD `EmitterPolicyRef`/`InsertionPolicyRef`, parity harness ids, method refs where the method definition is generative) and the active policy‑id(s) in SCR‑visible bindings and telemetry pins (ids only; governing-definition delegating). | Verify `MOOManifestId` is present when outcomes are intended for downstream use and does not redefine semantics. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack cites all included upstream artefacts by id/ref and exposes the required pins (`AuditPins`, UTS/Path pins, CrossingBundleIds when required). | Verify all present payload artefacts have ids and the pins needed to cite/replay them. |
| **CC‑G10.7 (CrossingBundle exposure).** | For each GateCrossing relevant to shipped artefacts, the pack exposes the relevant `CrossingBundleIds` (or records that no such crossings exist) **per delegated crossing visibility discipline**, and shipping fails fast on missing/non‑conformant crossing bundles when required. | Verify crossing bundle presence/absence is honest and aligned with the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := ⟨WorkPlanRef, planLocalContentLocator⟩[]` are present (exact WorkPlan plus plan-local content; no execution logs). | Verify the baseline resolves inside the cited WorkPlan; item and row designators have no independent identity, and decision records or execution logs do not replace the plan. |
| **CC‑G10.9 (Extension‑scoped pin declaration).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | Verify conditional extension pins are not silently omitted when the mode is used. |
| **CC‑G10.10 (Derived tradition-view shipping).** | If the visible shipped surface or shortlisted source is one derived tradition view such as `TraditionFront` or `TraditionArchive`, the pack **MUST** publish the declared `sourceSetFamily`, keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable, and carry the derivation basis (`derivedViewKind`, declared `Q`, or reachability/coverage rule id) with enough explicitness that the visible surface cannot be mistaken for the default palette semantics. | Verify derived tradition views are shipped as derived views, not as silent redefinitions of the base palette. |

### G.10:8.1 - Anti‑patterns and remedies

* **AP‑1 Format‑as‑governing‑specification.** Remedy: keep Core surfaces conceptual (E.5.2); move serialisation to Annex/Interop; enforce `CC‑G10.1`.
* **AP‑2 Hidden edition drift.** Remedy: require `…Ref.edition` pins in AuditPins and treat edition changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑3 “QD archive present” but missing definition pins.** Remedy: enforce `CC‑G10.2` and the `G.10:Ext.QDArchiveShippingPins` pin declarations.
* **AP‑4 Telemetry silently becomes dominance.** Remedy: keep telemetry report‑only unless an explicit CAL policy promotes it; require policy‑id recorded (ties to `CC‑G10.3` and MOO discipline).
* **AP‑5 No PathSlice key → refresh becomes global.** Remedy: enforce PathSlice‑keyed telemetry and path citations (`G.10‑5`, `G.10‑6`).
* **AP‑6 Cross-context reuse without its required grounds or anchors.** Remedy: cite the actual relation and the receiving-use and reliance grounds required by its governor; include calibration and policy pins when that account requires them. For an independently applicable `E.18` flow crossing or `A.21` gate, expose its required bundle or gate anchors and fail on missing or non-conformant ones (`CC‑G10.7`, `CC‑GCORE‑CROSS‑1`).
* **AP‑7 Interop ingestion rewrites semantics.** Remedy: ingest interop as cited notes only; semantics remain in `G.13` (`G.10‑7`, `G.10:Ext.InteropCitation`).
* **AP‑8 Derived-view collapse.** Remedy: ship `sourceSetFamily`, `derivedViewKind`, `basePaletteRef`, and the declared `Q` or reachability basis with enough explicitness that one derived tradition view cannot masquerade as the default palette meaning.

### G.10:8.2 - SoTA‑Echoing (post‑2015, for orientation)

* **Research‑object packaging & provenance.** Post‑2015 practice increasingly treats “release artefacts” as *packages with explicit provenance, versions, and minimal replay pins* (e.g., modern research‑object and RO‑Crate‑class approaches). `G.10` mirrors the “package‑as‑citation‑surface” idea while keeping semantics governing-definition delegated.
* **Reproducibility regimes in ML/AI.** Contemporary reproducibility checklists, artifact evaluation/badging, and benchmark reporting norms motivate: explicit version pins, explicit method disclosure, and separating telemetry summaries from decision criteria unless policy‑promoted.
* **Scholarly KG interoperability.** ORKG/OpenAlex‑class ecosystems highlight the need to treat external mappings as *interop notes with editions*, not as replacement governing spec refs — matching the `G.10‑7` and `G.10:Ext.InteropCitation` stance.

### G.10:9 - Relations

**Builds on:** `G.Core`; consumes/cites artefacts governed by cited patterns from `G.2` (harvest pack), `G.3` (CHR pack), `G.4` (CAL pack), `G.6` (EvidenceGraph), `G.7` (bridge calibration), `G.8` (SoS‑LOG bundle), `G.9` (parity report), optional `G.12` (dashboard slice), optional `G.13` (interop surface).
**Publishes to / used by:** UTS (pack identity), selector‑facing consumers (via `G.5`), audit and assurance publications (SCR/RSCR), refresh orchestration (`G.11`).
**Constrains:** tooling exports are downstream; serialisation and repository integration are explicitly non‑normative here.

### G.10:End

---

## G.11 - Decide Whether and How to Refresh SoTA Packs and Related Results (Telemetry and Decay)

**Tag.** Architectural pattern (architectural; notation-independent)
> **Status:** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time and maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs, when their use calls for them.** `RefreshQueue`, `RefreshPlan@Context` (a local application name for one exact `U.WorkPlan`, not a new kind), `RefreshReport@Context` (record of refresh Work or its audit), `DeprecationNotice@Context`, and `EditionBumpLog@Context`. Continued reliance on an already applicable result requires none of these solely to prove that refresh was omitted.

**Primary hooks.** `G.Core` (RSCR trigger catalogue, alias docking, and Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge Sentinels; CL, Φ, and plane policy pins), `G.5` (set-returning selection and dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness and decay), `E.18` (GateCrossing and CrossingBundle visibility), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support results whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note.**
`G.11` cites `G.Core` for RSCR trigger-kind meaning, CN and CG admissibility, tri-state guards, penalties, set-return semantics, shipping or harvesting delegation, `RSCRTriggerKindId` values, and default governing definitions.
Refresh plans and reports cite those governed definitions; they do not create local trigger meanings or default definitions inside the refresh record.

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, parity result, or a use that relies on an `A.6.RCD` predicate definition or derived relation kind may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, source currentness, a relied-on base relation definition, the named substrate edition, or derivation applicability changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner first decides what the available support permits for the receiving use. When a changed premise requires upkeep, the refresh kit names the affected object and scope, the source and policy basis, and the justified action. Planning and reporting remain separate, and refresh can stay local while preserving comparability and subject-specific result meanings.

When a later or replacement source may change a claim and the actual receiving uses must first be found and revalidated, use `A.10.1` for the bounded search frame, discovery coverage and gaps, exact-use test, action-changing reach, application of the direct subject guidance, and the independently obtained subject result. `G.11` continues to govern source currentness, decay, refresh planning, and refresh reporting. A practitioner or admitted System may use a separately established currentness result or independently obtained subject result to plan later refresh without changing either result or the governing patterns.

#### G.11:0.3 - First output

For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not decide whether the artifact improved.

First establish whether the current conditions and available basis already support the receiving use. If they do, retain that result without a new currentness line, WorkPlan, waiver or skip-refresh certificate. When a later recipient needs a changed limit or retained reason, keep the minimum useful content with the existing result or publication; a `RefreshCurrentnessLine@Context` can express it when a structured line is useful. Produce a `RefreshPlan@Context` only for selected planned refresh. For an underlying claim about a selected set, archive, culture, bridge, evidence, dashboard or shipping, obtain that subject pattern's result; currentness does not establish its adequacy.

When currentness is the live question, use G.11 to record framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions. In that record, cite `E.4` for the affected framework, `E.4.PFR` for a framework relation, `E.4.PFAD` for the framework architecture decision, the exact source contribution and bounded use, including the `G.2` pack when that route was used, and `E.11` for discovery. For publication, cite `E.17` for a source-backed face and return to source and `E.24.PUB` for the occurrence, form, carrier, audience, bounded use, and availability. Do not create private refresh vocabulary for these neighboring meanings.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **currentness conditions** (a relied-on premise changes, a justified review becomes due, or an actual qualification or use window ends),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

The kit addresses two recurring refresh failures:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only refresh result that leaves currentness drift unresolved.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: its users turn typed refresh causes into **scoped plans** and record execution in **auditable execution reports**. Cause semantics and universal invariants remain delegated to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and admissibility

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Local trigger aliases are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS, Path, or policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance, `PortfolioMode`, or Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Actual refresh Work must remain inspectable through the needed pins, references and paths. A currentness decision or an unchanged use must not become a fictitious Work occurrence.
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration kit

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

```text
GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.TriStateGuard,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },

  RSCRTriggerSetIds := {GCoreTriggerSetId.RefreshOrchestration},

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    RSCRTriggerKindId,
    RSCRTriggerAliasId?,
    scope: PathSliceId[] | PatternScopeId,
    payloadPins{…},

    RefreshPlanId?,
    RefreshReportId?,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    WorkPlanRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩
```

By the `G.Core` **Expansion rule**, the **effective** conformance ids, trigger kinds, and pin obligations for `G.11` are the manifest expansions (profiles, sets, and pin sets) plus the explicit deltas above.

**TriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (subject-qualified; conceptual artefacts)

`G.11` defines a kit of authoring-plane artefacts for actual refresh planning and reporting. `RefreshPlanId` is required on a plan and `RefreshReportId` on a report. The linkage manifest applies to the triggers and actions that occur; retaining applicable support creates no trigger, plan or report merely to fill their pins.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (one exact `U.WorkPlan`).**
   A planned refresh is one `U.WorkPlan` episteme under A.15.2. It **does not execute Work** and **does not embed gate decisions**. `RefreshPlan@Context` is only this pattern's application name for the plan; it declares:

   * `RefreshPlanId` (UTS-published id; editioned)
   * `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
   * `TargetScope := PathSliceId[] | PatternScopeId[]`
   * `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
   * `PlannedActions := RefreshAction[]` (each action delegates to a subject pattern)
   * `RequiredPins`: exact affected source and result editions, policy pins and scope for replayability; UTS pins for public identities actually used; graph Path pins when the selected scope is graph-expressed or an independently applicable receiving contract requires them.
   * `PlannedFillingRows[]?` as ClaimGraph content kept inside the WorkPlan under A.15.3 when a value must be pinned against a declaration member defined by its own pattern. A row is addressed only through the WorkPlan and has no separate reference or identity.
3. **`RefreshReport@Context` (record of refresh Work or its audit).**
   An execution or audit report that records:

   * `RefreshReportId` (UTS-published id; editioned)
   * `ExecutedActions[]` with links to cited artefacts governed by cited patterns (e.g., new parity report id, new pack id)
   * `ObservedDeltas` (telemetry deltas, admissibility changes, evidence-relation or source-relation changes) as refs and pins, not as untyped prose
   * `RSCRRefs[]` (any RSCR or regression harness artefacts invoked)
   * `EmittedNotices[] := DeprecationNoticeId[]` and `EditionBumpLogId[]`
   * the canonical trigger kinds actually applied (not only aliases)
4. **`DeprecationNotice@Context` and `EditionBumpLog@Context`.**
   Controlled evolution artefacts that preserve ID-continuity:

   * **DeprecationNotice** explains scope, reason class (canonical trigger kind ids), and successor refs.
   * **EditionBumpLog** records edition increments and the pins that justify them.

   > *Note (normative by delegation).* ID continuity and alias discipline are governed by `G.Core` (do not restate as local rules here).

#### G.11:4.2a - Selected-set, archive, and cultural-variant currentness

Use this line when refresh currentness concerns a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, path slice, reused `A.6.RCD` predicate definition, or admitted derived relation kind.

```text
RefreshCurrentnessLine@Context:
  governedObjectRef:
  currentnessObjectKind:
  sourceRecordRef:
  editionOrLineagePins:
  affectedPathSliceOrScope:
  subjectPatternLocator:
  receivingUseAndApplicableConditions:
  currentnessConclusion:
  plannedRefreshAction?:
  refreshReportRef?:
```

`currentnessObjectKind` may name, for example, a selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, a cultural lineage, a term bridge, or a reused predicate definition. Use the line only when its recipient needs this structured currentness result; identify the temporal reference and relevant window within its conditions and pins. `plannedRefreshAction?` is absent when no refresh is selected, and `refreshReportRef?` is absent when no such report exists. The line states applicability for a use, not that the subject claim is true or adequately supported. Use `G.5` for selected-set declaration, `E.17` and `E.24.PUB` for publication, `C.18` for archive and front relations, `C.19` for pool treatment, `C.36` for cultural-evolution claims, `F.17` for exact local `SchemeSenseCell`s, `F.18` for name settlement, `F.9` for obtaining Bridges, and `A.6.RCD` for a derived relation kind.

Use the existing result or publication for a needed currentness conclusion or limitation. Use `RefreshPlan@Context`, `RefreshReport@Context`, `DeprecationNotice@Context` or `EditionBumpLog@Context` when the corresponding plan, performed work, deprecation or edition change actually occurs; do not add an empty ticket or notice for unchanged applicability.

When the governed object is a reusable `A.6.RCD` predicate definition or an admitted derived relation kind, the currentness line pins the exact base definitions, named substrate and edition, authorized derivation operation, and applicability scope. A change to any of them reopens the affected derivation and its dependent uses under `A.6.RCD`; G.11 schedules the bounded refresh but does not redefine the relation or derivation.

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)



Use `G.11` to plan scoped actions from typed causes; action semantics remain with their subject patterns.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness and decay events (`B.3.4`),
* evidence, bridge, policy, edition, relied-on base-definition, named-substrate-edition, or derivation-applicability edits (from the respective subject patterns' publication faces, forms, or units).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure over the actual dependencies.**
Compute the minimal dependency closure over:

* cited evidence and source relations, with `G.6` `PathId` and `PathSliceId` refs when a graph path slice is the current math-lens expression,
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions and policies).

G.6 supplies graph expression and citation when used; a graph does not establish the source or dependency relation. For a nongraph result, name the exact source, receiving result/use and dependency under `PatternScopeId`; use `PathSliceId` when that dependency scope is actually graph-expressed or independently required by the receiving contract. The closure is a planning-time claim about affected slices, distinct from execution of the planned refresh actions. Interpret a B.3.4 trigger for the receiving claim and use: available information may establish continued applicability, a narrower use, an obtainable refresh need or a necessary suspension. An age-only signal does not determine that disposition. If support remains sufficient, stop with the usable result; retain only the limitation or reason a later recipient needs.

**4.3.3 Planning (P2W boundary).**
When the selected response requires planned refresh, use C.11 and C.19.2 for its marginal contribution, cost, delay and displaced work. Produce `RefreshPlan@Context` for the actions actually selected; possible action forms include:

* `RerunHarvest` (delegates to the selected harvesting or SoTA method, such as `G.2`; use `G.1` additionally only when its generator-kit cards or wiring must change)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetResult` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates changes to the obtaining Bridge to `F.9`, calibration-record changes to `G.7`, and crossing visibility to `E.18` and the applicable visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
When selected actions are performed as Work or Work-bound audit, publish the corresponding `RefreshReport@Context`. A scoped applicability judgement can reuse available information without a new experiment; a plan alone establishes neither performance nor a new observation.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped result consumes C.28, refresh planning watches the causes that can change a supported use, unsupported use, support-result verdict, limits, or downstream decision basis:

| Sentinel | Affected result | Refresh pins |
| --- | --- | --- |
| sampling-realizability shift | `CounterfactualSamplingRealizabilityResult` | target distribution, decision Method and any derivation, physical, ethical, operational, and history constraints, required sampling construction or obstruction, unresolved questions, status, supported use, and unsupported use |
| performed sampling or resulting-data shift | dated sampling Work plus A.10 evidence path and empirical data regime | WorkPlan when used; actual performer identified through A.13; dated Work independently admitted through A.15.1; Method and window; resulting sample or data; provenance and currentness. Add F.6 with the same A.13 assignment only if the refresh decision needs to say exactly under which assignment the Work was performed. F.6 identifies neither performer nor assignment; a missing or failed attribution leaves the Work intact. A realizability result cannot substitute. |
| identification or bound shift | `CausalIdentificationResult` | data-regime refs, assumptions, identifying derivation, bound or failure witness, sensitivity |
| estimate shift | `CausalEstimateResult` | identification or design basis, data, estimator Method, diagnostics, uncertainty, sensitivity, and any live estimation-consistency result |
| target-trial practice shift | protocol and mapping results | question/estimand, protocol-to-data mapping, assumptions, estimate/precision, sensitivity and reporting source edition |
| causal-fairness shift | C.28 support result plus D.5 `BiasAuditReport@Context` | fairness estimand, extra counterfactual-identification assumptions, estimate and consistency result when used, support components and result, affected population, audit limits, and decision |
| causal-representation shift | `CausalVariableRepresentationRecord` | intervention validity, invariance, abstraction fidelity, query preservation, shift and use limits |
| off-policy or causal-RL shift | `OffPolicyCausalEvaluationResult` | behaviour/evaluation policies, horizon/history, confounding, overlap, endpoints, estimator and uncertainty |
| simulation-validation shift | `simulationResultRef` in `CausalSupportComponentRefs` | model assumptions, validation, sensitivity, supported model use and unsupported realized/interventional use |
| transport-endpoint shift | `CausalTransportabilityResult` | source/target population, domain, environment and data-generating regime, assumptions, windows, formula and unresolved limits |

These are payload distinctions under existing G.Core trigger kinds, not new trigger kinds. Reopen only the affected result and downstream uses that consumed it.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring live as `GPatternExtension` blocks. Scheduling, ordering, priority, and budget policy for the refresh queue are not separate extension semantics: `G.11` defines the required policy pins on `RefreshQueue` and `RefreshPlan@Context`, while A.15.2 and A.15.3 keep the WorkPlan and its local content separate from dated Work.



##### G.11:4.4.1 - GPatternExtension — G.11:Ext.TriggerAliases


**PatternScopeId:** `G.11:Ext.TriggerAliases`
**GPatternExtensionId:** `TriggerAliases`
**GPatternExtensionKind:** `InteropSpecific` (alias docking)
**GoverningPatternId:** `G.Core`
**Uses:** `{G.Core}` (cites `G.Core.TriggerAliasMap.G11`)
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `RSCRTriggerKindId[]` (canonical ids recorded on triggers)
* `RSCRTriggerAliasId?` (e.g., `G.11:T0…T7` as labels only)
* `scope: PathSliceId[] | PatternScopeId`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.



##### G.11:4.4.2 - GPatternExtension — G.11:Ext.DecayAndDebt


**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (use-qualified currentness and interpreted planning debt)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* The receiving claim/use and the changed premise or applicable review condition, with source references where published.
* `FreshnessWindowDeclRef?`, `DecayPolicyIdRef?` or `EpistemicDebtBudgetRef?` only when the adopted window, deterioration model or planning measure is used. Their source supplies the meaning; no default expiry or debt budget is required.
* Exact dependent claims and uses actually affected, expressed as `PatternScopeId` for nongraph scope or `PathSliceId[]` for graph scope. Retain graph pins when an independently applicable profile requires them; carrier age alone does not select every use of that carrier.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** B.3.4 determines what the trigger means for the use. Continue, narrow, refresh, suspend or an authorized exception remain available where warranted; no Refresh/Deprecate/Waive triad or automatic downgrade is introduced here. Currentness is not assurance of the underlying claim. Budget and priority logic apply only when their interpreted policies are used.



##### G.11:4.4.3 - GPatternExtension — G.11:Ext.QDRefreshWiring


**PatternScopeId:** `G.11:Ext.QDRefreshWiring`
**GPatternExtensionId:** `QDRefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` (QD semantics; descriptor, distance, and insertion)
**Uses:** `{C.18, C.19, G.5, G.8}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `DescriptorMapRef.edition`, `DistanceDefRef.edition`
* `CharacteristicSpaceRef.edition?` (required when a domain-family coordinate is declared by the QD governing definition)
* `InsertionPolicyRef`, `EmitterPolicyRef` (policy-bound)
* Exact archive or illumination scope and `policy-id` for emitted telemetry triggers: `PatternScopeId` for nongraph scope; `PathSliceId` when graph-expressed or required by an independently applicable parity, evidence or shipping contract.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.



##### G.11:4.4.4 - GPatternExtension — G.11:Ext.OEERefreshWiring


**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration and exploration-exploitation logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the subject patterns)
* `GeneratorFamilyRowRef = <GeneratorFamilyId, rowEdition>` and `TransferRulesRef` wiring pins (as published by G.5 and the governing definitions); resolve the exact row edition used by the affected result
* exact telemetry scope and `policy-id`: `PatternScopeId` for nongraph scope; `PathSliceId` when graph-expressed or required by an independently applicable parity, evidence or shipping contract.

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:4.4a - Scheduling and priority policy pins

Scheduling strategies (bandit-style allocation, queueing, cadence policies, early stopping, or manual priority rules) may influence the order and budget of refresh work, but they do not define trigger meaning, action semantics, parity semantics, shipping semantics, or Part-G-wide defaults.

`G.11` therefore treats scheduling as policy-bound refresh planning:

* `RefreshPriorityPolicyIdRef` names the policy used to order or prioritize queue items.
* `BudgetDeclRef` names the time, compute, cost, risk, or cadence boundary for the planned refresh.
* `RSCRTriggerKindId[]` still comes from `G.Core`; scheduling policy does not mint trigger kinds.
* planned refresh remains the exact `U.WorkPlan` locally called `RefreshPlan@Context`; executed refresh is recorded in `RefreshReport@Context` or Work-bound audit.

If no priority or budget policy is declared, no scheduling heuristic is admissible by appearance; the plan must either use the ordinary queue order or state the missing policy pin as a blocker.

### G.11:5 - Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). The maintenance team uses `G.11` to produce a refresh plan scoped to the affected inspection slices and publishes a refresh report of the executed actions with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by subject pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Calibration evidence changes, potentially affecting a bounded-use claim or a justified loss consequence. The maintainers identify which receiving uses depend on the changed row, retain matching results that remain supported, and use the canonical triggers to plan any needed targeted parity rerun. Re-shipping follows only when the publication needs the resulting change; a CL revision alone grants or withdraws no use.

**Paired currentness case.** A pack's export-date label changes, but its relied-on claims, source editions, qualification conditions and receiving use remain unchanged and adequately supported by available information. Retain the result; no refresh plan, waiver or no-refresh notice is needed. In the paired case, a dependency changes so that the shipped benchmark comparison no longer supports use beyond its stated window. Restrict that comparison and retain the warning with the shipped result so a later receiver cannot infer continued comparability. Plan the targeted check or update when it is justified and obtainable; currentness reporting alone does not repair the comparison.

**Three bounded currentness cases.** These are constructed applications of the same rule.

* A pump shortlist still consumes the same two immutable method rows, eligibility conditions and source edition. An age alert supplies no changed premise or expired use condition, and the available support remains sufficient for the same triage use. Retain the shortlist; no plan or omission certificate is needed.
* A local selected-set result consumes `PumpReviewBudget-E1`. Its replacement `PumpReviewBudget-E2` changes the allowed review time from 30 to 20 minutes. The existing result explicitly cites that budget; no evidence graph is in use. Scope `PumpTriageSelection` names that exact result, changed budget and dependent eligibility comparison. If re-selection is chosen, plan only that comparison through G.5 under `PatternScopeId=PumpTriageSelection`, carrying both budget editions and the current task/row refs. Record performed refresh and any required targeted check in the resulting report before republication.
* A shipped QD archive expresses its affected dependencies in `PathSliceId=ArchiveCell-Q7`. A distance-definition change reopens the comparison using that definition. Retain the slice, old/new `DistanceDefRef.edition`, descriptor, insertion/emitter and policy pins, and the applicable G.9/G.10 evidence and shipping requirements. An OEE change to `TransferRulesRef.edition` similarly retains its affected graph slice, exact generator row edition and environment-validity scope. Nongraph support elsewhere does not relax these contracts.

### G.11:6 - Bias-Annotation (informative)

Bias lenses: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions and policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: create queue, plan and report content only for the corresponding need; retain applicable support without an omission certificate, while preserving warnings a later receiver needs.
* **Onto and Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System and Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose and Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion plus explicit deltas; delegated to `G.Core`).                                                                                                                                       | `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD and OEE wiring).**     | When QD, OEE, or both are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin, edition, and policy wiring of the applicable extension blocks: `G.11:Ext.QDRefreshWiring`, `G.11:Ext.OEERefreshWiring`, or both. **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while keeping method-specific pin lists inside the applicable extension blocks.                  |
| **CC‑G11.3 (Telemetry-metric admissibility).** | A refresh **SHALL** retain the metrics and pins required by the applicable subject method and receiving contract. Any Q, D, QD-score, coverage or regret it publishes **SHALL** be published as telemetry metrics, and any published IlluminationSummary as a telemetry summary. These values **SHALL** be excluded from dominance unless a CAL policy explicitly promotes them, and the promoting policy id **SHALL** be recorded in SCR-visible evidence bindings through the cited subject patterns. | Preserves required telemetry and prevents covert scalarisation. |
| **CC‑G11.4 (Bridge penalties).** | Any refresh reacting to a sense or kind correspondence change or to a change in an independently governed plane relation **SHALL** satisfy `CC‑GCORE‑PEN‑1`. It **SHALL** preserve the obtaining relation under its direct governor, cited calibration basis and losses, and the separate receiving-use and reliance claims consumed by the refreshed result. It **SHALL** publish the `CL`, `CL^k`, `CL^plane` values and policy/model pins required by the actual calibration or receiving use, including any required `Φ`, `Ψ` and `Φ_plane` policy ids. Any supported loss penalty **SHALL** follow its declared assurance rule and affect `R_eff` only (F and G invariant). | Keeps the actual relation, calibration and assurance grounds recoverable during refresh. |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set or archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) with the comparator admitted for that use at its applicable edition, and preserve the actual declared outcome: the relevant selected-set kind, narrowed handoff, abstention, or escalation. A changed comparator basis must be explicit under its own governor; G.11 introduces no scalarisation or replacement result semantics.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).** | Refresh actions that touch cross-context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` under the obtaining relation's direct governor, retaining its relation reference and the separate receiving-use and reliance grounds required by that governor. An independently governed E.18 flow crossing or A.21 gate that consumes the refreshed content **SHALL** retain its required harness, pins, lexical constraints and lane checks. Missing required grounds or pins **SHALL** block the affected publication. | Makes reuse and actual flow crossings or gates checkable under their own requirements. |
| **CC‑G11.7 (Use-qualified currentness).** | A freshness or decay trigger SHALL be interpreted under B.3.4 for the relied-on claim/use and affected dependencies. Continue on sufficient applicable support without mandatory refresh, deprecation, waiver, WorkPlan or omission certificate. A later receiver SHALL receive the minimum action-changing limitation or reason with the existing result/publication. Publish `DeprecationNotice@Context` only for actual deprecation; an exception requires actual authority and scope. | Preserves useful currentness warnings without treating age as lost assurance or manufacturing a completion artefact. |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`, dominance, Γ-fold, or guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` and the applicable subject patterns rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).** | Before changed refresh content is republished downstream, run or cite the required targeted RSCR or regression check for its affected scope. Keep the reference in the existing result/publication or corresponding `RefreshReport@Context`. Reuse a current matching result for unchanged content; no new execution report is required solely to repeat that reference. A missing required check retains the applicable `degrade` or `abstain` outcome under its governing policy. | Keeps actual republication checks while separating their evidence from unnecessary repeated work. |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed publication or output consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification and bounding, target-trial reporting, causal fairness, causal representation validation, off-policy and causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped causal-use results while preserving `G.Core` trigger governance. |
| **CC-G11.11 (Relation-derivation dependency refresh).** | When a reused `A.6.RCD` predicate definition or admitted derived relation kind depends on base definitions, a named substrate edition, an authorized derivation operation, or an applicability scope, the refresh plan **SHALL** pin those dependencies and reopen the affected derivation and dependent uses when one changes. The plan uses existing canonical trigger kinds; it does not mint a relation-specific trigger kind. | Prevents a once-valid derivation from surviving a changed semantic or substrate basis. |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Cross-context or plane reuse lacks required relation/use/reliance grounds, or an actual flow crossing or gate lacks required visibility pins. | The reuse or crossing cannot be checked against its governing rule. | Restore the missing grounds; apply E.18/A.21 harnesses to independently governed flow crossings or gates. Block the affected publication when required grounds or pins are missing (CC‑G11.6). |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Lost currentness warning** | A later recipient relies beyond the supported condition or window because the changed limitation was omitted. | The old result can no longer support that receiving use. | Keep the minimum useful warning or decision with the existing result; use a deprecation notice only for actual deprecation. An unchanged immediate use needs no skip-refresh record (CC‑G11.7). |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning and execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear governing-definition assignment boundaries.** Orchestration coordinates actions under their governing definitions; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids, editions, and policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop coordinates reruns and republishing; trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W planning-to-work boundary** so that the exact `U.WorkPlan` and its declaration-local planned-filling rows remain planning content while dated Work remains independently established.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

**0. QD currentness requires visible survey support.**
   Practice: current QD work is surveyed as approaches, applications, and challenges, with archive, diversity, descriptor, and evaluator-currentness concerns still live.
   Source: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 2026, DOI `10.1016/j.swevo.2025.102240`.
   Alignment: `RefreshCurrentnessLine@Context` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, descriptor or distance edition, and path-slice scope, while `C.18`, `C.19`, and `G.5` keep archive, pool, and selected-set meanings.
   Adoption: **Adopt and bound** (survey support changes refresh currentness fields and boundaries; it is not the governing ontology source).

**0a. Open-ended engineering outputs need source and evaluator currentness.**
   Practice: self-improving-agent, AlphaEvolve-style, and DeepEvolve-style lines use generated variants, external knowledge, evaluators, tests, archives, and empirical validation.
   Source: Darwin Godel Machine `arXiv:2505.22954`, AlphaEvolve `arXiv:2506.13131`, and DeepEvolve-style deep-research augmentation `arXiv:2510.06056`.
   Alignment: G.11 refresh records carry source, evaluator, descriptor, policy, edition, lineage, and report refs; generated method text, evaluator success, and archive update keep their subject patterns.
   Adoption: **Adopt and adapt** (refresh tracks currentness and smallest affected scope; it does not accept generated text as proof, gate passage, or performed work).

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring, retraining, and reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (`arXiv:1706.04599`, 2017); Amershi et al., *Software Engineering for Machine Learning* (ICSE-SEIP 2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition and policy pins for replay.
   Adoption: **Adopt and adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift and decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (`arXiv:1802.07569`, 2019); De Lange et al., *A Continual Learning Survey* (`arXiv:1909.08383`, 2021).
   Alignment: `B.3.4` supplies use-qualified currentness. `G.11` interprets changed conditions and justified review signals before planning an affected-scope refresh; elapsed time alone implies neither truth decay nor deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor and distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy and edition conditions.
   Source: contemporary QD families such as CMA-MAE (`arXiv:2205.10752`) and differentiable QD (`arXiv:2106.03894`).
   Alignment: QD-specific meaning lives with the subject patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set and archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (`arXiv:1901.01753`, 2019); later generator-family claims require a named `G.2` SoTA pack or exact current source.
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt and adapt** (adapted to Part G pin and UTS publication discipline).

5. **Efficient orchestration benefits from bandit and early-stopping scheduling, but scheduling must not redefine trigger, action, parity, shipping, or Part-G-wide default semantics.**
   Practice: modern hyperparameter and experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: ASHA (`arXiv:1810.05934`) and BOHB (`arXiv:1807.01774`) as representative post-2015 scheduling practice.
   Alignment: scheduling is expressed as `RefreshQueue` and `RefreshPlan@Context` policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and the exact `U.WorkPlan` stays separate from dated Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; Default Governing Definition Index), `G.6` (EvidenceGraph, `PathId` and `PathSliceId`), `G.7` (Bridge sentinels; CL, Φ, and plane pins), `G.5` (selector and set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness and decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), `A.6.RCD` for reopening reused predicate definitions and derived relation kinds when their base definitions, named substrate edition, authorized derivation operation, or applicability changes, `C.18` and `C.19` archive, front, and live-pool policy pins, `C.32.P2S` when telemetry, decay, or freshness reopens architecture problem-to-structure carry-through, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support results, verdicts, supported-use values, unsupported-use values, and SoTA-sensitive causal-use sentinel payloads), `F.15` (RSCR harness publications, when present).
**Publishes to:** UTS (refresh plan, refresh report, deprecations, edition bumps), and to the relevant subject patterns’ publication faces, forms, or units through delegated actions.

### G.11:End

## G.12 — DHC Dashboards (Discipline-Health Time Series and Views)

> **Status:** Stable

**Tag:** Architectural kit pattern; notation-independent.

**Stage:** optional series authoring → measurement and series-update Work when needed → representation → optional publication and refresh.

**Primary hooks:** C.21 for discipline-health Characteristics and the common replay basis; C.16 for measurement; C.2.1 for result and series epistemes; C.29 when the view uses a mathematical correspondence; E.24.PUB for publication availability; G.6 for evidence paths when relied on; G.11 for refresh; G.Core, A.19, and G.0 for the exact legality and comparison surfaces actually used.

**Optional hooks:** G.2 for SoTA palettes, G.5 for selector results, C.18 and C.19 for QD or open-ended telemetry, G.8 for maturity views, G.10 for shipping, F.18 when public names are needed, and F.9 only for actual distinct-local-sense comparison.

### G.12:0 — Use This When

Use G.12 when a team needs several recorded C.21 coordinate results arranged across windows, a dashboard view over them, or refresh wiring for that view.

Start from the C.21 results, not from a screen layout. State the discipline, intended use, ClaimScope, coordinate-result refs, and windows. Stop with a local view when no audience publication or refresh use exists.

Do not use G.12 for one ordinary field-health claim, to manufacture measurements from rows, to turn a dashboard into evidence or authority, or to require publication and telemetry for every C.21 use.

### G.12:1 — Intent

Produce a reproducible discipline-health series and view while keeping these objects separate:

1. C.16 measurement results and their C.2.1 coordinate-result epistemes;
2. one optional C.2.1 `DHCSeries` episteme that orders exact result refs by window;
3. rows and slices that represent those results or series;
4. any E.24.PUB publication occurrence, form, carrier, audience, and availability interval; and
5. any measurement, series-assembly, rendering, upload, or refresh Work.

### G.12:2 — Problem Frame

Dashboards drift or become misleading when they:

* treat `ClaimScope` and a selected `TargetSlice` as one field;
* copy a value without its C.21 replay basis;
* average nominal or ordinal values or mix Units;
* hide normalization, distance, comparison, or target-band rules;
* require a Bridge for every source difference or omit F.9 when distinct local senses are actually related;
* turn a row, screenshot, UTS name, form, or carrier into the measurement or series episteme;
* turn selected sets or archives into one scalar winner; or
* rebuild everything because changed definition and evidence pins cannot be localized.

### G.12:3 — Forces

| Force | Tension |
| --- | --- |
| Readable view vs replay | A useful dashboard should be easy to read, while every relied-on coordinate must return to its exact definition and result. |
| Stable history vs changed definitions | A new method or Scale edition may invalidate trend comparability without changing historical results. |
| Optional publication vs local use | A local view may be enough; audience availability adds a separate publication relation. |
| Selective refresh vs process burden | Refresh needs actionable pins, but a one-off view needs no telemetry framework. |
| Set-valued results vs headline pressure | A view can summarize without manufacturing a scalar winner. |

### G.12:4 — Solution

#### G.12:4.0 — G.Core linkage

This pattern consumes G.Core obligations only for the branches actually opened.

**GCoreLinkageManifest (G.12)**

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }.
* `RSCRTriggerSetIds` := {`GCoreTriggerSetId.BridgeCalibrationKit`} only when crossing or refresh wiring is used.
* `RSCRTriggerKindIds` := {`RSCRTriggerKindId.LegalitySurfaceEdit`} only when a persisted series or view depends on that surface. Optional panels add only their own declared trigger kinds.
* `DefaultsConsumed` := `∅`; portfolio defaults become current only through `G.12:Ext.PortfolioTelemetry`.
* `CorePinSetIds` := {`GCorePinSetId.PartG.AuthoringMinimal`, `GCorePinSetId.PartG.CrossingVisibilityPins`} with nil-elision.

The minimal durable series basis is `DHCSeriesRef.edition`, `DisciplineRef`, `IntendedUse`, `ClaimScopeRef`, exact coordinate-result refs, and their windows. Each coordinate resolves the complete `DHCReplayBasis` from C.21. `PathSliceId[]`, crossing pins, public-name rows, shipping pins, publication refs, and telemetry pins are conditional.

#### G.12:4.1 — Objects

| Local name | Exact object | Boundary |
| --- | --- | --- |
| `DHCCoordinateResultRef` | Ref to one persisted C.21/C.16 coordinate-result episteme and its active C.21 replay basis. | It is not a row, series, evidence path, or acceptance decision. |
| `DHCSeries` | One C.2.1 episteme whose EntityOfConcern is the discipline and whose ClaimGraph orders coordinate-result refs by explicit windows under one intended use, ClaimScope, and comparison basis. | It is not a public U-kind, publication occurrence, dashboard, carrier, or Work. |
| `DHCRow` | One representation element showing an exact coordinate-result ref and selected readable fields. | It does not compute, establish, or replace the result. |
| `DashboardSlice` | A dashboard representation or grouping over exact row, result, or series refs; use C.29 when a mathematical correspondence is claimed. | It adds no comparison, normalization, acceptance, or selection semantics. |
| `DHCTelemetryPin` | A G.11-facing refresh payload with a canonical trigger, exact affected scope, and changed definition, window, evidence, or policy pins. | It is not evidence, currentness, an edition relation, or refresh Work. |
| dashboard publication | An E.24.PUB occurrence for one exact selected episteme edition expressed by the dashboard form, with its audience, bounded use, carrier, and availability interval. The selected edition may be a series, a coordinate result, or a view independently constituted as a C.2.1 episteme. | A view element, UTS row, rendering, upload, or release label does not supply episteme identity or make publication obtain. |

Conceptual forms:

```text
DHCSeries := <
  DHCSeriesRef.edition,
  DisciplineRef,
  IntendedUse,
  ClaimScopeRef,
  ComparisonBasis,
  CoordinateResultRefs[],
  WindowOrder,
  DHCDefinitionSetRef.edition?,
  TargetSliceRef?,
  CurrentnessRuleRef?
>

DHCRow := <
  RowId,
  DHCCoordinateResultRef,
  Window,
  DisplayedValue,
  DisplayedScaleOrUnit,
  DisplayedStance?,
  DisplayAnnotations?
>

DashboardSlice := <
  DashboardSliceId,
  DHCSeriesRef.edition?,
  IncludedCoordinateResultRefs[],
  IncludedRowIds[],
  ViewSpecRef?,
  Annotations?
>
```

`TargetSliceRef` is present only when the series construction or publication consumes an A.2.6 selection. The ClaimGraph must then state how each selected slice belongs to or is covered by the authoritative `ClaimScope`. A changing time window is not silently encoded as “latest.”

#### G.12:4.2 — Method of obtaining the result

**Stage A — Select what the view is about**

1. **Start from exact results.** Select persisted C.21 coordinate-result refs for one already identified discipline. Do not compute from labels or restate Characteristic semantics in G.12.
2. **Fix use, scope, and windows.** Name IntendedUse and ClaimScope. Add a `TargetSliceRef` only when the computation or publication really consumes it, and state its relation to the scope.
3. **Check replay identity.** For every coordinate, resolve the C.21 `DHCReplayBasis`: Characteristic, Scale, Unit when current, `DHCMethodRef.edition`, exact Method, MethodDescription edition when used, model or calibration pins when used, time or population basis, and any active distance or definition-set edition.
4. **Choose the comparison branch.** Directly comparable C.16 readings need no Bridge. Actual distinct-local-sense use cites the obtaining F.9 relation, observed loss, and a separate affirmative bounded-use claim naming direction, use rule, and loss tolerance, with the current supporting reliance required by F.9. Add reference-plane routing only when a real plane crossing is used; cite its exact basis, and keep any assurance consequence in R only.
5. **Open optional panels only when used.** Portfolio, QD, open-ended, maturity, SoTA, shipping, and advanced-view fields appear only through their extension blocks.

**Stage B — Construct or update content**

1. When new coordinates are required, obtain their C.16 measurement results and coordinate-result epistemes with the active C.21 replay basis. Identify the exact Method and dated measurement Work, and the MethodDescription, model, and calibration basis required for that measurement use. Keep these objects separate; G.12 creates none of them from a row.
2. When the receiving use needs one series episteme, assemble or revise the `DHCSeries` ClaimGraph from exact coordinate-result refs and windows. Otherwise construct the local view directly over those result refs. Series assembly may be dated Work; its resulting episteme remains separate from the Work or work record.
3. Apply A.18 and any exact A.19/G.0 comparison, normalization, distance, or aggregation rule actually used. Nominal and ordinal values remain non-arithmetic unless an explicit lawful transformation creates another Scale.
4. Construct `DHCRow` and `DashboardSlice` representations. They may omit fields for readability only when every displayed claim still resolves its exact result and replay basis.

**Stage C — Publish or refresh only when required**

1. If public designators are needed, use F.18 for names of already constituted series or views. A name row is not publication.
2. If an audience must be able to obtain a selected episteme edition, establish E.24.PUB with that exact edition, audience, bounded use, dashboard form, carrier, and interval. If the view itself is the selected episteme, recover its independent C.2.1 identity. Otherwise a view over several source epistemes identifies each selected edition and its publication occurrence. Construct a series episteme only when the receiving use needs that additional ordered account.
3. If changed definitions, windows, evidence paths, crossing bases, or policies must trigger selective maintenance, emit G.11 telemetry pins naming the affected result or series slice. Otherwise stop without refresh wiring.

#### G.12:4.9 — Optional Extensions

> An extension adds only the panel-specific fields, pins, and triggers consumed by that view. It does not redefine C.21, C.16, comparison, evidence, publication, selection, or refresh semantics.



##### G.12:4.9.1 - `G.12:Ext.SoTAPalette` — SoTA palette alignment


* `PatternScopeId`: `G.12:Ext.SoTAPalette`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.2`
* Optional pins: `SoTA_PackRef.edition?`, exact F.17 cell refs, and obtaining F.9 relation refs when alignment is actually displayed.
* No additional trigger kind by default.



##### G.12:4.9.2 - `G.12:Ext.PortfolioTelemetry` — selector result panel


* `PatternScopeId`: `G.12:Ext.PortfolioTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `G.5`
* Conditional values: `TaskSignatureRef?`, resolved `DominanceRegime`, resolved `PortfolioMode`, and exact selector result and basis refs.
* Set-returning semantics remain visible. A scalar headline is only a view annotation unless a separate policy lawfully constructs it.



##### G.12:4.9.3 - `G.12:Ext.QDTelemetry` — illumination or archive panel


* `PatternScopeId`: `G.12:Ext.QDTelemetry`
* `GPatternExtensionKind`: `MethodSpecific`
* `GoverningPatternId`: `C.18`
* Conditional pins: `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `CharacteristicSpaceSpecRef.edition?`, `InsertionPolicyRef`, `EmitterPolicyRef?`, `ArchiveSnapshotRef?`, and `PathSliceId[]` when refresh uses them.
* Illumination and coverage stay telemetry unless a separate accepted policy promotes them into the comparator, dominance set, or selected-set criteria under C.18's trade-off and authority conditions.



##### G.12:4.9.4 - `G.12:Ext.OpenEndedTelemetry` — open-ended or transfer panel


* `PatternScopeId`: `G.12:Ext.OpenEndedTelemetry`
* `GPatternExtensionKind`: `GeneratorSpecific`
* `GoverningPatternId`: `C.19`
* Conditional pins: `TransferRulesRef.edition`, `EnvironmentValidityRegionId?`, `ProbeBudgetPolicyId?`, and `PathSliceId[]`.
* Open-ended signals do not become dominance objectives by display.



##### G.12:4.9.5 - `G.12:Ext.MaturityLadderPanel` — maturity view


* `PatternScopeId`: `G.12:Ext.MaturityLadderPanel`
* `GPatternExtensionKind`: `DisciplineSpecific`
* `GoverningPatternId`: `G.8`
* Conditional values: `MaturityCardRef`, `MaturityRungId?`, and evidence-path refs when the displayed rung relies on them.
* Adds `RSCRTriggerKindId.MaturityRungChange` only for a refresh-wired view.



##### G.12:4.9.6 - `G.12:Ext.PackInclusion` — shipping stub


* `PatternScopeId`: `G.12:Ext.PackInclusion`
* `GPatternExtensionKind`: `InteropSpecific`
* `GoverningPatternId`: `G.10`
* Conditional values: exact pack ref, selected `DHCSeriesRef.edition` or `DashboardSliceRef`, and the replay or shipping pins the included claims actually require.
* G.10 governs shipping; this extension only identifies what is included.



##### G.12:4.9.7 - `G.12:Ext.ViewFamilySeed` — advanced view seed


This non-normative seed reserves no semantics. An embedding, prediction, change-point, or drift panel needs its own selected governor, inputs, limitations, and policy before it can affect a claim or decision.

### G.12:5 — Interfaces

| Interface | Consumes | Produces |
| --- | --- | --- |
| `Create_DHCSeries` | exact coordinate-result refs, discipline, intended use, ClaimScope, windows, comparison basis, optional definition-set and target-slice refs | one C.2.1 `DHCSeries` episteme edition |
| `Update_DHCSeries` | prior series edition, added or replaced exact result refs, affected windows, edition rule | successor series episteme edition only when C.2.1's historical-continuation predicate holds, plus exact edition relation when asserted |
| `Render_DHCView` | exact result or series refs, view specification, annotations | `DHCRow[]` and/or `DashboardSlice` representations |
| `Publish_DHCView` | exact selected episteme edition (series, coordinate result, or independently constituted view episteme), dashboard form, and E.24.PUB audience, bounded use, carrier, and interval | obtaining publication relation for that edition when its predicate holds |
| `Emit_DHCTelemetry` | exact changed definition, window, evidence, crossing, or policy pin and affected slice | G.11-facing telemetry payload |
| optional panel interfaces | the corresponding extension's exact values | only that panel's representation and conditional refresh pins |

### G.12:6 — Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-G12-1` | Every displayed coordinate resolves one exact C.21/C.16 result episteme and the active C.21 replay basis. |
| `CC-G12-2` | ClaimScope is authoritative; TargetSlice is optional, consumed explicitly, and related to that scope. |
| `CC-G12-3` | Direct same-semantics comparison uses C.16 conditions without a Bridge; actual distinct-local-sense use cites the obtaining F.9 relation, observed loss, and a separate affirmative bounded-use claim with its direction, use rule, loss tolerance, and the current supporting reliance required by F.9. |
| `CC-G12-4` | Characteristic, Scale, Unit, Method, MethodDescription, model, calibration, Work, result, result episteme, series episteme, row, slice, publication, form, and carrier are not collapsed. |
| `CC-G12-5` | Numeric, ordinal, target-band, normalization, distance, comparison, and aggregation operations cite their exact lawful definitions. |
| `CC-G12-6` | A series ClaimGraph identifies exact result refs, windows, intended use, ClaimScope, and comparison basis; content change uses the applicable edition rule. |
| `CC-G12-7` | Rows and slices are view-only representations. They introduce no new objective, scalar winner, evidence, acceptance, or authority. |
| `CC-G12-8` | Public names and E.24.PUB publication are conditional and separate; local dashboards need neither. |
| `CC-G12-9` | Refresh telemetry appears only for a named maintenance receiver and identifies the exact affected slice and changed pins. |
| `CC-G12-10` | Optional panel fields appear only with their extension and preserve the source pattern's set, archive, maturity, transfer, shipping, or palette semantics. |
| `CC-G12-11` | The effective G.Core obligations are expanded by value; nil-elided or unused branches are not made mandatory. |

### G.12:7 — Bias-Annotation

G.12 counters screen-first, “latest”-by-default, scalar-winner, and publication-as-truth bias. A clean view can hide incompatible definitions, while a dense technical record can make a simple trend unreadable. Start from exact result claims, show the smallest useful view, and keep deeper replay and refresh detail addressable rather than visually dominant.

### G.12:8 — Consequences

**Benefits.** Dashboard claims can be read quickly and replayed from exact result and definition refs. Historical results remain distinct from changed definitions, and refresh can be local when needed.

**Costs.** A relied-on trend needs exact result, scope, window, and replay identities. Publication and refresh add their own conditional work.

**Risks avoided.** Screenshot-as-result, scope/slice collapse, hidden method drift, illicit ordinal arithmetic, scalarization by view, and carrier-as-publication are blocked.

### G.12:9 — Relations

**Builds on:** C.21, C.16, C.2.1, A.2.6, C.29, E.24.PUB, and G.Core only for the active Part-G branches.

**Coordinates with:** G.6 and G.11 for relied-on evidence and refresh; A.19 and G.0 for comparison or aggregation; F.9 for actual distinct-local-sense use; F.18 for optional public names; G.5, C.18, C.19, G.8, G.10, and G.2 through the declared extensions.

### G.12:10 — Author's Quick Checklist

1. Name the discipline, intended use, ClaimScope, exact coordinate-result refs, and windows.
2. Resolve the C.21 replay basis for every coordinate.
3. Add TargetSlice only when consumed and state its relation to ClaimScope.
4. Use the direct comparison branch unless distinct local senses actually require F.9.
5. Keep series episteme, measurement Work/result, row, slice, publication occurrence, form, and carrier separate.
6. Add public naming, publication, evidence paths, assurance, optional panels, and refresh only for named receivers.

### G.12:11 — Worked Micro-examples

**Decision-making dashboard.** A local view shows exact `ReproducibilityRate`, `FormalRecognitionStatus`, `PracticeAdoptionRate`, `AlignmentDensity`, `TraditionShareEntropy`, and `TraditionShareConcentration` result refs. Entropy and HHI occupy separate rows with their directions visible. A portfolio panel preserves the G.5 selected set. No audience publication is claimed.

**Evolutionary architecture dashboard.** A `DHCSeries` episteme orders exact reproducibility and DisruptionBalance results over declared windows. An optional open-ended panel shows transfer events as telemetry. A later E.24.PUB occurrence makes one selected dashboard form available to a named audience; that occurrence neither changes the series content nor turns the rendering Work into the health result.

### G.12:End

## G.13 - External Interop Hooks for SoTA Discipline Packs (conceptual)

**Tag.** Architectural kit pattern (conceptual interop kit; notation‑independent; normative when used)
**Stage.** *design‑time registration & alignment* → *run‑time ingestion, telemetry, refresh*
**Primary hooks.** `G.Core` (Part‑G core invariants + trigger catalogue + Default Governing Definition Index), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.4` (CAL Pack), `G.5` (selector & registries), `G.6` (EvidenceGraph + PathId/PathSliceId), `G.7` (BridgeMatrix + CL/planes), `G.8` (SoS‑LOG bundle surfaces), `G.9` (parity harness), `G.10` (shipping), `G.11` (refresh orchestration), `G.12` (dashboards), `A.19` (CN‑Spec), `A.18` (CSLC legality), `G.0` (CG‑Spec), `F.17` (UTS), `F.9` (cross-semantic relations and bounded-use claims), `E.17` (publication faces), `E.5.2` (notation independence), `E.18` (crossing visibility when a selected transformation-flow structure is in use), `A.21` (gate decisions under an applicable profile).

**Status.** Stable
**Normativity.** Normative when used (when any `G.13` surface is authored/emitted/consumed); informative otherwise.

**Part‑G linkage.** `G.Core` governs Part‑G‑wide invariants; the linkage manifest in §4.1 and the conformance checklist in §8 name the applicable obligations.

### G.13:1 - Problem frame

FPF already supports lawful characterization, evidence wiring, selector‑side set returns, parity, shipping, dashboards, and refresh. What remains frictionful in practice is **interoperability with external scholarly indexes and discipline repositories** (concept registries, paper/claim graphs, dataset registries, taxonomy stores, “science‑of‑science” indicator feeds), which teams routinely use as *inputs* when authoring a SoTA discipline pack.

Without an explicit **conceptual interop kit**, authors tend to build one‑off pipelines whose “implied semantics” leak into the framework: edition drift becomes invisible, cross‑plane/context reuse becomes implicit, and external signals quietly start acting like a shadow governing spec ref.

`G.13` provides the missing kit: **conceptual registration, alignment, and telemetry hooks** that let external sources be wired into the Part‑G pipeline (**G.2 → G.5 → G.9 → G.10 → G.11**, and optionally **G.12**) while preserving Part‑G invariants via `G.Core`.

### G.13:2 - Problem

External sources publish **claim‑adjacent signals** (citations, concept graphs, “task/method” tags, replication links, dataset usage, disruption‑style indicators, benchmark metadata). These are useful for *generation* (palette building, declared set-result exploration, candidate bridge discovery), not only for audit. But typical interop practices create predictable failure modes:

* **CN/CG spec-ref leakage.** External numeric signals get treated as if they were lawful “scores” without explicit binding to CHR/CAL/CG surfaces.
* **Implicit crossings.** Cross‑context and cross‑plane reuse happens through opaque transformations, without explicit exposure of the crossing bundle pins needed downstream.
* **Edition drift + refresh brittleness.** Snapshots change, schemas drift, indicator definitions get revised; without edition‑pinned interop surfaces and typed trigger causes, parity and dashboard stability degrade.
* **Evidence disconnect.** “Derived features” are produced without explicit EvidenceGraph anchoring, making later refutation/repair expensive.
* **Format‑as‑norm.** A convenient serialisation (KG export, JSON schema, RO‑Crate, etc.) becomes treated as the specification, undermining notation independence.

### G.13:3 - Forces

| Force                           | Tension                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Notation independence**       | Useful serialisations vs the requirement that conformance is judged on **conceptual** surfaces.        |
| **Pluralism vs parity**         | Diverse scholarly traditions and indexes vs lawful, edition‑aware comparability and reproducibility.   |
| **Interop as generation input** | Interop should speed SoTA authoring, not merely decorate audit reports.                                |
| **Planes & bridges**            | Cross‑plane/context reuse must remain explicit and auditable rather than implicit in “aligners”.       |
| **Telemetry vs dominance**      | External telemetry should inform exploration and refresh without silently changing selector semantics. |
| **Operational drift**           | External sources evolve; interop must be refresh‑ready by construction (typed causes + payload pins).  |

### G.13:4 - Solution — Conceptual interop kit: registered sources, alignment cards, feature derivations, and RSCR‑wired telemetry

#### G.13:4.1 - G.Core linkage (normative)

**Builds on:** `G.Core`.

**GCoreLinkageManifest (normative).**
*(Canonical form, Nil‑elision, and Expansion rule are defined in `G.Core`.)*

`GCoreLinkageManifest := ⟨
  CoreConformanceProfileIds := {
    GCoreConformanceProfileId.PartG.AuthoringBase,
    GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted,
    GCoreConformanceProfileId.PartG.ShippingBoundary
  },
  RSCRTriggerSetIds := {GCoreTriggerSetId.SoTAHarvestSynthesis},
  RSCRTriggerKindIds := {RSCRTriggerKindId.BaselineBindingEdit},   // delta: planned‑baseline linkage edits can be interop‑relevant

  CorePinSetIds := {
    GCorePinSetId.PartG.AuthoringMinimal,
    GCorePinSetId.PartG.CrossingVisibilityPins
  },

  CorePinsRequired := {
    // Interop pins (G.13‑specific; avoid duplicating `GCorePinSetId.PartG.CrossingVisibilityPins`)
    ExternalIndexRef.edition,
    ClaimMapperRef.edition?,
    MappingPolicyRef?,
    PlaneMapRef.edition?,
    ScaleEmbeddingSpecRef.edition?,

    EvidenceGraphId?,
    InteropSurfaceId?
  },

  DefaultsConsumed := {DefaultId.PortfolioMode, DefaultId.DominanceRegime}
⟩`

**Payload‑pin note (informative).** When emitting RSCR triggers for interop‑driven changes, payload pins should include the edited edition/policy identifiers, the impacted scope, and the applicable crossing‑visibility pins (per `GCorePinSetId.PartG.CrossingVisibilityPins`) when crossings/UTS/paths are involved.

#### G.13:4.2 - Interop kit objects & surfaces (pattern-governed; notation‑independent)

All objects below are **conceptual**. Any concrete serialisation belongs to Annex/Interop or tooling notes and is not normative for Part‑G conformance.

* **`ExternalIndexCard@Context`** — registration of an external source and its snapshot.

  **Shape (conceptual):**
  `⟨ ExternalIndexId, ProviderName?, ExternalIndexType, CoverageScope, Licence?, ExternalEdition, FreshnessWindow?, entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩, Notes? ⟩`

  **Intent.** Create a stable, citable “source card” so downstream artefacts can pin the *card edition* via `ExternalIndexRef.edition`, while the provider snapshot remains visible as `ExternalEdition` (do not echo provider snapshot ids into downstream cards; cite refs instead).

* **`ClaimMapperCard@Context`** — a conceptual “mapping recipe” that yields FPF‑native artefacts from an external source.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * This is **not** a shadow legality gate. It is an interop surface that **cites** governing definitions (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the required pins for downstream audit/refresh.
  * When cross-plane or cross-context reuse is implicated, alignment outputs must cite the actual relation and the receiving-use and reliance grounds required by its governor. Carry bundle or gate anchors when an independently applicable `E.18` flow crossing or `A.21` gate consumes the alignment, as required by `CC‑GCORE‑CROSS‑1`.
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation records **typing + provenance**; comparator and legality definitions remain with the cited governing patterns. When features are used as DHC measurements, establish or reuse C.16 measurement results. Make the active C.21 `DHCReplayBasis` recoverable for every persisted, compared, aggregated, or published coordinate.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** Make any representation alignment *explicitly constrained* and edition‑pinned, instead of silently “creating a new scale”.
  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a LEX head; when a public id is minted for a `ScaleEmbeddingSpec`, the corresponding UTS row must be published with twin labels (see `G.Core` / UTS profile).

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Publication.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector-facing or dashboard-facing summary of what interop publications and records exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Generation‑first interop flow (notation‑independent; governing-definition delegating)

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source/snapshot used for SoTA authoring, including `ExternalEdition` and the `entityOfConcern` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` describing which FPF artefacts are produced (ClaimSheets, BridgeHints, feature sets, UTS proposals), and which policies/specs constrain the mapping (policy refs + optional `PlaneMapRef` / `ScaleEmbeddingSpecRef`).
3. **Produce FPF‑native inputs.** Use the alignment recipe outputs as inputs to:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features support DHC readings; measurement claims consume C.16 results with the C.21 replay basis required by their use).
4. **Feed selection/parity/shipping without smuggling semantics.**

   * `G.5` consumes the produced artefacts under its own governing spec refs and returns its declared outcome, including the applicable set-result kind, narrowed handoff, abstain, or escalation result (selector semantics remain governed by `G.5` + `G.Core`).
   * `G.9` parity consumes pinned editions/windows and produces traceable parity reports.
   * `G.10` shipping may include interop surfaces **as cited publications or records**; `G.13` does not govern shipping.
5. **Emit telemetry and refresh causes.** On any change in external editions, alignment policies, plane maps, or embedding specs, emit:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * a scope (`PathSliceId[]` and/or `PatternScopeId`),
   * payload pins (editions/policies/UTS rows),
     enabling `G.11` to plan slice‑scoped refresh.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, entityOfConcern anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
| **G.13‑2 `Map_ClaimsToFPF`**   | Apply `ClaimMapperCard@Context`   | `ExternalIndexCard@Context`, `MappingPolicyRef`, optional `PlaneMapRef`/`ScaleEmbeddingSpecRef`, optional EvidenceGraph hooks | `ClaimSheet@Context`, `BridgeHints`, optional `SoSFeatureSet@Context`, optional UTS proposals |
| **G.13‑3 `Derive_SoSFeatures`**  | Produce CHR‑typed SoS features  | ClaimSheets / external signals refs, CHR typing refs, legality proof hooks | `SoSFeatureSet@Context` (CHR‑typed; provenance pinned)   |
| **G.13‑4 `Publish_InteropSurface`**  | Publish interop summary | outputs of G.13‑2/‑3, UTS refs | `InteropSurface@Context` (+ UTS rows/twins) |
| **G.13‑5 `Emit_IndexTelemetryPin`** | Emit refresh input  | edition/policy changes + scope + payload pins  | telemetry to `G.11` (typed causes + payload pins)   |
| **G.13‑6 `Wire_To_SoTA_Pack`** | Provide shipping hook  | `InteropSurface@Context` + citations to upstream artefacts  | `G.10` pack hooks (as cited payload; no serialisation mandated)  |

### G.13:5 - Extensions (pattern‑scoped; non‑core)

`G.13` keeps provider/method specifics out of the kit core. Any such specificity appears as `GPatternExtension` blocks with stable **PatternScopeId**s. These modules are **wiring‑only**: they bind pins/editions/policies and cite the governing pattern rather than redefining semantics.

#### G.13:5.1 - `G.13:Ext.ExternalIndexProviderWiring` *(Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.ExternalIndexProviderWiring`
**GPatternExtensionId:** `ExternalIndexProviderWiring`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(Annex/Interop or a future dedicated interop-governing pattern)*
**Uses:** `{G.13}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ExternalIndexType`
* `ExternalEdition` *(as published on `ExternalIndexCard@Context`)*
* `Licence?`
* `CoverageScope`
* `ProviderChangePolicyId?` *(if provider‑specific “schema drift” handling exists)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* Provider‑specific ingestion choices (e.g., OpenAlex‑class, Crossref‑class, ORKG‑class, discipline repositories) **must not** become Part‑G‑wide norms in Phase‑2. This module only records which provider cards exist and which editions/policies are pinned.

#### G.13:5.2 - `G.13:Ext.EmbeddingBasedAlignment` *(Phase‑3 seed; method‑specific wiring stub)*

**PatternScopeId:** `G.13:Ext.EmbeddingBasedAlignment`
**GPatternExtensionId:** `EmbeddingBasedAlignment`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(Annex/Interop or a future dedicated interop-governing pattern; Phase-3 governing-pattern decision required)*
**Uses:** `{G.13, A.19, E.5.2}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `ScaleEmbeddingSpecRef.edition`
* `NormalizationMethodRef.edition?` *(when a declared normalization/representation transform is used)*
* `MappingPolicyRef`
* `EvidenceGraphId?` *(when evidence paths for alignment decisions are published)*

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (wiring‑only; post‑2015 practice orientation):**

* “Embedding‑based” techniques are treated as **declared transforms** constrained by `ScaleEmbeddingSpec` and/or `NormalizationMethod` references, rather than as implicit semantics.
* The module binds editions and policies; it does not define what is “similar enough”.

#### G.13:5.3 - `G.13:Ext.EntityResolutionAndAliasDocking` *(interop‑specific; Phase‑3 seed)*

**PatternScopeId:** `G.13:Ext.EntityResolutionAndAliasDocking`
**GPatternExtensionId:** `EntityResolutionAndAliasDocking`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected` *(likely UTS-adjacent; requires Phase-3 governing-pattern decision)*
**Uses:** `{F.17, E.10}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `UTSRowId[]` *(for externally‑sourced entities that become publicly citable)*
* `ExternalIdAliasSetId?` *(labels only; canonical ids remain UTS ids)*
* `TokenizationPolicyId?`

**RSCRTriggerSetIds / RSCRTriggerKindIds:** `∅` *(covered by `G.13:4.1`)*
**Notes (seed; wiring‑only):**

* This module exists to prevent “ID drift by renaming” for externally sourced entities. It is intentionally a Phase‑3 seed until its governing pattern is selected.

### G.13:6 - Archetypal grounding (informative; SoTA‑oriented)

**System.** *Software architecture portfolio design.*
Register an external scholarly index edition for “software architecture” concept neighborhoods. Align extracted technique/tactic claims into ClaimSheets and derive a CHR‑typed feature set (e.g., evidence depth, maturity). Select a **set** of tactics under multi‑objective tradeoffs, use `G.5` to declare that result, and ship a SoTA pack that cites the interop surface.

**Episteme.** *Science‑of‑science discipline dashboard.*
Align external claim graphs (replication, standardisation, disruption-style proxies) into CHR-typed features. For the selected DHC coordinates, establish or reuse C.16 measurement results and recover their active C.21 `DHCReplayBasis`. Use those result refs in the DHC series and its dashboard slice. Publish the selected series episteme through the dashboard form, citing `ExternalIndexRef.edition`, `ClaimMapperRef.edition`, and `MappingPolicyRef`; emit refresh triggers when the external edition updates.

**OEE/QD.** *Open‑ended environment generation.*
Register external environment/task taxonomies as index cards. Align them into generator‑family registries (as cited publications or records), keeping coverage/regret strictly as telemetry inputs. Use refresh to re‑align when the taxonomy edition changes.

### G.13:7 - Bias‑Annotation (informative)

* **Vendor/tool bias.** The kit names conceptual surfaces only; it avoids vendor‑specific file formats or tooling claims.
* **Metric‑authority bias.** External indicators are treated as *inputs* that must be typed, pinned, and evidenced; they are not authority by default.
* **Representation bias.** Representation/embedding choices are forced into explicit `Spec` + edition pins (no hidden semantics).
* **Discipline bias.** Interop supports pluralism by preserving explicit crossings and versioned alignments instead of forcing a single canonical external ontology.

### G.13:8 - Conformance Checklist (CC‑G13; applies when G.13 surfaces are used)

1. **CC‑G13‑CoreRef.** *(normative)* `G.13` implementations **MUST** satisfy the *effective* `G.Core` obligations declared by `G.13:4.1` (`GCoreLinkageManifest`), including trigger typing, Default Governing Definition Index citation, and crossing‑visibility pin discipline.

2. **CC‑G13‑InteropIsNotASpecRefSurface.** *(delegated)* Interop surfaces **MUST NOT** introduce shadow legality/comparability gates; they cite `CN‑Spec`/`CG‑Spec`/CHR/CAL governing definitions and publish pins instead.
   → delegate to `CC‑GCORE‑CN‑CG‑1`.

3. **CC‑G13‑CrossingsAreExplicitWhenInteropTouchesPlanesOrContexts.** *(delegated)* Any cross‑plane/context reuse implied by alignment **MUST** be made explicit through the crossing visibility discipline.
   → delegate to `CC‑GCORE‑CROSS‑1`.

4. **CC-G13-PlanePenaltyPoliciesArePinned.** *(local; governing-definition citing)* If `PlaneMapRef` is used (or alignment implies plane‑level penalties), interop surfaces **MUST** publish the relevant policy‑id pins via the crossing‑visibility discipline, and any such policies **MUST** satisfy the constraints governed by `CG‑Spec` (cite `CC‑G0‑Φ`). Interop surfaces **MUST NOT** define interop‑local penalty functions.

5. **CC‑G13‑SetReturnPreserved.** *(delegated)* Interop **MUST NOT** introduce hidden scalarisation or forced single‑winner selection.
   → delegate to `CC‑GCORE‑SET‑1`.

6. **CC‑G13‑DefaultClaimsAreCitationsOnly.** *(delegated)* Any mention of defaults (e.g., dominance regime, `PortfolioMode`) is a **citation** to the default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`, not a local default statement.
   → delegate to `CC‑GCORE‑DEF‑1`.

7. **CC‑G13‑EditionDisciplineForInteropCards.** *(local)* `ExternalIndexCard@Context` and `ClaimMapperCard@Context` **MUST** expose edition pins (`ExternalIndexRef.edition`, `ClaimMapperRef.edition`). Any interop surface published to UTS **MUST** cite the relevant `…Ref.edition` values (incl. `PlaneMapRef.edition?`, `ScaleEmbeddingSpecRef.edition?`) when present.
   FPF edition keys **MUST** appear only on `…Ref.edition` pins when a reference is present. Provider snapshot labels (e.g., `ExternalEdition` on `ExternalIndexCard@Context`) may exist on the source card, but **MUST NOT** be copied into downstream artefacts as free‑floating “edition fields”; downstream artefacts cite the corresponding `…Ref.edition` pins instead.
   In particular, interop transforms **MUST NOT** perform illicit arithmetic on ordinal/compare‑only scales (e.g., averaging or subtraction); any aggregation must be via lawful CAL operators with explicit scale legality (cite `A.18` / `CC‑G0‑CSLC`).

8. **CC‑G13‑SoSFeaturesAreCHRTypedAndLegal.** *(local; governing-definition citing)* If `SoSFeatureTransform@Context` is used, produced SoS features **MUST** be CHR‑typed via `FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}` (governed by `G.3`) and any legality/units obligations must be satisfied via CSLC/CG governing definitions (cite `A.18` / `G.0` / `G.4`; do not invent interop‑local legality gates). When those features serve as DHC measurements, the use **MUST** consume C.16 measurement results; every persisted, compared, aggregated, or published coordinate **MUST** make its active C.21 `DHCReplayBasis` recoverable.

9. **CC‑G13‑TelemetryEmitsCanonicalTriggerKinds.** *(delegated)* Interop‑driven changes (external edition bumps, mapping policy changes, plane‑map edits, embedding‑spec edits) **MUST** emit canonical `RSCRTriggerKindId` causes with explicit scope and payload pins.
   → delegate to `CC‑GCORE‑TRIG‑1`, `CC‑GCORE‑TRIG‑2`, `CC‑GCORE‑TRIG‑3`, `CC‑GCORE‑TRIG‑4`.

10. **CC‑G13‑IDContinuityForExternallySourcedIdentifiers.** *(delegated)* Interop publication **MUST** follow Δ‑discipline: no “renaming by meaning”; use aliases/deprecations as required.
    → delegate to `CC‑GCORE‑ID‑1`, `CC‑GCORE‑ID‑2`.

11. **CC‑G13‑NotationIndependence.** *(local)* Conformance is judged on the conceptual objects in `G.13:4.2`. Any serialisation is non‑normative and must not redefine semantics.
   *(Cites `E.5.2` for notation independence.)*

### G.13:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern: “Format == spec”.** Treating an export schema (KG dump, JSON, RO‑Crate, etc.) as the normative definition.
  **Remedy:** Keep `ExternalIndexCard` / `ClaimMapperCard` / `InteropSurface` as the conceptual specification; treat serialisation as an appendix/tooling concern.

* **Anti‑pattern: Hidden scale invention.** An embedding similarity becomes a “score” without explicit typing/binding.
  **Remedy:** Require `ScaleEmbeddingSpecRef` + edition pins and bind any derived features through CHR/CAL governing definitions.

* **Anti‑pattern: Implicit plane/context reuse.** Reusing external concept graphs across contexts without explicit crossing pins.
  **Remedy:** Publish crossing visibility pins and cite bridge/plane governing definitions; never fuse contexts “inside the aligner”.

* **Anti‑pattern: Edition‑free dashboards.** Feeding externally derived rows into dashboards without pinned editions/policies.
  **Remedy:** Pin `ExternalIndexRef.edition` and `ClaimMapperRef.edition`; emit RSCR triggers on changes.

* **Anti‑pattern: Interop asserts defaults.** “Interop decides dominance regime / `PortfolioMode`.”
  **Remedy:** Treat defaults as citations only (the relevant governing definition is cited through `G.Core.DefaultGoverningDefinitionIndex`).

### G.13:10 - Consequences

* **Interop becomes refresh‑ready.** External source drift produces typed RSCR causes with scopes/payload pins; refresh becomes slice‑scoped rather than global guesswork.
* **Generation‑first authoring becomes cheaper.** External sources become controlled inputs into SoTA synthesis and declared set-result exploration, not ad‑hoc audit decoration.
* **Conceptual hygiene improves.** Explicit cards + edition pins reduce semantic leakage from tools/formats/providers.
* **Cross‑tradition reuse becomes auditable.** Plane/context reuse is surfaced as crossings rather than embedded assumptions.

### G.13:11 - Rationale

FPF is a conceptual framework for disciplined creative work. An explicit interop kit lets authors use the fast, wide coverage of external scholarly infrastructure while keeping comparisons, editions, and transformations visible.

`G.13` provides **conceptual registration, alignment, and telemetry hooks**: cards and surfaces pin editions, cite governing patterns, and expose provenance hooks; telemetry hooks produce typed refresh causes. Domain/tool specifics remain in `Extensions` (or Phase‑3 governing definitions).

### G.13:12 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Scholarly claim graphs & open indexes.** Open research KGs and open scholarly indexes encourage claim‑level representations and concept taxonomies as interop substrates (post‑2015 ecosystem: KG‑style contribution graphs; open indexing initiatives). Treat these as *sources* registered via `ExternalIndexCard`, not as governing patterns.

* **Neural representations for scientific text.** Transformer‑based scientific encoders (e.g., SciBERT‑class; citation‑aware paper representations such as SPECTER‑class; later retrieval‑oriented scientific embedding families) are useful as *alignment heuristics*. In FPF terms, they belong behind `ScaleEmbeddingSpec` + pinned editions/policies (see `G.13:Ext.EmbeddingBasedAlignment`).

* **Schema matching & entity resolution (deep‑learning era).** Modern matcher families (deep entity matching, contrastive representation alignment, GNN‑assisted graph alignment) help populate interop cards, but must not become “implicit semantics”; record their use as policy‑bound wiring in extensions.

* **Systematic review process modernisation.** PRISMA‑2020‑class review records (post‑2015 practice) are valuable as evidence anchors and coverage telemetry; treat them as evidenced inputs (EvidenceGraph anchors + pinned editions/windows), not as legality gates.

* **QD / Illumination and OEE declared set results.** Post‑2015 QD (MAP‑Elites successors, CMA‑ME line, differentiable QD toolkits) and OEE (POET‑class and related environment/method co‑evolution lines) often rely on external taxonomies and environment corpora. Interop should expose those as pinned external editions and keep coverage/regret as telemetry inputs—never as implicit dominance.

### G.13:13 - Relations

**Builds on:** `G.Core`.
**Imports:** `G.2`, `G.3`, `G.4`, `G.5`, `G.6`, `G.7`, `G.9`, `G.10`, `G.11`, `A.19`, `A.18`, `G.0`, `F.17`, `E.5.2`, `E.18`.
**Publishes to:** UTS (twin labels where applicable); refresh inputs to `G.11`; shipping hook surfaces to `G.10` (as cited publications or records).
**Relates to:** `G.12` (dashboards), `G.8` (SoS-LOG bundle surfaces) when interop-derived publications or records are consumed there.

### G.13:14 - Author’s quick checklist (informative)

1. Register each external source snapshot as an `ExternalIndexCard@Context` with explicit `ExternalEdition`.
2. Author a `ClaimMapperCard@Context` with explicit `MappingPolicyRef` and required edition pins.
3. If you derive SoS features, declare a `SoSFeatureTransform@Context` and cite CHR typing refs and provenance hooks.
4. Publish an `InteropSurface@Context` that cites all active `…Ref.edition` values and UTS rows.
5. On any external edition or policy change, emit canonical RSCR trigger causes with explicit scope + payload pins.
6. Keep provider/tool specifics in `Extensions` (or Phase‑3 seed) and do not let formats redefine semantics.

### G.13:End

# Part H - Reserved


# SOURCE_FILE: LICENSING.md
---
# Licensing FPF Library

Copyright (c) Anatoly Levenchuk.

## Our framework publications

The original content of First Principles Framework (FPF) and the DPF publications by Anatoly Levenchuk, including the Foundational Thinking, Engineering, Management and Human Capability Engineering DPF Suites, their predecessors, and Narrativization and Narrative Studies Principles Framework, is licensed under the [Creative Commons Attribution 4.0 International license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

This grant covers the FPF specification, our DPF publications, the Library and Suite READMEs and Architectural References, and their maintained textual sources, including pattern bodies, prefaces, explanations and original worked examples. It also covers our later revisions of these publications when they carry the same license notice. The complete, unmodified license is in [LICENSE](LICENSE).

You may copy, redistribute, translate and adapt this material, including commercially. When sharing under this license, give appropriate credit, link to the license and indicate changes; retain supplied attribution and notices as required by the license. Where your use needs no copyright permission, including under an applicable exception, the license conditions do not apply. Attribution must not imply the author's endorsement. The legal code defines the complete terms.

For example:

> Adapted from Anatoly Levenchuk, FPF Library, First Principles Framework (FPF Core), September 2026, https://github.com/ailev/FPF. Licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changes: translated the explanation and replaced the worked example.

For a precise citation, we recommend naming the actual framework or pattern, its stated date and a brief description of modifications. These details are citation recommendations; the license defines the required attribution and indication of changes.

## Your own DPF or LPF

Authors choose the license for their own original DPFs and LPFs, including a different open license or a proprietary license. Applying FPF concepts or methods, referring to its PatternIDs, or following its publication form does not require licensing the resulting work under CC BY 4.0. Copyright licenses govern protected expression, not the underlying ideas or methods.

When you share copied or adapted expression under CC BY 4.0, comply with its terms for that material. Applicable copyright exceptions remain available. You may choose terms for your own contributions to an adaptation, provided those terms do not prevent recipients from complying with CC BY 4.0 for the reused material. Identify the reused material and its license separately when the surrounding publication has different terms. CC BY 4.0 has no ShareAlike requirement.

## Other material in the repository

Third-party quotations, illustrations and other material remain subject to their rights holders' terms or applicable copyright exceptions. Follow their source credits and any item-specific notices; this grant covers only rights held by Anatoly Levenchuk. A bibliographic reference does not relicense the cited work.

Repository tooling (software, scripts and configuration files), imported source literature and other independently authored products are outside this grant unless explicitly marked otherwise. Consult their own notices. This publication release does not select a software license or impose a license on independently authored LPFs.


# SOURCE_FILE: USING-FPF.md
---
# Using FPF Library

This is the common working instruction for people and AI agents using FPF Library, including work that develops or reviews the frameworks themselves. Apply it whenever the work relies on their methods, not only when processing an intake. Paths below are relative to the folder containing this file.

For an assisting agent, make this instruction part of the project's ordinary instructions: attach the file or link it from `AGENTS.md` or the environment's equivalent. A link in a past conversation does not establish that the current performer can retrieve and apply it. Reuse a current reading while the instruction and access conditions remain unchanged; return to the relevant section when they change or the instruction is no longer available in working context.

When a referenced publication is present in this folder, resolve its pattern references in that copy, including references written as GitHub links. Use another edition when the task calls for an update or a comparison.

## Make the publications available

Check what the present environment can actually read and search. A GitHub link, a listed filename or a truncated preview is not access to the publication's full text. Some interfaces cannot retrieve a large publication through an attachment or connector. Do not assume that one interface's access limits apply to another.

Where the environment supports local files, obtain the publication files through an available download or repository checkout and use content search on those files. Keep this instruction with them. Where only excerpts can be supplied, obtain the complete relevant patterns or sections, including the conditions and dependencies needed for the question, and retain their publication names and pattern IDs. Use an accessible README, contents entry or search result to locate the needed material; the locator does not replace it. If the necessary passage cannot be obtained, state the missing access and keep the dependent conclusion open. You can continue work whose basis is available.

Establish the available publication set once, and update it when files or access change. The full distribution includes FPF Core, the Engineering, Management, Foundational Thinking and Human Capability Engineering DPF Suites, further domain frameworks, and the Architectural References for the Library and its Suites; a downloaded subset or one attached document offers less. The public `Readme.md` and Suite `README.md` files identify the publications. Search the available set together when the question might need contributions from more than one practice. A missing search result means that this search has not found an answer in those sources, not that the ecosystem lacks the method.

In the complete distribution, `FPF-Spec.md` and the [FPF Library Architectural Reference](FPF-LIBRARY-REFERENCE.md) are at the repository root. The [DPF catalogue](DPFs/) lists the Suite subfolders and standalone DPF files under `DPFs/`. This directory groups domain publications; it is not another Suite. The Architectural References explain which disciplines form each Suite and which are used across its boundaries. Using a framework from another Suite does not add it to the receiving Suite.

For development or review, use the edition and candidate selected by the assignment. Distinguish a proposed contribution from published guidance when reporting what the framework already supplies.

## Resolve a portable reference

A portable reference keeps the complete PatternID or SectionRef and enough context to recover the intended publication set and document. Add a document qualifier only when that identity is not already clear from the complete address and the context that travels with it. In this distribution the publication set is **FPF Library**. Its [document catalogue (Library.Reference:11.1)](FPF-LIBRARY-REFERENCE.md#libraryreference111---document-identities-and-current-carriers) associates 39 declared DocIDs with their full titles and current files. Short navigation and usage publications can be named by their full titles without a DocID. A DocID identifies a whole document; it does not turn its embedded Architectural Reference into a separate framework or identify an edition.

For example, within FPF Library, HCD.12:4.1 locates a section of the Human Capability Development Principles Framework, and Library.Reference:9.1 locates the Library's explanation of connected development. Those complete addresses already identify their declared documents. Use FPF C.39:4.1 when a Core reference needs a document qualifier. These addresses have different structures; resolve each complete address under its declarations. Retain every suffix and every member or endpoint of a referenced list or range. Name a selected edition separately when its exact published content matters.

A whole-document reference can use its declared DocID or full title within the identified publication set. For an unnumbered heading, give its title and enough document context: Practical entries in HCD distinguishes that heading from the heading of the same name in Core.

First look for the declared document among the files available to you. Match its DocID and title, then search for the exact heading address and read the relevant section with its conditions. A GitHub hyperlink can help open a carrier, but its hostname and path are not required to identify the contribution. If local files are unavailable, search by the publication set, document title or DocID, and full local address through the web or an available search, fpf.tools or MCP interface. Use only the access that the present interface actually provides; this instruction does not assert a special API or that any service indexes the complete Library.

Check that the returned text belongs to the intended document and contains the requested target. Keep the complete local address with any extracted fragment and restore any publication-set, document or edition context that will no longer accompany it. A search hit, similarly named pattern or newer edition is not a substitute for an unresolved target or a requested exact edition. State that limit and continue only work whose needed basis is available.

## Distinguish a source from material to apply

A citation such as “this distinction follows X” tells you where a claim or explanation comes from. Use the material already given when it is sufficient; opening its source is not an automatic extra step. Inspect the source when its meaning, assumptions or evidence matter to a question about relying on it.

An instruction such as “use X to compare these arrangements” asks for a contribution to the present work. Follow its conditions and distinguish a required move from one suggested way. Reuse an adequate result or an already understood Method when it fits; otherwise obtain and use the supplying explanation, then bring the result back to the work that needs it. Reading a title or following a link is not that result.

The same destination can serve either purpose. Ordinary wording should make the difference clear; short `Source:` and `Apply:` labels can help in compact lists but are not required. A contents entry or plain catalogue locator is only navigation. If a substantive reference is ambiguous, use FPF E.11.PUA:4.1.1 to decide what to read or apply. When writing such a passage, use FPF E.8:4.2.2.2 to make its purpose clear without redundant labels. An extract retains any necessary purpose or condition that would otherwise be lost with its heading or introduction.


## Keep the receiving work in view

Start with the actual situation, the object being worked on, and the result the answer needs to support. Apply [FPF C.39:4.1](FPF-Spec.md#c39---find-and-develop-a-way-to-obtain-a-result) to establish what would make the contribution sufficient for the next receiving action or judgement. Keep that use in view when the task already names a pattern, a source, a correction or a check. The named operation can supply only part of the needed result.

Use an adequate known answer directly. If the available text leaves you inventing a consequential distinction or connection, follow that gap through C.39:4.2–4.5. This is where conceptual and methodological synthesis enters ordinary work: construct what is missing, retain what already works, and explain enough for the intended use. E.4.CM applies that construction to a maintained framework contribution. Do not turn every lookup into framework development; a task-local answer, a usable supplier or a sufficient partial result may finish the present work.

On a return from local work, decide what the recipient can now obtain or do using that result. A checked extraction establishes what the source supplies; an explained general way may still require construction. A reader's private invention can reveal that need without establishing that the publication already supplies it. Follow the source or dependency only as far as the receiving decision requires. State the supported useful answer and the condition that changes its use. When a proposed action or evidence demand has unclear value or feasibility, use [FPF C.11.DUA](FPF-Spec.md#c11dua---make-advice-and-evidence-demands-worth-their-burden) to compare what the demanded work can change with its burden and return warranted advice for the receiving decision. A binding requirement continues to govern until its authority or agreement changes it.

These moves belong to the work itself, not a separate report for each response. Reuse the established receiving use and sound results while their conditions hold. After an interruption or a changed assignment, recover that connection before choosing the next local move.

## Choose what to read

If a pattern is already named, find its body directly. Otherwise search the available publications together, using terms for the difficulty and needed result. Include English technical terms when the user's language differs from the sources. You can find an individual method or a connected application without first choosing a Suite, Reference or pattern file.

When sources or terminology are uncertain, [FPF F.1:4.4](FPF-Spec.md#f1---find-and-select-sources-for-a-current-question) explains how to construct and adapt a search from the available access, preserve the original question, inspect candidates and return consequential limits. Finding alone requires no SourceCutNote; use F.1's source-selection branch only when a justified basis over several sources is needed. A sufficient known source can be used directly.

Inspect a promising passage with its enclosing heading. A pattern body supplies its method; a Reference answer can explain how several contributions work together; a README or contents row helps locate that explanation. Open the substantive source and the conditions needed for the present use. When exploring the repertoire without a useful search phrase, start with Core Part headings or the corresponding Suite overview, then retrieve selected entries. Search a large Table of Contents as text and read the matching rows; do not load it in full merely to begin a lookup. Its technical terms, practical questions and dependencies can help reformulate the search.

To perform a selected method, read its description, applicability conditions, and the related patterns needed for that use. To use a particular technique, read its section together with the conditions it depends on. Apply it to the facts and constraints of the task. If a candidate method presupposes a result you still need to obtain, search for that earlier result or operation rather than silently treating it as given. For example, resolving a known conflict does not by itself explain how to notice a difficulty in ordinary work. A later method's scope limit is not evidence that the earlier contribution is absent from the framework.

Explain results and give feedback in the language of the project's work. Preserve the source distinctions that affect the answer. Cite the patterns and locations used. State assumptions, missing evidence, use limits, and the need for human judgement where they affect the decision. Let the current question determine the next step.

When a question needs several methods, use a relevant connected example or Practical-Use Card. Follow the intermediate results: what each method returns, which operation uses it, and what changed condition sends the work back. A mantra helps retain that connection. Read the supplying patterns and start at the contribution whose inputs are available. If one method's result leaves the larger work unresolved, search the same publications for that larger result together with the method's ID or useful terms. Continue through the connected account only where it supplies a contribution the work still needs. An adequate earlier result or a sufficient individual method can end the lookup.

Also recover the constituent–whole connections in the relevant Method and Work structures: what larger work is being performed through this action now, what constituent performances it needs, and which conditions must hold together. Use B.1.5.EW when this is unclear and B.1.5.RS for a proposed constituent replacement. A DPF can describe only some of those connections. Retain already available capabilities, expose missing intermediate coordination or support, and check joint demands on shared resources. When these facts change which alternative continuation is available, use A.22.CGUS:4.1 to distinguish available, blocked and unknown continuations from their actual conditions, and return that judgement to the present choice. Explain the connection in the language of the work. C.30.ASV:4.5a helps distinguish the relevant structures when that affects the decision. If a drawing uses vertical or horizontal direction, name the represented structure and relation as A.22:4.3a explains; a diagram is optional.

## Learn the contribution the work needs

Using a method to obtain a result and learning to perform it are different purposes. Decide which contribution you need to make yourself and which can be supplied by a source, tool, specialist or AI assistant. For example, interpreting a model's limits may be necessary even when another contributor constructs and computes it. An available answer can be enough for the current work; it does not establish that you can produce or adapt it in a different situation.

When learning is the purpose, use the [Human Capability Development DPF (HCD)](DPFs/Human%20Capability%20Engineering%20DPF%20Suite/HUMAN-CAPABILITY-DEVELOPMENT-PRINCIPLES-FRAMEWORK.md). HCD.1–.3 connect later work, current preparation and the choice of development or support. HCD.9 guides practice with feedback and correction; HCD.10 helps vary it for the missing operation. HCD.12 distinguishes evidence of applying an already learned method under a changed condition from evidence of learning a new method with a source. HCD.15 reopens development when the work or its support changes. Read only the contributions needed for your question; the order of publications is not a requirement to learn every method first.

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

Use `rg` (ripgrep), or the environment's equivalent search tool with regular expressions. Run these commands with the public distribution folder as the working directory, or prepend its actual path to the file arguments. In a source repository, limit the search to the selected public publications; campaign notes and historical drafts are not the public corpus.

Inspect the available Markdown files once to establish the search scope. This lists filenames; it does not search their contents:

```sh
rg --files --no-ignore -g '*.md' .
```

For the illustrative question “obtain a needed engineering result: build or buy”, search the text across that scope:

```sh
rg -n -i -C 2 --no-ignore -g '*.md' -- 'build or buy|obtain a needed engineering result|obtain climate control' .
```

This query can return a pattern, a contents row and a connected Reference case. Compare the question each passage answers, open its enclosing section and retain the useful result or return condition. If the output is too large, use the same query with `-l` instead of `-n -C 2` to list matching files, then inspect promising passages. Reformulate an unsuccessful query; a lexical match alone does not establish fit, and no match does not establish that the method is absent.

A browser or retrieval system can serve the same search when it covers the declared publications, including Reference answers. If it exposes only one file or titles, state that limit and extend access when the question requires it.

Locate the file and the start and end lines of the selected pattern:

```sh
rg -n --no-ignore -g '*.md' '^## SYSE\.24 |^### SYSE\.24:End[ \t]*\r?$' -- .
```

Read that pattern in full:

```sh
rg -U --no-heading --no-line-number --no-filename --color never '(?ms)^## SYSE\.24 [^\r\n]*\r?\n.*?^### SYSE\.24:End[ \t]*\r?$' -- "DPFs/Engineering DPF Suite/SYSTEMS-ENGINEERING-PRINCIPLES-FRAMEWORK.md"
```

Here `-U` enables multiline search; `(?m)` makes `^` and `$` match line starts and ends, and `(?s)` lets a dot match a newline. `(?ms)` combines them. `.*?` matches through to the nearest specified `:End` heading; `\r?\n` accepts Windows and Unix line endings. Substitute another ID and file as needed; escape literal dots in IDs as `\.`.

For other searches, `-F` treats the query as literal text, `-i` ignores case, and `-C 2` includes neighbouring lines. `--no-ignore` searches files even in a Git-ignored folder; `-g '*.md'` selects Markdown files.

If the tool truncates a long result, read the selected text in successive line ranges with the available file reader. Folder search already covers separate publications; no combined file is needed.