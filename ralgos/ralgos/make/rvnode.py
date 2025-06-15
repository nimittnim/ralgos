from graphviz import Digraph
from ralgos.generator.Generator import Generator

class RVNode:
    def __init__(self, name=None):
        self.name = name

    def visualize(self, filename="rv_tree"):
        dot = Digraph(format='png')
        visited = set()

        def add_nodes_edges(node):
            # if id(node) in visited:
            #     return
            visited.add(id(node))

            label = node.name or ""
            if isinstance(node, RV):
                label = f"RV\n{label}"
            elif isinstance(node, Sum):
                label = f"Sum\n{label}"
            elif isinstance(node, Product):
                label = f"Product\n{label}"
            elif isinstance(node, Constant):
                label = f"Const\n{label}"
            else:
                label = f"Op\n{label}"

            dot.node(str(id(node)), label)

            for child in getattr(node, 'children', []):
                dot.edge(str(id(node)), str(id(child)))
                add_nodes_edges(child)

        add_nodes_edges(self)
        dot.render(filename, view=True)

    def sample(self, n=1):
        result = []
        # Step 1: collect all base nodes
        base_nodes = []

        def collect(node):
            if isinstance(node, RV):
                base_nodes.append(node)
            for child in getattr(node, 'children', []):
                collect(child)

        collect(self)

        # Step 2: group base nodes by generator
        from collections import defaultdict
        generator_to_bases = defaultdict(list)
        for base in base_nodes:
            generator_to_bases[base.generator].append(base)

        # Step 3: Assign values to RVs and evaluate
        for iter in range(n):
            for generator, bases in generator_to_bases.items():
                samples = generator.sample(len(bases))
                for i in range(len(bases)):
                    bases[i].value = samples[i]
            result.append(self.evaluate())

        return result
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = constant(other, name=str(other))
        if not isinstance(other, RVNode):
            raise TypeError("Addition is only supported with RVNode or number.")
        return sum(self, other, name=f"({self.name}+{other.name})")

    def __radd__(self, other):
        return self.__add__(other) 

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = constant(other, name=str(other))
        if not isinstance(other, RVNode):
            raise TypeError("Multiplication is only supported with RVNode or number.")
        return product(self, other, name=f"({self.name}*{other.name})")

    def __rmul__(self, other):
        return self.__mul__(other)  

    def evaluate(self):
        raise NotImplementedError


class RV(RVNode):
    def __init__(self, name, generator):
        super().__init__(name)
        self.generator = generator
        self.children = []
        self.value = None
    
    def evaluate(self):
        return self.value

class Operator(RVNode):
    def __init__(self, name, op, children):
        super().__init__(name)
        self.op = op 
        self.children = children

class Sum(Operator):
    def __init__(self, name, children):
        super().__init__(name, "sum", children)

    def evaluate(self):
        result = 0
        for child in self.children:
            result += child.evaluate()
        return result


class Product(Operator):
    def __init__(self, name, children):
        super().__init__(name, "product", children)

    def evaluate(self):
        result = 1
        for child in self.children:
            result *= child.evaluate()
        return result
    
class Constant(RVNode):
    def __init__(self,name,value):
        super().__init__(name)
        self.value = value

    def evaluate(self):
        return self.value


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

def nop(generator, op, n, name="Nop"):
    if not isinstance(generator,Generator):
        raise TypeError("expected generator")
    rvnodes = []
    for i in range(n):
        rvnodes.append(rv(generator,f"{name}{i}"))
    if (op == "+"):
        return Sum(name=f"({rvnodes[0].name}+..{n})",children=rvnodes)
    elif (op == "*"):
        return Sum(name="Product",children=rvnodes)
   

def constant(value, name="Const"):
    """
    Create a Constant node with given value"""
    if not (isinstance(value,int) or isinstance(value,float)):
        raise TypeError("constant expects a number.")
    return Constant(name=name,value=value)

