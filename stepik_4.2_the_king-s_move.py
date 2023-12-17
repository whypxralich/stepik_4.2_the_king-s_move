#stepik_4.2_the_king-s_move

st1 = int(input())
gr1 = int(input())
st2 = int(input())
gr2 = int(input())

st = st2 - st1  
gr = gr2 - gr1  

if -1 <= st <= 1 and -1 <= gr <= 1:
    print('YES')
else:
    print('NO')