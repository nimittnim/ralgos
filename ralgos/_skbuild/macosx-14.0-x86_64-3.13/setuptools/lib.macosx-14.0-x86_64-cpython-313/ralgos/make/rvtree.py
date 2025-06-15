from .rvnode import RV,Sum,Product,Constant, RVNode
from ralgos.generator.Generator import Generator

def rv(generator, name="RV"):
    """
    Create a base random variable node.
    `generator` must be an object with a `.sample(n)` method.
    """
    if not isinstance(generator,Generator):
        raise TypeError("rv expects a generator.")
    return RV(name=name, generator=generator)

def sum(*rvnodes, name="Sum"):
    """
    Create a Sum node from multiple RVNodes.
    """
    for node in rvnodes:
        if not isinstance(node, RVNode):
            raise TypeError("sum expects random variables.")
        
    return Sum(name=name, children=rvnodes)

def product(*rvnodes, name="Product"):
    """
    Create a Product node from multiple RVNodes.
    """
    for node in rvnodes:
        if not isinstance(node, RVNode):
            raise TypeError("product expects a random variables.")
        
    return Product(name=name, children=rvnodes)

def constant(value, name="Const"):
    """
    Create a Constant node with given value"""
    if not (isinstance(value,int) or isinstance(value,float)):
        raise TypeError("constant expects a number.")
    return Constant(name=name,value=value)