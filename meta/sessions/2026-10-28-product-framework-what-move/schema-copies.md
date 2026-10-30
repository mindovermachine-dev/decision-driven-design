# The two schema copies in product-cli — the diff, recorded, not reconciled

Round 1, Q-2: "take the ontology and shapes from product-cli's `schema/`, the copy the Rust
round-trip tests read. Record the diff between the two copies in the session record; reconcile
nothing from the other."

product-cli at `70395df`. `schema/` is the copy product-core's checks name (`rules_what.rs`,
`validate.rs`, `turtle.rs`, `mod.rs` cite `schema/shapes/shapes.shacl.ttl`). `spec/schema/` is the
other copy. Its last change is `f4a33d9b` (FT-109). `schema/ontology/` was last changed by `c1f77364`
(conform to Product Framework v1.7.0). Nothing from `spec/schema/` is carried into
`applications/sdlc/what/`. `how.shacl.ttl` is not carried either (Round 1, Q-3).

| File | `spec/schema/` | `schema/` | Changed lines |
|---|---|---|---|
| `ontology/product-framework.ttl` | 307 lines | 399 lines | 104 |
| `shapes/shapes.shacl.ttl` | | 167 lines | 72 |

In summary, `schema/` adds the §3.2.1 UI layer (AIO, context of use, application root, WCAG
criterion, attestation, content store, design system, CIO, token, reification rule, the typed
interaction edges) and renames archetype to blueprint. In the shapes, `spec/schema/` carries the
How shapes inline (top decision, principle, pattern, infrastructure and interface contracts).
`schema/` moves them out to `how.shacl.ttl` and adds the attribute, wireframe-step, surface and offer
shapes. `spec/schema/` is the vocabulary from before the v1.7.0 rename.

## Ontology: `diff -u spec/schema/ontology/product-framework.ttl schema/ontology/product-framework.ttl`

