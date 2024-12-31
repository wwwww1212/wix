import cv2
import numpy as np
import pyautogui
import time

def capture_screen():
    
    screen = np.array(pyautogui.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    return screen

def find_color(screen, target_color, threshold=30):

    lower_bound = np.array([max(0, c - threshold) for c in target_color])
    upper_bound = np.array([min(255, c + threshold) for c in target_color])
    
    mask = cv2.inRange(screen, lower_bound, upper_bound)
    loc = np.where(mask > 0)
    
    if len(loc[0]) > 0:
        top_left = (loc[1][0], loc[0][0])
        return top_left
    else:
        return None

def process_color(target_color, threshold):

    screen = capture_screen()
    location = find_color(screen, target_color, threshold)
    
    if location:
        center_x, center_y = location
        print(f"Found color at: ({center_x}, {center_y})")
        pyautogui.moveTo(center_x, center_y)
        pyautogui.click()
    else:
        print("Color not found.")

def main():
    color1 = (72, 73, 226)  # 目标颜色1 (B, G, R)
    color2 = (76, 94, 241)  # 目标颜色2 (B, G, R)
    threshold = 0  # 颜色匹配的阈值

    while True:
        try:
            process_color(color1, threshold)
            process_color(color2, threshold)
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(0.1)

if __name__ == "__main__":
    main()
