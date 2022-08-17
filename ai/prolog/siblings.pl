male(adam).
male(john).
male(joe).
female(alice).
female(jan).
female(jenny).
mother(alice, jan).
mother(alice, jenny).
mother(alice, john).
mother(alice, joe).
father(adam, jan).
father(adam, jenny).
father(adam, john).
father(adam, joe).
siblings(Sb1, Sb2):- (father(F, Sb1), father(F, Sb2), male(F), Sb1\==Sb2) | (mother(M, Sb1), mother(M, Sb2), female(M), Sb1\==Sb2).
brothers(B1, B2):- male(B1), male(B2), siblings(B1, B2).
sisters(F1, F2):-female(F1), female(F2), siblings(F1, F2).
