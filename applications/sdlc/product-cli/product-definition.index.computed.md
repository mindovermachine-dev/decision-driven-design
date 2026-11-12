# Computed from `product-definition.index.yaml`

**Computed, never edited by hand.** Regenerate it when the index or a listed file changes. The index model is accepted; the index content is proposed, so these results are provisional.

## Files and hashes

| Role | File | Git blob |
|---|---|---|
| member | `applications/sdlc/product-cli/product-definition.md` | `8019dc03ce2e4083bcfafbe8b6625f7fae901b24` |
| import | `applications/sdlc/what.md` | `b69555bb5ee1ad5da48329df6462ce2536a0a201` |
| import | `spec/decision-provenance/dpp-1.md` | `14d3f879641e6afa993016f2cbaac502a46c02bc` |
| import | writ (outside this repository) | n/a |

Index content hash (sha256, first 16): `e5b3d66e2488094f`

## Checks

| Check | Result |
|---|---|
| Every home resolves to a heading | yes |
| Terms used with no explanation found | 5: aggregate, change set, head, scope rule, session transport |
| Terms whose home is outside this repository | 3: Writ, Writ position, grant |
| Cycles between sections | 1 |
| Forward references (used before the home, in reading order) | 43 |
| Indexed terms never used in the member files | none |

## Cycles

Each group of sections below needs every other section in the group to be read first.

- Proposals and decisions ⇄ The workbench ⇄ MCP ⇄ The vocabulary (`sdlc:`) ⇄ Shapes ⇄ The What-version record
  - "Proposals and decisions" needs "MCP" for: phase
  - "Proposals and decisions" needs "Shapes" for: shape
  - "The workbench" needs "Proposals and decisions" for: adoption, proposal
  - "The workbench" needs "MCP" for: phase
  - "The workbench" needs "Shapes" for: finding
  - "MCP" needs "Proposals and decisions" for: adoption, proposal
  - "MCP" needs "The workbench" for: workbench
  - "The vocabulary (`sdlc:`)" needs "The What-version record" for: What-version record
  - "Shapes" needs "The vocabulary (`sdlc:`)" for: edition
  - "The What-version record" needs "Proposals and decisions" for: adoption, proposal
  - "The What-version record" needs "The vocabulary (`sdlc:`)" for: edition

## Sections in reading order

Depth 0 needs no other section of the set. A higher depth needs more read first. Fan-in is how many sections need this one.

| # | Section | Depth | Fan-in | Needs (in the set) | Imports | No explanation found |
|---|---|---|---|---|---|---|
| 1 | Product: product definition | 0 | 0 | – | dpp, what, writ | – |
| 2 | 1. The promise | 3 | 0 | Proposals and decisions, Shapes, The canonical export, Decision records and the profile, Scenarios and the wire protocol | dpp, what, writ | – |
| 3 | 2. Who it is for | 3 | 0 | Proposals and decisions, The workbench, MCP, Shapes, Scenarios and the wire protocol, Decider and Projector logic | what, writ | – |
| 4 | 3. The surface | 0 | 0 | – | – | – |
| 5 | Commands | 4 | 0 | The draft log, Proposals and decisions, The workbench, MCP, The vocabulary (`sdlc:`), Shapes, The canonical export, Exports, Scenarios and the wire protocol, Decider and Projector logic | dpp, what, writ | aggregate, change set |
| 6 | The draft log | 0 | 10 | – | writ | – |
| 7 | Proposals and decisions | 2 | 11 | The draft log, MCP, Shapes, Decision records and the profile | dpp, writ | change set, head |
| 8 | The workbench | 2 | 6 | The draft log, Proposals and decisions, MCP, Shapes | what | head |
| 9 | Adopting on the fly | 3 | 0 | Proposals and decisions, The workbench, MCP, Shapes, Decision records and the profile | dpp | change set, head |
| 10 | MCP | 2 | 7 | Proposals and decisions, The workbench | writ | – |
| 11 | 4. The formats | 0 | 0 | – | – | – |
| 12 | The vocabulary (`sdlc:`) | 2 | 9 | The What-version record, Scenarios and the wire protocol | dpp, what | scope rule |
| 13 | Shapes | 2 | 11 | The vocabulary (`sdlc:`) | what, writ | change set |
| 14 | The canonical export | 1 | 5 | The draft log | what, writ | – |
| 15 | The What-version record | 2 | 4 | The draft log, Proposals and decisions, The vocabulary (`sdlc:`), The canonical export | dpp, what | – |
| 16 | Decision records and the profile | 1 | 5 | The draft log | dpp | – |
| 17 | Exports | 3 | 4 | The draft log, The vocabulary (`sdlc:`) | dpp, what, writ | – |
| 18 | Scenarios and the wire protocol | 0 | 8 | – | what, writ | – |
| 19 | Decider and Projector logic | 0 | 4 | – | what | – |
| 20 | 5. The guarantees | 4 | 0 | The draft log, Proposals and decisions, The vocabulary (`sdlc:`), Shapes, The canonical export, The What-version record, Decision records and the profile, Exports, Scenarios and the wire protocol, Decider and Projector logic | dpp, what, writ | aggregate, change set, head, scope rule, session transport |
| 21 | 6. The contracts between parts | 4 | 0 | Proposals and decisions, The workbench, MCP, The vocabulary (`sdlc:`), Shapes, Exports, Scenarios and the wire protocol, Decider and Projector logic | what, writ | – |
| 22 | 7. Implementation | 4 | 0 | The draft log, Proposals and decisions, The workbench, MCP, The vocabulary (`sdlc:`), Shapes, The canonical export, The What-version record, Exports, Scenarios and the wire protocol | dpp, what, writ | scope rule |
| 23 | 8. Boundaries and decisions taken | 3 | 0 | The draft log, Proposals and decisions, The vocabulary (`sdlc:`), Shapes, Decision records and the profile, Scenarios and the wire protocol | dpp, what, writ | – |
| 24 | Cross-repository dependencies | 3 | 0 | The vocabulary (`sdlc:`), Shapes, The What-version record | what, writ | – |

