def fofa():
    print("========FOFA========")
    fofa_email = input("输入FOFA email: ") 
    fofa_key = input("输入FOFA API key: ")
    with open('fofa.json', 'w') as f:
        f.write('{"fofa_email":"' + fofa_email + '","fofa_key":"' + fofa_key + '"}')
    f.close()
    print("fofa.json已保存")




fofa()

