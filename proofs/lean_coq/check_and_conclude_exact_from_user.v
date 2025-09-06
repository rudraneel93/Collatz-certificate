From Stdlib Require Import QArith ZArith Lia.
From Stdlib Require Import Qabs.
Open Scope Q_scope.

Definition C_lower : Q := (52141067576471723699354534458178559415185013027024167533779#(5000000000000000000000000000000000000000000000000000000000)).
Definition C_upper : Q := (104282135152943447398709068916357118830370026054048335324573#(10000000000000000000000000000000000000000000000000000000000)).
Definition C_center : Q := (52141067576471723699354534458178559415185013027024167598033#(5000000000000000000000000000000000000000000000000000000000)).
Definition C_half : Q := (51403#(4000000000000000000000000000000000000000000000000000000000)).
Definition union_bad : Q := (97#(1048576)).
Definition tail_mass : Q := (1#(8589934592)).
Definition total_error : Q := (370026100426912307739257812500000000000000000000051403#(4000000000000000000000000000000000000000000000000000000000)).
Definition E_low_a : Q := (300000127156575491227414244427394158213183589766028405755043#(100000000000000000000000000000000000000000000000000000000000)).
Definition E_high_a : Q := (300000127156575491227414244427394120457#(100000000000000000000000000000000000000)).
Definition E_low_b : Q := (287681228157235084767676821784943595901222280627836427268701#(1000000000000000000000000000000000000000000000000000000000000)).
Definition E_high_b : Q := (57536245631447016953535364356988719180244456125567285525463#(200000000000000000000000000000000000000000000000000000000000)).
Definition N0 : nat := 1000000%nat.

Goal (C_upper - C_lower <= total_error)%Q.
Proof.
  unfold C_upper, C_lower, total_error.
  unfold Qle; simpl.
  (* Turn the Z comparison into a boolean and compute it fast to avoid heavy proof search *)
  apply Z.leb_le.
  vm_compute; reflexivity.
Qed.

Section Certificate.
  Variable C_N : nat -> Q.
  Variable C_mean : Q.
  (* Using the constants union_bad, tail_mass, C_half defined above *)
  Hypothesis reduction_correct : forall N : nat, (N >= N0)%nat -> Qabs (C_N N - C_mean) <= (union_bad + tail_mass + C_half)%Q.
  Hypothesis interval_bounds : (C_lower <= C_mean)%Q /\ (C_mean <= C_upper)%Q.
  Hypothesis sum_error_ok : (union_bad + tail_mass + C_half <= total_error)%Q.

  Theorem final_certificate : forall N : nat, (N >= N0)%nat -> Qabs (C_N N - C_mean) <= total_error.
  Proof.
    intros N HN.
    eapply Qle_trans.
    - apply reduction_correct; assumption.
    - apply sum_error_ok.
  Qed.
End Certificate.
