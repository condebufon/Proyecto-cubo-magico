from consoleverse import console


def init_square(n: int) -> list[list[int]]:
    """
    Función que inicializa un cuadrado de orden n.

    Parameters
    ----------
    n : int
        Orden del cuadrado.

    Returns
    -------
    list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    cuadrado = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    return cuadrado


def print_square(square: list[list[int]]) -> None:
    """
    Función que imprime un cuadrado.

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    console.println('Cuadrado Mágico:', style='bold', color='green')
    console.new_line()
    console.print_matrix(square, color_index='yellow', color='blue', color_style='cyan')


def is_valid_square(square: list[list[int]]) -> bool:
    """
    Función que verifica si un cuadrado es válido.
    El cuadrado es válido si todos los números son distintos y están en el rango [1, n^2].

    Examples
    --------
    >>> is_valid_square([[1, 2], [3, 4]])
    True
    >>> is_valid_square([[1, 2], [3, 1]])
    False

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.

    Returns
    -------
    bool
        True si el cuadrado es válido, False en caso contrario.
    """
    val_guard = []
    for row in square:
      for col in row:
        if col in val_guard:
          print("False")
          return False
        else:
          val_guard.append(col)
    print("True")      
    return True


def is_magic_square(square: list[list[int]]) -> bool:
    """
    Función que verifica si un cuadrado es mágico.
    El cuadrado es mágico si es válido y la suma de cada fila, columna y diagonal es la misma.

    Examples
    --------
    >>> is_magic_square([[1, 2], [3, 4]])
    False

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.

    Returns
    -------
    bool
        True si el cuadrado es mágico, False en caso contrario.
    """
    if not is_valid_square(square):
        return False
    return True
      

def set_value(square: list[list[int]], col: int, row: int, value: int) -> None:
    """
    Función que asigna un valor a una posición del cuadrado.

    Parameters
    ----------
    square : list[list[int]]
        Lista de listas que representa el cuadrado.
    col : int
        Columna.
    row : int
        Fila.
    value : int
        Valor a asignar.
    """
    n = len(square)
    if n > row and n > col and n **2 > value:    
        square[row][col] = value


def menu() -> int:
    """
    Función que muestra el menú y retorna la opción seleccionada.

    Returns
    -------
    int
        Opción seleccionada.
    """
    console.clear_screen()
    console.new_line()
    console.println('Menú', style='bold', color='blue')
    console.new_line()

    console.println('1.', style='bold', color='blue', endl=' ')
    console.println('Ingresar un valor')

    console.println('2.', style='bold', color='blue', endl=' ')
    console.println('Verificar si es mágico')

    console.println('3.', style='bold', color='blue', endl=' ')
    console.println('Mostrar cuadrado')

    console.println('4.', style='bold', color='blue', endl=' ')
    console.println('Salir')

    console.new_line()
    option = int(console.inputln('Ingrese una opción: ', style='bold'))
    return option


def init_game() -> list[list[int]]:
    """
    Función que inicializa el juego.

    Returns
    -------
    list[list[int]]
        Lista de listas que representa el cuadrado.
    """
    console.clear_screen()
    console.new_line()
    console.println('Cuadrado mágico', style='bold', color='blue')
    console.new_line()
    n = int(console.inputln('Ingrese el orden del cuadrado mágico: '))
    console.new_line()
    console.println('El cuadrado mágico de orden', n, 'es:')
    console.new_line()
    cuadrado_magico = init_square(n)
    print_square(cuadrado_magico)
    console.inputln('\nPresione enter para continuar', style='bold')
    return cuadrado_magico


def main():
    cuadrado_magico = init_game()
    while True:
        match menu():
            case 1:
                console.clear_screen()
                console.new_line()
                console.println('Ingresar un valor', style='bold', color='blue')
                console.new_line()
                row = int(console.inputln('Ingrese la fila: ', style='bold'))
                col = int(console.inputln('Ingrese la columna: ', style='bold'))
                value = int(console.inputln('Ingrese el valor: ', style='bold'))
                set_value(cuadrado_magico, col, row, value)
                console.inputln('\nPresione enter para continuar', style='bold')
            case 2:
                console.clear_screen()
                console.new_line()
                console.println('Verificar si es mágico', style='bold', color='blue')
                console.new_line()
                if is_magic_square(cuadrado_magico):
                    console.println('El cuadrado es mágico', style='bold', color='green')
                else:
                    console.println('El cuadrado no es mágico', style='bold', color='red')
                console.inputln('\nPresione enter para continuar', style='bold')
            case 3:
                console.clear_screen()
                console.new_line()
                console.println('Mostrar cuadrado', style='bold', color='blue')
                console.new_line()
                print_square(cuadrado_magico)
                console.inputln('\nPresione enter para continuar', style='bold')
            case 4:
                console.clear_screen()
                console.new_line()
                console.println('Salir', style='bold', color='blue')
                console.new_line()
                console.println('Gracias por jugar', style='bold', color='green')
                return
            case _:
                console.clear_screen()
                console.new_line()
                console.println('Opción inválida', style='bold', color='red')
                console.new_line()
                console.inputln('\nPresione enter para continuar', style='bold')
                continue


main()