from pynput import mouse
import keyboard

click_positions = []

def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        click_positions.append((x, y))
        print(f"Clicked at position: {x}, {y}")
        if len(click_positions) == 2:

            return False

def start_listening():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


# 主函数
def main():
    print("Press F2 to start listening for mouse clicks.")

    while True:
        if keyboard.is_pressed('F2'):
            start_listening()
            if len(click_positions) == 2:
                first_click, second_click = click_positions
                relative_x = second_click[0] - first_click[0]
                relative_y = second_click[1] - first_click[1]
                print(f"Relative coordinates from first to second click: {relative_x}, {relative_y}")
                click_positions.clear()
            else:
                print("Not enough clicks to determine relative coordinates.")
            break


if __name__ == "__main__":
    main()
