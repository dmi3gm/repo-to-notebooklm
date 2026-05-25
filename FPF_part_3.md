g; G.7 does not define thresholds)*
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

**System (Γ_sys):** *Cross‑standard safety assurance comparison (bridge‑first).*
A team must compare a safety assurance claim across two regulatory Traditions (e.g., a “functional safety case” tradition and a “ML system testing” tradition) for the *same physical system scope*. `G.7` forces explicit SenseCell‑level bridges (what exactly is the “hazard”, what is the “evidence carrier”, what is the “pass criterion”), records losses, pins planes, and provides sentinels so that changes in the safety evidence protocol editions trigger path‑local RSCR rather than re‑authoring the entire safety case.

**Episteme (Γ_epist):** *Benchmark protocol pluralism (post‑2015 evaluation practice).*
A research group wants to compare “state‑of‑the‑art” across multiple evaluation Traditions (IID performance, shift robustness, preference‑based evaluation). `G.7` turns “these are comparable” into explicit BridgeCards with declared row scope, pins the evaluation protocol editions, and emits sentinels so that when a benchmark protocol or policy pin changes, downstream selector decisions can be re‑audited by re‑citing the same PathSlice‑scoped evidence.

### G.7:6 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
Scope: Universal for the bridge calibration kit; any method‑family or discipline‑specific calibration technique is modularized as `GPatternExtension` and cited to its governing patterns.

### G.7:7 - Conformance Checklist (normative) — **CC‑G7**

| ConformanceId             | Requirement                                                                                                                                                                                                                                                                               | Purpose                                                                        |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **CC‑G7‑CoreRef**         | `G.7` is conformant only if it satisfies the effective `G.Core` obligations declared by the `GCoreLinkageManifest` in **§4.1** (after nil‑elision and expansion of profile/set/pinset ids), including any explicit deltas listed there. | Make universal invariants one governing definition and enforce citation‑based reuse.       |
| **CC‑G7‑BCT‑1**           | For any active `TradPairId` with cross‑Tradition reuse, a `BridgeCalibrationTable (BCT)` **MUST** exist, declare a `FreshnessWindowRef`, and provide `RowEntry` records that cite, at minimum: `RowEntryId`, `ComparableConstructId`, `RowScopeId`, `BridgeCardId[]`, `RowCL_min`, `PlanePins {ReferencePlane(src), ReferencePlane(tgt)}`, `PolicyPins {Φ(CL)}` (and `Ψ(CL^k)?`, `Φ_plane?` when applicable), plus `{RegressionSetId, SentinelSetId}`. | Ensure the kit exists as an auditable object rather than a prose matrix.       |
| **CC‑G7‑BridgeCard‑1**    | Any bridge published by G.7 **MUST** be consumable as an **F.9** `BridgeCard` and **MUST** be SenseCell‑anchored (directly or via explicit SenseCell anchor refs).                                                                                                                        | Prevent “Context‑only” or ambiguous bridges.                                   |
| **CC‑G7‑UTS‑1**           | G.7 outputs **MUST** mint/publish UTS‑citable ids (NameCards/twin labels as applicable) for (a) each BridgeCard (or its NameCard) and (b) each GateCrossing/crossing row that makes bridge use checkable; and **MUST** expose the resulting `UTSRowId[]` in the BCT/Ledger/crossing bundles. *(UTS discipline is delegated to `CC‑GCORE‑UTS‑1`.)* | Make bridge calibration externally citable and checkable.                      |
| **CC‑G7‑RowScope‑1**      | Every BCT row **MUST** declare its `RowScopeId` (what notion of “sameness” is claimed), and any loss notes **MUST** be recorded as citable artefacts (refs/ids), not only narrative text.                                                                                                 | Keep reuse honest and locally bounded.                                         |
| **CC‑G7‑CLRegime‑1**      | Every BCT row **MUST** record `RowCL_min` (and `RowCL_k_min?`, `RowCL_plane_min?` where applicable) and apply the admissibility regime from §4.2.1: `≥2` admissible; `=1` only with cited `WaiverRef[]`; `=0` forbidden for reuse. The honesty rule must be satisfied: ≥1 counterexample for `≤2`, and an explicit stated‑absence disclosure for `=3` when no counterexample is cited. | Make CL/waiver/plane regimes explicit and auditable at kit level.              |
| **CC‑G7‑SCRLinkage‑1**    | Whenever bridge calibration is cited in SCR/Evidence surfaces, the citation **MUST** include `{BridgeCardId[]}` (or `UTSRowId[]` for the bridge artefacts), an explicit row locator (`RowEntryId` or equivalent), `{BCT.id, RegressionSetId}`, and the active policy id pins `{Φ(CL), Ψ(CL^k)?, Φ_plane?}` (ids only; representation governed elsewhere). | Prevent “pins exist but are not visible/auditable” failure mode.               |
| **CC‑G7‑SoSLOG‑Pins‑1**   | When `G.7:Ext.SoSLogClauses` is in use, G.7 outputs **MUST** expose the cited SoS‑LOG rule ids and the relevant `PathId/PathSliceId` evidence citations; any change in those pins **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                               | Keep cross‑Tradition reuse explainable without embedding C.23 semantics.        |
| **CC‑G7‑Acceptance‑1**    | When `G.7:Ext.AcceptanceHooks` is in use, G.7 outputs **MUST** expose the Acceptance clause ids/policy ids used as gates; thresholds/unknown handling remain governed by Acceptance; any change **MUST** be RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                           | Keep thresholds and unknowns out of bridges while preserving auditability.     |
| **CC‑G7‑RowBottleneck‑1** | If a comparable construct row aggregates multiple bridge cells, row summaries (e.g., `RowCL_min`) **MUST** follow bottleneck discipline (F.7) and cite a counterexample whenever a cell carries a loss note.                                                                              | Forbid “CL averaging” and enforce loss‑aware summaries.                        |
| **CC‑G7‑PolicyPins‑1**    | G.7 outputs **MUST** publish the *policy id pins* required to audit penalty routing and plane effects (ids only), as required by `CC‑GCORE‑LINK‑1/2` and `CC‑GCORE‑PEN‑1`. G.7 MUST NOT duplicate policy tables or redefine penalty semantics.                                           | Keep penalty routing auditable while preserving single‑governing-pattern policy semantics. |
| **CC‑G7‑GateCrossing‑1**  | Any published crossing rows that rely on bridges **MUST** be checkable via GateCrossing/CrossingBundle harnesses (E.18/A.21): required pins are present; lexical constraints and lane purity checks are runnable.                                                                        | Make crossings checkable, not narrative.                                       |
| **CC‑G7‑Sentinels‑1**     | G.7 **MUST** register `BridgeSentinel` entries for bridges used by live scopes and **MUST** emit typed RSCR triggers (canonical `RSCRTriggerKindId`; see `CC‑GCORE‑TRIG‑1…TRIG‑4`) on calibration‑relevant edits, scoped to the watched `PathSliceId[]` or `PatternScopeId[]`, with the minimum payload pins from §4.1. | Enable targeted refresh rather than pack‑wide reruns.                          |
| **CC‑G7‑QD‑Pins‑1**       | When `G.7:Ext.QDParityPins` is in use, G.7 outputs **MUST** include `{DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef}` and treat any change to those pins as RSCR‑relevant per `CC‑GCORE‑TRIG‑1…TRIG‑4`.                                                          | Prevent silent QD telemetry drift.                                             |
| **CC‑G7‑DHC‑Units‑1**     | When AlignmentDensity (or related DHC accounts) are reported, G.7 outputs **MUST** (a) restrict the counted bridge set to rows with `RowCL_min ≥ 2` (treat `CL=3` as “free substitution”, `CL=2` as “guarded” for reporting), (b) include declared units, and (c) cite the relevant DHC method semantics (C.21). G.7 MUST NOT invent arithmetic over ordinal/illegal surfaces. | Keep dashboards and discipline‑health metrics lawful and interpretable.        |

### G.7:8 - Common Anti-Patterns and How to Avoid Them

* **Bridge‑by‑prose (“they have the same sense”).**
  **Avoid:** publish BCT rows + BridgeCards + UTS rows; require SenseCell anchoring and row scopes.
* **SenseFamily jump (scope‑bridge used as kind‑bridge).**
  **Avoid:** keep channel/sense‑family constraints governed by **F.9** visible; use `RowScopeId` to state which channel is claimed, and require `CL^k` + `Ψ(CL^k)` pins when a kind‑channel bridge is invoked (do not “upgrade” a scope‑channel bridge into kind substitution).
* **Plane blindness (“concept = world”).**
  **Avoid:** record plane pins and policy id pins; keep plane effects auditable and separable from CL/CL^k semantics.
* **CL smoothing / averaging.**
  **Avoid:** enforce row bottleneck summaries and counterexample citations for loss‑noted cells.
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
* **Why BCT + RegressionSet + SentinelSet?** Because calibration without regression tests drifts silently, and regression without sentinels is operationally unusable (refresh becomes global).
* **Why row scopes?** Because “comparable” is not one thing; scope must be explicit to avoid accidental substitution.

### G.7:11 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Edition‑aware evaluation and dataset shift practice.** Post‑2018 evaluation culture (robustness and shift benchmarks, protocol pinning, reproducibility checklists) motivates treating protocol versions and “what changed” as first‑class pins rather than prose.
* **Preference‑based optimisation families.** Modern preference‑learning lines (late‑2010s → 2020s) show how neighbouring objectives can share intent but diverge in assumptions—an archetypal case for row scope + loss notes.
* **Quality‑Diversity and differentiable QD.** MAP‑Elites successors (CVT variants, CMA‑ME line, differentiable QD ecosystems) emphasise archive/descriptor/distance artefacts whose editions must be pinned for comparability.
* **Open‑ended evolution and transfer‑rule portfolios.** POET‑class work motivates explicit transfer rule editions and environment validity regions as pins when bridges are used for cross‑tradition reporting.

### G.7:12 - Relations

**Builds on:** `G.Core`, `G.2`, `F.3`, `F.7`, `F.9`, `B.3`, `E.10`, `E.18`, `A.21`, `G.6`, `C.21`.
**Optionally uses via Extensions:** **G.4** (Acceptance hooks), **C.23** (SoS‑LOG clauses), **C.18 and C.19** (QD/OEE pins).
**Used by / prerequisite for:** **G.5** (cross‑Tradition eligibility/selection), **G.11** (refresh orchestration), **G.9** (parity across Traditions where bridges are required), **G.10** (shipping surfaces that must cite bridge calibration ids), **G.12** (DHC dashboards when bridge counts/units are surfaced).
**Publishes to:** **UTS** (bridge and crossing rows; twin labels as applicable) and emits RSCR‑ready telemetry/trigger payloads for **G.11**.
**Constrains:** Any downstream consumer that claims cross‑Context/Tradition reuse must use the calibrated bridge artefacts/pins surfaced by this kit (governed by G.Core crossing invariants apply).

### G.7:End

## G.8 - SoS‑LOG Bundles & Maturity Ladders

**Tag.** Architectural pattern (packaging kit).
**Stage.** Design‑time packaging (authoring & publication) with a run‑time consumption facade for `G.5` (selector/registry).
**Primary hooks:** `G.Core` (Part‑G invariants), `C.23` (SoS‑LOG semantics), `C.22` (TaskSignature), `G.4` (Acceptance & EvidenceProfiles), `G.6` (EvidenceGraph & `PathId/PathSliceId`), `G.5` (registry/selector), `G.11` (refresh orchestration), `G.10` (shipping boundary), `F.9` (BridgeCard & CL), `F.17` (UTS), `E.17` (publication faces), `G.7` (bridge calibration & Φ/Ψ/Φ_plane), `F.8` (Policy pins: `PolicySpecRef`/`MintDecisionRef` resolvability), `A.10` (anchors), `E.10` (LEX twin registers), `E.5.2` (notational independence), `E.18/A.21` (GateCrossing visibility and gate checks).

**Non‑duplication note (Phase‑2 universalization).** This pattern introduces **kit-governed packaging surfaces** for SoS‑LOG bundles and maturity ladders. All **Part‑G‑wide invariants** (no shadow specs, Bridge‑only crossings + visibility, tri‑state guard domain, penalties→`R_eff`‑only, set‑return semantics, P2W split, typed RSCR triggers + alias docking, defaults with one governing definition, shipping boundary) are **pinned through `G.Core`** and are not restated here.

**Modularity note (policy‑id pins are reference‑only).** This kit may pin/cite policy ids (e.g., `Φ/Ψ/Φ_plane` policies, `FailureBehaviorPolicyId`, illumination‑promotion policy ids, and E/E‑LOG policy ids) **as references only**. Conformance relies on the policy‑pin resolvability discipline of `F.8:8.1` (i.e., policy ids are not “inlined”; and when newly minted, they are backed by resolvable `PolicySpecRef` + `MintDecisionRef`). `G.8` does not define policy semantics and MUST NOT silently mint policy ids.

### G.8:1 - Problem frame

Method families compete within a `CG‑Frame`, but dispatch is only lawful if (i) admissibility decisions remain **tri‑state** and auditable, (ii) evidence and crossings are **explicitly citable** (by ids, not prose), and (iii) selection preserves **set-return semantics** under partial orders. In practice, SoS‑LOG rules (`C.23`) and “maturity stories” are often distributed across prose, dashboards, and ad‑hoc checklists, with thresholds embedded where they do not belong and with missing pins for evidence paths, crossings, and editions.

This pattern provides the missing packaging kit: a **selector‑facing, UTS‑citable bundle** that binds **(a)** rule ids (semantics governed by `C.23`), **(b)** an ordinal/poset maturity ladder (published as a citable card), and **(c)** explicit wiring to Acceptance (`G.4`), EvidenceGraph (`G.6`), selection/registry (`G.5`), and refresh (`G.11`)—without creating any shadow governing spec refs.

### G.8:2 - Problem

1. **Selector needs a stable input artefact.** `G.5` cannot consume “maturity narratives” and scattered SoS‑LOG snippets without re‑authoring semantics or inventing implicit defaults.
2. **Thresholds leak into LOG.** Numeric gates are often embedded directly into rule text or ladder rungs, blurring the boundary between LOG decisions (`C.23`) and Acceptance thresholds (`G.4`).
3. **Auditability is brittle.** Decisions (`pass/degrade/abstain`) lack stable, citable links to evidence paths (`G.6`) and crossing pins (Bridge/CL/Φ policy ids), so later re‑checks and RSCR become ad‑hoc.
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

**Separation rule (Phase‑2).** Method‑/generator‑specific pins are **normatively specified** only inside `Extensions` as `GPatternExtension` modules (see `G.8:5.*`). The bundle/ledger schema may mention such fields only as **extension‑gated optionals**, with the authoritative pin/edition/policy requirements stated in the corresponding extension block. The core linkage manifest lists only base‑kit pins and Part‑G‑wide linkage.

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
  MethodFamilyId,
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
Crossing payload pins (Bridge/CL/Φ/Ψ/Φ_plane) are introduced **only when reuse is asserted**, via `G.8:Ext.BridgeReuseWiring`.
Method-/generator‑specific payload pins are listed only inside the relevant `GPatternExtension` blocks in `G.8:5`.)*

*(Conditionality note for defaults.)* Include `DefaultId.GammaFoldForR_eff` in `DefaultsConsumed` **only if** the bundle/ledger exports aggregated `R_eff` summaries (otherwise Nil‑elide it).

#### G.8:4.2 - Kit: objects and naming discipline (LEX heads; twin‑register safe)

**Objects / surfaces (pattern-governed).**

* **`SoS‑LOG.Rule`**
  A rule id that denotes an executable tri‑state decision schema `{pass | degrade(mode) | abstain}` for `(TaskSignature, MethodFamily)`. *(“pass” may be described as “admit” in prose, but the normative tri‑state vocabulary is `G.Core`’s `{pass|degrade|abstain}`.)*
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
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  CNSpecRef.edition,
  CGSpecRef.edition,

  MethodFamilyId,
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
  GeneratorFamilyId? ,
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
* If cross-context or cross-plane reuse is asserted, crossing pins are made explicit (Bridge/CL/Φ policy ids), and evidence paths are citable when available.

**Binding obligations B1–B5 (packaging‑only; wiring‑only; semantics delegated):**

* **B1 — Evidence wiring.** At packaging time the bundle SHOULD provide resolvable evidence refs (typically `A10EvidenceGraphRef?[]` and/or `EvidenceGraphId?`). At run time, admissibility outcomes SHOULD cite `PathId/PathSliceId` when available (`G.6`), so rung transitions and `degrade/abstain` traces are audit‑stable.
* **B2 — CL/plane routing pins.** When reuse across Context or plane is asserted, the bundle/ledger MUST pin the relevant Bridge/CL/Φ/Ψ/Φ_plane policy ids (reference‑only; resolvable per `F.8:8.1`) and MUST respect the core penalty routing (penalties affect `R_eff` only; `F/G` invariance via `G.Core`).
* **B3 — `PortfolioMode`/QD fields.** If the bundle/ledger exposes `PortfolioMode`/QD fields (e.g., `PortfolioMode=Archive`), it MUST pin the descriptor/distance/insertion/emitter artefacts (editions/policies as applicable). Illumination remains **report‑only** unless explicitly promoted by a `G.4` governing-pattern policy id that is pinned and recorded in the run‑time trace.
* **B4 — Open‑ended fields.** If the bundle binds an open‑ended generator family, it MUST pin `GeneratorFamilyId` and `TransferRulesRef.edition` (and any validity region/coupler policy ids when used). Unknown transfer validity MUST be recorded as `degrade`/branching, not as an ad‑hoc fourth status.
* **B5 — Telemetry hooks.** On any material telemetry event (illumination increase, archive insertion, probe accounting update, open‑ended coverage/regret proxy update), the emitted telemetry pins SHOULD include the controlling policy ids plus the relevant edition pins (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `TransferRulesRef.edition`) and, when available, `PathSliceId` to keep RSCR planning auditable.

#### G.8:4.4 - `AdmissibilityLedger@Context` (run‑time view; selector‑facing)

A conforming ledger is a UTS‑published view (or a view‑projection of a Work/Audit artefact) with rows of the form:

`⟨ MethodFamilyId, SoSLogRuleId, GuardDecision ∈ {pass|degrade|abstain}, DegradeMode?/SoSLogBranchId[]?, MaturityRungId?, AcceptanceClauseId[]?, EvidencePathRefs?, CrossingPins?, PortfolioMode?, DominanceRegime?, Edition ⟩`

Where `EvidencePathRefs` are typically `PathId[]/PathSliceId[]` when `G.6` is in use (or resolvable), and “CrossingPins” are the explicit Bridge/CL/Φ policy pins when reuse is asserted.

#### G.8:4.5 - Maturity ladder as a citable poset (published card)

`MethodFamily.MaturityCardDescription@Context` is published with:

* closed rungs (UTS‑registered identifiers),
* `Scale kind = ordinal` and a declared `ReferencePlane`,
* (optional) explicit poset edges / precedence constraints,
* rung transition justifications that cite evidence paths (typically `G.6` paths).

This card is a **description** suitable for dispatch/audit and refresh; it is not a competing governing spec ref.

#### G.8:4.6 - Interfaces (minimal I/O standard; conceptual)

| Interface                               | Consumes                                                                                   | Produces                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **G.8‑1 `Publish_LOGBundle`**           | `MethodFamilyId`, `SoSLogRuleId[]` (C.23), pins to Acceptance/Evidence/Crossings (as applicable) | `SoS‑LOGBundle@Context` (UTS row)                                                     |
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
**Uses:** `{G.7, F.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `BridgeId/BridgeCardId`
* `CL/CL^k/CL^plane`
* `Φ/Ψ/Φ_plane policy-ids`
* `BridgeCalibrationTableId?`, `RegressionSetId?` *(if cited as calibration evidence)*

**RSCRTriggerSetIds:** `{GCoreTriggerSetId.BridgeCalibrationKit}` *(only if the bundle/ledger explicitly binds calibration records by id)*
**Notes (wiring‑only):**
* Present only when `SoS‑LOGBundle@Context` asserts cross-Context or cross-plane reuse. No additional crossing semantics are defined here.

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

* `GeneratorFamilyId`
* `TransferRulesRef.edition`
* `EnvironmentValidityRegionId?`
* `CouplerPolicyId?`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta}`
**Notes (wiring‑only):**
* Open‑ended coverage/regret (or similar) remains telemetry unless explicitly promoted by a governing-pattern policy.

### G.8:6 - Archetypal Grounding (System / Episteme)

