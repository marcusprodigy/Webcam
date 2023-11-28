import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(imgRGB)  # Corrigido para Hand.process()
    handspoint = results.multi_hand_landmarks
    h, w, _ = img.shape
    pontos = []
    if handspoint:
        for points in handspoint:
            # print(points)
            mpDraw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for id, cord in enumerate(points.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                cv2.putText(
                    img,
                    str(id),
                    (cx, cy),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 0, 0),
                    2,
                )
                pontos.append((cx, cy))
                # print(pontos)
        contador = 0

        if points:
            if (
                pontos[8][1] > pontos[5][1]
                and pontos[12][1] > pontos[9][1]
                and pontos[16][1] > pontos[13][1]
                and pontos[20][1] > pontos[17][1]
                and pontos[4][1] < pontos[5][1]
            ):
                print("A")
            elif (
                pontos[8][1] < pontos[7][1]
                and pontos[12][1] < pontos[11][1]
                and pontos[16][1] < pontos[15][1]
                and pontos[20][1] < pontos[19][1]
                and pontos[4][0] < pontos[1][0]
            ):
                print("B")
            elif (
                pontos[8][1] > pontos[6][1]
                and pontos[12][1] > pontos[10][1]
                and pontos[16][1] > pontos[14][1]
                and pontos[20][1] > pontos[18][1]
                and pontos[4][0] > pontos[1][0]
            ):
                print("C")
            elif (
                pontos[8][1] < pontos[7][1]
                and pontos[12][1] > pontos[11][1]
                and pontos[16][1] > pontos[15][1]
                and pontos[20][1] > pontos[19][1]
                and pontos[4][0] > pontos[1][0]
            ):
                print("D")
            elif (
                pontos[8][1] > pontos[6][1]
                and pontos[12][1] > pontos[10][1]
                and pontos[16][1] > pontos[14][1]
                and pontos[20][1] > pontos[18][1]
                and pontos[4][1] < pontos[2][1]
            ):
                print("E")
            elif (
                pontos[8][1] > pontos[6][1]
                and pontos[12][1] < pontos[11][1]
                and pontos[16][1] < pontos[15][1]
                and pontos[20][1] < pontos[19][1]
                and pontos[4][0] < pontos[5][1]
            ):
                print("F")
            elif (
                pontos[8][1] < pontos[7][1]
                and pontos[12][1] > pontos[11][1]
                and pontos[16][1] > pontos[15][1]
                and pontos[20][1] > pontos[19][1]
                and pontos[4][1] < pontos[2][1]
            ):
                print("g")

            else:
                print("nada")

        # print(contador)

    cv2.imshow("Imagem", img)
    cv2.waitKey(1)
