#312-01 csv파일 불러오기
import pandas as pd
location = 'C:/Users/flutterday/Documents/카카오톡 받은 파일/yemoonsaBigdata/datasets/Part2/housing_data.csv'
data = pd.read_csv(location, header= None, sep=',')
col_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV', 'isHighValue']
data.columns = col_names

#312-02 head 함수
print(data.head())

#321-01 Shape 함수
print(data.shape)

#321-02 info 함수
print(data.info())

#321-03 describe 함수
print(data.describe())

#322-01 결측치 개수 확인
print(data.isnull().sum())

#322-02 결측치 비율 확인
print(data.isnull().sum()/data.shape[0])

#322-03 결측치 대체(중앙값)
data1 = data.copy()
med_val = data['CRIM'].median()
data1['CRIM'] = data1['CRIM'].fillna(med_val)

#322-04 결측치 제거
data = data.loc[data['CRIM'].notnull()]
print(data.describe())

#323-01 MEDV 변수 박스 플롯
import seaborn as sns
sns.boxplot(data['MEDV'])

#323-02 IQR 값 기준 이상치
Q1, Q3 = data['MEDV'].quantile([0.25, 0.75])
IQR = Q3 - Q1
upper_bound = Q3 + 1.5*IQR
lower_bound = Q1 - 1.5*IQR

print('outlier 범위 : %.2f 초과 또는 %.2f 미만' %(upper_bound, lower_bound))
print('outlier 개수 : %.0f' %len(data[(data['MEDV']>upper_bound)|(data['MEDV']<lower_bound)]))
print('outlier 비율 : %.2f' % (len(data[(data['MEDV']>upper_bound)|(data['MEDV']<lower_bound)])/len(data)))


#331-01 데이터 생성
df_r = data.drop(['isHighValue'], axis =1)

#331-02 변수 상관관계 확인
cols = ['MEDV', 'LSTAT', 'RM', 'CHAS', "RAD", "TAX"]
print(df_r[cols].corr())

#332-01 데이터 분할
from sklearn.model_selection import train_test_split
X_cols = ['LSTAT', "PTRATIO", 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM']
X = df_r[X_cols].values
y = df_r['MEDV'].values

X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y, test_size = 0.3, random_state = 123)

#332-02 데이터 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_r_scaled = scaler.fit_transform(X_train_r)
X_test_r_scaled = scaler.transform(X_test_r)

#332-03 선형 회귀 학습
from sklearn.linear_model import LinearRegression
model_lr = LinearRegression()
model_lr.fit(X_train_r_scaled, y_train_r)

print(model_lr.coef_)
print(model_lr.intercept_)

#332-07 랜덤포레스트 학습
from sklearn.ensemble import RandomForestRegressor
model_rfr = RandomForestRegressor(random_state=123)
model_rfr.fit(X_train_r_scaled, y_train_r)

#333-01 예측값 생성
y_pred_lr = model_lr.predict(X_test_r_scaled)
y_pred_rfr = model_rfr.predict(X_test_r_scaled)

#333-02 평가지표 계산
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error

print('선형 회귀 결과')
print('MAE : %.3f' %mean_absolute_error(y_test_r, y_pred_lr))
print('MSE : %.3f' %mean_squared_error(y_test_r, y_pred_lr))
print('MAPE : %.3f' %mean_absolute_percentage_error(y_test_r, y_pred_lr))

print('랜덤포레스트 결과')
print('MAE : %.3f' %mean_absolute_error(y_test_r, y_pred_rfr))
print('MSE : %.3f' %mean_squared_error(y_test_r, y_pred_rfr))
print('MAPE : %.3f' %mean_absolute_percentage_error(y_test_r, y_pred_rfr))

# 4. 분류 모델링
# 341-01 데이터 생성
df_c = data.drop(['MEDV'], axis=1)

#341-02 LSTAT 변수 박스 플롯
import seaborn as sns
sns.boxplot(x = 'isHighValue', y = 'LSTAT', data = df_c)

# (2) 분석 모형 구축
#342-01 데이터 분할
from sklearn.model_selection import train_test_split
X_cols = ['LSTAT', 'PTRATIO', 'TAX', 'AGE', 'NOX', 'INDUS', 'CRIM']
X = data[X_cols].values
y = data['isHighValue'].values

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X, y, test_size=0.3, random_state=123)

#342-02 데이터 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train_c_scaled = scaler.fit_transform(X_train_c)
X_test_c_scaled = scaler.transform(X_test_c)

#342-07 랜덤포레스트 학습
from sklearn.ensemble import RandomForestClassifier

model_rfc = RandomForestClassifier(random_state = 123)
model_rfc.fit(X_train_c_scaled, y_train_c)

#343-01 예측값 생성
y_pred_rfc = model_rfc.predict(X_test_c_scaled)

#343-02 평가 지표 계산
from sklearn.metrics import classification_report
print(classification_report(y_test_c, y_pred_rfc, labels = [0,1]))