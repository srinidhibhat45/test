room(balcony).
room(hall).
room(kitchen).
room(bedroom1).
room(bedroom2).
room(bathroom).

door(bedroom1, hall).
door(bedroom2, hall).
door(kitchen, hall).
door(bathroom, hall).
door(balcony, hall).
door(bedroom1, bedroom2).

item(bed).
item(sofa).
item(shoerack).
item(basin).

contains(bed, bedroom1).
contains(bed, bedroom2).
contains(sofa, hall).
contains(shoerack, balcony).
contains(basin, bathroom).


position(R1):-  contains(X, R1) ,(door(R1, Y) | door(Y, R1)), write('You can move from '),write(R1), write(' to '), write(Y).

code:-
    write('What is your current location? '),nl,
    read(Current_room),nl,
    position(Current_room).

