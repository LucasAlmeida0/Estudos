''' 21 Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.   
    No visual studio seria diferente logo irei apenas pular ja que precisaria installar manualmente'''
import pygame
file = 'Exercicio021.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()