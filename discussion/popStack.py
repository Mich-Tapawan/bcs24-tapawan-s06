class PopStack:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size
        
    def is_full(self):
        return self.top == self.max_size - 1
   
    def is_empty(self):
        return self.top == -1
   
    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.stack.append(data)
            return True
        else:
            return "Stack overflow"
       
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            return "Stack Underflow"
 
    def display_elements(self):
        if self.is_empty():
            print("Stack undeflow")
        else:
            print("Element in stack list: ")
            for i in range(self.top + 1):
                print(self.stack[i])


def palindrome_checker(string):
    s = PopStack(len(string))

    for char in string:
        s.push(char)

    s.display_elements()
    
    for i in range(len(string)):
        popped = s.pop()
        if popped != string[i]:
            print("The input is not a palindrome.")
            return False
    
    print("The input is a palindrome!")
    return True


string = input("Please enter a palindrome: ").lower()
item = []

for char in string:
    if char.isalpha() == False:
        continue
    else:
        item.append(char)

key = "".join(item)
palindrome_checker(key)