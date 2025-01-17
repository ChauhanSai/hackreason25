:- use_module(library(scasp)).

% list queries
% check if an element is in a list
is_member(Element, [Element | _]).
is_member(Element, [_ | Tail]) :-
    is_member(Element, Tail).

% remove an element from a list
remove_element(_, [], []).
remove_element(Elem, [Elem|Tail], Result) :-
    remove_element(Elem, Tail, Result).
remove_element(Elem, [Head|Tail], [Head|Result]) :-
    Elem \= Head,
    remove_element(Elem, Tail, Result).

% append an element to the front of a list
append_element(Elem, List, [Elem|List]).

% reverse lists elements
reverse_list([], []).
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    reverse_element(ReversedTail, [Head], Reversed).

reverse_element([], List, List).
reverse_element([Head|Tail], List, [Head|Result]) :-
    reverse_element(Tail, List, Result).

% get element length of list
get_length([], 0). 
get_length([_| Tail], Length) :-
    get_length(Tail, TailLength),
    Length is TailLength + 1.

get_head([ HEAD | _], HEAD).

% Collect all cities from city/1 facts
all_cities(Cities) :-
    findall(City, city(City), Cities).

% city data
city(prague).
city(frankfurt).
city(rome).
city(vienna).

% route(start, finish, price, day)
route(prague, frankfurt, 300, 1).
route(prague, frankfurt, 250, 5).
route(prague, frankfurt, 400, 9).
route(prague, frankfurt, 320, 3).
route(prague, frankfurt, 350, 7).
route(frankfurt, prague, 320, 2).
route(frankfurt, prague, 270, 6).
route(frankfurt, prague, 300, 8).
route(frankfurt, prague, 290, 10).
route(frankfurt, prague, 310, 12).
route(prague, rome, 450, 3).
route(prague, rome, 500, 7).
route(prague, rome, 480, 2).
route(prague, rome, 430, 6).
route(prague, rome, 460, 11).
route(rome, prague, 430, 4).
route(rome, prague, 480, 8).
route(rome, prague, 410, 1).
route(rome, prague, 450, 5).
route(rome, prague, 420, 10).
route(prague, vienna, 200, 2).
route(prague, vienna, 220, 6).
route(prague, vienna, 180, 11).
route(prague, vienna, 190, 3).
route(prague, vienna, 210, 8).
route(vienna, prague, 210, 3).
route(vienna, prague, 230, 10).
route(vienna, prague, 220, 4).
route(vienna, prague, 200, 7).
route(vienna, prague, 240, 12).
route(frankfurt, rome, 350, 4).
route(frankfurt, rome, 400, 8).
route(frankfurt, rome, 375, 12).
route(frankfurt, rome, 390, 6).
route(frankfurt, rome, 360, 9).
route(rome, frankfurt, 360, 5).
route(rome, frankfurt, 390, 9).
route(rome, frankfurt, 340, 1).
route(rome, frankfurt, 370, 7).
route(rome, frankfurt, 380, 11).
route(frankfurt, vienna, 280, 3).
route(frankfurt, vienna, 260, 7).
route(frankfurt, vienna, 300, 12).
route(frankfurt, vienna, 290, 2).
route(frankfurt, vienna, 310, 10).
route(vienna, frankfurt, 290, 2).
route(vienna, frankfurt, 270, 10).
route(vienna, frankfurt, 300, 5).
route(vienna, frankfurt, 280, 9).
route(vienna, frankfurt, 320, 6).
route(rome, vienna, 250, 1).
route(rome, vienna, 275, 5).
route(rome, vienna, 290, 9).
route(rome, vienna, 260, 3).
route(rome, vienna, 300, 12).
route(vienna, rome, 260, 6).
route(vienna, rome, 300, 8).
route(vienna, rome, 280, 12).
route(vienna, rome, 270, 4).
route(vienna, rome, 310, 7).

