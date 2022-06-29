#科技节作品：拯救宇航员
#导入模块
import pygame
import sys,time,random
from colorama import Fore
#初始化
pygame.init()#pygame初始化
pygame.display.init()#屏幕初始化
pygame.font.init()#字体初始化
#设置游戏窗口
screen = pygame.display.set_mode((450,450))#设置窗口对象screen，边长450
start_image = pygame.image.load('太空背景.png')#设置背景
screen.blit(start_image,(-100,3))#调整背景
pygame.display.set_caption('拯救宇航员')#设置窗口标题
#开始界面设置
font = pygame.font.Font(".ttf/字体.ttf",60)#设置‘拯救宇航员’的字体
font2 = pygame.font.Font(".ttf/字体.ttf",40)#设置‘空格开始’的字体
font_auther = pygame.font.Font(".ttf/字体.ttf",30)#设置‘原创：Sun’的字体
#设置字体文件
font_spaceman1 = pygame.font.Font('.ttf/字体.ttf',32)
font_spaceman2 = pygame.font.Font('.ttf/字体.ttf',32)
font_spaceman3 = pygame.font.Font('.ttf/字体.ttf',32)
font_spaceman4 = pygame.font.Font('.ttf/字体.ttf',32)
font_spaceman5 = pygame.font.Font('.ttf/字体.ttf', 32)

#设置字体内容
text_spaceman1 = font_spaceman1.render("宇航员正要返回地球",True,(250,0,0))
text_spaceman2 = font_spaceman2.render("可却发现返回舱内缺失了1个零件",True,(250,0,0))
text_spaceman3 = font_spaceman3.render("帮助宇航员找回丢失的零件",True,(250,0,0))
text_spaceman4 = font_spaceman4.render("WASD控制",True,(250,0,0))
text_spaceman5 = font_spaceman5.render("躲避在太空中游荡的陨石", True, (250, 0, 0))

