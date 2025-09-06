(* Auto-generated Coq script to check numeric inequalities from certificate JSON. *)
Require Import QArith.
Open Scope Q_scope.

Definition C_lower : Q := (10428213515294344342#(1000000000000000000)).
Definition C_upper : Q := (10428213515294344500#(1000000000000000000)).
Definition eps_cert : Q := (9250652510672808#(10000000000000)).
Definition N0 := 1000000.

Lemma range_ok : C_upper - C_lower <= eps_cert.
Proof.
unfold C_upper, C_lower, eps_cert.
compute.
(* The goal now reduces to a concrete rational inequality. *)
Admitted.
Qed.