**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `RuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.
**Show‑A — Tri‑state admissibility with set‑valued selection (multi‑criteria).**
A CG‑Frame carries multiple offline/robust decision families (e.g., conservative offline RL and transformer‑based policy models post‑2020). The bundle publishes `SoSLogRuleId[]` (SoS‑LOG semantics in `C.23`), cites `AcceptanceClauseId[]` for any floors (governed by `G.4`), and emits an `AdmissibilityLedger` whose rows cite `PathSliceId` (when available) for each `pass/degrade/abstain`. `G.5` consumes the ledger and returns a **selected set** under the declared partial order—no scalar “winner”.

**Show‑B — QD archive dispatch with edition‑pinned descriptors (post‑2015 QD families).**
A method family uses a modern QD line (e.g., CMA‑ES‑driven archives, differentiable QD variants, and large‑scale JAX‑style QD toolchains). The bundle pins `DescriptorMapRef.edition` and `DistanceDefRef.edition`, plus insertion/emitter policies. Illumination metrics are logged as telemetry; any promotion into dominance is only via explicit CAL policy pins (recorded in the admissibility trace).

**Show‑C — Open‑ended environment–method co‑evolution (post‑2018 open‑ended families).**
A generator family operates in an open‑ended setting (e.g., POET‑style and PAIRED‑style regimes). The bundle carries `TransferRulesRef.edition` and validity region pins; unknown transfer validity triggers a `degrade` branch rather than an ad‑hoc fourth status. Telemetry (coverage/regret proxies) is emitted for refresh planning, not silently turned into dominance.

### G.8:7 - Bias‑Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.
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
  When a LOG bundle is used to drive or justify a produced selected-set outcome, the producing Work/Audit artefact SHOULD cite the controlling mechanism ids (e.g., parity/shipping/refresh artefact ids) and relevant policy pins; no “black box” provenance.

* **CC‑G8‑11 (SoTA‑of‑description trace).**
  If authoring methods (e.g., discovery, clustering, summarisation) materially shaped rule text or rung definitions, the bundle/card SHOULD cite their method description refs (edition‑pinned) to support cross‑stance traceability.

### G.8:9 - Common Anti‑Patterns and How to Avoid Them

* **Anti‑pattern:** Embedding thresholds inside SoS‑LOG rules or ladder rungs.
  **Avoid:** thresholds live in `G.4` Acceptance; bundle only cites clause ids.

* **Anti‑pattern:** Treating illumination/QD telemetry as a hidden scalar score that changes dominance.
  **Avoid:** keep telemetry report‑only unless explicitly promoted by a governing-pattern policy pin.

* **Anti‑pattern:** Publishing a bundle that “implies” cross‑context reuse without Bridge/CL/Φ pins.
  **Avoid:** if reuse is asserted, publish the crossing pins; otherwise downstream must abstain from reuse.

* **Anti‑pattern:** Re‑defining `PortfolioMode`/`DominanceRegime` defaults in the bundle text.
  **Avoid:** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex`.

* **Anti‑pattern:** Recording RSCR “reasons” as prose labels only.
  **Avoid:** emit canonical `RSCRTriggerKindId` values per `G.Core`.

### G.8:10 - Consequences

* **Positive:** `G.5` receives a stable, citable, selector‑facing artefact without importing rule semantics or threshold logic.
* **Positive:** Audit and refresh become tractable: pins, crossings, evidence paths, and trigger kinds are explicit.
* **Positive:** Maturity remains non‑scalar, reducing illegitimate aggregation and “readiness theater”.
* **Negative:** Requires stricter authoring discipline (UTS publication, pin completeness, explicit wiring).
* **Negative:** If evidence paths are not maintained (`G.6` absent), auditability degrades and downstream must rely on references with lower evidence-support class, or abstain.

### G.8:11 - Rationale

`C.23` governs **rule semantics**, `G.4` governs **thresholding/acceptance**, `G.6` governs **path‑addressable provenance**, and `G.5` governs **selection/registry semantics**. Without a dedicated packaging kit, projects either (i) duplicate semantics inside ad‑hoc “decision bundles” (creating shadow specs), or (ii) leave dispatch un‑auditable. `G.8` keeps these boundaries strict while providing a single, consumable surface.

### G.8:12 - SoTA‑Echoing (informative; post‑2015 practice alignment)

This pattern’s separation of **decision rules**, **acceptance thresholds**, **provenance paths**, and **set‑valued outputs** echoes post‑2015 practice in:

* **Set‑valued / set-returning selection** (multi‑objective and uncertainty‑aware regimes; avoiding forced scalar winners).
* **Quality‑Diversity and archive‑based evaluation** (post‑2015 QD variants emphasize edition‑pinned descriptors/distances and telemetry‑driven refresh).
* **Open‑endedness / curriculum generation** (post‑2018 lines emphasize explicit transfer rules, safe degrade branches, and telemetry‑driven orchestration rather than hidden gates).
* **Reproducibility‑aware publishing** (explicit identifiers, pinned editions/policies, citable traces rather than prose‑only decision rationales).

*(Examples are illustrative; they do not introduce new Part‑G‑wide norms.)*

### G.8:13 - Relations

**Builds on:** `G.Core`, `C.23`, `G.4`, `G.6`, `G.5`, `C.22`
**Uses:** `A.10` (anchors), `F.8` (policy-id resolvability), `F.9`/`F.17`/`E.17` + `G.7` (when cross-Context or cross-plane reuse is asserted), `G.11` (refresh planning/trigger consumption), `G.10` (shipping boundary; if bundled artefacts are shipped), `E.10` (LEX twin registers), `E.5.2` (notation independence), `E.18/A.21` (GateCrossing visibility and gate checks); optional `C.18` (QD) / `C.19` (E/E‑LOG) when those surfaces are declared.
**Publishes to:** `UTS` (bundle/ledger/card), `G.5` (selector/registry consumption), `G.11` (refresh via typed triggers and pinned telemetry)
**Constrains:** any SoS‑LOG packaging that claims FPF conformance for selector‑facing dispatch across method families.

### G.8:14 - Author’s quick checklist (informative)

* [ ] `RuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] `SoSLogRuleId[]` are ids only; rule semantics are governed by `C.23` (no re-definition in this bundle).
* [ ] Any numeric gates/thresholds are `G.4` Acceptance artefacts cited by id (no thresholds embedded in LOG or rungs).
* [ ] Evidence is citable: at run time use `PathId/PathSliceId` when available; at packaging time provide resolvable `A10EvidenceGraphRef?[]` / `EvidenceGraphId?`.
* [ ] Any cross-Context or cross-plane reuse is explicit: `BridgeId/BridgeCardId`, `CL/CL^k/CL^plane`, and `Φ/Ψ/Φ_plane` policy ids are pinned (policy ids resolvable per `F.8:8.1`).
* [ ] `PortfolioMode` and dominance defaults are not restated: cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` (governing definitions live outside `G.8`, typically `G.5`).
* [ ] QD pins are edition/policy pinned (`DescriptorMapRef.edition`, `DistanceDefRef.edition`, insertion/emitter policies); `CharacteristicSpaceRef.edition` is pinned iff cell boundaries/de‑dup/parity depend on it; **Spaces ≠ Maps**.
* [ ] If open‑ended surfaces are declared, pin `GeneratorFamilyId`, `TransferRulesRef.edition`, and any validity/coupler policy ids; unknown transfer validity is recorded as `degrade`/branching (no “fourth status”).
* [ ] `MaturityRungs` is a closed, UTS‑registered set; the maturity ladder is ordinal/poset with a declared `ReferencePlane`; rung transitions cite evidence.
* [ ] RSCR triggers are emitted as canonical `RSCRTriggerKindId` values (no prose-only “reasons”).
* [ ] Notation independence (`E.5.2`) and twin‑register discipline (`E.10`) are respected for all published heads/ids.
* [ ] If authoring tools materially shaped rule/rung content, cite `AuthoringMethodDescriptionRefs?[]` (edition‑pinned) for cross‑stance traceability.

### G.8:End

## G.9 — Parity / Benchmark Harness

> **Status:** Stable

### G.9:0 — Use this when

- rival method families, method sets, or adaptation paths must be compared under one declared baseline set and freshness window
- you need parity to publish one reproducible report rather than one opaque benchmark score
- downstream selection must recover comparator, normalization, bridge, and evidence pins without relying on one hidden scoring sheet

### G.9:0.1 — What goes wrong if missed

- benchmark numbers mix different windows, baselines, or comparator editions and still pretend to be comparable
- cross-context reuse or normalization mapping stays hidden until a disagreement appears downstream
- parity flattens a partial order into one scalar winner and silently changes what the comparison means

### G.9:0.2 — What this buys

- one `ParityPlan@Context` that fixes baseline, freshness, comparator, and bridge discipline up front
- one `ParityReport@Context` that echoes the active pins, outcomes, and evidence trace by value
- one harness that downstream selection can consume without inventing a `G.9`-local CSLC gate or a shadow governance card

Illumination, coverage, and regret remain telemetry by default. If they are promoted into dominance, that promotion must be one explicit policy-bound choice rather than one hidden scoring convenience.

### G.9:1 — Intent

Provide a **notation‑independent** harness that:

* plans parity runs with explicit scope (`describedEntity`, `ReferencePlane`, window), explicit governance, CSLC comparability and admissibility references, and comparator references (`CNSpecRef`, `CGSpecRef`, `ComparatorSpecRef`) and explicit reproducibility pins (editions + policy‑ids);
* executes parity in a way that is consumable by **G.5** (selected-set outcomes, DRR/SCR evidence trace);
* publishes **ParityReport@Context** suitable for downstream consumption, shipping, and refresh/RSCR wiring.

### G.9:2 — Problem frame

Parity claims become non‑reproducible or non‑comparable when any of the following are implicit:

* evidence window / freshness regime,
* comparator semantics (including any normalization / comparability mapping),
* method‑family “measurement” edition pins (incl. DHC method/spec),
* cross‑Context reuse (Bridge refs, crossing pins, and CL penalty placement),
* dominance and `PortfolioMode` interpretation rules,
* gate outcomes (why a run abstained or degraded).

G.9’s role is to make these recoverable as **pinned and publishable** as a *method of obtaining outputs* (MOO) without introducing new governing spec refs.

### G.9:3 — Forces

* **Pluralism vs comparability.** Multiple Traditions must be comparable *without semantic collapse*.
* **Partial orders.** Many targets are only partially ordered; parity reporting must preserve CSLC-admissible outcome shape (often selected sets or archives rather than a single scalar).
* **Edition sensitivity.** Parity must be robust to silent drift in measurement/comparator definitions. When DHC/QD/OEE modes are used, the required definition pins are introduced only via the corresponding `Extensions` blocks (nil‑elision when unused).
* **Telemetry vs objectives.** IlluminationSummary and coverage/regret are telemetry: **report‑only by default**; dominance changes require explicit CAL policy ids (recorded in audit pins).
* **GateCrossing visibility.** Any crossings/gates used by parity must be visible and auditable via CrossingBundle + GateCrossing checks; failures block parity publication/consumption.
* **Cross‑Context reuse.** Any reuse across contexts or reference planes must carry explicit crossing pins, audit support, and R-channel penalty placement.
* **Refreshability.** Parity must emit RSCR‑relevant causes as canonical ids, with enough pins to re‑run.

### G.9:4 — Solution
#### G.9:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant** and therefore binds to **G.Core** by declaration (not by restating invariants here).

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
  *(Pattern‑local deltas; cross‑tradition / bridge‑calibration causes are wired via `G.9:Ext.CrossTraditionParity` and MUST NOT over‑trigger baseline (within‑context) parity runs.)*

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
  `FreshnessWindows`,
  `BaselineSet`, `BaselineBindingRef`,
  `ParityPinSet`,
  `PlanItemRefs[]?`,
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

**(1) `ParityPlan@Context`** *(WorkPlanning record)*
A plan that fixes *what is being compared* and *under what pinned conditions*.

Minimal fields (conceptual; ids/pins only):

`ParityPlan@Context := ⟨
  ParityPlanId(UTS),
  CGFrameId?,                              // or CG-FrameContext id/scope anchor cited by the referenced frame records
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // when “normalize, then compare” is required (ids only; semantics come from CN‑Spec / UNM)
  EpsilonDominance?,                       // optional ε-front thinning (ε≥0; id/param; pinned when used)
  PortfolioMode?, DominanceRegime?,         // may be explicit or inherited via DefaultGoverningDefinition (semantics follow G.5)
  ParityContextId,
  BaselineSet,                            // method-family / generator-family baseline scope (ids; notation-independent)
  BaselineBindingRef,                      // evidence-backed baseline-set reference that says what counts as baseline
  FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, // edition-pinned refs
  SCPRef.edition?,                         // optional (when a specific SCP profile must be pinned/cited)
  MinimalEvidenceRef.edition?,             // optional (when CG-Spec exposes minima profiles by ref)
  Budgeting?,
  ParityPinSet,
  PlanItemRefs[]?                          // references to A.15.3 SlotFillingsPlanItem (planned baseline), when parity depends on planned slot fillings
⟩`

**(2) `ParityPinSet`** *(pin set)*
A declared set of pins required for reproducibility and audit (editions + policy‑ids + UTS/Path pins).
The concrete contents are *pattern-local* (G.9 declares the pin set), but must satisfy the *core pin discipline* via `G.Core`.

**(3) `ParityReport@Context`** *(UTS publication record; work-result or audit-facing publication record only when the neighboring source exists)*
A UTS-publishable parity publication record produced by running a `ParityPlan@Context`. By itself it is not a dated `U.Work` occurrence, audit performance, evidence path, assurance result, or gate decision; those claims require `A.15`/`A.15.1`, `A.10`/`G.6`, `B.3`, or `A.21` respectively.

`ParityReport@Context := ⟨
  ParityReportId(UTS),
  ParityPlanId,
  BaselineSet, FreshnessWindows,
  CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition,
  SCPRef.edition?, MinimalEvidenceRef.edition?,             // echoed iff used/pinned in the plan
  UNM_id?, NormalizationMethodId[]?, NormalizationMethodInstanceId[]?, // echoed iff used in the plan
  OutcomeRefs,                              // selected-set / archive outcomes (as refs to selector outputs)
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

**Naming discipline.**

* Heads reuse existing U‑types and LEX discipline; no new “strategy” primitive is minted here.
* Tech/Plain twins follow E.10 rules (no drift‑inducing synonyms in Tech).

#### G.9:4.2 — Parity planning (design‑time / WorkPlanning)

Planning is the act of making the parity run *reproducible by construction*:

1. **Fix the baseline set.** Choose the `BaselineSet` (MethodFamilies, and optionally GeneratorFamilies) to compare; where parity context matters, cite `SoS‑LOGBundleId?` and source-maturity ids by reference (acceptance-gate thresholds remain in `G.4` Acceptance).
2. **Bind scope.** Fix `describedEntity := ⟨GroundingHolon, ReferencePlane⟩` and record it in the plan (no silent widening/narrowing).
3. **Define baseline-set reference.** Declare what counts as “baseline set” and how it is cited (e.g., `BaselineBindingRef`, the evidence-backed baseline-set reference, pointing to an EvidenceGraph path slice or an upstream shipped package or publication-record id).
4. **Equalise window (and budget, if pinned).** Declare a single `FreshnessWindows` and apply it across all baselines; if `Budgeting` is used/pinned, it MUST be shared/pinned across baselines as well.

When specialization is part of the parity claim, the same plan should also hold constant the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and freshness window; if transfer, retention, downstream exploitation efficiency, downside field, or corridor entry are part of the claim, those pins should be explicit as well, including the baseline relative to which corridor entry is being claimed.

5. **Pin governance, CSLC comparability and admissibility references, and comparator references.** `CNSpecRef`, `CGSpecRef`, and `ComparatorSpecRef` are referenced with explicit edition pins.
6. **Pin measurement/comparator definitions (conditional).** Where parity depends on mode‑specific definition records (e.g., DHC/QD/OEE), pin the relevant definition ids/editions/policies. The minimum required pins are declared by the applicable `Extensions` blocks (e.g., `G.9:Ext.DHCParityPins`, `G.9:Ext.QDArchiveParity`, `G.9:Ext.OEEParity`) and the referenced records they cite.
7. **Bind comparator choice to CG-Spec (CSLC comparability and admissibility).** Any numeric comparison or aggregation MUST be CSLC‑admissible and cite the corresponding CG‑Spec entry (via `ComparatorSpecRef`). If Characteristics differ by unit, scale, or space, the plan MUST declare the ids used for “normalize, then compare” (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) — ids only; semantics are defined elsewhere.
8. **Declare order & PortfolioMode semantics.** Parity MUST preserve set‑return semantics; `PortfolioMode` and `DominanceRegime` are either explicitly pinned or cited through `G.Core.DefaultGoverningDefinitionIndex`. IlluminationSummary/coverage/regret remain telemetry unless a CAL policy explicitly promotes them (policy‑id pinned & recorded).
9. **Attach planned baselines (when applicable).** If parity depends on planned slot fillings, the plan cites the relevant `SlotFillingsPlanItem` refs (A.15.3) via `PlanItemRefs[]` rather than embedding a competing baseline object (nil‑elision when unused).
10. **Publish crossing pins (when invoked).** Cross-Context or cross-plane/Kind reuse requires explicit Bridge/CL/Φ pins; penalties affect `R_eff` only (invariants pinned through `G.Core`).

#### G.9:4.3 — Execution protocol (run‑time / selector‑adjacent)

Execution is **one run** under the pinned plan:

1. **Validate CSLC references and pins.** Validate the cited CSLC comparability and admissibility references, active pins, and witnesses; run eligibility or acceptance checks under the plan’s `TaskSignature (S2)` and refuse or abstain on non-admissible operations (record trace; no “fourth status”). If a live `A.21` gate consumes this check, cite its `GateDecisionRef`/`DecisionLogRef`; do not create a `G.9`-local CSLC gate.
2. **Invoke selection/dispatch.** Apply **G.5** under the plan’s pinned refs and emit selector outputs in a form consistent with G.5’s `PortfolioMode` and selected-set semantics.

When parity is comparing bounded specialization, the report should echo the active specialization profiles or equivalent pins so readers can recover the work-measure threshold target, prior exposure, budget-to-threshold, post-threshold efficiency when relevant, transfer, retention, downside field, and any corridor-entry baseline or evidence note from the parity object itself rather than from later narrative explanation.

3. **Record comparability mapping (when used).** If `UNM_id?` / `NormalizationMethodId[]?` / `NormalizationMethodInstanceId[]?` were declared, **echo them** in `ParityReport@Context` (or in its explicit pins deltas) and record their ids (and any scoped notes required by the cited governing spec ref) in audit pins/SCR; cite the applicable `PathId`s.
4. **Publish trace.** Emit `ParityReport@Context` with EvidenceGraph citations and all active pins (editions/policy‑ids), so the run can be re‑checked and re‑run.
5. **Emit telemetry hooks (optional, report‑only).** When telemetry is produced, it is emitted as telemetry pins/events for refresh wiring (not as a silent change in dominance interpretation).

#### G.9:4.3a — Worked parity slice

- Two agentic search setups both claim bounded specialization on the same declared task family.
- The `ParityPlan` pins the same freshness window, threshold target, adaptation budget, prior-exposure declaration, comparator editions, and corridor-entry baseline. One setup reaches threshold sooner but shows low retention and no transfer. The other reaches threshold later, but carries reusable transfer and lower downside field.
- A CSLC-admissible `ParityReport@Context` therefore states what was held constant, which signals remained telemetry, and why the outcome stays a governed selected set or partial order rather than collapsing into a scalar winner. The reader can recover the practical comparison from the parity slice itself before reading any optional wiring blocks.

#### G.9:4.3b — Conditional causal method rung parity

Use this conditional extension only when a parity report compares causal methods or causal-use claims. The parity report starts with a cheap screen and may stop at degraded parity or abstain when methods plainly answer different causal uses.

```text
CausalRungParityScreen:
  comparedMethodsRef: ComparedMethodSetRef
  targetCausalityLadderRungSet: {CausalityLadderRung...}
  causalEvidenceSupportBasisSet: {CausalEvidenceSupportBasis...}
  sameEstimand: yes | no | unclear
  sameOutcomeWindow: yes | no | unclear
  cheapParityStop: CausalRungParityScreenOutcome
```

```text
CausalRungParityScreenOutcome =
    comparableEnoughForFullRecord |
    crossRungDegrade |
    crossSupportBasisDegrade |
    differentEstimandAbstain |
    differentOutcomeWindowAbstain |
    returnToC28
```

Open the full `CausalMethodRungParityRecord` only when `CausalRungParityScreenOutcome = comparableEnoughForFullRecord`. Other outcomes are admissible cheap stops: degraded parity, abstain, or apply `C.28`, without fabricating a full parity record.

`targetCausalityLadderRungSet` is the first parity check. Here `CausalityLadderRung` is a cited causal-use taxonomy value, not a maturity level, upgrade ladder, or superiority scale. If the set has more than one causality-ladder rung and no declared bridge and loss makes the comparison meaningful, the screen returns `crossRungDegrade` rather than treating the methods as peers.

`causalEvidenceSupportBasisSet` is the second parity check. If methods depend on different causal support bases and no declared support-loss or bridge makes the comparison meaningful, the screen returns `crossSupportBasisDegrade`.

`sameEstimand = no` returns `differentEstimandAbstain` unless the report names a shared estimand, a bridge and loss relation, or a reason the comparison is intentionally non-parity. A scalar parity result is not admissible across different estimands by default.

`sameOutcomeWindow = no` returns `differentOutcomeWindowAbstain` unless the report pins a common follow-up window or declares the window loss. A method that wins at one horizon is not parity-superior at another horizon by default.

Parity reports comparing causal methods then carry a `CausalMethodRungParityRecord`:

```text
CausalMethodRungParityRecord:
  comparedMethodsRef
  causalUseQuestionRef?: U.CausalUseQuestion
  targetCausalUseClaimKind: CausalUseClaimKind
  targetCausalityLadderRung: CausalityLadderRung
  estimandRef: U.CausalEstimand
  declaredCausalityLadderBridgeOrLossRef?
  interventionBudgetOrActionSetRef?
  causalEvidenceSupportBasis: CausalEvidenceSupportBasis
  declaredCausalEvidenceSupportLossRef?
  causalUseSupportRecordRef?
  causalUseSupportVerdict?: CausalUseSupportVerdict
  causalFollowUpWindowRef
  outcomeMeasureRef
  sourcePopulationRef?
  targetPopulationRef?
  causalTransportabilityProfileRef?
  estimationValidityClassRef?
  causalParameterEstimationProfileRef?
  parityVerdict: parityEstablished | degraded | abstain
  supportedParityUse
  unsupportedParityUse
