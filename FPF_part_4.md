## G.11 - Telemetry-Driven Refresh and Decay Orchestrator

**Tag.** Architectural pattern (architectural; notation-independent)
> **Status:** Stable
**Normativity.** Normative (unless explicitly marked informative)

**Stage.** run-time and maintenance-time (selective re-computation, republication, and controlled deprecation)

**Primary outputs (kit publication units and records).** `RefreshQueue`, `RefreshPlan@Context` (WorkPlanning plan item), `RefreshReport@Context` (Work or Audit record), `DeprecationNotice@Context`, `EditionBumpLog@Context`.

**Primary hooks.** `G.Core` (RSCR trigger catalogue, alias docking, and Default Governing Definition Index), `G.6` (EvidenceGraph; `PathId` and `PathSliceId`), `G.7` (Bridge Sentinels; CL, Φ, and plane policy pins), `G.5` (set-returning selection and dispatch), `G.8` (SoS-LOGBundle telemetry hooks), `G.9` (parity reruns), `G.10` (shipping hooks and pack-level telemetry pins), `G.12` (dashboard telemetry pins), `B.3.4` (freshness and decay), `E.18` (GateCrossing and CrossingBundle visibility), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support records whose SoTA-sensitive fields can change downstream causal-use results).

**Non-duplication note.**
`G.11` cites `G.Core` for RSCR trigger-kind meaning, CN and CG admissibility, tri-state guards, penalties, set-return semantics, shipping or harvesting delegation, `RSCRTriggerKindId` values, and default governing definitions.
Refresh plans and reports cite those governed definitions; they do not create local trigger meanings or default definitions inside the refresh record.

### G.11:0 - Use this when

Use this pattern when a shipped pack, evidence set, dashboard, selected set, archive, front, Q-front, term bridge, descriptor set, or parity result may be stale because telemetry, freshness, edition pins, policy pins, evidence, bridge calibration, or source currentness changed.

#### G.11:0.1 - What goes wrong if missed

The team either rebuilds everything after every small change or keeps using a shipped record whose source, descriptor, edition, policy, bridge, or archive currentness has silently drifted. Refresh then becomes an informal maintenance habit rather than a scoped, reviewable work plan and report.

#### G.11:0.2 - What this buys

The practitioner gets a small refresh kit: name the affected object, currentness object kind, source record, edition or lineage pins, affected scope, governing pattern, planned refresh action, and report. The refresh can stay local while still preserving comparability, selected-set meaning, archive and front meaning, and source-currentness evidence.

#### G.11:0.3 - First output
For loop, harness, workflow-store, or DPF seed artifacts, a refresh line names the currentness object directly: source pack, evaluator, benchmark, harness edition, workflow edition, pattern seed, PFAD and PFR dependency, selected set, archive, front, or publication carrier. `G.11` records currentness, source decay, edition change, telemetry, scoped refresh action, and report refs; it does not create a local "reopen and refresh" pair and does not decide whether the artifact improved.

Write one `RefreshCurrentnessLine@Context` or one `RefreshPlan@Context` with the affected scope and direct governing pattern named. If the meaning belongs to selected-set publication, archive or front stewardship, cultural evolution, term bridges, evidence, dashboard, or shipping, cite that governing pattern rather than defining the meaning inside the refresh record.

Framework edition pins, source packs, publication-carrier currentness, deprecation, supersession, and source-decay conditions are refresh and currentness claims governed here when currentness is the live question. Record the framework-specific trigger and cite `E.4`, `E.4.PFR`, `E.4.PFAD`, `G.2`, `E.11`, or `E.17` as the direct owner of the affected framework, source, decision, or publication meaning instead of creating a private refresh vocabulary in the framework pattern.

### G.11:1 - Problem frame — Keeping shipped SoTA current without global rebuilds

Part G produces shipped, selector-ready publication units and records: packs, bundles, evidence graphs, parity reports, and dashboards. Once shipped, they are exposed to:

* **telemetry** (illumination and archive changes, parity outcomes, dashboard deltas),
* **decay** (freshness windows expire; epistemic debt grows),
* **edition drift** (descriptor, distance, or transfer rules bump; policy pins evolve),
* **bridge evolution** (CL or plane penalties or calibrations update).

Without an explicit orchestration kit, refresh becomes either:

* a brittle set of ad-hoc “full rerun” rituals, or
* an audit-only refresh result that silently accumulates drift.

`G.11` is the **Part G governing definition** of the **refresh orchestration kit**: it turns typed refresh causes into **scoped plans** and **auditable execution reports**, while delegating all cause semantics and universal invariants to `G.Core`.

### G.11:2 - Problem — Why naive refresh breaks comparability and admissibility

A refresh loop fails (conceptually) when any of the following happens:

1. **Full-rerun mania.** Minor edits (e.g., a single Bridge calibration) trigger pack-wide rebuilds without a traceable scope rationale.
2. **Editionless telemetry.** Telemetry signals are recorded without edition pins, making reruns non-comparable and parity-unreplayable.
3. **Alias-as-semantics.** Local trigger aliases are treated as if they define meaning, fragmenting refresh semantics across patterns.
4. **Silent crossings.** Refresh actions implicitly change crossing assumptions (UTS, Path, or policy pins) without a visible CrossingBundle.
5. **Orchestration smuggles semantics.** Refresh introduces new default behaviors (dominance, `PortfolioMode`, or Γ-fold) or coerces partial orders into scalars “for convenience.”

### G.11:3 - Forces — Minimal recomputation under strict invariants

* **Minimal scope vs. completeness.** Refresh must be *as local as possible* (slice-scoped), but still include a defensible dependency closure over evidence and crossings.
* **Operational urgency vs. auditability.** Refresh is triggered by run-time telemetry and decay, yet must remain auditable as Work (pins, refs, paths), not as opaque “decisions.”
* **Alias stability vs. semantic unification.** Existing trigger labels must remain usable, but their meaning must be one governing definition and id-based.
* **Modularity vs. orchestration power.** `G.11` must coordinate harvesting, parity, and shipping without re-implementing them or importing discipline-specific method semantics into core.
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

By the `G.Core` **Expansion rule**, the **effective** conformance ids, trigger kinds, and pin obligations for `G.11` are the manifest expansions (profiles, sets, and pin sets) plus the explicit deltas above.

**TriggerAliasIds (visible; labels only).** `{G.11:T0…T7}` (docked via `TriggerAliasMapRef`; aliases are never semantic authorities).

#### G.11:4.2 - Refresh orchestration kit (pattern-governed; conceptual artefacts)

`G.11` defines a minimal kit of *authoring-plane* artefacts that make refresh explicit and auditable.

1. **`RefreshQueue` (conceptual queue).**
   A queue of refresh candidates keyed by scope (`PathSliceId` preferred; `PatternScopeId` permitted).
   Ordering, prioritization, and batching are policy-bound (and therefore extension-scoped), but every queue item carries canonical trigger kind ids.

2. **`RefreshPlan@Context` (WorkPlanning plan item).**
   A planned refresh is a WorkPlanning object that **does not execute Work** and **does not embed gate decisions**. It declares:

* `RefreshPlanId` (UTS-published id; editioned)
* `EntityOfConcernRef` and `ReferencePlane` pins (by ref; no implicit widening)
* `TargetScope := PathSliceId[] | PatternScopeId[]`
* `PlannedTriggers := RSCRTrigger[]` (canonical trigger kind ids, scope, and payload pins)
* `PlannedActions := RefreshAction[]` (each action delegates to a governing pattern)
* `RequiredPins := {EditionPins, PolicyPins, UTS pins, Path pins}` for replayability
* `PlanItemRefs := SlotFillingsPlanItemRef[]` (when planning baselines or reruns requires explicit planned slot fillings)

3. **`RefreshReport@Context` (Work or audit artefact).**
   An execution report (Work or Audit artefact) that records:

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

Use this line when refresh currentness concerns a selected set, front, Q-front, archive, portfolio lineage, cultural-variant lineage, style or tradition term bridge, or path slice.

```text
RefreshCurrentnessLine@Context:
  governedObjectRef:
  currentnessObjectKind:
  sourceRecordRef:
  editionOrLineagePins:
  affectedPathSliceOrScope:
  directGoverningPatternRef:
  plannedRefreshAction:
  refreshReportRef?:
```

`currentnessObjectKind` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, cultural-variant lineage, style or tradition term bridge, or path-slice scope. G.11 records the refresh plan, scope, pins, report, and deprecation or edition-bump publication. It does not define selected-set publication, archive or front semantics, cultural-evolution semantics, or term-bridge semantics. Use `G.5`, `C.18`, `C.19`, `C.36`, `F.17`, `F.18`, and `F.9` for those meanings.

Freshness and currentness are handled by `RefreshPlan@Context`, `RefreshReport@Context`, `DeprecationNotice@Context`, and `EditionBumpLog@Context`; do not add a separate ticket kind for the same concern.

#### G.11:4.3 - Orchestration semantics (conceptual; delegating to governing definitions)



`G.11` turns typed causes into scoped actions without governing the semantics of those actions.

**4.3.1 Ingestion.**
Consume RSCR triggers from:

* telemetry hooks (e.g., `G.8`, `G.10`, `G.12`),
* freshness and decay events (`B.3.4`),
* evidence, bridge, policy, or edition edits (from the respective governing patterns’ publication faces, forms, or units).

Every ingested signal is normalized into an `RSCRTrigger` (canonical id, scope, payload pins), with optional alias labels.

**4.3.2 Scope closure (EvidenceGraph-first).**
Compute the minimal dependency closure over:

* cited evidence and source relations, with `G.6` `PathId` and `PathSliceId` refs when a graph path slice is the current math-lens expression,
* declared crossings (`G.7` sentinels; `CrossingBundle` visibility),
* and pinned references (editions and policies).

The closure is a *planning-time claim* (“these slices are affected”), not a Work-time output.

**4.3.3 Planning (P2W boundary).**
Produce `RefreshPlan@Context` that schedules actions of the form:

* `RerunHarvest` (delegates to the selected harvest, source-currentness, or SoTA governing definition named by value, such as `G.1` or `G.2`, when that definition is current)
* `RerunParity` (delegates to `G.9`)
* `RecomputeSelectionOrSetPublication` (delegates to `G.5`)
* `RebindBridgeOrCrossing` (delegates to `G.7` and visibility harnesses)
* `UpdateEvidenceBindings` (delegates to `G.6`)
* `ReshipPack` (delegates to `G.10`)
* `UpdateBundle` (delegates to `G.8`)
* `UpdateDashboardSlice` (delegates to `G.12`)
* `EmitDeprecationNotice` or `EmitEditionBumpLog` (publication units governed by this pattern)

**4.3.4 Execution and audit.**
Execute planned actions as Work (or Work-bound audit) and publish `RefreshReport@Context`.
Gating outcomes (admit, degrade, or abstain) follow `G.Core` tri-state semantics and are recorded through policy ids and cited evidence or source relations, rather than as local bespoke outcomes.

#### G.11:4.3a - Causal-use refresh sentinels

When a shipped pack, parity report, evidence relation, source relation, dashboard slice, fairness audit, policy evaluation, or selector output consumes `C.28`, refresh planning includes causal-use sentinel causes when they can change supported use, unsupported use, support verdict, or downstream assurance:

| Causal-use sentinel | Typical affected C.28 result or related claim | Refresh payload pins |
| --- | --- | --- |
| counterfactual-realizability shift | `CounterfactualSamplingRealizabilityProfile`, `realizedCounterfactualSampleSupportBasis`, causal evidence design | profile refs, action-primitive refs, work-plan refs, physical, ethical, and operational constraint refs, target counterfactual distribution refs, admissible-use refs, and unadmissible-use refs |
| counterfactual-data identification and bounding shift | `CausalIdentificationProfile`, `identifiedCounterfactualEstimateSupportBasis`, bounds or partial-identification result | available data regime set refs, realized counterfactual data refs, counterfactual-data identification method refs, counterfactual-data bound refs, assumption refs |
| target-trial reporting shift | `TargetTrialProtocolRecord`, `TargetTrialEmulationMappingRecord`, applied intervention-effect support verdict | protocol refs, observational data source refs, eligibility, treatment, time-zero, and assignment mappings, follow-up and outcome mappings, emulation-gap refs, residual-confounding and sensitivity refs and additional-analysis refs |
| causal-fairness shift | `CausalFairnessUseAuditCard`, causal fairness support verdict, fairness assurance | protected-variable refs, decision-variable refs, and outcome-variable refs, permitted-path refs and prohibited-path refs, fairness estimand refs, causal-use question refs, support basis refs, support record refs and verdict refs |
| causal-representation-validation shift | `CausalVariableRepresentationRecord`, learned causal-variable admissible use | intervention-validity, mechanism-invariance, abstraction-fidelity, counterfactual-query-preservation, representation-shift refs, OOD refs, supported-causal-variable-use refs, and unsupported-causal-variable-use refs |
| off-policy or causal-RL evaluation shift | `OffPolicyCausalEvaluationProfile`, causal action-policy admissible use, policy parity | behavior-policy refs and evaluation-policy refs, sequential horizon refs, adaptive policy class refs, unit-history conditioning refs, overlap refs and support-basis refs, policy transportability refs, estimator and uncertainty refs |
| simulation-validation shift | `simulationOnlyCounterfactualOutputBasis`, bounded model-supported counterfactual use | counterfactual model assumption refs, simulation validation refs, `CausalUseSupportStatement` and `CausalUseUnsupportedStatement` refs, sensitivity and rival-cause refs |

These sentinels do not mint new `RSCRTriggerKindId` values. They are domain-facing payload distinctions carried under the canonical trigger kinds governed by `G.Core`, usually evidence-publication edit, edition-pin change, policy-pin change, telemetry delta, freshness or decay event, or tokenization or name change.

#### G.11:4.4 - Extensions (pattern-scoped; non-core)

Discipline-specific refresh strategies and generator-specific wiring live as `GPatternExtension` blocks. Scheduling, ordering, priority, and budget policy for the refresh queue are not separate extension semantics: `G.11` governs the required policy pins on `RefreshQueue` and `RefreshPlan@Context`, while `A.15` keeps WorkPlanning separate from executed Work.

