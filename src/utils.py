def top_n(dict_1,n=5):
    return sorted(dict_1.items(),key=lambda x:x[1],reverse=True)[:n]