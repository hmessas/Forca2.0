
import pygame
import unidecode
import io
import random

pygame.font.init()
font1=pygame.font.SysFont("comicsans",80)
font2=pygame.font.SysFont("comicsans",64)
font3=pygame.font.SysFont("comicsans",45)
font4=pygame.font.SysFont("TimesNewRoman",45)
font5=pygame.font.SysFont('comicsans',25)

WIDTH,HEIGHT = 1200,700

GREEN = 0,255,127
ORANGE = 255,165,0
BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0

WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Forca")
    
def draw_forca(erros=0):

    WIN.fill(WHITE)

    pygame.draw.rect(WIN,BLACK,(240,620,120,30))
    pygame.draw.rect(WIN,BLACK,(285,200,30,420))
    pygame.draw.rect(WIN,BLACK,(285,200,200,30))
    pygame.draw.rect(WIN,BLACK,(435,230,10,20))

    pygame.draw.line(WIN,BLACK,(260,620),(285,595),5)
    pygame.draw.line(WIN,BLACK,(340,620),(315,595),5)

    if erros == 1:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)

    elif erros == 2:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)
        pygame.draw.rect(WIN,BLACK,(430,328,20,150))

    elif erros == 3:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)
        pygame.draw.rect(WIN,BLACK,(430,328,20,150))
        pygame.draw.rect(WIN,BLACK,(360,358,70,20))

    elif erros == 4:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)
        pygame.draw.rect(WIN,BLACK,(430,328,20,150))
        pygame.draw.rect(WIN,BLACK,(360,358,70,20))
        pygame.draw.rect(WIN,BLACK,(450,358,70,20))
        
    elif erros == 5:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)
        pygame.draw.rect(WIN,BLACK,(430,328,20,150))
        pygame.draw.rect(WIN,BLACK,(360,358,70,20))
        pygame.draw.rect(WIN,BLACK,(450,358,70,20))
        pygame.draw.line(WIN,BLACK,(439,468),(360,548),22)

    elif erros == 6:
        pygame.draw.circle(WIN,BLACK,(440,290),40,10)
        pygame.draw.rect(WIN,BLACK,(430,328,20,150))
        pygame.draw.rect(WIN,BLACK,(360,358,70,20))
        pygame.draw.rect(WIN,BLACK,(450,358,70,20))
        pygame.draw.line(WIN,BLACK,(439,468),(360,548),22)
        pygame.draw.line(WIN,BLACK,(439,468),(518,548),22)

def load_text(level):
    if level == 1:
        with io.open('bd_facil','r',encoding='utf8') as f:
            lines=f.readlines()
        return unidecode.unidecode(random.choice(lines)).strip()
    if level == 2:
        with io.open('bd_medio','r',encoding='utf8') as f:
            lines=f.readlines()
        return unidecode.unidecode(random.choice(lines)).strip()
    if level == 3:
        with io.open('bd_dificil','r',encoding='utf8') as f:
            lines=f.readlines()
        return unidecode.unidecode(random.choice(lines)).strip()

def checking_letters(palavra,lg):
    cr=['_']*len(palavra)
    erros = 0
    for i in lg:
        if i in palavra:
            for x in range(len(palavra)):
                if palavra[x] == i:
                    cr[x]=i
            
        else:
            erros+=1
    return ''.join(cr), erros

def checking_words(palavra, tentativa):
    if palavra==tentativa:
        return True
    else:
        return False
    
