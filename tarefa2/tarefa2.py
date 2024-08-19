class Stack:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def push(self, item):
        # Adiciona o item no topo da pilha
        self.linkedList.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        
        # Remove e retorna o item do topo da pilha
        topItem = self.linkedList[self.linkedList.numItems - 1]
        del self.linkedList[topItem]
        return topItem
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        
        # Retorna o item do topo da pilha sem removê-lo
        return self.linkedList[self.linkedList.numItems - 1]
    
    def isEmpty(self):
        return self.linkedList.isEmpty()
    
    def size(self):
        return self.linkedList.numItems

    def printStack(self):
        # Imprime os elementos da pilha
        self.linkedList.printList()

# Exemplo de uso:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.printStack()  # Output: 10 20 30
print(stack.pop())  # Output: 30
stack.printStack()  # Output: 10 20