```

Parity reports comparing causal methods fill this record so the "same" claims are checkable by fields rather than prose:

- comparedMethodsRef;
- targetCausalityLadderRung;
- targetCausalUseClaimKind: CausalUseClaimKind;
- estimandRef;
- interventionBudgetOrActionSetRef;
- causalEvidenceSupportBasis;
- causalUseSupportRecordRef and causalUseSupportVerdict when a `C.28` support record or verdict is being consumed;
- causalFollowUpWindowRef;
- outcomeMeasureRef;
- declaredCausalityLadderBridgeOrLossRef where causality-ladder rungs differ;
- causalTransportabilityProfileRef where source population, target population, domain, context, or evidence regime differs;
- causalParameterEstimationProfileRef where estimation validity, uncertainty, nuisance handling, or sensitivity differs;
- degraded or abstain posture where parity cannot be established.

Causality-ladder parity is a degrade/abstain condition, not a universal comparison ban. Cross-rung method comparisons must name `declaredCausalityLadderBridgeOrLossRef` and cannot become superiority claims by default.

What changes in practice: one benchmark cannot compare a predictive model, an interventional action/effect question optimizer, and a counterfactual comparison question strategy as one undifferentiated "method improvement" set.

What this does not authorize: `G.9` does not decide causal identification, causal fairness, or counterfactual sampling realizability; it keeps parity/benchmark harness authority and sends causal-use support to `C.28`.

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
* **RequiredPins/EditionPins/PolicyPins (minimum; conditional on use):**
  * `DHCMethodRef.edition`
  * `DHCMethodSpecRef.edition?` *(when the cited DHC method spec distinguishes method vs method-spec editions)*
* **RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
* **Notes (wiring-only):** Declares the pins required to make DHC‑based parity reproducible and RSCR‑refreshable; semantics of DHC lives in `C.21`.

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
| **G.9‑1 `Plan_Parity`**            | `BaselineSet`, `BaselineBindingRef`, `FreshnessWindows`, `Budgeting?`, `EpsilonDominance?`, `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`, `SCPRef.edition?`, `MinimalEvidenceRef.edition?`, `UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`, `ParityPinSet`, `PlanItemRefs[]?` | `ParityPlan@Context` (UTS entry; edition‑pinned)                                                |
| **G.9‑2 `Run_Parity`**             | `ParityPlan@Context`, `TaskSignatureRef` (S2), **G.5‑3 Select**                                                                                  | Selector outputs (selected sets / archives / sets as refs), DRR+SCR pins with `PathId[]`/`PathSliceId?` |
| **G.9‑3 `Publish_ParityReport`**   | parity-run trace refs + active pins                                                                                                            | `ParityReport@Context` (UTS publication record; emits canonical RSCR ids)                       |
| **G.9‑4 `Expose_ParityTelemetry`** | Telemetry deltas (archive changes, coverage/regret signals, etc.)                                                                                | Telemetry events carrying `PathSliceId?`, policy‑ids, and edition pins for refresh wiring       |

*Publication records are conceptual here; serialisations belong in shipping and interop publication forms (see `G.10` and interop annexes), not in `G.9`.*

### G.9:6 — Conformance Checklist (CC‑G9)

**CC‑G9‑CoreRef (normative; mandatory).**
G.9 conforms only if it satisfies the **effective** set of `CC‑GCORE‑*` declared in **G.9:4.0 GCoreLinkageManifest** (including trigger typing, Default Governing Definition Index links, and P2W split).

1. **CC‑G9.1 — Equal windows (and budgets) & pinned spec editions (local).**
   A ParityPlan **SHALL** declare a single `FreshnessWindows` shared across baselines. If `Budgeting` is used/pinned, it **SHALL** be shared across baselines as well. `ParityPinSet` **SHALL** include the edition pins required by the referenced governing spec and comparator refs (at minimum `CNSpecRef.edition`, `CGSpecRef.edition`, `ComparatorSpecRef.edition`).
   If the parity run depends on planned slot fillings (WorkPlanning baseline), the plan **SHALL** cite the relevant `SlotFillingsPlanItem` refs via `PlanItemRefs[]` (nil‑elision when not applicable).

2. **CC‑G9.2 — Mode‑specific definition pins are declared via Extensions (local; conditional).**
   When parity depends on mode‑specific definition records beyond the pinned governing spec refs (e.g., DHC/QD/OEE), the ParityPlan/Report **SHALL** include the corresponding `GPatternExtension` blocks and satisfy their `RequiredPins/EditionPins/PolicyPins` (typically carried inside `ParityPinSet`, and echoed via pins deltas in audit):
   * DHC parity → `G.9:Ext.DHCParityPins`
   * QD archive parity → `G.9:Ext.QDArchiveParity`
   * OEE parity → `G.9:Ext.OEEParity`

3. **CC‑G9.3 — CSLC-admissible orders and arithmetic (delegation point + local constraint).**
   Delegated to `CC‑GCORE‑SET‑1` (and the relevant G.5 `PortfolioMode` / selected-set semantics). Additionally: any numeric comparison or aggregation invoked by parity **SHALL** be CSLC-admissible and cite the corresponding CG‑Spec entry; non-admissible operations (e.g., ordinal means / mixed‑scale weighted sums) **SHALL** be refused or abstained with path‑cited trace (citation only; arithmetic admissibility comes from `CG‑Spec`/`MM‑CHR`).

4. **CC‑G9.4 — Normalization discipline (local citation only).**
   If Characteristics differ by unit, scale, or space, the ParityPlan **SHALL** cite the CSLC-admissible comparability mapping by id (`UNM_id?`, `NormalizationMethodId[]?`, `NormalizationMethodInstanceId[]?`) and compare only after that mapping is applied (“normalize, then compare”).
   If such mapping ids are used, the ParityReport **SHALL** echo the same ids (directly or via explicit pins deltas) so the run is reproducible/auditable without out‑of‑band context.
   The harness **SHALL NOT** define a local mapping.

5. **CC‑G9.5 — Dominance/PortfolioMode interpretation & telemetry separation (local).**
   ParityPlan/ParityReport **SHALL** either (i) explicitly pin the applicable regime/mode via refs/policy‑ids, or (ii) cite the corresponding defaults for `DefaultId.DominanceRegime` and `DefaultId.PortfolioMode` via `G.Core.DefaultGoverningDefinitionIndex`. Any non‑default “promotion” behaviour must be policy‑bound and recorded via policy‑id pins.
   IlluminationSummary/coverage/regret **SHALL** be treated as telemetry (report‑only by default); any promotion into dominance is an explicitly pinned CAL policy and MUST be recorded in audit pins/SCR.

5a. **CC‑G9.5a — Adaptation parity disclosure (local; conditional).**
   When the parity claim concerns bounded specialization, the ParityPlan and ParityReport **SHALL** pin the declared task family or target scope cut, the work-measure threshold target, adaptation budget, prior exposure declaration, and any transfer, retention, downstream exploitation efficiency, downside field, or corridor-entry baseline/evidence note that materially affects comparison.

6. **CC‑G9.6 — Epsilon‑front thinning (local; conditional).**
   If ε‑front thinning is used, `EpsilonDominance (ε≥0)` **SHALL** be explicit in the plan/report and pinned (param/id) such that the same ε is reproducible.

7. **CC‑G9.7 — Crossing visibility (delegation point).**
   Delegated to `CC‑GCORE‑CROSS‑1` and `CC‑GCORE‑PEN‑1`. This item remains as a stable delegation point for Bridge and reference-plane crossing visibility plus R-channel penalty placement discipline.

8. **CC‑G9.8 — Evidence trace completeness (local).**
   A ParityReport **SHALL** include an EvidenceTrace with `EvidenceGraphId` and the relevant `PathId[]` (and `PathSliceId?` when needed), covering both inclusions and refusals/abstains/degrades.

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
    `Run_Parity` / `Publish_ParityReport` **SHALL** record the ParityHarness identity (UTS ids) and the active pins required to interpret the outcome (editions + policy‑ids), so parity remains auditable without relying on “decision logs”.

14. **CC-G9-CLP-1 - Causal method rung parity.** If a parity report compares causal methods, it SHALL first run `CausalRungParityScreen`; when full parity remains plausible, it SHALL declare target causality-ladder rung, causal-use claim kind, `estimandRef`, interventional-action basis, causal evidence support basis, transportability basis for the source population and target population when needed, estimation-validity basis when needed, bridge and loss relation where rungs differ, `causalUseSupportRecordRef` and `causalUseSupportVerdict` when relevant `C.28` support is consumed, and degraded or abstain posture where parity cannot be established.


### G.9:7 — Anti‑patterns and remedies

* **AP‑1 Hidden edition drift.** Remedy: require edition pins in `ParityPinSet`; treat changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑2 Baseline set is informal prose.** Remedy: require `BaselineBindingRef` and EvidenceTrace pins.
* **AP‑3 Comparator semantics are “whatever the code did”.** Remedy: `ComparatorSpecRef.edition` (and any normalization/comparability refs) must be cited and pinned.
* **AP‑4 Cross‑Context reuse without visible crossing pins.** Remedy: cite Bridge/reference-plane records and crossing visibility records (delegated to G.Core).
* **AP‑5 Parity report becomes a hidden scoring sheet.** Remedy: preserve CSLC-admissible outcome shape and keep telemetry as telemetry unless explicitly policy‑promoted by the governing policy pattern.
* **AP‑6 “Metric” as a primitive in Tech.** Remedy: use `DHCMethodRef`/`U.Measure`/`DistanceDefRef` with editions; “metric” may appear only in Plain with an explicit pointer to canonical terms.
* **AP‑7 Hidden spec drift (spec edition pins missing).** Remedy: pin `DHCMethodSpecRef.edition` and register RSCR tests that fail on spec edition changes; refuse parity reuse on unpinned spec editions.

### G.9:8 — Archetypal grounding (informative; SoTA‑oriented)

**Show‑A — Multi‑tradition parity for decision systems (post‑2015 practice).**
ParityPlan pins a rolling evidence window and comparator refs; ParityReport publishes a selected-set outcome plus the evidence trace. Family labels such as preference-learning comparators, causal decision pipelines, offline-RL evaluation pipelines, and robust BO-style selectors remain illustrative until a `G.2` SoTA pack or named current source pins the exact family being compared; the parity report still must preserve the selected set or partial order rather than collapse everything into a single scalar.

**Show‑B — QD parity (MAP‑Elites lineage → CMA‑ME / DQD / QDax JMLR 2024, with QDHF or QDAIF refs only when a feedback-guided QD claim is live).**
ParityPlan pins descriptor/distance definitions and archive insertion policy editions. ParityReport includes archive outcomes and telemetry deltas needed for refresh, without silently converting illumination summaries into dominance.

**Show‑C — Open‑ended parity (POET as lineage; current generator-family claims require a named `G.2` SoTA pack or exact current source).**
ParityPlan pins transfer rule editions and exploration policy refs. ParityReport publishes selected-set outcomes plus transfer‑keyed traces (PathSlice), enabling refresh reruns when any pinned policy changes.

**Show-D — Causal method rung parity.**
A team compares an observational predictor, an intervention optimizer, and a counterfactual policy strategy under one "best causal method" headline. `G.9` first runs `CausalRungParityScreen`: if rungs, support bases, estimands, or outcome windows differ, the screen returns degraded parity or abstain before a full record is fabricated. When full parity remains plausible, `G.9` requires `CausalMethodRungParityRecord`: each method declares `targetCausalUseClaimKind`, target `CausalityLadderRung`, `estimandRef`, interventional-action basis, `CausalEvidenceSupportBasis`, relevant `C.28` support record and verdict when consumed, follow-up window, outcome measure, source population and target population basis, and estimation-validity basis. If those fields differ, the parity report names `declaredCausalityLadderBridgeOrLossRef`, transportability or estimation refs where available, and degraded or abstain posture. The admissible output may be a selected set by comparable rung, not one scalar winner.

### G.9:9 — Cited Records (what this pattern publishes)

**Exports (UTS‑publishable, edition‑pinned):**

* `ParityPlan@Context` (WorkPlanning plan item)
* `ParityReport@Context` (UTS publication record; work-result or audit-facing publication record only when the neighboring source relation is live)
* DRR+SCR refs (by id) and (when applicable) `PortfolioPackRef?`/selector output refs (by id), for downstream consumption.
* Telemetry pins/events (by id), for refresh wiring (`G.11`) and RSCR harnesses (`F.15`).

### G.9:10 — Relations

**C.27 temporal-claim relation.**

- C.27 may flag: dynamic parity when a benchmark actually compares rate-change, rhythm change, recovery speed, intervention effect, effort budget, or dynamic outcome.
- This pattern keeps: baseline, freshness, comparator edition, effort/budget parity, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: faster improvement is not benchmark superiority, and `dyn2BenchmarkParityBlock?` is a benchmark input declaration, not a benchmark harness.
- Exit: when live, recover `dynOrderCompared`, baseline window, adaptation/intervention window, effort or budget parity reference, rate/rate-change measure, `G9ParityPlanRef`, and optional `G9ParityReportRef`; G.5 is relevant only if selector publication consumes such a benchmark result.

**C.29 mathematical-lens adequacy relation.**

- C.29 may flag: parity or benchmark input whose comparator, distance, descriptor geometry, embedding, normalization, surrogate model, learned representation, parity measure, model-family label, or model-selection basis carries a load-bearing mathematical lens that is missing, under-specified, or overread.
- This pattern keeps: baseline set, freshness, comparator edition, normalization ids, bridge discipline, parity plan, parity report, and reproducible benchmark publication.
- Non-admissible use: a `C.29` output does not publish a benchmark report, create benchmark superiority, supply selector output, or supply parity-measure admissibility by itself.
- Exit: for an under-lensed or overread parity input, cite the applicable `C.29` output for the stated use: `NoMLANeeded`, `MLA.LensCandidateNote`, `MLA.OneLine`, `MLA.MiniCard`, `MLA.FullCard`, or `NeighborGoverningLocusNote`. Use the cheap output that changes the next admissible parity move; full-card work is only required when the live parity or benchmark claim needs it.


**Builds on:** `G.Core`, `G.5`, `G.6`, `G.4`, `F.15`, `E.17`, `E.18`, `A.21`, `F.17`, `E.5.2`, `E.10`.
**Publishes to:** **UTS** (plan/report ids), **G.11** (refresh wiring), **G.10** (shipping publication form; parity records are cited records).
**Uses:** **G.0**, **A.19**, **F.9**, and `C.28` when parity compares causal methods or causal-use claims.
**Uses (optional, via Extensions):** **G.7**, **C.18 and C.19** (QD/OEE wiring), **C.23** (SoS‑LOG narration and failure‑policy pins).

### G.9:11 — Working reading checks

- If two baselines are being compared under different freshness windows, comparator editions, or silent normalization rules, this pattern has not yet been satisfied.
- If parity cannot tell the reader what was held constant, what remained telemetry, and what crossings or penalties were active, the report is not yet usable.
- If a scalar winner is being claimed where only a selected set or partial order is CSLC-admissible, parity is overclaiming and should publish the CSLC-admissible outcome shape instead.

### G.9:End
## G.10 - SoTA Pack Shipping

**Tag:** Architectural pattern (conceptual; notation‑independent; pack‑boundary governing definition)
**Stage:** release‑time composition and publication; edition‑aware; **GateCrossing‑gated** via `E.18` CrossingBundle (and the relevant GateCrossing harness patterns).
**Builds on:** `G.Core` (Part‑G core invariants and delegation); upstream pack/kit governing definitions as cited publications or records (not redefined here).
**Governs (scope boundary):** *shipping* of Part‑G outputs as a **pack** (`SoTA‑Pack(Core)`), including the pack‑level publication kit: (i) selector‑facing selection/parity roster, (ii) PathId/PathSlice citation surface, (iii) telemetry pins for refresh planning, and (iv) optional interop ingestion as citation‑only notes.
**Does not govern:** governing spec refs (`CN‑Spec`, `CG‑Spec`), CHR/CAL semantics, selection semantics, evidence semantics, bridge calibration semantics, refresh orchestration (these remain with their governing definitions and are **cited**).

### G.10:1 - Problem frame — Shipping without smuggling semantics

Part G produces many **kit-governed** and **suite-governed** publications or records (harvest packs, CHR/CAL packs, evidence graphs, bridge calibration records, log bundles, parity reports). Without an explicit **pack-boundary governing definition**, “shipping” tends to become:

* an ad‑hoc folder/export ritual (tool‑locked, not citable), or
* a silent re‑specification layer (shipping accidentally redefines legality, defaults, or selection semantics), or
* a brittle hand‑off that cannot support RSCR/refresh (no actionable pins/editions/policies attached).

`G.10` fixes the pack boundary: it defines the **single, normative shipping surface** for Part‑G outputs — **`SoTA‑Pack(Core)`** — and a minimal choreography for making shipped artefacts **selector‑ready** and **audit‑citable**, while delegating all Part‑G‑wide invariants to `G.Core` (citation/delegation, not restatement).

### G.10:2 - Problem — Why naive shipping breaks reuse, legality, and refresh

Naive shipping fails (conceptually) when any of the following occurs:

1. **Format-as-governing-spec.** A concrete export format is treated as “the pack,” turning a tool choice into a governing pack definition.
2. **Editionless hand‑offs.** Shipped artefacts omit the edition/policy pins required to replay or compare outcomes, so parity and RSCR become non‑actionable.
3. **Pack smuggles semantics.** Shipping reintroduces “convenience” rules (hidden scalarisation, competing defaults, private gate decisions), fragmenting the governing spec ref.
4. **Invisible crossings.** Cross-context or cross-plane reuse is present, but the pack does not expose the crossing bundles and penalty policy pins needed for audit and refresh planning.
5. **No method‑of‑obtaining‑output disclosure.** Consumers receive outcomes without a minimal, citable trail of *which mechanisms/policies/editions produced them*.
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
  *(payload pins: `PackId(UTS)`, `publicationScopeId`, `CNSpecRef.edition`, `CGSpecRef.edition`, `PlanItemRefs := SlotFillingsPlanItemRef[]`, `AuditPins`, `UTSRowId[]`, `PathId/PathSliceId`, crossing policy pins, `TelemetryPinIds`, relevant upstream artefact ids)*

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

  `PlanItemRefs := SlotFillingsPlanItemRef[]?` *(WorkPlanning planned baseline refs)*,
  `AuditPins` *(pack‑level pin bundle: edition pins (only on `…Ref.edition`), policy‑ids, UTS/Path pins; ids only)*,

  `UTSRowId[]`,
  `PathId[]?`, `PathSliceId[]?`,
  `CrossingBundleIds := CrossingBundleId[]?`,
  `TelemetryPinIds := TelemetryPinId[]?`,
  `PortfolioRosterId?`,

  `MOOManifestId?` *(method‑of‑obtaining‑output disclosure; conceptual object id)*
  }
  *(Optional pins from `CrossingVisibilityPins` MAY be strengthened to unconditional by listing them above; `G.10` typically strengthens `UTSRowId[]` and path/crossing bundles when the pack is publicly shipped.)*

* `TriggerAliasMapRef` := `∅` *(no local trigger tokens in Phase‑2)*

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
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,

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
  PlanItemRefs := SlotFillingsPlanItemRef[]?,
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

#### G.10:4.2.1 - Portfolio roster (normative; pack-governed; governing-definition delegating)

`PortfolioRosterId` identifies the **selector‑facing** pack roster token. The corresponding `PortfolioRoster@Context` is one citation-and-binding roster record inside the shipped publication surface, not a `Surface` or `SurfaceKind` value:
it MUST NOT redefine selection / selected-set semantics (governed by `G.5`) or parity semantics (governed by `G.9`).
Mode‑specific definition pins (QD/OEE/interop) are introduced only via `G.10:Ext.*` blocks.

```
PortfolioRoster@Context :=
⟨
  PortfolioRosterId,
  PackId(UTS),
  CG-FrameContext,
  describedEntity,

  // Selector operation and default-resolution support
  portfolioMode?,
  dominanceRegime?,
  ε?,

  // Published selector outcome and set-surface declaration (metadata fields, not local semantics)
  selectorOutcomeKind?,
  setSurfaceKind?,
  handoffKind?,
  subjectKind?,
  sourceSurfaceKind?,
  derivedViewKind?,
  sourceSurfaceComposition?,
  basePaletteRef?,
  lensId?,
  shortlistId?,
  promotionPolicyRef?,
  retentionIntent?,

  // Selector-facing roster + provenance hooks (ids only)
  MethodFamilyIds := MethodFamilyId[]?,
  GeneratorFamilyIds := GeneratorFamilyId[]?,
  ParityReportId?,
  SCRId[]?, DRRId[]?,

  // Pin reuse: prefer referencing the enclosing pack’s AuditPins bundle
  AuditPins?,
  Notes?
