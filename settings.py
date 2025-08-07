from os.path import join
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
WINDOW_CENTER = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

IMAGES = {
    "star": join("images", "star.png"),
    "meteor": join("images", "meteor.png"),
    "laser": join("images", "laser.png"),
    "player": join("images", "player.png"),
    "invader": join("images", "invader.png")
}

ANIMATION = {
    "explosion": [join("images", "explosion", f"{i}.png") for i in range(21)]
}

FONT = join("images", "Oxanium-Bold.ttf")