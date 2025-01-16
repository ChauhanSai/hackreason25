append_element(Elem, [], [Elem]).
append_element(Elem, [Head|Tail], [Head|Result]) :-
    append_element(Elem, Tail, Result).!