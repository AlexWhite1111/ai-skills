# Benchmark Specification

## 1. Evaluation target

This benchmark measures **robust natural-language proof synthesis under low prerequisite load**.

It is not primarily a test of:

- theorem recall;
- numerical answer production;
- symbolic algebra throughput;
- access to advanced vocabulary;
- web-search skill.

A good item is understandable from ordinary high-school mathematics, but its proof requires several local facts to cooperate before the conclusion closes.

## 2. General design laws

### 2.1 Low floor, high ceiling

Keep the objects familiar: real numbers, integers, finite sets, elementary functions, inequalities, sequences, plane geometry, or simple combinatorial processes.

Difficulty should come from organizing constraints, not from importing a rare theorem.

### 2.2 Multiple independent locks

A candidate should require at least two, preferably three, mechanisms that are not restatements of one another. Typical locks include:

- cardinality or parity;
- conservation or invariant;
- extremal reduction;
- sharp inequality;
- construction or equality analysis;
- local-to-global coverage.

The decisive signal is not proof length. It is whether removing one lock leaves a real unresolved gap.

### 2.3 Representation must be necessary but insufficient

Strong models are good at discovering compressed representations. A good frontier item may reward that ability, but one reformulation should not collapse 80–100% of the proof.

Run a **representation-collapse audit**:

1. identify the strongest natural encoding;
2. grant that encoding explicitly;
3. ask whether the remaining proof is still substantial;
4. reject the item if the remainder is routine.

### 2.4 Proof closure outranks answer discovery

The benchmark distinguishes:

- correct answer with complete proof;
- correct answer with a major gap;
- plausible route with an exact remaining lemma;
- incorrect answer;
- refusal or unsupported confidence.

A model that gives the right constant and skips the only difficult case has not solved the proof task.

### 2.5 Clean difficulty

Reject “difficulty” created mainly by:

- arbitrary large constants;
- long mechanical casework;
- obscure notation;
- hidden use of university-level theory;
- an author-only trick with no structural motivation;
- computational exhaustion without a certificate.

The desired reaction after seeing the proof is “the ingredients were available,” not “the author hid a key under a random stone.”

### 2.6 Novelty is procedural, not rhetorical

For every live item record:

- authoring date;
- exact frozen statement;
- reverse-search queries and results;
- known nearby problems;
- paraphrase and relabel tests;
- model exposure history;
- release date.

“No close match found” is the strongest safe claim unless independent provenance establishes more.

### 2.7 Live and hidden evaluation

Static public benchmarks eventually become training data. Official comparisons therefore use:

- `private-test`: frozen and access-controlled;
- `live`: authored, audited, and evaluated before public release.

After the evaluation window, retire items into `public-dev` with reference solutions and attack notes.

### 2.8 Adversarial repair is a first-class capability

Run at least one targeted repair round when the initial proof contains a concrete major gap. Measure whether the model:

- identifies the exact dependency under attack;
- repairs it with a valid argument;
- abandons a structurally blocked route when needed;
- reruns affected equality and boundary checks;
- produces a final self-contained proof.

### 2.9 Calibration controls

A useful suite contains easier controls:

- a familiar-template item;
- a one-representation item;
- a false-statement or overclaim item.

They reveal whether failure on the frontier item reflects general malfunction, lack of representation discovery, proof incompleteness, or sycophancy.

## 3. Item roles

| Role | Purpose | Official score eligible |
|---|---|---:|
| `template-calibration` | Detects standard-method recognition | No |
| `representation-calibration` | Detects strong reformulation ability | No |
| `proof-integrity-challenge` | Tests multi-lock proof closure | Public: no; hidden/live: yes |
| `falsification-control` | Tests counterexample search and resistance to false premises | Hidden/live: yes |
| `live-frontier` | Current official comparison item | Yes, before release |

## 4. Candidate acceptance gate

Rate each dimension from 0 to 3.

### Prerequisite load

- `0`: middle-school or elementary high-school objects;
- `1`: standard high-school olympiad knowledge;
- `2`: specialized olympiad theorem or nonstandard formalism;
- `3`: undergraduate or higher prerequisite.

### Template familiarity risk

- `0`: no close public match found and no dominant named method;
- `1`: nearby motifs exist, but the dependency structure is materially different;
- `2`: recognizable standard skeleton;
- `3`: classic problem or light re-skin.

### Multi-lock depth

- `0`: one observation solves the task;
- `1`: one dominant route plus routine cleanup;
- `2`: two independent locks;
- `3`: three or more independent locks with a nontrivial merge.

### Coverage burden

- `0`: local computation;
- `1`: one simple global argument;
- `2`: boundary, equality, or exhaustive-family coverage matters;
- `3`: several plausible partial proofs fail on distinct regimes.

### Audit richness

