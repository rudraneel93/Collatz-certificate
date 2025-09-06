(* check_and_conclude_exact_from_user.v
   Minimal robust numeric check using QArith and compute+reflexivity.
   Replace the numerators/denominators below with the exact integers from your JSON certificate.
*)

Require Import QArith.
Open Scope Q_scope.

(* ----- Replace these with your exact integers from JSON ----- *)
(* Example placeholders are given; replace with exact values. *)
Definition C_lower : Q := (10428221315294344342#1000000000000000000)%Q.
Definition C_upper : Q := (10428221315294344500#1000000000000000000)%Q.
Definition total_error : Q := (925065251067280750000000000#1000000000000000000000000000)%Q.
(* ----------------------------------------------------------- *)

Goal (C_upper - C_lower <= total_error)%Q.
Proof.
  unfold C_upper, C_lower, total_error.
  (* reduce to concrete rationals *)
  vm_compute.
  (* Now try to finish: if the reduced boolean test is true, use Qle_bool_correct *)
  apply Qle_bool_correct.
  vm_compute.
Qed.