##### G.11:Ext.TriggerAliases

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

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.CrossingBundleEdit, RSCRTriggerKindId.PenaltyPolicyEdit, RSCRTriggerKindId.MaturityRungChange, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit}`
**Notes (wiring-only):** This block **does not define** what `T0…T7` mean; it only preserves the labels and requires docking via `G.Core.TriggerAliasMap.G11`.

##### G.11:Ext.DecayAndDebt

**PatternScopeId:** `G.11:Ext.DecayAndDebt`
**GPatternExtensionId:** `DecayAndDebt`
**GPatternExtensionKind:** `DisciplineSpecific`
**GoverningPatternId:** `B.3.4` (freshness and decay semantics)
**Uses:** `{B.3.4, G.6}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `FreshnessWindowDeclRef` (or equivalent window pin, as defined by the governing definition)
* `DecayPolicyIdRef` or `EpistemicDebtBudgetRef` (policy-bound)
* `PathSliceId[]` (affected evidence carriers)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.FreshnessOrDecayEvent, RSCRTriggerKindId.EvidencePathOrSourceRelationEdit, RSCRTriggerKindId.BaselineBindingEdit}`
**Notes (wiring-only):** Any budget or priority logic remains policy-bound; `G.11` only wires decay events to refresh planning.

##### G.11:Ext.QDRefreshWiring

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
* `PathSliceId` (archive or illumination scope) and `policy-id` for emitted telemetry triggers

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** `G.11` does not restate QD semantics; it ensures pins are present so reruns are comparable.

##### G.11:Ext.OEERefreshWiring

**PatternScopeId:** `G.11:Ext.OEERefreshWiring`
**GPatternExtensionId:** `OEERefreshWiring`
**GPatternExtensionKind:** `MethodSpecific`
**GoverningPatternId:** `C.19` (open-ended exploration and exploration-exploitation logistics)
**Uses:** `{C.19, G.5, G.8, G.9}`
**`⊑` and `⊑⁺`:** `∅`
**Required pins, edition pins, and policy pins (minimum):**

* `TransferRulesRef.edition`, `EnvironmentValidityRegion` (when OEE is declared by the governing patterns)
* `GeneratorFamilyId` and `TransferRulesRef` wiring pins (as published by the governing definitions)
* telemetry scope pins (`PathSliceId`, `policy-id`)

**RSCRTriggerKindIds:** `{RSCRTriggerKindId.EditionPinChange, RSCRTriggerKindId.TelemetryDelta, RSCRTriggerKindId.PolicyPinChange}`
**Notes (wiring-only):** Any OEE method semantics live with the governing definition; this module only wires refresh triggers to comparable reruns.

##### G.11:4.4a - Scheduling and priority policy pins

Scheduling strategies (bandit-style allocation, queueing, cadence policies, early stopping, or manual priority rules) may influence the order and budget of refresh work, but they do not define trigger meaning, action semantics, parity semantics, shipping semantics, or Part-G-wide defaults.

`G.11` therefore treats scheduling as policy-bound refresh planning:

* `RefreshPriorityPolicyIdRef` names the policy used to order or prioritize queue items.
* `BudgetDeclRef` names the time, compute, cost, risk, or cadence boundary for the planned refresh.
* `RSCRTriggerKindId[]` still comes from `G.Core`; scheduling policy does not mint trigger kinds.
* planned refresh remains `RefreshPlan@Context` under WorkPlanning; executed refresh remains `RefreshReport@Context` or Work-bound audit.

If no priority or budget policy is declared, no scheduling heuristic is admissible by appearance; the plan must either use the ordinary queue order or state the missing policy pin as a blocker.

### G.11:5 - Archetypal Grounding — System and Episteme (informative; Tell–Show–Show)

**`U.System` illustration — Safety-critical maintenance loop (pump and calibration).**
A centrifugal pump is serviced under a documented procedure (method description). Sensors report vibration drift (telemetry), and a calibration standard is updated (edition bump). `G.11` does not “rebuild the whole maintenance doctrine”: it emits a refresh plan scoped to the affected inspection slices and publishes a refresh report with pins to the updated standard edition and the evidence or source relations. Deprecation notices are issued for obsolete thresholds in the procedure’s acceptance clauses (by governing pattern), preserving ID continuity.

**`U.Episteme` illustration — Living review and benchmark pack (claims and parity).**
A claim sheet behind a shipped SoTA pack changes (new evidence, retraction, or revised measurement definition). Bridges are recalibrated, affecting CL or plane penalties. `G.11` ingests canonical trigger kinds, computes the minimal closure over affected `PathSliceId`s, schedules targeted parity reruns, then re-ships the pack through the pattern governing shipping semantics while publishing an edition bump log that makes the evolution replayable.

### G.11:6 - Bias-Annotation (informative)

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**.

* **Arch bias (toward explicit wiring).** Risk: authors feel “over-pinned.” Mitigation: keep the minimum pin set small; push scheduling sophistication into extensions and policies.
* **Gov bias (toward audit over speed).** Risk: refresh becomes bureaucratic. Mitigation: the kit is intentionally thin: refresh queue entries, `RefreshPlan@Context`, and `RefreshReport@Context` stay explicit, while action semantics remain delegated to governing definitions.
* **Onto and Epist bias (toward one governing definition semantics).** Risk: teams try to localize trigger meaning for convenience. Mitigation: alias docking is allowed, but semantics stay in `G.Core`.
* **Prag bias (toward minimal recomputation).** Risk: under-refresh if closure is too narrow. Mitigation: require closure rationale and allow explicit “scope wideners” as policy-bound pins.
* **Did bias (toward readable, reusable artefacts).** Risk: oversimplified examples. Mitigation: maintain System and Episteme grounding and keep SoTA-echoing explicit.

### G.11:7 - Conformance Checklist (normative)

| ID                                                    | Requirement                                                                                                                                                                                                                                                                                                                                     | Purpose and Notes                                                                                                            |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **CC‑G11‑CoreRef**                                    | A conforming `G.11` artefact **MUST** satisfy the **effective** core conformance set implied by the `GCoreLinkageManifest` in `G.11:4.1` (profile expansion plus explicit deltas; delegated to `G.Core`).                                                                                                                                       | `G.11` is conformant only if the relevant `G.Core` invariants and trigger discipline are satisfied. |
| **CC‑G11.1 (Slice-scoped planning).**                 | A conforming `RefreshPlan@Context` **SHALL** be scoped to `PathSliceId[]` (preferred) or `PatternScopeId[]` and **SHALL** record canonical `RSCRTriggerKindId` for each planned cause. Pack-wide reruns **MAY** occur only if the declared dependency closure spans all slices; the closure rationale **SHALL** be recorded.                    | Prevents full-rerun mania while keeping a safety escape hatch explicit and auditable.                                      |
| **CC‑G11.2 (Edition discipline; QD and OEE wiring).**     | When QD, OEE, or both are active, a conforming `RefreshPlan@Context` and `RefreshReport@Context` **SHALL** satisfy the required pin, edition, and policy wiring of the applicable extension blocks: `G.11:Ext.QDRefreshWiring`, `G.11:Ext.OEERefreshWiring`, or both. **`.edition` SHALL apply only on `…Ref`.** Missing required pins **SHALL** block publication. | Keeps replayability strict while keeping method-specific pin lists inside the applicable extension blocks.                  |
| **CC‑G11.3 (Telemetry-metric admissibility).**             | If a refresh publishes Illumination, QD, or OEE outcomes, it **SHALL** publish **Q, D, and QD‑score** and any coverage or regret as **telemetry metrics** and **IlluminationSummary** as a **telemetry summary**; these values **SHALL be excluded from dominance** unless a CAL policy explicitly promotes them, and the promoting **policy id SHALL be recorded** in SCR-visible evidence bindings through the cited governing patterns.                                                                                                      | Prevents covert scalarisation and keeps “telemetry vs order” separation explicit.                                          |
| **CC‑G11.4 (Bridge penalties).**                      | Any refresh reacting to Bridge or plane changes **SHALL** satisfy `CC‑GCORE‑PEN‑1` (delegation), and **SHALL** publish `CL`, `CL^k`, `CL^plane`, and the relevant `Φ`, `Ψ`, and `Φ_plane` policy ids with loss notes so penalties are assigned to `R_eff` only (F and G invariant).                                                                                                                                | Keeps penalty assignment auditable during refresh.                                                                            |
| **CC‑G11.5 (Selector invariants).**                   | Any orchestrated re‑selection or selected-set or archive update **SHALL** (i) satisfy `CC‑GCORE‑SET‑1` (delegation), and (ii) cite the selector governing definition (`G.5`) under an unchanged admissible `ComparatorSet` (edition‑pinned where applicable), returning **sets** (`Pareto` or `Archive`) and introducing **no scalarisation** inside `G.11`.                                                                                                                       | Prevents refresh from changing order semantics.                                                                            |
| **CC‑G11.6 (Crossing visibility).**                   | All refresh actions that touch cross-context reuse **SHALL** satisfy `CC‑GCORE‑CROSS‑1` (delegation) and the GateCrossing visibility harness (e.g., `E.18`): `CrossingRef`, BridgeCard, UTS, and `CL` or `Φ_plane` policy ids. Missing or non-conformant crossings **SHALL** block publication.                                                                                                                                 | Prevents “silent crossings” under refresh.                                                                                 |
| **CC‑G11.7 (Decay governance).**                      | When refresh is triggered by freshness or decay events, the refresh outputs **SHALL** choose and record a governance outcome (**Refresh**, **Deprecate**, or **Waive**) with **budget notes** (policy-bound), and **SHALL** publish the decision through `DeprecationNotice@Context` and related pins plus SCR-visible evidence bindings through `G.6` or cited governing patterns.                                                                                                                                                | Turns epistemic debt into explicit, comparable governance artefacts.                                                       |
| **CC‑G11.8 (No default smuggling).**                  | A conforming `G.11` refresh artefact **SHALL NOT** introduce new defaults for `PortfolioMode`, dominance, Γ-fold, or guard behavior. If orchestrated steps rely on defaults, the artefact **SHALL** cite each default's governing definition through `G.Core.DefaultGoverningDefinitionIndex` and the applicable governing patterns rather than restating defaults inside `G.11`.                                                                                                                                            | Protects default definition-citation discipline under orchestration pressure.                                                     |
| **CC‑G11.9 (Targeted RSCR before republication).**    | Before any refresh result is republished downstream (e.g., parity report updates, pack re-shipping, dashboard slice updates), the execution **SHALL** run or cite a targeted RSCR or regression check for the affected scope and record `RSCRRefs[]` or equivalent refs in `RefreshReport@Context`; exceptions **SHALL** be expressed as `degrade` or `abstain` outcomes (policy-bound) rather than silent skips.                                                                                         | Preserves “refresh ≠ vibes” by making regression gating explicit and slice-scoped.                                         |
| **CC-G11.10 (Causal-use refresh sentinels).**          | When a refreshed publication or output consumes `C.28`, a conforming `RefreshPlan@Context` **SHALL** include causal-use sentinel payload distinctions when counterfactual realizability, counterfactual-data identification and bounding, target-trial reporting, causal fairness, causal representation validation, off-policy and causal-RL evaluation, or simulation validation can change supported use, unsupported use, support verdict, assurance, parity, or downstream selection. | Keeps moving causal SoTA from silently invalidating shipped causal-use results while preserving `G.Core` trigger governance. |

### G.11:8 - Common Anti-Patterns and How to Avoid Them (informative)

| Anti-pattern                       | Symptom                                                           | Why it fails                                             | Repair                                                                            |
| ---------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Full-rerun mania**               | Any edit triggers a global rebuild                                | Costs explode; drift hides (no scope rationale)          | Enforce slice-scoped plans (CC‑G11.1); require closure rationale for global scope |
| **Editionless telemetry**          | Telemetry lacks `…Ref.edition`                                    | Reruns are non-comparable; parity breaks                 | Block publication on missing pins (CC‑G11.2)                                      |
| **Alias-as-semantics**             | `T*` labels are treated as meaning                                | Trigger meaning fragments; regressions become untestable | Dock aliases through `G.Core.TriggerAliasMap.G11`; record canonical ids               |
| **Silent crossing during refresh** | Refresh changes context or plane assumptions without crossings       | Violates crossing visibility; penalties become hidden    | Require crossing pins and E.18 visibility; block publication (CC‑G11.6)             |
| **Default smuggling**              | Refresh introduces “helpful” default dominance or `PortfolioMode` behavior | Competing defaults appear; downstream arguments drift    | Cite governing definitions through `G.Core.DefaultGoverningDefinitionIndex` (CC‑G11.8)                              |
| **Debt-by-prose**                  | “We decided not to refresh” exists only in narrative              | Not comparable; cannot be tested                         | Emit a DeprecationNotice (incl. a Waive outcome, if used) with pins (CC‑G11.7)    |

### G.11:9 - Consequences (informative)

* **Selective, replayable upkeep.** Refresh becomes a controlled planning and execution loop rather than an implicit “maintenance vibe.”
* **Stable semantics with flexible operations.** Trigger meaning is centralized (`G.Core`), while scheduling sophistication can evolve as policy-bound extensions.
* **Clear governing-definition assignment boundaries.** Orchestration coordinates governing definitions; it does not redefine their semantics (shipping remains `G.10`, selection remains `G.5`, etc.).
* **Cost: pin discipline overhead.** Authors must carry enough ids, editions, and policies to make refresh comparable. This is intentional: it replaces hidden drift with explicit wiring.

### G.11:10 - Rationale (informative)

`G.11` is intentionally a **thin orchestration governing definition**:

* The refresh loop is powerful enough to coordinate reruns and republishing, but **too thin to become a second spec**. That is why trigger semantics, invariants, and defaults are delegated to `G.Core`.
* The kit is split across the **P2W planning-to-work boundary** so that WorkPlanning plan items remain planning references and executed work remains auditably executed work.
* Alias stability is maintained by allowing trigger aliases (`T0…T7`) while prohibiting them from becoming semantic authorities.

### G.11:11 - SoTA-Echoing — Post‑2015 practices aligned (informative)

Each entry follows: **claim → practice → source → alignment → adoption status**.

0. **Queue-7 QD currentness requires visible survey support.**
   Practice: current QD work is surveyed as approaches, applications, and challenges, with archive, diversity, descriptor, and evaluator-currentness concerns still live.
   Source: `A survey on Quality-Diversity optimization: Approaches, applications, and challenges`, Swarm and Evolutionary Computation 2026, DOI `10.1016/j.swevo.2025.102240`.
   Alignment: `RefreshCurrentnessLine@Context` may name selected set, `Front`, `Q-front`, `ExplorationArchive`, `Archive`, portfolio lineage, descriptor or distance edition, and path-slice scope, while `C.18`, `C.19`, and `G.5` keep archive, pool, and selected-set meanings.
   Adoption: **Adopt and bound** (survey support changes refresh currentness fields and boundaries; it is not the governing ontology source).

0a. **Open-ended engineering outputs need source and evaluator currentness.**
   Practice: self-improving-agent, AlphaEvolve-style, and DeepEvolve-style lines use generated variants, external knowledge, evaluators, tests, archives, and empirical validation.
   Source: Darwin Godel Machine `arXiv:2505.22954`, AlphaEvolve `arXiv:2506.13131`, and DeepEvolve-style deep-research augmentation `arXiv:2510.06056`.
   Alignment: G.11 refresh records carry source, evaluator, descriptor, policy, edition, lineage, and report refs; generated method text, evaluator success, and archive update keep their governing patterns.
   Adoption: **Adopt and adapt** (refresh tracks currentness and smallest affected scope; it does not accept generated text as proof, gate passage, or performed work).

1. **Continuous refresh is necessary in deployed evaluation pipelines.**
   Practice: production ML systems use monitoring, retraining, and reevaluation triggers and insist on reproducibility hooks.
   Source: Breck et al., *The ML Test Score* (`arXiv:1706.04599`, 2017); Amershi et al., *Software Engineering for Machine Learning* (ICSE-SEIP 2019).
   Alignment: `G.11` formalizes triggers as typed causes and forces edition and policy pins for replay.
   Adoption: **Adopt and adapt** (adapted to id-based, PathSlice-scoped refresh rather than “retrain everything”).

2. **Non-stationarity requires explicit drift and decay handling, not ad-hoc updates.**
   Practice: continual learning emphasizes non-stationarity as a first-class maintenance condition.
   Source: Parisi et al., *Continual Lifelong Learning with Neural Networks* (`arXiv:1802.07569`, 2019); De Lange et al., *A Continual Learning Survey* (`arXiv:1909.08383`, 2021).
   Alignment: `B.3.4` supplies decay semantics; `G.11` wires decay events into refresh planning and controlled deprecation.
   Adoption: **Adapt** (refresh of conceptual artefacts and evidence closures, not untracked model mutation).

3. **Quality-Diversity requires archive semantics and comparability under descriptor and distance evolution.**
   Practice: QD methods treat the archive as the primary result and track changes under policy and edition conditions.
   Source: contemporary QD families such as CMA-MAE (`arXiv:2205.10752`) and differentiable QD (`arXiv:2106.03894`).
   Alignment: QD-specific meaning lives with the governing patterns; `G.11:Ext.QDRefreshWiring` ensures edition pins and scope pins exist so targeted archive refresh is admissible.
   Adoption: **Adopt** (set and archive preservation; no covert scalarization).

4. **Open-endedness co-evolves environments and agents; transfer rules must be versioned.**
   Practice: POET-class open-ended systems require explicit transfer rules and environment validity constraints.
   Source: Wang et al., POET (`arXiv:1901.01753`, 2019); later generator-family claims require a named `G.2` SoTA pack or exact current source.
   Alignment: `G.11:Ext.OEERefreshWiring` requires `TransferRulesRef.edition` and scope pins so refresh reruns remain comparable and auditable.
   Adoption: **Adopt and adapt** (adapted to Part G pin and UTS publication discipline).

5. **Efficient orchestration benefits from bandit and early-stopping scheduling, but it must not become semantics.**
   Practice: modern hyperparameter and experiment scheduling uses bandit-style resource allocation and asynchronous early stopping.
   Source: ASHA (`arXiv:1810.05934`) and BOHB (`arXiv:1807.01774`) as representative post-2015 scheduling practice.
   Alignment: scheduling is expressed as `RefreshQueue` and `RefreshPlan@Context` policy pins (`RefreshPriorityPolicyIdRef`, `BudgetDeclRef`) so core semantics remain stable and WorkPlanning stays separate from executed Work.
   Adoption: **Adapt** (useful practice, but quarantined outside core norms).

### G.11:12 - Relations

**Builds on:** `G.Core` (Part‑G invariants; RSCR trigger catalogue; alias docking; Default Governing Definition Index), `G.6` (EvidenceGraph, `PathId` and `PathSliceId`), `G.7` (Bridge sentinels; CL, Φ, and plane pins), `G.5` (selector and set-return), `G.8` (bundle telemetry hooks), `G.9` (parity), `G.10` (shipping hooks), `B.3.4` (freshness and decay), `E.18` (GateCrossing visibility).
**Coordinates with:** `G.12` (dashboard telemetry pins), `C.18` and `C.19` archive, front, and live-pool policy pins, `C.32.P2S` when telemetry, decay, or freshness reopens architecture problem-to-structure carry-through, `C.23` (SoS-LOG branches and maturity ladders), `C.28` (causal-use support records, support verdicts, supported-use values, unsupported-use values, and SoTA-sensitive causal-use sentinel payloads), `F.15` (RSCR harness publications, when present).
**Publishes to:** UTS (refresh plan, refresh report, deprecations, edition bumps), and to the relevant governing patterns’ publication faces, forms, or units through delegated actions.

### G.11:End

## G.12 — DHC Dashboards (Discipline‑Health time‑series; admissible telemetry; generation‑first)

**Tag:** Architectural kit pattern (conceptual; notation‑independent; dashboard‑kit governing definition)

**Stage:** design‑time authoring **→** run‑time computation & publication (series and slices); **refresh/RSCR‑wired**

**Primary hooks:** **G.Core** (core invariants, linkage catalogues, RSCR trigger catalogue, Default Governing Definition Index), **C.21** (DHC slots + `DHCPack` / `DHCMethodSpec` / `DHCSeries` artefacts), **G.6** (EvidenceGraph; `PathId`/`PathSliceId` citation), **G.7** (Bridge calibration / CL & `Φ/Ψ/Φ_plane` policy surfaces; when crossings/plane routing is used), **G.11** (telemetry‑driven refresh/decay orchestration), **G.5** (selector set-result / set‑returning outputs, when dashboard consumes performance trade‑offs), **A.19** (CN‑Spec governance card), **G.0** (CG‑Spec legality gate), **F.17/F.18** (UTS + twin labels), **E.5.2** (notation independence), **E.10** (LEX discipline).
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
* **Set‑returning discipline survives into views.** Dashboards must not silently scalarize partial orders or selector selected-set results; any scalarization/promotion is an explicit governing-pattern policy cited through **G.Core** conformance; semantics are governed by the relevant pattern or policy.
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
  entityOfConcern := ⟨GroundingHolon, ReferencePlane⟩,
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
If the dashboard depends on (i) selector set-result outputs, (ii) QD illumination / archive telemetry, (iii) open‑endedness telemetry, (iv) maturity ladder views, or (v) pack inclusion, then the relevant `GPatternExtension` block(s) in `G.12:4.9` MUST be present and their pins MUST be satisfied.

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

##### `G.12:Ext.PortfolioTelemetry` — selector set-result integration panel

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
| **G.12‑3 `Integrate_PortfolioTelemetry`** *(extension‑gated)* | Integrate selector set-result evidence into a slice/series | See `G.12:Ext.PortfolioTelemetry` | Extension‑gated fields / telemetry pins |
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
| **CC‑G12.4** | **Set‑returning selection is preserved.** If the dashboard consumes selection / set-result outputs, it MUST preserve set‑return semantics and MUST publish the resolved `DominanceRegime` and `PortfolioMode` by citing each default's governing definition (via `G.Core.DefaultGoverningDefinitionIndex`) rather than inventing local defaults. Any promotion of illumination/telemetry into dominance MUST cite the governing-pattern policy (typically CAL) and be auditable via evidence paths. | Check for set-result outputs; check that any scalar headline is view‑only; check citations to default governing definitions/policies. |
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
**Coordinates with:** `G.5` *(when selector set-result outputs are consumed)*, `G.7` *(when crossings/plane routing or `CL/Φ/Ψ/Φ_plane` policy pins are used)*, `G.8` *(when maturity ladder view is included)*, `G.10` *(when dashboard slices are shipped)*.
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

1. **Register source editions.** Author `ExternalIndexCard@Context` for each external source/snapshot used for SoTA authoring, including `ExternalEdition` and the `entityOfConcern` plane anchor.
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
* **Generation‑first authoring becomes cheaper.** External sources become controlled inputs into SoTA synthesis and declared set-result exploration, not ad‑hoc audit decoration.
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

# **Part H - Reserved**

# **Part I – Annexes & Extended Tutorials**

| §   | ID & Title                  |  Concise reminder                                                |
| --- | --------------------------- | --------------------------------------------------------------- |
| I.2 | Expanded Entry Disambiguation Cases | Expanded entry-disambiguation cases for high-risk or compact-insufficient first-entry comparison; compact `E.11` entry cues plus local Problem frames are complete when enough. |

## I.2 - Expanded Entry Disambiguation Cases

`I.2` is the canonical publication unit for `ExpandedEntryDisambiguationCase`
entries in this architecture. An `I.2` item expands one compact `E.11`-distributed
entry cue, README scenario, ToC query cue, or local pattern `Problem frame` when
first-pattern choice is high-risk, often misclassified, repeatedly failed,
retrieval-facing, or too dense for compact guidance.
Its `E.11` use is limited to disambiguation, wrong-pattern rejection,
entry-load reclassification, and admissible entry stop.

An `ExpandedEntryDisambiguationCase` is a bounded entry case. It is not
`U.Work`, not a workflow, not a route script, and not an execution trace.

`I.2` carries expanded disambiguation only when README scenarios, ToC query cues,
`E.11` entry-distribution cues, or local `Problem frame` recognition are
insufficient for one high-risk, often-misclassified, repeatedly failed,
retrieval-facing, or materially new first-entry pattern-comparison set. A compact
entry cue plus the pattern `Problem frame` is a complete admissible entry result
when it is enough.

Each expanded entry-disambiguation case keeps recoverable:

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
- **Tempting wrong pattern:** harden the cue into `A.6.P`, `C.16.Q`, `A.6.A`,
  or `C.25` before it is stable enough to be a claim, action, or quality
  object.
- **Disambiguating fact:** the phrase still needs preservation and entry-load
  typing; it is not yet an endpoint claim.
- **Decision movement:** if the phrase is still a cue, stay in `C.2.LS` /
  `A.16`; if it must be preserved across a seam, inspect `A.16.1` / `B.4.1`;
  if it is already a boundary claim, inspect `A.6.B` / `A.6.C`; if it is being
  forced into a quality endpoint or action-invitation endpoint too early, reject `C.16.Q`, `A.6.A`, and
  `C.25` for now.

- **Actual governing FPF pattern body or projection role:** `C.2.LS`, `A.16*`, and
  `B.4.1` are the first governing patterns for cue preservation and entry plurality;
  `A.6.B` / `A.6.C` become first governing patterns only after boundary claim structure is
  actually being made.
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
  `A.6.P` for relation wording; `C.16.Q` for quality wording; `A.6.A` for
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
  misclassification makes an expanded entry-disambiguation case necessary.
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

- **Case signal:** "We need to explain the same EntityOfConcern for another audience."
- **Initial uncertainty:** explanation, rendering, repair, representation
  transition, and comparison are all nearby, and the reader can accidentally
  mint one second EntityOfConcern.
- **Plausible candidate patterns:** `A.6.3.CR`, `A.6.3.RT`, `E.17.EFP`,
  `E.17.ID.CR`.
- **Nearby patterns:** `E.17.AUD.LHR` for pressured-head local repair;
  `E.17.AUD.OOTD` for `PublicationUnit` stability.
- **Tempting wrong pattern:** explanation-as-new-object or repair-as-second-rule
  track.
- **Disambiguating fact:** the same-EntityOfConcern rewrite/comparative-reading case stays the same; only rendering,
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


# SOURCE_FILE: Narrativization-and-Narrative-Studies-Principles-Framework.md
---
# Narrativization and Narrative Studies Principles Framework

> **Framework family:** Domain Principle Framework
> **Package edition ref:** `NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-06-30`
> **Dependency:** FPF Core, especially `A.6.3.NAR`, `A.6.3.RT`, `A.6.3.CSC`, `E.17.EFP`, `A.6.P`, `C.2.LS`, `C.2.4` through `C.2.7`, `A.16.1`, `A.16.2`, `C.16.Q`, `E.10`, `F.18`, `C.33`, `C.34`, `C.35`, `D.1` through `D.5`, `A.10`, `B.3`, `B.4`, `A.19.ECS`, `C.16`, `E.4.DPF`, `E.4.PFR`, `G.2`, `E.21`, `E.22`, `E.23`, and `G.11`

Use this package as a small FPF-style Domain Principle Framework publication carrier: table of contents, readme, preface, framework context, pattern bodies, relation records, acceptance cases, and refresh route.

# Table of Contents

Use the Table of Contents when you already know the DPF pattern or support section you need. Use the readme when you are deciding whether narrativization work is the right entry. Use the Preface when you need the cross-cutting ideas that make the pattern set cohere. Pattern bodies contain the action-guiding text.

How maps are reached during work: do not read support maps front-to-back unless you are designing or refreshing the package. During ordinary narrative work, enter a map only when a pattern relation, a low-value repair action, source-return condition, or boundary question points there.

| Work trigger | Map to open | Why |
| --- | --- | --- |
| The narrative route is architecture-mediated, uses views and viewpoints, candidate structures, structural-information capture, correspondence, or actual-structure feedback. | Architecture and Narrative Work Bridge | Translate narrative wording into the relevant FPF architecture owners without making Core depend backward on this DPF. |
| Style, hook, cue, coarsening, explanation, relation wording, quality wording, or precision restoration becomes load-bearing. | Semiotic And Language-Precision Bridge | Find the FPF owner before treating craft vocabulary as ontology or quality. |
| A source line supports a narratology, cognition, teaching, ethics, or generation claim; the source is absent, stale, or too narrow. | Source Use And Refresh Map | Bound the claim and route refresh through `G.2`/`G.11`. |
| A local term such as route, viewpoint, actant, epiplexity, engagement, generated plan, or learning route risks becoming a new kind. | DPF Precision Restoration And Owner Map | Recover the kind, owner, use boundary, and blocked overread. |
| The question is DPF prefix, edition dependency, package relation, or refresh route rather than narrative content. | Name And Edition Route or DPF Relation Records | Check package-level identity and dependency without mixing it into pattern bodies. |

| Locus | Title | Kind | Use |
| --- | --- | --- | --- |
| Readme | First practical entries | Informative | Choose the first DPF entry from the working problem. |
| Preface | Cross-cutting ideas and principles | Informative | Understand narrativization as source-structure-to-sequence work rather than style polish. |
| Package carrier structure-account note | What this DPF publication carrier exposes, for whom, captured structure, deliberately coarsened or deferred structure, and source-return boundary | Framework-level use note | Check what part of narrative-studies structure this package exposes before treating it as domain coverage. |
| Framework context | Package boundary and owner routing | Normative package frame | See dependency, owner, and reliance limits. |
| `NSTD.1` | Source-Structure Intake and Narrative Purpose | DPF pattern | Start from source structures and declared use before message or theme. |
| `NSTD.2` | Structure-to-Sequence Ordering | DPF pattern | Declare the ordering rule that turns structure into narrative sequence. |
| `NSTD.3` | Source Mechanism, Event Model, and Coherence | DPF pattern | Preserve mechanism, dependency, event, or state-change reconstruction. |
| `NSTD.4` | Voice, Focalization, and Agency | DPF pattern | Use viewpoint and protagonist choices without false agency or responsibility. |
| `NSTD.5` | Engagement, Attention, and Motivation | DPF pattern | Use engagement without turning attention into truth, permission, or authority. |
| `NSTD.6` | Declared-Use Narrative Rendering Quality Evaluation | DPF evaluation pattern | Evaluate one narrative rendering version for one declared use. |
| `NSTD.7` | Automated Narrativization and Story Planning | DPF pattern | Split generated carrier, admitted source basis, method, admission, evaluation, evidence, and responsibility. |
| `NSTD.8` | Learning-Route Narrative Rendering and Reconstruction Return | DPF pattern | Design and evaluate a learning route without moving teaching material into pattern bodies. |
| Acceptance cases | FPF seminar, franchise continuation, homotopy explanation, live event commentary | Use-test support section | Test the pattern set across heterogeneous narrative work. |
| Support maps | Architecture bridge, semiotic bridge, source use, precision map, naming and edition route | Reference | Use only when a pattern relation, low-value repair action, source-return condition, or owner-routing doubt points to one of the maps. |
| PFR records | DPF relation and edition records | Relation-record section | State specialization, source reuse, evaluation, generated-carrier, teaching publication-carrier, and ethics routing relations. |
| Refresh route | Source, evaluation, and edition refresh | Refresh-route section | State what must return to `G.2`, `E.22`, `E.23`, and `G.11`. |

# Readme - First Practical Entries

Narrativization and Narrative Studies DPF helps when a structure-bearing source must become a sequence that humans can follow, remember, teach, discuss, or generate, while source structure and source return remain recoverable.

Treat this as a problem-solving DPF, not an ontology of narratives and not a guide to chatting about narrative. Its patterns target recurring narrative-work failures: starting from theme before source structure, hiding temporal posture, choosing story order by habit, making events happen because the writer wants them, treating viewpoint as agency, letting engagement become truth or permission, trusting generated fluency, and copying blocked technical structure into a bad learning route. The intended payoff is a set of source-grounded solution moves that make those failures harder.

Use this DPF when the project question is not only "how do we write this nicely?" but one of these:

- a source graph, architecture, proof dependency, event set, mechanism, evidence set, canon, or knowledge base must become a narrative route;
- a historical, live, or prospective source must be narrated without hiding which temporal posture and uncertainty obligations apply;
- a learning route must preserve source structure rather than only examples, analogies, mood, or slogans;
- a generated text or story plan must be admitted, evaluated, and repaired before reliance;
- engagement or viewpoint helps comprehension but may distort source structure, agency, ethics, evidence, or authority;
- a team needs to know whether a narrative rendering is good enough for a declared use.

Do not use this DPF when the live issue is only source evidence, publication layout, legal permission, ethics mediation, proof status, generated-carrier admission, or pattern quality. Use the direct FPF owner first, then return here only if source structure is being rendered as narrative.

## First Practical Entry 1 - Turn A Source Structure Into A Narrative Route

Start with `NSTD.1`, then `NSTD.2`. Name the admitted source basis, selected source structures, source temporal posture, rendering mediation mode, narrating or rendering worker, intended reader use, narrative purpose, ordering rule, preserved structure, lost structure, and source-return condition.

Typical first result: one `NarrativePurposeIntake@Context` plus one `NarrativeOrderingRule@Context`.

## First Practical Entry 2 - Repair A Fluent But Misleading Narrative

Start with `NSTD.3`, `NSTD.4`, and `NSTD.5`. Check whether readers can reconstruct events, mechanisms, dependencies, viewpoint, agency, engagement boundary, and source-return limits.

Typical first result: a repair note that lowers causal, agency, engagement, evidence, or assurance claims and points to the owner that can carry them.

## First Practical Entry 3 - Evaluate Rendering Quality For Declared Use

Start with `NSTD.6`. First confirm that the object is an admitted narrative rendering version for one declared use. Then evaluate `NarrativeRenderingEpiplexity`, ordering recoverability, event-mechanism support, viewpoint-agency discipline, engagement boundedness, owner routing, medium fit, and source-return readiness.

Typical first result: `NarrativeRenderingQualityResultRow@Context` rows with values, evidence basis, lowering reason, repair action, owner, and reopen condition.

For repeated improvement, package those rows as `NarrativeRenderingQualityEvaluationResult@Context` and prepare `NarrativeRenderingImprovementLoopInput@Context` for `E.22`/`E.23`. Do not count a style pass, prompt retry, extra drama, or generated variant as improvement until the changed rendering version or declared changed slice is re-evaluated through `NSTD.6`.

## First Practical Entry 4 - Use LLM Or NLG Output Safely

Start with `NSTD.7` and `C.35`. Treat the generated result as a produced carrier until admitted source basis, selected structure, generation method, admission note, losses, evaluation, and human responsibility are explicit.

Typical first result: `AutomatedNarrativizationAdmissionCase@Context`.

## First Practical Entry 5 - Build A Learning Route

Start with `NSTD.8`, then `NSTD.6`. Keep actual lessons, slides, scripts, exercises, seminar notes, and teaching examples in separate teaching or test-run files. Pattern bodies only govern the route, reconstruction tasks, source return, and evaluation.

Typical first result: `LearningNarrativeRoute@Context` plus narrative rendering quality result rows.

# Preface - Cross-Cutting Ideas And Principles

This DPF is not a story-writing manual and not an ontology of narrative. It is an FPF-grounded pattern set for one recurring transformation: selected source structure becomes a sequential narrative rendering for a declared human use. The patterns are organized around problems and repair moves, because the framework is useful only if it helps a narrative worker avoid known failures and choose better routes.

The central distinction is simple. A narrative rendering is not the admitted source basis, not the selected source structure, not evidence, not assurance, not a gate, not a decision, and not work authorization. It is a representation relation with ordering, salience, loss, recoverability, and source-return obligations.

Narrative work has temporal postures. A historical reconstruction, reverse-engineering account, live match commentary, prospective project scenario, future event preview, and fictional continuation can all be narrative renderings, but they do not carry the same admitted source basis, uncertainty, evidence, telemetry, or source-return obligations. This DPF therefore requires the source temporal posture before drafting and before evaluation.

Narrativization has two rendering mediation modes. In the direct source-structure mode, a situation, event stream, proof field, canon, evidence set, or admitted source pack is rendered into narrative without making architecture work the central owner. In the architecture-mediated mode, actual or possible holon structure is first understood through architecture work, architecture descriptions, views, viewpoints, architecture decisions, candidate structures, or telemetry, and then narrated for a declared reader or listener use. The rendering mediation mode decides when `C.33`, `C.34`, and architecture owners stay live.

Direct source-structure work is still structured work. The pattern set must not pretend that a writer's intuition or LLM generation magically selected the needed structures. If selection, reader-use hypothesis, ordering, and loss accounting stay implicit, the result is a candidate carrier or candidate prose, not a checked narrative rendering. Improvement then starts by reconstructing the hidden selection record before changing style, drama, or prompt wording.

Narrative work is role work. The narrator, writer, teacher, commentator, designer, or tool-mediated rendering worker chooses sequence, viewpoint, loss profile, and engagement devices. The intended reader or listener role constrains those choices. A narrative worker cannot ignore reader-role interests, but reader interest also does not create evidence, assurance, ethics, publication permission, or source authority.

Narrativization is similar to serialization in one important way: a non-linear or differently ordered source structure must be made readable as a sequence. That sequence preserves some relations and loses others. The DPF keeps that similarity, then adds narrative-specific concerns: event comprehension, viewpoint, engagement, agency cues, ethics, teaching, generated text, and rendering-quality evaluation.

Sometimes the selected structure to be rendered is a constraint-governed unfolding structure under FPF Core. The admitted source basis may be a `G.2` source pack, an architecture description, a pattern body, a source publication carrier, or another admitted episteme; the selected structure is the `U.Structure` recovered from that admitted source basis for the declared narrative use. A learning route, architecture narrative, generated route card, or story-like explanation may render only a `DemonstrativeUnfoldingSlice@Context` over a wider `A.22.CGUS` or `E.18.3` structure. In those cases this DPF governs narrative intake, ordering, evaluation, generation, and learning-route repair; `A.22.CGUS` or the local FPF governing pattern still governs the selected unfolding structure and its admissible next forms.

Narrative studies is the broad domain label here. Narratology is one source tradition inside it, not the whole domain and not Core ontology. Storycraft, science communication, teaching design, cognitive narrative research, NLG, story planning, and qualitative narrative analysis all supply useful distinctions. The DPF uses those distinctions only after mapping them to FPF owners.

Core boundary decision: this package depends on FPF Core; FPF Core must not depend back on this package. The Core admission from this campaign is the general `A.6.3.NAR` relation: selected source structure is rendered into a sequential narrative rendering for declared use with preservation, loss, admissibility, and source return visible; that rendering may then be carried by a publication or access carrier. The `NSTD.*` patterns stay DPF material because they use narrative-studies, narratology, storycraft, learning-design, NLG, and narrative-evaluation solution moves for narrative-work problems. If a later framework finds one of those moves recurring outside narrative work, it should return through a separate FPF amendment instead of silently treating this DPF as Core.

The first discipline is source return. A good narrative can foreground one route through the admitted source basis and selected source structure, but it must say when the reader needs to return to that basis or to the direct governing pattern again. This matters in architecture explanation, mathematical teaching, science communication, generated story planning, and franchise-continuation storycraft.

The second discipline is owner routing. Engagement is not truth. Viewpoint is not responsibility. Protagonist is not `U.Role`. Actant is not `U.RoleAssignment`. Generated fluency is not admission. A learning route is not the source framework. Each stronger claim goes to the FPF pattern that owns it.

The third discipline is evaluation before improvement. `NSTD.6` does not ask whether a narrative is beautiful in general. It evaluates one admitted narrative rendering version for one declared use under `NarrativeRenderingEpiplexity`, ordering recoverability, source-return readiness, bounded engagement, owner-routed claims, values, evidence basis, missingness rules, repair actions, and reopen conditions.

## Package Carrier Structure-Account Note

This all-in-one package file is a DPF publication carrier: its readme, preface, pattern bodies, and support sections publish a sequential explanatory route through selected narrativization and narrative-studies problem-and-solution structures for FPF users who need to design, evaluate, repair, or govern narrative renderings. The carrier is not a narrative by type, not the domain itself, not the source pack, not a proof that every narrative will work, and not a replacement for the FPF Core patterns it depends on.

This publication carrier is written mainly for FPF authors, teachers, technical communicators, architects, researchers, AI-tool builders, and reviewers who must turn source structures into reader-usable narratives without losing source return. It foregrounds the architecture of recurring narrative-work problems and solution moves: source-structure selection before theme, temporal-posture errors, rendering-mediation choice, ordering-rule failure, event or mechanism reconstruction, viewpoint and agency distortion, engagement overclaim, declared-use quality, generated-output admission, learning-route design, precision repair, ethics routing, and refresh.

The package deliberately coarsens, abstracts, omits, or defers other structures. This is not merely shortening one text into another. A narrative-studies source may first be understood through architecture-like structure selection, views, models, source packs, or examples, and this all-in-one DPF publication carrier then makes that selected structure available again for use. In architecture-mediated narrative-rendering cases, the return chain is `narrative rendering carried by this publication carrier -> architecture description or view -> architecture as selected structures in context -> wider source structures`; when no narrative rendering is present, the first step is `DPF publication carrier -> selected source structures`. Each arrow can lose structure. The carrier does not carry a full history of narratology, a genre-specific storycraft course, a complete learning-sciences curriculum, a full NLG or story-planning survey, legal publication advice, a replacement ethics theory, or all source-pack rows. Those return to the source-use map, upstream FPF patterns, local teaching material, domain sources, or a stronger DPF when the declared use needs them.

For this all-in-one publication carrier, the structure-capture question is qualitative rather than a universal score for narrativity:

```text
FrameworkCarrierStructureCapture@NarrativizationAndNarrativeStudiesPrinciplesFramework:
  evaluatedCarrierRef: NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-06-30
  declaredUse: help FPF users design, evaluate, repair, and govern narrative renderings
  selectedSourceStructureDenominator: narrativization as source-structure-to-sequence work, with narrative-studies, cognition, learning, ethics, NLG, and FPF architecture/representation owners as source traditions
  foregroundedStructure: recurring narrative-work problem situations, solution moves, source selection, rendering mediation, ordering, event and mechanism reconstruction, viewpoint and agency, engagement, quality evaluation, generated-output admission, learning-route design, precision repair, source return, and refresh
  intentionallyCoarsenedAbstractedOmittedOrDeferredStructure: full domain history, genre craft, full pedagogy, full NLG algorithms, legal permissions, complete source pack, and formal metric calibration
  qualitativeCarrierEpiplexityForDeclaredUse: 4
  whyNot5: heterogeneous probes show transfer across teaching, franchise continuation, mathematical explanation, and live-event narration, but field use, stronger source-pack discharge, and better accounting of source-to-architecture-to-publication/access coarsening would be needed before claiming near-complete domain capture
  sourceReturnCondition: return to pattern bodies, FPF governing patterns, source-use map, and local domain material whenever a narrative claim becomes evidence, assurance, ethics, legal permission, pedagogy, generation-method, or domain-expert authority
