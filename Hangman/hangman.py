import pygame
from Hangman_logic import HangmanGame

pygame.init()
size = [500, 900]
screen = pygame.display.set_mode(size)
title = "행맨 게임"
pygame.display.set_caption(title)

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont("applegothic,applesangothicneo,arial", 55)
hint_font = pygame.font.Font(None, 60)
letter_font = pygame.font.Font(None, 34)
green = (50, 200, 50)
red = (200, 50, 50)

game = HangmanGame()
exit = False
entry_text = ""
answer = False

def tup_r(tup):
    return tuple(round(a) for a in tup)

# game event loop
while not exit:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode and len(event.unicode) == 1 and event.unicode.isalpha():
                entry_text = event.unicode.upper()
                answer = True

    if answer:
        game.guess(entry_text)
        answer = False
        entry_text = ""

    # 게임 종료 체크
    if game.is_finished():
        screen.fill(black)
        if game.is_won():
            msg = font.render("성공! 정답: " + game.get_word(), True, white)
        else:
            msg = font.render("실패! 정답: " + game.get_word(), True, white)
        msg_size = msg.get_size()
        msg_pos = tup_r((size[0]/2 - msg_size[0]/2, size[1]/2 - msg_size[1]/2))
        screen.blit(msg, msg_pos)
        pygame.display.flip()
        pygame.time.wait(2500)
        break
    
    # drawing
    screen.fill(black)
    
    # 교수대
    line_left_point_ground = tup_r((0, size[1]*2/3))
    line_right_point_ground = tup_r((size[0], line_left_point_ground[1]))
    line_ground_point = tup_r((size[0]/6, line_left_point_ground[1]))
    line_top_point = tup_r((line_ground_point[0], line_ground_point[0]))
    line_top_point_man = tup_r((size[0]/2, line_top_point[1]))
    line_botton_point_man = tup_r((line_top_point_man[0], line_top_point_man[1] + size[0]/6))
    pygame.draw.line(screen, white, line_left_point_ground, line_right_point_ground, 3)
    pygame.draw.line(screen, white, line_ground_point, line_top_point, 3)
    pygame.draw.line(screen, white, line_top_point, line_top_point_man, 3)
    pygame.draw.line(screen, white, line_top_point_man, line_botton_point_man, 3)
    
    # 신체 좌표 사전 계산 (조건부 드로잉을 위해 항상 계산)
    r_head_point = round(size[0]/12)
    head = (line_botton_point_man[0], line_botton_point_man[1] + r_head_point)
    neck_top = (head[0], head[1] + r_head_point)
    neck_bottom = tup_r((neck_top[0], neck_top[1] + r_head_point * 0.4))
    body_top = neck_bottom
    body_bottom = tup_r((body_top[0], body_top[1] + r_head_point * 3))
    arm_y = body_top[1] + r_head_point * 0.1
    arm_origin = tup_r((body_top[0], arm_y))
    left_arm_end  = tup_r((body_top[0] - r_head_point * 1.5, arm_y + r_head_point * 1.2))
    right_arm_end = tup_r((body_top[0] + r_head_point * 1.5, arm_y + r_head_point * 1.2))
    left_leg_end  = tup_r((body_bottom[0] - r_head_point * 1.2, body_bottom[1] + r_head_point * 2.5))
    right_leg_end = tup_r((body_bottom[0] + r_head_point * 1.2, body_bottom[1] + r_head_point * 2.5))

    # 틀린 횟수에 따라 신체 부위 점진적으로 표시 (최대 7번)
    tries = game.try_num
    if tries >= 1:
        pygame.draw.circle(screen, white, head, r_head_point, 3)       # 머리
    if tries >= 2:
        pygame.draw.line(screen, white, neck_top, neck_bottom, 3)       # 목
    if tries >= 3:
        pygame.draw.line(screen, white, body_top, body_bottom, 3)       # 몸통
    if tries >= 4:
        pygame.draw.line(screen, white, arm_origin, left_arm_end, 3)    # 왼팔
    if tries >= 5:
        pygame.draw.line(screen, white, arm_origin, right_arm_end, 3)   # 오른팔
    if tries >= 6:
        pygame.draw.line(screen, white, body_bottom, left_leg_end, 3)   # 왼다리
    if tries >= 7:
        pygame.draw.line(screen, white, body_bottom, right_leg_end, 3)  # 오른다리
    
    # 힌트 표시 - 글자마다 밑줄을 직접 그리고, 맞춘 글자는 위에 렌더링
    word_display = game.get_display()
    slot_w = 46
    word_total_w = len(word_display) * slot_w
    wx = round(size[0] / 2 - word_total_w / 2)
    wy = round(size[1] * 5 / 6)
    for i, c in enumerate(word_display):
        sx = wx + i * slot_w
        cx = sx + slot_w // 2
        pygame.draw.line(screen, white, (sx + 4, wy + 4), (sx + slot_w - 8, wy + 4), 3)
        if c != "_":
            cs = hint_font.render(c, True, white)
            screen.blit(cs, cs.get_rect(midbottom=(cx, wy + 1)))

    # 입력한 알파벳 순차 표시 (초록 박스: 정답, 빨강 박스: 오답)
    history = game.get_history()
    if history:
        box_w, box_h, gap = 36, 40, 4
        total_w = len(history) * (box_w + gap) - gap
        lx = round(size[0] / 2 - total_w / 2)
        ly = 625
        for i, letter in enumerate(history):
            x = lx + i * (box_w + gap)
            pygame.draw.rect(screen, red, (x, ly, box_w, box_h))
            surf = letter_font.render(letter, True, white)
            text_rect = surf.get_rect(center=(x + box_w // 2, ly + box_h // 2))
            screen.blit(surf, text_rect)

    pygame.display.flip()
    
# end of game loop
pygame.quit()