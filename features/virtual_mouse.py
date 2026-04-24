def map_to_screen(x, y, frame_w, frame_h, screen_w, screen_h):
    screen_x = int(x * screen_w / frame_w)
    screen_y = int(y * screen_h / frame_h)
    return screen_x, screen_y