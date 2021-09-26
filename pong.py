import pygame
import random
from pygame import mixer


#initializer
pygame.init()

#window_setup
window=pygame.display.set_mode((1080,2340))
ball_x=4*random.choice((1,-1))
ball_y=4*random.choice((1,-1))
player2_speed=7
score_value=0
score__value=0


font=pygame.font.Font("freesansbold.ttf",50)
#score
def show_score():
	score=font.render("SCORE : "+str(score_value),True,(255,255,255))
	window.blit(score,(270,20))
	
def show__score():
	score=font.render("SCORE : "+str(score__value),True,(255,255,255))
	window.blit(score,(620,20))
	
#ball_animation
def  Ball():
	global ball_x,ball_y,score_value,score__value
	ball.x+=ball_x
	ball.y+=ball_y
	pygame.draw.ellipse(window,(100, 150,250),ball)
	if ball.top<=0 or ball.bottom>=2200:
		ball_y*=-1
	if ball.left<=30 or ball.right>=1050:
		ball_reaction()

	#ball__collision
	if ball.colliderect(player1) or ball.colliderect(player2):
		ball_x*=-1
		score_value+=1
		s=mixer.Sound("pong__hit.mp3")
		s.play()
		
	if ball.colliderect(player2):
		ball_x*=-1
		score__value+=1
		s=mixer.Sound("pong__hit.mp3")
		s.play()

#ball_hitt
def ball_reaction():
	global ball_x,ball_y
	ball.center=((random.randint(300,600)),(random.randint(500,900)))
	ball_x*=random.choice((1,-1))
	ball_y*=random.choice((1,-1))


#computer_player_working
def player_o():
	global player2
	if player2.top<ball.y:
		player2.top+=player2_speed
	if player2.bottom>ball.y:
		player2.bottom-=player2_speed
	if player2.top<=0:
		player2.top=0
	if player2.bottom>=2200:
		player2.bottom=2340



#right_one=>player1
player1=pygame.Rect(19,860,30,280)
	


#left_one=>player2
player2=pygame.Rect(1025,860,30,280)



#circle_making
ball=pygame.Rect(500,500,30,30)


#main_loop
run=True
while run:
	window.fill((0,0,0))
	for event in pygame.event.get():
		if event==pygame.QUIT:
			run=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_a:
				player1.y-=250
			if event.key==pygame.K_l:
				player1.y+=250
			
	player_o()
	
	
	#ball_function_calling
	Ball()
	
	if player1.y<=0:
		player1.y=0
	if player1.y>=(2340-320):
		player1.y=(2340-400)
	#player_making
	pygame.draw.rect(window,(255,255,255),player1)
	pygame.draw.rect(window,(255,255,255),player2)
	
	pygame.draw.aaline(window,(200,200,200),(540,0),(540,2340))
	show_score()
	show__score()
	pygame.display.update()