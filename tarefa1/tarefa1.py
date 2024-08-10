class LinkedList:

    # Classe __Node é usada internamente por LinkedList.
    # Não é visível de fora da classe devido aos dois underscores
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self,next):
            self.next = next

    # construtor da classe LinkedList        
    def __init__(self,contents=[]):
    # Lista com cabeça e dois ponteiros: um para o inicio da lista, um para o final.
    # Também mantem-se um contador de elementos da lista
    # Nó cabeça está sempre na primeira posição da lista e não contem item. 
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e) # append da lista ligada
            
    # adiciona elemento ao final da lista ligara       
    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

        
    def isEmpty(self):
        return self.numItems == 0
    
    # sobrecardo do método get; retorna o valor de posicao i, a = x[i]    
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    # sobrecarga do método set; atualiza valor da posicao i x[i]=a        
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")
        
    # concatenação como sobrecarga do operador +    
    def __add__(self,other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for str(type(self)) + " + " + str(type(other))")

        result = LinkedList()

        #copia primeira lista    
        cursor = self.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        #copia segunda lista
        cursor = other.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = cursor.getNext()

        return result
    
    # remoção como sobrecarga do operador del
    def __delitem__(self,item):
        if self.isEmpty():
            raise TypeError("Attempt to delete from empty list")
            
            # elemento a ser eliminado é o primeiro
        if self.first.getItem() == item:  
            self.first = self.first.getNext()
            self.numItems -= 1
            
            # elemento a ser eliminado não é o primeiro
        else:
            previous = self.first
            current = self.first.getNext()
            
            while current != None:
                if current.getItem() == item:
                    previous.setNext(current.getNext())
                    self.numItems -= 1
                    # verifica se elemento é o ultimo
                    if self.last == current:  
                        self.last = previous 
                    break
                else:
                    previous = current
                    current = current.getNext()

            if current == None:
                raise IndexError(f"LinkedList does not have {item}")
    
    # iteração sobrecarregada
    def __iter__(self):
        current = self.first.getNext() 
        while current is not None:
            yield current.getItem()
            current = current.getNext()
    
    # imprime lista
    def printList(self):
        if self.numItems == 0:
            print("Empty list")
        else:
            cursor = self.first.getNext()
            for i in range(self.numItems):
                print(f"{cursor.getItem()}")
                cursor = cursor.getNext()

l = LinkedList([1,2,3])
for i in l:
    print(i)