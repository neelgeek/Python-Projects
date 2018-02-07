from statistics  import mean
import  numpy as np
import matplotlib.pyplot as plt

xs =np.array([1,2,3,4,5,6],dtype=np.float64)
ys= np.array([5,4,6,5,6,7],dtype=np.float64)


def best_fit_slope():
    num =  (mean(xs)*mean(ys))-mean(xs*ys)
    denom = (mean(xs)*mean(xs))- mean(xs*xs)
    m = num/denom

    c = mean(ys)-(m*mean(xs))

    return m,c

def squared_error(y_orig,y_line):
    return sum(((y_orig-y_line)**2))

def  coeff_dete(y_orig,y_line):
    y_mean_line  = [mean(y_orig) for y in y_orig]
    sq_err_regr =  squared_error(y_orig,y_line)
    sq_err_y_mean = squared_error(y_orig,y_mean_line)
    return 1 - (sq_err_regr/sq_err_y_mean)


m,c= best_fit_slope()

line = [(m*x)+c for x in xs]

print(coeff_dete(ys,line))


plt.scatter(xs,ys)
plt.plot(xs,line)
plt.show()

