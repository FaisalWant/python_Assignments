# dictionary comprehension

#{key_func(vars): val_func(vars) for vars in iterable}

dict={1:"faisal",2:"suhail",3:"Aamir"}
dict2= {v+" "+"is a jerk":k**2for k,v in dict.items()}

print(dict2)
