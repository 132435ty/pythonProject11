hypotenuse_lambda = lambda a, b: (a**2 + b**2)**0.5
hypotenuse = hypotenuse_lambda(int(input('первый катет: ')), int(input('второй катет: ')))
print(hypotenuse)
