## 넘파이와 리스트 처리 속도 비교


import numpy as np
import random
import time

## 배열의 크기
SIZE = 10000
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

## 2차원 리스트 생성
pythonList = [[random.randint(0, 255) for _ in range(SIZE)] for _ in range(SIZE)]

## 리스트 출력하기
start = time.time()
for i in range(SIZE) :
    for k in range(SIZE) :
        pythonList[i][k] = 255 - pythonList[i][k]
end = time.time()
print('## 리스트 처리 시간 : %10.2f 초' % (end - start))

## 넘파이 배열 처리
start = time.time()
numpyAry = 255 - numpyAry
end = time.time()
print('## 넘파이 처리 시간 : %10.2f 초' % (end - start))

## 리스트 처리 시간 :  9.45 초
## 넘파이 처리 시간 :  0.12 초

## 실행시 이와 같이 나타남
