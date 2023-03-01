import pygame as pg
import numpy

FIELD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
RES = 800
SIZE = 50
GOAL = None
START = None
# print(FIELD)

class give_route:
    ch_color = 0.95
    @staticmethod
    def search(el):
        """получает элементы которые нужно найти в списке"""
        ret = []
        el = round(give_route.ch_color**el, 64)
        for i in range(len(FIELD)):
            for a in range(len(FIELD[i])):
                if FIELD[i][a] == el:
                    ret.append([a,i])
        return ret
    @staticmethod
    def ch_sp():
        """проверяет пробелы"""#нужно предусмотреть случаи, когда к клетке нет пути
        for i in FIELD:
            for a in i:
                if a == 0:
                    return True
    @staticmethod
    def pokraska():
        """красит вокруг лежащие квадратики"""
        FIELD[GOAL[1]][GOAL[0]] = 1
        lvl = 0
        prev_ver = []
        while give_route.ch_sp() and give_route.search(lvl) != []:

            # print('ch_sp')
            Mozgi.frame(sc)
            # # print("-----")
            # for i in FIELD:
            #     # print(i)
            for i in give_route.search(lvl):
                # print('search')
                try:
                    # print(i[1])
                    # print(i[0] + 1)
                    if FIELD[i[1]+1][i[0]] != 2 and FIELD[i[1]+1][i[0]] == 0 and i[1] + 1>=0 and i[0]>=0:
                        # print("ch")
                        # print(i[1]+1)
                        # print(i[0])
                        FIELD[i[1]+1][i[0]] = round(give_route.ch_color**(lvl+1), 64)
                except IndexError:
                    pass
                try:
                    # print(i[1])
                    # print(i[0] + 1)
                    if FIELD[i[1] - 1][i[0]] != 2 and FIELD[i[1] -1][i[0]] == 0 and i[1] - 1>=0 and i[0]>=0:
                        # print("ch")
                        # print(i[1] - 1)
                        # print(i[0])
                        FIELD[i[1]-1][i[0]] = round(give_route.ch_color**(lvl+1), 64)
                except IndexError:
                    pass
                try:
                    # print(i[1])
                    # print(i[0] + 1)
                    if FIELD[i[1]][i[0]-1] != 2 and FIELD[i[1]][i[0]-1] == 0 and i[1]>=0 and i[0]-1>=0:
                        # print("ch")
                        # print(i[1])
                        # print(i[0]-1)
                        FIELD[i[1]][i[0]-1] = round(give_route.ch_color**(lvl+1), 64)
                except IndexError:
                    pass
                try:
                    # print(i[1])
                    # print(i[0] + 1)
                    if FIELD[i[1]][i[0]+1] != 2 and FIELD[i[1]][i[0]+1] == 0 and i[1]>=0 and i[0]+1>=0:
                        # print("ch")
                        FIELD[i[1]][i[0]+1] = round(give_route.ch_color**(lvl+1), 64)
                except IndexError:
                    pass
            lvl +=1
    @staticmethod
    def search_route():
        give_route.pokraska()
        route = [[START[1], START[0]]]
        while route[-1]!=[GOAL[1], GOAL[0]]:
            print('start')
            START_nxt = route[-1][1], route[-1][0]
            okrug_zn = []
            okrug_pos = []
            try:
                if FIELD[START_nxt[1]][START_nxt[0]-1] == 2 or START_nxt[0]-1 < 0 or START_nxt[1]<0:
                    raise IndexError
                okrug_zn.append(FIELD[START_nxt[1]][START_nxt[0] - 1])
                okrug_pos.append([START_nxt[1],START_nxt[0] - 1])
            except IndexError:
                okrug_zn.append(0)
                okrug_pos.append([])
            try:
                if FIELD[START_nxt[1]][START_nxt[0]+1] == 2 or START_nxt[0]+1 < 0 or START_nxt[1]<0:
                    raise IndexError
                okrug_zn.append(FIELD[START_nxt[1]][START_nxt[0] + 1])
                okrug_pos.append([START_nxt[1], START_nxt[0] + 1])
            except IndexError:
                okrug_zn.append(0)
                okrug_pos.append([])
            try:
                if FIELD[START_nxt[1] - 1][START_nxt[0]] == 2 or START_nxt[0]< 0 or START_nxt[1]-1<0:
                    raise IndexError
                okrug_zn.append(FIELD[START_nxt[1] - 1][START_nxt[0]])
                okrug_pos.append([START_nxt[1]-1, START_nxt[0]])
            except IndexError:
                okrug_zn.append(0)
                okrug_pos.append([])
            try:
                if FIELD[START_nxt[1] + 1][START_nxt[0]] == 2 or START_nxt[0] <0 or START_nxt[1]+1<0:
                    raise IndexError
                okrug_zn.append(FIELD[START_nxt[1] + 1][START_nxt[0]])
                okrug_pos.append([START_nxt[1]+1, START_nxt[0]])
            except IndexError:
                okrug_zn.append(0)
                okrug_pos.append([])
            if max(okrug_zn) == 0:
                print('Contact')
                break
            route.append(okrug_pos[okrug_zn.index(max(okrug_zn))])
        return route