```

Read that `4` narrowly. It means this DPF publication carrier makes enough selected structure available for its declared authoring and evaluation use. It does not mean the package exhausts narrative studies, guarantees reader impact, or replaces domain expertise. A `5` would require stronger evidence that the package's selected structures are both sufficient and non-dominated for the declared reader families and acceptance cases, including evidence that important architecture-level or source-level structure was not silently lost in the publication/access route.

## Package Boundary And Owner Routing


This package is a Domain Principle Framework for narrativization and narrative studies. Its governed use is narrow: it helps practitioners solve recurring narrative-work problems by rendering selected source structures into narrative renderings for declared reader or listener use, while preserving source return, ethics routing, evidence routing, generated-carrier admission, evaluation, and refresh discipline.

The package does not redefine FPF Core. `A.6.3.NAR` remains the Core owner for the source-to-narrative relation. `NSTD.*` patterns specialize that Core relation for narratology, narrative communication, storycraft, teaching, and generated-narrative work. The DPF adds domain methods, cases, and evaluation scales; it does not mint new Core `U.*` kinds.

Intended readers are FPF authors, teachers, technical communicators, architects, researchers, and tool builders who must make narrative renderings useful without turning narrative fluency into source authority.

Non-use boundary: this package is not FPF Core, not a style guide, not a seminar script, not a storycraft course, not an ethics authority, and not evidence or assurance for generated narratives. Actual seminar outlines, slides, exercises, scripts, session notes, generated outputs, and field-test evidence or publication carriers belong in separate files and may be evaluated by this package.

## Pattern Index

| Pattern id | Pattern title | First use |
| --- | --- | --- |
| `NSTD.1` | Source-Structure Intake and Narrative Purpose | Start from selected source structure and declared use before message, theme, or engagement. |
| `NSTD.2` | Structure-to-Sequence Ordering | Choose and justify the ordering rule that turns source structure into a narrative path. |
| `NSTD.3` | Source Mechanism, Event Model, and Coherence | Keep mechanism, event, dependency, and update structure intelligible. |
| `NSTD.4` | Voice, Focalization, and Agency | Govern viewpoint and protagonist choices when they affect comprehension, responsibility, or source loss. |
| `NSTD.5` | Engagement, Attention, and Motivation | Use engagement without turning attention into truth, permission, or authority. |
| `NSTD.6` | Declared-Use Narrative Rendering Quality Evaluation | Evaluate one narrative rendering version for one declared use. |
| `NSTD.7` | Automated Narrativization and Story Planning | Keep generated narrative output grounded, constrained, admitted, evaluated, and repairable. |
| `NSTD.8` | Learning-Route Narrative Rendering and Reconstruction Return | Design and evaluate a learning route without placing teaching material inside patterns. |

## NSTD.1 - Source-Structure Intake and Narrative Purpose

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `NarrativePurposeIntake@Context`, a DPF-local relation record for one narrative rendering case.

### NSTD.1:1 - Problem frame

Use this pattern when a writer, narrator, teacher, architect, researcher, commentator, story designer, or tool starts with a message, lesson, theme, persuasive effect, desired memory, live commentary line, or future scenario before naming the source structures that must survive the narrative rendering.

First useful move: write `NarrativePurposeIntake@Context` with admitted source basis refs, selected source structures, source-structure selection rationale, source temporal posture, rendering mediation mode, narrating or rendering worker, reader-interest or use hypothesis, intended reader or listener role and use, narrative purpose, blocked purpose overread, source-return owner, and any ethics or assurance owner.

What goes wrong if missed: purpose absorbs admitted source basis and selected source structure. The narrative may become memorable, but readers cannot recover which structure was selected, which uncertainty was retained, or which claims need source return.

What this buys: the writer can choose a narrative aim without letting that aim widen evidence, assurance, ethics, policy, or work authority.

Not this pattern when the issue is only publication face, source-pack admission, evidence sufficiency, or ethics mediation. Use the direct owner and return here only when narrative purpose must be tied to selected source structure.

### NSTD.1:2 - Problem

Narrative purpose is useful because a narrative rendering is made for someone and for some use. But ordinary purpose language is often too broad: "make it inspiring", "tell the story", "explain the architecture", "make learners care". Those phrases do not say which structures must be preserved, which distinctions may be coarsened, and which downstream use is blocked.

### NSTD.1:3 - Forces

| Force | Tension |
| --- | --- |
| Reader usefulness vs source discipline | A narrative needs a purpose, but the purpose cannot replace selected source structures. |
| Motivation vs authority | Motivation helps attention, but it does not create evidence, assurance, ethics clearance, or work permission. |
| Domain vocabulary vs FPF owners | Narratology and communication terms help design, but source-use, evidence, ethics, and assurance claims have FPF owners. |
| Writing speed vs replayability | Fast writing starts from message; replayable writing starts from source structure and use. |

### NSTD.1:4 - Solution

Create one intake record before drafting or evaluating the narrative.

```text
NarrativePurposeIntake@Context:
  sourceBasisRefs:
  selectedSourceStructureRefs:
  unfoldingStructureRefs?:
  demonstrativeSliceRefs?:
  sourceStructureSelectionRationale:
  sourceTemporalPosture:
  renderingMediationMode: direct-source-structure | architecture-mediated | mixed
  architectureMediationRef?:
  sourceStructureOwnerRef?:
  narratingOrRenderingWorkerRef?:
  readerOrListenerRoleRefs:
  readerInterestOrUseHypothesis:
  intendedReaderOrListenerUse:
  narrativePurpose:
  blockedPurposeOverread:
  sourceReturnOwner:
  ethicsOrAssuranceOwner?:
  refreshCondition?:
