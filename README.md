# DataFlow
DataFlow is a compiler for a data science language implemented using PLY (Python Lex-Yacc).

## Manual de usuario
### Dependencias y ejecución
Para in
```
pip install ply
pip install pandas
pip install ast
pip install collections
```

To execute a DataFlow program run:
```
python dataflow path/file.df
```
### Estructura para un programa DataFlow
La estructura básica de un programa DataFlow es así:
```
// Declaración del nombre del programa.
program ejemplo;

// Declaración de variables

// Declaración de funciones(En caso de usarlos)


void main {

    // Generar los diferentes estatutos
}
```
### Declaración de variables
Dataflow tiene los siguientes tipos para sus variables:`int`, `float`, `char`.
```
program ejemplo;

// Variables globales
// Ints
var int int_uno, int_dos;
// Floats
var float float_uno, float_dos;
// Chars
var char char_uno, char_dos;

// En caso de que sean arreglos o matrices. Se declara cada uno por separado:
var int arreglo_uno[6];
var int arreglo_dos[4];
var float matriz_uno[3][3];
var float matriz_dos[1][2];

void main {

}
```

### Declaración y llamada de funciones
En DataFlow existen funciones de tipo `int`, `float`, `char`.
Y también existen funciones de tipo `void`, los cuales no regresan ningún valor.
```
program ejemplo;

var int result;

int func return_something(int p) {
    // Declaración de variables locales.
    var int a;
    a = 10 + p - 7;
    // Devuelve un valor que debe de ser igual a la función.
    return a;
}

func void print_something(int x) {
    // Puedes generar estatutos pero no va a regresar ningún valor.
}


void main {
    // Para las llamadas de funciones se debe de poner la palabra `func` antes del id de la función.
    func print_something(4)
    result = func return_something(10);
}
```
### Expresiones
DataFlow tiene expresiones aritméticas, relacionales y lógicas.
Cada una se utiliza dependiendo el estatuto que se quiera utilizar.
```
program ejemplo;

var int a, b;
var float x, y;
void main {
    a = 3;
    b = a + 2; // Aritmética sencilla
    if (a > b) { // Expresión relacional
        print(a > b && a == 3) ; // Expresión lógica junto con dos expresiones relacionales.
    }
}
```
### Cubo semántico
|  left operator |  right operator |   =   |   +   |   -   |   *   |   /   |    >   |    <   |    ==   |    !=   |    &&   |    ||   |
|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|  int  |  int  |  int  |  int  |  int  |  int  |  int  | bool | bool | bool | bool | ERROR | ERROR |
|  int  | float | ERROR | float | float | float | float | bool | bool | bool | bool | ERROR | ERROR |
|  int  |  char | ERROR | char | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  int  |  bool | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
| float |  int  | float | float | float | float | float | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
| float | float | float | float | float | float | float | bool | bool | bool | bool | ERROR | ERROR |
| float |  char | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
| float |  bool | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  char |  int  | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  char | float | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  char |  char |  char |  char | ERROR | ERROR | ERROR | ERROR | ERROR | bool | bool | ERROR | ERROR |
|  char |  bool | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  bool |  int  | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  bool | float | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  bool |  char | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR |
|  bool |  bool |  bool | ERROR | ERROR | ERROR | ERROR | ERROR | ERROR | bool | bool | bool | bool |

### Escritura
Dataflow imprime valores en la consola utilizando la palabra clave `print()`.
Siendo una expresión válida dentro de los paréntesis.
```
program ejemplo;

var int a;
void main {
    a = 3;
    print(a);
}
```
### Condicionales
Dataflow permite dos formas de generar las condicionales correctamente.
- `if`.
- `if` seguido de un `else`
```
program ejemplo;

var int a;
void main {
    a = 3;
    if (a > 2){
        print(a > 2);
    }
    else{
        print(a);
    }
}
```

### Bucles
Dataflow cuenta con dos formas diferentes de generar bucles: `while` y `for`.

```
program patito; 
var int i, x, o, j, y; 
var float k, l;
void main {
    x = 1 + (4 + 2 * 3 - 2) * 4 + 5;
    i = 1;
    o = i + 4 + x;
    k = 3 + 6 / 2 * (4 + 1) / o;
    if(x + 3 - 5 > o + 60 - 5){
        o = 5 + 8 ;
        print(o);
    } else {
        o = 3 + 6 ;
        print(o);
    }
    while( x > i){
        i = i + 1;
        print(i);
    }
    for j = 1 to (4) do {
        for j = 1 to (6) do {
            j = o + 1;
            print(j);
        }
    }
    y = 3 + 9 ;
    print(y);
}
```
### Arreglos y matrices
En Dataflow se puede generar arreglos de una dimensión y matrices de dos dimensiones. 
Estos pueden ser utilizados de varias formas.

```
program bubble_sort_program; 

var int i, j, temp;
var int arreglo[6];
void main {
    arreglo[0] = 2;
    arreglo[1] = 4;
    arreglo[2] = 5;
    arreglo[3] = 3;
    arreglo[4] = 6;
    arreglo[5] = 1;

    for i = 0 to (5) do {
        for j = 0 to (5 - i) do {
            if (j + 1 < 6) {
                if (arreglo[j] > arreglo[j + 1]) {
                    temp = arreglo[j] ;
                    arreglo[j] = arreglo[j + 1] ;
                    arreglo[j + 1] = temp ;
                }
            }
            j = j + 1 ;
        }
        i = i + 1 ;
    }

    for i = 0 to (5) do {
        print(arreglo[i]);
        i = i + 1;
    }
}
```

```
program print_matrix;

var int matrix_one[3][3];
var int matrix_two[3][3];
void main {
    for i = 0 to (2) do {
        for j = 0 to (2) do {
            matrix_one[i][j] = j + i + 4;
            print(j + i + 4);
            j = j + 1;
        }
        i = i + 1;
    }
}
```

