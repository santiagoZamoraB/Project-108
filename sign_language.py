import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips = [8, 12, 16, 20]
thumb_tip = 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            # Acceder a los puntos de referencia por su posición
            lm_list=[]
            
            for lm_index in finger_tips:
                x,y = int(lm_list[tip].x*w, int(lm_list[tip].y*h))
                cv2.circle(img, (x,y), 15, (255,0,0), cv2.FILLED)

            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)
                finger_fold_status =[]
             # El código va aquí  
                if lm_list[tip].x < lm_list[tip-3].x:
                    cv2.circle(img, (x,y), 15,(0,255,0), cv2.FILLED)
                    finger_fold_status.append(True)
                else:
                    finger_fold_status.append(False)

                if all(finger_fold_status):
                    if lm_list[thumb_tip-1].y < lm_list[thumb_tip-2].y:
                        print("Me gusta")
                        cv2.putText(img, "Me gusta", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                    if lm_list[thumb_tip].y > lm_list[thumb_tip-1].y > lm_list[thumb_tip-2].y:
                        print("No me gusta")
                        cv2.putText(img, "No me gusta", (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255), 3)

            mp_draw.draw_landmarks(img, hand_landmark,
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2))
    

    cv2.imshow("Rastreo de manos", img)
    cv2.waitKey(1)
