
import pygame
import threading
import winsound

def sound_init():
    pygame.init()
    pygame.mixer.init()

def sound_create():
    sound_init()
    sounds_create = pygame.mixer.Sound('sounds/create.wav')
    sounds_create.play(loops=-1)

def sound_bgm():
    sound_init()
    sounds_bgm = pygame.mixer.Sound('sounds/bgm2.wav')
    sounds_bgm.play(loops=-1)

def sound_win_fight():
    sound_init()
    sounds_win_fight = pygame.mixer.Sound('sounds/fight_win.wav')
    sounds_win_fight.play()

def sound_trap():
    sound_init()
    sounds_trap = pygame.mixer.Sound('sounds/trap.wav')
    sounds_trap.play()

def sound_startup():
    sound_init()
    sounds_startup = pygame.mixer.Sound('sounds/startup.wav')
    sounds_startup.play()

def sound_game_over():
    sound_init()
    sounds_game_over = pygame.mixer.Sound('sounds/game_over.wav')
    sounds_game_over.play()

def sound_chest_o():
    sound_init()
    sounds_chest_o = pygame.mixer.Sound('sounds/chest_o.wav')
    sounds_chest_o.play()

def sound_chest_c():
    sound_init()
    sounds_chest_c = pygame.mixer.Sound('sounds/chest_c.wav')
    sounds_chest_c.play()

def sound_enter():
    sound_init()
    sounds_enter = pygame.mixer.Sound('sounds/enter.wav')
    sounds_enter.play()

def quit_pygame():
    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    sound_init()
    sound_create()