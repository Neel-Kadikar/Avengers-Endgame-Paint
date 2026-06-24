#imports necessary libraries
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog

# Initializing everything
init()
font.init()
mixer.init()

# Screen dimensions and setup
width, height = 1600, 900
screen = display.set_mode((width, height))
display.set_caption("Avengers Endgame Paint")


# Colors
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
VIOLET = (46, 27, 73)

# Font
textFont = font.SysFont("Calibri", 15)

# Loading images/icons
bgimage = image.load("images\\wallpaper2.jpg")
pencil = image.load("images\\pencilicon.png")
eraser = image.load("images\\erasericon.png")
fill = image.load("images\\fillicon.png")
line = image.load("images\\lineicon.png")
rectangle = image.load("images\\recticon.png")
filledrect = image.load("images\\filledrecticon.png")
circle = image.load("images\\circleicon.png")
filledcircle = image.load("images\\filledcircleicon.png")
sticker1 = image.load("images\\sticker1icon.png")
sticker2 = image.load("images\\sticker2icon.png")
sticker3 = image.load("images\\sticker3icon.png")
sticker4 = image.load("images\\sticker4icon.png")
sticker5 = image.load("images\\sticker5icon.png")
undo = image.load("images\\undoicon.png")
redo = image.load("images\\redoicon.png")
save = image.load("images\\saveimageicon.png")
insert = image.load("images\\insertimageicon.png")
previoustrack = image.load("images\\previoustrackicon.png")
multicolour = image.load("images\\multicoloursquare.png")
brush = image.load("images\\brushicon.png")
trash = image.load("images\\trashicon.png")
spray = image.load("images\\sprayicon.png")
titleicon = image.load("images\\titleicon.png")
droppericon = image.load("images\\droppericon.png")
pauseicon = image.load("images\\pauseicon.png")
nexttrackicon = image.load("images\\nexttrackicon.png")
gridicon = image.load("images\\gridicon.png")
muteicon= image.load("images\\muteicon.png")

# Drawing background and icons on the screen
screen.blit(bgimage, (0, 0))
screen.blit(pencil, (550, 715))
screen.blit(eraser, (550, 810))
screen.blit(fill, (730, 715))
screen.blit(line, (730, 810))
screen.blit(rectangle, (910, 715))
screen.blit(filledrect, (1090, 715))
screen.blit(circle, (910, 810))
screen.blit(filledcircle, (1090, 810))
screen.blit(sticker1, (20, 210))
screen.blit(sticker2, (200, 210))
screen.blit(sticker3, (380, 210))
screen.blit(sticker4, (20, 510))
screen.blit(sticker5, (290, 510))
screen.blit(undo, (1240, 20))
screen.blit(redo, (1320, 20))
screen.blit(save, (1420, 20))
screen.blit(insert, (1500, 20))
screen.blit(previoustrack, (60, 20))
screen.blit(multicolour, (20, 770))
screen.blit(brush,(20, 660))
screen.blit(trash,(120,660))
screen.blit(spray,(220,660))
screen.blit(titleicon,(550,20))
screen.blit(droppericon,(320,660))
screen.blit(pauseicon,(240, 20))
screen.blit(nexttrackicon,(310, 20))
screen.blit(gridicon,(420,660))
screen.blit(muteicon,(250, 170))


#Initializing variables
tool = "pencil"
size = 1
description="Draws a basic 1 pixel line on the canvas."
descriptionlntwo="Size cannot be adjusted for this tool."
descriptionlnthree="Colour is changed with the rectangle."
col=(0,0,0)
muted=False

