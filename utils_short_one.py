lst = ['a','b','e','f','h','i','k','l','m','n','o','t','u','w','']

def g(x):    #convert arrays to txt
    return {
        hash(tuple(np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))): 'a',
        hash(tuple(np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]))): 'b',
        hash(tuple(np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]))): 'e',
        hash(tuple(np.array([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]))): 'f',
        hash(tuple(np.array([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]))): 'h',
        hash(tuple(np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]))): 'i',
        hash(tuple(np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]))): 'k',
        hash(tuple(np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]))): 'l',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]))): 'm',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]))): 'n',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]))): 'o',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]))): 't',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]))): 'u',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]))): 'w',
        hash(tuple(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]))): ''}[hash(tuple(x))]
        
def f(x):   #convert txt to arrays
    return {
    'a': np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
    'b': np.array([[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]]),
    'e': np.array([[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]]),
    'f': np.array([[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]]),
    'h': np.array([[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]]),
    'i': np.array([[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]),
    'k': np.array([[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]]),
    'l': np.array([[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]),
    'm': np.array([[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]]),
    'n': np.array([[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]]),
    'o': np.array([[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]]),
    't': np.array([[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]]),
    'u': np.array([[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]]),
    'w': np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]),
    '' : np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])}[x]   
    
def X_gen(txt): #converts txt input to input array
    X_array = np.array([])
    
    for letter in txt:
        if letter in lst:
            if X_array.shape[0] == 0: X_array = f(letter)
            else: X_array = np.hstack((X_array,f(letter)))
            
    if len(txt) < 13:
        txtlen = 13 - len(txt)
        for i in range(txtlen):
            X_array = np.hstack((X_array,f("")))
    
    return (X_array)  

def y_gen(y): #converts predicted array to output txt
    for i in range(0,75,15): y[:,i:i+15] = (y[:,i:i+15] == y[:,i:i+15].max(axis=1)[:,None]).astype(int)
    txt = ""
    for i in range(0,75,15): txt = txt + g(y[:,i:i+15].ravel())
    return (txt)
