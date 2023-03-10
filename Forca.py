import pygame
import unidecode
import io
import random

pygame.font.init()
font1=pygame.font.SysFont("comicsans",80)#'


WIDTH,HEIGHT=1200,700

GREEN = 0,255,127
ORANGE = 255,165,0
BLACK=0,0,0
WHITE=255,255,255

WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Forca")
    
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
        pygame.display.update()
        (x,y)=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
        buttons=pygame.mouse.get_pressed()
        if buttons[0]==True:
            if WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 250<y<250+rects_h:
                pygame.quit()
            elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 370<y<370+rects_h:
                pygame.quit()
            elif WIDTH/2-rects_w/2<x<WIDTH/2-rects_w/2+rects_w and 490<y<490+rects_h:
                pygame.quit()

menu()