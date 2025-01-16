:- use_module(library(scasp)).

p(A) :- not w(A).
q(A) :- not p(A).
