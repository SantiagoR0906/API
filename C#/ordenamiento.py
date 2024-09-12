class Funciones_de_Ordenamiento:

    def __init__(self):
        pass

    def MergeSort(self, arreglito):
        base = len(arreglito)
        if base <= 1:
            return arreglito

        ListaIzquierda = arreglito[:len(arreglito)//2]
        ListaDerecha = arreglito[len(arreglito)//2:]

        ListaIzquierda = Funciones_de_Ordenamiento.MergeSort(self, ListaIzquierda)
        ListaDerecha = Funciones_de_Ordenamiento.MergeSort(self, ListaDerecha)

        return Funciones_de_Ordenamiento.Merge(self,ListaIzquierda, ListaDerecha)
 
    def Merge(self,ListaIzquierda, ListaDerecha):
        resultado = []
    
        while (len(ListaIzquierda) > 0 and len(ListaDerecha) > 0): 
            if ListaIzquierda[0] < ListaDerecha[0]:
                resultado.append(ListaIzquierda[0])
                ListaIzquierda = ListaIzquierda[1:]
            else:
                resultado.append(ListaDerecha[0])
                ListaDerecha = ListaDerecha[1:]
                
        if len(ListaDerecha) > 0:
            resultado = resultado + ListaDerecha
        if len(ListaIzquierda) > 0:
            resultado = resultado + ListaIzquierda
            
        return resultado

    def quick(self,arreglito):
        base = len(arreglito)
        
        if base <+ 1:
            return arreglito
        
        pivote = arreglito.pop()
        listaDerecha = []
        ListaIzquierda = []
        
        for i in arreglito:
            if i <= pivote:
                ListaIzquierda.append(i)
            else:
                listaDerecha.append(i)
                
        ListaDerecha = Funciones_de_Ordenamiento.quick(self,listaDerecha)
        ListaIzquierda = Funciones_de_Ordenamiento.quick(self, ListaIzquierda)
                
        return ListaIzquierda + [pivote] + ListaDerecha
    
    def InsertionSort(self, arreglito):
        for i in range(1, len(arreglito)):
            Valor = arreglito[i]
            j = i - 1
            while j >= 0 and Valor < arreglito[j]:
                arreglito[j + 1] = arreglito[j]
                j -= 1
            arreglito[j + 1] = Valor
        return arreglito


    def SelectionSort(self, arreglito):
        for i in range(len(arreglito)):
            min = i
            for j in range(i + 1, len(arreglito)):
                if arreglito[j] < arreglito[min]:
                    min = j
            arreglito[i], arreglito[min] = arreglito[min], arreglito[i]
        return arreglito