```

Use `unfoldingStructureRefs?` only when one selected source structure is governed as a constraint-governed unfolding structure by `A.22.CGUS`, `E.18.3`, or a local FPF block. Use `demonstrativeSliceRefs?` only for the slice the narrative renders for the reader; the slice is not the whole selected structure.

Then apply these moves:

1. Name admitted source basis refs, selected source structures, source-structure selection rationale, and source temporal posture.
2. Name the rendering mediation mode and any architecture mediation, source-structure owner, or telemetry source that remains live.
3. Name the narrating or rendering worker, reader-interest or use hypothesis, and intended reader or listener role and use in project terms.
4. State the narrative purpose as a relation to the selected source structures and reader or listener use.
5. State what the purpose may not justify: evidence, assurance, policy, work, ethics, or decision use.
6. Name the source-return owner and any neighboring FPF owner.

Use the intake in four passes, not as one form-filling gesture.

| Pass | Question | Output |
| --- | --- | --- |
| Source pass | What admitted source basis or source pack is being rendered, and which selected source structures must remain recoverable for the declared use? | Source-basis refs or source-pack refs, selected source structure refs, and source-return condition. |
| Use pass | Who will use the narrative, for what work or understanding, and what must they be able to recover or decide not to decide? | Reader or listener role, reader-interest hypothesis, intended use, and non-use boundary. |
| Mediation pass | Is the work direct source-structure rendering, architecture-mediated rendering, or mixed? What temporal posture changes source obligations? | Rendering mediation mode, temporal posture, architecture mediation refs, and live telemetry or source-return refs. |
| Authority pass | Which claims are tempting but not granted by the narrative purpose? | Blocked purpose overread plus evidence, assurance, ethics, policy, work, and decision owner exits. |

The intake is good enough to compose only when the selected source structures can be stated without looking at the current prose version. If the only answer is "the important bits are the bits I happened to write about", selection is still hidden. Return to the admitted source basis, name candidate structures, and choose by reader use. If the reader use is also vague, stop at an orientation cue or source-pack note; do not present the carrier-borne content as an admitted narrative rendering.

Use contrast cases before drafting:

- Admissible: "This route helps new FPF readers reconstruct why `EntityOfConcern`, forces, and neighboring-pattern exits matter during pattern use." The selected structures are named and the use is reconstructive.
- Below floor: "Make the seminar inspiring so people like FPF." Motivation is a possible engagement device, but source structures and reconstruction use are missing.
- Wrong owner: "Use the narrative to prove FPF is correct." That is evidence or assurance work, not narrative-purpose work.

For prospective or fictional material, the selected source structure may come from a constrained source pack rather than from already-realized facts. The intake must still name the canon references, scenario assumptions, design constraints, or future-state hypotheses admitted for the case. "The story world wants it" is not a source-structure selection rationale; the worker must state which admitted source-pack constraints make the narrative route legitimate for private planning, teaching, or scenario exploration.

When `selectedSourceStructureRefs` includes a constraint-governed unfolding structure, name the Core governing pattern and the selected structure ref before purpose is finalized. The selected structure may be `ConstraintGovernedUnfoldingStructure@Context`, an `E.18.3` transformation-flow unfolding structure, a P2S local block, an improvement-loop block, or a narrative-ordering block under `A.6.3.NAR`. The narrative purpose may choose one `DemonstrativeUnfoldingSlice@Context` for reader use, but it must state what branches, alternatives, loops, constraints, admissible next forms, and direct exits are preserved or lost. The slice is not the whole selected structure and not a work order.

Use role-specific intake prompts when the worker is stuck.

| Worker situation | Prompt | Expected answer |
| --- | --- | --- |
| Teacher or trainer | "After the narrative, what should learners reconstruct from source without relying on my story?" | Source spine, reconstruction task, and source-return condition. |
| Architect or analyst | "Which structure, trade-off, candidate, telemetry, or decision memory must survive the narrative?" | Architecture or source-structure refs plus rendering mediation mode. |
| Scientist or researcher | "Which mechanism, calculation, failed attempt, source uncertainty, or unresolved tension is being rendered?" | Mechanism or event support, uncertainty, evidence owner, and source return. |
| Story designer | "Which canon, premise, agency, continuity, or causal plot constraint governs this route?" | Bounded source pack and non-publication boundary when needed. |
| Live commentator | "Which observation, inference, prediction, and later official source must stay distinguishable?" | Temporal posture, uncertainty markers, and refresh condition. |
| Tool builder | "Which part is admitted source basis, which part is method, which part is generated carrier, and who admits it?" | Split between admitted source basis, method, generated carrier, and admission owner; generated-carrier admission route; human responsibility. |

If the answer names only mood, audience reaction, style, genre, or desired conclusion, the intake is not ready. Those can be legitimate later choices under `NSTD.4`, `NSTD.5`, `C.2.LS`, or `E.17`, but they cannot select the source structure by themselves.

Minimum worked intake cases:

```text
NarrativePurposeIntake@FPFLearningRoute:
  sourceBasisRefs: selected FPF pattern bodies and relation records
  selectedSourceStructureRefs: EntityOfConcern discipline; problem frame; forces; solution; neighboring exits; quality and improvement loop
  unfoldingStructureRefs: A.22.CGUS only when the lesson explicitly teaches source-to-next-use unfolding
  demonstrativeSliceRefs: first seminar route through selected pattern-use positions
  sourceStructureSelectionRationale: learners must reconstruct how a practitioner chooses and uses a pattern
  sourceTemporalPosture: prospective planned learning route over current source corpus
  renderingMediationMode: direct-source-structure unless architecture-of-FPF explanation is opened
  narratingOrRenderingWorkerRef: teacher or course designer
  readerOrListenerRoleRefs: new FPF author or reviewer
  readerInterestOrUseHypothesis: learner needs usable entry, not complete monolith memory
  intendedReaderOrListenerUse: reconstruct one pattern-use route and apply it to a new case
  narrativePurpose: orient attention and sequence learning tasks around source-returnable pattern use
  blockedPurposeOverread: lesson is not evidence that FPF is correct and not replacement for pattern bodies
  sourceReturnOwner: FPF source patterns and teaching publication-carrier relation
  refreshCondition: FPF edition, learner telemetry, or route evaluation changes
```

```text
NarrativePurposeIntake@HomotopyExplanation:
  sourceBasisRefs: formal definitions, examples, diagrams, proof-status notes, and selected textbook or lecture source basis
  selectedSourceStructureRefs: definition dependency; example and counterexample relation; theorem prerequisite; formal-source return
  sourceStructureSelectionRationale: learner needs an intuitive route that preserves formal boundaries
  sourceTemporalPosture: retrospective or atemporal explanation over existing mathematical material
  renderingMediationMode: direct-source-structure unless a teaching architecture is explicitly used
  narratingOrRenderingWorkerRef: teacher, explainer, or tool-assisted author
  readerOrListenerRoleRefs: learner who must later distinguish intuition from proof
  readerInterestOrUseHypothesis: learner needs recoverable dependency order and analogy boundary
  intendedReaderOrListenerUse: use examples and return to formal statements without treating metaphor as theorem
  narrativePurpose: make abstractions followable while preserving proof-status boundary
  blockedPurposeOverread: narrative does not prove the theorem, replace notation, or authorize informal equivalence
  sourceReturnOwner: mathematical source or proof owner
  refreshCondition: source correction, learner failure, or changed learning objective
```

```text
NarrativePurposeIntake@LiveCommentary:
  sourceBasisRefs: live observations, official event feed, telemetry, recording, later official result
  selectedSourceStructureRefs: event order; score state; possession or control changes; actor roles; uncertainty markers
  sourceStructureSelectionRationale: listener needs orientation during an unfolding event stream
  sourceTemporalPosture: live unfolding source with later refresh
  renderingMediationMode: direct-source-structure
  narratingOrRenderingWorkerRef: commentator or live analyst
  readerOrListenerRoleRefs: listener following the event and later checking the official event record
  readerInterestOrUseHypothesis: listener needs distinction between observation, inference, prediction, and official correction
  intendedReaderOrListenerUse: follow the event without treating provisional interpretation as fact
  narrativePurpose: maintain orientation and attention under uncertainty
  blockedPurposeOverread: commentary is not official evidence, blame assignment, or final tactical analysis
  sourceReturnOwner: event source owner, official record, recording, telemetry
  refreshCondition: official correction, telemetry, or post-event evidence changes
```

```text
NarrativePurposeIntake@FictionalContinuationProbe:
  sourceBasisRefs: admitted canon or local source pack for private storycraft test
  selectedSourceStructureRefs: canon constraints; continuity; premise and theme; character agency; causal plot support
  sourceStructureSelectionRationale: storycraft probe tests whether the DPF protects source constraints under dramatic pressure
  sourceTemporalPosture: prospective fictional source structure
  renderingMediationMode: direct-source-structure unless fictional organization or technology architecture is live
  narratingOrRenderingWorkerRef: story designer or tool-assisted writer
  readerOrListenerRoleRefs: private reviewer of storycraft plan
  readerInterestOrUseHypothesis: reviewer needs to see whether continuity and agency survive the route
  intendedReaderOrListenerUse: private design critique, not publication
  narrativePurpose: produce a source-returnable continuation route for testing
  blockedPurposeOverread: no authorization, no exhaustive canon authority, no publication permission
  sourceReturnOwner: source-pack and canon owner; rights and publication owner when those claims are made
  refreshCondition: source-pack correction, canon selection change, generated-carrier admission change
```

### NSTD.1:5 - Archetypal Grounding

#### Mature worked slice: FPF seminar from source spine to admitted route

Start with a weak request: "Tell a motivating story about FPF so people want to use it." This is not yet a narrative purpose intake. The source structure is hidden, the reader use is vague, and motivation is being asked to carry adoption, evidence, and teaching value at once.

Repair it in the intake, not later in style.

```text
NarrativePurposeIntake@FPFSeminarOrientation:
  sourceBasisRefs: selected FPF pattern bodies and relation records
  selectedSourceStructureRefs:
    - EntityOfConcern discipline
    - Problem frame and forces
    - Solution as admissible move under conditions
    - neighboring-pattern exits
    - quality and improvement loop entry
  sourceStructureSelectionRationale: new practitioners fail when they treat patterns as recipes rather than condition-bound moves
  sourceTemporalPosture: prospective planned learning route over current FPF source corpus
  renderingMediationMode: direct-source-structure
  narratingOrRenderingWorkerRef: seminar author
  readerOrListenerRoleRefs: new FPF practitioner; team lead evaluating local adoption
  readerInterestOrUseHypothesis: reader wants a first usable route through FPF without learning every pattern first
  intendedReaderOrListenerUse: reconstruct one pattern-use route and choose the next governing pattern
  narrativePurpose: orient attention and motivation toward source-returnable pattern use
  blockedPurposeOverread: not proof that FPF is correct; not replacement for pattern bodies; not authority for a local project
  sourceReturnOwner: selected FPF pattern body and relation record
  ethicsOrAssuranceOwner: none unless the seminar makes assurance, policy, or affected-party claims
  refreshCondition: FPF edition or selected-source pattern changes; learner reconstruction test fails
```

Now the narrative worker can compose. The first paragraph may be memorable, but every memorable move has a source return. "A pattern is not a recipe" returns to source conditions, forces, and neighboring exits. "Start with the thing being changed" returns to `EntityOfConcern`. "Do not optimize the visible proxy indicator" returns to quality and proxy-risk owners. The seminar publication carrier can be engaging, but the intake prevents it from becoming a local mythology about FPF.

Evaluation through `NSTD.6` later asks whether learners can rebuild the route: identify the source structure, say why the selected order was didactic, name what the story intentionally omitted, and return to the pattern body when they need authority. If learners only repeat the slogan "patterns are not recipes", `NSTD.1` did not select enough source structure for the declared use.

#### Mature worked slice: architecture-mediated narrative

An architect wants a narrative explaining a system's future structure after candidate synthesis. Do not start with "tell the journey from chaos to architecture". Start by deciding whether the narrative is architecture-mediated. If it is, architecture work remains live before narrative work.

```text
NarrativePurposeIntake@ArchitectureDecisionStory:
  sourceBasisRefs: architecture candidate set, selected architecture description, decision record, expected characteristics, known residuals
  selectedSourceStructureRefs:
    - problem situation and forces
    - candidate structures considered
    - selected structure and rejected alternatives
    - expected architecture characteristics
    - residual exceptions and developer continuation boundary
    - telemetry or later actual-structure feedback condition
  sourceTemporalPosture: prospective future holon structure before implementation
  renderingMediationMode: architecture-mediated
  architectureMediationRef: architecture description and candidate synthesis records
  readerOrListenerRoleRefs: developer team; product steward; later evaluator
  intendedReaderOrListenerUse: understand what structure to preserve while implementing and what may be locally detailed
  narrativePurpose: carry structural intent and trade-off rationale into development work
  blockedPurposeOverread: not the architecture itself; not implementation order; not assurance that realized structure will match
  sourceReturnOwner: architecture description, architecture decision record, and future telemetry route
  refreshCondition: candidate set, selected architecture, decision, or actual-structure feedback changes
```

This case teaches the architecture bridge. The narrative worker is not exempt from architecture owners just because the output is prose. `C.33` is live for structural-information capture and loss; `C.34` is live if correspondence between described and realized structure matters; `E.17` is live if the carrier is published; architecture decision owners remain live for decision authority. `NSTD.1` only binds the narrative purpose to selected structures and reader use.

#### Mature worked slice: franchise continuation probe

For a continuation-style storycraft probe using a well-known space-opera franchise such as `Star Wars`, the selected source is a bounded private source pack. The intake must state canon scope, character-agency constraints, continuity constraints, premise constraints, and non-publication boundary before any scene or plot move is accepted.

A bad intake says: "Write a surprising sequel that feels epic." A repaired intake says: "For private storycraft testing, render a continuation premise that preserves admitted canon constraints, character agency, causal consequence, and theme tension; block publication, rights, and authority claims." If a surprising turn works only because the source pack was ignored, the failure belongs to `NSTD.1` before `NSTD.2` or `NSTD.5` can repair it.

#### Role-specific mature first moves

| Worker | First source-selection move | Common hidden overread | Repair before composing |
| --- | --- | --- | --- |
| Teacher | Name the source spine and reconstruction task. | Learner interest means learning occurred. | Add source-return question and later `NSTD.6` row. |
| Architect | Name selected structures, candidates, residuals, and actual-structure feedback. | Explanatory story is the architecture decision. | Route decision authority to architecture decision owners. |
| Scientist | Name mechanism, calculation, uncertainty, and proof or evidence boundary. | Story coherence is evidence closure. | Add evidence owner and source-return condition. |
| Story designer | Name source pack, continuity, agency, and non-use boundary. | Dramatic surprise authorizes source violation. | Reopen source-pack selection before ordering. |
| Live commentator | Name event stream, provisional interpretation, and later official return. | Live causal claim is settled fact. | Mark uncertainty and telemetry return. |
| AI-agent operator | Name source plan, schema, admission owner, and evaluation route. | Fluent generated prose is an admitted rendering. | Send carrier to `NSTD.7` and `C.35` before `NSTD.6`. |

#### What this pattern teaches about FPF

`NSTD.1` is often the first place where a narrative worker learns why FPF separates admitted source basis, description, evidence, assurance, ethics, publication, and improvement. The pattern does not ask for more paperwork. It asks the worker to stop one very common collapse: "I have a purpose, therefore I know what the story should say." In FPF terms, a purpose is a relation to an `EntityOfConcern`, a role use, and selected source structures. It is not the admitted source basis, not the authority, and not the quality result.

An FPF seminar route wants learners to understand why pattern use is condition-based rather than recipe following. The selected source structures are `EntityOfConcern`, problem frame, forces, solution, consequences, and neighboring-pattern exits. The purpose is orientation for later reconstruction tasks. It is not permission to replace pattern bodies with seminar slogans. Source return points to the FPF patterns and the seminar publication carrier stays outside this DPF body.

A homotopy explanation starts differently. The admitted source basis is a mathematical corpus: definitions, examples, maps, equivalences, proof-status boundaries, and formal sources. The intended reader is not "any curious person"; it might be an undergraduate who must later distinguish intuitive pictures from formal definitions. The purpose can be "make paths, deformations, and invariants followable", but the blocked overread says that the narrative does not prove the theorem, replace formal notation, or license analogy as definition. The intake therefore protects formal return before any metaphor is selected.

A live football commentary has a live unfolding source posture. The commentator's purpose may be orientation and suspense, but the selected structures are event order, score state, possession changes, player actions, provisional interpretation, and later official source return. The intake blocks the overread that a dramatic prediction, blame cue, or emotional framing is evidence. If later official statistics contradict the live interpretation, the refresh condition is not optional.

A franchise-continuation storycraft test uses a prospective fictional source posture. The source structures are admitted canon constraints, continuity requirements, premise constraints, character-agency constraints, and non-publication boundary. The purpose may be private storycraft testing, not authorized sequel publication. The intake must state that publication rights, exhaustive canon authority, and moral permission are outside this DPF case.

### NSTD.1:6 - Bias-Annotation

This pattern blocks purpose-primacy drift: the message, theme, desired memory, or persuasion effect is allowed to choose source structures after the fact. Treating purpose as the source-selection owner collapses selected source structure, reader use, and authority boundary. Repair by reopening the intake, naming selected structures, and writing the blocked purpose overread before drafting or evaluating. Scope: DPF-local for narrative renderings; it does not govern all communication, evidence, assurance, or publication work.

### NSTD.1:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD1-1` | Admitted source basis and selected source structures are named before purpose is finalized. |
| `CC-NSTD1-2` | Source-structure selection rationale explains why these structures are needed for the reader or listener use. |
| `CC-NSTD1-3` | Source temporal posture and rendering mediation mode are explicit. |
| `CC-NSTD1-4` | Narrating or rendering worker, reader-interest or use hypothesis, and intended reader or listener role are named. |
| `CC-NSTD1-5` | Intended use is narrower than general persuasion, inspiration, or entertainment. |
| `CC-NSTD1-6` | Purpose states non-admissible downstream use. |
| `CC-NSTD1-7` | Evidence, assurance, ethics, policy, and work claims route to direct owners when made. |
| `CC-NSTD1-8` | Source-return owner and refresh condition are present when source currentness or hidden distinctions matter. |