#Rects/outlines for icons
canvasRect = Rect(550, 100, 1000, 600)
pencilRect = Rect(550, 715, 80, 80)
eraserRect = Rect(550, 810, 80, 80)
fillRect = Rect(730, 715, 80, 80)
lineRect = Rect(730, 810, 80, 80)
rectRect = Rect(910, 715, 80, 80)
filledrectRect = Rect(1090, 715, 80, 80)
circleRect = Rect(910, 810, 80, 80)
filledcircleRect = Rect(1090, 810, 80, 80)
sticker1Rect = Rect(20, 210, 148.333, 250)
sticker2Rect = Rect(200, 210, 148.333, 250)
sticker3Rect = Rect(380, 210, 148.333, 250)
sticker4Rect = Rect(20, 510, 250, 120)
sticker5Rect = Rect(290, 510, 235, 120)
titleRect = Rect(550, 20, 550, 50)
undoRect = Rect(1240, 20, 50, 50)
redoRect = Rect(1320, 20, 50, 50)
saveRect = Rect(1420, 20, 50, 50)
insertRect = Rect(1500, 20, 50, 50)
previoustrackRect = Rect(60, 20, 160, 50)
pausetrackRect = Rect(240, 20, 50, 50)
nexttrackRect = Rect(310, 20, 160, 50)
multicolourRect = Rect(20, 770, 250, 120)
currentcolourRect = Rect(290, 770, 230, 70)
currentcolouroutlineRect = Rect(290, 770, 230, 70)
currentlocationRect = Rect(290, 850, 230, 40)
toolinfoRect = Rect(1300, 715, 250, 175)
palRect = Rect(20, 770, 250, 120)
brushRect = Rect(20, 660, 80, 80)
trashRect = Rect(120,660, 80, 80)
sprayRect = Rect(220,660, 80, 80)
dropperRect = Rect(320,660,80, 80)
gridRect = Rect(420,660,105,80)
volumesliderRect = Rect (52,90,426,70)
muteRect = Rect (250, 170,30,30)

#Drawing tool outlines
draw.rect(screen, BLUE, pencilRect, 1)
draw.rect(screen, BLUE, eraserRect, 1)
draw.rect(screen, BLUE, fillRect, 1)
draw.rect(screen, BLUE, lineRect, 1)
draw.rect(screen, BLUE, rectRect, 1)
draw.rect(screen, BLUE, circleRect, 1)
draw.rect(screen, BLUE, filledcircleRect, 1)
draw.rect(screen, BLUE, filledrectRect, 1)
draw.rect(screen, BLUE, sticker1Rect, 1 , 10)
draw.rect(screen, BLUE, sticker2Rect, 1, 10)
draw.rect(screen, BLUE, sticker3Rect, 1, 10)
draw.rect(screen, BLUE, sticker4Rect, 1, 10)
draw.rect(screen, BLUE, sticker5Rect, 1, 10)
draw.rect(screen, BLUE, toolinfoRect, 0)
draw.rect(screen, BLUE, undoRect, 1)
draw.rect(screen, BLUE, redoRect, 1)
draw.rect(screen, BLUE, saveRect, 1)
draw.rect(screen, BLUE, insertRect, 1)
draw.rect(screen, BLUE, multicolourRect, 1)
draw.rect(screen, col, currentcolourRect, 0, 10)
draw.rect(screen, BLUE, currentcolouroutlineRect, 1, 10)
draw.rect(screen, BLUE, previoustrackRect, 1, 10)
draw.rect(screen, BLUE, pausetrackRect, 1)
draw.rect(screen, BLUE, nexttrackRect, 1, 10)
draw.rect(screen,BLUE,brushRect,1)
draw.rect(screen,BLUE,trashRect,1)
draw.rect(screen,BLUE,sprayRect,1)
draw.rect(screen,BLUE,dropperRect,1)
draw.rect(screen,BLUE,gridRect,1)
draw.rect(screen,BLUE,volumesliderRect,0,10)
draw.rect(screen,BLUE,muteRect,1,10)


# Audio setup
playlist = ["songs\\avengers_theme.mp3", "songs\\homecoming_theme.mp3", "songs\\black_panther_theme.mp3", "songs\\ant_man_theme.mp3"]
current_track = 0
mixer.music.load(playlist[current_track])
mixer.music.set_volume(0.5)
mixer.music.play()

#setting up volume slider background
volumeText = textFont.render("Volume: " + str(5), True, WHITE)
screen.blit(volumeText, (230, 100))
draw.line(screen, BLACK, (52, 135), (477, 135))
draw.circle(screen, WHITE, (265, 135), 8)


# Initial drawing setup
draw.rect(screen, WHITE, canvasRect)
canvasCap = screen.subsurface(canvasRect).copy()  # Canvas only
col = BLACK
myClock = time.Clock()
running = True
singleclicking = False
drawing = False

#lists for undo, do
undolist = [screen.copy().subsurface(canvasRect)]  #Start undo and redo with a clear canvas
redolist = [screen.copy().subsurface(canvasRect)]

