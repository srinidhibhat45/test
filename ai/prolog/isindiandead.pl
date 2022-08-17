man(marcus).
man(john).
indian(marcus).
not(indian(john)).
die(X, Now):- indian(X), gt(Now, 79), write(X is dead).
gt(OP1, OP2):- OP1 > OP2.

