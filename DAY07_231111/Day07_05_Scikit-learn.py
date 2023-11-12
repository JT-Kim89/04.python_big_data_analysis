#231-01 사이킷런 임포트
import sklearn
print(sklearn.__version__)

#234-01 붓꽃 데이터 세트 불러오기
from sklearn.datasets import load_iris
iris = load_iris()
print('붓꽃 데이터세트 타입 : ', type(iris))

keys = iris.keys()
print('붓꽃 데이터세트 키 : ', keys)

#234-02 붓꽃 데이터세트 키 출력
print('feature_names :')
print(iris.feature_names)
print('\ntarget_names :')
print(iris.target_names)
print('\ndata :')
print(iris.data)
print('\ntarget :')
print(iris.target)

#235-01 붓꽃 데이터 세트 훑어보기
import pandas as pd
iris_df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df.head(3))

#235-02 학습/테스트 데이터 세트 분할
from sklearn.model_selection import train_test_split
iris_data = iris.data
iris_label = iris.target
x_train, x_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size = 0.2, random_state = 11)

print('train dataset')
print('x_train dataset : ', len(x_train))
print('y_train dataset : ', len(y_train))

print('\ntest dataset')
print('x_test dataset : ', len(x_test))
print('y_test dataset : ', len(y_test))

#235-03 의사결정 트리 머신러닝 학습
from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier(random_state=11)
dt_clf.fit(x_train, y_train)

#235-04 의사결정 트리 머신러닝 테스트/평가
from sklearn.metrics import accuracy_score

pred = dt_clf.predict(x_test)
ac_score = accuracy_score(y_test, pred)
print('예측 정확도 : ', ac_score)

#236-01 레이블 인코딩
items = ['TV', '냉장고', '전자레인지', '컴퓨터', 'TV', '냉장고', '컴퓨터', '컴퓨터']
encoder = sklearn.preprocessing.LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
print('인코딩 변환값: ', labels)
print('인코딩 클래스: ', encoder.classes_)

#236-02 레이블 디코딩
origins = encoder.inverse_transform([0, 1, 2, 3, 0, 1, 3, 3])
print('디코딩 원본값 : ', origins)

#236-03 원-핫 인코딩
import numpy as np
labels = labels.reshape(-1,1)
oh_encoder = sklearn.preprocessing.OneHotEncoder()
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)

print('원-핫 인코딩 데이터')
print(oh_labels.toarray())
print('원-핫 인코딩 데이터 차원')
print(oh_labels.shape)

#236-04 판다스의 원-핫 인코딩
import pandas as pd
item_df = pd.DataFrame({'item' : items})
pd.get_dummies(item_df)

#236-05 스케일링 데이터 세트 훑어보기
iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data = iris_data, columns = iris.feature_names)

print('feature 들의 평균 값 : \n', iris_df.mean())
print('feature 들의 분산 값 : \n', iris_df.var())

#236-06 표준화
scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)
iris_df_scaled = pd.DataFrame(data = iris_scaled, columns = iris.feature_names)

print('feature 들의 평균 값 : \n', iris_df_scaled.mean())
print('feature 들의 분산 값 : \n', iris_df_scaled.var())

#236-07 최대-최소 정규화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)
iris_df_scaled = pd.DataFrame(data = iris_scaled, columns = iris.feature_names)

print('feature 들의 최소 값 : \n', iris_df_scaled.min())
print('feature 들의 최대 값 : \n', iris_df_scaled.max())

#238-08 스케일링 주의사항
from sklearn.preprocessing import MinMaxScaler
import numpy as np

train_array = np.arange(0,11).reshape(-1,1)
test_array = np.arange(0,6).reshape(-1,1)

scaler = MinMaxScaler()
scaler.fit(train_array)
train_scaled = scaler.transform(train_array)
print('원본 train_array 데이터 : ', np.round(train_array.reshape(-1), 2))
print('Scaled train_array 데이터 : ', np.round(train_scaled.reshape(-1),2))

#scaler.fit(test_array)
test_scaled = scaler.transform(test_array)
print('\n원본 test_array 데이터 : ', np.round(test_array.reshape(-1), 2))
print('Scaled test_array 데이터 : ', np.round(test_scaled.reshape(-1),2))