### NSTD.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Message-first drafting | The theme chooses the structure after the fact. | Reopen intake and name selected source structures before drafting. |
| Tacit selection as craft | The worker or model foregrounds structures, but no rationale ties them to reader use. | Reconstruct the selection rationale and reader-interest hypothesis before evaluating or improving the narrative. |
| Motivation as truth support | A moving narrative is treated as stronger evidence. | Route evidence to `A.10` and keep motivation as reader-use support. |
| Purpose without blocked use | The same narrative is reused for decision, policy, or work. | Add blocked purpose overread and source-return condition. |

### NSTD.1:9 - Consequences

The benefit is early kind stability: admitted source basis, selected structure, narrative rendering, reader use, and authority boundaries stop competing. The cost is one small intake record before drafting.

### NSTD.1:10 - Rationale

Narrative design traditions often begin with audience and communicative aim. FPF keeps that value, but it binds aim to selected source structure. This avoids semio-bias: the narrative is a rendering relation over source structure, not a free-standing communication product.

### NSTD.1:11 - SoTA-Echoing

#### Operational comparison against domain vocabulary

This DPF intentionally translates domain vocabulary into FPF owner work instead of importing it whole. When narratology says story, discourse, and presentation, this package asks: what source structure is selected, what order is chosen, what is foregrounded, and what source return remains? When cognitive narratology says event model, transportation, perspective, or memory, this package asks: which reconstruction target, engagement device, viewpoint, or evaluation characteristic is being changed? When NLG says content planning, discourse planning, and realization, this package asks: what is the source plan, what is the ordering rule, what is the generated carrier, and what admission and evaluation route owns it?

The practical consequence is a repair rule. If a domain term helps the worker choose or repair a narrative move, keep it as DPF vocabulary. If it starts carrying evidence, assurance, ethics, agency, publication, or Core ontology, route the claim to the FPF owner and state the blocked overread.

Hoffmann's "The Tensions of Scientific Storytelling" shows that scientific story construction can organize attempts, mechanisms, and unresolved tensions for readers; Schmid's `Narratology: An Introduction` and Chihaia's `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` show that presentation and audience-facing narrative traditions differ by source tradition; Castricato et al.'s "Towards a Formal Model of Narratives" supports explicit narrator-to-reader information flow, reader story-model evolution, and uncertainty; Dahlstrom and Ho's "Ethical Considerations of Using Narrative to Communicate Science" warns that communicative purpose can become persuasion risk. The DPF adapts audience and purpose only after source-structure selection, temporal posture, rendering mediation mode, and role split are named. When a purpose, reader-use, science-storytelling, teaching, future-scenario, or persuasion-risk claim depends on a cited source basis, name that source basis and keep the claim within its boundary.

### NSTD.1:12 - Relations

Uses `A.6.3.NAR` for Core relation ownership, `A.16.1` when the first honest material is only a pre-articulation narrative cue, `C.2.LS` when language-state facets or thresholds shape the intake, `G.2` for source-pack claims, `C.33` when architecture-relevant structural-information capture or loss is current, `NSTD.6` when non-architecture narrative epiplexity is evaluated, `D.1` through `D.5` when affected parties or persuasion are live, `A.10` for evidence, `B.3` for assurance, `E.10` and `F.18` for durable wording or naming repairs, and `G.11` for source and telemetry refresh. Support-map entry: open `Architecture and Narrative Work Bridge` when `renderingMediationMode` is `architecture-mediated` or `mixed`; open `Source Use And Refresh Map` when a cited source basis is relied on or stale; open `DPF Precision Restoration And Owner Map` when a local narrative term threatens to become ontology; open `Name And Edition Route` only for DPF-prefix or edition questions.

### NSTD.1:End

## NSTD.2 - Structure-to-Sequence Ordering

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `NarrativeOrderingRule@Context`, a DPF-local relation slot set for one narrative rendering.

### NSTD.2:1 - Problem frame

Use this pattern when a graph, mechanism, evidence set, architecture structure, candidate set, mathematical dependency structure, canon structure, or source tradition must be put into a sequence and the sequence changes what readers can recover.

First useful move: name the ordering rule, the source relations it preserves, the source relations it foregrounds, the source relations it coarsens or loses, and the source-return condition.

What goes wrong if missed: the order feels natural, but readers silently infer a different order kind: chronology, proof, causality, importance, decision order, work order, or moral priority.

What this buys: sequence becomes an explicit rendering choice rather than hidden ontology.

### NSTD.2:2 - Problem

Narrative is sequential. Many source structures are not. Trees, graphs, mechanism diagrams, dependency sets, option sets, proof dependencies, and architecture views must be traversed. A chosen order preserves some relations and hides others. If the ordering rule is implicit, a fluent sequence can misrepresent the selected source structure.

### NSTD.2:3 - Forces

| Force | Tension |
| --- | --- |
| Legibility vs structural fidelity | Linear order helps reading but cannot preserve every relation. |
| Teaching order vs source order | A good learning route may violate publication order or proof order. |
| Dramatic tension vs dependency truth | Suspense and reveal can hide prerequisites. |
| Compactness vs source return | The sequence needs to move, but hidden relations need return points. |

### NSTD.2:4 - Solution

Declare the ordering rule before treating the narrative rendering as good enough for declared use.

```text
NarrativeOrderingRule@Context:
  narrativeRenderingRef:
  sourceStructureRefs:
  unfoldingStructureRef?:
  demonstrativeSliceRef?:
  orderingRuleKind:
  orderRationale:
  preservedSourceRelations:
  foregroundedSourceRelations:
  coarsenedOrLostSourceRelations:
  sourceReturnCondition:
  neighboringGoverningPatternRefs:
```

Admissible ordering-rule kinds include chronology, causality, dependency, discovery, didactic prerequisite, tension, traversal, viewpoint, publication, decision memory, and declared local rule. The name is not enough; the record must say what the rule preserves and loses.

Choose the rule through a four-question ordering test.

| Test | Ask | If unclear |
| --- | --- | --- |
| Source topology | Is the source primarily chain, graph, hierarchy, cycle, option set, event stream, proof dependency, architecture view, or canon field? | Return to `NSTD.1`; selected source structure is not ready for sequencing. |
| Reader traversal | What path should the reader take first for the declared use: prerequisite, tension, discovery, causal, chronological, decision, viewpoint, or recap? | State two candidate rules and choose by reader-use effect, not by author taste. |
| Loss account | Which source relations become hidden or weaker under this order? | Add coarsened or lost relations and a source-return point before drafting. |
| Misread risk | What wrong order will readers infer if the rule is not stated? | Add a sentence or marker that blocks that inference. |

The ordering rule can be mixed, but only if the mixture is explicit. A teaching route may start with didactic prerequisites, use one discovery story to motivate a distinction, then return to formal dependency order. A live commentary may use chronological order for observations and causal order in a later recap. A franchise continuation may use reveal order for suspense while preserving an underlying causal or continuity order. The mixed rule must state where each order applies and what it must not imply.

When the selected source structure is a constraint-governed unfolding structure, the narrative order is a traversal or demonstration slice over that structure. The ordering rule must name the selected unfolding structure, the demonstrative slice used for reader orientation, the preserved constraints and invariants, and the branches, alternatives, loops, direct exits, or stop conditions hidden by the slice. The sequence in the narrative is not the whole unfolding structure and not a work order.

Use this repair table when the narrative feels coherent but readers reconstruct the wrong structure.

| Symptom | Likely hidden order | Repair |
| --- | --- | --- |
| Readers think the first-mentioned cause is the strongest cause. | Salience order mistaken for causal order. | Mark salience as viewpoint or teaching order; return causal-strength claims to the evidence or source governing pattern. |
| Learners can retell the lesson but fail formal exercises. | Didactic story order mistaken for proof order. | Add proof-return checkpoints and separate example order from theorem dependency. |
| Stakeholders think a narrative of architecture choices is the project decision sequence. | Explanation order mistaken for decision or work order. | Route decision claims to the architecture-decision governing pattern and name the explanatory order. |
| Fans like a reveal but continuity breaks. | Reveal order hides source canon constraints. | Add source-pack return and causal and continuity support before dramatic reveal. |
| A generated story has plausible steps but no preserved source graph. | Generator realization order mistaken for selected source structure. | Return to `NSTD.7`; recover source plan and selected structure before evaluation. |

Do not evaluate the sequence by elegance first. A beautiful order that hides a critical dependency is below floor for declared use. Evaluate it through `NSTD.6` only after the rule, preserved relations, foregrounded relations, lost relations, and source-return condition are in the record.

### NSTD.2:5 - Archetypal Grounding

#### Mature worked slice: graph-to-sequence serialization without source loss

Use this case when the source is not already a line. A knowledge graph about a domain has concepts, dependencies, counterexamples, evidence links, and practice routes. A narrative rendering must choose a traversal. If the traversal is not named, the reader may treat the story order as ontology, proof order, or historical order.

```text
NarrativeOrderingRule@HomotopyIntro:
  narrativeRenderingRef: HomotopyIntroNarrative@v1
  sourceStructureRefs:
    - topological space
    - path
    - deformation under constraints
    - invariant
    - example and counterexample
    - proof-status boundary
  orderingRuleKind: didactic prerequisite plus analogy-first cue
  orderRationale: learner needs visual intuition before formal return, but formal dependency must remain recoverable
  preservedSourceRelations: prerequisite relation; analogy-to-definition return; example-to-counterexample contrast
  foregroundedSourceRelations: deformation intuition and invariant question
  coarsenedOrLostSourceRelations: full proof order; advanced generality; categorical reformulation
  sourceReturnCondition: any claim about theorem, equivalence, or proof returns to formal statement and proof owner
  neighboringOwnerRefs: `A.6.3.CSC`, `E.17.EFP`, `A.10`, `NSTD.6`
```

This is a serialization decision with narrative consequences. The route can begin with a picture-like story about deforming paths, but the story must mark where analogy stops. A mature narrative might say, in ordinary prose, "The picture is a guide to the relation, not the definition; the formal boundary returns in the next step." That line is not decoration. It prevents the selected order from becoming false ontology.

#### Before and after repair: architecture order

Before:

> We tried several designs and eventually found the architecture that solved the coordination problem.

Failure: chronology and success wording hide candidate selection, trade-off, decision authority, and realized-structure uncertainty. The reader may infer that the final candidate is proven, implemented, and telemetry-confirmed.

After:

> This explanation follows decision-memory order. First it states the coordination problem, then the candidate splits considered, then the selected trade-off and the residual interface exceptions. It does not give implementation order or proof that the realized structure already has the expected characteristics. For authority, return to the architecture decision record; for actual structure, return to telemetry after implementation.

What changed: the ordering rule became explicit, preserved relations are named, lost relations are named, and source-return is recoverable. `NSTD.2` did not make the narrative longer for its own sake. It made the sequence truthful.

#### Before and after repair: live commentary

Before:

> The midfield is late, so the press has failed, and that is why the match is turning.

Failure: live chronological observation is mixed with causal explanation and outcome projection. The source at that moment may support late movement and lost possession, but not a settled causal account.

After:

> In live order, the midfield line arrives late and the press opens space. Treat that causal reading as provisional until the replay, event data, or post-match analysis confirms it. For now the narrative preserves observation, uncertainty, and listener orientation.

What changed: chronology, provisional causality, and later source return are separated. This is the same FPF move as separating evidence, interpretation, and assurance, but in narrative-order vocabulary.

#### Calibration for ordering values

| Value | Ordering condition |
| --- | --- |
| `2` | A readable sequence exists, but the ordering rule and lost relations are mostly hidden. |
| `3` | The ordering rule is named, but source-return and misread risks are weak. |
| `4` | The order preserves declared relations, states losses, and blocks the main wrong reconstruction for one use. |
| `5` | The order is replayable across at least two heterogeneous cases, with conflict between order layers explicitly handled and tested through `NSTD.6`. |

#### SoTA-to-action translation

Narratology often distinguishes source material, story, discourse, presentation, and focalization. `NSTD.2` treats that as domain vocabulary and restores the FPF object before use: admit the source basis, select the source structure, choose the traversal or order, name what the order preserves and loses, then compose. NLG makes a similar split through content selection, document planning, microplanning, and realization. Fluent wording realization cannot repair a bad ordering rule.

A homotopy-theory explanation orders material by learner dependency: spaces, paths, homotopy, fundamental group, examples, proof-status boundaries. This is not the historical discovery order and not the formal proof order of a research monograph. The narrative must state that definitions and proof obligations remain in source-return formal statements.

An architecture narrative for a team may order structures by decision memory: first the coordination problem, then candidate splits, then chosen trade-off, then residual interface exceptions. That order is not the architecture structure itself and not the chronological order of implementation work. The preserved relations are coupling, cohesion, interface grammar, responsibility boundary, and expected trade-off. The lost relations may include low-level module detail and alternative candidates. Source return goes to architecture description, decision record, and telemetry if actual-structure feedback exists.

A franchise-continuation outline may order scenes by reveal and tension. That does not mean reveal order is causal order. The underlying causal and continuity order must still name premise constraint, character motivation, event cause, consequence, and canon-return point. If a later twist works only because a source constraint was hidden from the writer as well as from the reader, the order is not a legitimate reveal; it is a source-selection failure.

A scientific storytelling case may order experiments by tension: failed attempt, surprising measurement, revised hypothesis, unresolved conflict. That order can be useful because it mirrors inquiry, but it cannot make unresolved tension into evidence closure. The sequence must name which calculations, mechanisms, and experimental facts remain source-return points.

Worked repair sequence:

1. Initial symptom: "The team first tried A, then B, and finally discovered the right architecture."
2. Hidden-order diagnosis: chronology is being read as decision quality and finality.
3. Source topology repair: name candidate structures, quality characteristics, rejected alternatives, and telemetry or decision basis.
4. Ordering rule repair: call the narrative "decision-memory order", not proof, implementation order, or architecture structure.
5. Loss repair: state what the narrative omits, such as lower-level exceptions or candidates excluded for scope.
6. Source-return repair: link to architecture description, decision record, or candidate comparison when a reader needs authority.

Second worked repair sequence:

1. Initial symptom: "We introduce homotopy with loops, then groups, then examples, because that is the natural story."
2. Hidden-order diagnosis: "natural story" hides the didactic prerequisite order and may be mistaken for formal proof order.
3. Source topology repair: list definitions, examples, theorem prerequisites, proof-status boundaries, and formal-source returns.
4. Ordering rule repair: choose didactic dependency order and explicitly state where it diverges from formal order.
5. Loss repair: record which formal details are deferred and where they return.
6. Evaluation repair: `NSTD.6` checks whether learners can reconstruct dependency and proof boundaries, not whether they enjoyed the story.

Case matrix for ordering work:

| Case | Candidate order | Preserves | Hides or weakens | Required source return |
| --- | --- | --- | --- | --- |
| FPF learning route | Didactic prerequisite order: entry condition, EoC, forces, solution, checks, exits, improvement. | Pattern-use route and learner build-up. | Monolith order, advanced variants, historical source evolution. | Source pattern body and relation records. |
| Homotopy explanation | Didactic dependency order with analogy before formal proof. | Learner accessibility and dependency sequence. | Full proof order, all lemmas, advanced generalization. | Formal statement, proof owner, example boundary. |
| Franchise continuation | Causal plot order plus reveal order. | Continuity, motivation, event consequence, source-pack return. | Exhaustive canon and publication rights. | Admitted canon refs and non-publication boundary. |
| Live commentary | Live chronological order plus provisional interpretation markers. | Event stream, uncertainty, listener orientation. | Later tactical recap, off-camera sources, official correction. | Official event record, telemetry, recording. |
| Architecture explanation | Decision-memory order or trade-off route. | Problem, candidate, selected trade-off, residual exception. | Implementation order, full structure, rejected-candidate detail. | Architecture description, candidate set, decision record, telemetry. |

Use the matrix as a pre-drafting design aid. The selected order should be visible before the narrative prose exists. If the matrix can only be filled after the text is written, the worker is reconstructing hidden choices and should mark the result as a repaired route, not as an originally controlled route.

When two orders conflict, preserve both as named layers. A learning route may teach prerequisites first and later show historical discovery. A mystery-like story may reveal effects before causes while keeping an internal causal order. A live recap may reorder events by causal explanation after first recording live chronology. The reader must be told which layer they are following.

### NSTD.2:6 - Bias-Annotation

This pattern blocks natural-sequence drift: a chronological, didactic, dramatic, traversal, or slide order is treated as if it were the source structure itself. The bias is especially likely when the order feels intuitive to the author. Repair by naming the ordering rule, preserved relations, foregrounded relations, lost relations, and source-return condition. Scope: DPF-local for source-structure-to-sequence rendering; it does not govern general serialization formats or publication order.

### NSTD.2:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD2-1` | Ordering rule and rationale are named. |
| `CC-NSTD2-2` | Preserved, foregrounded, and lost relations are explicit. |
| `CC-NSTD2-3` | Narrative order is not treated as physical time, proof order, work order, or decision authority without source support. |
| `CC-NSTD2-4` | Source-return condition is present when lost relations affect action or reliance. |
| `CC-NSTD2-5` | Preservation claims route to `C.34`; coarsening claims route to `A.6.3.CSC`, to `C.33` when architecture-relevant structural-information loss is current, or to `NSTD.6` epiplexity when the loss question is non-architecture DPF evaluation. |

### NSTD.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Natural-order assumption | The order is not named because it feels obvious. | Write the rule and one preserved or lost relation. |
| Tension as dependency | Reveal order is read as prerequisite order. | Split dramatic order from dependency order and add source return. |
| Slide order as source structure | A teaching sequence is treated as the corpus architecture. | Route the teaching publication carrier through `NSTD.8` and keep source structure separate. |

### NSTD.2:9 - Consequences

The benefit is that a narrative path can be optimized for comprehension without pretending to preserve all source relations. The cost is explicit loss accounting.

### NSTD.2:10 - Rationale

Narrative sequence is a transformation over structure. Making the ordering rule explicit preserves the useful similarity between serialization and narrativization: both choose an order for a structure, both preserve and lose relations, and both need a return path when the order is relied on.

### NSTD.2:11 - SoTA-Echoing

Schmid's `Narratology: An Introduction` supplies the source-material, story, narrative, and presentation distinction as narratology vocabulary; Chihaia's `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` keeps the DPF from treating one narratology tradition as the whole domain; Gatt and Krahmer's `Survey of the State of the Art in Natural Language Generation` makes content selection and realization separable; Cardona-Rivera and Ware et al.'s "The Story So Far on Narrative Planning" makes planned event and plot structure visible before wording. The DPF adopts that ordering discipline only after restoring admitted source basis, selected source structure, and FPF owner routes.

Operational payload:

- From Schmid, use selection, composition, and linearization as separate duties. A route may admit source basis and select source structure correctly but still linearize it badly. `NSTD.2` therefore evaluates ordering independently from `NSTD.1` selection.
- From Chihaia, do not assume one narratology school's order terms are universal. If a term such as plot, discourse, fabula, perspective, or presentation is used, it must be translated into the local ordering rule and FPF owner terms.
- From NLG, content planning and realization are distinct. A generated or human-written text can realize fluent sentences while hiding the content plan. `NSTD.2` asks for the plan before style.
- From narrative planning, plot order and event order may diverge. This is useful in storycraft and explanation, but the divergence must be recorded so readers do not infer false causality or dependency.
- From FPF architecture patterns, views and viewpoints are not free perspectives. When the narrative order traverses architecture-relevant structures, `C.30.ASV`, `C.33`, `C.34`, and architecture decision owners may become live.

The practical consequence is that "good order" is never a free aesthetic judgment. It is an ordering rule plus preserved relations, lost relations, and source return for one declared use.

### NSTD.2:12 - Relations

