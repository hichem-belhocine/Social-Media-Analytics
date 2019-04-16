import numpy


def matrix_factorization(R, U, V, K, max_iter=5000, alpha=0.0002, lambda_=0.02):
    '''
    :param R: user(row)-item(column) matrix. R similar to UxV^T
    :param U: |user| x k matrix. Each row of U represents the associations between a user and the features
    :param V: |item| x k matrix. Each row of V represents the associations between an item and the features
    :param K: number of features
    :param max_iter: number of iterations
    :param alpha: learning rate
    :param lambda_: regularization term for U and V
    :return: updated matrices U and V
    '''

    for current_iter in range(max_iter):
        for i in range(len(R)):  # R rows iterator
            for j in range(len(R[i])):  # R column iterator
                if R[i][j] > 0:  # indicator function
                    for k in range(K):
                        U_derivative = -((R[i][j] - numpy.dot(U[i, :], V[j, :])) * V[j][k]) + lambda_ * U[i][k]
                        V_derivative = -((R[i][j] - numpy.dot(U[i, :], V[j, :])) * U[i][k]) + lambda_ * V[j][k]

                        U[i][k] = U[i][k] - alpha * U_derivative
                        V[j][k] = V[j][k] - alpha * V_derivative
                        
        error = 0
        counter = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    error = error + 0.5 * pow(R[i][j] - numpy.dot(U[i, :], V[j, :]), 2) + (lambda_ / 2) * pow(numpy.linalg.norm(U[i, :]), 2) + (lambda_ / 2) * pow(numpy.linalg.norm(V[j, :]), 2)
                    
			        
                    counter = counter + 1

        average_error = error / counter
        print("{} iteration: average error {}".format(current_iter + 1, average_error))

	    
        if average_error < 0.4:
            break

    return U, V
       


def main():
    R_observed = [
        [4, 4, 5, 3, 5],
        [5, 5, 3, 0, 4],
        [5, 0, 2, 5, 3],
        [5, 4, 3, 4, 0],
        [4, 3, 0, 3, 5],
        [4, 5, 4, 5, 5],
    ]

    R_observed = numpy.array(R_observed)

    rows_number = len(R_observed)  # number of rows (users)
    colums_number = len(R_observed[0])  # number of columns (items)
    K = 3

    # how to obtain U and V: initialize the two matrices with some values, calculate how 'different' their product is to r, and then try to minimize this difference iteratively (gradient descent).
    U = numpy.random.rand(rows_number, K)
    V = numpy.random.rand(colums_number, K)

    new_U, new_V = matrix_factorization(R_observed, U, V, K)
    R_predicted = numpy.dot(new_U, new_V.T)

    print(R_predicted)


if __name__ == "__main__":
    main()