⟩
```

*Presence rule:* `PortfolioRosterId` MAY be omitted only when the shipped pack is *inputs‑only*
(e.g., shipping CHR/CAL/evidence without any selector‑consumable selected-set/shortlist output).

The `selectorOutcomeKind`, `setSurfaceKind`, `handoffKind`, `sourceSurfaceKind`, `sourceSurfaceComposition`, `derivedViewKind`, `basePaletteRef`, `lensId`, and `shortlistId` fields in this roster are payload metadata fields or refs inside the shipped publication surface. They do not define new Part-E `SurfaceKind` values and they do not let `G.10` re-govern `G.5`, `C.18`, `C.19`, or `G.2` semantics.

**Interpretation constraints (normative by delegation).** Any universal invariants governing (i) CN/CG spec-ref governing-definition assignment, (ii) crossing visibility and penalty routing, (iii) tri‑state guards, (iv) set‑return semantics, (v) P2W split, (vi) defaults, and (vii) RSCR trigger typing are **not restated here** and are enforced via `G.Core` conformance (see `CC‑G10‑CoreRef`).

#### G.10:4.3 - Shipping choreography (normative; governing-definition delegating)

`G.10` prescribes a minimal, governing-definition delegating sequence for composing a shipped pack:

1. **S‑1 — Gather & pin.** Collect upstream artefact ids and verify the **required pins** implied by the linkage manifest (edition pins, policy pins, UTS/Path pins).
2. **S‑2 — Compose `SoTA‑Pack(Core)` + MOO disclosure.** Assemble the pack object and attach a **`MOOManifest`** that lists the referenced mechanisms/policies/editions that produced the shipped outcomes (ids only; semantics stay with governing definitions).
3. **S‑3 — Publish selection/parity roster (selector‑facing).** Produce a selector‑readable `PortfolioRosterId` with the parity/definition pins required for reproducibility; do not mandate formats.
4. **S‑4 — Anchor and publish path citations.** Ensure A.10 anchors exist and publish/record `PathId/PathSliceId` citations required for downstream explainability (e.g., `C.23/H4`) and maturity rung changes.
5. **S‑5 — Expose CrossingBundle.** For each GateCrossing relevant to the shipped artefacts, expose the required `CrossingBundle` references (fail fast on missing or non‑conformant bundles when required).
6. **S‑6 — Emit telemetry pins for refresh planning.** Whenever illumination increases or archive/OEE pin state changes, emit PathSlice‑keyed telemetry with policy‑id and the active `…Ref.edition` pins (and QD `EmitterPolicyRef`/`InsertionPolicyRef` when applicable).
7. **S‑7 — Publish to UTS (twin labels).** Mint/refresh UTS Name Cards needed to cite the pack and shipped heads (Tech/Plain twins when required); cross‑Context identity travels only via Bridges with CL and loss notes.
8. **S‑8 — Optional: ingest interop surface.** If `G.13` interop is in use, ingest/cite `InteropSurface@Context` as annotation-only notes, pinning external index editions; do not redefine interop semantics.

#### G.10:4.4 - Interfaces & hooks (selector‑ and audit‑facing)

| ID         | Interface (conceptual)     | Consumes                                                          | Produces                                                |
| ---------- | -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| **G.10‑1** | `Compose_SoTA_Pack`        | G.* outputs, ComparatorSet, Bridges, editions, SCR/DRR deltas     | `SoTA‑Pack(Core)` (UTS row + surfaces) + `AuditPins` (+ `MOOManifestId?`) (+ `PortfolioRosterId?`) |
| **G.10‑2** | `Publish_UTS`              | `PackId(UTS)`, `UTSRowId[]`, deprecation/edition‑bump notes       | UTS rows/Name Cards for the pack and shipped heads (incl. twins when required) |
| **G.10‑3** | `Expose_CrossingHooks`     | GateCrossings, lanes/planes/contexts                              | **CrossingBundle** (**E.18:CrossingBundle**) per GateCrossing; **fail** on missing/non‑conformant bundles |
| **G.10‑4** | `Pack_MOO`                 | referenced mechanism/policy/edition ids                           | `MOOManifestId` (ids only; governing-definition delegating) |
| **G.10‑5** | `Emit_TelemetryPins`       | Illumination/archive/OEE events                                   | PathSlice‑keyed telemetry: `policy‑id`, `…Ref.edition` (+ QD/OEE pins when applicable) |
| **G.10‑6** | `Publish_PathCitations`    | A.10 anchors, PathIds                                             | PathId/PathSlice citations for `C.23/H4` & rung changes |
| **G.10‑7** | `Ingest_InteropSurface?`   | (optional) `G.13 InteropSurface@Context`                          | Annotated pack notes citing external‑index editions     |

*Surfaces remain **conceptual** per **E.5.2**; RO‑Crate/ORKG/OpenAlex mappings belong to **Annex/Interop** and do not affect Core conformance.*

> **Note.** Any concrete serialisation/export is *not* part of this interface set. Serialisation belongs to interop/annex governing-definition assignment and must not become the governing definition.

#### G.10:4.5 - Consequence of governing-definition assignment (normative boundary statement)

`G.10` is the **one governing definition** of “shipping” in Part G *(by delegation to `CC‑GCORE‑SKP‑1`)*.
Other `G.x` patterns may produce artefacts that are shipped, but they must not embed shipping obligations; they cite `G.10` shipping surfaces instead.

#### G.10:4.6 - Extensions (pattern‑scoped; non‑core)

All method‑/generator‑/interop‑specific shipping extension declarations live here as `GPatternExtension` blocks.

##### GPatternExtension — `G.10:Ext.QDArchiveShippingPins`

**PatternScopeId:** `G.10:Ext.QDArchiveShippingPins`
**GPatternExtensionId:** `QDArchiveShippingPins`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18`
**Uses:** `{C.18, G.5, G.8, G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `DHCMethodRef.edition?`
* `DHCMethodSpecRef.edition?`
* `EmitterPolicyRef` *(policy‑id / ref)*
* `InsertionPolicyRef` *(policy‑id / ref)*
* `CharacteristicSpaceRef` *(id/ref; iff archive partitioning is declared)*
* `CharacteristicSpaceRef.edition?` *(iff partitioning depends on an editioned space definition)*
* `PathSliceId[]` *(to bind telemetry/refresh scope when archive behaviour is present)*

**RSCRTriggerSetIds:** `∅` *(covered by `G.10` core linkage via `GCoreTriggerSetId.RefreshOrchestration`)*
**Notes (shipping-pin discipline):**
* This block never redefines archive semantics; it only states which pins must be present in the shipped pack when QD archive fields are present.

##### GPatternExtension — `G.10:Ext.OEEShippingPins`

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

##### GPatternExtension — `G.10:Ext.InteropCitation`

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

- Published surfaces should carry the selector outcome kind and, when applicable, the set-surface kind or handoff kind, plus the subject kind, source surface kind, and relevant declared surface pins.
- These are publication payload metadata fields inside `SoTA-Pack(Core)`, not new Part-E `SurfaceKind` values.
- Good publication fields include `selectorOutcomeKind`, `setSurfaceKind`, `handoffKind`, `subjectKind`, `sourceSurfaceKind`, `sourceSurfaceComposition`, `dominanceRegime`, `lensId`, `shortlistId`, and any declared archive or promotion-policy ids that the reader needs to interpret the visible set.
- Those payload fields should use controlled tokens, cited ids, or already-declared head labels rather than shipping-local prose values.
- When the visible surface or the shortlisted source is one derived tradition view, also publish the derivation explicitly.
- Useful additional fields there include `derivedViewKind`, `basePaletteRef`, and the declared `qId` or reachability rule id that disciplined that derivation.
- `portfolioMode` may remain as one support field about selector operation, but it should not stand in for the public set label.
- A published surface should mirror semantics that are already declared in the governing palette, front, archive, or shortlist language.
- It should not redefine that semantics locally.
- When one shipped surface still needs a plain-language label, use the declared set-surface kind and source surface rather than falling back to `portfolioMode`.

#### G.10:4.7.1 - Worked publication slice

- If the visible surface is one tradition front under the declared `Q`, publish `selectorOutcomeKind=SetSurfaceOutcome`, `setSurfaceKind=Front`, `sourceSurfaceKind=Front`, `derivedViewKind=TraditionFront`, and keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable instead of pretending that the palette itself already was that front.
- If one shortlist is emitted from that derived tradition front, publish `selectorOutcomeKind=SetSurfaceOutcome`, `setSurfaceKind=Shortlist`, `sourceSurfaceKind=Front`, `derivedViewKind=TraditionFront`, `basePaletteRef=SoTAPaletteDescriptionId`, and the named `lensId` together.
- If that same shortlisted surface is emitted as one stable public object, also publish `shortlistId=<...>` and keep it recoverable that the token names that shortlist rather than replacing it.
- If one retained tradition archive view is shown, publish `selectorOutcomeKind=SetSurfaceOutcome`, `setSurfaceKind=Archive`, `sourceSurfaceKind=Archive`, `derivedViewKind=TraditionArchive`, and keep the same `basePaletteRef` recoverable.
- If the shortlist is later ordered, publish `setSurfaceKind=RankedShortlist` and keep the declared source surface visible.
- Do not publish `setSurfaceKind=ChoiceSet` unless the shipped object is explicitly one mathematical analysis artifact rather than the public selected surface.
- Do not publish `sourceSurfaceKind=TraditionPalette` alone when the visible object is already one derived tradition view; readers need to know which view is on the surface and which base palette it depends on.
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

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Format bias (Arch/Prag).** A popular export format is tempting to treat as “the pack”.
  *Mitigation:* keep Core surfaces conceptual (E.5.2); move serialisation recipes to Annex/Interop; keep conformance on semantics.
* **Centralisation bias (Gov).** A single pattern governing shipping semantics can become a bottleneck.
  *Mitigation:* keep shipping as one explicit governing-pattern responsibility, but push mode/method specifics into explicit `G.10:Ext.*` extension blocks and cite governing patterns.
* **Telemetry→dominance bias (Onto/Prag).** Shipping pipelines often “promote” telemetry proxies (illumination/coverage) into ranking.
  *Mitigation:* preserve the telemetry/order separation and require explicit CAL policy‑id for any promotion; record the policy‑id in audit pins/telemetry.
* **Interop authority bias (Onto/Epist).** External indexes can silently override local legality/typing.
  *Mitigation:* `G.10‑6` ingests interop only as cited notes (editions + mapping policy refs), never as a replacement governing spec ref.

### G.10:7 - Archetypal grounding (informative; post‑2015 method families)

**World‑plane (benchmark shipping).**
A CG‑Frame ships a selected set that includes a QD archive (e.g., MAP‑Elites‑class / CMA‑ME‑class families) and a generator family (e.g., POET‑class environment generation). The shipped `SoTA‑Pack(Core)` cites the CHR/CAL packs and records the QD/OEE extension-required pins through the extension blocks so that downstream parity and refresh can be scoped to the affected `PathSliceId`s rather than forcing a global rebuild.

**Episteme‑plane (synthesis shipping).**
A CG‑Frame ships a pluralistic set of admissible methods gathered from post‑2015 literature streams (living review + synthesis pack). The shipped pack carries explicit CN/CG spec refs, evidence path citations, and method‑of‑obtaining‑output disclosure; downstream selection uses set‑valued outcomes and can schedule refresh when the synthesis pack or key pins change.

### G.10:8 - Conformance checklist (CC‑G10)

This pattern inherits order/illumination, evidence, and bridge/penalty legality from the cited governing patterns (not restated here). Shipping‑specific requirements:

| ID  | Statement   | Verification notes (conceptual)  |
| --- | ----------- | -------------------------------- |
| **CC‑G10‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `G.10:4.1` (after profile/set/pin‑set expansion under `Nil‑elision`). | Check that the linkage manifest is present and that the expanded obligations are not contradicted. |
| **CC‑G10.1 (Notation‑independent).** | The pack MUST NOT rely on any specific file syntax; cards/tables are conceptual; tool serialisations are informative only. | Look for format‑free conceptual fields; any serialisation is explicitly non‑normative. |
| **CC‑G10.2 (Pack parity pins).** | If QD/OEE fields are present, pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, (optional) `DHCMethodRef.edition` / `DHCMethodSpecRef.edition` when used, and (OEE) `TransferRulesRef.edition`; include `CharacteristicSpaceRef` (+ `CharacteristicSpaceRef.edition` when it affects partitioning reproducibility); for QD archive semantics also pin `EmitterPolicyRef` and `InsertionPolicyRef`. | Verify the corresponding `G.10:Ext.*` block is present and the pins appear in AuditPins and (when relevant) in telemetry pins. |
| **CC‑G10.3 (Telemetry discipline).** | Any illumination increase or archive edit SHALL log `PathSliceId`, the active `policy‑id`, the active editions of the pinned `…Ref` fields (incl. OEE `TransferRulesRef.edition`), and the active `EmitterPolicyRef`/`InsertionPolicyRef` when applicable. | Verify emitted telemetry is PathSlice‑keyed and carries the required pins; ensure causes are recorded using canonical trigger kinds (alias labels optional only). |
| **CC‑G10.4 (UTS publication & twins).** | All shipped heads appear on UTS with Tech/Plain twins **per delegated UTS discipline**; cross‑Context identity (when present) is routed via Bridges with CL and loss notes **per delegated crossing discipline**. | Verify UTS rows exist and that any cross‑Context identity is routed via Bridge artefacts with visible CL/loss notes. |
| **CC‑G10.5 (MOO surfaced in shipping).** | For every declared selector set-surface or archive published, the pack SHALL list the applicable generation/parity mechanism ids (e.g., QD `EmitterPolicyRef`/`InsertionPolicyRef`, parity harness ids, method refs where the method definition is generative) and the active policy‑id(s) in SCR‑visible bindings and telemetry pins (ids only; governing-definition delegating). | Verify `MOOManifestId` is present when outcomes are intended for downstream use and does not redefine semantics. |
| **CC‑G10.6 (Pack completeness as a citation surface).** | The pack cites all included upstream artefacts by id/ref and exposes the required pins (`AuditPins`, UTS/Path pins, CrossingBundleIds when required). | Verify all present payload artefacts have ids and the pins needed to cite/replay them. |
| **CC‑G10.7 (CrossingBundle exposure).** | For each GateCrossing relevant to shipped artefacts, the pack exposes the relevant `CrossingBundleIds` (or records that no such crossings exist) **per delegated crossing visibility discipline**, and shipping fails fast on missing/non‑conformant crossing bundles when required. | Verify crossing bundle presence/absence is honest and aligned with the shipped artefacts’ declared crossings. |
| **CC‑G10.8 (Baseline binding is explicit when used).** | If the shipped pack claims a planned baseline, `PlanItemRefs := SlotFillingsPlanItemRef[]` are present (WorkPlanning plan items, cited; no execution logs). | Verify plan items are cited by id and the pack does not treat decision records or execution logs as authoritative plan items. |
| **CC‑G10.9 (Extension‑scoped pin declaration).** | If QD/OEE/interop fields are present, the corresponding `GPatternExtension` block is present and its required pins/editions/policies are recorded in AuditPins and in emitted telemetry pins when those pins affect refreshability. | Verify conditional extension pins are not silently omitted when the mode is used. |
| **CC‑G10.10 (Derived tradition-view shipping).** | If the visible shipped surface or shortlisted source is one derived tradition view such as `TraditionFront` or `TraditionArchive`, the pack **MUST** publish the declared `sourceSurfaceKind`, keep `basePaletteRef=SoTAPaletteDescriptionId` recoverable, and carry the derivation basis (`derivedViewKind`, declared `Q`, or reachability/coverage rule id) with enough explicitness that the visible surface cannot be mistaken for the default palette semantics. | Verify derived tradition views are shipped as derived views, not as silent redefinitions of the base palette. |

### G.10:8.1 - Anti‑patterns and remedies

* **AP‑1 Format‑as‑governing‑specification.** Remedy: keep Core surfaces conceptual (E.5.2); move serialisation to Annex/Interop; enforce `CC‑G10.1`.
* **AP‑2 Hidden edition drift.** Remedy: require `…Ref.edition` pins in AuditPins and treat edition changes as RSCR‑relevant via canonical trigger kinds.
* **AP‑3 “QD archive present” but missing definition pins.** Remedy: enforce `CC‑G10.2` and the `G.10:Ext.QDArchiveShippingPins` pin declarations.
* **AP‑4 Telemetry silently becomes dominance.** Remedy: keep telemetry report‑only unless an explicit CAL policy promotes it; require policy‑id recorded (ties to `CC‑G10.3` and MOO discipline).
* **AP‑5 No PathSlice key → refresh becomes global.** Remedy: enforce PathSlice‑keyed telemetry and path citations (`G.10‑4`, `G.10‑5`).
* **AP‑6 Cross‑Context reuse without visible crossing pins.** Remedy: require `CrossingBundleIds` + Bridge/CL policy pins; fail fast on missing/non‑conformant bundles (`CC‑G10.7`).
* **AP‑7 Interop ingestion rewrites semantics.** Remedy: ingest interop as cited notes only; semantics remain in `G.13` (`G.10‑6`, `G.10:Ext.InteropCitation`).
* **AP‑8 Derived-view collapse.** Remedy: ship `sourceSurfaceKind`, `derivedViewKind`, `basePaletteRef`, and the declared `Q` or reachability basis with enough explicitness that one derived tradition view cannot masquerade as the default palette meaning.

### G.10:8.2 - SoTA‑Echoing (post‑2015, for orientation)

* **Research‑object packaging & provenance.** Post‑2015 practice increasingly treats “release artefacts” as *packages with explicit provenance, versions, and minimal replay pins* (e.g., modern research‑object and RO‑Crate‑class approaches). `G.10` mirrors the “package‑as‑citation‑surface” idea while keeping semantics governing-definition delegated.
* **Reproducibility regimes in ML/AI.** Contemporary reproducibility checklists, artifact evaluation/badging, and benchmark reporting norms motivate: explicit version pins, explicit method disclosure, and separating telemetry summaries from decision criteria unless policy‑promoted.
* **Scholarly KG interoperability.** ORKG/OpenAlex‑class ecosystems highlight the need to treat external mappings as *interop notes with editions*, not as replacement governing spec refs — matching the `G.10‑6` and `G.10:Ext.InteropCitation` stance.

### G.10:9 - Relations

**Builds on:** `G.Core`; consumes/cites artefacts governed by cited patterns from `G.2` (harvest pack), `G.3` (CHR pack), `G.4` (CAL pack), `G.6` (EvidenceGraph), `G.7` (bridge calibration), `G.8` (SoS‑LOG bundle), `G.9` (parity report), optional `G.12` (dashboard slice), optional `G.13` (interop surface).
**Publishes to / used by:** UTS (pack identity), selector‑facing consumers (via `G.5`), audit and assurance publications (SCR/RSCR), refresh orchestration (`G.11`).
**Constrains:** tooling exports are downstream; serialisation and repository integration are explicitly non‑normative here.

### G.10:End

---

## G.11 - Telemetry-Driven Refresh & Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
**Status.** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time + maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit publication units and records).** `RefreshQueue`, `RefreshPlan@Context` (WorkPlanning plan item), `RefreshReport@Context` (Work or Audit record), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue + alias docking + Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId`/`PathSliceId`), `G.7` (Bridge Sentinels; CL/Φ/plane policy pins), `G.5` (set-returning selection/dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness/decay), `E.18` (GateCrossing/CrossingBundle visibility), optional `C.18 and C.19` (QD/E–E policy pins), `C.23` (SoS-LOG branches / maturity ladders), `C.28` (causal-use support records whose SoTA-sensitive fields can change downstream support).

**Non-duplication note (Phase-2).**
This pattern **does not** (i) define the meaning of RSCR trigger kinds, (ii) introduce “shadow specs” for CN/CG legality, (iii) redefine tri-state guards / penalties / set-return semantics, (iv) re-govern shipping or harvesting, or (v) mint new `RSCRTriggerKindId` / default governing definitions (design-time changes live in `G.Core` and are recorded via DRR, `E.9`).
All such universal norms are **cited via `G.Core`** and enforced through **delegation** in this pattern’s conformance checklist.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination/archive changes, parity outcomes, dashboard deltas),
* **decay** (freshness windows expire; epistemic debt grows),
* **edition drift** (descriptor/distance/transfer rules bump; policy pins evolve),
* **bridge evolution** (CL/plane penalties or calibrations update).

Without an explicit orchestration kit, refresh becomes either:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only posture that silently accumulates drift.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: it turns typed refresh causes into **scoped plans** and **auditable execution reports**, while delegating all cause semantics and universal invariants to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and legality

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Deprecated trigger labels (e.g., `T0…T7`) are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS/Path/policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance/`PortfolioMode`/Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Refresh is triggered by run-time telemetry and decay, yet must remain auditable as Work (pins, refs, paths), not as opaque “decisions.”
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting/parity/shipping without re-implementing them or importing discipline-specific method semantics into core.
* **Policy-bound behavior vs. “smart defaults.”** Ordering of refresh, priority heuristics, and budget handling are valuable—but must live as policy-bound extensions, not as hidden universal rules.

### G.11:4 - Solution — RSCR-driven refresh as a P2W-scoped orchestration kit

#### G.11:4.1 - G.Core linkage (normative)

**GCoreLinkageManifest (normative; canonical shape per `G.Core`; Nil‑elision permitted).**

`GCoreLinkageManifest := ⟨
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

    RefreshPlanId,
    RefreshReportId,
    DeprecationNoticeId?,
    EditionBumpLogId?,

    SlotFillingsPlanItemRef[]?
  },

  DefaultsConsumed := ∅,
  TriggerAliasMapRef := G.Core.TriggerAliasMap.G11
⟩`

By the `G.Core` **Expansion rule**, the **effective** conformance ids / trigger‑kinds / pin‑obligations for `G.11` are the manifest expansions (profiles/sets/pin‑sets) plus the explicit deltas above.

**LegacyTriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (pattern-governed; conceptual artefacts)

`G.11` defines a minimal kit of *authoring-plane* artefacts that make refresh explicit and auditable.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (WorkPlanning plan item).**
   A planned refresh is a WorkPlanning object that **does not execute Work** and **does not embed gate decisions**. It declares:

