# callback function

class Button:
    def __init__(self):
        self.click_count = 0

    def register_click(self, callback):
        def increment_count():
            self.click_count += 1

        increment_count()
        callback()

def click_handler():
    print("Button clicked!")

button = Button()
button.register_click(click_handler) 
print(button.click_count)
