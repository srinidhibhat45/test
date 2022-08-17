repeat.
repeat:-
    repeat.
user2(bob, 123).

logon:- getdata(_,_), write('sucess').

logon:-
    repeat, write('login failed'),
    write('try again'),getdata(_,_),write('sucess').

getdata(U,P):-
    write('What is your username?'),nl,
    read(U),nl,
    write('What is your password?'),nl,
    read(P),nl,
    user(U,P).