def ag():
    WIN.fill(WHITE)
    txt=font2.render('Letra já chutada!',1,BLACK)
    WIN.blit(txt,((WIDTH/2-txt.get_width()//2),250+(100-txt.get_height())//2))
    pygame.display.update()
    pygame.time.delay(1000)

def draw_lg(lg,palavra):
    txt1=font3.render('Letras erradas:',1,BLACK)
    WIN.blit(txt1,(800,65))
    lg2=lg.copy()
    for i in palavra:
        if i in lg2:
            lg2.remove(i)
    lg2=sorted(lg2)
    for i, char in enumerate(lg2):
        txt=font3.render(char,1,BLACK)
        WIN.blit(txt,((800+(i%5)*55,(120))))

def draw_suport(lvl):
    pygame.draw.rect(WIN,BLACK,(1110,610,60,60),3,3)
    txt=font4.render('?',1,BLACK)
    WIN.blit(txt,(1128,615))
    (x,y)=pygame.mouse.get_pos()
    if 1110<x<1170 and 610<y<670:
        txt1=font5.render('Acerte a palavra para salvar o inocente.',1,BLACK)
        txt2=font5.render('Você tem apenas 6 chances de acertar as letras.',1,BLACK)
        txt3=font5.render('Também pode chutar uma palavra mas, se errar,',1,BLACK)
        txt4=font5.render('o prisioneiro será enforcado!',1,BLACK)
        WIN.blit(txt1,(600,300))
        WIN.blit(txt2,(600,355))
        WIN.blit(txt3,(600,410))
        WIN.blit(txt4,(600,465))
        txt5=font5.render(f"Dificuldade: {lvl}",1,BLACK)
        WIN.blit(txt5,(600,520))

def draw_cr(cr):
    cr=''.join(cr)
    cr_txt=font1.render(cr,1,BLACK)
    WIN.blit(cr_txt,(370,545))

def draw_erros(erros):
    if erros ==5:
        color=RED
    else:
        color=BLACK
    erros_txt=font2.render(f'Erros: {erros}',1,color)
    WIN.blit(erros_txt,(50,30))

def draw_derrota(palavra):
    WIN.fill(WHITE)
    txt=font2.render(f'Você perdeu! a palavra era: {palavra}',1,BLACK)
    WIN.blit(txt,((WIDTH/2-txt.get_width()//2),250+(100-txt.get_height())//2))

def draw_volta():
    pygame.draw.rect(WIN,BLACK,(27,620,126,60),3,3)
    txt=font3.render('Menu',1,BLACK)
    WIN.blit(txt,(30,610))
    (x,y)=pygame.mouse.get_pos()
    buttons=pygame.mouse.get_pressed()
    if buttons[0]==True:
        if 27<x<143 and 620<y<680:
            menu()

def draw_ct(ct):
    ct=''.join(ct)
    ct_txt=font1.render(ct,1,BLACK)
    WIN.blit(ct_txt,((WIDTH/2-ct_txt.get_width()//2),250+(100-ct_txt.get_height())//2))

def main(level):
    if level==1:
        lvl='Fácil'
    elif level==2:
        lvl='Médio'
    elif level==3:
        lvl='Difícil'
    run=True
    clock=pygame.time.Clock()
    palavra=load_text(level)
    cr=''.join(['_']*len(palavra))
    
    erros=0
    ct=[]
    lg=[]
    while run:
        clock.tick(60)
        draw_forca()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if len(ct)<len(palavra):
                    if event.key == pygame.K_a:
                        ct.append("a")
                    if event.key == pygame.K_b:
                        ct.append("b")
                    if event.key == pygame.K_c:
                        ct.append("c")
                    if event.key == pygame.K_d:
                        ct.append("d")
                    if event.key == pygame.K_e:
                        ct.append("e")
                    if event.key == pygame.K_f:
                        ct.append("f")
                    if event.key == pygame.K_g:
                        ct.append("g")
                    if event.key == pygame.K_h:
                        ct.append("h")
                    if event.key == pygame.K_i:
                        ct.append("i")
                    if event.key == pygame.K_j:
                        ct.append("j")
                    if event.key == pygame.K_k:
                        ct.append("k")
                    if event.key == pygame.K_l:
                        ct.append("l")
                    if event.key == pygame.K_m:
                        ct.append("m")
                    if event.key == pygame.K_n:
                        ct.append("n")
                    if event.key == pygame.K_o:
                        ct.append("o")
                    if event.key == pygame.K_p:
                        ct.append("p")
                    if event.key == pygame.K_q:
                        ct.append("q")
                    if event.key == pygame.K_r:
                        ct.append("r")
                    if event.key == pygame.K_s:
                        ct.append("s")
                    if event.key == pygame.K_t:
                        ct.append("t")
                    if event.key == pygame.K_u:
                        ct.append("u")
                    if event.key == pygame.K_v:
                        ct.append("v")
                    if event.key == pygame.K_w:
                        ct.append("w")
                    if event.key == pygame.K_x:
                        ct.append("x")
                    if event.key == pygame.K_y:
                        ct.append("y")
                    if event.key == pygame.K_z:
                        ct.append("z")

                if event.key == pygame.K_BACKSPACE and len(ct)>0:
                    ct.pop()    

                if event.key==pygame.K_RETURN:
                    if len(ct)==0:
                        continue
                    if len(ct)==1:
                        if ct[0] not in lg:
                            lg.append(ct[0])
                        else:
                            ag()
                        ct.clear()
                        cr , erros=checking_letters(palavra,lg)
                        if erros==6:
                            draw_derrota(palavra)
                            pygame.display.update()
                            pygame.time.delay(5000)
                            menu()
                    if len(ct)==len(palavra):
                        status=checking_words(palavra,ct)
                        if status==False:
                            draw_derrota(palavra)
                            pygame.display.update()
                            pygame.time.delay(5000)
                            menu()
        draw_forca(erros)
        draw_cr(cr)
        draw_ct(ct)
        draw_erros(erros)
        draw_lg(lg,palavra)
        draw_suport(lvl)
        draw_volta()
        pygame.display.update()

    

def menu():
    while True:
        rects_w,rects_h=450,100
        WIN.fill(WHITE)
        pygame.draw.rect(WIN,BLACK,(WIDTH/2-rects_w/2,250,rects_w,rects_h),border_radius=5)
        texto_f=font1.render("Fácil",1,WHITE)
        texto_m=font1.render("Médio",1,WHITE)
        texto_d=font1.render("Difícil",1,WHITE)
        titulo=font1.render('Jogo da Forca',1,BLACK)
        WIN.blit(titulo,((WIDTH/2-titulo.get_width()//2),60+(rects_h-titulo.get_height())//2))
        WIN.blit(texto_f,((WIDTH/2-texto_f.get_width()//2),250+(rects_h-texto_f.get_height())//2))
        pygame.draw.rect(WIN,BLACK,(WIDTH/2-rects_w/2,370,rects_w,rects_h),border_radius=5)
        WIN.blit(texto_m,((WIDTH/2-texto_m.get_width()//2),370+(rects_h-texto_m.get_height())//2))
        pygame.draw.rect(WIN,BLACK,(WIDTH/2-rects_w/2,490,rects_w,rects_h),border_radius=5)
        WIN.blit(texto_d,((WIDTH/2-texto_d.get_width()//2),490+(rects_h-texto_d.get_height())//2))

        (x,y)=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
        buttons=pygame.mouse.get_pressed()
        if WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 250<y<250+rects_h:
            txt=font3.render('Palavras entre 4 e 5 letras',1,BLACK)
            WIN.blit(txt,((WIDTH/2-txt.get_width()//2),150))
        elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 370<y<370+rects_h:
            txt=font3.render('Palavras entre 6 e 7 letras',1,BLACK)
            WIN.blit(txt,((WIDTH/2-txt.get_width()//2),150))        
        elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 490<y<490+rects_h:
            txt=font3.render('Palavras entre 8 e 10 letras',1,BLACK)
            WIN.blit(txt,((WIDTH/2-txt.get_width()//2),150))   
        pygame.display.update()
        if buttons[0]==True:
            if WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 250<y<250+rects_h:
                main(1)
            elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 370<y<370+rects_h:
                main(2)
            elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 490<y<490+rects_h:
                main(3)

menu()