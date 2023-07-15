import pygame
from sys import exit
import datetime
import fileprocessing
from loadassets import LoadAssets
from button_utils import ButtonUtils
import os

pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Doodles")
pygame_icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()

assets = LoadAssets()
assets.load_all_assets()


def mood_info_frame(screen, mood_img, date, mood_desc):
    date_surf = assets.date_font.render(date, True, "Black")
    date_rect = date_surf.get_rect(center=(350, 100))
    mood_img_surf = mood_img
    mood_img_rect = mood_img_surf.get_rect(center=(350, 250))
    mood_desc_surf = assets.date_font.render(mood_desc, True, "#F3AA60")
    mood_desc_rect = mood_desc_surf.get_rect(center=(350, 430))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    frame = "current month"
                    assets.click_sound_swoosh.play()
                    return

        screen.blit(assets.bg_surf, (0, 0))
        screen.blit(assets.back_button_surf, assets.back_button_rect)
        screen.blit(assets.past_mood_text_surf, assets.past_mood_text_rect)
        screen.blit(date_surf, date_rect)
        screen.blit(mood_img_surf, mood_img_rect)
        screen.blit(assets.text_box_surf, assets.text_box_rect)
        ButtonUtils.enlarge_button(screen, assets.back_button_surf, assets.back_button_rect, assets.enlarge_scale)

        if mood_desc == "":
            none_msg_surf = assets.date_font.render("You didn't say much on this day :<", True, "gray")
            non_msg_rect = none_msg_surf.get_rect(center=(350, 430))
            screen.blit(none_msg_surf, non_msg_rect)
        else:
            screen.blit(mood_desc_surf, mood_desc_rect)

        pygame.display.update()


def create_month_frame(screen, month_data):
    global current_month_index
    x = 50
    y = 120

    month_names = list(month_data.keys())

    if month_names == []:
        month_name = datetime.datetime.now().strftime("%B %Y")
    else:
        month_name = month_names[current_month_index]

    month_name_surf = assets.title_font.render(month_name, True, "White")
    month_name_rect = month_name_surf.get_rect(center=(350, 40))
    screen.blit(month_name_surf, month_name_rect)

    entries = month_data.get(month_name, [])
    if not entries:
        no_entry_surf = assets.date_font.render("No entries yet, tell me how you feel today :D", True, "Black")
        no_entry_rect = no_entry_surf.get_rect(center=(350, 240))
        screen.blit(no_entry_surf, no_entry_rect)
    else:
        screen.blit(assets.trash_button_surf, assets.trash_button_rect)
        ButtonUtils.enlarge_button(screen, assets.trash_button_surf, assets.trash_button_rect, assets.enlarge_scale)
        for i, entry in enumerate(entries):
            mood_surf = pygame.transform.scale(assets.mood_list[entry["mood"] - 1], (50, 50)).convert_alpha()
            mood_rect = mood_surf.get_rect(midleft=(x + 60, y))
            screen.blit(mood_surf, mood_rect)
            ButtonUtils.enlarge_button(screen, mood_surf, mood_rect, assets.enlarge_scale)

            if mood_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    assets.click_sound_powerup.play()
                    if pygame.mouse.get_pressed()[0]:
                        mood_info_frame(screen, assets.mood_list[entry["mood"] - 1], entry["date"], entry["mood_desc"])

            if i < len(entries) - 1:
                next_entry = entries[i + 1]
                next_date_surf = assets.date_font.render(next_entry["date"], True, "Black")
                next_date_rect = next_date_surf.get_rect(midleft=(x + 120, y))
                if next_date_rect.right > 650:
                    x = 50
                    y += 60
                else:
                    x += 70
            else:
                x = 100
                y += 40

    if current_month_index > 0:
        screen.blit(assets.prev_button_surf, assets.prev_button_rect)
        ButtonUtils.enlarge_button(screen, assets.prev_button_surf, assets.prev_button_rect, assets.enlarge_scale)

    if current_month_index < len(month_names) - 1:
        screen.blit(assets.next_button_surf, assets.next_button_rect)
        ButtonUtils.enlarge_button(screen, assets.next_button_surf, assets.next_button_rect, assets.enlarge_scale)


frame = "title screen"
i = 0
text = [""]
month_data = fileprocessing.FileProcessing.load_month_data()
months_length = len(month_data)
current_month_index = months_length - 1
error_sound_played = False