# Main loop
while running:  # 60 times per second
    for evt in event.get():
        if evt.type == QUIT:
            running = False
       
        mx, my = mouse.get_pos()

                        
        if volumesliderRect.collidepoint(mx, my) and 60 < mx < 470 and mb[0]: #min and max vals of the slider
            tool="volume_slider"
            description="Used to adjust volume."
            descriptionlntwo="Maximum 10, minimum 0"
            descriptionlnthree="Enjoy the wonderful hero themes!" #tool descriptions
            
            volVal = floor((((mx - 50) / 410)*10) ) 
            print("volume val is", volVal)
            draw.rect(screen, BLUE, volumesliderRect,0,10)  #redraws the shapes so that slider looks clean
            draw.line(screen, BLACK, (52, 135), (478, 135))
            draw.circle(screen, WHITE, (mx, 135), 8)
            volumeText = textFont.render("Volume: " + str(volVal), True, WHITE) #displays volume
            screen.blit(volumeText, (230, 100))
            mixer.music.set_volume(volVal/10) #scales volume
            
       
        if evt.type == MOUSEBUTTONDOWN and evt.button == 1:  # Check for left click
            
            if nexttrackRect.collidepoint(mx, my): #skips to next track if clicked
                current_track = (current_track + 1) % len(playlist)  # Loop back to first track
                mixer.music.load(playlist[current_track])
                mixer.music.play()
            if previoustrackRect.collidepoint(mx, my): #goes to previous track if clicked
                current_track = (current_track - 1) % len(playlist)  # Loop back to first track
                mixer.music.load(playlist[current_track])
                mixer.music.play()
            if pausetrackRect.collidepoint(mx, my): #pauses and unpauses music
                if mixer.music.get_busy():
                    mixer.music.pause()
                else:
                    mixer.music.unpause()

            ##sets up basic tools and description
            if pencilRect.collidepoint(mx, my):
                tool = "pencil"
                description="Draws a basic 1 pixel line on the canvas."
                descriptionlntwo="Size cannot be adjusted for this tool."
                descriptionlnthree="Colour is changed with the rectangle."
            if eraserRect.collidepoint(mx, my):
                tool = "eraser"
                description="Erases drawn parts, replaces with white."
                descriptionlntwo="Size can be adjusted with scroll wheel."
                descriptionlnthree="Used to get rid of small mistakes."
            if fillRect.collidepoint(mx, my):
                tool = "fill"
                description="Fills screen with a chosen color."
                descriptionlntwo="Colour is changed with the rectangle."
                descriptionlnthree="Used to cover/reset entire screen."
            if lineRect.collidepoint(mx, my):
                tool = "line"
                description="Draws a straight line between 2 points"
                descriptionlntwo="Size can be adjusted with scroll wheel."
                descriptionlnthree="Used to draw shapes."
            if rectRect.collidepoint(mx, my):
                tool = "rectangle"
                description="Draws rectangular shape on canvas"
                descriptionlntwo="Shape is unfilled (hollow)."
                descriptionlnthree="Border can be adjusted with scroll wheel."
            if filledrectRect.collidepoint(mx, my):
                tool = "filled_rectangle"
                description="Draws filled rectangular shape on canvas"
                descriptionlntwo="Completely filled shape."
                descriptionlnthree="Used to cover mistakes and draw."
            if circleRect.collidepoint(mx, my):
                tool = "circle"
                description="Draws circle outline, no fill."
                descriptionlntwo="Size can be adjusted with scroll wheel."
                descriptionlnthree="Used to draw faces and designs."
               
            if filledcircleRect.collidepoint(mx, my):
                tool = "filled_circle"
                description="draws filled in circle, no outline."
                descriptionlntwo="Completely filled in."
                descriptionlnthree="Used for drawing, covering, etc."
            if sticker1Rect.collidepoint(mx, my):
                tool = "sticker1"
                description="Sticker of Iron Man's suit."
                descriptionlntwo="Can be placed anywhere."
                descriptionlnthree="Used for adding themed decoration."

            if sticker2Rect.collidepoint(mx, my):
                tool = "sticker2"
                description="Sticker of Thor and his hammer"
                descriptionlntwo="Position as needed."
                descriptionlnthree="Perfect for adding a heroic touch."

            if sticker3Rect.collidepoint(mx, my):
                tool = "sticker3"
                description="Sticker of Thanos with Gold Armour."
                descriptionlntwo="Movable across the canvas."
                descriptionlnthree="Great for adding a villainous flair."
            if sticker4Rect.collidepoint(mx, my):
                tool = "sticker4"
                description="Sticker of Black Panther leaping."
                descriptionlntwo="Can be placed anywhere on canvas."
                descriptionlnthree="Adds a bold, royal touch to your design."

            if sticker5Rect.collidepoint(mx, my):
                tool = "sticker5"
                description="Sticker of Ant-Man in his suit."
                descriptionlntwo="Positionable anywhere."
                descriptionlnthree="Perfect for a mini hero effect."

            if undoRect.collidepoint(mx, my):
                tool = "undo"
                description="Undoes previous action"
                descriptionlntwo="Used to undo mistakes"
                descriptionlnthree="Great tool for artists"
                #undo functionality, goes to previous screenshot in list if clicked
                if undoRect.collidepoint(mx, my):
                    if len(undolist) > 1:
                        redolist.append(undolist.pop())
                        screen.set_clip(canvasRect)
                        screen.blit(undolist[-1], canvasRect)
                        screen.set_clip(None)
                        
            if redoRect.collidepoint(mx, my):
                tool = "redo"
                description="Redoes previously undone action"
                descriptionlntwo="Used to redo things you undid"
                descriptionlnthree="Useful for accidental undos"
                #redo functionality, goes to next screenshot in list if clicked
                if len(redolist) > 1:
                    undolist.append(redolist.pop())
                    screen.blit(undolist[-1], canvasRect)

            #mute tool, mutes if audio is on, unmutes if already muted                    
            if muteRect.collidepoint(mx, my):
                if muted==True:
                    mixer.music.set_volume(0.5)
                    muted = False
                else:
                    mixer.music.set_volume(0)
                    muted = True
                

            #More tool descriptions and set up
            if brushRect.collidepoint(mx, my):
                tool = "brush"
                description="Allows drawing with variable width."
                descriptionlntwo="Size can be adjusted with scroll wheel."
                descriptionlnthree="Used for creating custom, artistic strokes."


            
                    
            if previoustrackRect.collidepoint(mx, my):
                tool = "previous_track"
                description="Goes to the previous track"
                descriptionlntwo="Plays another Marvel track"
                descriptionlnthree="Heroic music for while you create"      
            if trashRect.collidepoint(mx,my):
                tool = "clear_screen"
                description="Clears the whole screen"
                descriptionlntwo="Gets rid of graphics, drawings, etc."
                descriptionlnthree="Used for reseting for new drawing."
                draw.rect(screen, WHITE, (550, 100, 1000, 600))
            if sprayRect.collidepoint(mx,my):
                tool = "spray"
                description="Sprays random dots in a circle."
                descriptionlntwo="Size can be adjusted with scroll wheel."
                descriptionlnthree="Used for creating graffiti effect"
            if insertRect.collidepoint(mx,my) and evt.button==1:
                filetype = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")])
                uploadimg = image.load(filetype)
                draw.rect(screen,WHITE, canvasRect)
                screen.set_clip(canvasRect)
                screen.blit(uploadimg,(800,450))
                screen.set_clip(None)
            if saveRect.collidepoint(mx,my) and evt.button==1:
                filename=filedialog.asksaveasfilename()
                if "." not in filename:
                    filename += ".png"
                    image.save(screen.subsurface(canvasRect),filename)
            if dropperRect.collidepoint(mx,my):
                tool= "dropper"
                description="Picks colour you're hovered over."
                descriptionlntwo="Can pick any colour from canvas."
                descriptionlnthree="Used to maintain same colours."
            
            if gridRect.collidepoint(mx,my):
                tool="grid"
                description="Draws grid lines on the canvas."
                descriptionlntwo="Makes straight lines"
                descriptionlnthree="Used to maintain same colours."
                for x in range(550, 550 + 1000 + 1, 80):  
                    draw.line(screen, col, (x, 100), (x, 100 + 600))  

                for y in range(100, 100 + 600 + 1, 80):  
                    draw.line(screen, col, (550, y), (550 + 1000, y))
                    
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:  # Left click
                sx, sy = evt.pos  # Starting point for the line
                if tool in ["sticker1", "sticker2", "sticker3", "sticker4", "sticker5", "next_track"]:
                    singleclicking = True
       
            if evt.button == 4:  # Mouse wheel up
                if size < 100:
                    size += 1  # Increase size
            if evt.button == 5:  # Mouse wheel down
                if size > 1:
                    size -= 1  # Decrease size

        if evt.type == MOUSEBUTTONUP and canvasRect.collidepoint(mx, my):
             if evt.button == 1:
                canvasCap = screen.subsurface(canvasRect).copy()  # Screenshot canvas only
                undolist.append(canvasCap)  # Add that copy to the undo list

    mb = mouse.get_pressed()
    canvasx = mx - 550
    canvasy = my - 100
    

    # Tool info and location text
    draw.rect(screen, BLACK, currentlocationRect)  
    draw.rect(screen,BLUE,currentlocationRect,1,10)
    if canvasRect.collidepoint(mx, my):  
        print(f"Current Location: {canvasx}, {canvasy}")
        txt = textFont.render(f"Current Location: {canvasx}, {canvasy}", True, WHITE)
        screen.blit(txt, (300, 860))

    #Tool info
    draw.rect(screen, BLUE, toolinfoRect, 0)
    tooltext = textFont.render(f"Current Tool: {tool}", True, WHITE)
    tooldesc = textFont.render(f"{description}", True, WHITE)
    tooldesclntwo = textFont.render(f"{descriptionlntwo}", True, WHITE)
    tooldesclnthree = textFont.render(f"{descriptionlnthree}", True, WHITE)

    screen.blit(tooltext, (1360, 720))
    screen.blit(tooldesc, (1305, 755))
    screen.blit(tooldesclntwo, (1305, 795))
    screen.blit(tooldesclnthree, (1305, 835))

       
       
           
           

    # Using tools logic (drawing, undo, redo, etc.)
    if canvasRect.collidepoint(mx, my) and mb[0]:
        screen.set_clip(canvasRect)

        if tool == "pencil":
            draw.line(screen, col, (mx, my), (ox, oy))
           
        if tool == "eraser":
            draw.circle(screen, WHITE, (mx, my), size)
        if tool == "fill":
            draw.rect(screen, col, (550, 100, 1000, 600))
        if tool == "line":
            if mb[0]:
                screen.set_clip(canvasRect)
                screen.blit(canvasCap, canvasRect)  
                draw.line(screen, col, (sx, sy), (mx, my), size)
                screen.set_clip(None)
                
        if tool == "rectangle":
            screen.blit(canvasCap, canvasRect)
            width = abs(sx - mx)
            height = abs(sy - my)
            Recttopx = min(mx, sx)
            Recttopy = min(my, sy)
            draw.rect(screen, col, (Recttopx, Recttopy, width, height), size)
        if tool == "circle":
            screen.blit(canvasCap, canvasRect)
            width = abs(sx - mx)
            height = abs(sy - my)
            circletopx = min(mx, sx)
            circletopy = min(my, sy)
            draw.ellipse(screen, col, (circletopx, circletopy, width, height), size)
        if tool == "filled_circle":
            screen.blit(canvasCap, canvasRect)
            width = abs(sx - mx)
            height = abs(sy - my)
            circletopx = min(mx, sx)
            circletopy = min(my, sy)
            draw.ellipse(screen, col, (circletopx, circletopy, width, height), 0)
        if tool == "filled_rectangle":
            screen.blit(canvasCap, canvasRect)
            width = abs(sx - mx)
            height = abs(sy - my)
            Recttopx = min(mx, sx)
            Recttopy = min(my, sy)
            draw.rect(screen, col, (Recttopx, Recttopy, width, height), 0)
        if tool == "brush":
            bigX = mx - ox
            bigY = my - oy
            d = hypot(bigX,bigY)
            d = max(1, d)
            sx = bigX / d
            sy = bigY / d
            for i in range(int(d)):
                draw.circle(screen, col,(ox+sx*i,oy+sy*i), size) #...except that the size can vary
        if tool == "spray":
            for i in range(30):
                rad = randint(1,2)
                x = randint(mx-size*3,mx+size*3)        
                y = randint(my-size*3,my+size*3)
                if dist((mx,my),(x,y))<size*3:
                    draw.circle(screen,col,(x,y),rad)  
                    time.wait(1)
        if tool == "dropper":
            col = screen.get_at((mx, my))


            
       


        if mb[0] and singleclicking:
            if tool == "sticker1":
                screen.blit(sticker1, (mx - 80, my - 125))
                singleclicking = False
            if tool == "sticker2":
                screen.blit(sticker2, (mx - 80, my - 125))
                singleclicking = False
            if tool == "sticker3":
                screen.blit(sticker3, (mx - 80, my - 125))
                singleclicking = False
            if tool == "sticker4":
                screen.blit(sticker4, (mx - 100, my - 90))
                singleclicking = False
            if tool == "sticker5":
                screen.blit(sticker5, (mx - 100, my - 90))
                singleclicking = False
               

    # Color palette selection logic
    if mb[0] and palRect.collidepoint(mx, my):
        col = screen.get_at((mx, my))
        draw.rect(screen, col, currentcolourRect, 0, 10)
        draw.rect(screen, BLUE, currentcolouroutlineRect, 1, 10)

    print(tool)
    print("playlistindex is", current_track)
    print(len(undolist))
    screen.set_clip(None)
    myClock.tick(60)
    display.flip()

    ox, oy = mx, my  # Update the previous mouse position for line drawing

quit()
