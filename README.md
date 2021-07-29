# Whack-a-mole_Game_Macro

## 과정  
1. 게임선택
2. 사용된 이미지
3. 코드
4. 
5. 문제점


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

ground = pyautogui.locateOnScreen('ground.png',confidence = 0.2)
```
> locateOnScreen 매서드는 주어진 사진과 크기가 정확하게 같을때만 인식하기 때문에 창의 크기가 다르면 게임화면을 인식하지 못하는 문제가 있었다.
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
> cv.moveWindow("result",0,0) 의 맨 오른쪽 두 0 좌표값으로 두더지 인식 여부를 확인 할 수 있는 창의 좌표를 정할 수 있다.
```python
while True:
    pic = pyautogui.screenshot(region=ground)
    img_frame = np.array(pic)
    img_frame = cv.cvtColor(img_frame, cv.COLOR_RGB2GRAY)
    meth = 'cv.TM_CCOEFF'
    method = eval(meth)

    res_dig = cv.matchTemplate(img_dig_piece, img_frame, method)
    res_dag = cv.matchTemplate(img_dag_piece, img_frame, method)

    min_val_d, max_val_d, min_loc_d, max_loc_d = cv.minMaxLoc(res_dig)
    min_val_da, max_val_da, min_loc_da, max_loc_da = cv.minMaxLoc(res_dag)

    top_left_d = max_loc_d
    top_left_da = max_loc_da

    bottom_right_d = (top_left_d[0] + w_dig, top_left_d[1] + h_dig)
    bottom_right_da = (top_left_da[0] + w_dag, top_left_da[1] + h_dag)

    cv.rectangle(img_frame, top_left_d, bottom_right_d, (0, 255, 0), 2)
    cv.rectangle(img_frame, top_left_da, bottom_right_da, (0, 255, 0), 2)
    # 비율을 고려하여 좌표계산
    point = (ground[0]//2+(top_left_d[0] + w_dig//2)//2,ground[1]//2+(top_left_d[1]+h_dig//2)//2)
    point2 = (ground[0]//2+(top_left_da[0] + w_dag//2)//2,ground[1]//2+(top_left_da[1]+h_dag//2)//2)
```
> 계산된 두더지의 좌표는 cv2모듈 창에서의 좌표이므로 창에서의 상대적인 두더지의 위치를 이용하여 게임화면에서의 두더지위치를 계산한다. 
```python
    pyautogui.click(point)  # 두더지를 클릭
    pyautogui.click(point2)
```
```python
    position = pyautogui.position()
    if position[0] < 500:
        print("finish!")
        exit()
```
> 프로그램을 실행 중간에 강제종료를 하기위한 방법으로 마우스를 화면의 왼쪽으로 움직였을때 종료되도록 하였다. 
> 여기서 position[0]는 마우스의 x좌표를 의미하므로 500과 부등호의 방향을 수정하여 강제종료를 위한 커서 위치를 설정할 수 있다.
```python
    cv.imshow('result', img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break

print("게임종료")
```

## 결과
## 문제점
- 선택한 게임이 다른곳을 눌렀을 때 감점되는 방식이 아니어서 단순하게 만들 수 있었지만 감점이 있는 게임이라면 추가적인 논리가 필요하다.
- 게임종료를 판단하고 프로그램을 종료하기 위해 게임종료화면 이미지를 사용하여 종료순간을 포착하려고 하였으나 루프를 도는 속도가 느려져 게임점수가 많이 떨어지게 되는 문제가 발생하였다. **게임종료를 판단하는 로직을 추가해야한다.**