* `RefreshPlanId` (UTS-published id; editioned)
* `describedEntity` and `ReferencePlane` pins (by ref; no implicit widening)
* `TargetScope := PathSliceId[] | PatternScopeId[]`
* `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids + scope + payload pins)
* `PlannedActions := RefreshAction[]` (each action delegates to a governing pattern)
* `RequiredPins := {EditionPins, PolicyPins, UTS/Path pins}` for replayability
* `PlanItemRefs := SlotFillingsPlanItemRef[]` (when planning baselines or reruns requires explicit planned slot fillings)

3. **`RefreshReport@Context` (Work/Audit artefact).**
   An execution report (Work or Audit artefact) that records:

* `RefreshReportId` (UTS-published id; editioned)
* `ExecutedActions[]` with links to cited artefacts governed by cited patterns (e.g., new parity report id, new pack id)
* `ObservedDeltas` (telemetry deltas, legality changes, evidence-path changes) as refs/pins—not as untyped prose
* `RSCRRefs[]` (any RSCR / regression harness artefacts invoked)
* `EmittedNotices[] := DeprecationNoticeId[]` and `EditionBumpLogId[]`
* the canonical trigger kinds actually applied (not only aliases)

4. **`DeprecationNotice@Context` and `EditionBumpLog@Context`.**
   Controlled evolution artefacts that preserve ID-continuity:

* **DeprecationNotice** explains scope, reason class (canonical trigger kind ids), and successor refs.
* **EditionBumpLog** records edition increments and the pins that justify them.

> *Note (normative by delegation).* ID continuity and alias discipline are governed by `G.Core` (do not restate as local rules here).

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)

`G.11` turns typed causes into scoped actions without governing the semantics of those actions.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness/decay events (`B.3.4`),
* evidence/bridge/policy/edition edits (from the respective governing patterns’ publication surfaces).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence paths (`G.6` `PathId/PathSliceId`),
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions/policies).

The closure is a *planning-time claim* (“these slices are affected”), not a Work-time output.

**4.3.3 Planning (P2W seam).**
Produce `RefreshPlan@Context` that schedules actions of the form:

* `RerunHarvest` (delegates to `G.2`/`G.1`/governing definition; if used)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetSurface` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates to `G.7` and visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` / `EmitEditionBumpLog` (publication surfaces governed by this pattern)

**4.3.4 Execution + audit.**
Execute planned actions as Work (or Work-bound audit) and publish `RefreshReport@Context`.
Gating outcomes (admit / degrade / abstain) follow `G.Core` tri-state semantics and are recorded via policy ids and cited evidence paths, rather than as local bespoke statuses.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped pack, parity report, evidence path, dashboard slice, fairness audit, policy evaluation, or selector surface consumes `C.28`, refresh planning includes causal-use sentinel causes when they can change supported use, unsupported use, support verdict, or downstream assurance:

| Causal-use sentinel | Typical affected support | Refresh payload pins |
| --- | --- | --- |
| counterfactual-realizability shift | `CounterfactualSamplingRealizabilityProfile`, `realizedCounterfactualSampleSupportBasis`, causal evidence design | profile refs, action-primitive refs, work-plan refs, physical, ethical, and operational constraint refs, target counterfactual distribution refs, admissible-use refs, and unadmissible-use refs |
| counterfactual-data identification/bounding shift | `CausalIdentificationProfile`, `identifiedCounterfactualEstimateSupportBasis`, bounds/partial-identification posture | available data regime set refs, realized counterfactual data refs, counterfactual-data identification method refs, counterfactual-data bound refs, assumption refs |
| target-trial reporting shift | `TargetTrialProtocolRecord`, `TargetTrialEmulationMappingRecord`, applied intervention-effect support | protocol refs, observational data source refs, eligibility, treatment, time-zero, and assignment mappings, follow-up and outcome mappings, emulation-gap refs, residual-confounding and sensitivity refs and additional-analysis refs |
| causal-fairness shift | `CausalFairnessUseAuditCard`, causal fairness support verdict, fairness assurance | protected-variable refs, decision-variable refs, and outcome-variable refs, permitted-path refs and prohibited-path refs, fairness estimand refs, causal-use question refs, support basis refs, support record refs and verdict refs |
| causal-representation-validation shift | `CausalVariableRepresentationRecord`, learned causal variable support | intervention-validity, mechanism-invariance, abstraction-fidelity, counterfactual-query-preservation, representation-shift refs, OOD refs, supported-causal-variable-use refs, and unsupported-causal-variable-use refs |
| off-policy or causal-RL evaluation shift | `OffPolicyCausalEvaluationProfile`, causal action-policy support, policy parity | behavior-policy refs and evaluation-policy refs, sequential horizon refs, adaptive policy class refs, unit-history conditioning refs, overlap refs and support refs, policy transportability refs, estimator and uncertainty refs |
| simulation-validation shift | `simulationOnlyCounterfactualOutputBasis`, bounded model-supported counterfactual use | counterfactual model assumption refs, simulation validation refs, `CausalUseSupportStatement` / `CausalUseUnsupportedStatement` refs, sensitivity and rival-cause refs |

These sentinels do not mint new `RSCRTriggerKindId` values. They are domain-facing payload distinctions carried under the canonical trigger kinds governed by `G.Core`, usually evidence-surface edit, edition-pin change, policy-pin change, telemetry delta, freshness/decay event, or tokenization/name change.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

All discipline-specific refresh strategies, scheduling heuristics, and generator-specific wiring live as `GPatternExtension` blocks.

##### G.11:Ext.LegacyTriggers

**PatternScopeId:** `G.11:Ext.LegacyTriggers`
**GPatternExtensionId:** `LegacyTriggers`
**GPatternExtensionKind:** `InteropSpecific` (alias docking)
**GoverningPatternId:** `G.Core`
**Uses:** `{G.Core}` (cites `G.Core.TriggerAliasMap.G11`)
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `RSCRTriggerKindId[]` (canonical ids recorded on triggers)
* `RSCRTriggerAliasId?` (e.g., `G.11:T0…T7` as labels only)
* `scope: PathSliceId[] | PatternScopeId`

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidenceSurfaceEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (freshness/decay semantics)
**Uses:** `{B.3.4, G.6}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `FreshnessWindowDeclRef` (or equivalent window pin, as defined by the governing definition)
* `DecayPolicyIdRef` / `EpistemicDebtBudgetRef` (policy-bound)
* `PathSliceId[]` (affected evidence carriers)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidenceSurfaceEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** Any budget/priority logic remains policy-bound; `G.11` only wires decay events to refresh planning.

##### G.11:Ext.QDRefreshWiring

**PatternScopeId:** `G.11:Ext.QDRefreshWiring`
**GPatternExtensionId:** `QDRefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` (QD semantics; descriptor/distance/insertion)
**Uses:** `{C.18, C.19, G.5, G.8}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `DescriptorMapRef.edition`, `DistanceDefRef.edition`
* `CharacteristicSpaceRef.edition?` (required when a domain-family coordinate is declared by the QD governing definition)
* `InsertionPolicyRef`, `EmitterPolicyRef` (policy-bound)
* `PathSliceId` (archive/illumination scope) + `policy-id` for emitted telemetry triggers

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.

##### G.11:Ext.OEERefreshWiring

**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration / E–E logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the governing patterns)
* `GeneratorFamilyId` / `TransferRulesRef` wiring pins (as published by the governing definitions)
* telemetry scope pins (`PathSliceId`, `policy-id`)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:Ext.SchedulingHeuristics (Phase-3 seed)

**PatternScopeId:** `G.11:Ext.SchedulingHeuristics`
**GPatternExtensionId:** `SchedulingHeuristics`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected`
**Uses:** `{G.11}`
**⊑/⊑⁺:** `∅`
**RequiredPins / EditionPins / PolicyPins (minimum):**

* `RefreshPriorityPolicyIdRef` (policy-bound)
* `BudgetDeclRef` (time/compute/cost/risk ceilings; policy-bound)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.MaturityRungChange}`
**Notes (seed, non-normative):** Scheduling strategies (bandit-style, queueing, cadence policies) are valuable but must not become Part‑G‑wide norms.

### G.11:5 - Archetypal Grounding — System / Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump + calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices (paths) and publishes a refresh report with pins to the updated standard edition and the evidence paths. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by governing pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims + parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL/plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

### G.11:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions/policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: the kit is intentionally thin (queue/plan/report), while action semantics remain delegated to governing definitions.
* **Onto/Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System+Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose / Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion + explicit deltas; delegated to `G.Core`).                                                                                                                                       | Phase‑2 bridge clause: `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD/OEE wiring).**     | When QD and/or OEE are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin/edition/policy wiring of the applicable extension blocks (`G.11:Ext.QDRefreshWiring` and/or `G.11:Ext.OEERefreshWiring`). **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while moving method‑specific pin lists into `Extensions` (Phase‑2 modularity).                  |
| **CC‑G11.3 (Telemetry‑metric legality).**             | If a refresh publishes Illumination/QD/OEE outcomes, it **SHALL** publish **Q/D/QD‑score** (and any coverage/regret) as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy‑id SHALL be recorded** in SCR‑visible evidence bindings (via the cited governing patterns).                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge/plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL/CL^k/CL^plane` and the relevant `Φ/Ψ/Φ_plane` policy‑ids with loss notes so penalties route to `R_eff` only (F/G invariant).                                                                                                                                | Keeps penalty routing auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set/archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (Pareto/Archive) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross‑context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef` + BridgeCard + UTS + `CL/Φ_plane` policy‑ids. Missing/non‑conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness/decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh / Deprecate / Waive**) with **budget notes** (policy‑bound), and **SHALL** publish the decision via `DeprecationNotice@Context` (and related pins) and SCR‑visible evidence bindings (via `G.6` / cited governing patterns).                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`/dominance/Γ‑fold/guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition (via `G.Core.DefaultGoverningDefinitionIndex` and the applicable governing patterns) rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re‑shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR/regression check for the affected scope and record `RSCRRefs[]` (or equivalent) in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade/abstain` outcomes (policy‑bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice‑scoped.                                         |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed surface consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification/bounding, target-trial reporting, causal fairness, causal representation validation, off-policy/causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped support while preserving `G.Core` trigger governance. |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases via `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context or plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins + E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance/PortfolioMode behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Debt-by-prose**                  | “We decided not to refresh” exists only in narrative              | Not comparable; cannot be tested                         | Emit a DeprecationNotice (incl. a Waive outcome, if used) with pins (CC‑G11.7)    |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning/execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear governing-definition assignment boundaries.** Orchestration coordinates governing definitions; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids/editions/policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop is powerful enough to coordinate reruns and republishing, but **too thin to become a second spec**. That is why trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W seam** so that WorkPlanning plan items remain planning references and executed work remains auditably executed work.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring + retraining / reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (2017); Amershi et al., *Software Engineering for Machine Learning* (2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition/policy pins for replay.
   Adoption: **Adopt/Adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift/decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (2019); De Lange et al., *A Continual Learning Survey* (2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor/distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy/edition conditions.
   Source: contemporary QD families such as CMA‑ME (post‑2018) and differentiable QD lines (post‑2019).
   Alignment: QD-specific meaning lives with the governing patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set/archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (2019) and subsequent POET extensions (2020+).
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt/Adapt** (adapted to Part‑G pin/UTS publication discipline).

5. **Efficient orchestration benefits from bandit/early-stopping scheduling—but it must not become semantics.**
   Practice: modern hyperparameter/experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: Async Hyperband / BOHB-style work (2018+) as representative post‑2015 scheduling practice.
   Alignment: scheduling lives as policy-bound extension (`G.11:Ext.SchedulingHeuristics`) so core semantics remain stable.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; Default Governing Definition Index), `G.6` (EvidenceGraph, `PathId/PathSliceId`), `G.7` (Bridge sentinels; CL/Φ/plane pins), `G.5` (selector & set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness/decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), optional `C.18 and C.19` (QD/E–E pins), `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support records and SoTA-sensitive causal-use sentinel payloads), `F.15` (RSCR harness surfaces, when present).
**Publishes to:** UTS (refresh plan/report, deprecations, edition bumps), and to the relevant governing patterns’ publication surfaces via delegated actions.

### G.11:End


## G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)

**Tag:** Architectural kit pattern (conceptual; notation‑independent; dashboard‑kit governing definition)

**Stage:** design‑time authoring **→** run‑time computation & publication (series and slices); **refresh/RSCR‑wired**

**Primary hooks:** **G.Core** (core invariants, linkage catalogues, RSCR trigger catalogue, Default Governing Definition Index), **C.21** (DHC slots + `DHCPack` / `DHCMethodSpec` / `DHCSeries` artefacts), **G.6** (EvidenceGraph; `PathId`/`PathSliceId` citation), **G.7** (Bridge calibration / CL & `Φ/Ψ/Φ_plane` policy surfaces; when crossings/plane routing is used), **G.11** (telemetry‑driven refresh/decay orchestration), **G.5** (selector set-surface / set‑returning outputs, when dashboard consumes performance trade‑offs), **A.19** (CN‑Spec governance card), **G.0** (CG‑Spec legality gate), **F.17/F.18** (UTS + twin labels), **E.5.2** (notation independence), **E.10** (LEX discipline).
*(Optional, extension‑gated hooks:* **G.2** (SoTA palette & DHC alignment hooks), **C.18 and C.19** (QD / E‑E / OEE telemetry pins), **G.8** (SoS‑LOG bundle & maturity ladder view), **G.10** (shipping inclusion of dashboard slices).)*

**Why this exists.** **C.21** defines *what* lawful “discipline health” slots are (CHR‑typed; scale/legality aware; freshness‑windowed), but it does not, by itself, provide a **generation‑first** method for producing **edition‑pinned, evidence‑citable DHC time series** that remain refreshable under RSCR.
**G.12** is that dashboard method: it defines the **dashboard kit surfaces** (`DHCSeries@Context`, `DHCRow@Context`, `DashboardSlice@Context`, telemetry pins) and a pipeline for computing and publishing DHC readings **without shadow specs**, **without illicit arithmetic**, and **without smuggling scalar winners** out of partial orders or telemetry.

**Modularity note.** G.12 governs **dashboard publication units and wiring** only. It **does not** govern CN-Spec, CG-Spec, CHR, CAL, selection semantics, evidence semantics, shipping, or refresh heuristics. It binds to those governing definitions via refs/pins/editions/policy‑ids and keeps any method‑/generator‑specific panels strictly inside **Extensions** (`GPatternExtension` blocks).

### G.12:1 — Intent

Produce **admissible, reproducible, refresh-aware discipline-health dashboards** by turning **C.21** DHC definitions into:

1. a **UTS‑published** time series (`DHCSeries@Context`) whose rows are evidence‑citable by **`PathId`/`PathSliceId`**,
2. a dashboard slice view (`DashboardSlice@Context`) that is **view‑only** (no hidden re‑aggregation or “new objectives”), and
3. **telemetry pins** that allow **G.11** to plan **slice‑scoped refresh** (rather than “rerun everything”).

### G.12:2 — Problem frame

Dashboards routinely drift or become illegal when they:

* mix scales (ordinal treated as interval; “average maturity level”),
* hide normalization and re‑parameterization (“normalized score” with no CN‑Spec pins),
* silently cross Contexts or planes (implicit reuse without explicit Bridge/Plane routing),
* fail to pin editions of computation methods, descriptor spaces, or distances,
* turn selected sets or archives into a single scalar “winner” by dashboard fiat,
* cannot refresh selectively (no actionable telemetry pins; only narrative “this changed”).

We need a **dashboard kit** that makes the *method of obtaining dashboard values* explicit and auditable, while keeping universal invariants governed in **G.Core**.

### G.12:3 — Forces

* **Legality and comparability are governed by CN-Spec and CG-Spec.** Dashboards must not invent local legality/acceptance/normalization “mini‑specs”; they pin and cite **CN‑Spec** and **CG‑Spec** surfaces as required by **G.Core** conformance.
* **Ordinal discipline is non‑negotiable.** The most common dashboard failure mode is illicit arithmetic on ranks/categories; the kit must make “compare‑only” enforceable.
* **Set‑returning discipline survives into views.** Dashboards must not silently scalarize partial orders or selector selected-set surfaces; any scalarization/promotion is an explicit governing-pattern policy cited through **G.Core** conformance; semantics are governed by the relevant pattern or policy.
* **Edition‑awareness is the difference between “trend” and “drift”.** If the method definition changes, the dashboard must either (i) fork series edition, or (ii) emit telemetry and refresh slices under pinned conditions.
* **RSCR must be actionable.** Causes are emitted as **canonical ids** (typed trigger kinds + id‑valued pins), not prose.

### G.12:4 — Solution — Compute and publish DHC series admissibly, with RSCR-ready telemetry

#### G.12:4.0 — G.Core linkage (normative)

This pattern is **core‑invariant‑bearing** and therefore binds to **G.Core** by declaration (not by restating invariants here).

**GCoreLinkageManifest (G.12)** *(normative; expands per `G.Core:4.2`)*
Effective obligations/pins/triggers are computed as **union(expand(sets), explicit deltas)** under `Nil‑elision`.

* `CoreConformanceProfileIds` := {
  `GCoreConformanceProfileId.PartG.AuthoringBase`,
  `GCoreConformanceProfileId.PartG.TriStateGuard`,
  `GCoreConformanceProfileId.PartG.UTSWhenPublicIdsMinted`,
  `GCoreConformanceProfileId.PartG.ShippingBoundary`
  }

* `RSCRTriggerSetIds` := {
  `GCoreTriggerSetId.BridgeCalibrationKit`
  }

* `RSCRTriggerKindIds` := {
  `RSCRTriggerKindId.LegalitySurfaceEdit`
  }
  *(Any additional causes required by optional dashboard panels MUST be introduced only by the corresponding `GPatternExtension` blocks in `G.12:4.9`.)*

* `DefaultsConsumed` := `∅`
  *(Default-citation discipline for `DefaultId.PortfolioMode` and `DefaultId.DominanceRegime` is only relevant when selection outputs with `PortfolioMode` are consumed; see `G.12:Ext.PortfolioTelemetry`.)*

* `CorePinSetIds` := {
  `GCorePinSetId.PartG.AuthoringMinimal`,
  `GCorePinSetId.PartG.CrossingVisibilityPins`
  }

* `CorePinsRequired` *(pattern delta; pin names only; all are id‑valued unless noted)* := {
  `DHCSeriesId`,
  `TargetSlice` *(USM tuple; varies only by `Γ_time` across rows; no implicit “latest”)*,
  `Γ_time` *(time selector / freshness window; required per row; series MAY additionally declare a window‑family spec)*,
  `DHCSlotId[]` *(typed DHC slots governed by C.21; each resolves to `CharacteristicId` + scale/unit/polarity + reference plane binding + lane discipline)*,
  `DHCMethodSpecRef.edition`,
  `DHCMethodRef.edition`,
  `PathSliceId[]`
  }
  *(Nil‑elision applies. All other definition pins are conditional: they MUST appear only when actually used and when their governing pattern/extension is present (e.g., UNM/normalization pins, QD/OEE telemetry pins, transfer rules pins, pack inclusion pins).)*

* `TriggerAliasMapRef` := `∅`

#### G.12:4.1 — Objects (LEX heads; twin‑register discipline)

All objects below are **notation‑independent**; serialisations (if any) live under shipping or interop governance, not here.

**(1) `DHCSeries@Context`** *(UTS‑published dashboard series; C.21‑grounded)*
A time‑indexed publication of computed DHC readings for a `Discipline × ContextSlice`, aligned with `U.DHCSeries` semantics from **C.21** and pinned to method/governing spec refs.

Minimal fields (conceptual; ids/pins only):

`DHCSeries@Context := ⟨
  DHCSeriesId,
  CG-FrameContext,
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  TargetSlice,                         // USM tuple; time series varies Γ_time across rows (explicit, no implicit “latest”)
  DHCSlotId[],                         // slot set selected from C.21 (typed DHC slots; not “just Characteristic ids”)
  DHCPackRef.edition?,
  DHCMethodSpecRef.edition,
  WindowSpec?,                         // optional window-family spec used to generate per-row Γ_time
  CNSpecRef.edition, CGSpecRef.edition,
  EvidenceGraphId?,                    // if resolvable; else row-level Path pins suffice
  DashboardSliceId[]?,                 // published view slices (optional)
  TelemetryPinSetId?                   // wiring to refresh (conceptual)
⟩`

**(2) `DHCRow@Context`** *(one timepoint / window reading; Work/Audit‑citable)*
A single computed row of the series.

`DHCRow@Context := ⟨
  DHCRowId,
  DHCSeriesId,
  Γ_time,
  DesignRunTag = run,
  DHCSlotId,
  value, units/scaleRef?, compareOnly?,
  stance ∈ {pass|degrade|abstain},
  DHCMethodRef.edition, DHCMethodSpecRef.edition,
  PathSliceId[], PathId[]?, EvidenceGraphId?,
  evidenceLaneTags? := {TA|VA|LA},
  crossingPins? := ⟨BridgeId[], PlaneMapRef.edition?, CL/CL^k/CL^plane?, Φ/Ψ/Φ_plane policy‑ids…⟩
⟩`

**(3) `DashboardSlice@Context`** *(view; non‑semantic)*
A view‑friendly grouping over one or more series/rows. It MUST NOT introduce new aggregation/legality semantics; it is a projection over already computed, pinned, citable rows.

`DashboardSlice@Context := ⟨
  DashboardSliceId(UTS),
  DHCSeriesId(UTS)[],
  SliceAnnotations?,                  // labels, grouping metadata, explanatory text
  ViewSpecId?,                        // view template id (policy‑bound; no semantics implied)
  IncludedRowIds?
⟩`

