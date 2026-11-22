def erlang_b(traffic, lines):
    b=1.0
    for n in range(1,lines+1): b=traffic*b/(n+traffic*b)
    return b
A=120*3/60
print(f'offered load {A:.1f} Erlangs')
for n in (6,8,10,12): print(f'{n:2d} lines: blocking {erlang_b(A,n):6.2%}')
need=next(n for n in range(1,100) if erlang_b(A,n)<=0.01)
print('lines needed for blocking of 1% or less:',need)
print('for 180 calls/hour:',next(n for n in range(1,100) if erlang_b(9,n)<=0.01))