% Additional routes between cities
route(prague, frankfurt, 340, 13).
route(prague, frankfurt, 310, 17).
route(prague, frankfurt, 330, 19).
route(prague, frankfurt, 290, 21).
route(prague, frankfurt, 360, 25).
route(frankfurt, prague, 320, 14).
route(frankfurt, prague, 280, 16).
route(frankfurt, prague, 300, 22).
route(frankfurt, prague, 270, 27).
route(frankfurt, prague, 350, 30).
route(prague, rome, 450, 13).
route(prague, rome, 460, 15).
route(prague, rome, 420, 18).
route(prague, rome, 480, 23).
route(prague, rome, 490, 26).
route(rome, prague, 440, 14).
route(rome, prague, 430, 20).
route(rome, prague, 450, 24).
route(rome, prague, 470, 28).
route(rome, prague, 410, 29).
route(prague, vienna, 190, 13).
route(prague, vienna, 200, 17).
route(prague, vienna, 220, 19).
route(prague, vienna, 210, 23).
route(prague, vienna, 230, 26).
route(vienna, prague, 240, 14).
route(vienna, prague, 200, 18).
route(vienna, prague, 210, 22).
route(vienna, prague, 230, 28).
route(vienna, prague, 220, 30).
route(frankfurt, rome, 380, 13).
route(frankfurt, rome, 360, 17).
route(frankfurt, rome, 400, 20).
route(frankfurt, rome, 390, 24).
route(frankfurt, rome, 370, 28).
route(rome, frankfurt, 350, 14).
route(rome, frankfurt, 340, 16).
route(rome, frankfurt, 370, 21).
route(rome, frankfurt, 360, 26).
route(rome, frankfurt, 390, 30).
route(frankfurt, vienna, 300, 13).
route(frankfurt, vienna, 310, 16).
route(frankfurt, vienna, 280, 20).
route(frankfurt, vienna, 290, 23).
route(frankfurt, vienna, 320, 28).
route(vienna, frankfurt, 270, 14).
route(vienna, frankfurt, 290, 18).
route(vienna, frankfurt, 300, 21).
route(vienna, frankfurt, 310, 24).
route(vienna, frankfurt, 330, 27).
route(rome, vienna, 280, 13).
route(rome, vienna, 270, 17).
route(rome, vienna, 300, 21).
route(rome, vienna, 290, 25).
route(rome, vienna, 310, 29).
route(vienna, rome, 270, 14).
route(vienna, rome, 260, 19).
route(vienna, rome, 300, 23).
route(vienna, rome, 280, 27).
route(vienna, rome, 320, 30).

% hotel(city, price) the price is constant for all days
hotel(prague, 120).
hotel(frankfurt, 180).
hotel(rome, 80).
hotel(vienna, 90).

% get total hotel cost for stay based on flight days
hotel_cost(CITY, CURRENTDAY, [PREVDAY | _], X) :-
    hotel(CITY, PRICE),
    % access first and next element as CURRENTDAY and PREVDAY
    DAYS is CURRENTDAY - PREVDAY,
    X is DAYS * PRICE.

% logic will find all possible trips to visit every city

% base case
oneWayTrip(END, END, BUDGET, HOLIDAYS, CURRENTTOTAL, VISITED, FLIGHTDAYS, TOTALCOST, PLACESVISITED, FINALFLIGHTDAYS) :-
    hotel_cost(END, HOLIDAYS, FLIGHTDAYS, COST),
    NEWTOTAL is CURRENTTOTAL + COST,
    TOTALCOST = NEWTOTAL,
    reverse_list(VISITED, PLACESVISITED),
    % PLACESVISITED = VISITED,
    reverse_list(FLIGHTDAYS, FINALFLIGHTDAYS).
    % FINALFLIGHTDAYS = FLIGHTDAYS.
    

% recursive call
oneWayTrip(CURRENT, END, BUDGET, HOLIDAYS, CURRENTTOTAL, VISITED, FLIGHTDAYS, TOTALCOST, PLACESVISITED, FINALFLIGHTDAYS) :-
    % make sure that these are valid cities
    city(CURRENT), % debug
    city(END), % debug

    % find next possible flight to next possible destination
    route(CURRENT, NEXT, PRICE, DAY),
    get_head(FLIGHTDAYS, CURDAY),
    DAY .>. CURDAY,

    % find a possible next destination
    not is_member(NEXT, VISITED),

    % check to make sure its in budget & in time range
    hotel_cost(CURRENT, DAY, FLIGHTDAYS, HOTELCOST),
    (CURRENTTOTAL + PRICE + HOTELCOST) .<. BUDGET,
    DAY.<.HOLIDAYS,
    NEWTOTAL is CURRENTTOTAL + PRICE + HOTELCOST,

    % add the projected city to the visited list
    append_element(NEXT, VISITED, NEWVISITED),

    % add the flight days to list
    append_element(DAY, FLIGHTDAYS, NEWFLIGHTDAYS),

    oneWayTrip(NEXT, END, BUDGET, HOLIDAYS, NEWTOTAL, NEWVISITED, NEWFLIGHTDAYS, TOTALCOST, PLACESVISITED, FINALFLIGHTDAYS).


trip(START,END,BUDGET,HOLIDAYS, TOTALCOST, PLACESVISITED, FINALFLIGHTDAYS) :-
    oneWayTrip(START,END,BUDGET,HOLIDAYS, 0, [START], [1], TOTALCOST, PLACESVISITED, FINALFLIGHTDAYS).

% test run
?- trip(prague, vienna, 200000, 16, X, Y, Z). 