import scipy.stats as stats

# Z-value와 누적 확률 구하기
# 1. z-value의 확률 구하기
# norm.cdf(): z-value보다 작은 누적 확률을 구하는 함수
stats.norm.cdf(3) # z-value = 3

# 2. 확률에 해당하는 z-value 구하기
# norm.ppf(): 왼쪽부터 누적 확률에 해당하는 z-value 값 구하는 함수
stats.norm.ppf(0.9) # 확률 0.9에 해당하는 z-value


# T 분포
"""
정규분포와 유사
모평균의 추론과 가설검정에 사용됨.
샘플이 적으면 넓게 분포되고, 샘플이 많으면 좁게 분포됨.
샘플의 크기가 커질수록(~30) 표준정규분포에 가까워짐.
"""

# t-value와 누적 확률 구하기
# 1. t-value의 확률 구하기
# t.cdf(): 특정 자유도(degree of freedom)를 가진 t-value 보다 작은 값을 가질 확률을 산출하는 함수
stats.t.cdf(2.1, 29) # t-value = 2.1, df= 29

# 2. 확률의 t-value 구하기
# t.ppf(): 특정 자유도를 가지고 특정 확률을 가지는 지점의 t-value를 구하는 함수
stats.t.ppf(0.75, 29) # 0.75 확률을 가지는 지점의 t-value

# 3. critical t-value 구하기
# t.ppf()함수를 이용하여 a/2 - 0.025까지의 누적확률과 df=29에 해당하는 t-value 구하기
stats.t.ppf(1-0.025, 29)


# Computing z-score using default values
import numpy as np
a = np.array([0.8976,0.9989,0.5678,0.1234,0.7765,1,1.675,1.456])
stats.zscore(a)

# Computing z-score along specified axis using degrees of freedom
b = np.array([[0.1234,0.4567,0.7890,0.9876],
                     [0.6789,0.7890,0.9987,0.6657],
                     [0.2234,0.9987,0.3345,0.5567]])
stats.zscore(b, axis=1, ddof=1)


# Computing z-score using nan-policy
c = np.array([[0.1234,np.nan,0.7890,0.9876],
                     [0.6789,0.7890,0.9987,0.6657],
                     [np.nan,0.9987,0.3345,np.nan]])
stats.zscore(c,axis=1) # default = 'propagate'
stats.zscore(c,axis=1, nan_policy='raise')


# 신뢰구간 구하기
# 예제1) 표본크기 = 30, 표본평균 = 62.1, 표본표준편차 = 13.46
import math

# Specify sample mean(x_bar), sample std(s), sample size(n), confidence level
x_bar = 62.1
s = 13.46
n = 30
confidence_level = 0.95 # 95%의 신뢰구간

# Calculate alpha, degrees of freedom(df), the critical t-value, margin of error
alpha = (1-confidence_level)    # 오차율 (신뢰구간이 모수를 포함하지 않을 확률, 표본추출오차)
df = n-1
standard_error = s/math.sqrt(n)
critical_t = stats.t.ppf(1-alpha/2, df)     # t분포표의 29자유도, 꼬리면적 0.025 해당 값 = 2.045
margin_of_error = critical_t * standard_error

# Calculate the lower and upper bound of the confidence interval
lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

# print the results
print("Critical t-value: {:3f}".format(critical_t))
print("Margin of Error: {:3f}".format(margin_of_error))
print("Confidence Interval: [{:.3f},{:.3f}]".format(lower_bound, upper_bound))
print("The {:.1%} confidence interval for the population mean is:".format(confidence_level))
print("between {:.3f} and {:.3f}".format(lower_bound, upper_bound))

#t분포 기반 신뢰구간 (위 예제1을 한번에 계산)
stats.t.interval(confidence_level, df, x_bar, standard_error)

# 예제2)
#define sample data
data = [12, 12, 13, 13, 15, 16, 17, 22, 23, 25, 26, 27, 28, 28, 29]

#create 95% confidence interval for population mean wiehgt
conf_int = stats.t.interval(alpha=0.95, df=len(data)-1, loc=np.mean(data), scale=stats.sem(data))
print(round(conf_int[0],3), round(conf_int[1],3))

# 정규분포 기반 신뢰구간
stats.norm.interval(confidence_level, x_bar, standard_error) # standard_error = stats.sem(data)

# 예제3)
#define sample data
np.random.seed(0)
data2 = np.random.randint(10, 30, 50)

#create 95% confidence interval for population mean wiehgt
conf_int2 = stats.norm.interval(alpha=0.95, loc=np.mean(data2), scale=stats.sem(data2))
print(round(conf_int2[0],2), round(conf_int2[1],2))


# 가설검정
"""
절차:
 1. 조건 확인
    - Sample들이 random하게 선택되었는지 확인
    - mean value(정량적 데이터)
    - proportions(정성적 데이터)
 2. 귀무가설 및 대립(연구)가설 정의
 3. 유의수준(a) 설정
 4. 검정통계량(test statistic) 계산
 5. 결론
"""

# 모비율 가설 검정
# 비율의 검정통계량(test statistic) 구하기

# Specify the number of occurrences(x), sample size(n), proportion claimed in the null-hypothesis (p)
x = 10
n = 40 # 샘플 수
p = 0.2

# Calculate the sample proportion
p_hat = x/n

# Calculate and print the test statistic
print((p_hat - p) / (math.sqrt((p * (1-p))/(n))))