Uses `A.6.3.NAR`, `A.6.3.CSC`, `C.33` for architecture-relevant structural-information capture or loss, `C.34`, `E.17`, `E.17.EFP`, `A.16.2` when a route must back off or respecify after overcommitment, `A.6.P` when ordering rationale hides relation-kind claims, `NSTD.6`, and `G.11`. Non-architecture capture and loss questions feed the DPF-local epiplexity basis in `NSTD.6`. Reopen when source structure, reader use, ordering rule, source-return condition, route authority, relation precision, or low `NSTD.6` ordering value changes. Support-map entry: open `Architecture and Narrative Work Bridge` when sequence is over architecture views, candidate structures, descriptions, correspondence, or actual-structure feedback; open `Semiotic And Language-Precision Bridge` or `DPF Precision Restoration And Owner Map` when ordering terms hide coarsening, relation-kind, or quality claims.

### NSTD.2:End

## NSTD.3 - Source Mechanism, Event Model, and Coherence

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `NarrativeEventMechanismSupport@Context`, a DPF-local support record for one narrative rendering.

### NSTD.3:1 - Problem frame

Use this pattern when locally fluent narrative passages fail because readers cannot build a coherent model of source mechanism, event flow, dependency structure, architecture relation, state change, or proof dependency.

First useful move: state whether the selected source structure is event-like, mechanism-like, dependency-like, architecture-like, proof-like, canon-like, or mixed; then state what readers must reconstruct for the declared use.

What goes wrong if missed: fluency is mistaken for source coherence. Readers remember the story but cannot say what changed, why it changed, which relation mattered, or where the claim stops.

What this buys: coherence is tied to recoverable source structure, not to smooth prose alone.

### NSTD.3:2 - Problem

Narratives often use events and agents because they are easy to follow. But many source structures are not event sequences. Architecture structures, mathematical definitions, evidence graphs, mechanism diagrams, and source packs can be misread when forced into a fiction-like event model.

### NSTD.3:3 - Forces

| Force | Tension |
| --- | --- |
| Event readability vs non-event structures | Readers follow events easily, but not every source relation is an event. |
| Causal wording vs causal support | "Because" helps comprehension but may need `C.28`. |
| Mechanism clarity vs uncertainty | A good mechanism story can hide unknown or contested source relations. |
| Reconstruction vs entertainment | The declared use may require reconstruction, not only engagement. |

### NSTD.3:4 - Solution

Use an event and mechanism support record when the narrative asks readers to understand change, dependency, or explanation.

```text
NarrativeEventMechanismSupport@Context:
  narrativeRenderingRef:
  sourceStructureKind:
  requiredReaderReconstruction:
  eventOrMechanismModel:
  participatingHolonOrRoleRefs?:
  dependencyOrConstraintRefs?:
  causalUseOwnerRef?:
  uncertaintyOrUnknownRefs?:
  reconstructionTaskRefs?:
  sourceReturnCondition:
```

Then perform four checks: source structure kind, reader reconstruction target, supported relation claims, and source return.

Build the support record before polishing the prose.

1. Convert each important passage into a source-support row: what changed, what relation is being suggested, what source structure backs it, and what remains unknown.
2. Mark the relation strength: observed event, temporal sequence, dependency, constraint, mechanism hypothesis, causal claim, proof dependency, architecture trade-off, canon continuity, or reader-facing analogy.
3. Mark the reconstruction target: after reading, what should the reader be able to state, distinguish, predict, update, or return to source for?
4. Mark the overclaim risk: which verbs, connectors, or story beats make the relation sound stronger than the source allows?
5. Add repair before style: lower the relation word, add uncertainty, add source return, or open the direct owner.

Use these relation-strength distinctions in narrative review.

| Narrative wording pressure | Minimum support needed | Direct owner when stronger |
| --- | --- | --- |
| "then" or "after" | Event or sequence source | Source or event owner if factual |
| "because" | Causal or mechanism support | `C.28`, evidence owner, or domain causal owner |
| "therefore" | Inference or proof support | Proof or evidence owner and source return |
| "had to" | Constraint or necessity support | Constraint, architecture, proof, or canon owner |
| "wanted" or "decided" | Agent or responsibility support | `A.13`, `A.2`, `A.2.1`, `D.*` when ethical |
| "shows that" | Evidence support | `A.10` and source owner |

For non-event structures, do not invent fake events just to make a story move. A proof dependency can be narrated as a sequence of questions and distinctions; an architecture view can be narrated as a path through forces and trade-offs; a source pack can be narrated as a controlled return route. The narrative event model is only a reader-facing scaffold. The selected source structure remains the denominator for reconstruction and later `NSTD.6` evaluation.

Reader reconstruction tasks should be concrete:

- "Name the mechanism and the unresolved relation" is better than "understand the mechanism."
- "Distinguish observed event, inference, and prediction" is better than "follow the live story."
- "Point to the formal statement where the analogy stops" is better than "get the math intuition."
- "Recover which architecture trade-off was accepted and which exception remains" is better than "remember the project story."

If no reconstruction task can be written, the narrative may still be entertaining or orienting, but it is not yet a reliable structure-to-narrative rendering for a reliance-bearing use.

### NSTD.3:5 - Archetypal Grounding

#### Mature worked slice: event support in a scientific narrative

A science narrative says: "The failed experiment forced the theory to change." That line may be a useful story beat, but it hides several relation kinds: observed result, incompatibility with expectation, proposed mechanism, community decision, and later evidence. `NSTD.3` repairs the relation support before the story is trusted.

```text
NarrativeEventSupportRecord@ExperimentTension:
  narrativeRenderingRef: ScienceStory@v1
  eventOrMechanismClaim: failed measurement challenged the prior mechanism hypothesis
  sourceStructureRef: measurement record, model expectation, uncertainty interval, alternative explanations
  relationStrength: observed mismatch plus mechanism hypothesis, not proof of forced theory change
  reconstructionTarget: reader can distinguish observed result, hypothesis pressure, and later evidence
  overclaimRisk: "forced", "proved", "settled", and "therefore" make the relation too strong
  sourceReturnCondition: return to measurement record and evidence owner for truth claim
```

Before:

> The experiment failed, so the old theory collapsed.

After:

> The measurement contradicted the expected value under the old mechanism model. The narrative uses that mismatch as tension, but the evidence claim remains narrower: the result pressures the mechanism and opens alternatives; it does not by itself prove which replacement is right.

The after version is not less narrative. It is a better narrative because the reader can reconstruct the event support and return to source when the claim becomes load-bearing.

#### Mature worked slice: franchise plot support

In a continuation-style storycraft probe, a scene says that a character betrays an ally "because the plot needs a darker turn." That is a narrative-function explanation, not source support. Repair it as source structure:

```text
NarrativeEventSupportRecord@CharacterTurn:
  eventOrMechanismClaim: character changes allegiance under named pressure
  sourceStructureRef: admitted canon constraint, prior motivation, current dilemma, consequence chain
  relationStrength: plausible character-agency hypothesis within private source pack
  reconstructionTarget: reader can state motive, pressure, action, consequence, and canon-return condition
  overclaimRisk: author need or theme is treated as character cause
  sourceReturnCondition: return to source pack and agency constraints
```

This repair blocks a common beginner and stale-practice failure: plot events occur because the writer wants them. `NSTD.3` asks what event support the reader can reconstruct. If the answer is "the writer needed a twist", the event belongs to story-planning repair, not admitted narrative rendering.

#### Calibration for relation support

| Value | Relation-support condition |
| --- | --- |
| `2` | Events are followable, but cause, dependency, motivation, proof, or evidence strength is inferred from wording. |
| `3` | Relation kinds are named, but reconstruction target or overclaim risk is weak. |
| `4` | Each load-bearing event or mechanism claim has source support, relation strength, reconstruction target, and source return. |
| `5` | The rendering survives perturbation: if wording, order, or viewpoint changes, readers still recover the same relation strength and know where stronger claims return. |

#### FPF owner teaching

`NSTD.3` is where narrative workers learn that "because" is not one relation. It may carry chronology, cause, mechanism, evidence, proof dependency, motivation, trade-off, or analogy. FPF already has owners for evidence, assurance, relation precision, and architecture structure. This DPF pattern teaches how those owners become visible when the publication expression is a story.

An architecture explanation tells why a modular split reduced coordination cost but increased interface exceptions. The narrative event is "the split happened"; the source mechanism is coupling, interface grammar, evidence-reuse loss, and residual repair. The story must let the reader reconstruct the architecture trade-off, not only the before-and-after drama.

A science story can say that an experimental result "forced" a revised hypothesis only if the source line supports that constraint. Often the honest relation is weaker: the result made one hypothesis less useful, exposed a tension, or suggested a new mechanism to test. `NSTD.3` keeps the tension narratable while preventing the narrative from closing evidence that the source left open.

A live match commentary says "the press is breaking down because the midfield line is late." The source event may support late midfield movement and lost possession; the causal claim may be provisional. The support record separates observed event, tactical interpretation, uncertainty, and later source return to recording or telemetry.

In a homotopy explanation, a deformation story may help learners track invariance, but it is not a proof by itself. The support record says which formal relation the story illustrates, what the learner should reconstruct, and where analogy must return to definitions or proof-status boundaries.

Use rewrite diagnostics when a sentence sounds good but may overclaim.

| Initial sentence | Source-support question | Safer narrative repair |
| --- | --- | --- |
| "The failed experiment revealed the true mechanism." | Did the source establish the mechanism or only expose a tension? | "The failed experiment exposed a tension that made this mechanism worth testing." |
| "The module split solved coordination." | Did it solve, reduce, move, or trade off coordination cost? | "The split reduced one coordination path and introduced interface exceptions." |
| "The character had no choice." | Is necessity supported by canon, causal constraint, or only dramatic pressure? | "The route presents the action as constrained by these canon and causal conditions." |
| "The proof idea is that loops remember holes." | Is this an analogy, definition, theorem, or proof step? | "The image helps track the invariant; the formal statement returns here." |
| "The team was outplayed because the press failed." | Is this observed cause, provisional interpretation, or later analysis? | "The live reading treats the late press as a provisional explanation to check against telemetry." |

If the repair makes the narrative less exciting, that is not automatically a defect. The repair preserves the source relation. Engagement can be rebuilt later through `NSTD.5` around the safer relation instead of by restoring the overclaim.

Minimum support-record sketches:

```text
NarrativeEventMechanismSupport@ArchitectureTradeoff:
  sourceStructureKind: architecture-like and mechanism-like trade-off
  requiredReaderReconstruction: why the split reduces one coordination path while creating interface exceptions
  eventOrMechanismModel: selected modular split changes dependency paths and exception-handling burden
  dependencyOrConstraintRefs: coupling refs; interface grammar refs; residual repair refs
  causalUseOwnerRef: architecture or evidence owner when causal strength is claimed
  uncertaintyOrUnknownRefs: telemetry not yet collected; candidate alternatives omitted
  reconstructionTaskRefs: reader names trade-off and residual exception
  sourceReturnCondition: architecture description and decision record for reliance
```

```text
NarrativeEventMechanismSupport@HomotopyAnalogy:
  sourceStructureKind: proof-like and definition-like dependency
  requiredReaderReconstruction: distinguish intuitive deformation image from formal equivalence relation
  eventOrMechanismModel: path deformation story used as analogy for invariant tracking
  dependencyOrConstraintRefs: formal definitions; examples; counterexamples; theorem prerequisites
  causalUseOwnerRef: none unless a causal learning claim is made
  uncertaintyOrUnknownRefs: analogy may fail outside named examples
  reconstructionTaskRefs: learner states where analogy stops and where proof returns
  sourceReturnCondition: formal source statement for proof or exercise use
```

```text
NarrativeEventMechanismSupport@LiveCommentary:
  sourceStructureKind: live event stream with provisional interpretations
  requiredReaderReconstruction: observed event vs inference vs prediction vs official correction
  eventOrMechanismModel: state updates and tactical hypothesis under uncertainty
  participatingHolonOrRoleRefs: teams, players, officials, broadcast or event source roles when needed
  uncertaintyOrUnknownRefs: off-camera events; later telemetry; official review
  reconstructionTaskRefs: listener can say what was observed and what was inferred
  sourceReturnCondition: official record, recording, statistics, or telemetry
```

These sketches are not mandatory formats. They teach the level of detail needed before coherence becomes reviewable. The record can be shorter in low-risk cases, but it must still state source-structure kind, reconstruction target, relation strength, uncertainty, and source return.

### NSTD.3:6 - Bias-Annotation

This pattern blocks fluent-coherence drift: smooth event language is mistaken for a mechanism, dependency, architecture, proof, or causal model. The bias appears when readers can retell the story but cannot reconstruct the selected source relation. Repair by naming the source-structure kind, the reconstruction target, the owner for causal or dependency claims, and the source-return condition. Scope: DPF-local for narrative coherence over selected source structure; it does not certify mechanism truth or causal evidence.

### NSTD.3:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD3-1` | Source structure kind is named and not forced into event form when inappropriate. |
| `CC-NSTD3-2` | Reader reconstruction target is explicit. |
| `CC-NSTD3-3` | Causal, dependency, constraint, goal, obstacle, hierarchy, prediction, and update relations are routed to their owners when claim-bearing. |
| `CC-NSTD3-4` | Unknown, contested, or deferred source relations are visible. |
| `CC-NSTD3-5` | Teaching or reliance-facing use includes reconstruction tasks or source-return points. |

### NSTD.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluent mechanism fiction | The passage reads well but cannot be reconstructed. | Add event or mechanism support fields and reconstruction task. |
| Causal overrun | Narrative causality exceeds supported causal-use claims. | Route to `C.28` or lower the claim to dependency or temporal sequence. |
| Event forcing | A graph, proof dependency, or architecture view is converted into fake events. | Name source structure kind and choose a better ordering rule through `NSTD.2`. |

### NSTD.3:9 - Consequences

The benefit is that narrative coherence becomes testable. The cost is that some dramatic simplifications must be weakened or paired with source return.

### NSTD.3:10 - Rationale

Narrative comprehension often depends on event models and causal schemas. FPF uses that strength but keeps event support distinct from causal evidence, mechanism truth, architecture evaluation, and proof status.

### NSTD.3:11 - SoTA-Echoing

Tan T. Nguyen's "A Review of Mechanistic Models of Event Comprehension" supplies the event-comprehension pressure: readers build event, hierarchy, prediction, updating, and causal-like models. Hoffmann's "The Tensions of Scientific Storytelling" shows scientific narratives can organize mechanisms and unresolved theory and experiment tension without proving them. Gatt and Krahmer's `Survey of the State of the Art in Natural Language Generation` keeps content selection separate from wording realization. The DPF adapts these lines by making source-structure kind and reconstruction target explicit.

Operational payload:

- From event-comprehension work, assume readers will build event, causal-like, hierarchical, and prediction or update models even when the source is weaker. `NSTD.3` therefore asks what model the reader is allowed to build.
- From scientific storytelling, unresolved tension is narratively useful. It must stay unresolved when the source is unresolved. A good story may preserve tension rather than close it.
- From NLG, a generated or edited realization can make a relation sound coherent even when content selection was wrong. `NSTD.3` therefore reviews source-support rows, not only wording coherence.
- From FPF evidence and assurance owners, coherence is not evidence. If the narrative says "shows", "proves", "forces", or "because", the relation strength must be routed to the owner that can carry it.
- From architecture work, a mechanism-like story about structure must keep trade-offs, residual exceptions, and telemetry distinct. A before-and-after story is not by itself an architecture evaluation.

The practical consequence is that narrative coherence is a reconstruction promise. If the reader cannot reconstruct the source relation and its uncertainty boundary, smooth prose is a liability.

### NSTD.3:12 - Relations

Uses `A.6.3.NAR`, `NSTD.2`, `C.28`, `A.10`, `B.3`, `C.33` for architecture-relevant structural-information capture or loss, `C.34`, `NSTD.6`, and `G.11`. Non-architecture mechanism-support recovery feeds `NSTD.6` epiplexity and event-mechanism values. Reopen when the source mechanism, causal support, reconstruction target, or evaluation result changes. Support-map entry: open `Architecture and Narrative Work Bridge` when event, mechanism, dependency, or coherence support is architecture-relevant; open `Source Use And Refresh Map` when a source or cognition claim supports reconstructability; open `DPF Precision Restoration And Owner Map` when event, mechanism, coherence, support, or cause language starts doing evidence or quality work.

### NSTD.3:End

## NSTD.4 - Voice, Focalization, and Agency

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `NarrativeViewpointAgencyDiscipline@Context`, a DPF-local record for one viewpoint and agency treatment.

### NSTD.4:1 - Problem frame

Use this pattern when narrator, voice, viewpoint, focalized object, protagonist, actant, personification, or agency treatment changes what a reader understands, remembers, trusts, blames, or treats as capable of action.

First useful move: state viewpoint or focalized object, what it reveals, what it hides, and whether any source bearer is being personified or treated as an actor.

What goes wrong if missed: viewpoint looks like style while it changes source visibility and responsibility assignment. A structure, institution, model, or document can be written as if it decided, wanted, knew, or authorized.

What this buys: the narrative can use viewpoint and protagonist design without smuggling agency, capability, responsibility, or moral permission.

### NSTD.4:2 - Problem

Narratology terms such as voice, focalization, protagonist, and actant are useful because they describe how narrative directs attention. But FPF cannot let those terms replace role, assignment, capability, responsibility, evidence, or ethics owners.

### NSTD.4:3 - Forces

| Force | Tension |
| --- | --- |
| Reader orientation vs ontological discipline | A focalized object helps readers, but it may not be an actor. |
| Storycraft roles vs FPF roles | Protagonist and actant are narrative functions, not `U.Role` by default. |
| Personification vs responsibility | Personification can teach, but responsibility and moral standing need direct owners. |
| Future agency profile vs current owner | `C.9` is planned, so current agency work must not rely on it operationally. |

### NSTD.4:4 - Solution

Create a viewpoint and agency discipline record when viewpoint is load-bearing.

```text
NarrativeViewpointAgencyDiscipline@Context:
  narrativeRenderingRef:
  viewpointOrVoice:
  focalizedObjectRef:
  revealedSourceStructureRefs:
  hiddenOrWeakenedSourceStructureRefs:
  narrativeFunctionTerms:
  personificationOrAgencyWording:
  directOwnerRefs:
  blockedAgencyOverread:
  repairAction:
```

Operational owner rules:

1. Use `A.13` for agential participation and agency spectrum when current.
2. Use `A.2` and `A.2.1` for role values and role assignments.
3. Use `A.2.2` for capability.
4. Use `D.1` through `D.5` for value, harm, conflict, bias, responsibility, and assurance-facing ethics claims.
5. Use `A.19.ECS` and `C.16` for any local agency characteristic or evaluation scale.
6. Mention `C.9` only as planned and non-operational until admitted.

Review viewpoint in four passes.

| Pass | What to inspect | Repair if failed |
| --- | --- | --- |
| Reveal or hide pass | What source structures become visible or invisible because of this viewpoint? | Add hidden-structure note, source-return link, or alternate viewpoint. |
| Function and kind pass | Is protagonist, actant, narrator, voice, or focalized object being treated as an FPF role, agent, capability, or responsibility bearer? | Split narrative function from FPF owner claim. |
| Literalization pass | Which personifications would become false if read literally? | Mark metaphor or personification, lower wording, or name the literal owner. |
| Affected-party pass | Does the viewpoint erase harmed parties, dissenting roles, uncertainty, or downstream reliance pressure? | Route to `D.1` through `D.5`, add counter-viewpoint, or block downstream use. |

Use narrative-function terms positively, but only inside their lane.

| Narrative function | Useful for | Not enough for |
| --- | --- | --- |
| Protagonist | Centering attention or action path. | Responsibility, role assignment, moral standing, or capability. |
| Actant | Describing function in a plot or transformation. | `U.Role`, `U.RoleAssignment`, or method ownership. |
| Voice | Controlling stance, distance, confidence, or witness posture. | Evidence strength, source authority, or ethical permission. |
| Focalization | Selecting what the reader sees and from whose constraints. | Completeness, neutrality, or source truth. |
| Personification | Teaching or memory aid for abstract structures. | Actual agency, decision authority, or intent. |

When a phrase has both narrative value and ontological risk, keep the phrase only if the record states the safe reading. "The architecture wants fewer dependencies" may be safe in a teaching aside if the same passage says that architects choose structures to reduce dependency under stated characteristics. It is unsafe when the sentence becomes decision rationale, blame assignment, or evidence of system behavior.

