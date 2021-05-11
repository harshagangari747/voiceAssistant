import json
def getenglish(query) :
    f=open('C:\\Users\\user\\OneDrive\\Desktop\\Final Project\\telugudict.txt','r',encoding='utf-8')
    data = f.read()
    js =json.loads(data)
    query = list(query)
    engquery = ''
    for i in query :
        if i in js :
            engquery = engquery + js[i]+" "
    return engquery

