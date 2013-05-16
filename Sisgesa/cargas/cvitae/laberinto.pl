% Autor:
% Fecha: 28/04/2012

% laberintos de ejemplo
% sintaxis:
% laberinto( Num, Lab )
% Num--> n�mero de laberinto
% Lab --> matriz bidimensional de caracteres que representa al laberinto
%%
entrada(Num,X,Y)
% Num--> n�mero de laberinto
% X --> coordenada x de la entrada al laberinto Num
% Y --> coordenada y de la entrada al laberinto Num
salida(Num,X,Y)
% Num--> n�mero de laberinto
% X --> coordenada x de la salida del laberinto Num
% Y --> coordenada y de la salida del laberinto Num
% Nota:
% un espacio en blanco (caracter 32) representa pasillo
% un car�cter distinto del blanco representa pared
laberinto(1,[
"####### ######",
"##### ######",
"##### ## ###",
"##### # ###",
"# ###### ###",
"# # ###",
"# ############"
]).
entrada(1,7,0).
salida(1,1,6).
% Operadores de b�squeda
% sintaxis:
% mover( Mov, X1, Y1, X2, Y2 )
% Mov = {arr|aba|izq|der} --> nombre del movimiento
% X1 --> coordenada X actual
% Y1 --> coordenada Y actual
% X2 --> coordenada X de la posici�n a la que se llega con el movimiento seleccionado
% Y2 --> coordenada Y de la posici�n a la que se llega con el movimiento seleccionado
% Nota:
% X1,Y1 = estado actual
% {arr|aba|izq|der} = operadores
% X2,Y2 = estado siguiente
mover(arr,X1,Y1,X1,Y2 ):- Y2 is Y1 - 1.
mover(izq,X1,Y1,X2,Y1 ):- X2 is X1 - 1.
mover(aba,X1,Y1,X1,Y2 ):- Y2 is Y1 + 1.
mover(der,X1,Y1,X2,Y1 ):- X2 is X1 + 1.
% Comprobaci�n de nodo v�lido
% El nodo (estado) ser� v�lido si no est� fuera del laberinto, es un pasillo y no hemos pasado ya por �l
% sintaxis:
% valido( X, Y, Laberinto, Visitados )
% X --> coordenada x
% Y --> coordenada y
% Laberinto --> laberinto
% Visitados --> lista de los nodos por los que hemos pasado
valido(X,Y,Laberinto,Visitados):-filas(F), columnas(C), X>=0, Y>=0, X<C, Y<F,
matriz( Laberinto, X, Y, 32 ), not( esta(visitado(X,Y),Visitados) ).
% buscar la soluci�n y mostrarla en pantalla
% sintaxis:
% resuelve( Lab, Destx, Desty, Origx, Origy, Solucion )
% Lab --> laberinto
% Destx --> coordenada X de destino
% Desty --> coordenada Y de destino
% OrigX --> coordenada X de origen
% OrigY --> coordenada Y de origen
% Solucion --> lista de movimientos del camino
% limpiar los hechos din�micos
resuelve(_,_,_,_,_,_):-retract( filas(_) ),fail.
resuelve(_,_,_,_,_,_):-retract( columnas(_) ),fail.
resuelve( Lab, Destx, Desty, Origx, Origy, Solucion ):-
% Calculamos el tama�o del laberinto e introducimos los hechos correspondientes
tamanio( Lab, Filas ),
Lab = [Fila1|_],
tamanio( Fila1 , Cols),
assert( filas(Filas) ),
assert( columnas(Cols) ),
% buscamos el camino desde el origen al destino
% al principio s�lo hemos visitado el origen
camino( Lab, Destx, Desty, Origx, Origy, Solucion, [visitado(Origx, Origy)] ),
% mostramos el laberinto
muestra( Lab ),
% mostramos la lista de movimientos
write( Solucion ).
% Busca el camino en el laberinto, llevando cuenta de los nodos visitados para evitar bucles
%sintaxis:
% camino( Laberinto, Objx, Objy, X, Y, Movimientos, Anteriores )
% Laberinto --> laberinto
% Objx --> x objetivo (destino)
% Objy --> y objetivo (destino)
% X --> x posici�n actual
% Y --> y posici�n actual
% Movimientos --> lista de movimientos necesarios para ir de la posici�n actual al objetivo
% Anteriores --> lista de posiciones por las que se ha pasado
% caso base: estamos en el destino, no hay que dar ning�n paso, indiferentes los visitados

camino(_, X, Y, X, Y, [], _).
% recursi�n
camino(Laberinto, Objx, Objy, X, Y, [Mov|Resto], Anteriores):-
% pasar a una posici�n adyacente (generar un nuevo estado)
mover(Mov,X,Y,X2,Y2),
% comprobar que la nueva posici�n es v�lida
valido(X2,Y2,Laberinto,Anteriores),
% buscar un camino desde la nueva posici�n al destino
camino(Laberinto, Objx, Objy, X2, Y2, Resto, [visitado(X2,Y2)|Anteriores]).
