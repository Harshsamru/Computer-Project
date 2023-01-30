import pygame, sys
from pygame import mixer
from moviepy.editor import * 
mixer.init()
pygame.init()
X = 1200
Y = 600
clock=pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
def akinator_intro():
    img = pygame.image.load("bg\\6.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B1 = button(860, 184, 2, 155, 288, 970, 400)
def akinator_singleplayer():
    img = pygame.image.load("bg\\2.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B2=button(759,184,4,285,288,980,400)
def akinator_multiplayer():
    img = pygame.image.load("bg\\2.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B7 = button(759, 184, 11, 285, 288, 980, 400)
def akinator_sports(player):
    width = 205
    w1 = 550
    w2 = 910
    height = 421
    if player == 1:
       p = player_name1('akinator')
    import random
    V = random.randrange(0, 10)
    T = (('MESSI', 'LIONEL MESSI',), ('YUVRAJ', 'YUVRAJ SINGH'), ('SINDHU', 'PV SINDHU'),
        ('DE VILLIERS', 'AB DE VILLIERS'),('NEERAJ', 'NEERAJ CHOPRA'), ('FEDERER', 'ROGER FEDERER'),
        ('PHELPS', 'MICHAEL PHELPS'), ('WILLIAMS', 'SERENA WILLIAMS'), ('JOHNSON', 'DUSTIN JOHNSON'),('LEBRON JAMES','LEBRON RAYMONE JAMES SR'))
    L = [{1: "CLUE-1 The referred person's father,Jorge, was steelworker\n and coach of the local youth football team",
          2: "CLUE-2 This person had growth hormone deficiency, which was\n stopping his normal growth rate at a tender age of 11. Most\n importantly, his parents couldn’t afford his treatment\n of $900 per month",
          3: "CLUE-3 Holds the record for winning the most number of Ballon\n d'Or awards"},
         {1: "CLUE-1 He/she has won 7 Player of the Series awards in ODI cricket,\n which is joint 3rd highest by an Indian",
          2: "CLUE-2 The person referred here was diagnosed with a cancerous\n tumor in his/her left lung and underwent chemotherapy treatment\n in Boston and Indianapolis",
          3: "CLUE-3 On September 19, 2007, at Kingsmead, he/she smashed six\n sixes in a single over"},
         {1: "CLUE-1 The referred person was born and brought up in Hyderabad,\n was educated at Auxilium High School, Hyderabad and at St.\n Ann's College for Women, Hyderabad.",
          2: "CLUE-2 Though,the referred person's parents played professional\n volleyball, she chose badminton over it because she drew\n inspiration from the success of Pullela Gopichand, the 2001 All\n England Open Badminton Champion.",
          3: 'CLUE-3 This person was honoured with Padma Bhushan Award, the \nthird-highest civilian award in India, in January 2020'},
         {1: 'CLUE-1 The referred person is a right-handed batter who accumulated \n over 8,000 runs in Tests including 22 centuries and 46 fifties\n and holds the record for most Test innings without registering a duck ',
          2: 'CLUE-2 He holds the records for the fastest 50 (16 balls),100 (31 balls) \nand 150 (64 balls) of all time in One Day Internationals by any batsmen.',
          3: 'CLUE-3 On 4 April 2008, he became the first South African to score a \ndouble century against India with a top score of 217.'},
         {1: "CLUE-1 The referred person was born on 24 December 1997 in Chandra \nvillage, Haryana, father is a professional farmer, and mother is a housewife.",
          2: 'CLUE-2 On 4 August 2021, he/she made his/her debut at the Olympics,\n representing India in the Japan National Stadium and also topped the\n qualifying group for entry to the final with a throw of 86.65 metres',
          3: 'CLUE-3 This person has won the gold medal in the final on 7 August\n with a throw of 87.58 m(second attempt), becoming the first Indian \nOlympian to win a gold medal in athletics'},
         {1: 'CLUE-1 He was ranked world No. 1 by the Association of Tennis \nProfessionals (ATP) for 310 weeks, including a record 237 \nconsecutive weeks, and finished as the year-end No. 1 five times.',
          2: 'CLUE-2 On 15 September 2022, he announced his impending \nretirement from professional tennis on the ATP Tour, noting \nthat the Laver Cup would be his final ATP event',
          3: 'CLUE-3 He is a Swiss former professional tennis player'},
        {1: 'CLUE-1 He also holds the all-time records for Olympic \ngold medals (23),Olympic gold medals in individual events (13),\n and Olympic medals in individual events (16)',
         2: 'CLUE-2 He is an American former competitive swimmer',
         3: "CLUE-3 He is the long course world record holder in the \nmen's 400-meter individual medley as well as the former long course \nworld record holder in the 200-meter freestyle, 100-meter\n butterfly, 200-meter butterfly, and 200-meter individual medley"},
        {1: "CLUE-1 Considered among the greatest tennis players of all\n time, she was ranked world No. 1 in singles by the Women's Tennis\n Association (WTA) for 319 weeks, including a joint-record 186 \nconsecutive weeks, and finished as the year-end No. 1 five times",
         2: "CLUE-2 She also won 14 major women's doubles titles, all with her\n sister Venus, and the pair was unbeaten in Grand Slam doubles finals",
         3: 'CLUE-3 She won 23 Grand Slam singles titles, the most by any \nplayer in the Open Era, and the second-most of all time'},
        {1: 'CLUE-1 He has six World Golf Championships victories and he \nis the first player to win each of the four World Golf Championship events',
         2: 'CLUE-2 In February 2017 he became the world number one \nranked golfer and remained there for 64 consecutive weeks \nand has been at number 1 for a total of over 130 weeks',
         3: 'CLUE-3 He is an American professional golfer. He has won two \nmajor championships the 2016 U.S. Open and the 2020 Masters Tournament'},
        {1: 'CLUE-1 He is an American professional basketball player for the \nLos Angeles Lakers of the National Basketball Association (NBA)',
         2: 'CLUE-2 In 2022, he became the first and only player in NBA history\n to accumulate over 10,000 career points, rebounds, and assists',
         3: 'CLUE-3 He has won four NBA championships, four NBA MVP awards, \nfour NBA Finals MVP awards, three All-Star MVP awards, \nand two Olympic gold medals'}]
    for j in range(player+1):
        if player==1 and j==0:
            disp_1=display_player1(p)
        elif player==1 and j==1:
            disp_2=display_player2(p)
        NL=[V]
        if j == 0 and player == 1:
            clues_1 = 0
        elif j==1 and player == 1:
            clues_2 = 0
        if j == 1:
            V = random.randrange(0, 10)
            while V in NL:
                V = random.randrange(0, 10)
        for i in range(1, 4):
            img = pygame.image.load("answer.png").convert()
            screen.blit(img, (0, 0))
            pygame.display.flip()

            if i == 3:
                img = pygame.image.load("Winner (5).png").convert()
                screen.blit(img, (0, 0))
                pygame.display.flip()
                font = pygame.font.SysFont('gabriola', 50)
                z=L[V][3].split('\n')
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                position=0
                for run in range (len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d+position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position+=60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer :', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(400,1000,500)
                r = r.strip()
                if r.upper() in T[V]:

                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 340
                    else:
                        posi = 380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_sports(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'sports')
                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_sports(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'sports')
            else:
                font = pygame.font.SysFont('gabriola', 50)
                z = L[V][i].splitlines()
                position = 0
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                for run in range(len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d + position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position += 60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer ', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(400,1018,488)
                pygame.display.update()
                mouse=pygame.mouse.get_pos()
                if r == ['complex',{1:'$'}]:
                    mixer.music.load("wrong-answer-129254.mp3")
                    mixer.music.play()
                    continue
                elif (r.strip()).upper() in T[V]:
                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219,239,244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi=340
                    else:
                        posi=380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_sports(0)
                    if player == 1 and j==0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j==1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'sports')
                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_sports(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'sports')
def akinator_movies(player):
    img = pygame.image.load("bg\\1.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B3=button(780,200,10,780,350,player+1.3,0)
def akinator_hollywood(player):
    width = 205
    w1 = 550
    w2 = 910
    height = 421
    if player == 1:
       p = player_name1('akinator')
    import random
    V = random.randrange(0, 10)
    T = (('DWAYNE', 'DWAYNE JOHNSON',), ('TOM', 'TOM HOLLAND'), ('DANIEL', 'DANIEL CRAIG'),('GAL', 'GAL GADOT'),('TOM', 'TOM CRUISE'), ('HENRY', 'HENRY CAVILL'),
        ('SCARLETT', 'SCARLETT JOHANSSON'), ('EMILY', 'EMILY BLUNT'), ('MATT', 'MATT DAMON'), ('CHRISTIAN', 'CHRISTIAN BALE'))
    L = [{1: "CLUE-1 He is an American actor and former professional wrestler ",
          2: "CLUE-2 He began his theatrical career in The Mummy Returns (2001)\n, The Scorpion King (2002), The Rundown (2003), and Walking Tall (2004)",
          3: "CLUE-3  In 2016, he co-starred with Kevin Hart in the\n action-comedy Central Intelligence and had a lead\n voice role in the Disney animated film Moana"},
        {1: "CLUE-1 He achieved international recognition playing \nSpider-Man/Peter Parker in six Marvel Cinematic Universe \n(MCU) superhero films, beginning with Captain America: Civil War (2016) ",
         2: "CLUE-2 He received a third consecutive Saturn \nAward for Best Performance by a Younger Actor for Far From Home,\n having previously won for Civil War and Homecoming",
         3: "CLUE-3 He voiced roles in computer-animated features\n, including Onward (2020)"},
        {1: 'CLUE-1  He is an English-American actor who \ngained international fame playing the secret agent\n James Bond in five films in the film series, from Casino \nRoyale (2006) up to No Time to Die (2021)',
         2: 'CLUE-2 He also starred in Glass Onion,the sequel to Knives Out',
         3: 'CLUE-3 For his performance as Detective Benoit Blanc\n in the comedy mystery films Knives Out (2019), and Glass \nOnion (2022), he received two Golden Globe Award nominations.'},
        {1: 'CLUE-1 Her first international film performance was \nas Gisele Yashar in Fast & Furious (2009) ',
         2: 'CLUE-2 She is an Israeli actress',
         3: 'CLUE-3 She went on to achieve global stardom for\n her portrayal of Wonder Woman in the DC Extended Universe'},
        {1: 'CLUE-1 He began acting in the early 1980s and made his\n breakthrough with leading roles in the comedy film \nRisky Business (1983) and action film Top Gun (1986)',
         2: 'CLUE-2 He has played Ethan Hunt in all six of the\n Mission: Impossible films from 1996 to 2018',
         3: 'CLUE-3 His other notable roles in the genre include \nVanilla Sky (2001), Minority Report (2002), The Last Samurai (2003)\n, Collateral (2004), War of the Worlds (2005), Knight and Day (2010) '},
        {1: "CLUE-1 He is a British actor known for his portrayal of\n  DC Comics character Superman in the DC Extended Universe",
         2: 'CLUE-2 He also played the role of Sherlock Holmes in \nthe Netflix film Enola Holmes (2020) and its 2022 sequel',
         3: 'CLUE-3 Following his international breakthrough as Superman,\n he has starred in the spy films The Man from U.N.C.L.E. (2015)\n and Mission: Impossible – Fallout (2018)'},
        {1: 'CLUE-1 She has received various accolades, including a Tony \nAward and a British Academy Film Award, in addition to nominations \nfor two Academy Awards and five Golden Globe Awards',
         2: 'CLUE-2 She made her film debut in the fantasy comedy North (1994)\n, and gained early recognition for her roles in Manny & Lo (1996), \nThe Horse Whisperer (1998), and Ghost World (2001)',
         3: "CLUE-3 She played Black Widow in Jon Favreau's Iron Man 2 (2010),\n a part of the Marvel Cinematic Universe (MCU)"},
        {1: 'CLUE-1 She is the recipient of several accolades, including a Golden\n Globe Award and a Screen Actors Guild Award, in addition to \nnominations for three British Academy Film Awards',
         2: 'CLUE-2 She made her acting debut in a 2001 stage production of The Royal\n Family. She went on to appear in the television film Boudica \n and portrayed Queen Catherine Howard in the miniseries Henry VIII.',
         3: 'CLUE-3 Her profile continued to grow with leading roles in the period \nfilm The Young Victoria, the romantic comedy Salmon Fishing in the\n Yemen, the science fiction films The Adjustment Bureau, Looper.'},
        {1: 'CLUE-1 He has received various awards and nominations, including an \nAcademy Award and two Golden Globe Awards, in addition to nominations\n for three British Academy Film Awards and seven Primetime Emmy Awards',
         2: 'CLUE-2 He won the Golden Globe Award for Best Actor for playing \nan astronaut stranded on Mars in The Martian (2015)',
         3: 'CLUE-3 His other notable performances were in Saving Private Ryan (1998),\n Syriana (2005), The Departed (2006), The Informant! (2009), \nInvictus (2009), True Grit (2010), Contagion (2011)'},
        {1: 'CLUE-1 In 2005, he played superhero Batman in Batman Begins and \nagain in The Dark Knight (2008) and The Dark Knight Rises (2012)',
         2: 'CLUE-2 He continued in starring roles in a range of films outside \nhis work as Batman, including the period drama The Prestige (2006), \nthe action film Terminator Salvation (2009), the epic film Exodus: Gods\n and Kings (2014) and the superhero film Thor: Love and Thunder (2022).',
        3: 'CLUE-3 For his portrayal of boxer Dicky Eklund in the 2010 \nbiographical film The Fighter, he won an Academy Award and a\n Golden Globe Award.'}]
    for j in range(player+1):
        if player==1 and j==0:
            disp_1=display_player1(p)
        elif player==1 and j==1:
            disp_2=display_player2(p)
        NL=[V]
        if j == 0 and player == 1:
            clues_1 = 0
        elif j==1 and player == 1:
            clues_2 = 0
        if j == 1:
            V = random.randrange(0, 10)
            while V in NL:
                V = random.randrange(0, 10)
        for i in range(1, 4):
            img = pygame.image.load("answer.png").convert()
            screen.blit(img, (0, 0))
            pygame.display.flip()

            if i == 3:
                img = pygame.image.load("Winner (5).png").convert()
                screen.blit(img, (0, 0))
                pygame.display.flip()
                font = pygame.font.SysFont('gabriola', 50)
                z=L[V][3].split('\n')
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                position=0
                for run in range (len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d+position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position+=60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer :', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1000,500)
                r = r.strip()
                if r.upper() in T[V]:

                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 340
                    else:
                        posi = 380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_hollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'hollywood')
                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_hollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'hollywood')
            else:
                font = pygame.font.SysFont('gabriola', 50)
                z = L[V][i].splitlines()
                position = 0
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                for run in range(len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d + position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position += 60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer ', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1018,488)
                pygame.display.update()
                mouse=pygame.mouse.get_pos()
                if r == ['complex',{1:'$'}]:
                    mixer.music.load("wrong-answer-129254.mp3")
                    mixer.music.play()
                    continue

                elif (r.strip()).upper() in T[V]:
                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219,239,244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi=340
                    else:
                        posi=380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_hollywood(0)
                    if player == 1 and j==0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j==1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'hollywood')

                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_hollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'hollywood')
def akinator_bollywood(player):
    width = 205
    w1 = 550
    w2 = 910
    height = 421
    if player == 1:
       p = player_name1('akinator')
    import random
    V = random.randrange(0, 10)
    T = (('AYUSHMANN', 'AYUSHMANN KHURRANA',), ('ALIA', 'ALIA BHATT'), ('VARUN', 'VARUN DHAWAN'),
        ('PRIYANKA CHOPRA', 'PRIYANKA CHOPRA JONAS'),('AMITABH', 'AMITABH BACHCHAN'), ('DEEPIKA', 'DEEPIKA PADUKONE'),
        ('SHAH RUKH', 'SHAH RUKH KHAN'), ('MADHURI DIXIT', 'MADHURI DIXIT NENE'), ('KARTIK AARYAN', 'KARTIK AARYAN TIWARI'), ('ANUSHKA SHARMA', 'ANUSHKA SHARMA'))
    L = [{1:"CLUE-1 After completing his graduation and post-graduation in\n Journalism, first job was as a radio personality at BIG FM, Delhi.",
         2: "CLUE-2 Hosted the second season of MTV Rock On and \nIndia's Got Talent on Colors, also a part of the anchoring team \nof Extra Innings T20 for IPL Season 3.",
         3: "CLUE-3 He made his acting debut in 2012 with Shoojit \nSircar's movie-Vicky Donor, co-starring Annu Kapoor."},
        {1: "CLUE-1 The referred person was born to a Gujarati-Hindu\n father and a Kashmiri-German-Muslim mother, holds a British\n citizenship since her mother is from UK",
         2: "CLUE-2 She has performed playback singing for the song\n 'Sooha Saaha' in Highway (2014).",
         3: "CLUE-3 She has launched her own production company named\n Eternal Sunshine Productions in early 2019"},
        {1: "CLUE-1 This person has appeared in Forbes India's Celebrity\n 100 list since 2014, peaking at the 15th position in \n2018 (annual income-₹495.8 million)",
         2: 'CLUE-2 He is the brand ambassador of newly formed ISL club FC Goa',
         3: 'CLUE-3 He has worked as an assistant director to Karan Johar\n on the film "My Name Is Khan"'},
        {1: 'CLUE-1 She has set up a production company Purple Pebble \nPictures with an aim to introduce and promote new talent in the \nIndian film industry.',
         2: "CLUE-2 This person has received numerous accolades, including\n two National Film Award and five Filmfare Awards and was \nalso honoured with Padma Shri",
         3: 'CLUE-3 This person has worked with UNICEF since 2006 and was \nappointed as the national and global UNICEF Goodwill \nAmbassador for child rights '},
        {1: 'CLUE-1 He has won sixteen Filmfare Awards and is the most nominated\n performer in any major acting category at Filmfare, with\n 42 nominations overall. ',
         2: 'CLUE-2 The Government of France honoured him with its highest \ncivilian honour, Knight of the Legion of honour, in 2007.',
         3: 'CLUE-3 His first acting role was as one of the seven protagonists\n in the film Saat Hindustani,directed by Khwaja Ahmad Abbas'},
        {1: 'CLUE-1 She was born on 5 January 1986 in Copenhagen, Denmark, in\n a Saraswat Brahmin family to Konkani-speaking parents.',
         2: "CLUE-2 She collaborated with Saif Ali Khan for the fourth \ntime in Abbas–Mustan's Race 2, an ensemble action thriller \nthat served as a sequel to Race",
         3: "CLUE-3 She is considered as one of the most awarded actresses\n from 2007's as she is the recipient of 80 accolades into her credit"},
        {1: 'CLUE-1 In terms of audience size and income, he has been \ndescribed as one of the most successful film stars in the world.',
         2: 'CLUE-2 He is co-chairman of the motion picture production\n company Red Chillies Entertainment and its subsidiaries',
         3: 'CLUE-3 He made his Bollywood debut in 1992 with Deewana'},
        {1: "CLUE-1 She was among the country's highest-paid celebrities\n throughout the 1990s and early 2000s.",
         2: 'CLUE-2 She has worked with UNICEF since 2014 to advocate the\n rights of children and prevent child labour',
         3: 'CLUE-3 She made her acting debut in 1984 with a leading role\n in the drama Abodh, directed by Hiren Nag'},
        {1: 'CLUE-1 He was born on 22 November 1990 in Gwalior, Madhya Pradesh.\nBoth his parents are doctors; his father is a paediatrician\n and his mother is a gynaecologist',
         2: 'CLUE-2 He has also co-hosted the 2018 IIFA Awards with Ayushmann \nKhurrana, and the 2019 Zee Cine Awards with Vicky Kaushal.',
         3: 'CLUE-3 His breakthrough came in 2018 when he collaborated with \nRanjan and Bharucha for the fourth time in Sonu Ke Titu Ki Sweety'},
        {1: 'CLUE-1 She was the co-founder of the production company Clean \nSlate Filmz, under which she produced several films and web series',
         2: 'CLUE-2 In October 2017, She launched her own clothing line, \nnamed Nush.',
         3: 'CLUE-3 She made her acting debut opposite Shah Rukh Khan in \nthe film Rab Ne Bana Di Jodi (2008)'}]
    for j in range(player+1):
        if player==1 and j==0:
            disp_1=display_player1(p)
        elif player==1 and j==1:
            disp_2=display_player2(p)
        NL=[V]
        if j == 0 and player == 1:
            clues_1 = 0
        elif j==1 and player == 1:
            clues_2 = 0
        if j == 1:
            V = random.randrange(0, 10)
            while V in NL:
                V = random.randrange(0, 10)
        for i in range(1, 4):
            img = pygame.image.load("answer.png").convert()
            screen.blit(img, (0, 0))
            pygame.display.flip()

            if i == 3:
                img = pygame.image.load("Winner (5).png").convert()
                screen.blit(img, (0, 0))
                pygame.display.flip()
                font = pygame.font.SysFont('gabriola', 50)
                z=L[V][3].split('\n')
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                position=0
                for run in range (len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d+position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position+=60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer :', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1000,500)
                r = r.strip()
                if r.upper() in T[V]:

                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 340
                    else:
                        posi = 380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_bollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 =[i,i]
                        akinator_winner(clues_1, clues_2,'bollywood')
                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_bollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 =[4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'bollywood')
            else:
                font = pygame.font.SysFont('gabriola', 50)
                z = L[V][i].splitlines()
                position = 0
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                for run in range(len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d + position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position += 60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer ', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1018,488)
                pygame.display.update()
                mouse=pygame.mouse.get_pos()
                if r == ['complex',{1:'$'}]:
                    mixer.music.load("wrong-answer-129254.mp3")
                    mixer.music.play()
                    continue

                elif (r.strip()).upper() in T[V]:
                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219,239,244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi=340
                    else:
                        posi=380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_bollywood(0)
                    if player == 1 and j==0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j==1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'bollywood')

                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_bollywood(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'bollywood')
def akinator_scientists(player):
    width = 205
    w1 = 550
    w2 = 910
    height = 421
    if player == 1:
       p = player_name1('akinator')
    import random
    V = random.randrange(0, 10)
    T = (('FLEMING','ALEXANDER FLEMING',), ('BOHR', 'NIELS BOHR'), ('FARADAY', 'MICHAEL FARADAY'),('BENJAMIN FRANKLIN', 'BENJAMIN FRANKLIN'),('CURIE','MARIE CURIE'), ('GALILEO','GALILEO GALILEI' ),
         ('HOOKE', 'ROBERT HOOKE'), ('LOVELACE', 'ADA LOVELACE'), ('NEWTON', 'ISSAC NEWTON'), ('ROSALIND FRANKLIN', 'ROSALIND FRANKLIN'))
    L = [{1: "CLUE-1 He discovered the first broadly effective antibiotic \nsubstance ",
          2: "CLUE-2 He recieved the nobel Prize in physics in 1945 ",
          3: "CLUE-3 He discovered penicillin"},
         {1: "CLUE-1 He stated that electrons revolve around the nucleus \nin stable orbits  ",
          2: "CLUE-2 He was a Danish physicist who made contributions to \nunderstanding atomic structure and quantum theory ",
          3: "CLUE-3  He became the first chairman of  the Nordic Institute\n of theoretical physics "},
         {1: 'CLUE-1 He was an English scientist who was best known for his\n work in electromagnetism and electrochemistry',
          2: 'CLUE-2 He made the first electric generator in 1831.',
          3: 'CLUE-3 He discovered that many metals exhibit a weak repulsion \nfor a magnetic field which he termed diamagnetism'},
         {1: 'CLUE-1 He is known as one of the founding fathers of the \nUnited States ',
          2: 'CLUE-2 In 1729 he became the publisher of the newspaper \ncalled The Pennsylvania Gazette',
          3: 'CLUE-3 He invented the lightning rod'},
         {1: 'CLUE-1 She was the first woman to win a Nobel Prize',
          2: 'CLUE-2 She is known pioneering research on radioactivity',
          3: 'CLUE-3 She discovered polonium and radium'},
         {1: 'CLUE-1 He has been called the "father" of observational astronomy',
          2: 'CLUE-2 He invented the thermoscope',
          3: 'CLUE-3 His contributions to observational astronomy include the\n observation of the four largest satellites of Jupiter'},
         {1: 'CLUE-1 In 1660, he discovered the law of elasticity',
          2: 'CLUE-2 He coined the term cell',
          3: 'CLUE-3  In 1673, he built the earliest Gregorian telescope,\n and then he observed the rotations of the planets \nMars and Jupiter.'},
         {1: 'CLUE-1 She is often regarded as the first computer programmer',
          2: "CLUE-2 She was in particular interested in Babbage's work on \nthe Analytical Engine",
          3: 'CLUE-3 She was the first to recognise that the machine had \napplications beyond pure calculation, and to have published the \nfirst algorithm intended to be carried out by such a machine'},
         {1: 'CLUE-1 He built the first practical reflecting telescope',
          2: 'CLUE-2 He made the first theoretical calculation of the \nspeed of sound',
          3: 'CLUE-3 He also formulated an empirical law of cooling'},
         {1: 'CLUE-1 She is best known for her work on the X-ray diffraction \nimages of DNA',
          2: 'CLUE-2 She discovered the tobacco mosaic virus',
          3: 'CLUE-3 She was a British chemist and X-ray crystallographer whose\n work was central to the understanding of the molecular \nstructures of DNA , RNA , viruses, coal, and graphite'}]

    for j in range(player+1):
        if player==1 and j==0:
            disp_1=display_player1(p)
        elif player==1 and j==1:
            disp_2=display_player2(p)
        NL=[V]
        if j == 0 and player == 1:
            clues_1 = 0
        elif j==1 and player == 1:
            clues_2 = 0
        if j == 1:
            V = random.randrange(0, 10)
            while V in NL:
                V = random.randrange(0, 10)
        for i in range(1, 4):
            img = pygame.image.load("answer.png").convert()
            screen.blit(img, (0, 0))
            pygame.display.flip()

            if i == 3:
                img = pygame.image.load("Winner (5).png").convert()
                screen.blit(img, (0, 0))
                pygame.display.flip()
                font = pygame.font.SysFont('gabriola', 50)
                z=L[V][3].split('\n')
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                position=0
                for run in range (len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d+position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position+=60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer :', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1000,500)
                r = r.strip()
                if r.upper() in T[V]:

                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 340
                    else:
                        posi = 380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_scientists(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'scientists')
                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_scientists(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'scientists')
            else:
                font = pygame.font.SysFont('gabriola', 50)
                z = L[V][i].splitlines()
                position = 0
                if len(z)==1:
                    d=250
                elif len(z)==2:
                    d=200
                elif len(z)==3:
                    d=150
                elif len(z)==4:
                    d=100
                for run in range(len(z)):
                    text = font.render(z[run], True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (600, d + position)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    position += 60
                font = pygame.font.SysFont('gabriola', 70)
                text = font.render('Enter your answer ', True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (600, 370)
                screen.blit(text, textRect)
                pygame.display.update()
                r = text_input(420,1018,488)
                pygame.display.update()
                mouse=pygame.mouse.get_pos()
                if r == ['complex',{1:'$'}]:
                    mixer.music.load("wrong-answer-129254.mp3")
                    mixer.music.play()
                    continue

                elif (r.strip()).upper() in T[V]:
                    mixer.music.load("success-1-6297.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (15).png").convert()
                    else:
                        img = pygame.image.load("Winner (17).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(str(i), True, (219,239,244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi=340
                    else:
                        posi=380
                    textRect.center = (850, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_scientists(0)
                    if player == 1 and j==0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [i,i]
                        break
                    elif player == 1 and j==1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [i,i]
                        akinator_winner(clues_1, clues_2,'scientists')

                else:
                    mixer.music.load("videogame-death-sound-43894.mp3")
                    mixer.music.play()
                    if player == 0:
                        img = pygame.image.load("Winner (11).png").convert()
                    else:
                        img = pygame.image.load("Winner (16).png").convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    font = pygame.font.SysFont('gabriola', 60)
                    text = font.render(T[V][1], True, (219, 239, 244))
                    textRect = text.get_rect()
                    if player == 0:
                        posi = 350
                    else:
                        posi = 390
                    textRect.center = (600, posi)
                    screen.blit(text, textRect)
                    pygame.display.update()
                    if player == 0:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        quit()
                                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        home()
                                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                                        mixer.music.load("interface-124464.mp3")
                                        mixer.music.play()
                                        akinator_scientists(0)
                    if player == 1 and j == 0:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_1 = [4,i]
                        break
                    elif player == 1 and j == 1:
                        count = 0
                        while count <= 2000:
                            pygame.display.flip()
                            count += 1
                        clues_2 = [4,i]
                        akinator_winner(clues_1, clues_2,'scientists')
def akinator_winner(clues_1,clues_2,game):
    if clues_1[0]==clues_2[0]:
        width = 205
        w1 = 550
        w2 = 910
        height = 421
    else:
        width = 1026
        height = 60
        h1=240
        h2=420
    if clues_1[0] == clues_2[0]:
        img = pygame.image.load("Winner (20).png").convert()
        screen.blit(img, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        quit()
                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        home()
                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        if game == 'sports':
                            akinator_sports(1)
                        elif game == 'hollywood':
                            akinator_hollywood(1)
                        elif game == 'bollywood':
                            akinator_bollywood(1)
                        elif game == 'scientists':
                            akinator_scientists(1)
    elif clues_1[0]<clues_2[0]:
        img = pygame.image.load("Winner (18).png").convert()
        screen.blit(img, (0, 0))
        pygame.display.flip()
        font = pygame.font.SysFont('gabriola', 70)
        text = font.render(P1.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (410, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(clues_1[1]), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (510, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(P2.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (770, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(clues_2[1]), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (880, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        while True:
           for event in pygame.event.get():
              if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if width <= mouse[0] <= width + 120 and h2 <= mouse[1] <= h2 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    quit()
                elif width <= mouse[0] <= width + 120 and h1 <= mouse[1] <= h1 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    home()
                elif width <= mouse[0] <= width + 120 and height <= mouse[1] <= height + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    if game == 'sports':
                        akinator_sports(1)
                    elif game == 'hollywood':
                        akinator_hollywood(1)
                    elif game == 'bollywood':
                        akinator_bollywood(1)
                    elif game == 'scientists':
                        akinator_scientists(1)
              pygame.display.update()
    elif clues_1[0]>clues_2[0]:
        img = pygame.image.load("Winner (18).png").convert()
        screen.blit(img, (0, 0))
        pygame.display.flip()
        font = pygame.font.SysFont('gabriola', 70)
        text = font.render(P2.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (410, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(clues_2[1]), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (510, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(P1.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (770, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(clues_1[1]), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (880, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        while True:
          for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if width <= mouse[0] <= width + 120 and h2 <= mouse[1] <= h2 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    quit()
                elif width <= mouse[0] <= width + 120 and h1 <= mouse[1] <= h1 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    home()
                elif width <= mouse[0] <= width + 120 and height <= mouse[1] <= height + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    if game == 'sports':
                        akinator_sports(1)
                    elif game == 'hollywood':
                        akinator_hollywood(1)
                    elif game == 'bollywood':
                        akinator_bollywood(1)
                    elif game == 'scientists':
                        akinator_scientists(1)
             pygame.display.update()
def guess_intro():
    img = pygame.image.load("guess.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B4=button(926,410,6,0,0,0,0)
def guess_choice():
    img = pygame.image.load("bg\\6.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B5 = button(860, 184, 7, 155, 288, 970, 400)
def guess_level():
    img = pygame.image.load("bg\\5.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    B6 = button(930, 184, 3, 115, 288, 940, 400)
def player_name1(game):
    img = pygame.image.load("Winner (4).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    global P1
    P1=text_input(500,1020,495)
    mixer.music.load("interface-124464.mp3")
    mixer.music.play()
    pygame.display.update()
    img = pygame.image.load("Winner (4).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    global P2
    P2=text_input(500,1020,495)
    mixer.music.load("interface-124464.mp3")
    mixer.music.play()
    width=434
    height=301
    radius=59
    img = pygame.image.load("Untitled design.png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    #pygame.draw.circle(screen, (0, 255, 0),[width, height], radius, 3)
    pygame.display.update()
    import random
    V = random.randrange(1, 3)
    while True:
        for event in pygame.event.get():
            print('hello')
            if V==1:
                print('done')
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('done')
                    mouse = pygame.mouse.get_pos()
                    if (width-mouse[0])**2+(height-mouse[1])**2<radius**2:
                        clip = VideoFileClip('untitled design (2).mp4')
                        clip.preview()
                        img = pygame.image.load("Untitled design (1).png").convert()
                        screen.blit(img, (0, 0))
                        pygame.display.update()
                        B7=button(1050,470,8,0,0,0,0)
                        if B7=='It works!!':
                            if V==1:
                                pass
                            elif V==2:
                                P1, P2 = P2, P1
                                print(P1, P2)
                            if game=='guess':
                                guess_multiplayer(P1,P2)
                            if game=='akinator':
                                return([P1,P2])
                mouse = pygame.mouse.get_pos()


            if V==2:
                print('done')
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print('done')
                    mouse = pygame.mouse.get_pos()
                    if (width-mouse[0])**2+(height-mouse[1])**2<radius**2:
                        clip = VideoFileClip('untitled design (1).mp4')
                        clip.preview()
                        img = pygame.image.load("Untitled design (2).png").convert()
                        screen.blit(img, (0, 0))
                        pygame.display.update()
                        B7=button(1050,470,8,0,0,0,0)
                        if B7=='It works!!':
                            if V==1:
                                pass
                            elif V==2:
                                P1, P2 = P2, P1
                                print(P1, P2)
                            if game=='guess':
                                guess_multiplayer(P1,P2)
                            if game=='akinator':
                                return([P1,P2])
                mouse = pygame.mouse.get_pos()
def display_player1(p):
    c=1
    img = pygame.image.load("winner (3).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    font = pygame.font.SysFont('gabriola', 70)
    text = font.render(p[0].capitalize(), True, (51,54,82))
    textRect = text.get_rect()
    textRect.center = (600, 315)
    screen.blit(text, textRect)
    while c<=800:
       pygame.display.update()
       c+=1
    return('done')
def display_player2(p):
    c = 1
    img = pygame.image.load("winner (3).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.flip()
    font = pygame.font.SysFont('gabriola', 70)
    text = font.render(p[1].capitalize(), True, (51,54,82))
    textRect = text.get_rect()
    textRect.center = (600, 315)
    screen.blit(text, textRect)
    while c <= 800:
        pygame.display.update()
        c += 1
    return ('done')
def guess_singleplayer(chance):
    width=205
    w1=550
    w2=910
    height=421
    color_dark = (100, 100, 100)
    img = pygame.image.load("Winner (5).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    font = pygame.font.SysFont('gabriola', 70)
    text = font.render('Enter the Number', True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (600, 300)
    screen.blit(text, textRect)
    pygame.display.flip()
    pygame.display.update()
    import random
    v = random.randrange(0, 101, 1)
    while v%5 == 0:
        v = random.randrange(0, 101, 1)
    for i in range(chance):
        x = int(text_input(580,1050,500))
        if x > v:
            mixer.music.load("wrong-answer-129254.mp3")
            mixer.music.play()
            img = pygame.image.load("Winner (5).png").convert()
            screen.blit(img, (0, 0))
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            left = 'No of guesses left: ' + str(chance - (i + 1))
            text = font.render(left, True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (1000, 50)
            screen.blit(text, textRect)
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 70)
            text = font.render('Enter the Number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 300)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            text = font.render('Entered number is greater than the random number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 370)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()
        elif x < v:
            mixer.music.load("wrong-answer-129254.mp3")
            mixer.music.play()
            img = pygame.image.load("Winner (5).png").convert()
            screen.blit(img, (0, 0))
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 70)
            text = font.render('Enter the Number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 300)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            left = 'No of guesses left: ' + str(chance - (i + 1))
            text = font.render(left, True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (1000, 50)
            screen.blit(text, textRect)
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            text = font.render('Entered number is lesser than the random number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 370)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()

        elif x == v:
            img = pygame.image.load("Winner (14).png").convert()
            screen.blit(img, (0, 0))
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 75)
            y = str(i + 1)
            text = font.render(y, True, (219,239,244))
            textRect = text.get_rect()
            textRect.center = (840,340)
            screen.blit(text, textRect)
            pygame.display.update()
            mixer.music.load("success-1-6297.mp3")
            mixer.music.play()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                            mixer.music.load("interface-124464.mp3")
                            mixer.music.play()
                            quit()
                        elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                            mixer.music.load("interface-124464.mp3")
                            mixer.music.play()
                            home()
                        elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                            mixer.music.load("interface-124464.mp3")
                            mixer.music.play()
                            guess_level()
                   # pygame.draw.rect(screen, color_dark, [width, height, 100, 90])
                   # pygame.draw.rect(screen, color_dark, [w1, height, 100, 90])
                   # pygame.draw.rect(screen, color_dark, [w2, height, 100, 90])
                    pygame.display.update()
    if x != v:
        mixer.music.load("videogame-death-sound-43894.mp3")
        mixer.music.play()
        img = pygame.image.load("Winner (10).png").convert()
        screen.blit(img, (0, 0))
        pygame.display.update()
        font = pygame.font.SysFont('gabriola', 100)
        text = font.render(str(v), True, (219,239,244))
        textRect = text.get_rect()
        textRect.center = (848, 300)
        screen.blit(text, textRect)
        pygame.display.flip()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        quit()
                    elif w1 <= mouse[0] <= w1 + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        home()
                    elif w2 <= mouse[0] <= w2 + 100 and height <= mouse[1] <= height + 90:
                        mixer.music.load("interface-124464.mp3")
                        mixer.music.play()
                        guess_level()
                pygame.display.update()
def guess_multiplayer(P1,P2):
    width = 1026
    height = 60
    h1=240
    h2=420
    global guess_1
    guess_1=0
    global guess_2
    guess_2=0
    color_dark = (100, 100, 100)
    img = pygame.image.load("Winner (5).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    font = pygame.font.SysFont('gabriola', 70)
    text = font.render('Enter the Number', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (600, 300)
    screen.blit(text, textRect)
    pygame.display.update()
    import random
    v = random.randrange(0, 101, 1)
    while v%5 == 0:
        v = random.randrange(0, 101, 1)
    game_over =True
    c=0
    while game_over:
        if c % 2 == 0:
            guess_1+=1
            #display_player1()
            font = pygame.font.SysFont('gabriola', 70)
            player=P1.capitalize()+"'s turn"
            text = font.render(player, True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (600, 200)
            screen.blit(text, textRect)
            pygame.display.update()
        else:
            guess_2+=1
            #display_player2()
            font = pygame.font.SysFont('gabriola', 70)
            player=P2.capitalize()+"'s turn"
            text = font.render(player, True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (600, 200)
            screen.blit(text, textRect)
            pygame.display.update()
        x = int(text_input(580,1018,488))

        if x > v:
            mixer.music.load("wrong-answer-129254.mp3")
            mixer.music.play()
            img = pygame.image.load("Winner (5).png").convert()
            screen.blit(img, (0, 0))
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 70)
            text = font.render('Enter the Number', True, (255, 255, 255))
            textRect = text.get_rect()
            textRect.center = (600, 300)
            screen.blit(text, textRect)
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            text = font.render('Entered number is greater than the random number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 370)
            screen.blit(text, textRect)
            pygame.display.update()

        elif x < v:
            mixer.music.load("wrong-answer-129254.mp3")
            mixer.music.play()
            img = pygame.image.load("Winner (5).png").convert()
            screen.blit(img, (0, 0))
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 70)
            text = font.render('Enter the Number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 300)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()
            font = pygame.font.SysFont('gabriola', 50)
            text = font.render('Entered number is lesser than the random number', True, (255,255,255))
            textRect = text.get_rect()
            textRect.center = (600, 370)
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()

        elif x == v:
            mixer.music.load("success-1-6297.mp3")
            mixer.music.play()
            game_over=False
        c+=1

    img = pygame.image.load("Winner (12).png").convert()
    screen.blit(img, (0, 0))
    pygame.display.update()
    if c%2==0:
        font = pygame.font.SysFont('gabriola', 70)
        text = font.render(P2.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (350, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(guess_2), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (485, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(P1.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (730, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(guess_1), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (845, 435)
        screen.blit(text, textRect)
        pygame.display.update()
    else:
        font = pygame.font.SysFont('gabriola', 70)
        text = font.render(P1.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (350, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(guess_1), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (485, 435)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(P2.capitalize(), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (730, 150)
        screen.blit(text, textRect)
        pygame.display.update()
        text = font.render(str(guess_2), True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (845, 435)
        screen.blit(text, textRect)
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if width <= mouse[0] <= width + 120 and h2 <= mouse[1] <= h2 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    quit()
                elif width <= mouse[0] <= width + 120 and h1 <= mouse[1] <= h1 + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    home()
                elif width <= mouse[0] <= width + 120 and height <= mouse[1] <= height + 110:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    player_name1('guess')
            #pygame.draw.rect(screen, color_dark, [width, height, 120, 110])
            #pygame.draw.rect(screen, color_dark, [width, h1, 120, 110])
            #pygame.draw.rect(screen, color_dark, [width, h2, 120, 110])
            pygame.display.update()
def button(width,height,life,w1,h1,w2,h2):
    color_dark = (100, 100, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and life == 1:
                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_intro()
                elif w1 <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_intro()
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 4:
                if width  <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_movies(0)
                elif w1  <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_scientists(0)
                elif w2 <= mouse[0] <= w2 + 100 and h2 <= mouse[1] <= h2 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_sports(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 2:
                if width  <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_singleplayer()
                elif w1  <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_multiplayer()
                elif w2 <= mouse[0] <= w2 + 100 and h2 <= mouse[1] <= h2 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    #multiplayer2()
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 5:
                if width  <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_level()
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 3:

                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_singleplayer(5)
                elif w1 <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_singleplayer(6)
                elif w2 <= mouse[0] <= w2 + 100 and h2 <= mouse[1] <= h2 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_singleplayer(7)
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 6:
                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_choice()
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 7:

                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    guess_level()
                elif w1 <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    #guess_mp2()
                    player_name1('guess')
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 9:
                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    #decider()
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 10:
                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90 and w2==1.3:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_bollywood(0)
                elif w1 <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90 and w2==1.3:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_hollywood(0)
                if width <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90 and w2==2.3:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_bollywood(1)
                elif w1 <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90 and w2==2.3:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_hollywood(1)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 11:
                if width  <= mouse[0] <= width + 100 and height <= mouse[1] <= height + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_movies(1)
                elif w1  <= mouse[0] <= w1 + 100 and h1 <= mouse[1] <= h1 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_scientists(1)
                elif w2 <= mouse[0] <= w2 + 100 and h2 <= mouse[1] <= h2 + 90:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    akinator_sports(1)
            elif event.type == pygame.MOUSEBUTTONDOWN and life == 8:
                 if width  <= mouse[0] <= width + 110 and height <= mouse[1] <= height + 100:
                    mixer.music.load("interface-124464.mp3")
                    mixer.music.play()
                    return('It works!!')
        mouse = pygame.mouse.get_pos()
        #pygame.draw.rect(screen, color_dark, [width, height , 100, 90])
        #pygame.draw.rect(screen, color_dark, [w1, h1, 100, 90])
        #pygame.draw.rect(screen, color_dark, [w2, h2, 100, 90])
        pygame.display.update()
def text_input(x,width,height):
    clock = pygame.time.Clock()
    base_font = pygame.font.SysFont('comicsansms', 60)
    input_rect = pygame.Rect(x, 480, 140, 90)
    color_active = pygame.Color(226,233,238)
    color_passive = pygame.Color(226,233,238)
    color = color_passive
    color_dark = (100, 100, 100)
    active = False
    user_text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:

                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    clock.tick(2)
                    return (user_text)
                else:
                    user_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN and width == 1018:
                if 1018 <= mouse[0] <= 1018 + 100 and 488 <= mouse[1] <= 488 + 90:
                    mixer.music.load("wrong-answer-129254.mp3")
                    mixer.music.play()
                    return(['complex',{1:'$'}])
        mouse = pygame.mouse.get_pos()
        #pygame.draw.rect(screen, color_dark, [width, height, 100, 90])
        pygame.display.update()
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (51, 54, 82))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()
        clock.tick(60)
def home():
    screen = pygame.display.set_mode((X, Y), pygame.RESIZABLE + pygame.SCALED)
    pygame.display.set_caption('Computer Project')
    imp = pygame.image.load("Futuristic.png").convert()
    screen.blit(imp, (0, 0))
    pygame.display.flip()
    s = True
    while s:
        for event in pygame.event.get():
            #clip = VideoFileClip('Intro video.mov')
            #clip.preview()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    img = pygame.image.load('bg\\4.png').convert()
                    screen.blit(img, (0, 0))
                    pygame.display.flip()
                    c= button(925,340,1,773,220,0,0)
        if event.type == pygame.QUIT:
            s = False
            sys.exit()
        pygame.display.update()
def intro():
    clip = VideoFileClip('Winner.mp4')
    clip.preview()
    home()
def quit():
    width=1080
    height=509
    radius=61
    imp = pygame.image.load("Winner (21).png").convert()
    screen.blit(imp, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (width - mouse[0]) ** 2 + (height - mouse[1]) ** 2 < radius ** 2:
                    mixer.music.load("mixkit.mp3")
                    mixer.music.play()
                    c=0
                    while c<=200:
                        pygame.display.update()
                        c+=1
                    pygame.quit()
intro()