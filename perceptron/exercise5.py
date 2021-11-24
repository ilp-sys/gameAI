def calculate(input):
    global weights, bias
    activation = bias
    for i in range(2):
        activation += weights[i]*input[i]
    if activation >= 0:
        return 1
    else:
        return 0

def train_weights(X, y, l_rate, epoch):
    global weights, bias
    for epoch in range(n_epoch):
        sum_error = 0
        for row, target in zip(X, y):
            actual = calculate(row)
            error = target - actual
            bias = bias + l_rate * error
            sum_error += error**2
            for i in range(2):
                weights[i] = weights[i] + l_rate * error * row[i]
            print(weights, bias)
        print("epochNum=%d>> l_rate=%.3f, error=%.3f"%(epoch, l_rate, sum_error))
    return weights

X = [[0.1,1],[0.4,1],[0.7,0.7],[0.9,0.4],[0.1,0.7],[0.3,0.6],[0.5,0.2],[0.6,0.3]]
y = [1,1,1,1,0,0,0,0]

weights = [0,0]
bias  = 0

l_rate = 0.1
n_epoch = 20
weights = train_weights(X, y, l_rate, n_epoch)
print(weights, bias)




