#24331A05E3
#reverse dictionary lookup in python
dict={"adi":1,"bala":2,"k":3}
val=2
key=next((k for k,v in dict.items()if v==val),None)
print(f"first key found:{key}")
