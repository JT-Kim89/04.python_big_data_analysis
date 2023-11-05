import numpy as np
a = np.arange(1, 8, 2).reshape((2,2)) # [[1, 3], [5, 7]]
print(a)
#sum : Sum of array elements over a given axis.
np.sum(a) # 1 + 2 + 3 + 4 = 10
np.sum(a, axis=0) # [1 + 3], [2 + 4]
np.sum(a, axis=1) # [1 + 2], [3 + 4]

#max: Return the maximum of an array or maximum along an axis.
np.max(a) # 1 < 2 < 3 < 4
np.max(a, axis=0) # [1 < 3], [2 < 4]
np.max(a, axis=1) # [1 < 2], [3 < 4]

#min: Return the minimum of an array or minimum along an axis.
np.min(a) # 1 < 2 < 3 < 4
np.min(a, axis=0) # [1 < 3], [2 < 4]
np.min(a, axis=1) # [1 < 2], [3 < 4]

#ptp(peak to peak): Range of values (maximum - minimum) along an axis.
c = np.arange(1,18, 2).reshape((3,3)) # [[1, 3, 5], [7, 9, 11], [13, 15, 17]]
print(c)
np.ptp(c) # 17 - 1 = 16
np.ptp(c, axis=0) # [7 - 1], [8 - 2], [9 - 3]
np.ptp(c, axis=1) # [3 - 1], [6 - 4], [9 - 7]

"""
#percentile:Compute the q-th percentile of the data along the specified axis.
                 Returns the q-th percentile(s) of the array elements.
"""
np.percentile(c, 50)
np.percentile(c, 50, axis = 0)
np.percentile(c, 50, axis = 1)

#quantile: Compute the q-th quantile of the data along the specified axis.
np.quantile(c, 0.5)
np.quantile(c, 0.5, axis = 0)
np.quantile(c, 0.5, axis = 1)

"""
median: Compute the median along the specified axis.
             Returns the median of the array elements.
             -> percentile 50 = quantile 0.5 = median
"""
np.median(c)
np.median(c, axis = 0)
np.median(c, axis = 1)

#average: Compute the weighted average along the specified axis.
np.average(c)
np.average(c, axis=0)
np.average(c, axis=0, weights=[0.5, 0.2, 0.3])

"""
mean: Compute the arithmetic mean along the specified axis.
          Returns the average of the array elements. 
          The average is taken over the flattened array by default, 
          otherwise over the specified axis. 
          float64 intermediate and return values are used for integer inputs.
"""
np.mean(c)
np.mean(c, axis=0)
np.mean(c, axis=1)

"""
std: Compute the standard deviation along the specified axis.
Returns the standard deviation, a measure of the spread of a distribution, of the array elements. 
The standard deviation is computed for the flattened array by default, 
otherwise over the specified axis.
"""
np.std(c)
np.std(c, axis=0)
np.std(c, axis=1)

"""
var: Compute the variance along the specified axis.
Returns the variance of the array elements, a measure of the spread of a distribution.
The variance is computed for the flattened array by default, otherwise over the specified axis.
"""
np.var(c)
np.var(c, axis=0)
np.var(c, axis=1)

#corrcoef(상관관계계수): Return Pearson product-moment correlation coefficients.
np.corrcoef(c)

#cov(공분산): Estimate a covariance matrix, given data and weights.
np.cov(c)


# NaN 처리 (0 또는 제외하여 계산)
"""
nansum: Return the sum of array elements over a given axis
              treating Not a Numbers (NaNs) as zero.
              -> Nan = 0 처리 후 합
nanmax: Return the maximum of an array or maximum along an axis,
              ignoring any NaNs.
              When all-NaN slices are encountered a RuntimeWarning is raised
              and NaN is returned for that slice.
nanmin: Return minimum of an array or minimum along an axis,
             ignoring any NaNs.
             When all-NaN slices are encountered a RuntimeWarning is raised 
             and Nan is returned for that slice.
nanpercentile: Compute the qth percentile of the data along the specified axis,
                      while ignoring nan values.
                      Returns the qth percentile(s) of the array elements.
"""
b = a.astype(float)
b[1][1] = np.nan
np.nansum(b) # 1 + 2 + 3 + 0 = 6
np.sum(b) # nan

np.nanmax(b) #  1 < 2 < 3
np.nanmax(b, axis=0) # [1 < 3], [2]
np.nanmax(b, axis=1) # [1 < 2], [3]

np.nanmin(b) #  1 > 2 > 3
np.nanmin(b, axis=0) # [1 < 3], [2]
np.nanmin(b, axis=1) # [1 < 2], [3]

d = c.astype(float)
d[2][2] = np.nan
np.nanpercentile(d, 50) # 1 ~ 8 -> (1+8)/2 = 4.5
np.nanpercentile(d, 50, axis=0)
np.nanpercentile(d, 50, axis=1)

np.nanquantile(d, 0.5) # 1 ~ 8 -> (1+8)/2 = 4.5
np.nanquantile(d, 0.5, axis=0)
np.nanquantile(d, 0.5, axis=1)

np.nanmedian(d) # 1 ~ 8 -> (1+8)/2 = 4.5
np.nanmedian(d, axis=0)
np.nanmedian(d, axis=1)

np.nanmean(d) #
np.nanmean(d, axis=0)
np.nanmean(d, axis=1)

np.nanstd(d)
np.nanstd(d, axis=0)
np.nanstd(d, axis=1)

np.nanvar(d)
np.nanvar(d, axis=0)
np.nanvar(d, axis=1)
