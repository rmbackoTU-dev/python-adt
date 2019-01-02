import UserDict

class scHashTable:
    
    #It is reccomending to have a prime key size to reduce collisions 
    DEFAULT_KEYS=7
    DEFAULT_CHAINSIZE=3


    '''
    Function to initialize seperate chaining hash
    Threshold/Capacity is the number of spaces total a hash should have
	'''
	def __init__(self, capacity=DEFAULT_KEYS*DEFAULT_CHAINSIZE, \
		chainsize=DEFAULT_CHAINSIZE):
        self.size=DEFAULT_KEYS;
        self.threshold=capacity;
        self.chains=[[] for _ in range(capacity//chainsize)]

    '''
    Takes an item and hashs the item to a key, if a key is provided  it uses the key
    If not then then hash hashs to the alphanumeric position mod the capacity
    '''
    def __hash__(self, item, key=DEFAULT_KEYS):
    	pass

     '''
     Returns the size of the keys in the hash table
     '''
    def __len__(self):
    	return self.size;

    '''
    Enumerator class function implements get item:
    Gets a item at location key
    If key is out of range raise IndexError
    If key is inappropriate type (mutable) raises TypeError
    If key is not found raises KeyError
    '''
    def __getitem__(self, key):
    	pass

     '''
     Enumerator class function implements delete item:
     Deletes and its attached items
    To delete a single item from the chain see delete Item
    Throws similar exceptions to __getitem__
     '''
    def __delitem__(self, key):
    	pass
    '''
    Enumerator class function implements contains:
    Checks for presense of a key and returns boolean
    if found return true if  not found returns false
    '''
    def __contains__(self, key):
    	pass

    ''''
    Enumerator class function implements length hint
    Gives an estimate of how large the hash table could be
    by returning the capacity
    '''
    def  __length_hint__(self):
    	pass

    '''
    Enumerator class function implements missing 
    Called by __getitem__ to return an object when non is 
    found by __getitem__
    '''
    def __missing__(self, key):
    	pass

    '''
    Enumerator class function implements reversed
    Returns a new iterator which when iterated goes through keys backward
    Reverse only reverses keys not their chains
    '''
    def __reversed__(self):
    	pass

    '''
    Object class test if a seperate chain hash is equal.
    As such they have similar keys,
    And items resolve to similar strings
    '''
    def __eq__(self, other):
    	pass

    '''
    Object class test if a seperate chain hash is not equal
    Checks for one key or one item which does not match
    returns a boolean based on if a violation if found
    '''
    def __ne__(self, other):
    	pass

    '''
    Object class repersentation returns a string that contains
     the seperate chain as a sntactically correct
    repersentation as a python built_in function, or dictionary
    '''
    def __repr__(self):
    	pass
    '''
    Object class string returns a string which is a 
    visual repesentation of the seperate chain
    '''
    def __str__(self):
    	pass

    '''
     Implements a rehash of all of the keys to a new key as determined by the size
    '''
    def rehash(self):
    	pass

    '''
        Enlarges the capacity to the new capcacity size
    '''
    def resize(self, capacity):
    	pass

    '''
     Test for 0 keys found
    '''
    def is_empty(self):
    	pass

    '''
    Used to insert item into seperate chain at key location
    '''
    def insert(self, key, item):
    	pass


    '''
    Used to delete an item at seperate chain at key location
    '''
    def deleteItem(self, key, item):
    	pass


    '''
    Used to copy all the contents to a new memory location
    '''
    def deepcopy(self, dest):
        pass

    '''
    Used to return the old memory location to a new variable
    '''
    def copy(self):
    	pass

    '''
    Used to list all of the values in the seperatation chain hash
    '''
    def values(self):
    	pass

    '''
    Used to list all the keys in the seperation chain hash
    '''
    def keys(self):
    	pass

    '''
    Used to empty out the seperatation chain hash
    '''
    def clear(self):
    	pass

    '''
    Used to insert another interable like a list into the seperatation chain hash
    '''
    def update(self, iterable):
    	pass
