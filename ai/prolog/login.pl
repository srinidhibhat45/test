user(bob, 123456).

answer(yes).

check(X,Y):-
    user(X,Y), write('Login Sucessful');
    write('Login Failed'),nl,nl,
    write('Would you like to try again? yes/no'),nl,
    read(A),
    (   answer(A), logon).

logon:-
    write('What is your username?'),nl,
    read(Username),nl,
    write('What is your password?'),nl,
    read(Password),nl,
    check(Username, Password).


