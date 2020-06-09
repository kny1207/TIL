### day23_자전거 데이터 분석(EDA)



```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from scipy  import stats
```



#### 데이터 가져오기

```python
# bike sharing 데이터 가져오기

train = pd.read_csv("bike-sharing-demand/train.csv", parse_dates=["datetime"]) 
# parse_dates=["datetime"] 옵션주기
```



#### 데이터 확인

```python
train.info()
train.head()
```

![데이터확인](images/데이터확인.png)

* describe()

```python
# describe()
train.describe()

# 특정 컬럼 기술통계치 볼 수 있음
# 기온과 관련된 temp 컬럼에 대해서만 기술통계치 구하기
train.temp.describe()

"""
median(50%)과 mean값 비교하면서 이상치에 대해서 예측할 수 있음
: median과 mean이 비슷하면 이상치 많이 없다고 해석할 수도 있음
"""
```

![describe](images/describe.png)

* 결측값 확인

```python
# isnull로 결측값 확인
train.isnull()
# 각 column별 결측값 확인해봐야
train.isnull().sum() 

# 결측값 시각화해서 눈으로 한번에 확인하기
import missingno as msno
msno.matrix(train, figsize=(12,5))
```

![missingno](images/missingno.png)

#### 데이터 추출

```python
# 원하는 데이터 추출 

train['datetime']

# 데이터 추출해서 새로운 행 만들기
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second

train.head()
```

![원하는데이터추출_새로운행만들기](images/원하는데이터추출_새로운행만들기.png)

#### 시각화

> subplots함수 사용
> subplots: 여러 개의 plot을 출력할 때 사용
>
> subplots(nrows=2, ncols=3): 총 2행 3열 6개의 plot 출력하는 것
> fig(=figure): 그래프 6개로 이루어진 전체를 가리킴
> subplot(>plot) == axes(=axis x,y로 이루어짐) == 6군데 들어가 있는 작은 그래프

* 시각화1

```python
fig,((ax1, ax2, ax3),(ax4,ax5,ax6))=plt.subplots(nrows=2, ncols=3)
fig.set_size_inches(16,8)

# y='count'는 자전거 대여수
sns.barplot(data=train, x='year', y='count', ax=ax1)
sns.barplot(data=train, x='month', y='count', ax=ax2)
sns.barplot(data=train, x='day', y='count', ax=ax3)
sns.barplot(data=train, x='hour', y='count', ax=ax4)
sns.barplot(data=train, x='minute', y='count', ax=ax5)
sns.barplot(data=train, x='second', y='count', ax=ax6)
```

![시각화1](images/시각화1.png)

* 시각화 2

```python
# fig,axes=plt.subplots(nrows=2, ncols=2)로도 표현 가능
fig,axes=plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(16,8)

# boxplot으로 표현: 이상치 확인에 용이한 그래프
sns.boxplot(data=train, x='season', y='count', ax=axes[0][0])
sns.boxplot(data=train, x='workingday', y='count', ax=axes[0][1])  
sns.boxplot(data=train, orient='v', y='count', ax=axes[1][0]) # orient='v': 수직방향
sns.boxplot(data=train, x='hour', y='count', ax=axes[1][1])
```



* 새로운 행 만들기

```python
train['dayofweek'] = train['datetime'].dt.dayofweek
train.shape # (10886, 19) > 19개의 column으로

train['dayofweek'].unique()

# 각 요일별로 데이터 몇 건씩 있는지 출력: value_counts() 활용
train['dayofweek'].value_counts()
```

* 그래프 다양하게 그려서 시각화

```python
# fig,ax1 = plt.subplots(nrows=1)
# sns.pointplot(data=train, x='hour', y='count', ax=ax1)

fig,(ax1, ax2, ax3, ax4,ax5) = plt.subplots(nrows=5)
fig.set_size_inches(18,25)

sns.pointplot(data=train, x='hour', y='count', ax=ax1)

# hue 옵션, hue를 기준으로 주면 된다
# hue='workingday' 옵션 추가 > 근무일이냐 아니냐 나눠서 그래프 확인 가능
# 0이 workingday 아닌 날, 1이 workingday인 날
sns.pointplot(data=train, x='hour', y='count', hue='workingday', ax=ax2)

# ax3 추가, nrows=3으로 바꾼 후 hue='dayofweek' 옵션 추가
sns.pointplot(data=train, x='hour', y='count', hue='dayofweek', ax=ax3) # 0-4:출근/ 5,6: 주말

# ax4 추가, nrows=4로 변경
sns.pointplot(data=train, x='hour', y='count', hue='weather', ax=ax4)

# ax5 추가, nrows=5로 변경
sns.pointplot(data=train, x='hour', y='count', hue='season', ax=ax5)
```

![다양하게시각화](images/다양하게시각화.png)

* regplot: 선형성 확인 

