import cv2

class Sketcher:
    def __init__(self, name, dests, color_func):
        self.name = name
        self.dests = dests
        self.color_func = color_func
        self.show()
        cv2.setMouseCallback(self.name, self.on_mouse)
    def show(self):
        cv2.imshow(self.name, self.dests[0])
        cv2.imshow(self.name+':mask',self.dests[1])
    def on_mouse(self, event, x, y , flags, param):
        if event == cv2.EVENT_LBuTTONDOWN \
            and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.color_func()):
                cv2.line(dst, (x,y),(x,y),color,10)
            self.show()




