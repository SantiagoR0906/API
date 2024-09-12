from API import apiAccidentes
from ordenamiento import Funciones_de_Ordenamiento as FO
#from ordenamiento import ordenamiento1

def main():
    # Crea una instancia de la clase api
    api = apiAccidentes('https://www.datos.gov.co/resource/mg8y-amuh.json')
    arreglo = api.consumo()
    
    print('''\nDesorganizado\n''')
    print(arreglo)
    
    ordenar = FO()
    
    print('''\nMetodo Merge Sort\n''')
    resultado = ordenar.MergeSort(arreglo)
    print(resultado)
    
    print('''\nQuick Sort\n''')
    resultado = ordenar.quick(arreglo)
    print(resultado)
    
    print('''\nSelection Sort\n''')
    resultado = ordenar.SelectionSort(arreglo)
    print(resultado)
    
    print('''\nInsertion Sort\n''')
    resultado = ordenar.InsertionSort(arreglo)
    print(resultado)
    
if __name__ == "__main__":
    main()