**(4) `DHCTelemetryPin`** *(refresh wiring pin; id‑based causes)*
A conceptual telemetry pin emitted to refresh/orchestration (governed by **G.11**) with canonical trigger kind ids.

`DHCTelemetryPin := ⟨
  triggerKindId: RSCRTriggerKindId,
  scope: PathSliceId[] | PatternScopeId,
  payloadPins: { …ids… }              // editions, policy‑ids, UTS row ids, window ids, etc.
⟩`

**Ref discipline.** `.edition` SHALL appear only on `…Ref` (per **E.10**). Dashboard artefacts that mint public ids publish **Tech/Plain twins** (UTS discipline).

#### G.12:4.2 — Method‑of‑Obtaining Output (generation‑first; design‑time → run‑time)

**Stage A — Author & bind (design‑time)**

A1. **Select the DHC slot set (governed by C.21).**
Choose `DHCSlotId[]` from **C.21** (typed DHC slots), and declare the series scope explicitly as `TargetSlice` (USM tuple) plus an explicit time selector (`Γ_time` per row; optionally a `WindowSpec` that generates the row windows). Do not restate slot semantics in the dashboard kit; cite the C.21 governing definitions.

A2. **Bind governance card and legality gate (governing definitions: A.19, G.0).**
Pin `CNSpecRef.edition` and `CGSpecRef.edition`. Any normalization or numeric comparability assumptions are expressed by explicit CN‑Spec artefacts (ids/refs) and any numeric legality requirements cite CG‑Spec artefacts (SCP / MinimalEvidence / Γ‑fold pins as applicable). The dashboard does not introduce local “shadow specs”.
If the dashboard series/slice actually uses cross‑Context or cross‑plane routing, it MUST additionally pin the relevant crossing and penalty‑policy surfaces as ids (Bridge/CL/plane ids, `Φ/Ψ/Φ_plane` policy‑ids, `PlaneMapRef.edition?`) and cite their governing patterns (typically `G.7` for bridge calibration/CL kits, pinned through `G.Core`). The dashboard MUST NOT encode a dashboard‑local “penalty regime”.

A3. **Pin computation methods (governed by C.21).**
For each slot/method used to compute a time series value, record `DHCMethodSpecRef.edition` and `DHCMethodRef.edition` (table‑backed, per C.21). The dashboard series is edition‑aware: if a method spec changes, the dashboard either forks the series edition or emits telemetry and refreshes under explicit pins.

A4. **Declare optional panels via Extensions only.**
If the dashboard depends on (i) selector set-surface outputs, (ii) QD illumination / archive telemetry, (iii) open‑endedness telemetry, (iv) maturity ladder views, or (v) pack inclusion, then the relevant `GPatternExtension` block(s) in `G.12:4.9` MUST be present and their pins MUST be satisfied.

**Stage B — Compute rows (run‑time; Work/Audit)**

B1. **Resolve evidence by Path (governed by G.6).**
Compute rows from evidence cited as `PathSliceId[]` (and `PathId[]` when needed), under the declared window/freshness regime. Preserve lane discipline and handle missingness using tri‑state stances governed by **G.Core**.

B2. **Compute slot values using pinned methods (governed by C.21).**
Compute each slot value by applying the pinned `DHCMethodRef.edition`/`DHCMethodSpecRef.edition` under the pinned governance card and legality gate. Enforce “no illicit arithmetic” for ordinals/categoricals as a dashboard‑kit obligation (see CC‑G12.\*).
Any cross-Context or cross-plane use is expressed only via explicit crossing pins (Bridge/Plane routing) and policy ids governed by **G.Core**.

B3. **Emit RSCR‑actionable telemetry pins (governing definition: G.11).**
When any of the declared pins/editions/policies/windows/evidence slices change, emit `DHCTelemetryPin` events with canonical `RSCRTriggerKindId` and payload pins sufficient for **slice‑scoped** refresh planning.

**Stage C — Publish series & slices (run‑time; publication)**

C1. **Publish `DHCRow@Context` and `DHCSeries@Context` as UTS publication units.**
Mint/publish UTS rows with Tech/Plain twins and include the required pins (window, reference plane, method editions, evidence paths).

C2. **Publish `DashboardSlice@Context` as a view‑only projection.**
Slices are groupings/annotations over already computed rows; they must not redefine legality, acceptance, or scalarization.

C3. **Wire refresh via telemetry pins (no orchestration governance).**
Dashboards emit pins; refresh orchestration remains governed by **G.11**.

#### G.12:4.9 — Extensions (pattern‑scoped; non‑core)

> **Extension rule (Phase‑2).** Anything method‑, generator‑, or view‑family‑specific belongs here, as `GPatternExtension` modules. These modules may add **mode‑specific definition pins** and additional RSCR trigger kinds, but MUST NOT redefine Part‑G‑wide invariants or defaults.

##### `G.12:Ext.SoTAPalette` — SoTA palette & DHC alignment hooks (optional)

**PatternScopeId:** `G.12:Ext.SoTAPalette`
**GPatternExtensionId:** `SoTAPalette`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.2` *(SoTA palette + DHC alignment hooks semantics are governed by G.2; G.12 only wires them)*
**Uses:** `{G.2}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTA_PackRef.edition?`
* `DHC-SenseCellId[]?` *(when series pins to DHC alignment hooks / sense‑cell inventories)*
* `DHCAlignmentHookId[]?`

**RSCRTriggerKindIds (delta):** `∅`

##### `G.12:Ext.PortfolioTelemetry` — selector set-surface integration panel

**PatternScopeId:** `G.12:Ext.PortfolioTelemetry`
**GPatternExtensionId:** `PortfolioTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `G.5` *(`PortfolioMode` citation plus selected-set semantics and set‑return discipline)*
**Uses:** `{G.5, G.6}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TaskSignatureRef?` *(when `PortfolioMode` semantics depend on TaskSignature traits)*
* `DominanceRegime` *(cite the governing definition for `DefaultId.DominanceRegime`; publish the resolved regime, do not invent a local default)*
* `PortfolioMode` *(cite the governing definition for `DefaultId.PortfolioMode`; publish the resolved mode)*
* `SCRId/DRRId` *(or equivalent selector evidence pins, when dashboard row depends on selector outcomes)*

