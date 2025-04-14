import pygame
from game.states.menu_state import MenuState
from game.states.play_state import PlayState
from game.states.game_over_state import GameOverState
from game.states.instructions_state import InstructionsState

class GameManager:
    
    def __init__(self, screen):
        self.screen = screen
        self.states = {}
        self.current_state = None
        
        self.init_states()
        
        self.change_state('menu')
    
    def init_states(self):
        self.states['menu'] = MenuState(self)
        self.states['play'] = PlayState(self)
        self.states['game_over'] = GameOverState(self)
        self.states['instructions'] = InstructionsState(self)
    
    def change_state(self, state_name):
        if state_name in self.states:
            self.current_state = self.states[state_name]
            self.current_state.enter()
    
    def handle_event(self, event):
        if self.current_state:
            self.current_state.handle_event(event)
    
    def update(self):
        if self.current_state:
            self.current_state.update()
    
    def render(self):
        if self.current_state:
            self.current_state.render(self.screen)