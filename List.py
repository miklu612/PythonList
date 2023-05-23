
class ListIterator:

    def __init__(self, list_value=None):
        self.current = list_value

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            return_value = self.current.value
            self.current = self.current.child
            return return_value

    

class List:


    def __init__(self, iterable=None):

        if iterable == None:
            self.child = None
            self.value = None
        else:
            self.child = None
            self.value = None

            previous = None
            current = self

            for value in iterable:
                previous = current
                current.value = value
                current.child = List()
                current = current.child

            previous.child = None


    # Returns self
    def remove(self, index:int):

        current = self

        # If the index is 0 we want to remove the parent node. To achieve this
        # we will just copy the parent's child into the parent.
        if index == 0:
            if self.child != None:
                self.value = self.child.value
                self.child = self.child.child
            else:
                self = None
            return self

        # Search for the child to remove. We are actually searching the one
        # before the child we want to remove, since we can't go back in the list
        # so we just have to take the one before it, and replace its child with 
        # the child of the child we want to remove.
        while index - 1 > 0:
            assert(current.child != None), "Invalid"
            current = current.child
        
        assert(current.child != None), "Invalid"

        if current.child.child != None:
            current.child = current.child.child
        else:
            current.child = None

        return self

    # Returns self
    def replace(self, value_to_replace, replace_value):

        current = self

        # Simply just iterate through the children and replace any occurence of 
        # the value
        while current != None:
            if current.value == value_to_replace:
                current.value = replace_value
            current = current.child

        return self

    # Returns self
    def add(self, value):

        # If the current value is empty just add it there, and call it a day
        if self.value == None:
            self.value = value
            return self


        # This is used to iterate through the children to find the ond with an 
        # empty spot for the value
        current = self

        while current.value != None:
            if current.child == None:
                current.child = List()
            current = current.child
        
        
        current.add(value)

        return self

    def map_all(self, map_function):

        current = self

        while current != None:
            if current.value == None:
                break
            current.value = map_function(current.value)
            current = current.child

        return self

    def __repr__(self)->str:

        current = self
        output = ""

        while current.value != None:
            if output == "":
                output += str(current.value)
            else:
                output += ", " + str(current.value)
            if current.child != None:
                current = current.child
            else:
                break

        return "[" + output + "]"

    def __getitem__(self, key:int):

        current = self
        while key > 0:
            current = current.child

            if current == None:
                error_message = "Index `{}` not found".format(i)
                raise IndexError(error_message)

        return current.value

    def __iter__(self)->ListIterator:
        return ListIterator(self)

    def __len__(self):

        current = self
        length = 0

        while current != None:
            length += 1
            current = current.child

        return length
            

