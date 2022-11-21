from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddles(Widget):
    
    score = NumericProperty(0)
    def bounce_ball(self,ball):
        if self.collide_widget(ball): #if self collides with ball and here self is paddle
            ball.velocity_x*=-1

class PongBall(Widget):
    velocity_x=NumericProperty(0) #initial values of velocity in x and y direction when ball is placed at the center
    velocity_y=NumericProperty(0)  
    velocity = ReferenceListProperty(velocity_x,velocity_y)  #updates the velocity_x and y whenever value of velocity is changes

    def move(self):
        self.pos=Vector(self.velocity) + self.pos

class PongGame(Widget): #here Game cannot be changed i.e. ChessGame possible but not Chessxyz 
    
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve(self):
        self.ball.velocity = Vector(6,0).rotate(randint(0,360)) 

    def update(self, dt):
        self.ball.move()

        if self.ball.x < 0: 
            self.ball.velocity_x*=-1
            self.player2.score+=1
        
        if self.ball.x > self.width - 50:
            self.ball.velocity_x*=-1
            self.player1.score+=1

        if self.ball.y < 0 or self.ball.y > self.height - 50:
            self.ball.velocity_y*=-1
        
        self.player1.bounce_ball(self.ball) #passing the ball from here
        self.player2.bounce_ball(self.ball)
        

    #NOTE: there are 3 functions on_touch_up, on_touch_down, on_touch_move
    #up works when you lift up the finger
    #down works when you touches the screen
    #move works on dragging on the screen
    def on_touch_move(self, touch):
        if touch.x < self.width/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y


class PongApp(App): ##here App cannot be changed i.e. ChessApp possible but not Chessxyz 
    def build(self):
        game = PongGame() #creating the object of the class PongGame
        game.serve()
        Clock.schedule_interval(game.update,1.0/60.0) #this fun will call update func of PongGame 60 times in every 1 sec (fps)
        return game 
    
PongApp().run()