from pyray import *
x = 800
y = 450
radius = 100
init_window(x, y, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text("Hello world", 190, 200, 20, VIOLET)
    draw_circle(x // 2, y // 2, radius, PINK)
    end_drawing()
close_window()