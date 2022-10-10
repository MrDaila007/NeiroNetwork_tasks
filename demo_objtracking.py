import cv2, numpy as np

camera = cv2.VideoCapture(0)  # веб камера

while True:
    iSee = False     # флаг: был ли найден контур
    controlX = 0.0      # нормализованное отклонение цветного объекта от центра кадра в диапазоне [-1; 1]
    
    success, frame = camera.read()  # читаем кадр с камеры

    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    if success:     # если прочитали успешно
        height, width = frame.shape[0:2]    # получаем разрешение кадра
            
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    # переводим кадр из RGB в HSV
        #binary = cv2.inRange(hsv, lower_blue, upper_blue)  # пороговая обработка кадра (выделяем все синие)
        binary = cv2.inRange(hsv, (16, 60, 100), (32, 255, 255))  # пороговая обработка кадра (выделяем все желтое)
        #binary = cv2.inRange(hsv, (0, 0, 0), (255, 255, 35))  # пороговая обработка кадра (выделяем все черное)

        """
        # Чтобы выделить все красное необходимо произвести две пороговые обработки, т.к. тон красного цвета в hsv 
        # находится в начале и конце диапазона hue: [0; 180), а в openCV, хз почему, этот диапазон не закольцован.
        # поэтому выделяем красный цвет с одного и другого конца, а потом просто складываем обе битовые маски вместе
        
        bin1 = cv2.inRange(hsv, (0, 60, 70), (10, 255, 255)) # красный цвет с одного конца
        bin2 = cv2.inRange(hsv, (160, 60, 70), (179, 255, 255)) # красный цвет с другого конца
        binary = bin1 + bin2  # складываем битовые маски
        """
        roi = cv2.bitwise_and(frame, frame, mask=binary)    # за счет полученной маски можно выделить найденный объект из общего кадра

        contours, _ = cv2.findContours(binary, cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_NONE)  # получаем контуры выделенных областей 

        if len(contours) != 0:  # если найден хоть один контур

            cnt = contours[0]
            M = cv2.moments(cnt)
            #print (M)
            maxc1 = max(contours, key=cv2.contourArea)  # находим наибольший контур
            print(maxc1)
            maxc2 = contours[10]   # находим наибольший контур
            moments1 = cv2.moments(maxc1) # получаем моменты этого контура
            moments2 = cv2.moments(maxc2)  # получаем моменты этого контура
            """
            # moments["m00"] - нулевой момент соответствует площади контура в пикселях,
            # поэтому, если в битовой маске присутствуют шумы, можно вместо
            # if moments["m00"] != 0:  # использовать
                
            if moments["m00"] > 20: # тогда контуры с площадью меньше 20 пикселей не будут учитываться 
            """
            if moments1["m00"] > 20: #  контуры с площадью меньше 20 пикселей не будут учитываться
                cx1 = int(moments1["m10"] / moments1["m00"])  # находим координаты центра контура (найденного объекта) по x
                cy1 = int(moments1["m01"] / moments1["m00"])  # находим координаты центра контура (найденного объекта) по y

                iSee = True  # устанавливаем флаг, что контур найден
                controlX = 2 * (cx1 - width/2) / width   # находим отклонение найденного объекта от центра кадра и нормализуем его (приводим к диапазону [-1; 1])
                controlY = 2 * (cy1 - height / 2) / height ## находим отклонение найденного объекта от центра кадра и нормализуем его (приводим к диапазону [-1; 1])
        
                cv2.drawContours(frame, maxc1, -1, (0, 255, 0), 2)  # рисуем контур
                cv2.line(frame, (cx1, 0), (cx1, height), (0, 255, 0), 2)  # рисуем линию линию по x
                cv2.line(frame, (0, cy1), (width, cy1), (0, 255, 0), 2)  # линия по y

                if moments2["m00"] > 20:  # контуры с площадью меньше 20 пикселей не будут учитываться
                    cx2 = int(
                        moments2["m10"] / moments2["m00"])  # находим координаты центра контура (найденного объекта) по x
                    cy2 = int(
                        moments2["m01"] / moments2["m00"])  # находим координаты центра контура (найденного объекта) по y

                    iSee = True  # устанавливаем флаг, что контур найден
                    controlX = 2 * (cx2 - width / 2) / width  # находим отклонение найденного объекта от центра кадра и нормализуем его (приводим к диапазону [-1; 1])
                    controlY = 2 * (cy2 - height / 2) / width  ## находим отклонение найденного объекта от центра кадра и нормализуем его (приводим к диапазону [-1; 1])

                    cv2.drawContours(frame, maxc2, -1, (255, 0, 0), 2)  # рисуем контур
                    cv2.line(frame, (cx2, 0), (cx2, height), (255, 0, 0), 2)  # рисуем линию линию по x
                    cv2.line(frame, (0, cy2), (width, cy2), (255, 0, 0), 2)  # линия по y

        cv2.putText(frame, 'iSee: {};'.format(iSee), (width - 370, height - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA) # текст
        cv2.putText(frame, 'controlX: {:.2f}'.format(controlX), (width - 200, height - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA) # текст
        cv2.putText(frame, 'controlY: {:.2f}'.format(controlY), (width - 200, height - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)  # текст
                

        cv2.circle(frame, (width//2, height//2), radius=4, color=(0, 0, 255), thickness=-1)    # центр кадра
        cv2.imshow('frame', frame)  # выводим все кадры на экран
        cv2.imshow('binary', binary)
        cv2.imshow('roi', roi)
        
    if cv2.waitKey(1) == ord('q'):  # чтоб выйти надо нажать 'q' на клавиатуре
        break

camera.release()
cv2.destroyAllWindows()
