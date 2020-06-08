from collections import deque
import numpy as np
import cv2
import time


class Painter(object):
    def __init__(self, img, start_point=(20, 20)):
        self.horizons_center = (0, 0)
        self.point_list = []
        self.line_list = []
        self.get_point_line(img, start_point)

    def add_text(self, img, text, point, size=0.5, color=(0, 0, 255)):
        cv2.putText(img, text, point, cv2.FONT_HERSHEY_COMPLEX, size, color, 1)
        return img

    def draw_a_circle(self, img, point, radius=3, color=(255, 0, 0), thickness=2):
        img = self.draw_a_point(img, point, radius, color, thickness)
        return img

    def draw_a_point(self, img, point, radius=3, color=(255, 0, 0), thickness=-4):
        cv2.circle(img, point, radius, color, thickness)
        return img

    def draw_all_point(self, img):
        for point in self.point_list:
            if point == self.horizons_center:
                img = self.draw_a_point(img, self.horizons_center, 6, (0, 0, 255))
                lable_point = (self.horizons_center[0] - 5, self.horizons_center[1] - 5)
                img = self.add_text(img, str(self.horizons_center), lable_point)
            else:
                img = self.draw_a_point(img, point)
        return img

    def draw_a_line(self, img, start_point, end_point, color=(0, 255, 0), thickness=1, lineType=4):
        cv2.line(img, start_point, end_point, color, thickness, lineType)
        return img

    def draw_all_line(self, img):
        for point in self.line_list:
            img = self.draw_a_line(img, point[0], point[1])
        return img

    def get_point_line(self, img, start_point):
        start_value = start_point[0]
        space = start_value
        img_x, img_y = img.shape[1], img.shape[0]
        self.horizons_center = (int(img_x / 2), int(img_y / 2))

        for x_point in range(start_value, img_x, space):
            for y_point in range(start_value, img_y, space):
                self.point_list.append((x_point, y_point))

        num_row = int((img_y - start_value) / space)
        num_column = int((img_x - start_value) / space)
        for j in range(1, num_column + 1):
            self.line_list.append(((j * space, start_value), (j * space, (img_y - space))))
        for i in range(1, num_row + 1):
            self.line_list.append(((start_value, i * space), ((img_x - space), i * space)))


class FindTarget(object):
    def __init__(self):
        self.redLower = np.array([156, 43, 46])  # 设定红色阈值，HSV空间
        self.redUpper = np.array([180, 255, 255])
        self.target_position = (0, 0)
        self.target_radius = 0
        cv2.namedWindow("camera", 1)
        self.camera = cv2.VideoCapture(0)

    def get_one_flame(self):
        ret, img = self.camera.read()
        return ret, img

    def start_find(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 转到HSV空间
        mask_red = cv2.inRange(hsv, self.redLower, self.redUpper)  # 根据阈值构建掩膜
        mask_red = cv2.erode(mask_red, None, iterations=2)  # 腐蚀操作
        mask_red = cv2.dilate(mask_red, None, iterations=2)  # 膨胀操作，其实先腐蚀再膨胀的效果是开运算，去除噪点
        cnts_red = cv2.findContours(mask_red.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  # 轮廓检测
        if len(cnts_red) > 0:
            c = max(cnts_red, key=cv2.contourArea)  # 找到面积最大的轮廓
            (red_x, red_y), self.target_radius = cv2.minEnclosingCircle(c)
            self.target_position = (int(red_x), int(red_y))
            return True, img
        return False, img

    def is_horizons_center(self, center):
        x_low, x_high = center[0] - 5, center[0] + 5
        y_low, y_high = center[1] - 5, center[1] + 5
        x_target, y_target = self.target_position[0], self.target_position[1]
        if x_low < x_target < x_high and y_low < y_target < y_high:
            return True
        return False

    def is_target_on_node(self, point_list):
        x_target, y_target = self.target_position[0], self.target_position[1]
        for point in point_list:
            if (point[0] - 3) < x_target < (point[0] + 3) and (point[1] - 3) < y_target < (point[1] + 3):
                return True
        return False

    def show_result(self, img):
        cv2.imshow('Frame', img)

    def is_exit(self):
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            return True
        return False

    def close(self):
        self.camera.release()  # 摄像头释放
        cv2.destroyAllWindows()  # 销毁所有窗口


if __name__ == '__main__':

    toFind = FindTarget()
    ret, flame = toFind.get_one_flame()

    if ret:
        painter = Painter(flame, (40, 40))
        while True:
            _, flame = toFind.get_one_flame()
            result, flame = toFind.start_find(flame)
            if result:
                flame = painter.draw_a_circle(flame, toFind.target_position, int(toFind.target_radius), (0, 255, 255))
                flame = painter.draw_a_point(flame, toFind.target_position, 5, (0, 255, 0))
                flame = painter.add_text(flame, str(toFind.target_position), toFind.target_position)
                if toFind.is_horizons_center(painter.horizons_center):
                    flame = painter.add_text(flame, 'arrive center point!', (30, 30), 1, (0, 0, 255))
                if toFind.is_target_on_node(painter.point_list):
                    flame = painter.add_text(flame, 'YES!', (550, 30), 1, (0, 0, 255))
                print('目标物体坐标:  ', toFind.target_position)
            flame = painter.draw_all_point(flame)
            flame = painter.draw_all_line(flame)

            toFind.show_result(flame)
            if toFind.is_exit():
                break
    else:
        print('No Camera')

    toFind.close()

