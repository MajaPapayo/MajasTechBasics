### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)
I followed the link you provided since I face great difficulties searching anything myself so thank you for that!
I choose a flappyBird pygame, since I want to work with pygame in my final project and Im familiar with the concept of Flappy Bird, but other than some other files, it seemed like I could learn from it.
link --> (https://github.com/geekcomputers/Python/blob/master/flappyBird_pygame/flappy_bird.py) 

---

1. What does the program do? What's the general structure of the program? 

Overview:
- the game loads a bird and animates it according to the players input
- the pipes get generated randomly, so that the bird can still surpass
- the games ends and shows the score if the player collides with a pipe
- one can also end the game by pressing e for exit
-----

1. Function analysis: pick one function and analyze it in detail:

- What does this function do?
- What are the inputs and outputs?
- How does it work (step by step)?
---> I first did the analysis then read this, So I baisicaly explained the the entire code and what it does, Output and Inputs are mainly predefined pictures or the e-key to exit, but that is also explained. I tried to explain line by line. I hope this is what you wanted from us in enough detail! 
(whenever I understood smth later I put the original thought in brackets)


import math
import os
from collections import deque
from random import randint

import pygame
from pygame.locals import *

// First they Import everything that will be needed //

FPS = 60
ANI_SPEED = 0.18  # pixels per millisecond
W_WIDTH = 284 * 2  # BG image size: 284x512 px; tiled twice
W_HEIGHT = 512

// All constants, the screen size, the speeds of movement of the objects//

class Bird(pygame.sprite.Sprite):

    WIDTH = 32  #   bird image width
    HEIGHT = 32  #   bird image height
    DOWN_SPEED = 0.18  #   pix per ms  -y
    UP_SPEED = 0.3  #   pix per ms  +y
    UP_DURATION = 150  #   time for which bird go up

// This its the first class, first they define another list of constants relevent for the Bird, which will be the moving object. so they define:
- picture sizeof the bird
- how fast the bird is falling
- how fast it can move up
- how long the bird stays up
//

def __init__(self, x, y, ms_to_up, images):

        super(Bird, self).__init__()
        self.x, self.y = x, y
        self.ms_to_up = ms_to_up
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)


// inside the class they define all the difference states the bird can be in, 
- such as its position, x and y
- all this linked to pictures of the bird 
(- ms_to_up converts the time of the bird being up to milliseconds)
=> correction i have read further and I think it actually show how much more up millisecond are needed till the bird is at the top 
//

  def update(self, delta_frames=1):

        if self.ms_to_up > 0:
            frac_climb_done = 1 - self.ms_to_up / Bird.UP_DURATION
            self.y -= (
                Bird.UP_SPEED
                * frames_to_msec(delta_frames)
                * (1 - math.cos(frac_climb_done * math.pi))
            )
            self.ms_to_up -= frames_to_msec(delta_frames)
        else:
            self.y += Bird.DOWN_SPEED * frames_to_msec(delta_frames)

// first we figure out 
- if the bird is currently going up, 
- if so  we apply the according speed defined above 
- and wait till that predefined time is done.
- frac climb done is here so that the bird only 'climbs' aka flies a fraction of the total climb distance
-??? then the climb is multiplied by pi???
=> not sure why my guesses: since the bird would fall imideatly again, and the frac climb is subtracted from the total possible climb disstance this helps make the fly look more natrual?? so that we don't end on the exact same pixel every time??
- the new y position is set according to that calulation and moves according to the up speed 
- afterwards the distance aka time to the top get subtracted from the new defined frames to the top  
- else: the new y position is set according how far the bird can fall with the speed of the falling speed => Bird.DOWN_SPEED
//

@property
    def image(self):
        # to animate bird
        if pygame.time.get_ticks() % 500 >= 250:
            return self._img_wingup
        else:
            return self._img_wingdown

// - according to the time ticking the bird picture switches between wings up and wings down //

@property
    def mask(self):
        # collision detection
        if pygame.time.get_ticks() % 500 >= 250:
            return self._mask_wingup
        else:
            return self._mask_wingdown

// 
(- ??? this is almost the same code as before? but its supposed to detect when something collides?
- could not find anything online to this function, still confuesed??
- maybe the programmer wanted to be able to call this under this name too?? Or maybe mask_wingdown holds something different)
=> since the file above is refering to img which is a later defined function to load images, there is need to make this a seperate function 
//

 @property
    def rect(self):
        # return birds params
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)

