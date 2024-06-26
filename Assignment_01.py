class Empty(Exception):
    ''' Error attempting to access an element from an empty container.'''
    pass

class _DoublyLinkedBase:
    '''A base class providing a doubly linked list representation.'''

    #-----------------------------------------------------------------
    class _Node:
        '''Lightweight, nonpublic class for storing a doubly linked node.'''
        __slots__ = '_element', '_prev', '_next'        # streamline memory

        def __init__(self, element, prev, next): # initialize node's field
            self._element = element       # element to be stored
            self._prev = prev             # Previous node reference
            self._next = next             # next node reference
    #-------------------------------------------------------------------
    def __init__(self):
        '''Create an empty list.'''
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer      # trailer is after header
        self._trailer._prev = self._header      # header is before trailer
        self._size = 0                          # Number of elements

    def __len__(self):
        '''Return the number of elements in the list.'''
        return self._size

    def is_empty(self):
        '''Return True if list is empty.'''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return new node.'''
        newest = self._Node(e, predecessor, successor) # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''Delete nonsentinel node from the list and return its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1                 # record deleted element
        element = node._element
        node._prev = node._next = node._element = None # deprecate node
        return element      # return deleted element

class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access'''

    # -------------- nested Position Class ----------------------------
    class Position:
        '''An abstraction representing the location of a single element'''

        def __init__(self, container, node):
            '''Constructor should not be invoked by user'''
            self._container = container
            self._node = node

        def element(self):
            '''Return the element stored at this Position'''
            return self._node._element

        def __eq__(self, other):
            '''Return True if other is a Position representing the same location'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''Return True if other does not represent the same location'''
            return not (self == other)

        #-------------------- Utility Methods ---------------------------

    def _validate(self, p):
        '''Return position's node or raise appropriate error if invalid'''
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:   # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        ''' Return Position instance for a given node(or None if sentinel)'''
        if node is self._header or node is self._trailer:
            return None             #boundary violation - sentinel node
        else:
            return self.Position(self, node)    # legitimate position

    # ------------------- Accessors ----------------------------
    def first(self):
        ''' Return the first Position in the list (or None if list is empty)'''
        return self._make_position(self._header._next)

    def last(self):
        '''Return the last Position in the list (or None if list is empty)'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''Return the Position just before Position p (or None if p is first)'''
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        '''Return the Position just after Position p (or None if p is last)'''
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        '''Generate a forward iteration of the elements of the list'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __str__(self):
        ''' Generates a string representation of the list'''
        arr = ''
        cursor = self.first()
        while cursor is not None:
            arr += str(cursor.element()) + ', '
            cursor = self.after(cursor)
        return '<' + arr + '>'

    #-------------- Mutators ------------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        '''Add element between existing nodes and return new Position'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        '''Insert element e at the front of the list and return new Position'''
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        '''Insert element e at the back of the list and return new Position'''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        '''Insert element e into list before Position p and return new Position'''
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        '''Insert element e into list after Position p and return new Position.'''
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        '''Remove and return the element at Position p'''
        original = self._validate(p)
        return self._delete_node(original) # inherited method returns element

    def replace(self, p, e):
        '''
        Replace the element at Position p with e.
        Return the element formerly at Position p.
        '''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

class NameBasedPositionalList(PositionalList):
    '''A modified positional list that organizes characters based on a specific name provided during initialization'''

    def __init__(self, name):
        '''Create a NameBasedPositionalList with the given name.'''
        super().__init__()
        self._name = name
        self._name_set = set(name)
        self._name_count = {char: 0 for char in name}

    def insert_character(self, char):
        '''Insert a character into the list based on the given rules.'''
        if char in self._name_set and self._name_count[char] < self._name.count(char):
            # If the character is part of the name and still needed
            self._insert_char_in_name(char)
        else:
            # If the character is not part of the name or not needed anymore
            self.add_last(char)

    def _insert_char_in_name(self, char):
        '''Insert a character into the list at the appropriate position based on the name.'''
        current = self.first()
        while current is not None:
            if current.element() not in self._name_set or current.element() == char:
                # Insert the character before the first non-name character or its repeated occurrence
                self.add_before(current, char)
                break
            current = self.after(current)
        if current is None:
            # If no non-name character is found, append to the end of the list
            self.add_last(char)

    def __str__(self):
        ''' Generates a string representation of the list'''
        arr = ''
        current = self.first()
        while current is not None:
            arr += str(current.element()) + ', '
            current = self.after(current)
        return '<' + arr + '>'

# Demonstration
if __name__ == "__main__":
    # Input the user's name
    user_name = input("Enter your name: ")

    # Create a NameBasedPositionalList with the user's name
    name_list = NameBasedPositionalList(user_name)

    # Input characters to insert
    characters_to_insert = input("Enter characters to insert: ")

    # Insert characters according to the rules
    for char in characters_to_insert:
        name_list.insert_character(char)

    # Display the resulting list
    print("Final list:", name_list)