while True:
    curr_date_surf = assets.date_font.render(datetime.datetime.now().strftime("%B %d, %Y"), True, "Black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if frame == "title screen":

            if assets.enter_text_button_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    assets.click_sound_click.play()
                    frame = "current month"

        elif frame == "current month":

            i = 0
            create_month_frame(screen, month_data)
            ButtonUtils.enlarge_button(screen, assets.add_button_surf, assets.add_button_rect, assets.enlarge_scale)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if assets.next_button_rect.collidepoint(pygame.mouse.get_pos()) and current_month_index < len(
                        month_data) - 1:
                    assets.click_sound_click.play()
                    current_month_index += 1

                if assets.prev_button_rect.collidepoint(pygame.mouse.get_pos()) and current_month_index > 0:
                    assets.click_sound_click.play()
                    current_month_index -= 1

                if assets.add_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_pop.play()
                    frame = "add mood"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if months_length > 0 or os.path.exists("data.json"):
                        if assets.trash_button_rect.collidepoint(pygame.mouse.get_pos()):
                            assets.click_sound_pop.play()
                            text = [""]
                            fileprocessing.FileProcessing.delete_all_entries()
                            frame = "entries deleted"
                            month_data.clear()
                            current_month_index = 0
                            assets.click_sound_success.play()

            ButtonUtils.enlarge_button(screen, assets.prev_button_surf, assets.prev_button_rect, assets.enlarge_scale)
            ButtonUtils.enlarge_button(screen, assets.next_button_surf, assets.next_button_rect, assets.enlarge_scale)

        elif frame == "add mood":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    frame = "current month"
                    assets.click_sound_swoosh.play()
                    current_month_index = months_length - 1

                if assets.fwd_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_click.play()
                    i += 1
                    if i > len(assets.mood_list) - 1:
                        i = 0

                if assets.bk_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_click.play()
                    i -= 1
                    if i < 0:
                        i = len(assets.mood_list) - 1

                if assets.add_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_pop.play()
                    frame = "selected day"

        elif frame == "selected day":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_swoosh.play()
                    frame = "add mood"
                    text = [""]

                if assets.save_entry_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_pop.play()
                    current_date = datetime.datetime.now()
                    month_name = current_date.strftime("%B %Y")
                    day = current_date.day
                    entries = month_data.setdefault(month_name, [])

                    for entry in entries:
                        entry_date = datetime.datetime.strptime(entry["date"], "%B %d, %Y")
                        if entry_date.day == day:
                            frame = "same day error message"
                            break
                    else:
                        entry = {
                            "date": current_date.strftime("%B %d, %Y"),
                            "mood": i + 1,
                            "mood_desc": text[0],
                        }
                        entries.append(entry)
                        fileprocessing.FileProcessing.store_month_data(month_data)
                        assets.click_sound_success.play()
                        frame = "success"

            if event.type == pygame.TEXTINPUT:
                if len(text[-1]) + len(event.text) <= 70:
                    text[-1] += event.text

            if event.type == pygame.KEYDOWN:
                assets.typing_sound.play()
                if event.key == pygame.K_BACKSPACE:
                    text[-1] = text[-1][:-1]
                    if len(text[-1]) == 0:
                        if len(text) > 1:
                            text = text[:-1]

        elif frame == "success":

            if event.type == pygame.MOUSEBUTTONDOWN:
                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_swoosh.play()
                    frame = "current month"
                    current_date = datetime.datetime.now()
                    month_name = current_date.strftime("%B %Y")
                    current_month_index = list(month_data.keys()).index(month_name)
                    text = [""]

        elif frame == "same day error message":

            if event.type == pygame.MOUSEBUTTONDOWN:
                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_swoosh.play()
                    frame = "current month"
                    text = [""]
                    error_sound_played = False

        elif frame == "entries deleted":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if assets.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                    assets.click_sound_swoosh.play()
                    frame = "current month"

    if frame == "current month":
        screen.blit(assets.calendar_surf, (0, 0))
    else:
        screen.blit(assets.bg_surf, (0, 0))

    if frame == "title screen":
        screen.blit(assets.logo_surf, assets.logo_rect)
        if month_data == {}:
            if assets.enter_text_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(assets.enter_hover_button_surf, assets.enter_text_button_rect)
            else:
                screen.blit(assets.enter_text_button_surf, assets.enter_text_button_rect)
        else:
            if assets.enter_text_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(assets.wback_hover_button_surf, assets.wback_text_button_rect)
            else:
                screen.blit(assets.wback_text_button_surf, assets.wback_text_button_rect)

        pygame.display.update()

    elif frame == "current month":
        create_month_frame(screen, month_data)
        ButtonUtils.enlarge_button(screen, assets.add_button_surf, assets.add_button_rect, assets.enlarge_scale)

    elif frame == "add mood":
        screen.blit(assets.add_mood_text_surf, assets.add_mood_text_surf_rect)
        screen.blit(curr_date_surf, assets.curr_date_rect)
        screen.blit(assets.home_button_surf, assets.home_button_rect)
        screen.blit(assets.mood_list[i], assets.mood_list[i].get_rect(center=(350, 250)))
        screen.blit(assets.mood_desc_surf[i], assets.mood_desc_rects[i])
        screen.blit(assets.fwd_button_surf, assets.fwd_button_rect)
        screen.blit(assets.bk_button_surf, assets.bk_button_rect)
        ButtonUtils.enlarge_button(screen, assets.add_button_surf, assets.add_button_rect, assets.enlarge_scale)
        ButtonUtils.enlarge_button(screen, assets.home_button_surf, assets.home_button_rect, assets.enlarge_scale)
        ButtonUtils.enlarge_button(screen, assets.fwd_button_surf, assets.fwd_button_rect, assets.enlarge_scale)
        ButtonUtils.enlarge_button(screen, assets.bk_button_surf, assets.bk_button_rect, assets.enlarge_scale)

    elif frame == "selected day":
        screen.blit(assets.back_button_surf, assets.back_button_rect)
        screen.blit(curr_date_surf, assets.curr_date_rect)
        screen.blit(assets.selected_mood_text_surf, assets.selected_mood_text_surf_rect)
        screen.blit(assets.mood_list[i], assets.mood_list[i].get_rect(center=(350, 250)))
        screen.blit(assets.text_box_surf, assets.text_box_rect)
        screen.blit(assets.save_entry_surf, assets.save_entry_rect)
        screen.blit(assets.placeholder_surf, assets.placeholder_rect)
        ButtonUtils.enlarge_button(screen, assets.save_entry_surf, assets.save_entry_rect, assets.enlarge_scale)
        ButtonUtils.enlarge_button(screen, assets.back_button_surf, assets.back_button_rect, assets.enlarge_scale)

        for row, line in enumerate(text):
            mood_desc = ButtonUtils.draw_text(screen, line, assets.date_font, "#F3AA60", 350, 430 + (row * 25))

    elif frame == "success":
        screen.blit(assets.home_button_surf, assets.home_button_rect)
        screen.blit(curr_date_surf, assets.curr_date_rect)
        screen.blit(assets.selected_mood_text_surf, assets.selected_mood_text_surf_rect)
        screen.blit(assets.mood_list[i], assets.mood_list[i].get_rect(center=(350, 250)))
        screen.blit(assets.mood_quotes_surf[i], assets.mood_quotes_rects[i])
        screen.blit(assets.mood_save_text_surf, assets.mood_save_text_rect)
        ButtonUtils.enlarge_button(screen, assets.home_button_surf, assets.home_button_rect, assets.enlarge_scale)

    elif frame == "same day error message":
        if not error_sound_played:
            assets.error_sound.play()
            error_sound_played = True
        screen.blit(assets.error_image_surf, assets.error_image_rect)
        screen.blit(assets.home_button_surf, assets.home_button_rect)
        screen.blit(assets.error_text, assets.error_text_rect)
        ButtonUtils.enlarge_button(screen, assets.home_button_surf, assets.home_button_rect, assets.enlarge_scale)

    elif frame == "entries deleted":
        screen.blit(assets.home_button_surf, assets.home_button_rect)
        screen.blit(assets.deleted_entries_surf, assets.deleted_entries_rect)
        screen.blit(assets.deleted_text_surf, assets.deleted_text_rect)
        ButtonUtils.enlarge_button(screen, assets.home_button_surf, assets.home_button_rect, assets.enlarge_scale)
    pygame.display.update()
    clock.tick(60)
