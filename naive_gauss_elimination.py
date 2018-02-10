
def example():
    c_matrix = [[2,1,3],\
                [4,4,7],\
                [2,5,9]]
    e_elem = [1,1,3]
    naive_gauss(c_matrix, e_elem)

def naive_gauss(coef_matrix, elim_elem):
    output_matrix = [0] * len(coef_matrix)
    for pivot_row in coef_matrix[:-1]:
        print('Pivot Row = {}'.format(pivot_row))
        for elim_row in coef_matrix[1:]:
            print('Elim Row = {}'.format(elim_row))
            print(coef_matrix[coef_matrix.index(elim_row)][coef_matrix.index(elim_row)])
    #         factor = coef_matrix[elim_row][coef_matrix.index(pivot_row)]/coef_matrix[coef_matrix.index(pivot_row)][coef_matrix.index(pivot_row)]
    #         for column in coef_matrix[elim_row]:
    #             coef_matrix[elim_row][column] -= factor * coef_matrix[pivot_row][column]
    #         elim_elem[elim_row] -= factor * elim_elem[pivot_row]
    # output_matrix[-1] = elim_elem[-1] / coef_matrix[-1][-1]
    # for sol_row in coef_matrix[:-0:-1]:
    #     total = 0
    #     for elimination in elim_elem[1::-1]:
    #         total += coef_matrix[sol_row][elimination] * elim_elem[elimination]
    #     output_matrix[sol_row] = elim_elem[sol_row] - total / coef_matrix[sol_row][sol_row]
    # print(output_matrix)

example()