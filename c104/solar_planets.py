import cv2 

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
             "Sol",
              (70,100),
             cv2.FONT_HERSHEY_COMPLEX,
              2,
             (0,0,255)
        )

cv2.putText(img,
             "Mercurio",
              (70,190),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Venus",
              (180,190),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Tierra",
              (280,180),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Marte",
              (380,190),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Jupiter",
              (440,150),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Saturno",
              (780,150),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Urano",
              (970,145),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )

cv2.putText(img,
             "Neptuno",
              (1110,150),
             cv2.FONT_HERSHEY_COMPLEX,
              .5,
             (255,255,255)
        )


cv2.imshow("etiqueta", img);
cv2.waitKey(0)  # Esperar hasta que se presione una tecla
cv2.destroyAllWindows()