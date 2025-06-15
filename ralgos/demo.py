# Test file to demonstrate ralgos functionalities

import ralgos

# Generators
g1 = ralgos.generator.kuniform(2)  # kwise uniform generator with k = 2, m = 100 (default)
g2 = ralgos.generator.uniform()    # independent unifrom generator with m = 100 (default)
g3 = ralgos.generator.uuniform()    # universal unifrom generator with m = 100 (default)
g4 = ralgos.generator.normal()       # normal generator mu = 0, std = 1
g5 = ralgos.generator.bernoulli()    # bernoulli with p = 0.5 (default)
g6 = ralgos.generator.kbernoulli(2)   # kwise bernoulli with k = 2, p = 0.5(default)
g7 = ralgos.generator.margulis(5,100)  # margulis random walk generator with n = 5, m = 100

print("\nOutput:\n")

print("Generators: ")
n = 10
generators = [g1,g2,g3,g4,g5,g6,g7]
for i in range(7):
    print(generators[i].type,": ",generators[i].sample(n))

# RV Definition
x1 = ralgos.make.rv(g1, name="x1")
x2 = ralgos.make.rv(g2, name="x2")
x3 = ralgos.make.rv(g3, name="x3")
x4 = ralgos.make.rv(g4, name="x4")
# x5 = ralgos.make.sum(ralgos.make.sum(x1,x2, name="s1"),ralgos.make.product(x3, x4, name="p1"),name="s2")
x5 = x1*x2 + x3*x4 + 2

print("\nNew Random Variable")
# x5.visualize()   # visualising constructed rv
print("x5: ",x5.sample(n))    # samping constructed rv


# Infer

x6 = ralgos.make.nop(g5,"+",10,"x6")
print("x6: ",x6.sample(n))    # samping constructed rv


x7 = ralgos.make.nop(g2,"+",10,"x7")
print("x6: ",x7.sample(n))    # samping constructed rv


print("\nChernoff bound on x4: ",ralgos.infer.concentrate.chernoff(x4,3)) # chernoff bound for x4, e^(-(3^2)/2)
print("Hoeffding bound on x4: ",ralgos.infer.concentrate.hoeffding(x4,3))

# Sum of Independet Bernoulli RVs
print("Chernoff bound on x6: ", ralgos.infer.concentrate.chernoff(x6,6))
print("Hoeffding bound on x6: ", ralgos.infer.concentrate.hoeffding(x6,6))

# Sum of Independent Unifrom RVs
print("Chernoff bound on x7: ", ralgos.infer.concentrate.chernoff(x7,800))
print("Hoeffding bound on x7: ", ralgos.infer.concentrate.hoeffding(x7,800))

