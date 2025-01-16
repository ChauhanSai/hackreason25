:- use_module(library(scasp)).

p(A) :- not q(A).
q(A) :- not p(A).
?- p(A).