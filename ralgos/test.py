import ralgos
from ralgos.make import nop, rv

g1 = ralgos.generator.kbernoulli(k=2)
# g2 = ralgos.generator.bernoulli()
# g3 = ralgos.generator.bernoulli()
# print(g2 == g2)
# l1 = g1.sample(1000)
# l2 = g2.sample(1000)
# print(sum(l1)/100)
# print(sum(l2)/100)

x1 = rv(g1,"x1")
x2 = rv(g1,"x2")

x3 = nop(x1,"+",10) + x2
x4 = x3 * x1

# x4.visualize()
print(x4.sample(10))
# x6.visualize()
# print(x1.sample(10))
# x5 = sum(x1,x1)
# x5.visualize()
# print(x5.sample(10))

# print(ralgos.infer.concentrate.chernoff(x5,0.5))

# g = ralgos.generator.margulis(10,100)
# print(g.sample(100))