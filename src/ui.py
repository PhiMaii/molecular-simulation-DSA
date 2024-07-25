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

        # -------------------------------- temperature ------------------------------- #
        self.slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 20), (config.MENU_WIDTH - 100, 30)),
            text="Temperature",
            manager=self.manager
        )
        self.temperature_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 50), (config.MENU_WIDTH - 150, 30)),
            start_value=1.0,
            value_range=(0.1, 10.0),
            manager=self.manager
        )

        self.reset_temp = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50 + config.MENU_WIDTH - 135, 50), (30, 30)),
            text='',
            manager=self.manager
        )

        # --------------------------------- ball size -------------------------------- #
        self.ball_size_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 100), (config.MENU_WIDTH - 100, 30)),
            text="Ball size: ",
            manager=self.manager
        )
        self.ball_size_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 130), (config.MENU_WIDTH - 150, 30)),
            start_value=7.0,
            value_range=(2.0, 30.0),
            manager=self.manager
        )
        self.reset_size = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50 + config.MENU_WIDTH - 135, 130), (30, 30)),
            text='',
            manager=self.manager
        )

        # --------------------------------- show vels -------------------------------- #
        self.show_vectors = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 200), (config.MENU_WIDTH - 100, 40)),
            text="Show velocities",
            manager=self.manager
        )

        # ----------------------------------- pause ---------------------------------- #
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 250), (config.MENU_WIDTH - 100, 40)),
            text='Pause',
            manager=self.manager
        )
        
        # ----------------------------------- reset ---------------------------------- #
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 300), (config.MENU_WIDTH - 100, 40)),
            text="Reset",
            manager=self.manager
        )


        # --------------------------------- max speed -------------------------------- #
        self.max_speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 400), (config.MENU_WIDTH - 100, 30)),
            text='Max Particle Speed: ',
            manager=self.manager,   
        )

        # --------------------------------- min speed -------------------------------- #
        self.min_speed_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 420), (config.MENU_WIDTH - 100, 80)),
            text='Min Particle Speed: ',
            manager=self.manager,   
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

                # self.max_speed_label.set_text("0")
                # self.min_speed_label.set_text("0")

            elif event.ui_element == self.show_vectors:
                config.show_vels = not config.show_vels

            elif event.ui_element == self.reset_size:
                self.ball_size_slider.set_current_value(7.0)

            elif event.ui_element == self.reset_temp:
                self.temperature_slider.set_current_value(1.0)

        

        config.ball_size = self.ball_size_slider.current_value
        config.temperature = self.temperature_slider.current_value


    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, screen):
        self.manager.draw_ui(screen)