## Forward references

| Term | Used in | Explained later in |
|---|---|---|
| adoption | 1. The promise | Proposals and decisions |
| canonical document | 1. The promise | The canonical export |
| finding | 1. The promise | Shapes |
| profile | 1. The promise | Decision records and the profile |
| proposal | 1. The promise | Proposals and decisions |
| scenario | 1. The promise | Scenarios and the wire protocol |
| shape | 1. The promise | Shapes |
| wire protocol | 1. The promise | Scenarios and the wire protocol |
| adoption | 2. Who it is for | Proposals and decisions |
| finding | 2. Who it is for | Shapes |
| phase | 2. Who it is for | MCP |
| proposal | 2. Who it is for | Proposals and decisions |
| scenario | 2. Who it is for | Scenarios and the wire protocol |
| signature | 2. Who it is for | Decider and Projector logic |
| wire protocol | 2. Who it is for | Scenarios and the wire protocol |
| workbench | 2. Who it is for | The workbench |
| adoption | Commands | Proposals and decisions |
| canonical document | Commands | The canonical export |
| canonical graph | Commands | Exports |
| draft log | Commands | The draft log |
| draft position | Commands | The draft log |
| edition | Commands | The vocabulary (`sdlc:`) |
| exporter | Commands | Exports |
| finding | Commands | Shapes |
| phase | Commands | MCP |
| proposal | Commands | Proposals and decisions |
| scenario | Commands | Scenarios and the wire protocol |
| signature | Commands | Decider and Projector logic |
| violation | Commands | Shapes |
| warning | Commands | Shapes |
| wire protocol | Commands | Scenarios and the wire protocol |
| workbench | Commands | The workbench |
| phase | Proposals and decisions | MCP |
| profile | Proposals and decisions | Decision records and the profile |
| shape | Proposals and decisions | Shapes |
| finding | The workbench | Shapes |
| phase | The workbench | MCP |
| finding | Adopting on the fly | Shapes |
| phase | Adopting on the fly | MCP |
| profile | Adopting on the fly | Decision records and the profile |
| shape | Adopting on the fly | Shapes |
| What-version record | The vocabulary (`sdlc:`) | The What-version record |
| scenario | The vocabulary (`sdlc:`) | Scenarios and the wire protocol |

## Paths

A path is a term's home, then every section that uses the term, in reading order.

- **draft log**: home "The draft log" → Commands → Proposals and decisions → The workbench → The canonical export → The What-version record → Decision records and the profile → Exports → 5. The guarantees → 7. Implementation → 8. Boundaries and decisions taken
- **proposal**: home "Proposals and decisions" → 1. The promise → 2. Who it is for → Commands → The workbench → Adopting on the fly → MCP → The What-version record → 5. The guarantees → 6. The contracts between parts → 7. Implementation
- **What-version record**: home "The What-version record" → The vocabulary (`sdlc:`) → 5. The guarantees → 7. Implementation → Cross-repository dependencies
- **canonical document**: home "The canonical export" → 1. The promise → Commands → The What-version record → 5. The guarantees → 7. Implementation
- **scenario**: home "Scenarios and the wire protocol" → 1. The promise → 2. Who it is for → Commands → The vocabulary (`sdlc:`) → 5. The guarantees → 6. The contracts between parts → 7. Implementation → 8. Boundaries and decisions taken
