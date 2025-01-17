from itertools import tee, starmap, chain, islice
from operator import pow
from functools import partial


# TASK 1:
print("TASK 1:")

def transform_iterator(pairs):
    it1, it2 = tee(pairs, 2)

    c_values = starmap(pow, it2)
    
    return (a + (c,) for a, c in zip(it1, c_values))

pairs = iter([(1, 2), (3, 4), (5, 6)])

result = transform_iterator(pairs)

for triplet in result:
    print(triplet)

# TASK 2:
print("TASK 2:")

def make_tree(n, iterable):
    """Creates a balanced binary tree from the first n elements of an iterable."""
    elements = list(islice(iterable, n))
    
    if not elements:
        return None
    
    mid = len(elements) // 2
    left = make_tree(mid, iter(elements[:mid]))
    right = make_tree(len(elements) - mid - 1, iter(elements[mid + 1:]))
    return (left, elements[mid], right)

tree = make_tree(7, "alakota")
print(tree)
# Output: (((None, 'a', None), 'l', (None, 'a', None)), 'k', ((None, 'o', None), 't', (None, 'a', None)))


def traverse_yield(tree, preorder=False, inorder=False, postorder=False):
    """Traverses a binary tree using yield and yield from."""
    if sum([preorder, inorder, postorder]) != 1:
        raise ValueError("Exactly one of the parameters preorder, inorder, or postorder must be True.")
    
    if tree is None:
        return
    
    left, el, right = tree
    
    if preorder:
        yield el
        yield from traverse_yield(left, preorder, inorder, postorder)
        yield from traverse_yield(right, preorder, inorder, postorder)
    elif inorder:
        yield from traverse_yield(left, preorder, inorder, postorder)
        yield el
        yield from traverse_yield(right, preorder, inorder, postorder)
    elif postorder:
        yield from traverse_yield(left, preorder, inorder, postorder)
        yield from traverse_yield(right, preorder, inorder, postorder)
        yield el


for el in traverse_yield(tree, inorder=True):
    print(el, end=" ")
print("")

from itertools import chain, repeat

def traverse_chain(tree, preorder=False, inorder=False, postorder=False):
    """Traverses a binary tree using itertools.chain."""
    if sum([preorder, inorder, postorder]) != 1:
        raise ValueError("Exactly one of the parameters preorder, inorder, or postorder must be True.")
    
    if tree is None:
        return iter(())
    
    left, el, right = tree
    
    left_gen = traverse_chain(left, preorder, inorder, postorder)
    right_gen = traverse_chain(right, preorder, inorder, postorder)
    
    if preorder:
        return chain(repeat(el, 1), left_gen, right_gen)
    elif inorder:
        return chain(left_gen, repeat(el, 1), right_gen)
    elif postorder:
        return chain(left_gen, right_gen, repeat(el, 1))


for el in traverse_chain(tree, inorder=True):
    print(el, end=" ")
print("")

# TASK 3:
print("TASK 3:")

def debug(func):
    """Decorator to print function call arguments and its result."""
    def wrapper(*args, **kwargs):
        print(f"Function call: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# Example function
@debug
def add(a, b):
    return a + b

add(2, 3)
