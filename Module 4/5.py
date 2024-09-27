import pyautogui

def draw_half_pyramid(height):
    screenWidth, screenHeight = pyautogui.size()
    block_width = screenWidth // height
    block_height = screenHeight // height
    start_x = screenWidth // 2 - (block_width * height) // 2
    start_y = screenHeight // 2 - (block_height * height) // 2

    for row in range(height):
        num_blocks = row + 1
        row_start_x = start_x + (height - num_blocks) // 2 * block_width
        row_start_y = start_y + row * block_height

        for col in range(num_blocks):
            block_x = row_start_x + col * block_width
            block_y = row_start_y
            pyautogui.drawRect(block_x, block_y, block_width, block_height)

# Prompt the user to enter the height of the pyramid
height = int(input("Enter the height of the pyramid: "))

# Draw the half pyramid
draw_half_pyramid(height)
