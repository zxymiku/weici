from PIL import ImageGrab, Image
import pytesseract
import pygetwindow as gw
import difflib
import pyautogui
from sql import row

window_title = 'MuMu模拟器12'
def get_window_position(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if not window:
        raise Exception(f"Window with title '{window_title}' not found")
    win = window[0]
    return (win.left, win.top, win.right, win.bottom)

# (左上角x, 左上角y, 右下角x, 右下角y)
relative_coordinates = [
    (10, 10, 110, 110),
    (210, 210, 310, 310),
    (410, 410, 510, 510)
]

def capture_and_ocr(window_position, relative_coordinates):
    results = []
    for idx, coord in enumerate(relative_coordinates):
        abs_coord = (
            window_position[0] + coord[0],
            window_position[1] + coord[1],
            window_position[0] + coord[2],
            window_position[1] + coord[3]
        )
        img = ImageGrab.grab(bbox=abs_coord)
        img.save(f"screenshot_{idx}.png")
        text = pytesseract.image_to_string(img)
        results.append(text.strip())
    return results

def is_similar(str1, str2, threshold=0.8):
    similarity = difflib.SequenceMatcher(None, str1, str2).ratio()
    return similarity >= threshold

def compare_with_row(ocr_results, row_string):
    pos = None
    for idx, result in enumerate(ocr_results):
        if is_similar(result, row_string):
            pos = relative_coordinates[idx]
            break
    return pos

def click_position(window_position, relative_pos):
    abs_x = window_position[0] + (relative_pos[0] + relative_pos[2]) // 2
    abs_y = window_position[1] + (relative_pos[1] + relative_pos[3]) // 2
    pyautogui.click(abs_x, abs_y)

def main():
    window_position = get_window_position(window_title)
    row_string = row()
    ocr_results = capture_and_ocr(window_position, relative_coordinates)
    pos = compare_with_row(ocr_results, row_string)
    if pos:
        click_position(window_position, pos)
    else:
        print("没有匹配的坐标")

# 执行主函数
if __name__ == "__main__":
    main()