text = font.render("拯救宇航员",True,(20,0,255))#设置字体内容，颜色
text2 = font2.render("空格开始",True,(255,20,5))#设置字体内容，颜色
text_auther = font_auther.render("原创：Sun",True,(250,0,5))
screen.blit(text, (100,80))#把三个文本推送到屏幕上
screen.blit(text2,(150,250))
screen.blit(text_auther,(160,200))
pygame.display.flip()#更新窗口
while True:#进入游戏主循环
    for event in pygame.event.get():
        #检测是否按下‘X’键
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)#如果按下就退出
        elif event.type == pygame.KEYDOWN:#检测键盘是否被按下
            key_list = pygame.key.get_pressed()#获取键盘检测列表
            if key_list[pygame.K_SPACE]:#如果空格被按下就进入游戏
                pygame.display.init()
                screen.fill('black')
                #进入游戏
                #推送文本到主屏幕
                screen.blit(text_spaceman1,(105,180))
                pygame.display.flip()
                time.sleep(3)
                screen.fill('black')

                screen.blit(text_spaceman2,(30,180))
                pygame.display.flip()
                time.sleep(3)
                pygame.display.init()
                screen.fill('black')

                screen.blit(text_spaceman3,(65,180))
                pygame.display.flip()
                time.sleep(3)
                screen.fill('black')

                screen.blit(text_spaceman4,(160,180))
                pygame.display.flip()
                time.sleep(3)
                screen.fill('black')

                screen.blit(text_spaceman5,(80,180))
                pygame.display.flip()
                time.sleep(3)
                pygame.display.init()
                screen.fill('black')

                pygame.display.flip()

                #导入宇航员图片
                spaceman = pygame.image.load('yuhangyuan.png')
                game_background = pygame.image.load('gamebg.jpg')
                xingqiu = pygame.image.load('xingqiu.png')

                #导入零件图片
                l1 = pygame.image.load('零件1.png')

                #设置零件初始坐标
                l1x = random.randint(2,400)
                l1y = random.randint(2,400)

                #宇航员坐标初始化
                x = 194
                y = 186
                xingqiu_x1 = random.randint(2, 400)
                xingqiu_y1 = random.randint(2, 400)
                xingqiu_x2 = random.randint(2, 400)
                xingqiu_y2 = random.randint(2, 400)
                xingqiu_x3 = random.randint(2, 400)
                xingqiu_y3 = random.randint(2, 400)
                xingqiu_x4 = random.randint(2, 400)
                xingqiu_y4 = random.randint(2, 400)

                bg_x = -300
                bg_y = 0

                #推送宇航员到主屏幕
                screen.blit(spaceman,(x,y))
                screen.blit(game_background,(bg_x,bg_y))
                pygame.display.flip()

                starttime = time.time()
                font_far = pygame.font.Font('.ttf/字体.ttf', 30)
                text_far = font_far.render("零件离你还很远！", True, (255, 0, 0))

                font_60 = pygame.font.Font('.ttf/字体.ttf', 30)
                text_60 = font_60.render("零件离你有一段距离了！", True, (255, 0, 0))

                font_30 = pygame.font.Font('.ttf/字体.ttf', 30)
                text_30 = font_30.render("零件离你很近了！", True, (255, 0, 0))

                font_20 = pygame.font.Font('.ttf/字体.ttf', 30)
                text_20 = font_20.render("你快找到零件了！", True, (255, 0, 0))
                screen.blit(xingqiu,(xingqiu_x1,xingqiu_y1))
                screen.blit(xingqiu,(xingqiu_x2,xingqiu_y2))
                screen.blit(xingqiu,(xingqiu_x3,xingqiu_y3))
                screen.blit(xingqiu,(xingqiu_x4,xingqiu_y4))
                screen.blit(spaceman,(x,y))
                pygame.draw.rect(screen,(0,0,0),(0,10,150,5),0)
                pygame.display.flip()
                #游戏主循环
                while True:
                    star_x1 = xingqiu_x1 - x
                    star_y1 = xingqiu_y1 - y
                    star_x2 = xingqiu_x2 - x
                    star_y2 = xingqiu_y2 - y
                    star_x3 = xingqiu_x3 - x
                    star_y3 = xingqiu_y3 - y
                    star_x4 = xingqiu_x4 - x
                    star_y4 = xingqiu_y4 - y
                    #设置零件与宇航员的坐标之差，用于比较距离
                    Y = l1y - y
                    X = l1x - x

                    #检测坐标差
                    if X <= 10 and X >= -10 and Y <= 10 and Y >= -10:
                        endtime = round(time.time() - starttime)
                        font_time = pygame.font.Font('.ttf/字体.ttf', 35)
                        text_time = font_time.render(f"耗时{endtime}秒", True, (0, 10, 250))  # 找到零件所用的时间
                        #如果坐标差在5以内，就找到零件
                        font_found = pygame.font.Font('.ttf/字体.ttf', 30)
                        text_found = font_found.render("恭喜你，找到了丢失零件！", True, (30, 140, 250))

                        screen.fill('black')
                        screen.blit(text_found, (95, 170))
                        pygame.display.flip()
                        time.sleep(2)
                        pygame.display.init()
                        screen.blit(game_background,(bg_x,bg_y))
                        pygame.display.flip()

                        screen.blit(l1,(l1x+50,l1y+50))
                        screen.blit(spaceman,(x-10,y-10))
                        pygame.display.flip()
                        time.sleep(3)

                        screen.fill('black')
                        screen.blit(text_time,(140,170))
                        pygame.display.flip()
                        time.sleep(2)

                        #退出
                        pygame.quit()
                        sys.exit(0)

                    elif X <= 20 and X >= -20 and Y <= 20 and Y >= -20:
                        pygame.draw.rect(screen, (0, 0, 0),(0, 0, 190, 50), 0)
                        screen.blit(text_20, (0, 10))#坐标差如果在20以内，判定为快找到零件

                    elif X <= 30 and X >= -30 and Y <= 30 and Y >= -30:
                        pygame.draw.rect(screen, (0, 0, 0),(0, 0, 190, 50),0)
                        screen.blit(text_30, (0, 10))#坐标差如果在30以内，那么宇航员离零件很近

                    elif X <= 60 and X >= -60 and Y <= 60 and Y >= -60:
                        pygame.draw.rect(screen, (0, 0, 0),(0, 0, 250, 50), 0)
                        screen.blit(text_60, (0, 10))#坐标差在60以内，那么宇航员与零件有一定距离

                    elif star_x1 <= 10 and star_x1 >= -10 and star_y1 <= 10 and star_y1 >= -10:
                        screen.blit(xingqiu,(xingqiu_x1+5,xingqiu_y1+5))
                        pygame.display.flip()
                        time.sleep(1)
                        screen.fill('black')
                        font_gameover = pygame.font.Font('.ttf/字体.ttf',30)
                        text_gameover = font_gameover.render('你撞到了陨石,Game Over',True,(255,10,0))
                        screen.blit(text_gameover,(90,180))
                        pygame.display.flip()
                        time.sleep(1)
                        pygame.quit()
                        sys.exit(0)
                    elif star_x2 <= 10 and star_x2 >= -10 and star_y2 <= 10 and star_y2 >= -10:
                        screen.blit(xingqiu,(xingqiu_x2+5,xingqiu_y2+5))
                        pygame.display.flip()
                        time.sleep(1)
                        screen.fill('black')
                        font_gameover = pygame.font.Font('.ttf/字体.ttf',30)
                        text_gameover = font_gameover.render('你撞到了陨石,Game Over',True,(255,10,0))
                        screen.blit(text_gameover,(90,180))
                        pygame.display.flip()
                        time.sleep(1)
                        pygame.quit()
                        sys.exit(0)
                    elif star_x3 <= 10 and star_x3 >= -10 and star_y3 <= 10 and star_y3 >= -10:
                        screen.blit(xingqiu,(xingqiu_x3+5,xingqiu_y3+5))
                        pygame.display.flip()
                        time.sleep(1)
                        screen.fill('black')
                        font_gameover = pygame.font.Font('.ttf/字体.ttf',30)
                        text_gameover = font_gameover.render('你撞到了陨石,Game Over',True,(255,10,0))
                        screen.blit(text_gameover,(90,180))
                        pygame.display.flip()
                        time.sleep(1)
                        pygame.quit()
                        sys.exit(0)
                    elif star_x4 <= 10 and star_x4 >= -10 and star_y4 <= 10 and star_y4 >= -10:
                        screen.blit(xingqiu,(xingqiu_x4+5,xingqiu_y4+5))
                        pygame.display.flip()
                        time.sleep(1)
                        screen.fill('black')
                        font_gameover = pygame.font.Font('.ttf/字体.ttf',30)
                        text_gameover = font_gameover.render('你撞到了陨石,Game Over',True,(255,10,0))
                        screen.blit(text_gameover,(90,180))
                        pygame.display.flip()
                        time.sleep(1)
                        pygame.quit()
                        sys.exit(0)
                    else:
                        pygame.draw.rect(screen, (0, 0, 0),(0, 0, 190, 50), 0)
                        screen.blit(text_far,(0,10))#坐标差较大，就说明宇航员离零件很远
                    #WASD控制宇航员
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                        else:
                            key_list = pygame.key.get_pressed()
                            #W键
                            if key_list[pygame.K_w]:
                                y -= 1.5
                                screen.blit(spaceman,(x,y))
                                pygame.display.flip()
                                screen.blit(game_background,(bg_x,bg_y))
                            #S键
                            elif key_list[pygame.K_s]:
                                y += 1.5
                                screen.blit(spaceman,(x,y))
                                pygame.display.flip()
                                screen.blit(game_background,(bg_x,bg_y))
                            #A键
                            elif key_list[pygame.K_a]:
                                x -= 1.5
                                screen.blit(spaceman,(x,y))
                                pygame.display.flip()
                                screen.blit(game_background,(bg_x,bg_y))
                            #D键
                            elif key_list[pygame.K_d]:
                                x += 1.5
                                screen.blit(spaceman,(x,y))
                                pygame.display.flip()
                                screen.blit(game_background,(bg_x,bg_y))
#原创：Sun
#2021/12/4制作完成