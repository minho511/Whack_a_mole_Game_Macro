# Whack-a-mole_Game_Macro

## 과정  
1. 게임선택
2. 코드 설명
3. 코드
4. 문제점


## 1. 게임선택
우연히 링크를 공유받아 해보게된 두더지잡기 게임
전형적인 두더지잡기 게임이며 약 1분동안의 게임시간동안 많은 두더지를 잡는것이 목표이다.  
**[게임링크](http://g.regogame.com/game/48/)**

## 2. 필요한 이미지 구하기
이미지1)  
게임화면의 좌표를 구하기 위한 시작화면   
<img width="180" alt="스크린샷 2021-07-29 오후 8 27 37" src="https://user-images.githubusercontent.com/57162448/127484535-d9349a4f-669c-4f34-a307-03d55cc9390c.png">  
위 시작화면에서 필요한 부분은 두더지가 나오는 영역이다.  
<img width="300" alt="ground" src="https://user-images.githubusercontent.com/57162448/127487281-5f31a44e-67df-426c-8678-e3dbd486aca0.png">

이미지2)
두더지를 인식하기 위해 필요한 두더지 이미지  
실제 게임에서 등장하는 두더지는 아래 사진과 같지만  
<img width="80" src="http://g.regogame.com/game/48/res/game/diglett1.png">  
올라오는 두더지의 머리를 인식할때 점수가 더 좋았다.  
따라서 다음과 같은 사진을 사용하였다.  
<img width="80" alt="dig2" src="https://user-images.githubusercontent.com/57162448/127487832-806eeb8e-b760-412d-bc7b-9f911595794c.png">
![dag2](https://user-images.githubusercontent.com/57162448/127487850-3c053be7-32a7-4536-857d-4fc04c86e90d.png)

## 3. 코드
