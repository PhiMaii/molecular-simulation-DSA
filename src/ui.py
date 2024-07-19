import pygame
import pygame_gui
import pygame_gui.ui_manager

import config

class GUI:
    def __init__(self, manager: pygame_gui.ui_manager):
        self.manager = manager
        self.create_elements()

    def create_elements(self):
        print("created elements")
        # Slider
        self.slider_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 20), (config.MENU_WIDTH - 100, 30)),
            text="Slider",
            manager=self.manager
        )
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 50), (config.MENU_WIDTH - 100, 50)),
            start_value=1.0,
            value_range=(0.1, 10.0),
            manager=self.manager
        )


        label_1 = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 220), (config.MENU_WIDTH - 100, 30)),
        text='Checkbutton',
        manager=self.manager
        )
        self.checkbutton_label = label_1

        self.button_1 = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((config.SIMULATION_WIDTH + 50, 250), (config.MENU_WIDTH - 100, 40)),
        text='Checkbutton',
        manager=self.manager
        )

    def process_events(self, event):
        self.manager.process_events(event)

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button_1:
                print('Hello World!')


    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, screen):
        self.manager.draw_ui(screen)