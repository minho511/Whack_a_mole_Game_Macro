import cv2 as cv
import numpy as np
import pyautogui

ground = pyautogui.locateOnScreen('ground.png',confidence = 0.2)
img_dig_piece = cv.imread('img1.png', cv.IMREAD_GRAYSCALE)
img_dag_piece = cv.imread('img2.png', cv.IMREAD_GRAYSCALE)
h_dig, w_dig = img_dig_piece.shape[:2]
h_dag, w_dag = img_dag_piece.shape[:2]

input("엔터를 눌러서 시작>>")
cv.namedWindow("result")
cv.moveWindow("result",0, 0)
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

    pyautogui.click(point)
    pyautogui.click(point2)

    position = pyautogui.position()
    if position[0] < 500:
        print("finish!")
        exit()

    cv.imshow('result', img_frame)

    key = cv.waitKey(1)
    if key == 27:
        break

print("게임종료")