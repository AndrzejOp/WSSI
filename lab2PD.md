zad 1
A
x i y mają dwóch wspólnych rodziców (są rodzeństwem).

rodzic(x,a).
rodzic(y,a).
rodzic(y,b).
rodzic(x,b).

jest_rodzicem(X, Y) :- rodzic(X, Y).
jest_rodzenstwem(X, Y) :- rodzic(X,A), rodzic(Y,A).

B
x i y mają wspólnego rodzica rodziców (to czyni ich kuzynami).

rodzic(c,a).
rodzic(b,a).
rodzic(x,b).
rodzic(y,c).
rodzenstwo(b,c).
kuzyni(x,y).

jest_kuzynem(X, Y) :-
    rodzic(X, A),
    rodzic(Y, B),
    rodzenstwo(A, B),
    X \= Y.

C
x i y są rodzicami rodziców, którzy mają wspólnego potomka (są dziadkami jednego wnuka).

rodzic(a,x).
rodzic(b,y).
rodzic(c,b).
rodzic(c,a).

sa_dziadkami(X,Y) :- 
    rodzic(A, X),
    rodzic(B, Y),
    rodzic(C, A),
    rodzic(C, B).

D
x i y w tym wypadku są na róznych poziomach hierarchii w taki sposób, że rodzic x jest, jest wpółrodzicem innego elementu (y jest przybranym rodzicem x).

rodzic(b,y).
rodzic(b,a).
rodzic(x,a).

jest_przybranym_rodzicem(X,Y) :- 
    rodzic(B, Y),
    rodzic(B, A),
    rodzic(X, A).
                          
E
x i y mają jednego wspólnego rodzica, ale także po jednym różnym rodzicu (są przybranym rodzeństwem).

rodzic(x,a).
rodzic(x,b).
rodzic(y,b).
rodzic(y,c).

jest_przybranym_rodzenstwem(X,Y) :- 
    rodzic(Y, B),
    rodzic(X, B),
    rodzic(X, A),
    rodzic(Y, C).

F
x i y na jednym poziomie i x jest współrodzicem z potomkiem rodzica y (y jest szwagrem/szwgaierką y).

rodzic(b,a).
rodzic(c,b).
rodzic(c,x).
rodzic(y,a).

jest_wspolrodzicem_potomstwa_rodzenstwa(X,Y) :- 
    rodzic(Y, A),
    rodzic(B, A),
    rodzic(C, B),
    rodzic(C, X).

G
x i y mają jednego wspólnego rodzica, ale y jest również potomkiem rodzeństwa x ( x jest równocześnie rodzeństwem y jak i potomstwem rodzeństwa).S

rodzic(x,a).
rodzic(x,b).
rodzic(c,a).
rodzic(y,b).
rodzic(y,c).

jest_rodzenstwem_i_potomstwem_rodzenstwa(X,Y) :- 
    rodzic(Y, A),
	rodzic(X, A),
    rodzic(X, B),
    rodzic(C, B),
    rodzic(Y, C).


zad 2


mezczyzna(X):- 
    mezczyzna(X).
rodzic(X,Y):- 
    rodzic(X,Y).
osoba(X):- 
    osoba(X).
kobieta(X):- 
    \+ mezczyzna(X),
    osoba(X).
ojciec(X,Y):-
    rodzic(X,Y),
    mezczyzna(X).
matka(X,Y):- 
    kobieta(X),
    rodzic(X,Y).
corka(X,Y):-
    kobieta(X),
    rodzic(Y,X).
brat_rodzony(X,Y):-
    mezczyzna(X),
    rodzic(A,X),
    rodzic(A,Y),
	X \= Y.    
brat_przyrodni(X,Y):-
    mezczyzna(X),
    rodzic(A,X),
    rodzic(A,Y),
    rodzic(B,Y),
    rodzic(C,X),
	X =\ Y,
	A =\ B,
	A =\ C.
kuzyn(X,Y):- 
    rodzic(A,X),
    rodzic(B,Y),
    brat_rodzony(A,B).

dziadek_od_strony_ojca(X,Y):- 
    ojciec(X,A),
    ojciec(A,Y).
dziadek_od_strony_matki(X,Y):-
    ojciec(X,A),
    matka(A,Y).
dziadek(X,Y):-
    ojciec(X,A),
    rodzic(A,Y).
babcia(X,Y):-
    matka(X,A),
    rodzic(A,Y).
wnuczka(X,Y):-
    kobieta(Y),
    dziadek(X,Y);
    babcia(X,Y).
przodek_do2pokolenia_wstecz(X,Y):-
    babcia(X,Y);
    dziadek(X,Y);
    rodzic(X,Y).
przodek_do3pokolenia_wstecz(X,Y):-
    rodzic(X, A),
    przodek_do2pokolenia_wstecz(A,Y).
    
    
    
    
    
