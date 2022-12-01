import numpy as np
from scipy.optimize import curve_fit

def gaussian(x, height, centre, sigma):
    '''Generates Gaussian with given parameters'''
    return height * np.exp(-(np.power(x - centre, 2) / (2 * sigma ** 2)))

def FitGaussian(x,y,params=None, meth=None, lims=(-np.inf, np.inf)):
    fit,success=curve_fit(gaussian,x,y,p0=params, method=meth, bounds=lims)
    fit_err = np.sqrt(np.diag(success))
    return fit,fit_err