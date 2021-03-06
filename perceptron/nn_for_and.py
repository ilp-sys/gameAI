def calculate(input):
    global weights, bias
    activation = 0
    for i in range(2):
        activation += weights[i] * input[i]
    activation += bias
    if activation >= 0: #step function
        return 1
    else:
        return 0

def train_weights(X, y, l_rate, n_epoch):
    global weights, bias
    for epoch in range(n_epoch):
        sum_error = 0
        for row, target in zip(X,y):
            actual = calculate(row)
            error = target - actual
            bias = bias + l_rate * error
            sum_error += error**2
            for i in range(2):
                weights[i] = weights[i] + l_rate * error * row[i]
            print(weights, bias)
        print("epoch = %d>> l_rate = %3f, error= %3f" %(epoch, l_rate, sum_error))
    return weights

X = [[0,0], [0,1], [1,0], [1,1]]
y = [0,0,0,1]

weights = [0,0]
bias = 0

l_rate = 0.1
n_epoch = 5
weights = train_weights(X, y, l_rate, n_epoch)
print((weights, bias))