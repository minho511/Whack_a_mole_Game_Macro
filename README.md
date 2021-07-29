# Whack-a-mole_Game_Macro

## 과정  
1. 게임선택
2. 사용된 이미지
3. 코드
4. 문제점


## 1. 게임선택
우연히 링크를 공유받아 해보게된 두더지잡기 게임
전형적인 두더지잡기 게임이며 약 1분동안의 게임시간동안 많은 두더지를 잡는것이 목표이다.  
**[게임링크](http://g.regogame.com/game/48/)**

## 2. 필요한 이미지 구하기
**이미지1**  
게임화면의 좌표를 구하기 위한 화면이미지  
<img width="180" alt="스크린샷 2021-07-29 오후 8 27 37" src="https://user-images.githubusercontent.com/57162448/127484535-d9349a4f-669c-4f34-a307-03d55cc9390c.png">
<img width="300" alt="ground" src="https://user-images.githubusercontent.com/57162448/127487281-5f31a44e-67df-426c-8678-e3dbd486aca0.png">  
왼쪽의 이미지가 실제 게임화면이지만 프로그램이 실행될때 필요한 부분은 **두더지가 나오는 일부영역**이다.  
(시작화면 ground.png)
**이미지2**  
두더지를 인식하기 위해 필요한 두더지 이미지  
실제 게임에서 등장하는 두더지는 아래 사진과 같지만  
<img width="80" src="http://g.regogame.com/game/48/res/game/diglett1.png">  
올라오는 두더지의 머리를 인식할때 점수가 더 좋았다.  
따라서 다음과 같은 사진을 사용하였다.  
<img width="80" alt="dig2" src="https://user-images.githubusercontent.com/57162448/127487832-806eeb8e-b760-412d-bc7b-9f911595794c.png">
![dag2](https://user-images.githubusercontent.com/57162448/127487850-3c053be7-32a7-4536-857d-4fc04c86e90d.png)

## 3. 코드
```python
import cv2 as cv
import numpy as np
import pyautogui
```
- **게임 시작화면이미지를 사용하여 스크린샷을 찍을 좌표를 찾는다**
```python
ground = pyautogui.locateOnScreen('ground.png',confidence = 0.2)
```
이때 locateOnScreen 매서드는 주어진 사진과 크기가 정확하게 같을때만 인식하기 때문에 창의 크기가 다르면 게임화면을 인식하지 못하는 문제가 있었다.
confidence = 0.2 매개변수값을 변경(기본값 1)하여 창의 크기가 다를때에도 인식 가능하도록 했다.
```python
img_dig_piece = cv.imread('img1.png', cv.IMREAD_GRAYSCALE)
img_dag_piece = cv.imread('img2.png', cv.IMREAD_GRAYSCALE)
h_dig, w_dig = img_dig_piece.shape[:2]
h_dag, w_dag = img_dag_piece.shape[:2]

input("엔터를 눌러서 시작 >> ")
cv.namedWindow("result")  
cv.moveWindow("result",0, 0)  
```

