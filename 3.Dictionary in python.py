#it has a key for a value
data = {1:'pratik',2:'choubey',4: 'Happy'}
print(data)
print(data[1])
print(data[4])
#print(data[3])  error
print(data.get(1))
print(data.get(3))
print(data.get(1,'Not found'))
print(data.get(3,'NOt found'))
keys = [1,2,3]
value = ['pratik','subbu','ssss']
data  = dict(zip(keys,value))
print(data)
data[4] = 'dddd'
print(data)
del data[3]
print(data)
prog = {'js':'Atom','python':['pycharm','sublime'],'java':{'jse':'Netbeans','jee':'Eclipse'}}
print(prog['js'])
print(prog['python'])
print((prog['python'][0]))
print(prog['java']['jee'])
print(prog['java'])
#dictionary.items()
