
import pygame

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

def sound_OHKO():
    sound_init()
    sounds_OHKO = pygame.mixer.Sound('sounds/OHKO.wav')
    sounds_OHKO.play()

def sound_encounter():
    sound_init()
    sounds_encounter = pygame.mixer.Sound('sounds/encounter.wav')
    sounds_encounter.play()

def sound_battle():
    sound_init()
    sounds_battle = pygame.mixer.Sound('sounds/battle.wav')
    sounds_battle.play(loops=-1)

def sound_hit():
    sound_init()
    sounds_hit = pygame.mixer.Sound('sounds/hit.wav')
    sounds_hit.play()

def sound_item():
    sound_init()
    sounds_item = pygame.mixer.Sound('sounds/item.wav')
    sounds_item.play()

def sound_ok():
    sound_init()
    sounds_ok = pygame.mixer.Sound('sounds/ok.wav')
    sounds_ok.play()

def sound_marchand():
    sound_init()
    sounds_marchand = pygame.mixer.Sound('sounds/marchand.wav')
    sounds_marchand.play()

def sound_shop():
    sound_init()
    sounds_shop = pygame.mixer.Sound('sounds/shop.wav')
    sounds_shop.play(loops=-1)

def sound_level_up():
    sound_init()
    sounds_level_up = pygame.mixer.Sound('sounds/level_up.wav')
    sounds_level_up.play()

def sound_fuite():
    sound_init()
    sounds_fuite = pygame.mixer.Sound('sounds/fuite.wav')
    sounds_fuite.play()

def sound_heal():
    sound_init()
    sounds_heal = pygame.mixer.Sound('sounds/heal.wav')
    sounds_heal.play()

def quit_pygame():
    pygame.mixer.quit()
    pygame.quit()