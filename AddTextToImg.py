import cv2;
import textwrap;

def put_text(img, text, x_value, y_value):
    font = cv2.FONT_HERSHEY_DUPLEX
    wrapped_text = textwrap.wrap(text, width=20)
    x, y = 200, 40
    font_size = 5
    font_thickness = 3

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 40
        y = y_value + i * gap
        #y = int((img.shape[0] + textsize[1]) / 2) + i * gap
        x = int((img.shape[1] - textsize[0]) / 2)
        cv2.putText(img, line, (x_value, y), font,
                    font_size,
                    (255,255,255),
                    font_thickness,
                    lineType = cv2.LINE_AA)


img = cv2.imread("img.jpg")
put_text(img, "Follow us on IG : @aadesh__lokhande", 150, 250)
put_text(img, "Aadesh", 150, 750)
cv2.imwrite("output.jpg", img)