class Mozgi:
     @staticmethod
     def frame(sc):
         for i in range(0,16):
             for a in range(0,16):
                 if FIELD[i][a] == 2:
                     pg.draw.rect(sc, pg.Color("yellow"), (SIZE*a,SIZE*i,SIZE,SIZE))
                 elif FIELD[i][a] > 0:
                     pg.draw.rect(sc, (0,220 * FIELD[i][a],0), (SIZE*a,SIZE*i,SIZE,SIZE))
         if GOAL != None:
            pg.draw.rect(sc, pg.Color("green"), (SIZE*GOAL[0],SIZE*GOAL[1],SIZE,SIZE))
         if START != None:
            pg.draw.rect(sc, pg.Color("red"), (SIZE*START[0],SIZE*START[1],SIZE,SIZE))
     @staticmethod
     def draw_route(sc, coordinates):
         # print(coordinates)
         for i in coordinates:
             pass
             # print("connected")
             pg.draw.rect(sc, pg.Color("blue"), (SIZE*i[1], SIZE*i[0], SIZE, SIZE))
     @staticmethod
     def change_1(pos_x, pos_y):
         FIELD[pos_y][pos_x] = 2

     @staticmethod
     def change_0(pos_x, pos_y):
         FIELD[pos_y][pos_x] = 0

pg.init()
sc = pg.display.set_mode([RES, RES])

t_typed = False
route = []
while True:
    sc.fill(pg.Color("black"))
    Mozgi.frame(sc)
    Mozgi.draw_route(sc, route)
    pg.display.flip()
    if t_typed:
        if GOAL != None and START != None:
            # print("pokraska_started")
            give_route.pokraska()
            print('pokraska_done')
            route = give_route.search_route()
        # print(route)
        t_typed = False
    # print('out_event')
    for event in pg.event.get():
        # print('event')
        if event.type == pg.QUIT:
            # print(FIELD)
            exit()
        key = pg.key.get_pressed()
        if event.type == pg.MOUSEMOTION and key[pg.K_w]:
            x, y = event.pos
            Mozgi.change_1(x // SIZE, y // SIZE)
        if event.type == pg.MOUSEMOTION and key[pg.K_q]:
            x, y = event.pos
            START = x//SIZE, y//SIZE
        if event.type == pg.MOUSEMOTION and key[pg.K_e]:
            x, y = event.pos
            GOAL = x // SIZE, y // SIZE
        if event.type == pg.MOUSEMOTION and key[pg.K_r]:
            x, y = event.pos
            Mozgi.change_0(x//SIZE,y//SIZE)
        if key[pg.K_t]:
            print("t")
            t_typed = True
            # FIELD_np = numpy.array(FIELD)
            # print(numpy.round(FIELD, decimals=2))
            # print(FIELD)
        if key[pg.K_y]:
            route = []
            # print("-------")
            FIELD = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]