**DefaultsConsumed:** {`DefaultId.DominanceRegime`, `DefaultId.PortfolioMode`} *(cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex`; no local defaults)*

**RSCRTriggerKindIds (delta):** `∅` *(base triggers suffice; any extra triggers must be explicit)*

**Notes (wiring‑only):**

* The dashboard may visualise selected-set / Archive telemetry, but MUST keep set‑returning semantics; any scalar “headline number” is a view projection, not a legality‑bearing decision.

##### `G.12:Ext.QDTelemetry` — illumination / archive telemetry panel

**PatternScopeId:** `G.12:Ext.QDTelemetry`
**GPatternExtensionId:** `QDTelemetry`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.18` *(QD / NQD‑CAL semantics; descriptor/distance/insertion policy)*
**Uses:** `{C.18, G.5, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `DescriptorMapRef.edition`
* `DistanceDefRef.edition`
* `CharacteristicSpaceSpecRef.edition?` *(iff the descriptor or characteristic space is editioned as a published surface; required for view reproducibility)*
* `InsertionPolicyRef`
* `EmitterPolicyRef?`
* `ArchiveSnapshotRef?` *(id/pin for the published archive snapshot, if any)*
* `PathSliceId[]` *(scope for refresh; slice‑keyed)*

**RSCRTriggerKindIds (delta):** `∅` *(base trigger set already includes `RSCRTriggerKindId.TelemetryDelta`; add only genuinely additional kinds here)*

**Notes (wiring‑only):**

* Illumination/coverage signals are treated as telemetry. Any promotion of telemetry into selection dominance is governed elsewhere (typically CAL policy; pinned through `G.Core`).
* If descriptor characteristics are surfaced as published identifiers (not just local UI text), they MUST follow the Tech/Plain twin-label discipline (UTS Name Cards); otherwise they remain non-normative view annotations.

##### `G.12:Ext.OpenEndedTelemetry` — open‑endedness / transfer telemetry panel

**PatternScopeId:** `G.12:Ext.OpenEndedTelemetry`
**GPatternExtensionId:** `OpenEndedTelemetry`
**GPatternExtensionKind:** `GeneratorSpecific`
**GoverningPatternId:** `C.19` *(E/E‑LOG & exploration accounting; generator/transfer telemetry wiring)*
**Uses:** `{C.19, G.5, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `TransferRulesRef.edition` *(when transfer rules are part of the telemetry interpretation)*
* `EnvironmentValidityRegionId?`
* `ProbeBudgetPolicyId?`
* `PathSliceId[]`

**RSCRTriggerKindIds (delta):** `∅` *(base trigger set already includes `RSCRTriggerKindId.TelemetryDelta`; add only genuinely additional kinds here)*

**Notes (wiring‑only):**

* Open‑endedness metrics are telemetry‑level artefacts; dashboards must not silently convert them into “dominance objectives”.

##### `G.12:Ext.MaturityLadderPanel` — maturity ladder view (optional)

**PatternScopeId:** `G.12:Ext.MaturityLadderPanel`
**GPatternExtensionId:** `MaturityLadderPanel`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `G.8` *(maturity ladder semantics in SoS‑LOG bundle/maturity cards)*
**Uses:** `{G.8, G.6, G.11}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `MaturityCardRef`
* `MaturityRungId?`
* `PathId/PathSliceId` *(evidence citations for rung claims)*

**RSCRTriggerKindIds (delta):** `{RSCRTriggerKindId.MaturityRungChange}`

##### `G.12:Ext.PackInclusion` — shipping inclusion stub (optional)

**PatternScopeId:** `G.12:Ext.PackInclusion`
**GPatternExtensionId:** `PackInclusion`
**GPatternExtensionKind:** `InteropSpecific`
**GoverningPatternId:** `G.10` *(shipping semantics are governed by G.10)*
**Uses:** `{G.10}`
**⊑/⊑⁺:** `∅`

**RequiredPins/EditionPins/PolicyPins (minimum):**

* `SoTA‑PackId`
* `DashboardSliceId(UTS)` *(or `DHCSeriesId(UTS)` when shipping series directly)*
* `CNSpecRef.edition`, `CGSpecRef.edition` *(as shipped pins, per G.10 wiring)*

**RSCRTriggerKindIds (delta):** `∅`

**Notes (wiring‑only):**

* This module is a wiring stub: it does not define shipping behaviour; it only states which dashboard artefacts may be cited by `SoTA‑Pack(Core)`.

##### `G.12:Ext.ViewFamilySeed` — advanced view families (Phase‑3 seed; governing pattern TBD)

**PatternScopeId:** `G.12:Ext.ViewFamilySeed`
**GPatternExtensionId:** `ViewFamilySeed`
**GPatternExtensionKind:** `Phase3Seed`
**GoverningPatternId:** `governing pattern not yet selected`
**Uses:** `{}`
**⊑/⊑⁺:** `∅`

**Notes (Phase‑3 seed; non‑normative):**

* Placeholder for advanced dashboard view families (e.g., embedding‑based similarity panels, predictive drift detectors, change‑point overlays). Any such module must remain policy‑bound and must not introduce new Part‑G‑wide norms.

### G.12:5 — Interfaces (conceptual; kit surface)

| ID  | Interface   | Consumes   | Produces  |
| --- | ----------- | ---------- | --------- |
| **G.12‑1 `Create_DHCSeries`** | Create/bind a DHC series scope (C.21‑grounded; edition‑aware) | `DHCSlotId[]`, `DHCPackRef.edition?`, `DHCMethodSpecRef.edition`, `TargetSlice` (USM), `WindowSpec?`, `ReferencePlane`, `CNSpecRef.edition`, `CGSpecRef.edition` | `DHCSeries@Context` (UTS publication unit; edition‑aware) |
| **G.12‑2 `Update_DHCSeries`** | Compute/update one or more rows under pinned conditions (run‑time; Work/Audit‑citable) | `PathSliceId[]`, `EvidenceGraphId?`, `DHCMethodRef.edition`, `DHCMethodSpecRef.edition`, `Γ_time`, crossing pins (if any) | `DHCRow@Context[]` (UTS publication units; stance and pins; `DesignRunTag = run`) |
| **G.12‑3 `Integrate_PortfolioTelemetry`** *(extension‑gated)* | Integrate selector set-surface evidence into a slice/series | See `G.12:Ext.PortfolioTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑4 `Integrate_QDTelemetry`** *(extension‑gated)* | Integrate QD illumination/archive telemetry | See `G.12:Ext.QDTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑5 `Integrate_OEETelemetry`** *(extension‑gated)* | Integrate open‑endedness / transfer telemetry | See `G.12:Ext.OpenEndedTelemetry` | Extension‑gated fields / telemetry pins |
| **G.12‑6 `Publish_DashboardSlice`** | Publish a view slice as a projection over computed rows | `DHCSeriesId(UTS)[]`, `DHCRowId(UTS)[]?`, `SliceAnnotations?` | `DashboardSlice@Context` (UTS publication unit; view‑only) |
| **G.12‑7 `Emit_TelemetryPins`** | Emit RSCR‑actionable telemetry pins for refresh | `RSCRTriggerKindId`, `scope`, `payloadPins` | `DHCTelemetryPin[]` (consumed by `G.11`) |

(*No file formats are introduced here; serialisation recipes live under shipping or interop governance.*)

### G.12:6 — Conformance checklist (CC‑G12, normative)

| CC ID   | Requirement  | Verification notes  |
| ------- | ------------ | ------------------- |
| **CC‑G12‑CoreRef** | The pattern satisfies the **effective** `G.Core` obligations declared by `GCoreLinkageManifest (G.12)` (profiles/sets/deltas expanded per `G.Core:4.2`).    | Evidence: the manifest is present; required pins/defaults/triggers are accounted for; no local restatement overrides core governing definitions.  |
| **CC‑G12.1** | **DHC slot typing (C.21‑grounded).** Every published dashboard value is indexed by a **C.21‑authored** `DHCSlotId` (typed DHC slot: `CharacteristicId` + scale/unit/polarity + reference plane binding + lane discipline) and is scoped by an explicit `TargetSlice` + `Γ_time`. | Evidence: row/series references `DHCSlotId` and pins `ReferencePlane` and `Γ_time` (or a series `WindowSpec` that yields row Γ_time). |
| **CC‑G12.2** | **Edition discipline (no drift).** Every published time‑series value carries `DHCMethodRef.edition` and any other definition‑pins actually used to obtain it (e.g., `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `UNM_id`, `NormalizationMethodInstanceId[]`, `ComparatorSetRef.edition?`). No free‑text versioning. | Check that `.edition` appears only on `…Ref`; check presence of all definition pins used by the pipeline; extension pins appear only when their extension blocks are present. |
| **CC‑G12.3** | **Spec citation for numeric operations (no shadow specs; no illicit arithmetic).** Any numeric operation in the dashboard pipeline is legal only under explicit **CG‑Spec** and **CN‑Spec** pins (e.g., `SCPRef.edition`, `MinimalEvidenceRef.edition`, `ΓFoldRef.edition?` when used), and any normalization is explicit (`UNM_id` + `NormalizationMethodInstanceId[]` etc). Ordinal/categorical slots remain **compare‑only** (no illicit arithmetic). | Check that operations cite pinned governing definitions; reject “normalize, then compare” without explicit UNM pins; reject arithmetic over ordinal slots unless the governing definition declares an admissible mapping. |
| **CC‑G12.4** | **Set‑returning selection is preserved.** If the dashboard consumes selection / set-surface outputs, it MUST preserve set‑return semantics and MUST publish the resolved `DominanceRegime` and `PortfolioMode` by citing each default's governing definition (via `G.Core.DefaultGoverningDefinitionIndex`) rather than inventing local defaults. Any promotion of illumination/telemetry into dominance MUST cite the governing-pattern policy (typically CAL) and be auditable via evidence paths. | Check for set-surface outputs; check that any scalar headline is view‑only; check citations to default governing definitions/policies. |
| **CC‑G12.5** | **UTS publication discipline.** `DHCSeries@Context` and its rows (and any published slices) are published as UTS publication units with Tech and Plain twins plus stable identifiers; deprecations and edition bumps follow the canonical UTS discipline. | Check stable ids and twin labels; check that publication does not smuggle `GateDecision` values as authoritative UTS publication content. |
| **CC‑G12.6** | **Bridge/plane routing is explicit when used.** If a series crosses contexts or planes, the rows MUST cite the Bridge/PlaneMap routing (`BridgeId[]`, `CL/CL^k/CL^plane`, `Φ/Ψ/Φ_plane policy‑ids`, `PlaneMapRef.edition?`) and respect penalty routing to `R_eff` only (semantics pinned through `G.Core`). | Check presence of crossing pins when contexts or planes differ; check that any loss is expressed via R‑lane impact only. |
| **CC‑G12.7** | **Telemetry sufficiency for slice‑scoped RSCR.** Emitted dashboard telemetry pins MUST (i) use canonical `RSCRTriggerKindId`, (ii) include `scope` (PathSliceId[] or PatternScopeId) and the touched `…Ref.edition`/policy/window pins, and (iii) block publication when required pins are missing. Each published row is evidence‑citable by `PathSliceId[]` under explicit `Γ_time`. | Check: no free‑text causes; payload includes path/window/editions/policies; missing pins block publish; row has PathSliceId[] and Γ_time. |
| **CC‑G12.8** | **Extension gating.** If any fields and pins governed by the extension appear, the corresponding `G.12:Ext.*` module is present and satisfied. | E.g., QD pins require `G.12:Ext.QDTelemetry`; maturity panel requires `G.12:Ext.MaturityLadderPanel`; SoTA palette hooks require `G.12:Ext.SoTAPalette`; pack inclusion requires `G.12:Ext.PackInclusion`. |

### G.12:7 — Bias‑Annotation (informative)

* **Didactic:** dashboard publication units publish pins and paths first; views second.
* **Architectural:** no “dashboard‑local governing spec refs”; invariant citation is via `G.Core`.
* **Pragmatic:** slice‑scoped refresh is enabled by canonical trigger ids + payload pins.
* **Epistemic:** compare‑only ordinals and explicit provenance prevent “trend‑as‑drift”.

### G.12:8 — Consequences

* **Dashboards become reproducible artefacts, not screenshots.** A `DHCRow@Context` is re‑derivable under pinned editions and evidence windows.
* **Selective maintenance becomes possible.** Telemetry pins let `G.11` refresh what changed (path slice / window / method edition), rather than rerunning the entire pipeline.
* **Illicit scalarization is structurally discouraged.** Set‑returning and CN/CG-governed semantics are preserved into the dashboard layer.

### G.12:9 — Relations

**Builds on:** `G.Core`, `C.21`, `G.6`, `G.11`, `A.19`, `G.0`, `F.17/F.18`, `E.5.2`, `E.10`.
**Coordinates with:** `G.5` *(when selector set-surface outputs are consumed)*, `G.7` *(when crossings/plane routing or `CL/Φ/Ψ/Φ_plane` policy pins are used)*, `G.8` *(when maturity ladder view is included)*, `G.10` *(when dashboard slices are shipped)*.
**Constrains:** dashboard consumers: dashboards are projections over pinned, evidence‑citable rows; they do not mint new governing-spec semantics.

### G.12:10 — Author’s quick checklist

1. Declare the dashboard series scope: `TargetSlice` (USM tuple), `ReferencePlane`, and an explicit `Γ_time` regime (per‑row; optionally a `WindowSpec` that yields the row windows).
2. Select `DHCSlotId[]` and cite **C.21** (do not restate slot semantics).
3. Pin `DHCMethodSpecRef.edition` and `DHCMethodRef.edition` for every computed slot/value (plus any other definition pins actually used).
4. Ensure rows are evidence‑citable by `PathSliceId[]` and include explicit `Γ_time` (row is run‑time: `DesignRunTag = run`).
5. Publish UTS publication units with twins and the required pins.
6. Emit canonical telemetry pins (`RSCRTriggerKindId` + scope + payload pins) for `G.11`.
7. If SoTA palette hooks / selection / QD / OEE / maturity / shipping panels are needed, add the corresponding `G.12:Ext.*` blocks and satisfy their pins.

### G.12:11 — Worked micro‑examples (informative; SoTA‑oriented)

**(A) Decision‑making discipline dashboard (multi‑tradition).**
Slots (from **C.21**): *ReproducibilityRate* (freshness‑windowed), *StandardisationLevel* (ordinal), *AlignmentDensity* (bridge density over DHC‑SenseCells), *MetaDiversity* (operator family diversity), *DisruptionBalance* (target‑band metric).
Evidence: citation graphs, benchmark traces, and bridge calibrations are referenced via `PathSliceId[]`.
Optional panels:

* `G.12:Ext.PortfolioTelemetry` to visualise set‑returning method selected sets without forcing a scalar winner.
* `G.12:Ext.QDTelemetry` to include illumination/archive telemetry using modern QD families (e.g., CMA‑ME / policy‑gradient QD variants / surrogate‑assisted illumination lines) as telemetry.

**(B) Evolutionary software architecture dashboard (open‑endedness‑aware).**
Slots: stability/reproducibility metrics, standardisation stages (ordinal), cross‑paradigm alignment density, and disruption balance.
Optional panels:

* `G.12:Ext.OpenEndedTelemetry` to include open‑endedness telemetry (environment diversity / transfer events) using POET‑style and related post‑2015 open‑ended generation families, while keeping such signals in telemetry unless an explicit governing-pattern policy promotes them.

### G.12:End

## G.13 - External Interop Hooks for SoTA Discipline Packs (conceptual)

**Tag.** Architectural kit pattern (conceptual interop kit; notation‑independent; normative when used)
**Stage.** *design‑time registration & alignment* → *run‑time ingestion, telemetry, refresh*
**Primary hooks.** `G.Core` (Part‑G core invariants + trigger catalogue + Default Governing Definition Index), `G.2` (SoTA Synthesis Pack), `G.3` (CHR Pack), `G.4` (CAL Pack), `G.5` (selector & registries), `G.6` (EvidenceGraph + PathId/PathSliceId), `G.7` (BridgeMatrix + CL/planes), `G.8` (SoS‑LOG bundle surfaces), `G.9` (parity harness), `G.10` (shipping), `G.11` (refresh orchestration), `G.12` (dashboards), `A.19` (CN‑Spec), `A.18` (CSLC legality), `G.0` (CG‑Spec), `F.17` (UTS), `F.9` (BridgeCard / CL), `E.17` (publication faces), `E.5.2` (notation independence), `E.18/A.21` (GateCrossing/CrossingBundle checks).

**Status.** Stable (Phase‑2 universalized; `G.Core` linkage explicit)
**Normativity.** Normative when used (when any `G.13` surface is authored/emitted/consumed); informative otherwise.

**Non‑duplication note (Phase‑2 universalization).** This pattern **does not restate** Part‑G‑wide invariants (CN/CG spec-ref governing-definition assignment, crossing visibility, penalty routing, set‑return discipline, typed RSCR triggers, Default Governing Definition Index, Δ‑discipline). Those are governed in `G.Core` and referenced here via the linkage manifest and CC delegations (*cite, don’t duplicate*).

### G.13:1 - Problem frame

FPF already supports lawful characterization, evidence wiring, selector‑side set returns, parity, shipping, dashboards, and refresh. What remains frictionful in practice is **interoperability with external scholarly indexes and discipline repositories** (concept registries, paper/claim graphs, dataset registries, taxonomy stores, “science‑of‑science” indicator feeds), which teams routinely use as *inputs* when authoring a SoTA discipline pack.

Without an explicit **conceptual interop kit**, authors tend to build one‑off pipelines whose “implied semantics” leak into the framework: edition drift becomes invisible, cross‑plane/context reuse becomes implicit, and external signals quietly start acting like a shadow governing spec ref.

`G.13` provides the missing kit: **conceptual registration, alignment, and telemetry hooks** that let external sources be wired into the Part‑G pipeline (**G.2 → G.5 → G.9 → G.10 → G.11**, and optionally **G.12**) while preserving Part‑G invariants via `G.Core`.

### G.13:2 - Problem

External sources publish **claim‑adjacent signals** (citations, concept graphs, “task/method” tags, replication links, dataset usage, disruption‑style indicators, benchmark metadata). These are useful for *generation* (palette building, declared set-surface exploration, candidate bridge discovery), not only for audit. But typical interop practices create predictable failure modes:

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
  `⟨ ExternalIndexId, ProviderName?, ExternalIndexType, CoverageScope, Licence?, ExternalEdition, FreshnessWindow?, describedEntity := ⟨GroundingHolon, ReferencePlane⟩, Notes? ⟩`

  **Intent.** Create a stable, citable “source card” so downstream artefacts can pin the *card edition* via `ExternalIndexRef.edition`, while the provider snapshot remains visible as `ExternalEdition` (do not echo provider snapshot ids into downstream cards; cite refs instead).

* **`ClaimMapperCard@Context`** — a conceptual “mapping recipe” that yields FPF‑native artefacts from an external source.

  **Shape (conceptual):**
  `⟨ MapperId, ExternalIndexId, MappingPolicyRef, Targets{ClaimSheet|BridgeHints|SoSFeatureSet|UTSProposals}, PlaneMapRef?, ScaleEmbeddingSpecRef?, EvidenceGraphId?, CSLCProofStubs? ⟩`

  **Notes.**

  * This is **not** a shadow legality gate. It is an interop surface that **cites** governing definitions (`A.19`, `G.0`, `G.3`, `G.4`) and publishes the required pins for downstream audit/refresh.
  * When cross‑plane or cross‑context reuse is implicated, the alignment outputs must use the existing crossing bundles (see `G.Core` linkage).
  * Avoid “edition echo”: downstream artefacts cite `ExternalIndexRef.edition` and `ClaimMapperRef.edition` (and optional `PlaneMapRef.edition` / `ScaleEmbeddingSpecRef.edition`) rather than copying snapshot ids/editions as free fields.

* **`SoSFeatureTransform@Context`** — declares how external signals become **CHR‑typed** SoS features (for DHC/dashboard usage and/or SoS‑LOG rule evaluation).

  **Shape (conceptual):**
  `⟨ SoSFeatureTransformId, Inputs{ClaimSheetId[] | ExternalSignalsRef}, SoSFeatureSetId, FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}, ReferencePlane, EvidenceGraphId?, PathSliceId[]?, ProofHooks? ⟩`

  **Notes.**

  * The derivation is a **typing + provenance** surface; it does not introduce new comparators or new governance cards or legality gates.

* **`ScaleEmbeddingSpec@Context`** — optional constraints for representation/space alignment used inside an alignment recipe.

  **Shape (conceptual):**
  `⟨ ScaleEmbeddingSpecId, IntendedUse, AllowedTransformFamily, RequiredPins{NormalizationMethodRef.edition?}, ProhibitedCoercions ⟩`

  **Design intent.** Make any representation alignment *explicitly constrained* and edition‑pinned, instead of silently “creating a new scale”.
  **LEX/UTS note (informative).** `ScaleEmbeddingSpec` is a new LEX head; when it mints a public id it must be published to UTS with twin labels (see `G.Core` / UTS profile).

* **`IndexTelemetryPin`** — an emitted refresh input that makes interop changes RSCR‑visible.

  **Shape (conceptual; RSCR‑typed):**
  `⟨ triggerKindId: RSCRTriggerKindId, scope: PathSliceId[] | PathId[] | PatternScopeId, payloadPins{ExternalIndexId, ExternalIndexRef.edition, ClaimMapperRef.edition?, MappingPolicyRef?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, PathId[]?, PathSliceId[]?, UTSRowId[]?, …} ⟩`

  **Publication.** Emitted to `G.11` as refresh input; recorded with canonical `RSCRTriggerKindId` causes.

* **`InteropSurface@Context`** — a selector-facing or dashboard-facing summary of what interop publications and records exist and how they are pinned.

  **Shape (conceptual):**
  `⟨ InteropSurfaceId, ExternalIndexId, ExternalIndexRef.edition, MapperId?, ClaimMapperRef.edition?, MappingPolicyRef?, SoSFeatureSetId?, EvidenceGraphId?, PathSliceId[]?, PlaneMapRef.edition?, ScaleEmbeddingSpecRef.edition?, UTSRowId[] ⟩`

  **Publication.** Published to UTS with twin labels as applicable.

#### G.13:4.3 - Generation‑first interop flow (notation‑independent; governing-definition delegating)

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source/snapshot used for SoTA authoring, including `ExternalEdition` and the `describedEntity` plane anchor.
2. **Author mapping recipes.** Create `ClaimMapperCard@Context` describing which FPF artefacts are produced (ClaimSheets, BridgeHints, feature sets, UTS proposals), and which policies/specs constrain the mapping (policy refs + optional `PlaneMapRef` / `ScaleEmbeddingSpecRef`).
3. **Produce FPF‑native inputs.** Use the alignment recipe outputs as inputs to:

   * `G.2` harvesting (ClaimSheets / operator & object inventories / candidate bridge hints),
   * `G.3` CHR typing (when numeric signals are formalized as CHR characteristics/scales/coordinates),
   * `G.4` acceptance/threshold policies (when a downstream decision requires explicit CAL policy rather than telemetry),
   * `G.12` dashboards (when derived SoS features are used as DHC slots).
4. **Feed selection/parity/shipping without smuggling semantics.**

   * `G.5` consumes the produced artefacts under its own governing spec refs and returns set‑valued outcomes (selector semantics remain governed by `G.5` + `G.Core`).
   * `G.9` parity consumes pinned editions/windows and produces traceable parity reports.
   * `G.10` shipping may include interop surfaces **as cited publications or records**; `G.13` does not govern shipping.
5. **Emit telemetry and refresh causes.** Any change in external editions, alignment policies, plane maps, or embedding specs emits:

   * a canonical `RSCRTriggerKindId` (per `G.Core`),
   * a scope (`PathSliceId[]` and/or `PatternScopeId`),
   * payload pins (editions/policies/UTS rows),
     enabling `G.11` to plan slice‑scoped refresh.

#### G.13:4.4 - Interfaces — minimal I/O standard (conceptual; kit‑only)

| ID   | Interface   | Consumes  | Produces   |
| ---- | ----------- | --------- | ---------- |
| **G.13‑1 `Register_ExternalIndex`**  | Register `ExternalIndexCard@Context` | Provider metadata, scope, **ExternalEdition**, freshness, describedEntity anchor   | `ExternalIndexCard@Context` (+ UTS row when published)   |
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
Register an external scholarly index edition for “software architecture” concept neighborhoods. Align extracted technique/tactic claims into ClaimSheets and derive a CHR‑typed feature set (e.g., evidence depth, maturity). Use `G.5` to select a **set** of tactics under multi‑objective tradeoffs, and ship a SoTA pack that cites the interop surface.

**Episteme.** *Science‑of‑science discipline dashboard.*
Align external claim graphs (replication, standardisation, disruption‑style proxies) into CHR‑typed features for DHC series. Publish a dashboard slice that cites the external edition and alignment policy; refresh triggers fire when the external edition updates.

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

8. **CC‑G13‑SoSFeaturesAreCHRTypedAndLegal.** *(local; governing-definition citing)* If `SoSFeatureTransform@Context` is used, produced SoS features **MUST** be CHR‑typed via `FeatureTypingRefs{CharacteristicId/ScaleId/CoordinateId}` (governed by `G.3`) and any legality/units obligations must be satisfied via CSLC/CG governing definitions (cite `A.18` / `G.0` / `G.4`; do not invent interop‑local legality gates).

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
* **Generation‑first authoring becomes cheaper.** External sources become controlled inputs into SoTA synthesis and declared set-surface exploration, not ad‑hoc audit decoration.
* **Conceptual hygiene improves.** Explicit cards + edition pins reduce semantic leakage from tools/formats/providers.
* **Cross‑tradition reuse becomes auditable.** Plane/context reuse is surfaced as crossings rather than embedded assumptions.

### G.13:11 - Rationale

FPF is a conceptual framework for disciplined creative work, not a data governance system. External scholarly infrastructure is valuable precisely because it provides fast, wide coverage—but without an explicit interop kit, that value is purchased by silently importing semantics (implicit comparisons, unpinned editions, hidden transformations).

`G.13` resolves the tension by turning “interop” into **first‑class conceptual wiring**: cards/surfaces that pin editions, cite governing patterns, expose provenance hooks, and produce typed refresh causes, while leaving domain/tool specifics in `Extensions` (or Phase‑3 governing definitions).

### G.13:12 - SoTA‑Echoing (post‑2015, for orientation; non‑normative)

* **Scholarly claim graphs & open indexes.** Open research KGs and open scholarly indexes encourage claim‑level representations and concept taxonomies as interop substrates (post‑2015 ecosystem: KG‑style contribution graphs; open indexing initiatives). Treat these as *sources* registered via `ExternalIndexCard`, not as governing patterns.

* **Neural representations for scientific text.** Transformer‑based scientific encoders (e.g., SciBERT‑class; citation‑aware paper representations such as SPECTER‑class; later retrieval‑oriented scientific embedding families) are useful as *alignment heuristics*. In FPF terms, they belong behind `ScaleEmbeddingSpec` + pinned editions/policies (see `G.13:Ext.EmbeddingBasedAlignment`).

* **Schema matching & entity resolution (deep‑learning era).** Modern matcher families (deep entity matching, contrastive representation alignment, GNN‑assisted graph alignment) help populate interop cards, but must not become “implicit semantics”; record their use as policy‑bound wiring in extensions.

* **Systematic review process modernisation.** PRISMA‑2020‑class review records (post‑2015 practice) are valuable as evidence anchors and coverage telemetry; treat them as evidenced inputs (EvidenceGraph anchors + pinned editions/windows), not as legality gates.

* **QD / Illumination and OEE declared set surfaces.** Post‑2015 QD (MAP‑Elites successors, CMA‑ME line, differentiable QD toolkits) and OEE (POET‑class and related environment/method co‑evolution lines) often rely on external taxonomies and environment corpora. Interop should expose those as pinned external editions and keep coverage/regret as telemetry inputs—never as implicit dominance.

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

# **Part H – Glossary & Definitional Pattern Index**

| §   | ID & Title                     | Concise reminder                                               |
| --- | ------------------------------ | ---- | -------------------------------------------------------------- |
| H.1 | Alphabetic Glossary            |  Every `U.Type`, relation & operator with four‑register naming. |
| H.2 | Definitional Pattern Catalogue |  One‑page micro‑stubs of every definitional pattern for quick lookup.  |
| H.3 | Cross‑Reference Maps           |  Bidirectional links: Part A ↔ Part C ↔ Part B terms.           |


# **Part I – Annexes & Extended Tutorials**

| §   | ID & Title                  |  Concise reminder                                                |
| --- | --------------------------- | --- | --------------------------------------------------------------- |
| I.1 | Deprecated Aliases          |  Deprecated names kept as alias labels for continuity; aliases do not carry current semantics. |
| I.2 | Detailed Walk-throughs | Worked entry readings for high-risk or compact-insufficient entry neighborhoods; compact-index-only is a complete admissible posture when enough. |
| I.3 | Change‑Log (auto‑generated) |  Version history keyed to DRR ids.                               |
| I.4 | External Standards Mappings |  Trace tables to ISO 15926, BORO, CCO, Constructor‑Theory terms. |


## I.2 - Detailed Walk-throughs

`I.2` is the canonical worked entry-reading support role in this architecture.
An `I.2` item can serve as one entry-reading vignette, one didactic learning
walkthrough, or both. When it serves as entry reading, its `E.11` force is
limited to disambiguation, wrong-pattern rejection, entry-load reclassification,
and admissible entry stop.

`worked entry reading` here is an explanatory reading case. It is not
`U.Work`, not a workflow, not a route script, and not an execution trace.

`I.2` carries expanded reading only when compact `J.4` guidance plus local
`Problem frame` recognition are insufficient for one high-risk,
often-misclassified, repeatedly failed, retrieval-facing, or materially new
entry neighborhood. Compact-index-only posture is a complete admissible entry result
when the `J.4` row and pattern `Problem frame` are enough.

Each worked entry reading keeps recoverable:

- `Case signal`
- `Initial uncertainty`
- `Plausible candidate patterns`
- `Tempting wrong pattern, wrong defining episteme, or false family`
- `Disambiguating fact`
- `Recognition repair or entry-load reclassification`
- `Actual governing FPF pattern body or projection role`
- `Admissible entry stop`
- `What not to infer`

### I.2.1 - Project alignment

- **Case signal:** "We keep mixing responsibility, method, plan, and what
  actually happened."
- **Posture:** compact-index-only is normally sufficient.
- **Initial uncertainty:** the reader may think FPF starts with the whole
  specification, but the entry load is narrower: align context, roles, method vocabulary, work vocabulary,
  and actual execution.
- **Plausible candidate patterns:** `A.1.1`, `A.15`, `A.15.2`, `A.15.3`,
  `B.5.1`.
- **Nearby patterns:** `F.11` for method vocabulary and work vocabulary; `F.9` for bridge
  discipline; `F.17` for an early term sheet when vocabulary is the live
  stabilizing result.
- **Tempting wrong pattern:** treat `F.17` or `E.9` as a universal first stop.
- **Actual governing FPF pattern body or projection role:** `A.15` and its neighbors govern
  the role, method, plan, and run split; `F.17` is a stabilizing lexical projection,
  not the whole alignment governing pattern.
- **Admissible entry stop:** the reader has opened the right alignment governing pattern or has
  enough first shared vocabulary to proceed.
- **What not to infer:** no universal first chain is implied.

### I.2.2 - Partly-said cue and language-state discovery

- **Case signal:** "This phrase matters, but it is not yet a claim."
- **Initial uncertainty:** the reader can be seeing one cue, one early
  language-state requirement, one publication seam, or one L/A/D/E-classified claim family.
- **Plausible candidate patterns:** `C.2.LS`, `A.16`, `A.16.1`, `A.16.2`,
  `B.4.1`, `B.5.2.0`.
- **Tempting wrong pattern:** harden the cue into `A.6.P`, `A.6.Q`, `A.6.A`,
  or `C.25` before it is stable enough to be a claim, action, or quality
  object.
- **Disambiguating fact:** the phrase still needs preservation and entry-load
  typing; it is not yet an endpoint claim.
- **Decision movement:** if the phrase is still a cue, stay in `C.2.LS` /
  `A.16`; if it must be preserved across a seam, inspect `A.16.1` / `B.4.1`;
  if it is already a boundary claim, inspect `A.6.B` / `A.6.C`; if it is being
  forced into a quality endpoint or action-invitation endpoint too early, reject `A.6.Q`, `A.6.A`, and
  `C.25` for now.

- **Actual governing FPF pattern body or projection role:** `C.2.LS`, `A.16*`, and
  `B.4.1` are the first governing patterns for cue preservation and entry plurality;
  `A.6.B` / `A.6.C` become first governing patterns only after boundary claim structure is
  actually live.
- **Admissible entry stop:** cue preserved, entry plurality opened, or entry-load
  reclassified into the right boundary-claim pattern.
- **What not to infer:** do not recast the cue as a finished requirement, work
  record, quality claim, or action invitation too early.

### I.2.3 - Boundary unpacking and claim decomposition

- **Case signal:** "The API or contract-language description says X."
- **Initial uncertainty:** the reader may be seeing one boundary description,
  an admissibility gate, a duty, an evidence claim, an action invitation, or an
  interface/access note.
- **Plausible candidate patterns:** `A.6`, `A.6.B`, `A.6.C`.
- **Nearby patterns:** `A.6.RSIG` if first-contact recognition is still live;
  `A.6.P` for relation wording; `A.6.Q` for quality wording; `A.6.A` for
  action invitation wording; `E.17` for publication or view question.
- **Tempting wrong pattern:** treat an API/access phrase as a promise of
  downstream effect, or treat one boundary phrase as a complete Contract Bundle.
- **Disambiguating fact:** the sentence mixes admissibility, gate, duty, evidence, and action-invitation
  requirements, or the encountered description's defining `U.Episteme` is not yet
  clear.
- **Recognition repair or entry-load reclassification:** use `A.6.RSIG` if the
  first question is "what description is this?"; otherwise inspect `A.6.B`
  / `A.6.C` for atomic boundary claim structure.
- **Actual governing FPF pattern body or projection role:** `A.6.B` and `A.6.C` govern
  L/A/D/E-classified claim decomposition; `A.6.RSIG` only governs first-contact
  description recognition.
- **Admissible entry stop:** boundary claim pattern opened, or one Claim Register or
  L/A/D/E-classified atomic claim set is ready for the next governing FPF pattern.
- **What not to infer:** one contract-language or API cue does not by itself create one
  work action, quality claim, or evidence relation.

### I.2.4 - Admissible comparison, candidate-pool policy, selection, and selected-set publication

- **Case signal:** "We need a shortlist, not one winner."
- **Initial uncertainty:** the live entry load can be comparison substrate,
  candidate-pool policy, one local choice, call planning, or selected-set
  publication.
- **Plausible candidate patterns:** `A.19.CN`, `A.17-A.19`, `C.18`, `C.19`,
  `G.0`, `G.5`.
- **Nearby patterns:** `C.11` if the entry load narrows to one local decision
  doctrine; `C.24` if the next honest artifact is a call plan or checkpoint
  return; `A.19.CPM` and `A.19.SelectorMechanism` if comparator/selector
  structure is live.
- **Tempting wrong pattern:** treat `C.11` as the first governing pattern while the real
  entry load is candidate-pool policy or selected-set publication.
- **Disambiguating fact:** the output remains one governed set, shortlist, or
  selected-set publication question rather than one single winner.
- **Decision movement:** if the work is still forming a candidate pool, inspect
  `C.19`; if the set is ready to be published as a governed shortlist, inspect
  `G.5`; if the question has narrowed to choosing one option under a local
  decision doctrine, inspect `C.11`; if the missing object is a call plan or
  planned comparison setup, inspect `C.24`.

- **Actual governing FPF pattern body or projection role:** `C.19` for candidate-pool
  policy, `G.5` for selected-set publication, `C.11` for local choice,
  `C.24` for call-planning/checkpoint-return.
- **Admissible entry stop:** the correct first governing pattern is opened, or an admissible
  candidate-pattern set is stabilised without implying sequence.
- **What not to infer:** do not force a one-winner answer when the honest
  output is still a governed selected set.

### I.2.5 - Generator, SoTA, or Portfolio Kit

- **Case signal:** "We need a reusable search/harvest/portfolio scaffold, not
  one recommendation."
- **Posture:** compact-index-only is normally sufficient unless repeated
  misclassification makes a worked reading necessary.
- **Initial uncertainty:** the reader can confuse generator/scaffold authoring
  with one-off recommendation, one comparison, one selected-set publication, or
  tooling choice.
- **Plausible candidate patterns:** `A.0`, `G.0`, `G.1`, `G.2`, `G.5`.
- **Nearby patterns:** `B.5.2.1` and `C.17-C.19` when creative search,
  novelty, or explore/exploit policy is already central; `G.10` or `G.11` when
  shipping or refresh is live.
- **Tempting wrong pattern:** jump to `G.5` publication or a local selector
  before the reusable generator/SoTA scaffold is declared.
- **Disambiguating fact:** the generator, SoTA, or portfolio kit must be reusable across
  searches, portfolios, or updates.
- **Actual governing FPF pattern body or projection role:** `G.1` and `G.2` for generator and
  SoTA support; `G.5` only when selected-set publication is live.
- **Admissible entry stop:** scaffold/generator pattern body opened, or portfolio
  publication pattern identified.
- **What not to infer:** not every generator/SoTA entry load is a tool implementation or
  one immediate publication obligation.

### I.2.6 - Same-entity rewrite, explanation, and comparative reading

- **Case signal:** "We need to explain the same described entity for another audience."
- **Initial uncertainty:** explanation, rendering, repair, representation
  transition, and comparison are all nearby, and the reader can accidentally
  mint one second described entity.
- **Plausible candidate patterns:** `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`,
  `E.17.ID.CR`.
- **Nearby patterns:** `E.17.AUD.LHR` for pressured-head local repair;
  `E.17.AUD.OOTD` for `PublicationUnit` stability.
- **Tempting wrong pattern:** explanation-as-new-object or repair-as-second-rule
  track.
- **Disambiguating fact:** the governed object stays the same; only rendering,
  reading posture, or explanatory framing changes.
- **Recognition repair or entry-load reclassification:** move toward same-entity
  rewrite or explanation-facing rendering while rejecting second-object drift.
- **Actual governing FPF pattern body or projection role:** `A.6.3.CR` for same-entity
  retextualization, `A.6.3.RT` for representation transition, `E.17.EFP` for
  explanation-facing rendering, `E.17.ID.CR` for bounded comparative reading.
- **Admissible entry stop:** same-entity rewrite opened or explanation-facing
  rendering stabilized with source pins.
- **What not to infer:** explanation or comparison does not by itself justify a
  second semantic track.

### I.2.7 - Temporal claim adequacy: state -> rate -> Dyn2

- **Case signal:** "Adding review capacity for two sprints will double backlog reduction rate."
- **Initial uncertainty:** the reader may be seeing ordinary prose, one state reading or snapshot, one measured rate, one intervention-sensitive temporal claim, a benchmark claim, a quality claim, a viability claim, a promise, a causal claim, an evaluation claim, a dynamics-law claim, or a residual QL question.
- **Plausible candidate patterns:** `C.27`, `C.16`, `A.3.3`, `B.1.4`, `B.1.6`, `C.24`, `G.9`, `C.25`, `C.26.3`, `C.26`.
- **Tempting wrong pattern:** treat every speed or rhythm word as C.27, or treat every C.27 card as benchmark proof, causal proof, service promise, quality claim, viability claim, reusable transition law, or QL activation.
- **Disambiguating fact:** the phrase changes admissible use only when effort, window, resistance or cost, basis, and reopen condition matter for action.
- **Recognition repair or question reclassification:** keep a snapshot as Dyn0; keep a measured trend or rate as Dyn1 and inspect `C.16` when measurement construction or comparability is live; use `Dyn2TemporalClaimAdequacyCard` when the intervention-sensitive temporal claim itself changes admissible use; move the other question to the named FPF pattern that governs it.
- **Actual governing FPF pattern or projection role:** `C.27` carries authored temporal-claim adequacy; `C.16` carries measurement construction and comparability; `A.3.3` carries reusable transition law or formal dynamics model; `G.9` carries benchmark parity; `C.25` carries quality-family adequacy; `C.26.3` carries viability-envelope regulation; `C.26` carries residual QL reading only after ordinary temporal, measurement, work, benchmark, proxy, and dynamics readings are exhausted.
- **Admissible entry stop:** ordinary prose, Dyn0, Dyn1 with `C.16` when measurement construction or comparability is live, a local `Dyn2TemporalClaimAdequacyCard`, a boundary-crossing `Dyn2TemporalClaimProfile`, or a named neighboring FPF pattern relation.
- **What not to infer:** faster is not automatically better, a velocity target is not proof of improvement, a dynamic benchmark is not benchmark superiority, and a rhythm or inertia word does not by itself mint a new dynamics object.

### I.2.8 - Causal-use and counterfactual-support repair

- **Case signal:** "This policy would have prevented harm", "this intervention caused the improvement", "this fairness result is causal", "this method is better on counterfactual outcomes", or "these simulated counterfactuals prove the decision".
- **Initial uncertainty:** the reader may be seeing association, a metric disparity, temporal change, method execution, work-plan use, work occurrence, simulation output, deontic boundary language, or a real causal-use claim.
- **Plausible candidate patterns:** `C.28`, `A.10`, `B.3`, `C.11`, `C.19`, `C.24`, `C.26`, `C.27`, `D.5`, `G.5`, `G.9`, `A.15`, `A.3.2`, `A.6`, `C.16`.
- **Tempting wrong pattern:** use `D.5` to treat metric fairness as causal fairness; use `G.9` to compare methods across different causal rungs; use `C.26` to hide causal under quantum-like wording; use `C.27` to treat rate change as causal effect; use `A.15` or `A.3.2` to treat a sampling method, intervention procedure, or target-trial recipe as causal support by itself; use `A.6` to turn causal evidence into a duty or release gate.
- **Disambiguating fact:** the decisive question is not whether a causal-looking word appears. The decisive question is whether the claim is used to publish, choose, deploy, assure, audit, benchmark, or dispatch a causal use governed by `C.28`: effect, intervention success, counterfactual comparison, causal fairness, policy optimality, causal evidence support, off-policy/causal-RL evaluation, or causal method superiority.
- **Recognition repair or question reclassification:** if only a measured value is live, repair in `C.16`; if only rate, trend, or temporal adequacy is live, repair in `C.27`; if only method, work, or work-plan structure is live, repair in `A.15` and `A.3.2`; if only boundary duty or agreement language is live, split with `A.6`; if only residual QL modeling language is live, use `C.26` only after ordinary measurement, temporal, work, benchmark, proxy, and dynamics readings are exhausted.
- **Actual governing FPF pattern body or projection role:** `C.28` carries causal-use question, causality-ladder rung, claim kind, causal estimand, identification, counterfactual sampling realizability, causal evidence support basis, support record and verdict, supported use, and unsupported use. `A.10` carries evidence/provenance path, `B.3` carries assurance consequence, `D.5` carries ethical/fairness audit, `G.5` carries method dispatch, and `G.9` carries benchmark parity only as consumers of `C.28` support.
- **Admissible entry stop:** a cheap downgrade sentence, a local `CausalUseTriageRecord`, a local or durable `CausalUseEvidenceDesignRecord`, a `CausalUseSupportVerdict`, or a named neighbor-pattern use that cites `C.28` without claiming broader authority.
- **What not to infer:** a randomized procedure is not automatically counterfactual support; a simulation is not realized counterfactual data; a target-trial phrase is not proof of identification; a fairness metric is not causal fairness; a method benchmark is not comparable if methods sit on different causal rungs or estimands; and a causal support record does not by itself create a duty, promise, commitment, release gate, or admissibility predicate.

### I.2:End

# **Part J – Indexes & Navigation Aids**

| §   | ID & Title               |  Concise reminder                                        |
| --- | ------------------------ | ------------------------------------------------------- |
| J.1 | Concept‑to‑Pattern Index |  Quick jump from idea (“boundary”) to pattern (§, id).   |
| J.2 | Pattern‑to‑Example Index |  Table listing every archetypal grounding vignette.      |
| J.3 | Principle‑Trace Index    |  Maps each Pillar / C‑rule / P‑rule to concrete clauses. |
| J.4 | First Practical Entry Neighborhood Index | Compact entry-neighborhood index matching the public entry families without route-state, authority-reference, or output columns. |

## J.4 - First Practical Entry Neighborhood Index

This index is informative navigation only.
It helps one reader compare plausible first pattern entries under one live
entry load. It is not one route table, not one workflow, not one learning syllabus,
and not one pattern-local recognition role. It is one compact comparison of
nearby starting points.

Plain reading: choose by what you are really trying to decide, not by document
order. A row names first patterns to inspect, plausible wrong first stops, and
where entry can stop without pretending there is a required workflow.

Plain column key: entry neighborhood = nearby starting-point cluster; first
honest entry load = what you are really trying to decide or stabilize; candidate
patterns = first patterns to inspect; admissible entry stop = enough to proceed
without pretending there is a workflow.

| Entry neighborhood | First honest entry load or case signal | Candidate patterns | Nearby patterns and entry-load reclassifications | First admissible entry stop | Not this entry when | Worked reading and lexical-query support |
| --- | --- | --- | --- | --- | --- | --- |
| Project alignment | "We keep mixing responsibilities, working method, plans, and what actually happened." | `A.1.1`; `A.15`; `A.15.2`; `A.15.3`; `B.5.1` | `F.11` when method vocabulary or work vocabulary is itself unstable; `F.9` when bridge discipline is live; `F.17` as a typical vocabulary-stabilizing output | the right alignment pattern is opened, or a first shared work/term form is stable enough to proceed | not when the live entry load is already comparison, boundary claim routing, or SoTA/generator scaffold design | `I.2.1` gives compact-index-only posture; ToC cues stay sparse |
| Partly-said cue and language-state discovery | "Something important is there, but it is too early to publish as a settled claim, requirement, or work record." | `C.2.LS`; `A.16`; `A.16.1`; `A.16.2`; `B.4.1`; `B.5.2.0` | endpoint claim, action, or quality patterns become candidates only after the cue is mature enough | cue preserved, language-state cue typed, or entry plurality opened without endpoint hardening | not when the claim is already stable enough for a L/A/D/E-classified boundary claim set or endpoint record | `I.2.2` worked reading; lexical cues may mention "vague cue", "not yet a claim" |
| Boundary unpacking and claim decomposition | "A contract, API, protocol, SLA, acceptance, or compliance sentence mixes law, gate, duty, evidence, or action." | `A.6`; `A.6.B`; `A.6.C` | `A.6.RSIG` if first-contact recognition of the boundary description is still live; `A.6.P`, `A.6.Q`, `A.6.A` when relation, quality, or action wording is live | boundary claim pattern opened, or an L/A/D/E-classified atomic claim set or Claim Register is ready for the next governing FPF pattern | not when the phrase is only a partly-said cue, or when a full L/A/D/E-classified claim set already exists | `I.2.3` worked reading; ToC cues should not turn API wording into generic contract authority |
| Admissible comparison, candidate-pool policy, selection, and selected-set publication | "We need comparison, a shortlist, a live pool, a call-planning distinction, or a selected set without forcing one winner too early." | `A.19:0`; `A.17-A.19`; `A.19.CN`; `C.18`; `C.19`; `G.0`; `G.5` | `C.11` when the entry load narrows to one local decision doctrine; `C.24` when the next honest C.24 object is `CallPlan` or `CheckpointReturn`; `A.19.CPM` and `A.19.SelectorMechanism` when comparator/selector structure is live | candidate-pool policy, comparison substrate, local choice, call-plan, or selected-set publication pattern identified honestly | not when a selector mechanism or selected-set publication pattern is already settled elsewhere | `I.2.4` worked reading; lexical cues may include "shortlist not winner" and "acceptable option set" |
| Generator, SoTA, or portfolio kit | "The work is to publish a reusable search, harvest, generator, selector, or portfolio scaffold, not one recommendation." | `A.0`; `G.0`; `G.1`; `G.2`; `G.5` | `B.5.2.1` and `C.17-C.19` when creative search, novelty, or explore/exploit policy is already central; `G.10` or `G.11` when shipping or refresh is live | kit or scaffold entry load opened, or portfolio or set publication pattern identified | not when the entry load is only one local comparison or one one-off recommendation | `I.2.5` gives compact-index-only posture unless repeated misclassification makes depth necessary |
| Same-entity rewrite, explanation, and comparative reading | "We need to restate, explain, render, repair, or compare the same claim-bearing `PublicationUnit` without quietly changing what it is about." | `A.6.3.CR`; `A.6.3.RT`; `E.17.EFP`; `E.17.ID.CR` | `E.17.AUD.LHR` and `E.17.AUD.OOTD` when pressured-head repair or `PublicationUnit` stability is live | same-entity rewrite, representation transition, explanation-facing rendering, or bounded comparative reading opened | not when the entry load is one new `U.Episteme`, new rule track, or independent `PublicationUnit` | `I.2.6` worked reading; ToC cues should include "same unit, different audience" |
| Temporal claim adequacy under effort, window, and resistance | "This should speed up, slow down, recover sooner, stabilize, keep cadence, or improve throughput under a changed effort, tool-use, rollout, or policy." | `C.27`; `C.16` when only measurement is live; `A.3.3` when reusable transition law or formal model is live | `B.1.4`, `B.1.6`, `C.18.1`, `C.19`, `C.22.1`, `C.24`, `C.25`, `C.26`, `C.26.3`, or `G.9` as the other question requires | ordinary prose, Dyn0, Dyn1 with `C.16` when measurement construction or comparability is live, `Dyn2TemporalClaimAdequacyCard`, `Dyn2TemporalClaimProfile`, or a named neighboring FPF pattern relation | not when the phrase is only a speed metaphor, one state reading or snapshot, one measured rate, a service promise, a benchmark harness, or a residual QL cue without an intervention-sensitive temporal claim | `I.2.7` state-to-rate-to-Dyn2 worked reading; lexical cues: speed, velocity, rhythm, cadence, throughput, recovery, braking, stabilization |
| Causal-use and counterfactual-support repair | "We want to say this caused that, this intervention would work, this policy would have prevented harm, this fairness result is causal, or this method is better on a counterfactual benchmark." | `C.28`; `A.10`; `B.3`; `D.5`; `G.5`; `G.9` | `C.16` when only a metric, score, or reading is live; `C.27` when only state, rate, or intervention-sensitive temporal adequacy is live; `C.26` when the phrase is only a residual quantum-like modeling cue; `A.15` or `A.3.2` when the question is only method, work-plan, or work-occurrence structure; `A.6` when a mixed causal/deontic boundary sentence must be split | causal-use triage/card names rung, claim kind, estimand, support basis, support verdict, supported use, and unsupported use; or the wording is downgraded to association, metric, temporal, simulation-only, QL, method, work-plan, work-occurrence, or boundary-claim support | not when the sentence only records observed association, one measured metric, one process execution, one schedule, one boundary duty, or one simulation trace with no causal-use claim | `I.2.8` worked reading; lexical cues: caused, would have prevented, effect, intervention, counterfactual, target trial, policy optimality, causal fairness, causal evidence, counterfactual data, method improves |

Rows are for likely first practical entries, common wrong first guesses, or
public/retrieval-facing entry points. A pattern does not need a `J.4` row merely
because it exists.
Index maintainers update a row when the pattern becomes a practical entry point
or its first-pattern choice changes; ordinary pattern authors only need the
pattern's own `Problem frame` and any live wrong-pattern boundary to be clear.

A `J.4` row usually stays bounded: `3-6` candidate patterns, `1-3` nearby or
reclassification cues, one short not-this-entry sentence, and one short admissible
entry-stop phrase. The row remains compact enough to read in one pass and
specific enough not to smuggle workflow.

`J.4` remains the compact projection role for these rows. It does
not become the applicable governing pattern body for the entry loads or relations it points to. If a
referenced pattern's own `Problem frame` does not expose its use situation, the
pattern itself remains under-authored. If a row cannot stay compact, the depth
belongs in `I.2`.

### J.4:End

# **Part K  – Lexical debt**

## Mandatory replacement map for measurement terms

> **Rule:** In all **normative** content (specifications, data schemas, etc.), the deprecated terms **“axis”** and **“dimension”** (and their plural or compound forms) **MUST NOT** be used to denote a measurable aspect. Use **Characteristic** in the Tech register instead. Other colloquial terms should be mapped to canonical terms as listed below. In **Plain** narrative, deprecated aliases may appear _only on first use_ and only if paired with their canonical equivalent for clarity.

| Deprecated term (context) | **Replace with** (Tech register) | Plain register allowance | Canonical Reference |
| --- | --- | --- | --- |
| axis (of measurement); dimension (of a system or quality) | **(disallowed in Core prose)** → use **Characteristic** | No parenthetical allowance in Core; use **Characteristic**, **Measure**, or **Coordinate** only | A.17 (CHR-NORM) |
| point (on an axis); data point | **Coordinate** (on a Scale) | “point” _(in explanations only, e.g. “a point on the scale”)_ | A.18 (CSLC-KERNEL) |
| metric value; raw score | **Coordinate** (or **Value**) | “value” _(acceptable in plain usage when context is clear, but formally it’s a Coordinate tied to a Characteristic)_ | A.18, C.16 |
| score (composite or normalized) | **Score** (produced via a **ScoringMethod**) | “score” _(if needed in narrative, ensure it’s explained as a result of a defined ScoringMethod)_ | A.17/A.18 (ScoringMethod/Score) |
| unit dimension; unit axis | **Unit** (of a Scale) | “unit” _(plain usage okay)_ | A.18 (Scale/Unit) |
| metric (as a noun) | **Avoid in Tech and as primitive** → use **`U.DHCMethodRef` / `U.Measure` / Score** | “metric” _(Plain only on first use, with pointer to canonical terms)_ | C.16 § 5.1 (L5), A.18 |

## Temporal claim lexical debt from C.27

Retire untyped velocity, acceleration, cadence, agility, rhythm, inertia, and dynamics language when it is used outside a named C.27, C.16, or A.3.3 reading. Repair each occurrence to one of: ordinary prose, Dyn0 state reading or snapshot, Dyn1 measured rate or trend, Dyn2 intervention-sensitive temporal claim, C.16 measurement construction, or A.3.3 reusable transition law or model.

Russian/English Plain-Tech twins for authoring:

| Russian Plain | Safe Tech reading |
| --- | --- |
| скорость | rate, throughput, or tempo reading |
| ускорение | rate-change or intervention-sensitive temporal claim |
| усилие | planned effort, work, resource, or input basis, or intervention basis |
| инерция | resistance/inertia proxy, not a physical mass analogue by default |
| ритм | bearer/anchor/window/proxy relation |
| динамика второй производной | Dyn2 claim reading, not second-derivative ontology |

## Migration debt from A.2.6 (Scope, ClaimScope, WorkScope)

### Deprecations (normative)

The following terms **MUST NOT** name scope objects in normative text, guards, or conformance blocks:

* *applicability*, *envelope*, *generality*, *capability envelope*, *validity* (as a characteristic name).

Use instead:

* **`U.ClaimScope`** (*Claim scope*, nick **G**) for epistemes;
* **`U.WorkScope`** (*Work scope*) for capabilities;
* **`U.Scope`** only when explaining the abstract mechanism (not in guards).

### Affected locations and required edits (normative)

Editors SHALL apply the following replacements:

1. **Part C.2.2 (F–G–R).**

   * Replace any internal definition of “Generality” with a normative reference to **A.2.6 §6.3** (*Claim scope (G)*).
   * Where “abstraction level” is mentioned as G, replace with “Claim scope (where the claim holds)”; keep **AT** (AbstractionTier) only as optional didactics (non‑G).
   * Ensure composition examples use **intersection/SpanUnion** for G, not ordinal “more/less general”.

2. **Part C.2.3 (Formality F).**

   * No change to F itself.
   * Any example that implies “raising F widens G” MUST be rephrased: F changes expression form; G changes only via **ΔG**.

3. **Part A.2.2 (Capabilities).**

   * Replace “capability envelope/applicability” with **`U.WorkScope`**.
   * Method–Work gates MUST test **Work scope covers JobSlice**, with **measures** and **qualification windows** bound.

4. **Part B (Bridges & CL).**

   * Add a note: **CL penalties apply to R**, not to **F/G**; mapping MAY recommend **narrowing** the mapped scope (best practice).

5. **Part E (Lexicon).**

   * Add entries for **Claim scope (G)**, **Work scope**, **Scope** (mechanism).
   * Mark listed deprecated terms as **deprecated aliases** allowed only in explanatory notes.

6. **ESG & Method–Work templates.**

   * Replace any “applicability”/“envelope” guard phrasing with **ScopeCoverage** (see §10).
   * Require explicit **`Γ_time`** selectors in all scope‑sensitive guards.

### Migration playbook (informative)

1. **Inventory** scope‑like phrases across your Context (search: applicability, envelope, generality, capability envelope, valid\*).
2. **Classify** each occurrence as **Claim scope** (episteme) or **Work scope** (capability); replace any “scope characteristic(s)” with “scope object”, “scope type”, or “USM scope object” depending on sentence grammar.
3. **Rewrite** guards to use `Scope covers TargetSlice` + explicit **`Γ_time`**; remove “latest”.
4. **Publish** any required **Bridges** with **CL** for Cross‑context usage.
5. **Document** ΔG changes separately from evidence freshness (R).

### Alias and body-prose continuity (informative)

Existing body prose may keep older phrasing only when it is explanatory and carries no current requirement. All **guards, conformance checklists, and state assertions** MUST be rewritten to the USM terms and semantics.

### Change Log (normative migration record)

* **A.2.6 introduced.** Defines `U.ContextSlice`, `U.Scope`, `U.ClaimScope (G)`, `U.WorkScope`; sets algebra and guard patterns.
* **Deprecated labels.** “applicability / envelope / generality / capability envelope / validity” as characteristic names.
* **Edits required.** C.2.2 (G = Claim scope), A.2.2 (Work scope for capabilities), Part B (CL→R note), Part E (Lexicon updates), ESG/Method–Work guard templates (ScopeCoverage + `Γ_time`).
* **No change.** C.2.3 (F) unchanged; its examples updated only for wording consistency.