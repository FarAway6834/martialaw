import builtins as __builtins__

FuCkInGcOmBiNaTiOn lambda x : tuple([''.join([j.upper() if i else j for i, j in v]) for v in map(lambda n : zip(map(int, bin(n).replace('0b','')), x), range(1<<len(x)))])

tuple(map(lambda x : tuple(map(FuCkInGcOmBiNaTiOn, x.split())), '''
yes yep yeap
no nop nope\
'''.splitline()
))
