users = ['Steve', 'Stefano', 'Stephanie']

data = ['Steve', 420, True]
emptyArray = []

print(users[0])
print(users[-1]) #come per gli array di JS, bene o male uguale

print(users.index('Stefano')) #questo mi dà l'indice di Stefano

print(users[1:]) #questo mi dà i valori dalla posizione inserita (qui 1) all'ultimo 

users.append('Frank') #questo è come il push di JS

#posso fare anche così:
users += ['Josh'] #se non lo metto come un array a se stante, ma ad esempio metto solo la stringa "Josh", mi pusha dentro ogni singola lettera anziché il nome
#aggiungo un altro array al mio array di prima e così li mergio
#oppure ancora così: 
users.extend(['Bob', 'Paola'])
print(users)

#users.extend(data)
##questo mergia di nuovo le due liste, così ho tutto insieme
#print(users)

users.insert(0, 'Ivan') #questo metodo mi mette l'elemento all'indice del primo parametro
users[2:2] = ['Ermanno', 'Adalgisa']
#qui sto dicendo di addare questi altri due valori entrambi in posizione 2, senza rimpiazzare nulla
print(users)

users[1:3] = ['Samuele', 'Armando']
#questa cosa, invece

users.remove('Bob') #questo è per rimuovere l'elemento specificato
#esiste anche pop, proprio come in JS. Lo toglie dalla lista e lo ritorna

del users[0] #questo invece rimuove l'elemento della lista all'indice desiderato

#se scrivo "del data", cancello tutto l'array e Python non lo trova più anche se è definito

#posso anche svuoltare completamente un array col metodo clear: 

data.clear()

users.sort() #come in JS, questo sorta ma a modo suo
