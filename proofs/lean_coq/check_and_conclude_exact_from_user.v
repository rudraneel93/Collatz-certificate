(* Auto-generated Coq numeric check file using exact rationals from the certificate *)
Require Import QArith.
Require Import ZArith.
Open Scope Q_scope.

Definition C_lower : Q :=
(104282135152943447398709068916357118830370026054048335067558#10000000000000000000000000000000000000000000000000000000000).

Definition C_upper : Q :=
(104282135152943447398709068916357118830370026054048335324573#10000000000000000000000000000000000000000000000000000000000).

Definition total_error : Q :=
(9250652510672807693481445312500000000000000000000001285075#100000000000000000000000000000000000000000000000000000000000).

Definition union_bad : Q :=
(9250640869140625#100000000000000000).

Definition tail_mass : Q :=
(116415321826934814453125#1000000000000000000000000000).

Definition N0 : nat := 1000000.

(* Use Qle_alt to reduce rational inequality to integer inequality on Qnum/Qden,
   then evaluate that integer inequality with vm_compute. This avoids boolean helpers
   that may not be present on some Coq installs. *)
Goal (C_upper - C_lower <= total_error)%Q.
Proof.
  unfold C_upper, C_lower, total_error.
  (* Qle_alt reduces x <= y to: Qnum x * Zpos (Qden y) <= Qnum y * Zpos (Qden x) *)
  apply Qle_alt.
  vm_compute. (* reduces the Z-inequality to concrete integers *)
  reflexivity.
Qed.
