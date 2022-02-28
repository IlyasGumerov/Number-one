import pygame
import sys
import random


size = width, height = 600, 600
fps = 20


def terminate():
    global all_score, games, language, record
    with open('datas.txt', 'w', encoding='UTF-8') as f:
        f.write(str(all_score) + '\n')
        f.write(str(games) + '\n')
        f.write(str(record) + '\n')
        f.writelines(language)
    pygame.quit()
    sys.exit()


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.surface.Surface((300, 300))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect().move(150, 150)


class Text(pygame.sprite.Sprite):
    def __init__(self, nots, text):
        super().__init__(all_sprites)
        self.image = pygame.surface.Surface((len(text) * 30, (nots + 1) * (30 + 10 * nots)))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect().move((150 + (300 - self.image.get_width()) // 2,
                                                150 + (300 - self.image.get_height()) // 2))
        font = pygame.font.Font(None, 30)
        text_coord = 0
        global language
        for i in range(nots + 1):
            if language == 'tat':
                if i != 0:
                    string_rendered = font.render('Түгел', True, pygame.color.Color('white'))
                else:
                    string_rendered = font.render(text, True, pygame.color.Color('white'))
            else:
                if i < nots:
                    notes = {'rus': 'НЕ', 'eng': 'NOT'}
                    string_rendered = font.render(notes[language], True, pygame.color.Color('white'))
                else:
                    string_rendered = font.render(text, True, pygame.color.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 0
            text_coord += intro_rect.height
            self.image.blit(string_rendered, intro_rect)


def check(key, nots, answer):
    if nots % 2:
        if key != answer:
            return True
        return False
    if key == answer:
        return True
    return False


def new_word(delta_time, lang):
    if delta_time < 20:
        if lang == 'rus':
            sp = ['ВВЕРХ', 'ВНИЗ', 'НАПРАВО', 'НАЛЕВО']
        elif lang == 'tat':
            sp = ['Өскә', 'Аска', 'Сулга', 'Уңга']
        else:
            sp = ['UP', 'DOWN', 'RIGHT', 'LEFT']
        nots = 0
    elif delta_time < 40:
        if lang == 'rus':
            sp = ['ВВЕРХ', 'ВНИЗ', 'НАПРАВО', 'НАЛЕВО', 'НИЧЕГО']
        elif lang == 'tat':
            sp = ['Өскә', 'Аска', 'Сулга', 'Уңга']
        else:
            sp = ['UP', 'DOWN', 'RIGHT', 'LEFT', 'NOTHING']
        nots = random.randint(0, 1)
    else:
        if lang == 'rus':
            sp = ['ВВЕРХ', 'ВНИЗ', 'НАПРАВО', 'НАЛЕВО', 'НИЧЕГО']
        elif lang == 'eng':
            sp = ['UP', 'DOWN', 'RIGHT', 'LEFT', 'NOTHING']
        else:
            sp = ['Өскә', 'Аска', 'Сулга', 'Уңга', 'Бернәрсә']
        nots = random.randint(0, 3)
    ans = random.choice(sp)
    time = 140 - delta_time
    if delta_time < 60:
        delta_time += 2
    return ans, nots, time, delta_time


def new_game():
    global language
    all_sprites = pygame.sprite.Group()
    ans, nots, time, delta_time = new_word(0, language)
    return all_sprites, ans, nots, time, delta_time


def pause(typ, *args):
    global language, all_score, games, record
    pygame.display.set_caption('NotNot')
    if typ == 'pause':
        if language == 'rus':
            intro_text = ["Продолжить", "Смена языка", 'Меню']
        elif language == 'eng':
            intro_text = ['Continue', 'Change language', 'Menu']
        else:
            intro_text = ["Дәвам итү", "Тел алыштыру", 'Меню']
        text_coord = 50
    else:
        all_score += int(args[0])
        games += 1
        if int(args[0]) > record:
            record = int(args[0])
        if language == 'rus':
            intro_text = ["Ваш счет: " + args[0], "Начать заново", "Смена языка", "Меню"]
        elif language == 'eng':
            intro_text = ["Your score: " + args[0], 'Play again', 'Change language', 'Menu']
        else:
            intro_text = ["Сезнең исәп: " + args[0], "Яңадан башларга", "Тел алыштыру", "Меню"]
        text_coord = 0
    fon = pygame.transform.scale(pygame.image.load('pause_fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 100
        intro_rect.top = text_coord
        intro_rect.x = 200
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0], event.pos[1]
                if 100 < x < 500:
                    if 150 < y < 275:
                        return
                    if 275 < y < 400:
                        global ans, a
                        x = {'ВВЕРХ': 'UP', 'ВНИЗ': 'DOWN', 'НАПРАВО': 'RIGHT', 'НАЛЕВО': 'LEFT', 'НИЧЕГО': 'NOTHING',
                             'UP': 'Өскә', 'DOWN': 'Аска', 'LEFT': 'Сулга', 'RIGHT': 'Уңга', 'NOTHING': 'Бернәрсә',
                             'Өскә': 'ВВЕРХ', 'Аска': 'ВНИЗ', 'Сулга': 'НАЛЕВО',
                             'Уңга': 'НАПРАВО', 'Бернәрсә': 'НИЧЕГО'}
                        if language == 'rus':
                            language = 'eng'
                        elif language == 'eng':
                            language = 'tat'
                        else:
                            language = 'rus'
                        ans = x[ans]
                        a.kill()
                        a = Text(nots, ans)
                        if typ == 'pause':
                            if language == 'rus':
                                intro_text = ["Продолжить", "Смена языка", 'Меню']
                            elif language == 'eng':
                                intro_text = ['Continue', 'Change language', 'Menu']
                            else:
                                intro_text = ["Дәвам итү", "Тел алыштыру", 'Меню']
                            text_coord = 50
                        else:
                            if language == 'rus':
                                intro_text = ["Ваш счет: " + args[0], "Начать заново", "Смена языка", "Меню"]
                            elif language == 'eng':
                                intro_text = ["Your score: " + args[0], 'Play again', 'Change language', 'Menu']
                            else:
                                intro_text = ["Сезнең исәп: " + args[0], "Яңадан башларга", "Тел алыштыру", "Меню"]
                            text_coord = 0
                        fon = pygame.transform.scale(pygame.image.load('pause_fon.jpg'), (width, height))
                        screen.blit(fon, (0, 0))
                        font = pygame.font.Font(None, 30)
                        for line in intro_text:
                            string_rendered = font.render(line, True, pygame.Color('white'))
                            intro_rect = string_rendered.get_rect()
                            text_coord += 100
                            intro_rect.top = text_coord
                            intro_rect.x = 200
                            text_coord += intro_rect.height
                            screen.blit(string_rendered, intro_rect)
                    elif 400 < y < 525:
                        start_screen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.flip()
        clock.tick(fps)


def start_screen():
    if language == 'rus':
        intro_text = ["Начать игру", "Правила игры", "Статистика"]
    elif language == 'eng':
        intro_text = ['Start game', 'Rules', 'Statistic']
    else:
        intro_text = ["Уенны башлау", "Уен кагыйдәләре", "Статистика"]
    pygame.display.set_caption('NotNot')
    fon = pygame.transform.scale(pygame.image.load('fon_menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 100
        intro_rect.top = text_coord
        intro_rect.x = 200
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                y = event.pos[1]
                if y > 350:
                    stat()
                    fon = pygame.transform.scale(pygame.image.load('fon_menu.jpg'), (width, height))
                    screen.blit(fon, (0, 0))
                    font = pygame.font.Font(None, 30)
                    text_coord = 50
                    for line in intro_text:
                        string_rendered = font.render(line, True, pygame.Color('white'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 100
                        intro_rect.top = text_coord
                        intro_rect.x = 200
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                elif y < 250:
                    return
                else:
                    rules()
                    fon = pygame.transform.scale(pygame.image.load('fon_menu.jpg'), (width, height))
                    screen.blit(fon, (0, 0))
                    font = pygame.font.Font(None, 30)
                    text_coord = 50
                    for line in intro_text:
                        string_rendered = font.render(line, True, pygame.Color('white'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 100
                        intro_rect.top = text_coord
                        intro_rect.x = 200
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
        clock.tick(fps)


def stat():
    global record, games, all_score
    pygame.display.set_caption('NotNot')
    if games == 0:
        z = 0
    else:
        z = all_score / games
    if language == 'rus':
        intro_text = ["Рекорд: " + str(record), "Общий счет: " + str(all_score),
                      "Всего игр: " + str(games), "Средний результат: " + str(z)[:5]]
    elif language == 'eng':
        intro_text = ["Record: " + str(record), "Total score: " + str(all_score),
                      "Total games: " + str(games), "Average score: " + str(z)[:5]]
    else:
        intro_text = ["Рекорд:" + str(record), "Гомуми балл:" + str(all_score),
                      "Гомуми уеннар:" + str(games), "Уртача:" + str(z)[: 5]]
    fon = pygame.transform.scale(pygame.image.load('fon_stat.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 100
        intro_rect.top = text_coord
        intro_rect.x = 200
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


def rules():
    if language == 'rus':
        intro_text = ["Вам будут выводится на экран",
                      "различные логические задания",
                      "Чтобы дать ответ, вам нужно",
                      "нажать на стрелки на клавиатуре",
                      "Время ограничено и уменьшается с каждым ответом",
                      "Игра заканчивается после одного неправильного ответа",
                      "Вы можете остановить игру на паузу нажав 'Esc'"]
    elif language == 'eng':
        intro_text = ["You will be displayed",
                       "various logical tasks",
                       "To give an answer, you need",
                       "click on the arrows on the keyboard",
                       "Time is limited and decreases with each answer",
                       "The game ends after one wrong answer",
                       "You can pause the game by pressing 'Esc'"]
    else:
        intro_text = ["Сез күрсәтелерсез",
                       "төрле логик биремнәр",
                       "җавап бирү өчен сезгә клавиатурадагы",
                       "укларга басарга кирәк",
                       "Вакыт чикләнгән һәм һәр җавап белән кими",
                       "Уен бер ялгыш җаваптан соң бетә",
                       "Сез 'Esc' басыгыз белән уенны туктата аласыз"]
    fon = pygame.transform.scale(pygame.image.load('fon_rules.jpg'), (width, height))
    pygame.display.set_caption('NotNot')
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 0
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 0
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


all_sprites = pygame.sprite.Group()
with open('datas.txt', 'r', encoding='UTF-8') as f:
    x = f.readlines()
    all_score = int(x[0])
    games = int(x[1])
    record = int(x[2])
    language = x[3]
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.flip()
    score = 0
    clock = pygame.time.Clock()
    start_screen()
    square = Square()
    pygame.display.set_caption('NotNot')
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 30)
    pygame.mixer.music.load("Wake me up.mp3")
    pygame.mixer.music.play(1)
    for i in range(5):
        pygame.mixer.music.queue("Californication.mp3")
        pygame.mixer.music.queue("Faded.mp3")
        pygame.mixer.music.queue("Wake me up.mp3")
    pygame.display.flip()
    delta_time = 0
    fon = pygame.image.load('foni.jpg')
    pygame.transform.scale(fon, (width, height))
    vol = 1.0
    flPause = False
    ans, nots, time, delta_time = new_word(delta_time, language)
    a = Text(nots, ans)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    a.kill()
                    if language == 'eng':
                        z = 'UP'
                    elif language == 'rus':
                        z = 'ВВЕРХ'
                    else:
                        z = 'Өскә'
                    if check(z, nots, ans):
                        score += 1
                        ans, nots, time, delta_time = new_word(delta_time, language)
                        a = Text(nots, ans)
                    else:
                        pause('end', str(score))
                        square.kill()
                        a.kill()
                        all_sprites, ans, nots, time, delta_time = new_game()
                        square = Square()
                        a = Text(nots, ans)
                        score = 0
                if event.key == pygame.K_DOWN:
                    a.kill()
                    if language == 'eng':
                        z = 'DOWN'
                    elif language == 'rus':
                        z = 'ВНИЗ'
                    else:
                        z = 'Аска'
                    if check(z, nots, ans):
                        score += 1
                        ans, nots, time, delta_time = new_word(delta_time, language)
                        a = Text(nots, ans)
                    else:
                        pause('end', str(score))
                        square.kill()
                        a.kill()
                        all_sprites, ans, nots, time, delta_time = new_game()
                        square = Square()
                        a = Text(nots, ans)
                        score = 0
                if event.key == pygame.K_LEFT:
                    a.kill()
                    if language == 'eng':
                        z = 'LEFT'
                    elif language == 'rus':
                        z = 'НАЛЕВО'
                    else:
                        z = 'Сулга'
                    if check(z, nots, ans):
                        score += 1
                        ans, nots, time, delta_time = new_word(delta_time, language)
                        a = Text(nots, ans)
                    else:
                        pause('end', str(score))
                        square.kill()
                        a.kill()
                        all_sprites, ans, nots, time, delta_time = new_game()
                        square = Square()
                        a = Text(nots, ans)
                        score = 0
                if event.key == pygame.K_RIGHT:
                    a.kill()
                    if language == 'eng':
                        z = 'RIGHT'
                    elif language == 'rus':
                        z = 'НАПРАВО'
                    else:
                        z = 'Уңга'
                    if check(z, nots, ans):
                        score += 1
                        ans, nots, time, delta_time = new_word(delta_time, language)
                        a = Text(nots, ans)
                    else:
                        pause('end', str(score))
                        square.kill()
                        a.kill()
                        all_sprites, ans, nots, time, delta_time = new_game()
                        square = Square()
                        a = Text(nots, ans)
                        score = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pause('pause')
                elif event.key == pygame.K_SPACE:
                    flPause = not flPause
                    if flPause:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                elif event.key == pygame.K_PLUS:
                    vol += 0.1
                    pygame.mixer.music.set_volume(vol)
                elif event.key == pygame.K_MINUS:
                    vol -= 0.1
                    pygame.mixer.music.set_volume(vol)
        time -= 1

        if time == 0:
            a.kill()
            if language == 'eng':
                z = 'NOTHING'
            elif language == 'tat':
                z = 'Бернәрсә'
            else:
                z = 'НИЧЕГО'
            if check(z, nots, ans):
                score += 1
                ans, nots, time, delta_time = new_word(delta_time, language)
                a = Text(nots, ans)
            else:
                pause('end', str(score))
                square.kill()
                a.kill()
                all_sprites, ans, nots, time, delta_time = new_game()
                square = Square()
                a = Text(nots, ans)
                score = 0

        screen.blit(fon, (0, 0))
        if language == 'rus':
            string_rendered = font.render('Счет: ' + str(score), True, pygame.Color('black'))
        else:
            string_rendered = font.render('Score: ' + str(score), True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 50
        intro_rect.x = 450
        screen.blit(string_rendered, intro_rect)
        all_sprites.draw(screen)
        if time / (140 - delta_time) > 0.75:
            c = time - (140 - delta_time) * 0.75
            pygame.draw.line(screen, (255, 255, 255), (150, 150),
                             (150, 150 + int(c / ((140 - delta_time) // 4) * 300)), 2)
            pygame.draw.line(screen, (255, 255, 255), (150, 150), (450, 150), 2)
            pygame.draw.line(screen, (255, 255, 255), (450, 150), (450, 450), 2)
            pygame.draw.line(screen, (255, 255, 255), (150, 450), (450, 450), 2)
        elif time / (140 - delta_time) > 0.5:
            c = time - (140 - delta_time) // 2
            pygame.draw.line(screen, (255, 255, 255), (450, 150),
                             (450 - int(c / (140 - delta_time) * 1200), 150), 2)
            pygame.draw.line(screen, (255, 255, 255), (450, 150), (450, 450), 2)
            pygame.draw.line(screen, (255, 255, 255), (150, 450), (450, 450), 2)
        elif time / (140 - delta_time) > 0.25:
            c = time - (140 - delta_time) // 4
            pygame.draw.line(screen, (255, 255, 255), (450, 450),
                             (450, 450 - int(c / ((140 - delta_time) // 4) * 300)), 2)
            pygame.draw.line(screen, (255, 255, 255), (150, 450), (450, 450), 2)
        elif time / (140 - delta_time) > 0:
            c = time
            pygame.draw.line(screen, (255, 255, 255), (150, 450),
                             (150 + int(c / ((140 - delta_time) // 4) * 300), 450), 2)
        pygame.display.flip()
        clock.tick(fps)