X = T.dmatrix()
y = T.dmatrix()

X_input = np.genfromtxt('X.csv',delimiter=',') #5000x195
y_input = np.genfromtxt('y.csv',delimiter=',')  #5000x75

input_layer_size, hidden_layer_size_1, hidden_layer_size_2, y_size = 195, 15, 15, 75

theta1 = theano.shared(np.array(np.random.rand(hidden_layer_size_1, (input_layer_size+1)), dtype=theano.config.floatX))
theta2 = theano.shared(np.array(np.random.rand(hidden_layer_size_2, (hidden_layer_size_1+1)), dtype=theano.config.floatX))
theta3 = theano.shared(np.array(np.random.rand(y_size, hidden_layer_size_2+1), dtype=theano.config.floatX))

def computeCost(X, y, w1, w2, w3):
    m = X.shape[0]
    b = T.ones((m,1))
    a_1 = T.concatenate([b, X], axis=1)
    z_2 = T.dot(a_1, T.transpose(w1))
    a_2 = T.nnet.nnet.sigmoid(z_2)
    a_2 = T.concatenate([b, a_2], axis=1)
    z_3 = T.dot(a_2, T.transpose(w2))
    a_3 = T.nnet.nnet.sigmoid(z_3)
    a_3 = T.concatenate([b, a_3], axis=1)
    z_4 = T.dot(a_3, T.transpose(w3))
    h   = T.nnet.nnet.sigmoid(z_4)
    cost = T.sum(-y * T.log(h) - (1-y) * T.log(1-h))/m
    return cost

fc = computeCost(X, y, theta1, theta2, theta3)

def grad_desc(cost, theta):
    alpha = 0.1 #learning rate
    return theta - (alpha * T.grad(cost, wrt=theta))

cost = theano.function(inputs=[X, y], outputs=fc, updates=[
        (theta1, grad_desc(fc, theta1)),
        (theta2, grad_desc(fc, theta2)),
        (theta3, grad_desc(fc, theta3))])

cur_cost = 0        

for i in range(2000):
    for k in range(len(X_input)):
        x, y = X_input[k], y_input[k]
        x.shape = (1,195)
        y.shape = (1,75)
        cur_cost = cost(x,y)
    if i % 50 == 0: print('Cost: %s' % (cur_cost,))
        
