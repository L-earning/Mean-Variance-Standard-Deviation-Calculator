import numpy as np

def calculate(list):
    #output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix
    calculations = {}
    #errors
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(list).reshape(3,3)

    mean_a1= np.mean(matrix,axis=0).tolist()
    mean_a2 = np.mean(matrix,axis=1).tolist()
    mean_tot = np.mean(matrix).tolist()

    var_a1 = np.var(matrix,axis=0).tolist()
    var_a2= np.var(matrix,axis=1).tolist()
    var_tot= np.var(matrix).tolist()

    sd_a1 = np.std(matrix,axis=0).tolist()
    sd_a2 = np.std(matrix,axis=1).tolist()
    sd_tot = np.std(matrix).tolist()

    max_a1 = np.max(matrix,axis=0).tolist()
    max_a2 = np.max(matrix,axis=1).tolist()
    max_tot = np.max(matrix).tolist()

    min_a1 = np.min(matrix,axis=0).tolist()
    min_a2 = np.min(matrix,axis=1).tolist()
    min_tot = np.min(matrix).tolist()

    sum_rows = np.sum(matrix,axis=0).tolist()
    sum_cols = np.sum(matrix,axis=1).tolist()
    sum_elm = np.sum(matrix).tolist()

    calculations = {"mean":[mean_a1,mean_a2,mean_tot], "variance":[var_a1,var_a2,var_tot], "standard deviation":[sd_a1,sd_a2,sd_tot], "max":[max_a1,max_a2,max_tot], "min":[min_a1,min_a2,min_tot],"sum":[sum_rows,sum_cols,sum_elm] }
    

    #The values in the returned dictionary should be lists and not Numpy arrays
    return calculations
