% Author: Joel Verhagen, edits by Ivan Uemlianin

% Define the set of digits.
digit(1..9).

% A cell is a pair of two digits.
cell(X, Y) :- digit(X), digit(Y).

% Each cell has exactly one digit.
1 { cellHasDigit(X, Y, D) : digit(D) } 1 :- cell(X, Y).

% Digit D in row X is in cube S.
rowCubeDigit(X, S, D) :-
    S = (((Y - 1) / 3) + (3 * ((X - 1) / 3))),
    cellHasDigit(X, Y, D).

% Digit D in column Y is in cube S.
colCubeDigit(Y, S, D) :-
    S = (((Y - 1) / 3) + (3 * ((X - 1) / 3))),
    cellHasDigit(X, Y, D).

% Same digits may not share row or column.
:- cellHasDigit(X, Y1, D), cellHasDigit(X, Y2, D), Y1 != Y2.
:- cellHasDigit(X1, Y, D), cellHasDigit(X2, Y, D), X1 != X2.

% Don't allow a digit in the same cube but different row.
:- rowCubeDigit(X1, S, D), rowCubeDigit(X2, S, D), X1 != X2.

% Don't allow a digit in the same cube but different column.
:- colCubeDigit(Y1, S, D), colCubeDigit(Y2, S, D), Y1 != Y2.

#show cellHasDigit/3.