// - a property that holds the coordinates of the bird. as stated above //

class PipePair(pygame.sprite.Sprite):

    WIDTH = 80  #    width of pipe
    PIECE_HEIGHT = 32
    ADD_INTERVAL = 3000

// a New class of the pipes the bird will be flying through
- constants defined of the size of the pipes and when there will appear an interval
//

def __init__(self, pipe_end_img, pipe_body_img):

        self.x = float(W_WIDTH - 1)
        self.score_counted = False

        self.image = pygame.Surface((PipePair.WIDTH, W_HEIGHT), SRCALPHA)
        self.image.convert()  # speeds up blitting
        self.image.fill((0, 0, 0, 0))
        total_pipe_body_pieces = int(
            (
                W_HEIGHT
                - 3 * Bird.HEIGHT  # fill window from top to bottom
                - 3 * PipePair.PIECE_HEIGHT  # make room for bird to fit through
            )
            / PipePair.PIECE_HEIGHT  # 2 end pieces + 1 body piece  # to get number of pipe pieces
        )
        self.bottom_pieces = randint(1, total_pipe_body_pieces)
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces

// 
- position of the pipe
- image of the pipe being imported
- making enough space in the 'holes' for a bird to fit through, by subtracting the size of the bird and the pipe pieces from the height of the pipe 
- the bottom pipe is random and the top pipe is according to that how much pipe still fits to make a big enough 'hole'
//


# bottom pipe
        for i in range(1, self.bottom_pieces + 1):
            piece_pos = (0, W_HEIGHT - i * PipePair.PIECE_HEIGHT)
            self.image.blit(pipe_body_img, piece_pos)
        bottom_pipe_end_y = W_HEIGHT - self.bottom_height_px
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)
        self.image.blit(pipe_end_img, bottom_end_piece_pos)

// 
- the position of the bottom pipe gets created with a for loop
- they also calculate the pipe According to the possible height and the needed hole 
- then the ending and the bottom pieces position get calculated 
- the images get used
//

 # top pipe
        for i in range(self.top_pieces):
            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))
        top_pipe_end_y = self.top_height_px
        self.image.blit(pipe_end_img, (0, top_pipe_end_y))

// top pipe gets defined, since it gets defined according to bottom pipe, less calc
- simmiliar process, image gets loaded etc.
//

 # compensate for added end pieces
        self.top_pieces += 1
        self.bottom_pieces += 1

        # for collision detection
        self.mask = pygame.mask.from_surface(self.image)

// 
- the pictures of the end pieces take in space to so that the bird cant fly through her is a compensation
- here mask gets used ??? 
//

 @property
    def top_height_px(self):
        # returns top pipe's height in pix
        return self.top_pieces * PipePair.PIECE_HEIGHT

    @property
    def bottom_height_px(self):

        return self.bottom_pieces * PipePair.PIECE_HEIGHT
    
 @property
    def visible(self):
        # pipe is on screen or not
        return -PipePair.WIDTH < self.x < W_WIDTH

    @property
    def rect(self):
        # Get the Rect which contains this Pipe.
        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)

    def update(self, delta_frames=1):

        self.x -= ANI_SPEED * frames_to_msec(delta_frames)

    def collides_with(self, bird):

        return pygame.sprite.collide_mask(self, bird)


// 
- private functions, how tall are the pipes?
- can one see the pipes on the screen yet?
- rectangle aka box that is the pipe
- updating frames
- bird collides with a pipe
//

