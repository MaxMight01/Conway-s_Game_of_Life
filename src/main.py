import pygame
import os
import utils

pygame.init()

#Opening the `parameters.json` file.
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(root_dir, 'parameters.json')
params = utils.load_parameters(config_file_path)

#Screen resolution.
ratio_w, ratio_h = map(int, params["aspect_ratio"].split("-"))
screen_width, screen_height = utils.calculate_screen_dimensions(ratio_w, ratio_h)

#Screen setup and caption.
screen = utils.setup_screen_and_caption(screen_width, screen_height, params["caption"])

#Colors.
c_DEAD = params["colors"]["dead"]
c_LIVE = params["colors"]["live"]

#fps and timer.
fps = params["fps"]
timer = pygame.time.Clock()


#Main loop.
running = True
while running:
    timer.tick(fps)
    screen.fill(c_DEAD)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()