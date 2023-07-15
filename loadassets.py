import pygame
from pygame import mixer
import datetime


class LoadAssets:
    def __init__(self):
        self.title_font = pygame.font.Font("assets/Milky Mania.ttf", 30)
        self.date_font = pygame.font.Font("assets/Milky Mania.ttf", 20)
        self.mixer = mixer
        self.current_date = datetime.datetime.now()
        self.formatted_date = self.current_date.strftime("%B %d, %Y")
        self.enlarge_scale = 1.2
        self.mood_desc = {
            1: "hehe (happy)",
            2: "huhu (sad)",
            3: "asdfghjkl (anxious)",
            4: "hAaa (tired)",
            5: "gege (calm)",
            6: "haayy (bored)",
            7: "grr (angry)",
            8: "eww (disgusted)",
            9: "hihi (excited)"
        }
        self.mood_quotes = {
            1: "Choose happiness and let your radiant spirit brighten the world.",
            2: "Remember, tough times don't last forever. You're stronger than you think.",
            3: "Take a deep breath. You're safe, and everything will be okay.",
            4: "Rest and recharge. You deserve the peace that comes with relaxation.",
            5: "Find calmness in the present moment and let it soothe your soul.",
            6: "Embrace the simple joys that bring warmth and contentment to your heart.",
            7: "Release your anger and choose forgiveness for your own inner peace.",
            8: "Allow yourself to let go of disgust and cultivate compassion instead.",
            9: "Embrace the excitement of new possibilities and let it inspire your dreams."
        }
        self.bg_surf = None
        self.add_button_surf = None
        self.mood_list = []
        self.back_button_surf = None
        self.home_button_surf = None
        self.fwd_button_surf = None
        self.bk_button_surf = None
        self.next_button_surf = None
        self.prev_button_surf = None
        self.text_box_surf = None
        self.click_sound_swoosh = None
        self.click_sound_click = None
        self.click_sound_pop = None
        self.click_sound_powerup = None
        self.click_sound_success = None
        self.typing_sound = None
        self.cal_text_surf = None
        self.add_mood_text_surf = None
        self.curr_date_surf = None
        self.mood_desc_surf = []
        self.mood_quotes_surf = []
        self.selected_mood_text_surf = None
        self.past_mood_text_surf = None
        self.placeholder_surf = None
        self.enter_text_button_surf = None
        self.wback_text_button_surf = None
        self.mood_save_text_surf = None
        self.error_text = None
        self.add_button_rect = None
        self.back_button_rect = None
        self.home_button_rect = None
        self.fwd_button_rect = None
        self.bk_button_rect = None
        self.text_box_rect = None
        self.next_button_rect = None
        self.prev_button_rect = None
        self.text_input_rect = None
        self.cal_text_surf_rect = None
        self.add_mood_text_surf_rect = None
        self.curr_date_rect = None
        self.mood_desc_rects = []
        self.mood_quotes_rects = []
        self.selected_mood_text_surf_rect = None
        self.placeholder_rect = None
        self.enter_text_button_rect = None
        self.past_mood_text_rect = None
        self.wback_text_button_rect = None
        self.mood_save_text_rect = None
        self.error_text_rect = None
        self.logo_rect = None
        self.error_sound = None
        self.error_image_rect = None
        self.calendar_surf = None
        self.save_entry_surf = None
        self.save_entry_rect = None
        self.trash_button_surf = None
        self.trash_button_rect = None
        self.deleted_entries_surf = None
        self.deleted_entries_rect = None
        self.deleted_text_surf = None
        self.deleted_text_rect = None
        self.logo_surf = None
        self.error_image_surf = None
        self.enter_hover_button_surf = None
        self.wback_hover_button_surf = None

    def load_fonts(self):
        self.title_font = pygame.font.Font("assets/Milky Mania.ttf", 30)
        self.date_font = pygame.font.Font("assets/Milky Mania.ttf", 20)

    def load_music(self):
        self.mixer.music.load("music assets/BGM.wav")
        self.mixer.music.play(-1)

    def load_images(self):
        self.bg_surf = pygame.image.load("assets/bg.png").convert()
        self.add_button_surf = pygame.image.load("assets/add_button.png").convert_alpha()
        self.mood_list = [pygame.image.load(f"assets/{i}.png").convert_alpha() for i in range(1, 10)]
        self.back_button_surf = pygame.image.load("assets/back_button.png").convert_alpha()
        self.home_button_surf = pygame.image.load("assets/home_button.png").convert_alpha()
        self.fwd_button_surf = pygame.image.load("assets/fwd_button.png").convert_alpha()
        self.bk_button_surf = pygame.image.load("assets/bk_button.png").convert_alpha()
        self.next_button_surf = pygame.image.load("assets/fwd_button.png").convert_alpha()
        self.next_button_surf = pygame.transform.scale(self.next_button_surf, (40, 40))
        self.prev_button_surf = pygame.image.load("assets/bk_button.png").convert_alpha()
        self.prev_button_surf = pygame.transform.scale(self.prev_button_surf, (40, 40))
        self.text_box_surf = pygame.image.load("assets/text_box.jpg").convert_alpha()
        self.logo_surf = pygame.image.load("assets/logo.png").convert_alpha()
        self.error_image_surf = pygame.image.load("assets/error_image.png").convert_alpha()
        self.calendar_surf = pygame.image.load("assets/calendar.png").convert_alpha()
        self.save_entry_surf = pygame.image.load("assets/save.png").convert_alpha()
        self.trash_button_surf = pygame.image.load("assets/trash.png").convert_alpha()
        self.deleted_entries_surf = pygame.image.load("assets/deleted.png").convert_alpha()

    def load_sounds(self):
        self.click_sound_swoosh = self.mixer.Sound("music assets/swoosh.wav")
        self.click_sound_click = self.mixer.Sound("music assets/click.wav")
        self.click_sound_pop = self.mixer.Sound("music assets/pop.wav")
        self.click_sound_powerup = self.mixer.Sound("music assets/powerup.wav")
        self.click_sound_success = self.mixer.Sound("music assets/success.wav")
        self.typing_sound = pygame.mixer.Sound("music assets/typing_sound.wav")
        self.error_sound = pygame.mixer.Sound("music assets/error_sound.wav")

    def render_texts(self):
        self.cal_text_surf = self.title_font.render(datetime.date.today().strftime("%B").upper(), True, (0, 0, 0))
        self.add_mood_text_surf = self.title_font.render("How are you feeling today?", True, "Black")
        self.curr_date_surf = self.date_font.render(self.formatted_date, True, (0, 0, 0))
        self.mood_desc_surf = [self.date_font.render(self.mood_desc[i], True, (0, 0, 0)) for i in range(1, 10)]
        self.mood_quotes_surf = [self.date_font.render(self.mood_quotes[i], True, (0, 0, 0)) for i in range(1, 10)]
        self.selected_mood_text_surf = self.title_font.render("On this day, you feel...", True, "Black")
        self.past_mood_text_surf = self.title_font.render("On this day, you felt...", True, "Black")
        self.placeholder_surf = self.date_font.render("Say something about today... (max of 70 characters)", True,
                                                      "#FFD89C")
        self.enter_text_button_surf = self.title_font.render("Welcome! Click me to enter :)", True, "Black")
        self.wback_text_button_surf = self.title_font.render("Welcome back! Click me to enter :)", True, "Black")
        self.enter_hover_button_surf = self.title_font.render("Welcome! Click me to enter :)", True, "#F3AA60")
        self.wback_hover_button_surf = self.title_font.render("Welcome back! Click me to enter :)", True, "#F3AA60")
        self.mood_save_text_surf = self.date_font.render("Success! Your mood has been added.", True, "#F3AA60")
        self.error_text = self.title_font.render("You can only add an entry to a day once!", True, "Black")
        self.deleted_text_surf = self.title_font.render("Yay! You have deleted all entries : D", True, "Black")

    def create_rects(self):
        self.add_button_rect = self.add_button_surf.get_rect(center=(350, 450))
        self.back_button_rect = self.back_button_surf.get_rect(center=(90, 65))
        self.home_button_rect = self.home_button_surf.get_rect(center=(90, 65))
        self.fwd_button_rect = self.fwd_button_surf.get_rect(center=(600, 250))
        self.bk_button_rect = self.bk_button_surf.get_rect(center=(100, 250))
        self.next_button_rect = self.next_button_surf.get_rect(center=(640, 250))
        self.prev_button_rect = self.prev_button_surf.get_rect(center=(60, 250))
        self.text_box_rect = self.text_box_surf.get_rect(center=(350, 430))
        self.text_input_rect = pygame.Rect(250, 425, 300, 50)
        self.cal_text_surf_rect = self.cal_text_surf.get_rect(center=(350, 50))
        self.add_mood_text_surf_rect = self.add_mood_text_surf.get_rect(center=(350, 50))
        self.curr_date_rect = self.curr_date_surf.get_rect(center=(350, 90))
        self.mood_desc_rects = [surf.get_rect(center=(350, 385)) for surf in self.mood_desc_surf]
        self.mood_quotes_rects = [surf.get_rect(center=(350, 400)) for surf in self.mood_quotes_surf]
        self.selected_mood_text_surf_rect = self.selected_mood_text_surf.get_rect(center=(350, 50))
        self.placeholder_rect = self.placeholder_surf.get_rect(center=(350, 415))
        self.enter_text_button_rect = self.enter_text_button_surf.get_rect(center=(350, 400))
        self.past_mood_text_rect = self.past_mood_text_surf.get_rect(center=(350, 50))
        self.wback_text_button_rect = self.wback_text_button_surf.get_rect(center=(350, 400))
        self.mood_save_text_rect = self.mood_save_text_surf.get_rect(center=(350, 440))
        self.error_text_rect = self.error_text.get_rect(center=(350, 400))
        self.logo_rect = self.logo_surf.get_rect(center=(400, 220))
        self.error_image_rect = self.error_image_surf.get_rect(center=(350, 230))
        self.save_entry_rect = self.save_entry_surf.get_rect(center=(620, 65))
        self.trash_button_rect = self.trash_button_surf.get_rect(center=(620, 450))
        self.deleted_entries_rect = self.deleted_entries_surf.get_rect(center=(350, 230))
        self.deleted_text_rect = self.deleted_text_surf.get_rect(center=(350, 400))

    def load_all_assets(self):
        self.load_fonts()
        self.load_music()
        self.load_images()
        self.load_sounds()
        self.render_texts()
        self.create_rects()