def load_images():
    def load_image(img_file_name):

        file_name = os.path.join(".", "images", img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {
        "background": load_image("background.png"),
        "pipe-end": load_image("pipe_end.png"),
        "pipe-body": load_image("pipe_body.png"),
        # images for animating the flapping bird -- animated GIFs are
        # not supported in pygame
        "bird-wingup": load_image("bird_wing_up.png"),
        "bird-wingdown": load_image("bird_wing_down.png"),
    }

// outside the class now new function
- loading the images used
- returning the image
- image loading is defined as img => explains why mask has to seperate
- the image names are shortend
//

def frames_to_msec(frames, fps=FPS):

    return 1000.0 * frames / fps


def msec_to_frames(milliseconds, fps=FPS):

    return fps * milliseconds / 1000.0


// functions to define a fps to millisecond convertor and wise versa //

def gameover(display, score):
    font = pygame.font.SysFont(None,55)
    text = font.render("Game Over! Score: {}".format(score),True,(255,0,0))
    display.blit(text, [150,250])"""

// the gameover screen
- the writing with the input of the score
//

def main():

    pygame.init()

    display_surface = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
    pygame.display.set_caption("Flappy Bird by PMN")

    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont(None, 32, bold=True)  # default font
    images = load_images()

    # the bird stays in the same x position, so bird.x is a constant
    # center bird on screen
    bird = Bird(
        50,
        int(W_HEIGHT / 2 - Bird.HEIGHT / 2),
        2,
        (images["bird-wingup"], images["bird-wingdown"]),
    )

// the main game loop:
- initiating pygame
- showing the screen
- caption of the screen
- clock for time to pass
- font of the score
- using images function under 'images'
- bird gets centered
//

pipes = deque()

    frame_clock = 0  # this counter is only incremented if the game isn't paused
    score = 0
    done = paused = False

// deque() is poping elements form both end of the queue in this case the pipes 
there for deleting the pipe which is leaving on the left side of the screen while adding a new one on the right side of the screen
- everything set to 0 as a start
// 


    while not done:
        clock.tick(FPS)

        # Handle this 'manually'.  If we used pygame.time.set_timer(),
        # pipe addition would be messed up when paused.
        if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
            pp = PipePair(images["pipe-end"], images["pipe-body"])
            pipes.append(pp)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = True
                break
            elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                paused = not paused
            elif e.type == MOUSEBUTTONUP or (
                e.type == KEYUP and e.key in (K_UP, K_RETURN, K_SPACE)
            ):
                bird.ms_to_up = Bird.UP_DURATION

        if paused:
            continue  # don't draw anything

// when the game is running or started 
- the clock ticks according to the FPS
- pipes get added to the list 
- e for exiting or quitting the game, the window closes then
- the milliseconds spend going up are the duration the bird is up
- when thew game is paused it stops drawing -> confusing naming
//

 # check for collisions
        pipe_collision = any(p.collides_with(bird) for p in pipes)
        if pipe_collision or 0 >= bird.y or bird.y >= W_HEIGHT - Bird.HEIGHT:
            done = True

        for x in (0, W_WIDTH / 2):
            display_surface.blit(images["background"], (x, 0))

        while pipes and not pipes[0].visible:
            pipes.popleft()

        for p in pipes:
            p.update()
            display_surface.blit(p.image, p.rect)

        bird.update()
        display_surface.blit(bird.image, bird.rect)

// the game is done when a bird collides or falls out the window
- images of bakcground gets blitted - which helps them, load faster
- pipes get poped when they escape through the left side of the screen
- pipes get updated
- bird gets updated
//

# update and display score
        for p in pipes:
            if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                score += 1
                p.score_counted = True

        score_surface = score_font.render(str(score), True, (255, 255, 255))
        score_x = W_WIDTH / 2 - score_surface.get_width() / 2
        display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))

        pygame.display.flip()
        frame_clock += 1

// - depending of how many pipes could be surppassed your score is calculated
 - clock and score get rendered and displayed
 //
 
  # gameover(display_surface, score)

    print("Game over! Score: %i" % score)

    pygame.quit()


if __name__ == "__main__":
    # If this module had been imported, __name__ would be 'flappybird'.
    # It was executed (e.g. by double-clicking the file), so call main.
    main()

// - game over display get printed
- game quits
- file gets named
//

---

1. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

- making an explicit function for loading the images seems very helpful
- overall the concept of object oriented coding confused me at first, but now I feel like I better understand how to structure object oriented code and why you put the main function at the bottom.


1. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?

-as I already mentioned in my notes, there were to functions that seemed very similar 'mask' and 'image'. While reading I better understood why they both needed to be there. 
I also think 'deque' from collections is a helpful import. Once I googled it and understood how it was used in the code I can now imagine using it in a game that is moving. 
---

Extra notes

Im sorry for so much text I hope it is readable and understandable but overall this task helped me a lot to better get in the coding thinking!! :)