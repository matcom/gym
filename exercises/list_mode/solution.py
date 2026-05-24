from typing import Any

SUBMIT = True


def list_mode(_items: list[Any]) -> Any:
    if(_items == []):
        return None
    #todos se inicializan en 0 (da igual para los valores que no son numericos es solo para asignarle algun valor )
    count_1 = 0 #te da el valor d la i segun 
    count_solution = count_1 #en caso de que sea mayor la cantidad de apariciones del valor anterior se actualiza , sino se mantien
    current_value = count_solution #si el numero es mayor entonces cambiamos la variable 
    
    
    for i in _items:
        for j in _items:
            if i == j:
                count_1+=1
        if(count_1 > count_solution):
            count_solution = count_1
            current_value = i
            count_1 = 0
                
    return current_value

#le añadi el caso de prueba para el None que no estaba 
def test() -> None:
    """Simple self-test for Most Common Element."""
    cases: list[tuple[list[Any], Any]] = [
        ([1, 2, 2, 3, 3, 3], 3),
        (["a", "b", "a"], "a"),
        ([10], 10),([],None)
    ]
    for items, expected in cases:
        try:
            res = list_mode(items)
            assert res == expected, (
                f"Failed for {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
