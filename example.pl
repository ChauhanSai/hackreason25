father(tony, abe).
father(tony, sarah).
father(abe, john).
father(bill, susan).
father(john, jill).
father(rob, jack).
father(rob, phil).
father(jack, jim).
 
mother(lisa, abe).
mother(lisa, sarah).
mother(nancy, john).
mother(sarah, susan).
mother(mary, jill).
mother(susan, jack).
mother(susan, phil).
 
parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
gp(X,Y) :- parent(X,Z), parent(Z,Y).
ggp(X,Y) :- parent(X,Z), gp(Z,Y).
gggp(X,Y) :- parent(X,Z), ggp(Z,Y).
 
 
 
 
 
 
 
 
 
 
 
% Gender information.
 
male(tony).
male(abe).
male(bill).
male(john).
male(rob).
male(jack).
male(phil).
male(rick).
male(jim).
 
female(lisa).
female(nancy).
female(sarah).
female(mary).
female(susan).
female(jill).
female(ann).
female(kim).
female(martha).