```diff
@@ -35,11 +35,11 @@
 pf:Product a owl:Class ;
   rdfs:subClassOf pf:Artifact ;
   rdfs:label "Product" ;
-  rdfs:comment "The top: a composition of archetype instances sharing one domain model (framework §Composition / Product layer)." .
+  rdfs:comment "The top: a composition of blueprint instances sharing one domain model (framework §Composition / Product layer)." .
 
-pf:Archetype a owl:Class ;
+pf:Blueprint a owl:Class ;
   rdfs:subClassOf pf:Artifact ;
-  rdfs:label "Archetype" ;
+  rdfs:label "Blueprint" ;
   rdfs:comment "A reusable, pre-filled How for a recurring system shape. A product realises one or more." .
 
 #################################################################
@@ -105,6 +105,56 @@
   rdfs:label "Flow" ;
   rdfs:comment "An ordered behaviour: a timeline of wireframe → command → event(s) → read model." .
 
+pf:Aio a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Abstract Interaction Object" ;
+  rdfs:comment "§3.2.2 — a context-independent kind of interaction a UI step is typed against; never a concrete control." .
+
+pf:ContextOfUse a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Context of Use" ;
+  rdfs:comment "§3.2.2 — a declared form factor / modality a reification rule is written against; carries no realisation." .
+
+pf:ApplicationRoot a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Application Root" ;
+  rdfs:comment "§3.2.4 — the distinguished node of the page graph; its navigatesFromRoot out-edges are the global destinations." .
+
+pf:WcagCriterion a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "WCAG Criterion" ;
+  rdfs:comment "§3.2.3 — an ingested WCAG 2.2 success criterion (level + machine/assisted/manual verification) a UI step or AIO must satisfy." .
+
+pf:Attestation a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Attestation" ;
+  rdfs:comment "§3.2.3 — a dated, attributed record that a non-machine criterion was evaluated and met for a step." .
+
+pf:ContentStore a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Content Store" ;
+  rdfs:comment "§4.6 — the swappable provider of words; resolves (content key, locale) → string for a UI step's content references." .
+
+pf:DesignSystem a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Design System" ;
+  rdfs:comment "§4.5 — the closed CIO catalog + token surface a screen composes from." .
+
+pf:Cio a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Concrete Interaction Object" ;
+  rdfs:comment "§4.5 — an on-system design-system component an AIO reifies into." .
+
+pf:Token a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Design Token" ;
+  rdfs:comment "§4.5 — a design token (colour, spacing, typography); styling references tokens, never literals." .
+
+pf:ReificationRule a owl:Class ;
+  rdfs:subClassOf pf:Artifact ;
+  rdfs:label "Reification Rule" ;
+  rdfs:comment "§4.5 — a reify(AIO, context) → CIO rule carrying its UX rationale." .
+
 #################################################################
 #  HOW — §4.1 the Why (decisions, principles, patterns)
 #################################################################
@@ -191,7 +241,7 @@
 pf:seam                   a pf:VerificationKind ; rdfs:label "seam" .
 pf:domainConformance      a pf:VerificationKind ; rdfs:label "domain-conformance" .
 pf:behaviouralConformance a pf:VerificationKind ; rdfs:label "behavioural-conformance" .
-pf:crossArchetype         a pf:VerificationKind ; rdfs:label "cross-archetype" .
+pf:crossBlueprint         a pf:VerificationKind ; rdfs:label "cross-blueprint" .
 
 pf:Verdict a owl:Class ;
   rdfs:label "Verdict" ;
@@ -282,14 +332,52 @@
 pf:realisedBy a owl:ObjectProperty ;
   rdfs:label "realised_by" ;
   rdfs:domain pf:BoundedContext ;
-  rdfs:range pf:Archetype ;
-  rdfs:comment "Which archetype instance realises this context (composition)." .
+  rdfs:range pf:Blueprint ;
+  rdfs:comment "Which blueprint instance realises this context (composition)." .
 
 pf:contains a owl:ObjectProperty ;
   rdfs:label "contains" ;
   rdfs:comment "Membership: a feature/release contains these graph nodes; a context contains entities." .
 
 #################################################################
+#  WHAT — §3.2.1 UI interaction (typed edges)
+#
+#  A UI step's interactions are blank nodes that pair a target
+#  (a projection or a command) with the AIO it is typed_as. The
+#  blank node keeps the (target, AIO) pairing unambiguous.
+#################################################################
+
+pf:hasAttribute a owl:ObjectProperty ;
+  rdfs:label "has_attribute" ;
+  rdfs:domain pf:Entity ;
+  rdfs:comment "An entity's named attribute, carried as a blank node ([ attr_name ; attr_type ])." .
+
+pf:surfaces a owl:ObjectProperty ;
+  rdfs:label "surfaces" ;
+  rdfs:domain pf:WireframeStep ;
+  rdfs:comment "A (projection, display-AIO) the step surfaces, as a blank node carrying typed_as." .
+
+pf:offers a owl:ObjectProperty ;
+  rdfs:label "offers" ;
+  rdfs:domain pf:WireframeStep ;
+  rdfs:comment "A (command, action-AIO) the step offers, as a blank node carrying typed_as." .
+
+pf:projection a owl:ObjectProperty ;
+  rdfs:label "projection" ;
+  rdfs:range pf:ReadModel ;
+  rdfs:comment "The read model a surface interaction shows (on a pf:surfaces blank node)." .
+
+pf:command a owl:ObjectProperty ;
+  rdfs:label "command" ;
+  rdfs:range pf:Command ;
+  rdfs:comment "The command an offer interaction issues (on a pf:offers blank node)." .
+
+pf:typedAs a owl:ObjectProperty ;
+  rdfs:label "typed_as" ;
+  rdfs:range pf:Aio ;
+  rdfs:comment "§3.2.1 A UI step's interaction is typed against an Abstract Interaction Object (an AIO), never a concrete control (a CIO)." .
+
+#################################################################
 #  COMMON DATATYPE PROPERTIES
 #################################################################
 
@@ -305,3 +393,7 @@
 pf:verificationKind a owl:ObjectProperty ; rdfs:label "verification_kind" ; rdfs:range pf:VerificationKind .
 pf:conformanceLevel a owl:DatatypeProperty ; rdfs:label "conformance_level" ;
   rdfs:comment "Described | Realised | Verified | Delivered." ; rdfs:range rdfs:Literal .
+pf:attrName a owl:DatatypeProperty ; rdfs:label "attr_name" ;
+  rdfs:comment "The name of an entity attribute (on a pf:hasAttribute blank node)." ; rdfs:range rdfs:Literal .
+pf:attrType a owl:DatatypeProperty ; rdfs:label "attr_type" ;
+  rdfs:comment "The optional declared type of an entity attribute." ; rdfs:range rdfs:Literal .
```

## Shapes: `diff -u spec/schema/shapes/shapes.shacl.ttl schema/shapes/shapes.shacl.ttl`

