from singly_linked_list import LinkedList
from random import randint

#example one
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def populate_list(n=20, upper_bound=1000):
    """
    this populates a linked list with values.

    Parameter
    --------
    * n - the number of elements in our linked list
    default: 20
    * upper_bound - the upper bound of random integers
    in our list.

    Returns
    -------
    a LinkedList  object from 
    singly_linked_list.py
    """
    listing = LinkedList()
    [listing.append(randint(0,1000))
                    for _ in range(n)]
    return listing
        

def traverse_list(cur, f):
    # do some work
    if cur:
        f(cur)
        traverse_list(cur.next, f)
    else:
        return None
    
def accumulate_values(cur, f, accumulation):
    if cur is None:
        return accumulation
    else:
        return accumulate_values(cur.next, f, accumulation+f(cur))


# this code will not be executed,
# unless the script is run
if __name__ == '__main__':
     listing = populate_list()
     traverse_list(listing.head, lambda x: print(x.data))
     print("Accumulation",accumulate_values(listing.head, lambda x: x.data*2, 0))
