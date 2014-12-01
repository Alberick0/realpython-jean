from numpy import arange, reshape, vstack, dot

first_matrix = arange(3,12)
first_matrix = first_matrix.reshape(3,3)
print first_matrix,'\n'

print 'The minimum is {minimum} and maximum is {maximum}\n'.format(minimum=first_matrix.min(), maximum=first_matrix.max())

second_matrix = first_matrix ** 2
print second_matrix, '\n'

third_matrix = vstack([first_matrix, second_matrix])
print third_matrix, '\n'

print dot(third_matrix, first_matrix), '\n'

third_matrix = third_matrix.reshape(3,3,2)
print third_matrix
