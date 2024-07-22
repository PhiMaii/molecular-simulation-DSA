import pygame
import pygame_gui
import pygame_gui.ui_manager

import config
import utils

class GUI:
    def __init__(self, manager: pygame_gui.ui_manager):
        self.manager = manager
        self.create_elements()

    def create_elements(self):
        print("created elements")

        # Slider
        self.slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 20), (config.MENU_WIDTH - 100, 30)),
            text="Temperature",
            manager=self.manager
        )
        self.temperature_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 50), (config.MENU_WIDTH - 100, 50)),
            start_value=1.0,
            value_range=(0.1, 10.0),
            manager=self.manager
        )

        # Pause
        self.pause_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 220), (config.MENU_WIDTH - 100, 30)),
            text='Pause/Reset',
            manager=self.manager
        )
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 250), (config.MENU_WIDTH - 100, 40)),
            text='Pause',
            manager=self.manager
        )
        # Reset button
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 300), (config.MENU_WIDTH - 100, 40)),
            text="Reset",
            manager=self.manager
        )

        # particle details

        self.max_speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 400), (config.MENU_WIDTH - 100, 30)),
            text='Max Particle Speed: ',
            manager=self.manager,   
        )

        self.min_speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 440), (config.MENU_WIDTH - 100, 80)),
            text='Min Particle Speed: ',
            manager=self.manager,   
        )

        # ball size
        self.particle_size = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 100), (config.MENU_WIDTH - 100, 30)),
            start_value=5.0,
            value_range=(1, 25),
            manager=self.manager
        )

    def process_events(self, event:pygame_gui.elements):
        self.manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            if event.ui_element == self.pause_button:
                config.paused = not config.paused
                print(config.paused)
                self.pause_button.set_text('Resume' if config.paused else 'Pause') 
                # self.pause_button.set_text

            elif event.ui_element == self.reset_button:
                from main import balls
                balls.clear()
                balls.extend(utils.generateGasParticles())

                self.max_speed_label.set_text("fasfd")
                self.min_speed_label.set_text("fasdf")



    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, screen):
        self.manager.draw_ui(screen)