- `0`: no plausible wrong proof;
- `1`: one obvious trap;
- `2`: several tempting gaps or boundary failures;
- `3`: targeted attacks discriminate answer recognition from proof understanding.

A `live-frontier` candidate should normally satisfy:

- prerequisite load `<= 1`;
- template familiarity risk `<= 1`;
- multi-lock depth `>= 2`;
- coverage burden `>= 2`;
- audit richness `>= 2`;
- complete reference proof;
- at least one independent-context reconstruction;
- at least three recorded attacks;
- no unresolved critical or major issue.

These thresholds are gates, not a fabricated scalar “difficulty score.”

## 5. Run protocol

### 5.1 Freeze conditions

Before the first run freeze:

- item version and hash;
- exact prompt language;
- model/provider/version;
- reasoning setting;
- web and tool permissions;
- time, token, and retry budgets;
- whether follow-up attacks are allowed;
- grader and rubric version.

### 5.2 Access modes

#### `blind-proof`

No web, no retrieval, no external solver, no reference answer. Local scratch computation may be allowed only if stated.

#### `open-research`

Web and tools are allowed. Every external source and copied dependency must be recorded. This measures research-assisted proof production, not blind reasoning.

#### `solver-with-verifier`

A solver may call a checker, CAS, proof assistant, or critic under a fixed interface. Report verifier calls and distinguish formal certificates from heuristic checks.

### 5.3 Phases

1. **Initial proof**: statement only.
2. **Targeted attack**: smallest sufficient critique of a real defect.
3. **Final reconstruction**: one self-contained final proof.

Do not feed the reference route during repair unless the experiment explicitly studies hint use.

## 6. Scoring

### 6.1 Answer score: 0–2

- `0`: wrong target or no answer;
- `1`: partially correct target;
- `2`: correct conclusion, sharp constant, classification, or construction.

### 6.2 Proof score: 0–10

- target and quantifiers correctly understood: `0–1`;
- necessary structural reductions established: `0–2`;
- local inferences valid: `0–2`;
- global cases, boundaries, and dependencies covered: `0–2`;
- sharpness, construction, equality, or uniqueness completed: `0–1`;
- assumptions and scope explicit: `0–1`;
- no theorem-strength gap disguised by terminology or “routine calculation”: `0–1`.

### 6.3 Repair score: 0–4

- exact attack acknowledged: `0–1`;
- attacked dependency genuinely repaired: `0–2`;
- affected downstream claims rechecked: `0–1`.

### 6.4 Strict pass

`strict_pass = true` only when:

- the conclusion is correct;
- no critical or major defect remains;
- all required cases and equality/optimality claims are closed;
- the proof is self-contained under the declared prerequisite policy.

A numerical score never overrides an open critical or major defect.

### 6.5 Failure labels

Use one primary and any relevant secondary labels:

- `answer_error`;
- `template_miss`;
- `representation_collapse`;
- `local_invalid_step`;
- `global_coverage_gap`;
- `equality_gap`;
- `advanced-name-as-proof`;
- `search_contamination`;
- `sycophantic_acceptance`;
- `repair_without_closure`;
- `bounded_partial`;
- `strict_solve`.

## 7. Reporting

For each model report:

- strict-pass rate;
- answer accuracy;
- answer-correct/proof-fail rate;
- major-gap detection rate;
- repair closure rate;
- tool/search usage;
- median cost, latency, and output length when available;
- item-level failure labels.

Do not aggregate public-dev and hidden/live results into one headline number.

## 8. Public, private, and live lifecycle

1. Author candidate in private.
2. Complete reference proof and attack set.
3. Freeze exact statement.
4. Run models under fixed conditions.
5. Grade and, where possible, independently review.
6. Publish the run record.
7. Retire the item into public development data.
8. Replace it with a genuinely new private/live item.

Paraphrasing an exposed item is not enough to restore contamination resistance.

## 9. Methodological sources

The following projects motivate parts of this protocol:

- [FrontierMath](https://arxiv.org/abs/2411.04872): original, expert-vetted, previously unpublished mathematical items and strong verification discipline.
- [LiveBench](https://arxiv.org/abs/2406.19314): continuously refreshed evaluation to reduce static-benchmark contamination.
- [MathArena](https://arxiv.org/abs/2505.23281): evaluating newly released competition problems quickly and separating final-answer performance from proof-writing.
- [Proof or Bluff?](https://arxiv.org/abs/2503.21934): expert grading shows that full proofs expose failures hidden by answer-only scoring.
- [BrokenMath](https://arxiv.org/abs/2510.04721): false statements and user pressure reveal sycophantic theorem-proving behavior.
- [ARC Prize verified testing policy](https://arcprize.org/policy): hidden splits, controlled exposure, and reproducible testing policy as foundations of benchmark trust.

This skill focuses on a different niche: elementary prerequisites with adversarially audited, multi-lock natural-language proofs.
