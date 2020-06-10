def change(st):
    dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    st = st.lower()
    ret = ''
    print(st)
    for i in dic:
        if i in st:
            ret+='1'
        else:
            ret+='0'
    return ret

