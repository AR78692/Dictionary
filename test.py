My_Dics={'Facebook':'MarkGukurBag','Google':'Larry Pag','Whatsapp':'Brain Acton'}
print('___Access Dictionary Key___')
for m in My_Dics:
    print(m)
print('___Access Dictionary Value___')
for a,n in My_Dics.items():
    print(a,n)
print('___For Check___')
if 'Facebook1' in My_Dics:
    print('Yes Facebook in dic')
else:
    print('Facebook not here!')
print('___For Dictionary Length___')
print(len(My_Dics))
print('___For Adding Itmes___')
My_Dics['Mobile']='Martin Copper'
for x,y in My_Dics.items():
    print(x,y)
print('___For Remove Itme___')
My_Dics.pop('Google')
for ataur, nabila in My_Dics.items():
    print(ataur,nabila)
print('___Remove for Popitem___')
My_Dics.popitem()
for ataur,nabila in My_Dics.items():
    print(ataur,nabila)
print('__For Del keyword___')
del My_Dics['Facebook']
for x,y in My_Dics.items():
    print(x,y)
# print('___Del Keyword delete also Dictionary completely___')
# del My_Dics
# print(My_Dics)
#--------------------------------------------------
# print('___Clear Method Empty the dictionary___')
# My_Dics.clear()
# for x in My_Dics:
#     print(x)
print('___Method for Copy dictionary___')
My_Copy_Dict=My_Dics.copy()
print(My_Copy_Dict)
print('___Another Method For Copy___')
My_Copy=dict(My_Dics)
print(My_Copy)
#-------------------------------------------
print('___Nested Dictionary___')
myfamily={'child1':{'Name':'Ataur rahaman','Age':'22'},
        'child2':{'Name':'Masiur rahaman','Age':'23'},
        'child3':{'Name':'Asfak Rahaman','Age':'25'}
myfamily={'child1':child1,
                'child2':child2,
                'child3':child3
                }
}
print(myfamily)