The strongest repair is often not deletion. Good narrative sometimes needs viewpoint and personification. Repair by adding the missing owner split: who actually decides, which structure is being highlighted, what is hidden, which source should be returned to, and which moral or work claim is not being made.

### NSTD.4:5 - Archetypal Grounding

#### Mature worked slice: viewpoint without false agency

An architecture explanation says: "The database wants to protect consistency, while the service wants speed." This can be a useful teaching viewpoint, but literal reading creates false agency and hides the real owners: architecture decision, component responsibility, consistency requirement, latency requirement, and trade-off.

```text
NarrativeViewpointRecord@ArchitecturePersonification:
  narrativeRenderingRef: ArchitectureExplanation@v1
  viewpointOrVoiceKind: didactic personification
  focalizedSourceStructureRef: consistency and latency trade-off across selected architecture structures
  narrativeFunction: make the trade-off memorable and traversable
  hiddenOrWeakenedSourceStructureRefs: actual component responsibility, decision record, measured characteristics
  agencyOrResponsibilityRisk: component metaphor may be read as actor agency or authority
  literalizationRepair: lower "wants" to "is treated as protecting" or name the real owner
  sourceReturnCondition: return to architecture description and decision record for authority
```

Before:

> The database refuses to let the service move fast.

After:

> In this teaching view, we personify the consistency boundary as the part that "pushes back." Literally, the owner is the architecture decision: consistency is protected by transaction and replication choices, and the service latency trade-off returns to the decision record and later telemetry.

This repair keeps the narrative value while protecting ontology. The viewpoint is a lens over selected source structures, not a new actor.

#### Mature worked slice: narrator and reader roles

A narrative rendering about a future project can speak from the viewpoint of "the future user". That may help the team notice consequences, but the imagined user is not evidence and not an affected-party consultation. `NSTD.4` requires the narrative worker to state the role boundary:

```text
NarrativeViewpointRecord@FutureUserScenario:
  viewpointOrVoiceKind: prospective scenario voice
  focalizedSourceStructureRef: expected use situation and system interaction
  narrativeFunction: expose usability and risk questions before design is final
  hiddenOrWeakenedSourceStructureRefs: actual user evidence, policy claim, safety claim
  agencyOrResponsibilityRisk: imagined voice is treated as real stakeholder authority
  literalizationRepair: mark as scenario hypothesis and route evidence to user research owner
  sourceReturnCondition: return to source assumptions and later evidence
```

#### Viewpoint repair ladder

1. **Keep as ordinary style** when the phrase is clearly not claim-bearing and no reader use depends on it.
2. **Mark as viewpoint** when it helps attention but could be mistaken for source structure.
3. **Lower the wording** when metaphor or focalization implies agency, evidence, certainty, or responsibility.
4. **Name the literal owner** when architecture, evidence, ethics, work, decision, or assurance authority is touched.
5. **Reject the move** when the viewpoint works only by hiding a source constraint or affected-party boundary.

#### Calibration for viewpoint quality

| Value | Viewpoint condition |
| --- | --- |
| `2` | Voice or focalization is effective, but agency, responsibility, evidence, or source visibility can be misread. |
| `3` | Viewpoint function is named, but literalization repair is incomplete. |
| `4` | Viewpoint, source structure, hidden structures, and owner exits are recoverable for one declared use. |
| `5` | A reader can shift viewpoint or remove the metaphor and still recover the same source structure and owner routing. |

#### FPF owner teaching

`NSTD.4` makes the parallel with architecture views explicit for narrators. A viewpoint selects and highlights structure for a use. It is valuable for attention, but it does not create a new `U.Role`, `U.RoleAssignment`, responsibility bearer, evidence source, or decision authority. The narrative vocabulary may say narrator, focalization, protagonist, actant, or voice; FPF keeps asking which owner carries the claim if the wording becomes load-bearing.

A technical story says "the architecture wants to reduce coupling." `NSTD.4` repairs this as personification for reader orientation. The source structure is an architecture candidate with coupling and cohesion characteristics. The architecture is not an agent and has no responsibility. The actor may be an architect role assignment, and the decision or method claim goes to its direct owner.

In a franchise storycraft case, the protagonist may be the center of narrative attention while agency discipline asks whether the character's action is supported by admitted canon, premise constraints, and causal plot support. "The Force guided the decision" may be a story-world explanation, but it is not a license to skip character motivation, source constraints, or responsibility language when the case is used as a DPF probe.

In a homotopy explanation, a space, path, or loop may be written as if it "wants" to deform or "remembers" a hole. That can help intuition, but the focalized object is not an agent. The repair is to state the formal relation being highlighted and where the personification stops.

In live commentary, viewpoint may follow one player, coach, or tactical unit. That can make the stream intelligible, but it may hide off-ball actions, referee uncertainty, or later official correction. The commentary record needs the hidden-structure note before blame or capability claims are treated as stable.

Use a literalization rewrite ladder.

| Risky phrase | Safe if read as | Repair if literal reading would be false |
| --- | --- | --- |
| "The architecture wants..." | Shorthand for a selected quality pressure. | Name the architect, decision, characteristic, or trade-off owner. |
| "The paper proves..." | Shorthand for a source claim inside the paper. | Name proof status, evidence owner, or author claim. |
| "The model knows..." | Shorthand for model output behavior. | Name the training-data claim, admitted source basis claim, or method claim and admission boundary. |
| "The protagonist represents the system..." | Reader-facing focalization. | State which source structures the protagonist highlights and hides. |
| "The market punished..." | Aggregate outcome narrative. | Name actual actors, mechanism uncertainty, evidence owner, or lower the claim. |

When the phrase is kept for readability, put the safe reading close enough that a reader will not need a hidden glossary. "The architecture wants fewer dependencies" can be followed by "more precisely, the selected architecture characteristic rewards fewer dependency edges under this trade-off." If that clarification ruins the passage, the passage was probably carrying more authority than the source supports.

Use alternate viewpoint when one viewpoint hides a load-bearing source structure. A learner-facing story may first focalize the novice, then briefly switch to the maintainer who pays the cost of hidden coupling. A live commentary may follow the attacking player, then mark what the defensive line or official review could change. A future-scenario narrative may focalize a user, then return to the system owner for constraints and responsibility.

Filled viewpoint records:

```text
NarrativeViewpointAgencyDiscipline@ArchitecturePersonification:
  viewpointOrVoice: teacher voice using personification
  focalizedObjectRef: selected architecture candidate
  revealedSourceStructureRefs: coupling pressure; cohesion target; interface exception
  hiddenOrWeakenedSourceStructureRefs: architect role assignment; decision record; telemetry
  narrativeFunctionTerms: "architecture wants" as memory aid
  personificationOrAgencyWording: architecture described as wanting fewer dependencies
  directOwnerRefs: architect role assignment; architecture decision; characteristic evaluation
  blockedAgencyOverread: architecture is not an agent and has no responsibility
  repairAction: add "more precisely" sentence naming characteristic pressure and decision owner
```

```text
NarrativeViewpointAgencyDiscipline@FictionalProtagonistProbe:
  viewpointOrVoice: close protagonist viewpoint for private storycraft testing
  focalizedObjectRef: protagonist function in continuation route
  revealedSourceStructureRefs: character agency constraint; premise; causal plot support
  hiddenOrWeakenedSourceStructureRefs: alternative viewpoints; broader canon conflicts; publication rights
  narrativeFunctionTerms: protagonist; actant; motivation
  directOwnerRefs: source-pack and canon owner; agency and role owner when moral responsibility is claimed
  blockedAgencyOverread: protagonist centrality does not create moral permission or canon authority
  repairAction: record character action support and route rights and publication outside this DPF
```

```text
NarrativeViewpointAgencyDiscipline@LiveCommentaryView:
  viewpointOrVoice: commentator follows attacking side under time pressure
  focalizedObjectRef: attacking player or unit
  revealedSourceStructureRefs: possession, pressure, chance creation
  hiddenOrWeakenedSourceStructureRefs: defensive shape, off-ball movement, official review
  narrativeFunctionTerms: "forced", "wanted", "could not"
  directOwnerRefs: event source owner; evidence owner for claims; ethics owner if blame or harm framing appears
  blockedAgencyOverread: live focalization is not settled blame or capability assessment
  repairAction: mark provisional interpretation and later source-return route
```

The practitioner should be able to fill at least a compact version of this record before using strong agency language. If the record feels too heavy for the use, lower the language: use "is presented as", "the route follows", "the example highlights", or "the story treats" rather than "decides", "knows", "forces", or "is responsible".

### NSTD.4:6 - Bias-Annotation

This pattern blocks story-function agency drift: protagonist, actant, focalized object, voice, or personification is read as role assignment, capability, responsibility, or moral standing. Repair by splitting narrative function from current FPF owners for agency, role, capability, responsibility, ethics, evidence, and assurance claims. Scope: DPF-local for viewpoint and agency treatment in narrative renderings; it does not create a new agency ontology.

### NSTD.4:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD4-1` | Viewpoint, voice, focalized object, or protagonist choice is named when load-bearing. |
| `CC-NSTD4-2` | Revealed and hidden source structures are explicit. |
| `CC-NSTD4-3` | Protagonist, actant, and focalized object remain narrative functions unless direct owner admits role, assignment, agency, capability, or responsibility. |
| `CC-NSTD4-4` | `C.9` is not used as an operational owner while planned only. |
| `CC-NSTD4-5` | Personification has a repair route: literal owner, lowered wording, or source-return note. |

### NSTD.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Protagonist as responsible agent | Narrative centrality becomes moral or operational responsibility. | Split protagonist function from `A.13`, `A.2.1`, and ethics owner claims. |
| Episteme as actor | A paper, standard, pattern, or model "decides" or "knows". | Rewrite as source-use, evidence, method description, or author work through direct owners. |
| Viewpoint hides harmed party | A compelling viewpoint erases affected parties. | Route to `D.1` through `D.5` and add a source-return or viewpoint correction. |

### NSTD.4:9 - Consequences

The benefit is that storycraft remains available without agency inflation. The cost is that some memorable phrases need repair or explicit personification status.

### NSTD.4:10 - Rationale

Narrative voice and focalization are not decorative only. They shape source visibility and responsibility cues. FPF therefore treats them as source-structure rendering choices that may trigger role, agency, capability, ethics, evidence, or assurance owners.

### NSTD.4:11 - SoTA-Echoing

Schmid's `Narratology: An Introduction` and Chihaia's `Introductions to Narratology: Theory, Practice and the Afterlife of Structuralism` supply voice, focalization, actant, and perspective vocabulary as narrative-function language; Chen and Xu's "Neural and Behavioral Evidence for Differential Processing of Narrative Perspective in Novel Reading" gives current support that perspective can change processing; Nguyen-Trung and Nguyen's "Narrative-Integrated Thematic Analysis" keeps LLM-assisted narrative analysis tied to human interpretive agency. The DPF adopts the attentional and perspective value, while rejecting any automatic agency or responsibility import.

Operational payload:

- From narratology, voice, focalization, protagonist, and actant are useful because they locate attention and function inside a narrative. `NSTD.4` keeps them as narrative functions unless another FPF owner admits a stronger claim.
- From perspective-processing evidence, viewpoint can change what readers process and remember. It is not ornamental. The pattern therefore requires revealed and hidden source structures.
- From LLM-assisted narrative analysis, machine-suggested themes or viewpoints do not remove human interpretive responsibility. Tool-mediated viewpoint choices need admission and human owner routing.
- From FPF agency and role patterns, narrative centrality is not role assignment. A character, model, architecture, organization, or source can be focalized without becoming an agent.
- From ethics patterns, viewpoint can erase affected parties. When harm, blame, policy, or responsibility is live, a single compelling viewpoint is insufficient.

The practical consequence is that viewpoint is both a design tool and a risk locus. It earns its place by revealing needed source structure and naming what it hides.

### NSTD.4:12 - Relations

Uses `A.6.3.NAR`, `A.13`, `A.2`, `A.2.1`, `A.2.2`, `A.19.ECS`, `C.16`, `D.1` through `D.5`, `A.10`, `B.3`, and `G.11`. Reopen when viewpoint changes source visibility or when new source-pack or FPF agency owners change the owner map. Support-map entry: open `Architecture and Narrative Work Bridge` when viewpoint or focalization is really an architecture view and viewpoint over selected structures; open `Semiotic And Language-Precision Bridge` when voice, focalization, salience, sign, or language-state choice changes interpretation; open `DPF Precision Restoration And Owner Map` when protagonist, actant, agency, personification, or responsibility wording needs owner split.

### NSTD.4:End

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

Use this pattern when a team must decide whether one admitted narrative rendering version is good enough for one declared reader or listener use.

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

Construct and use one narrative rendering quality evaluation characteristic space for one declared use.

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

Default value meanings for ordinal content evaluation:

| Value | Meaning |
| --- | --- |
| `0` | Wrong-kind object, no admissible basis, or evaluation must stop before value use. |
| `1` | Object is a narrative rendering but unusable for the declared use. |
| `2` | Orientation only; source return is needed before reliance. |
| `3` | Locally usable with named limitations and repair obligations. |
| `4` | Good for declared use with bounded losses and source return. |
| `5` | Strong for declared use; source relation, repair history, and boundary cases are replayable. |

Default floor: for reliance-bearing or teaching use, all load-bearing characteristics must be at least `4`, and `NarrativeRenderingEpiplexity`, `OrderingRecoverability`, and `SourceReturnReadiness` may not be below `4`. When the selected source structure is a constraint-governed unfolding structure, `DemonstrativeSliceRecoverability` is load-bearing and may not be below `4`. A local low-risk orientation use may set floor `3` only if non-admissible downstream use is explicit.

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

Before assigning values, require construction-route evidence. The evaluator must be able to point to the records or source passages that played the role of `NSTD.1` source selection, `NSTD.2` ordering, `NSTD.3` event or mechanism support when live, `NSTD.4` viewpoint and agency discipline when live, `NSTD.5` engagement boundary when live, `NSTD.7` generated-carrier admission when live, and `NSTD.8` learning-route design when live. If those records were not written before drafting, they may be reconstructed from source and carrier, but the reconstruction must be explicit. Do not allow "the narrative already looks good" to substitute for the missing construction route.

Use this evaluation sequence:

1. Object-kind fit: is this an admitted narrative rendering version, not source text, source pack, slide deck, prompt output, style guide, or broad communication plan?
2. Construction-route fit: can the evaluator recover the selected source structures, ordering rule, source-return condition, and live neighboring governing-pattern routes?
3. Declared-use fit: is the reader or listener use narrow enough to evaluate, and are non-admissible downstream uses stated?
4. Load-bearing characteristics: assign values only to the characteristics needed for the declared use, but include every characteristic whose failure would make the use unsafe or useless.
5. Low-value repair: for every value below floor, name the smallest repair route before proposing style, drama, or generation retries.
6. Re-evaluation route: if any repair changes the object version or selected source basis, plan a new `NSTD.6` evaluation before claiming improvement.

Missingness and lowering rules:

| Missing or defect condition | Lowering rule |
| --- | --- |
| Selected source structures absent | `NarrativeRenderingEpiplexity` no higher than `1`; evaluation may stop as wrong object if the rendering has no recoverable source-structure denominator. |
| Ordering rule absent | `OrderingRecoverability` no higher than `2`. |
| Source temporal posture, rendering mediation mode, narrating worker, or reader role absent | `TemporalPostureAndRoleFit` no higher than `2`; return to `NSTD.1` before trusting evaluation. |
| Source-structure selection rationale or reader-interest hypothesis absent | `NarrativeRenderingEpiplexity` no higher than `2`, `TemporalPostureAndRoleFit` no higher than `2`, and evaluation must return to `NSTD.1` before style or engagement repair. |
| Source-return condition absent | `SourceReturnReadiness` no higher than `2`. |
| Constraint-governed unfolding structure is selected but the rendering declares only a sequence, route card, story line, or lesson chain | `DemonstrativeSliceRecoverability` no higher than `2`; return to `NSTD.1`, `NSTD.2`, and `A.22.CGUS` or the local governing pattern before treating the narrative as a rendering of the wider structure. |
| Artistic, literary, simplified, or dramatic wording changes source recovery without owner routing | `LanguageStatePrecisionAndCoarseningFit` no higher than `2`; return to `C.2.LS`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, or `C.16.Q` before treating style repair as improvement. |
| Early hook, vibe, story seed, or route hint is evaluated as an admitted narrative rendering | Wrong-kind object for this evaluation; return to `A.16.1`, then `NSTD.1` and `NSTD.2` when route selection becomes explicit. |
| Engagement effect asserted without persuasion boundary when influence is live | `EngagementBoundedness` no higher than `3` and ethics owner must be named. |
| Generated output not admitted through `C.35` | Wrong-kind object for this evaluation; return to `NSTD.7` and `C.35`. |
| Evidence or assurance claim made without owner | Relevant characteristic value lowered and claim routed to `A.10` or `B.3`. |

Default narrative rendering quality characteristics:

| Characteristic | Evaluation question | Low-value repair action |
| --- | --- | --- |
| `SourceStructureSelectionFit` | Are the selected source structures and reader-interest or use hypothesis explicit, non-magical, and well matched to the declared use? | Reopen `NSTD.1`; reconstruct or revise the source-structure selection rationale before changing style, drama, or prompt wording. |
| `NarrativeRenderingEpiplexity` | How much of the selected source-structure denominator is recoverably pulled into this narrative rendering for the declared use, observer boundary, and source-return condition? | Reopen `NSTD.1`; add source refs, source pins, preserved, foregrounded, or lost-structure accounting, or source-return links. Use `C.33` when architecture-relevant structural-information capture is current. |
| `OrderingRecoverability` | Can the reader say why this sequence was chosen and what it hides? | Reopen `NSTD.2`; state ordering rule, preserved relations, and lost relations. |
| `DemonstrativeSliceRecoverability` | When a constraint-governed unfolding structure is selected, can the reader recover the wider structure, the demonstrative slice, and the hidden branches, loops, alternatives, direct exits, or stop conditions? | Reopen `NSTD.1` and `NSTD.2`; name the selected CGUS or local block, the demonstrative slice, preserved constraints, lost structure, and return to `A.22.CGUS` or the local governing pattern. |
| `TemporalPostureAndRoleFit` | Do source temporal posture, rendering mediation mode, narrating or rendering worker, reader or listener role, uncertainty, and source-return obligation match the declared use? | Reopen `NSTD.1`; mark retrospective, live, prospective, architecture-mediated, or mixed posture; repair narrator and reader role split and lower claims that overread provisional or fictional structure. |
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
| FPF seminar handout | `NarrativeRenderingEpiplexity` | `4` | Learners can recover `EntityOfConcern`, forces, solution, and neighboring exits from the handout. | To reach `5`, add a transfer task where learners choose a governing pattern for a new situation. |
| FPF seminar handout | `SourceReturnReadiness` | `5` | Every slogan-like line has a source pattern return and one reconstruction exercise. | No proposal unless source patterns change. |
| FPF seminar handout | `EngagementBoundaryFit` | `4` | Failure story is marked as archetype, not evidence. | Add an explicit evidence-owner exit if the story is used in public adoption material. |
| Homotopy explanation | `LanguageStatePrecisionAndCoarseningFit` | `3` | Analogy is vivid but learners may not know where formal conditions return. | Add an analogy-stop line and a formal boundary task. |
| Homotopy explanation | `OrderingRecoverability` | `4` | Didactic order is named and proof order is deferred by value. | To reach `5`, add a second problem where learner maps story order to formal dependency order. |
| Franchise continuation probe | `SourceReturnReadiness` | `4` | Private source-pack constraints and non-publication boundary are named. | Add a continuity perturbation test: change one premise and check whether event support remains valid. |
| Live commentary | `EventMechanismSupport` | `3` | Observation and provisional interpretation are separated, but later telemetry return is only generic. | Add specific official record, replay, or statistics return condition. |
| Generated graph-to-text narrative | `GeneratedCarrierAdmissionFit` | `2` | Output is fluent, but source plan and selected lost relations are not admitted. | Return to `NSTD.7`; do not call this an admitted rendering yet. |

#### Before and after evaluation repair

Before evaluation statement:

> The narrative is strong because readers liked it and remembered the main point.

Failure: engagement and memory are treated as total quality. Source recovery, relation strength, owner routing, and use boundary are absent.

After evaluation statement:

> For the declared onboarding use, the rendering receives value `4` on source recovery because learners can reconstruct the pattern-use route, value `3` on source-return readiness because two slogans lack pattern-body refs, and value `4` on engagement boundary because the failure story is marked as archetypal. The first repair is to add source-return refs for the slogans before changing style.

Now `E.23` has a real changed slice: add two source-return refs and re-evaluate. It is not "make it better somehow".

#### Adjacent-value calibration

| Characteristic | `3` means | `4` means | `5` means |
| --- | --- | --- | --- |
| `NarrativeRenderingEpiplexity` | Some selected structure is recoverable, but important preserved or lost structure is implicit. | Selected structure, intentional loss, observer and use boundary, and source return are recoverable. | Recovery survives a heterogeneous transfer or perturbation case. |
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

`NSTD.6` teaches that epiplexity is not a mood about detail. It asks how much selected structure is recoverable in this rendering, for this observer and use, with explicit losses and source returns. For architecture-relevant renderings, `C.33` remains the stronger owner. For ordinary narrative renderings, the DPF-local epiplexity basis keeps the same information discipline without pretending that every story is an architecture description.

Pass case: an FPF seminar handout narrates how a practitioner moves from problem frame to forces to solution and checks. It names FPF pattern source sections, ordering rule, learner reconstruction task, and source-return points. Values reach `4` or `5` for teaching orientation, but the handout is not evidence that FPF is correct.

Fail despite fluency: a polished architecture story says one chosen architecture "won" because it felt coherent, hides rejected candidates, omits architectural characteristics, and gives no source-return path. `NarrativeRenderingEpiplexity`, `OrderingRecoverability`, and `SourceReturnReadiness` fall below floor even if engagement is high.

Wrong-kind object: an LLM produces a fluent story before `C.35` carrier admission and before selected source structures are recoverable. The object returns to `NSTD.7` and `C.35`; `NSTD.6` may record object-kind-fit value `0`, but it must not evaluate the text as an admitted narrative rendering.

### NSTD.6:6 - Bias-Annotation

This pattern blocks proxy-as-quality drift: readability, fluency, liking, engagement, expert approval, or generated-text benchmark value replaces object-kind fit and declared-use rendering quality. It also blocks the opposite drift where a test program is treated as the characteristic itself. Repair by selecting the evaluated object kind, scales, value meanings, evidence basis, missingness and lowering rules, floor, result rows, and repair actions. Scope: DPF-local for evaluating narrative rendering versions; it does not govern evidence, assurance, gate, decision, or publication authority.

### NSTD.6:7 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-NSTD6-1` | Evaluated object kind, declared use, and object-kind fit rule are explicit. |
| `CC-NSTD6-2` | At least three discriminating cases are present: pass, below-floor, and wrong-kind. |
| `CC-NSTD6-3` | Each characteristic binds one scale or is explicitly an ordinal content evaluation. |
| `CC-NSTD6-4` | Value meanings, evidence basis, missingness rules, floor, exceptional meaning, and stop or reopen condition are declared. |
| `CC-NSTD6-5` | Result rows include value, evidence basis, lowering reason, repair action, owner, and reopen condition. |
| `CC-NSTD6-6` | Measurement, eval program, evidence, assurance, gate, decision, publication, and pattern-quality claims route to owners. |
| `CC-NSTD6-7` | If repeated improvement is claimed, the `E.22` or `E.23` input names object version, `NSTD.6` as evaluation, improvement aim, protected trade-offs, allowed change slice, cost and risk account, and expected re-evaluation form. |
| `CC-NSTD6-8` | No quality movement is claimed until the changed narrative rendering version or declared changed slice is re-evaluated by `NSTD.6` or a declared stronger evaluation. |

### NSTD.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Fluency benchmark value as quality | Smoothness replaces structure recovery. | Lower source-related characteristics and repair through `NSTD.1` through `NSTD.3`. |
| Style repair as precision repair | A nicer wording pass is treated as sufficient while relation kind, quality sense, language-state threshold, or coarsening loss remains hidden. | Lower `LanguageStatePrecisionAndCoarseningFit`; apply the selected FPF precision, coarsening, explanation, or language-state owner before assigning value movement to style gains. |
| Prompt loop as improvement | The worker keeps regenerating more engaging drafts without a named object version, allowed change slice, protected trade-offs, or re-evaluation. | Open `E.22` when needed, route the repair to `E.23`, and re-evaluate the changed version through `NSTD.6`; otherwise keep the generated text as an unadmitted candidate carrier under `NSTD.7` and `C.35`. |
| Evaluation theft | Quality result is used as evidence, assurance, or gate. | Keep `NSTD.6` as evaluation; route wider use to `A.10`, `B.3`, or gate owner. |
| Wrong-kind evaluation | Source text, style guide, script, or generated output is evaluated as narrative rendering. | Apply object-kind fit and return to the correct evaluation or admission owner. |
| Characteristics as eval programs | Test scripts or automated checks are treated as characteristics. | Keep characteristics in `A.19.ECS`; automated evals are measurement or eval-program carriers under direct owners. |

### NSTD.6:9 - Consequences

The benefit is a usable improvement target: `E.23` can improve narrative versions because values, floors, evidence, and repairs are declared. The cost is heavier evaluation before reliance-bearing use.

### NSTD.6:10 - Rationale

`A.19.ECS` says improvement cannot be better than its evaluation. `NSTD.6` specializes that lesson for narrative renderings: first recover object kind and use, then choose characteristics that discriminate narrative rendering quality for that declared use.

### NSTD.6:11 - SoTA-Echoing

FPF `A.19.ECS` and `C.16` supply the characteristic-space and result-row discipline. FPF `C.33` supplies the structural-information note for architecture-relevant carriers, while the same general epiplexity line supplies the broader DPF pressure: a carrier is useful only to the extent that selected structure is recoverable under an observer and use boundary. FPF `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, and `C.16.Q` supply the language-state, cue, backoff, coarsening, explanation, lexical, relation, and quality-term repairs that narrative work often needs under different vocabulary. Castricato et al.'s "Towards a Formal Model of Narratives" supports evaluating narrator-reader information flow, reader story-model evolution, uncertainty, and conveyed-information accuracy. Mengelkamp et al.'s "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" and Georgiou et al.'s "Large-scale study of human memory for meaningful narratives" make declared learner use, memory, and overconfidence measurable pressures. Ma et al.'s "Text-to-Text Automatic Story Generation: A Survey" and Rahman et al.'s "Game Knowledge Management System: Schema-Governed LLM Pipeline for Executable Narrative Generation in RPGs" show that generated narratives need coherence, controllability, structural and semantic evaluation, and human-study probes rather than fluency alone. The DPF adopts those moves through `A.19.ECS`, `C.16`, DPF-local epiplexity basis rules, and FPF owner-routing for language-state and precision repairs, not by importing a generic writing-quality rubric.

### NSTD.6:12 - Relations

Uses `A.19.ECS`, `A.17`, `A.18`, `C.16`, `C.16.Q`, `C.2.LS`, `A.16.1`, `A.16.2`, `A.6.3.CSC`, `E.17.EFP`, `E.10`, `A.6.P`, `C.33`, `E.22`, `E.23`, `B.4`, `A.10`, `B.3`, `E.17`, `C.35`, and `G.11`. `C.33` is used here only when the evaluated narrative rendering is an architecture-relevant structural-information carrier; non-architecture cases keep the epiplexity basis local to `NSTD.6` until a broader FPF owner is admitted. `E.23` consumes `NSTD.6` result rows only after object version, allowed change slice, protected trade-offs, cost and risk, and re-evaluation form are explicit. `B.4` is used only for an evolution claim over a narrative episteme, learning route, or other holon under repeated use; `G.11` handles currentness and refresh. Reopen when evaluated object kind, declared use, source pack, characteristic set, language-state profile, cue or backoff status, coarsening or explanation relation, precision-restoration result, epiplexity basis, value meanings, floor, evidence basis, allowed improvement slice, or low-value repair route changes. Support-map entry: open `Architecture and Narrative Work Bridge` when `NarrativeRenderingEpiplexity` is architecture-relevant or tied to `C.33`; open `Semiotic And Language-Precision Bridge` for language-state, coarsening, explanation, relation, or quality-word repairs; open `Source Use And Refresh Map` when evidence basis or source-currentness supports a value; open `DPF Precision Restoration And Owner Map` when a characteristic name risks becoming a new ontology.

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
| Structure capture and loss | `C.33` for architecture-relevant carriers; `NSTD.6` epiplexity basis for non-architecture DPF cases |
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
| Schema compliance as source fidelity | The story satisfies a schema but changes the selected source structure or a constraint in the admitted source basis. | Add `C.34` correspondence checks; use `C.33` capture-loss checks only for architecture-relevant structural-information use, and use `NSTD.6` epiplexity for non-architecture source-structure loss. |
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

Uses `G.2`, `C.35`, `A.6.3.NAR`, `C.33` for architecture-relevant structural-information capture or loss, `C.34`, `NSTD.6`, `A.19.ECS`, `C.16`, `E.22`, `E.23`, `A.10`, `B.3`, `D.1` through `D.5`, and `G.11`. `E.22`/`E.23` apply only after carrier admission and `NSTD.6` result rows exist; generation retries remain carrier candidates until re-evaluation. Reopen when admitted source basis, generator, method, schema, admission note, evaluation result, or generated-narrative SoTA changes. Support-map entry: open `Source Use And Refresh Map` when generation, NLG, story-planning, schema, or source-pack claims are relied on; open `DPF Precision Restoration And Owner Map` when generated source plan, plot plan, schema constraint, admission, correspondence, or responsibility words blur object kinds; open `Semiotic And Language-Precision Bridge` when prompt output changes language state, coarsening, cue, or quality wording.

### NSTD.7:End

## NSTD.8 - Learning-Route Narrative Rendering and Reconstruction Return

> **Type:** DPF pattern body

> **Primary EntityOfConcern:** `LearningNarrativeRoute@Context`, a source-returnable learning route plus its teaching or learning publication-carrier relation and evaluation route.

### NSTD.8:1 - Problem frame

Use this pattern when a complex source structure must be taught, explained, or learned through a narrative route, and the route must preserve enough structure for learners to reconstruct and apply it later.

First useful move: name learner use, source-structure spine, learning-step ordering rule, source-return links, learner reconstruction tasks, and evaluation route.

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
| Anchor pass | Repeated terms, diagrams, questions, or cases that return learners to the source spine. | Learners remember episodes but lose the framework. |
| Reconstruction pass | Tasks that ask learners to rebuild source structure, not only recall the narrative. | Satisfaction and memory replace practical competence. |
| Evaluation pass | `NSTD.6` rows for one route version and declared learner use. | Teaching tweaks are treated as improvement without evidence. |

Do not optimize the learning-route architecture for local neatness. A locally neat blocked route can be globally weak: it gives learners the answer key for the current block, so they do not practice selecting the right owner under mixed cues. Interleaving is useful when the learner must later discriminate similar patterns, methods, proof obligations, architecture structures, or source-return owners. Spacing is useful when the learner must still retrieve a structure after other material has intervened. Use them as design moves with declared learner use, not as decorative variety.

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

Use a two-column lesson plan before writing materials.

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

### NSTD.8:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
| --- | --- | --- |
| Learning route as source structure | Lesson sequence, seminar order, analogy chain, or explainer order is treated as framework architecture, proof order, or source structure. | Declare learning-step ordering rule and source-return links. |
| Reference manual as course | The source topic map is copied into lessons one topic at a time. | Keep the topic map as source architecture; design a learning-route architecture with interleaved and spaced retrieval. |
| Blocked practice fluency | Learners perform well inside each topic block because the block label gives away the owner. | Add mixed owner-choice cases and delayed no-label retrieval before claiming transfer. |
| Materials inside pattern body | Slides or exercises are inserted into DPF patterns. | Move them to teaching publication-carrier files and reference only the carrier relation. |
| Recall as reconstruction | Learners remember examples but cannot use patterns. | Add reconstruction and application tasks; evaluate through `NSTD.6`. |
| Teaching tweak as evolution | A revised slide, example, or prompt is described as evolved route quality without telemetry and re-evaluation. | Treat the tweak as an `E.23` changed slice after `NSTD.6`; use `G.11` for refresh and reserve `B.4` for actual evolution claims over the route across operation. |

### NSTD.8:9 - Consequences

The benefit is a teachable path that stays source-returnable and can be improved without confusing entertainment with understanding. The cost is maintaining separate teaching publication carriers and evaluation evidence.

### NSTD.8:10 - Rationale

Didactic primacy requires examples, analogies, routes, interleaving, and spaced returns. Ontological discipline requires that learning publication carriers do not become the source framework. This pattern holds both: the route is designed, tested, and refreshed without entering pattern bodies as teaching content.

The architectural lesson is counterintuitive for engineers. In a source corpus, strong modularity often helps: each pattern or topic has its own boundary, internal coherence, and relation exits. In a learning route, copying that modularity can hurt. Learners need to meet similar structures under varied cues, return to earlier distinctions after delay, and practice choosing the right owner when the block label is gone. Therefore the course architecture is a transformation over the source architecture, not a mirror of it.

### NSTD.8:11 - SoTA-Echoing

Mengelkamp et al.'s "Effects of Reading Goal Instructions on the Comprehension and Metacomprehension of Informative Narratives" makes study goals and metacomprehension risk visible; Georgiou et al.'s "Large-scale study of human memory for meaningful narratives" shows that long narratives can be remembered as gist and sequence rather than source detail; Hoffmann's "The Tensions of Scientific Storytelling" supplies a science-storytelling example where unresolved tension and source return matter. Dunlosky et al.'s "Improving Students' Learning With Effective Learning Techniques" rates practice testing and distributed practice as high-utility techniques and treats interleaved practice as promising for appropriate situations. Rohrer and Taylor's "The shuffling of mathematics problems improves learning" directly shows the risk of standard blocked textbook practice and the benefit of spaced and mixed practice in mathematics problems. Kang's "Spaced Repetition Promotes Efficient and Effective Learning" gives a policy-level synthesis: spacing repeated encounters with material improves long-term learning and can be combined with tests. Until a separate curriculum-design or cognitive-apprenticeship source row is admitted, `NSTD.8` uses these sources for learning route, reconstruction, memory, spacing, interleaving, engagement-boundary, and source-return pressure, not as a complete pedagogy doctrine.

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
6. `NSTD.6`: evaluate the route only after the above fields exist; a low `NarrativeRenderingEpiplexity` value sends the route back to source-spine selection rather than to style polish.

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

1. `NSTD.1`: name listener use, live temporal posture, commentator or rendering worker, event-source owner, provisional interpretation boundary, and source-return route.
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
| developer or transformer role receiving architecture work | writer, narrator, teacher, commentator, story designer, tool operator, performer, generator controller | Name the narrating or rendering worker in `NSTD.1`; use A.15-family owners only when method, work, readiness, or performed-work claims become live. |
| structural information capture and source return in `C.33` | how much selected source structure got into the story, what the story hides, what must be checked in the admitted source basis or direct governing pattern, epiplexity of rendering | Use `NarrativeRenderingEpiplexity` in `NSTD.6`; use `C.33` when the carrier is architecture-relevant structural information. |
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
| Castricato et al., "Towards a Formal Model of Narratives"; prospective narrative practice such as design-fiction or experiential-futures sources | `NSTD.1`, `NSTD.2`, `NSTD.4`, `NSTD.6`, acceptance cases | Narrating worker, reader or listener role, reader story-model evolution, uncertainty, and temporal posture become explicit drafting and evaluation slots; these rows do not create FPF Core ontology. |
| Green and Brock, "The Role of Transportation in the Persuasiveness of Public Narratives"; Dahlstrom and Ho, "Ethical Considerations of Using Narrative to Communicate Science"; Meretoja, "Narrative and Human Existence: Ontology, Epistemology, and Ethics" as background only; FPF `D.1` through `D.5` | `NSTD.5`, `NSTD.6`, acceptance cases | Engagement and persuasion are real design effects, but ethics, harm, evidence, and assurance stay with FPF owners. |
| Dunlosky et al., "Improving Students' Learning With Effective Learning Techniques"; Rohrer and Taylor, "The shuffling of mathematics problems improves learning"; Kang, "Spaced Repetition Promotes Efficient and Effective Learning" | `NSTD.8`, `NSTD.6`, architecture bridge, source-use refresh | Learning-route architecture may need spaced retrieval and interleaving rather than blocked topic order; a coherent source architecture must not be copied automatically as the course architecture. |
| Gatt and Krahmer, `Survey of the State of the Art in Natural Language Generation`; Alabdulkarim et al., "Automatic Story Generation: Challenges and Attempts"; Cardona-Rivera and Ware et al., "The Story So Far on Narrative Planning"; Chakrabarty et al., "SceneCraft"; Ma et al., "Text-to-Text Automatic Story Generation: A Survey"; Rahman et al., "Game Knowledge Management System"; Nguyen-Trung and Nguyen, "Narrative-Integrated Thematic Analysis" | `NSTD.7` | Generation splits content planning, discourse planning, method, schema, repair, admission, evaluation, and human interpretive agency; fluency never grants authority. |

Refresh condition: use `G.11` when source pack, FPF Core edition, narrative-studies source basis, generated-narrative practice, reader telemetry, teaching-test evidence, or evaluation results change.

## DPF Precision Restoration And Owner Map

These terms are local working vocabulary unless a source owner and naming owner admit a more durable term. The map states the owner and blocks accidental `U.*` minting.

| Term | Kind and owner | Use in this DPF | Blocked overread |
| --- | --- | --- | --- |
| admitted source basis | Existing FPF source or episteme use; `G.2`, `A.10`, `E.17.EFP` as applicable | Admitted source pack, source publication carrier, architecture description, pattern body, event record, formal text, or other episteme from which selected source structures may be recovered for this narrative use | Not the selected source structure by itself and not a permission to treat every mentioned object as source authority |
| selected source structure | Existing FPF structure use; `A.22`, `A.6.3.NAR`, `C.33` when architecture-relevant structural-information capture is current | Structure that must remain recoverable after rendering | Not the narrative rendering and not evidence authority |
| source-structure selection rationale | DPF-local slot under `NSTD.1`, with source-owner support when needed | Why these structures were selected for the declared reader or listener use and not merely because the current rendering foregrounded them | Not proof that the selection is correct and not a substitute for source, evidence, or architecture owners |
| source temporal posture | DPF-local slot under `A.6.3.NAR` and `NSTD.1` | Whether the selected source structure or admitted source basis concerns retrospective or reverse-engineered actual structure or event record, live unfolding, prospective planned structure, prospective fictional structure or canon, or a mixed case | Not evidence strength, chronology, or publication date by itself |
| rendering mediation mode | DPF-local slot under `A.6.3.NAR` and `NSTD.1` | Whether narrative rendering is direct source-structure rendering, architecture-mediated rendering, or mixed | Not a claim that all narrativization is architecture and not a reason to bypass architecture owners when architecture is live |
| architecture-mediated narrativization route | Rendering mediation mode using architecture understanding, architecture description, views, viewpoints, decisions, candidate structures, or telemetry as mediating source | Narrate actual or future holon structure for a declared reader or listener use | Not architecture decision, not architecture description itself, and not implementation authority |
| narrating or rendering worker | DPF-local role slot under `NSTD.1`, with human or tool responsibility routed to direct owners | Writer, narrator, teacher, commentator, story designer, or tool-mediated worker arranging source structure into narrative | Not source owner, evidence owner, ethical owner, or responsible agent unless direct owners assign that |
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
| narrative rendering epiplexity | DPF-local quality characteristic specializing the general epiplexity move; `NSTD.6`, `A.19.ECS`, `C.16`, with `C.33` when architecture-relevant structural-information capture is current | How much selected source structure is pulled into one narrative rendering for one declared use and observer boundary | Not a universal narrative value, not proof, not evidence, not assurance, and not a new U-kind |
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
  frameworkEditionRef: NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-06-30
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
  sourceRef: NarrativizationAndNarrativeStudiesPrinciplesFramework@2026-06-30
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