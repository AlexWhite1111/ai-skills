# Reader Cognition and Knowledge Evidence

Use this reference to design what the manuscript prepares a careful reader to do. It does not diagnose any real reader.

## Contents

- [Keep three states separate](#keep-three-states-separate)
- [Evidence vector](#evidence-vector)
- [Summary state](#summary-state)
- [Concept entry](#concept-entry)
- [Cognitive actions inside fiction](#cognitive-actions-inside-fiction)
- [Delayed return plan](#delayed-return-plan)
- [Working-memory budget](#working-memory-budget)
- [Productive and destructive uncertainty](#productive-and-destructive-uncertainty)
- [Evidence record](#evidence-record)
- [Transfer test for external evaluation](#transfer-test-for-external-evaluation)
- [False evidence warnings](#false-evidence-warnings)

## Keep three states separate

Track:

1. **character knowledge**: what a fictional person knows or believes;
2. **expected reader evidence**: what opportunities the manuscript has supplied;
3. **actual reader performance**: what a real reader demonstrates in testing.

Never infer the third from the first two.

## Evidence vector

Represent concept preparation across dimensions:

```text
recognition
prediction
representation_mapping
operation
discrimination
explanation
delayed_retrieval
transfer
```

Suggested meanings:

- `recognition`: identify the phenomenon, quantity, or concept when encountered;
- `prediction`: state what should happen when a relevant condition changes;
- `representation_mapping`: connect equation, diagram, code, measurement, and physical mechanism;
- `operation`: calculate, manipulate, configure, or apply a procedure;
- `discrimination`: separate nearby causes, methods, or failure modes;
- `explanation`: give a causal or formal account with assumptions and limits;
- `delayed_retrieval`: recover the concept after intervening chapters without a full re-teach;
- `transfer`: select and adapt the concept in a materially different context.

Use evidence values such as:

```text
none | opportunity | supported
```

`opportunity` means the manuscript invited the action. `supported` means the manuscript showed enough reasoning and feedback to make the action plausible for a careful reader. Neither means a real reader succeeded.

## Summary state

For compatibility, maintain a conservative summary:

```text
unseen
exposed
intuitive
operational
formal
transfer-ready
```

Derive it from evidence instead of advancing it by assertion.

A reasonable mapping is:

- `unseen`: no meaningful encounter;
- `exposed`: recognition opportunity only;
- `intuitive`: prediction or explanation is supported qualitatively, with a stated boundary;
- `operational`: operation or discrimination is supported on the target case;
- `formal`: required notation, definitions, derivations, or proof structure are licensed;
- `transfer-ready`: at least one materially different transfer opportunity is supported, and the concept has been retrieved after delay when the book's scale permits.

Do not require every book to reach every dimension. Match the end capability.

## Concept entry

Before introducing a concept, establish:

```text
target object
current reader model
what that model predicts
observable mismatch
smallest repair
representation used
immediate consequence
boundary
```

Do not introduce a taxonomy larger than the local decision needs.

## Cognitive actions inside fiction

Create active reasoning without adding textbook exercises.

### Prediction

Let a character commit to what should happen before a measurement, reveal, or experiment. The reader can form the same prediction.

### Discrimination

Keep two or more live explanations and introduce evidence that rules them apart. Make the diagnostic question legible.

### Self-explanation

Let a character justify a choice, teach another person imperfectly, defend a design, or reconstruct a failure. The explanation should have consequences and may expose a gap.

### Representation mapping

Return to the same object through waveform, spectrum, constellation, equation, code, or physical behavior. State what each view reveals and hides.

### Retrieval

Bring a concept back after unrelated events. Give a cue smaller than the original explanation. Let failure to retrieve have a manageable consequence, then repair it if necessary.

### Transfer

Use a new surface problem that requires selecting and adapting the idea. Changing only numbers, names, or colors is not transfer.

## Delayed return plan

For each major concept, schedule:

```text
first necessity
immediate use
first delayed return
misleading near-neighbor
transfer challenge
final integration
```

Do not repeat the original explanation verbatim. Each return should add a new cognitive action or expose a boundary.

Example:

```text
Orthogonality first appears through aligned projection.
Later, timing offset breaks the cancellation.
Still later, carrier-frequency offset creates inter-carrier interference.
Finally, the reader must distinguish timing, common phase rotation, and frequency offset from observed symptoms.
```

## Working-memory budget

Count unfamiliar changes, not merely terms.

A scene becomes overloaded when it asks the reader to hold several of the following at once:

- a new physical object;
- new notation;
- a new representation;
- a new causal mechanism;
- a new algorithm;
- a new exception;
- a new character or timeline;
- an emotional reversal.

Default to one major conceptual repair per scene and at most three unfamiliar transformations in active view. Compress familiar algebra, not the correspondence that licenses it.

Reuse notation, objects, and examples until the current gap is crossed.

## Productive and destructive uncertainty

Productive uncertainty:

```text
I know the candidate causes and the observation that could distinguish them.
```

Destructive uncertainty includes:

- representation break: symbols or objects lose referents;
- causal break: the conclusion does not follow;
- motivation break: the reader understands the explanation but not why it matters now;
- state break: the manuscript assumes an earlier capability that was never prepared.

Resolve destructive uncertainty. Preserve productive uncertainty when it fuels inference.

## Evidence record

A reader-state entry may use:

```json
{
  "state": "operational",
  "evidence_vector": {
    "recognition": "supported",
    "prediction": "supported",
    "representation_mapping": "opportunity",
    "operation": "supported",
    "discrimination": "opportunity",
    "explanation": "supported",
    "delayed_retrieval": "none",
    "transfer": "none"
  },
  "evidence": [
    "Chapter 4 asks the reader to predict which projection terms vanish over an aligned symbol interval.",
    "Chapter 4 then uses the result to reverse an incorrect filter change."
  ],
  "next_return": {
    "chapter_range": "7-9",
    "action": "distinguish timing offset from carrier-frequency offset"
  }
}
```

Evidence statements should identify the chapter action, not praise the prose.

## Transfer test for external evaluation

When real evaluation is available, give readers a new task after reading:

```text
new surface context
same underlying concept
enough information to solve
no copied wording from the chapter
observable answer or reasoning criteria
```

Score whether the reader selected the right concept, mapped variables, applied it, and stated limits. Keep literary preference evaluation separate from transfer performance.

## False evidence warnings

Do not advance state because:

- a mentor explained accurately;
- the protagonist said “I understand”;
- the narrator summarized the lesson;
- a formula appeared;
- the same example was repeated with new numbers;
- a validator passed;
- one model reviewer found the chapter clear.

These are exposure or process signals, not demonstrated capability.