> regplot: 선형성 확인 가능
> data에 선을 그린다 == 모델을 만든다는 것으로 데이터의 선형성 잘 나타내는 선(모델)이 데이터 잘 반영한 것
>
> - 데이터 값들 간 차이 적은 것이 선형성 잘 나타낸 그래프로 선 w(기울기)와 b(편향성) 변경
>
> * 가장 실제 데이터와 차의 제곱합이 최소인 그래프를 찾는 과정을 하게 된다.

```python
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)
fig.set_size_inches(12,5)
sns.regplot(x='temp', y='count', data=train, ax=ax1)
sns.regplot(x='windspeed', y='count', data=train, ax=ax2)
#> 0에 data들이 많이 붙어 있어 > 바람이 0 => 말이 안되는 것 > 잘 처리해야
sns.regplot(x='humidity', y='count', data=train, ax=ax3)
#> 습도와는 음의 상관관계를 보이는 추이가 보임
```

![선형화](images/선형화.png)





##### 연도, 월 행 추출하기

```python
# 연도별 평균 아닌 2011,2012 따로 분류해서 보고싶음

# 연도별 자전거 대여수 평균 출력

# 연도, 월 추출하기
def ym(mydt):
    return"{0}-{1}".format(mydt.year, mydt.month)
    
train['year_month'] = train['datetime'].apply(ym)
train[['datetime','year_month']]
```

![연도별행추출](images/연도별행추출.png)

* 시각화

```python

fig,axes=plt.subplots(nrows=1, ncols=1)
fig.set_size_inches(18,6)
sns.barplot(data=train, x='year_month', y='count', ax=axes)
```

![연도월별시각화](images/연도월별시각화.png)



#### 이상치 제거

```python
np.abs(train['count'] - train['count'].mean()) 
# 각각의 데이터에서 평균 빼고 절대값 구하기 > 평균과의 차이

train['count'].std() # 표준편차
#> 181.14445383028496

# 표준편차 3배
np.abs(train['count'] - train['count'].mean())  <= (train['count'].std()*3)
# > False인 값을 outlier로 볼 수 있다
trainWithoutOutliers = train[np.abs(train['count'] - train['count'].mean()) <= (train['count'].std()*3)]
print(train.shape)
print(trainWithoutOutliers.shape)

#> (10886, 20)
#> (10739, 20)
```



* 0값 많은 windspeed 값 예측해서 대체하기

```python
# train 풍속=0

train['windspeed'].mean()
#> 12.799395406945093

# windspped가 0인 경우
# train.loc[train['windspeed']==0, 'windspeed'] = train['windspeed'].mean()

# windspped가 0이 아닌 경우
# train.loc[train['windspeed']!=0, 'windspeed'] = train['windspeed'].mean()


# 풍속이 0인 것과 아닌 것을 구분해서 저장
trainWind0 =  train.loc[train['windspeed']==0]
trainWindnot0 = train.loc[train['windspeed']!=0]

print(trainWind0.shape)
print(trainWindnot0.shape)

#> (1313, 20)
#> (9573, 20)
```



#### RandomForest

> 머신러닝 랜덤포레스트로 풍속 예측

> decision tree(=의사결정 나무) 알고리즘 : 스무고개와 비슷

```python
# 랜덤포레스트 예측 만들어보기

from sklearn.ensemble import RandomForestClassifier

# 풍속이 0인 값 너무 많아 값이 0인 데이터 예측한 값으로 대체하기
# == data의 windspeed값이 0인 데이터를 랜던포레스트를 이용하여 예측한 값으로 대체
def predict_windspeed(data):
    # 풍속예측에 사용되는 변수(column)
    wCol = ['season','humidity','month','temp','weather','year','atemp']
    
    # 풍속을 0인 것과 아닌 것으로 구분
    dataWind0 = data.loc[data['windspeed']==0]
    dataWindNot0 = data.loc[data['windspeed']!=0]
    
    # 랜덤포레스트 분류기 생성
    # 객체 생성 후 rfModel로 이름 지어줌
    rfModel = RandomForestClassifier() # >분류기 객체 만들어짐
    
    # windspeed data가 string이어야 rf 가능
    dataWindNot0['windspeed'] = dataWindNot0['windspeed'].astype("str")
    
    # wCol에 따라 풍속 예측하고자 => 풍속결정짓는 wCol 일반화해주는 fit()
    # wCol -> 풍속 학습 -> 모델완성
    rfModel.fit(dataWindNot0[wCol],dataWindNot0['windspeed'])
    # windspeed를 알고자, windspeed값을 wCol에 있는 것들로 학습
    
    # 학습한 모델로 풍속 0에 대한 데이터 예측
    preValue = rfModel.predict(X=dataWind0[wCol]) # X=dataWind0[wCol]: 입력 데이터
    print(preValue)
    
    predictWind0 = dataWind0
    predictWindNot0 = dataWindNot0
    
    predictWind0['windspeed'] = preValue
    
    data = predictWindNot0.append(predictWind0)
    
    return data

print(predict_windspeed(train))
```

![랜덤포레스트 결과](images/랜덤포레스트 결과.png)