```diff
@@ -25,7 +25,16 @@
   sh:property [
     sh:path pf:inContext ; sh:minCount 1 ; sh:class pf:BoundedContext ;
     sh:message "§3.1 An entity must belong to exactly one bounded context (never a flat model)." ;
-    sh:maxCount 1 ] .
+    sh:maxCount 1 ] ;
+  sh:property [
+    sh:path pf:hasAttribute ; sh:node pf:AttributeShape ;
+    sh:message "§3.1 An entity attribute (when present) must name a field (attr_name); attr_type is optional." ] .
+
+# An attribute is a blank node [ pf:attrName "…" ; pf:attrType "…"? ].
+pf:AttributeShape a sh:NodeShape ;
+  sh:property [
+    sh:path pf:attrName ; sh:minCount 1 ;
+    sh:message "§3.1 An entity attribute must name a field." ] .
 
 pf:RelationShape a sh:NodeShape ;
   sh:targetClass pf:Relation ;
@@ -83,48 +92,43 @@
     sh:path pf:projects ; sh:minCount 1 ;
     sh:message "§3.2 A read model must project at least one entity/event (read-model provenance: no ghost views)." ] .
 
-#########################  HOW — §4.1  ##########################
+####################  WHAT — §3.2.1 UI layer  ###################
+#  A UI step's interactions are blank nodes pairing a target with
+#  the AIO it is typed_as: pf:surfaces [ pf:projection … ;
+#  pf:typedAs … ] and pf:offers [ pf:command … ; pf:typedAs … ].
+#  The §3.2.1 rule: every interaction is typed against an AIO,
+#  never a concrete control (a CIO).
 
-pf:TopDecisionShape a sh:NodeShape ;
-  sh:targetClass pf:TopDecision ;
+pf:WireframeStepShape a sh:NodeShape ;
+  sh:targetClass pf:WireframeStep ;
   sh:property [
-    sh:path pf:rationale ; sh:minCount 1 ;
-    sh:message "§4.1 A top decision must carry rationale (what it buys, when it applies)." ] ;
+    sh:path pf:surfaces ; sh:node pf:SurfaceShape ;
+    sh:message "§3.2.1 A surfaced projection must be typed against an AIO." ] ;
   sh:property [
-    sh:path pf:licenses ; sh:minCount 0 ; sh:class pf:Principle ;
-    sh:message "§4.1 A top decision licenses zero or more principles." ] .
+    sh:path pf:offers ; sh:node pf:OfferShape ;
+    sh:message "§3.2.1 An offered command must be typed against an AIO." ] .
 
-pf:PrincipleShape a sh:NodeShape ;
-  sh:targetClass pf:Principle ;
+pf:SurfaceShape a sh:NodeShape ;
   sh:property [
-    sh:path pf:statement ; sh:minCount 1 ;
-    sh:message "§4.1 A principle must be stated checkably (a vague principle cannot back a verification)." ] ;
-  # Earn-their-place: a principle must be applied by a work unit OR enforced by a verification.
-  sh:or (
-    [ sh:property [ sh:path [ sh:inversePath pf:applies ] ; sh:minCount 1 ] ]
-    [ sh:property [ sh:path [ sh:inversePath pf:enforces ] ; sh:minCount 1 ] ]
-  ) ;
-  sh:message "§4.1 Earn-their-place: a principle must be applied by a work unit or enforced by a verification, else it is documentation, not architecture." .
-
-pf:PatternShape a sh:NodeShape ;
-  sh:targetClass pf:Pattern ;
+    sh:path pf:projection ; sh:minCount 1 ; sh:class pf:ReadModel ;
+    sh:message "§3.2.1 A surface interaction must show a real projection (read model)." ] ;
   sh:property [
-    sh:path pf:realizes ; sh:minCount 1 ; sh:class pf:Principle ;
-    sh:message "§4.1 A pattern must realise at least one principle." ] .
-
-#########################  HOW — §4.2 / 4.4  ####################
+    sh:path pf:typedAs ; sh:minCount 1 ; sh:class pf:Aio ;
+    sh:message "§3.2.1 A UI step's interactions must be typed against an Abstract Interaction Object (an AIO), never a concrete control (a CIO)." ] .
 
-pf:InfrastructureContractShape a sh:NodeShape ;
-  sh:targetClass pf:InfrastructureContract ;
+pf:OfferShape a sh:NodeShape ;
   sh:property [
-    sh:path pf:conformsTo ; sh:minCount 1 ; sh:class pf:ApplicationContract ;
-    sh:message "§4.2 An infrastructure contract must satisfy (conform to) the application contract." ] .
-
-pf:InterfaceContractShape a sh:NodeShape ;
-  sh:targetClass pf:InterfaceContract ;
+    sh:path pf:command ; sh:minCount 1 ; sh:class pf:Command ;
+    sh:message "§3.2.1 An offer interaction must issue a real command." ] ;
   sh:property [
-    sh:path pf:derivedFrom ; sh:minCount 1 ;
-    sh:message "§4.4 An interface contract must be generated from (derived_from) the domain/event model, not hand-written." ] .
+    sh:path pf:typedAs ; sh:minCount 1 ; sh:class pf:Aio ;
+    sh:message "§3.2.1 A UI step's interactions must be typed against an Abstract Interaction Object (an AIO), never a concrete control (a CIO)." ] .
+
+#########################  HOW — §4  ############################
+#  The How conformance shapes (decisions, principles, patterns,
+#  the two contracts, layout, interface, and the trace-truth
+#  rule) live in their own file: how.shacl.ttl. Loaded alongside
+#  this one by validate.py.
 
 #########################  WORK UNITS — §5  #####################
 
```
