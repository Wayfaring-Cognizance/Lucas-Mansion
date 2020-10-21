#Lucas' Mansion, A Text-Based Adventure Game. Soon to be a Point-and-Click Adventure Game!

import pygame

#Starts pygame
pygame.init()

#Create Screen
screen = pygame.display.set_mode((1000, 600))

#Title and Icon
pygame.display.set_caption("Lucas' Mansion")

#Colors and Menues
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.SysFont(None, 25)
open_font = pygame.font.SysFont(None, 80)
top = pygame.Rect(10, 10, 725, 90)
nar = pygame.Rect(10, 50, 725, 30)
char = pygame.Rect(10, 500, 980, 100)
room = pygame.draw.rect(screen, white, (745, 10, 245, 150))
play_screen = pygame.draw.rect(screen, white, (10, 105, 725, 385))
inventory = pygame.draw.rect(screen, white, (745, 170, 245, 320))

#This saved time and lines
def click_clear(obj):
    screen.fill((black), nar)
    screen.fill((black), char)
    screen_text = font.render(obj.look_at, True, white)
    screen.blit(screen_text, (nar))
    pygame.display.update()
def clear():
    screen.fill((black), nar)
    screen.fill((black), char)
    pygame.display.update()
def obj_act(obj):
    screen_text = font.render(obj, True, white)
    screen.blit(screen_text, (char))
    pygame.display.update()
def render():
    clear()
    screen.fill((white), room)
    screen_text = font.render('Items in the ' + rname.name + ':', True, black)
    screen.blit(screen_text, (750, 20))
    screen_text = font.render(rname.ri[0].name, True, black)
    screen.blit(screen_text, (750, 50))
    screen_text = font.render(rname.ri[1].name, True, black)
    screen.blit(screen_text, (750, 80))
    screen_text = font.render(rname.ri[2].name, True, black)
    screen.blit(screen_text, (750, 110))
    screen_text = font.render(rname.ri[3].name, True, black)
    screen.blit(screen_text, (750, 140))
    screen.fill((white), inventory)
    screen_text = font.render('Inventory:', True, black)
    screen.blit(screen_text, (750, 180))
    screen_text = font.render(inv[0].name, True, black)
    screen.blit(screen_text, (750, 210))
    screen_text = font.render(inv[1].name, True, black)
    screen.blit(screen_text, (750, 240))
    screen_text = font.render(inv[2].name, True, black)
    screen.blit(screen_text, (750, 270))
    screen_text = font.render(inv[3].name, True, black)
    screen.blit(screen_text, (750, 300))
    screen_text = font.render(inv[4].name, True, black)
    screen.blit(screen_text, (750, 330))
    screen_text = font.render(inv[5].name, True, black)
    screen.blit(screen_text, (750, 360))
    screen_text = font.render(inv[6].name, True, black)
    screen.blit(screen_text, (750, 390))
    screen_text = font.render(inv[7].name, True, black)
    screen.blit(screen_text, (750, 420))
    screen_text = font.render(inv[8].name, True, black)
    screen.blit(screen_text, (750, 450))
    pygame.display.update()
def add_inv(obj):
    ind = inv.index(nothing)
    if inv[8] != nothing:
        screen.fill((black), nar)
        screen.fill((black), char)
        screen_text = font.render('You can\'t carry anymore...', True, white)
        screen.blit(screen_text, (nar))
    else:
        inv.insert(ind, obj)
        rname.ri.remove(obj)
        render()
    pygame.display.update()
def drop(obj):
    if obj in inv:
        inv.remove(obj)
    if nothing in rname.ri:
        rname.ri.insert(rname.ri.index(nothing), obj)
        render()
    pygame.display.update()
def read(text):
    for i in range(len(text)):
        screen_text = font.render(text[i], True, black)
        screen.blit(screen_text,(15, 110 + 30*(i)))
        pygame.display.update()
        #pygame.time.delay(2000) This is cool and may be good for sometimes... but it's also slow and stops the game. Gets buggy if you try to break it, too.
def useon(self, obj2):
    if obj2 in self.useitem:
        ind = self.useitem.index(obj2)
        clear()
        screen_text = font.render(self.itemreacts[ind], True, white)
        self.useaction()
        screen.blit(screen_text, (char))
        pygame.display.update()
    else:
        clear()
        screen_text = font.render('Nothing happens.', True, white)
        screen.blit(screen_text, (char))
        pygame.display.update()
def clickwithuse(ritem, item, click, b1center, b1):
    try:
        if item.use == True:
            click = item
            useon(click, ritem)
            click.use = False
        elif click.use == True:
            useon(click, ritem)
            click.use = False
        else:
            ritem.click(b1center, b1)
    except AttributeError:
        ritem.click(b1center, b1)

#Object Class and Subclasses
class Object:
    def __init__(self, name, look_at, act1, b1center, b1, b2center = (0, 0), b2 = '', b3center = (0, 0), b3 = '', b4center = (0, 0), b4 = '', act2 = '', act3 = '', act4 = ''):
        self.name = name
        self.look_at = look_at
        self.act1 = act1
        self.act2 = act2
        self.act3 = act3
        self.act4 = act4
        self.b1center = b1center
        self.b1 = b1
        self.b2center = b2center
        self.b2 = b2
        self.b3center = b3center
        self.b3 = b3
        self.b4center = b4center
        self.b4 = b4
        self.use = False
    def click(self, b1center, b1, b2center=(0,0), b2='', b3center=(0,0), b3='', b4center=(0,0), b4=''):
        #MAYBE need 4 or 5 ellipses scoped out so i can just drop their name into below
        screen.fill(white, play_screen)
        if self != nothing:
            click_clear(self)
            pygame.draw.ellipse(screen, (white), (10, 500, 150, 80))
            screen_text = font.render(b1, True, black)
            screen.blit(screen_text, b1center)
            if self.b2 != '':
                pygame.draw.ellipse(screen, (white), (170, 500, 150, 80))
                screen_text = font.render(self.b2, True, black)
                screen.blit(screen_text, self.b2center)
            if self.b3 != '':
                pygame.draw.ellipse(screen, (white), (330, 500, 150, 80))
                screen_text = font.render(self.b3, True, black)
                screen.blit(screen_text, self.b3center)
            if self.b4 != '':
                pygame.draw.ellipse(screen, (white), (490, 500, 150, 80))
                screen_text = font.render(self.b4, True, black)
                screen.blit(screen_text, self.b4center)
            pygame.display.update()
        else:
            click_clear(nothing)
        pygame.display.update()
    def action(self, act):
        clear()
        obj_act(act)
    def itemmove(self, count, b1, item, act1):
        if self.count == 0:
            self.count += 1
            self.b1 = 'Drop'
            self.act1 = self.drpmsg
            render()
            add_inv(self)
        elif rname.ri[0] == nothing or rname.ri[1] == nothing or rname.ri[2] == nothing or rname.ri[3] == nothing:
            self.b1 = 'Take'
            self.act1 = self.takemsg
            drop(self)
            self.count -= 1
        else:
            clear()
            obj_act('Nope, room\'s too full.')
        pygame.display.update()
        
nothing = Object('', 'Nothing here...', '', '', '', '', '', '', '', '', '')
usemsg = 'Use on which item? (Click one in room or inventory)'
used = 'You\'ve already made the magic happen.'

#Bob the GodDarn Bear...
bobtxt1 = ['You take a leap of faith.' , '', '"Bob...?" you say.', '...', '"How do you know my name?" asks the bear.', '"I know Lucas." you say. "He... told me all about you!"', '"Oh!" says the bear, "You\'re a person Lucas has known!', 'Hi! Yes, I\'m Bob. Nice to meet you!"', 'The bear sticks his mighty paw out for a handshake. You oblige.']
bobtxt2 = ['Bob: Man, I can\'t believe Irv broke the pedal plane again.', 'I need to call Lucas\' dad, but I don\'t have his number!', 'You pull out your phone and check your contacts. No luck.', '"Can you ask some of your friends if they have his number?", Bob asks.', 'I don\'t like being inside... everything\'s so small!']
bobtxt3 = ['Bob: Oh, you found his number? Sweet! Uh... can I borrow your phone?', 'You dial up Lucas\' dad, hand Bob your phone, and wait.', 'Bob: Erik! What\'s uuup bro? Hahaha hell yeah man. What? Nah, you\'ve gotta be joshing me.', 'You\'ve gotta be. fuddle sticks no! You ARE! Hahahaha fuddle sticks.', 'Alright, well hey I\'m calling because Irv\'s dumbass broke the pedal plane again.', 'We\'ll be late picking you up. Alright, see you later, king.', 'Bob hangs up and hands back your phone.', 'Bob: Darn, I\'m hungry. I\'mma go eat some candy cron. Thanks again, see ya!']
class bob(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.count = count
    def action(self, act):
        if bob.count == 1 and act == bob.act1:
            read(bobtxt2)
        clear()
        obj_act(act)
bob = bob('Large Bear', 'This guy looks horrifying... and hungry. You can\'t go any further.', 'Lucas wouldn\'t invite a bad bear over. Maybe you could talk him down if you knew his name...', (30, 535), 'Stand Still', (0, 0), '', (0, 0), '', (0, 0), '', 0)

#Starting Inventory Items
cphonetxt1 = ['...', '...', 'He doesn\'t pick up']
cphonetxt2 = ['Of course! You have Lucas\' Dad\'s number!', 'You dial it. Maybe he can help...', 'Lucas\' Dad: Yes, Bob? I\'ve just landed.', 'I\'m down in the yard. I\'ll be there soon.', 'You hang up, no time to loose!']
class cphone(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if lmom.count == 1:
            #Maaaybe add another lmom count so this stopps showing?
            read(cphonetxt2)
            wbyard.ri.insert(wbyard.ri.index(nothing), ldad)
            render()
        if act == cphone.act1 and Ernie in rname.ri and lmom.count != 1:
            clear()
            obj_act('*You call Ernie!* ... Ernie: Jonathan, I\'m right here!')
        if act == cphone.act1 and Ernie not in rname.ri and lmom.count != 1:
            clear()
            obj_act(act)
            read(cphonetxt1)
        if act == usemsg:
            cphone.use = True
            clear()
            obj_act(act)
    def useaction(self):
        if bob.count == 1:
            read(bobtxt3)
            rname.ri.remove(bob)
            bob.count += 1
            bob.look_at = 'Bob is proped up against a wall with candy corn all over his chest.'
            bob.act1 = 'Bob: Ugghhh... I\'m so full.'
            ccpoolr.ri.insert(ccpoolr.ri.index(nothing), bob)
            render()
            cphone.itemreacts[0] = used
        else:
            pass
cphone = cphone('Cell Phone', 'Your trusty cell phone!', 'You call Ernie!', '', (65, 535), 'Call', (225, 535), '', (0, 0), '', (0, 0), '', [bob], ['You tell Bob Lucas\' Dad\'s number.'])

class fmap(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
    def action(self, act):
        if act == fmap.act1:
            img = pygame.image.load(r'Map of First Floor-page000123.jpg')#This works so long as jpg and py files are in same folder.
            screen.blit(img, (145, 105))
            clear()
            obj_act(act)
fmap = fmap('Map of First Floor', 'A map!', 'You look.', (65, 535), 'Look', (0, 0), '', (0, 0), '', (0, 0), '')

#Defining inventory
inv = [cphone, fmap, nothing, nothing, nothing, nothing, nothing, nothing, nothing]

#North Chapel Originating Objects
class Ernie(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, a1, a1center):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.count = count
        self.a1 = a1
        self.a1center = a1center
    def action(self, act):
        clear()
        obj_act(act)
        if act == '' and Ernie.b2 == 'Ask About':
            Ernie.b2 = ''
            Ernie.act1 = 'Bob is a delightful individual. I don\'t know Lucas\' dad\'s number.'
            Ernie.click(Ernie.a1center, Ernie.a1)
        else:
            Ernie.act1 = 'Ernie: Hello, Jonathon.'
#When whatever moves Ernie happens, add a count to Ernie.
Ernie = Ernie('Ernie', 'It\'s Ernie!', 'Ernie: Hello, Jonathon.', '', (55, 535), 'Say hi', (200, 535), '', (0, 0), '', (0, 0), '', 0, 'Bob the Bear', (25, 535))

class b_organ(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.count = count#After als is played on it, it gets a count

#These are set up so that when one goes away, it gives a 1 count to the next one and makes it render in north_chapel.render something to do with use function
bottle_organ = b_organ('Broken Bottle Organ', 'A small, medium, and large bottle are missing from this organ...', 'CLUNK! Perhaps you could find the bottles to play the missing notes...', (65, 535), 'Play', (0, 0), '', (0, 0), '', (0, 0), '', 0)

billytxt1 = ['You inform Berry that there is a large bear outside named Bob who wants.', 'Lucas\' dad\'s phone number.', 'After Berry finishes laughing he lets you program the number into your phone', '"Now just use your phone on Bob", Berry says.', '"I think I\'ve played around enough. It\'s time to get back to searching for Lucas! See ya!']
class Berry(Object):
    def __init__(self, name, look_at, act1, bact1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, a1center, a1):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.bact1 = bact1
        self.act2 = act2
        self.count = count
        self.a1center = a1center
        self.a1 = a1
    def action(self, act):
        clear()
        obj_act(act)
        if Berry.count == 0 and act == Berry.act2:
            Berry.count += 1
            rname.ri[2] = nothing
            render()
            Berry.act1 = Berry.bact1
            obj_act('You attempt to flag Berry down, but he heads West.')
            west_jroom.ri.insert(west_jroom.ri.index(nothing), Berry)
        if Berry.count == 0 and act == Berry.act1:
            Berry.count += 1
            rname.ri[2] = nothing
            render()
            obj_act(act)
            Berry.act1 = Berry.bact1
            west_jroom.ri.insert(west_jroom.ri.index(nothing), Berry)
        elif act == '' and rname != north_chapel:
            Berry.act1 = 'Berry: I miss him...'
            Berry.b2 = ''
            if bob.count == 1:
                Berry.act2 = 'You ask about Bob the Bear'
                Berry.b2 = 'Bob the Bear'
                Berry.b2center = (185, 535)
            if Berry.count != 0:
                Berry.click(Berry.a1center, Berry.a1)
        elif act == 'You ask about Bob the Bear':
            Berry.count += 1
            rname.ri.remove(Berry)
            render()
            read(billytxt1)
            cphone.act2 = usemsg
            cphone.b2 = 'Use'
            rrec_room.ri.insert(rrec_room.ri.index(nothing), Berry)
            Berry.act1 = 'Berry: The answer lies just beyond that door...'
            Berry.bact1 = 'Berry: The answer lies just beyond that door...'
            Berry.act2 = ''
            Berry.b2 = 'Ask about'
        elif act == 'Berry: I miss him...':
            Berry.act1 = Berry.bact1
            Berry.act2 = ''
            Berry.b2 = 'Ask about'

Berry = Berry('Berry', 'Berry looks ready to rock with a leather jacket and long hair.', 'Berry: We have to find Lucas! I\'ll go check the Jam Room.', 'Berry is shredding like the devil himself.', '', (45, 535), 'Speak to', (200, 535), 'Ask about', (0, 0), '', (0, 0), '', 0, (65, 535), 'Lucas')

#Items Origionating in Art Gallery:
class larsport(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
    def action(self, act):
        clear()
        obj_act(act)
larsport = larsport('Portrait of Lucas', 'Do you dare gaze upon the majesty?', 'You don\'t look away for quite some time...', (65, 535), 'Look', (0, 0), '', (0, 0), '', (0, 0), '')

class picframe(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.count = count
picframe = picframe('Picture Frame', 'The frame surrounds a metal sheet with three key pads. An inscription above them reads \"My Best Friends\"', 'You try several combinations of Josh, Matthew, Berry, and Ernie to no avail. Got any other ideas?', (25, 535), 'Try Names', (0, 0), '', (0, 0), '', (0, 0), '',  0)

class bearpaint(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == bearpaint.act1 and picframe.count == 0:
            bearpaint.itemmove(bearpaint.count, bearpaint.b1, bearpaint, bearpaint.act1)
            drop(picframe)
            picframe.count += 1
        if act == bearpaint.act1 and picframe.count == 1:
            bearpaint.itemmove(bearpaint.count, bearpaint.b1, bearpaint, bearpaint.act1)
        else:
            bearpaint.act1 = 'Better not move Lucas\'s picture again...'
        if act == bearpaint.act2:
            bearpaint.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if picframe.count != 2:
            rname.ri.remove(picframe)
            picframe.count -= 1
            bearpaint.itemmove(bearpaint.count, bearpaint.b1, bearpaint, bearpaint.act1)
        if picframe.count == 2:
            rname.ri.remove(picframe)
            bearpaint.itemmove(bearpaint.count, bearpaint.b1, bearpaint, bearpaint.act1)
            bearpaint.itemreacts[0] = used
            bearpaint.act1 = 'Better not move Lucas\'s picture again...'
        else:
            pass
bearpaint = bearpaint('Painting of Bears', 'Lucas has his arms around two bears while another is giving him a noogie. He is elated.', 'You take the picture of Lucas with his bear friends. Maybe you could hang it up in your room!', usemsg, 'Don\'t just leave art lying around!', 'You sure you wanna drop that HERE?', (65, 535), 'Take', (230, 535), 'Use', (0, 0), '', (0, 0), '', 0, [picframe], ['You slide the painting back into place.'])

class cardpile(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
cardpile = cardpile('Pile of Cardboard', 'You refuse to look at this mess. It smells bad.', 'You summon the courage to poke... and then it fades away. No, fuddle sticks this gross pile of cardboard.', (65, 535), 'Poke', (0, 0), '', (0, 0), '', (0, 0), '')

#Marty...
mtxt = ['"Who\'s there?" asks Marty as you walk into his room unannounced.', '"Oh, you a friend of Lucas. He\'s gone now.', 'I told him, I told him \'Run Lucas.\', but he didn\'t listen.', '', 'You don\'t know what to say.', '', '\"Just ask ya questions\", says Marty']
class m(Object):
    def __init__(self, name, look_at, act1, act2, act3, b1center, b1, b2center, b2, b3center, b3, b4center, b4, a1, a1center, a2, a2center, a3, a3center):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.a1 = a1
        self.a1center = a1center
        self.a2 = a2
        self.a2center = a2center
        self.a3 = a3
        self.a3center = a3center
    def action(self, act):
        clear()
        obj_act(act)
        if Marty.act2 == '' and act == Marty.act1:
            read(mtxt)
        if Marty.act2 != '':
            Marty.act1 = 'You awkwardly nod to Marty.'
            Marty.act2 = ''
            Marty.act3 = ''
            Marty.b2 = 'Ask About'
            Marty.b2center = (200, 535)
            Marty.b3 = ''
            Marty.b3center = (0, 0)
        if act == '':
            Marty.act1 = 'Marty: Lucas is one goofy sas motha\'fuddle sticksa.'
            Marty.act2 = 'Marty: Lucas loves them bears. Kicks it wit dem more than me. I ain\'t know they names, though.'
            Marty.act3 = 'Marty: Wha-da WUT?! WHERE?! *Marty proceeds to freak the fuddle sticks out under his bed for a while*'
            Marty.b2 = Marty.a2
            Marty.b2center = Marty.a2center
            Marty.b3 = Marty.a3
            Marty.b3center = Marty.a3center
            Marty.click(Marty.a1center, Marty.a1, Marty.a2center, Marty.a2, Marty.a3center, Marty.a3)           
Marty = m('Marty K.', 'It\'s Lucas\' high school friend Marty! They ran track together.', 'You awkwardly nod to Marty.', '', '', (45, 535), 'Speak to', (200, 535), 'Ask About', (0, 0), '', (0, 0), '', 'Lucas', (65, 535), 'The Art Gallery', (180, 535), 'Black Holes', (350, 535))

#Landing
class gware(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.count = count
    def action(self, act):
        if gware.count == 0:
            gware.count += 1
            drop(sm_bottle)
            gware.act1 = 'Everything in this pile is pretty dusty and gross. Nothing usefull in the least.'
        clear()
        obj_act(act)
gware = gware('Glassware', 'An assortment of jars, bottles, and cups.', 'Hey! One of these bottles might work on the organ down in the Chapel!', (55, 535), 'Search', (0, 0), '', (0, 0), '', (0, 0), '', 0)

class sbottle(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == sm_bottle.act1:
            sm_bottle.itemmove(sm_bottle.count, sm_bottle.b1, sm_bottle, sm_bottle.act1)
        if act == sm_bottle.act2:
            sm_bottle.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if bottle_organ.name == 'Broken Bottle Organ':
            inv.remove(sm_bottle)
            bottle_organ.name = 'Partially Broke Bottle Organ'
            bottle_organ.look_at = 'A couple more bottles are missing...'
            bottle_organ.act1 = 'You play the new key over and over... oh yeah!'
            lg_bottle.itemreacts[0] = 'The stinkey bottle slides right into place! Hopefully the smell will air out...'
            render()
        else:
            pass
sm_bottle = sbottle('Small Glass Bottle', 'A small glass bottle with a little bit of dust.', 'This bottle will definitely fit in the organ.', usemsg, 'Go put it in the organ!', 'I mean... you need this, but okay.', (65, 535), 'Take', (230, 535), 'Use', (0, 0), '', (0, 0), '', 0, [bottle_organ], ['Hell yeah! the bottle slid right into one of the places.'])

#South Chapel Origionating Objects
class pew(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if pew.count == 0:
            pew.act1 = pew.act2
            drop(hymnal)
            pew.count += 1
            render()
        clear()
        obj_act(act)
pew = pew('Pew', 'An old, wooden pew.', 'CREEEEK! You sit down on a hymnal!', 'You have a seat and gaze to the painting of Lucas above...', (70, 535), 'Sit', (0, 0), '', (0, 0), '', (0, 0), '', 0)

class cpew(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if c_pew.count == 0:
            c_pew.act1 = c_pew.act2
            drop(bible)
            c_pew.count += 1
            render()
        clear()
        obj_act(act)
c_pew = cpew('Cracked Pew', 'The pew has a crack down the middle, you but can still sit on it.', 'You have a seat and notice a bible in the book rack in front of you.', 'You have a seat and get real bored.', (70, 535), 'Sit', (0, 0), '', (0, 0), '', (0, 0), '', 0)

class hym(Object):
    def __init__(self, name, look_at, act1, act2, act3, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == hymnal.act1:
            hymnal.itemmove(hymnal.count, hymnal.b1, hymnal, hymnal.act1)
        if act == hymnal.act3:
            hymnal.use = True
        clear()
        obj_act(act)
    def useaction(self):
        pass
hymnal = hym('Hymnal', 'An unusual Hymnal filled with bluegrass tunes.', 'Seems legit', 'This hymnal includes Spring is Here by the Silver String Band...', usemsg, 'Seems legit', 'fuddle sticks Banjo hymns!', (65, 535), 'Take', (225, 535), 'Read', (385, 535), 'Use on', (0, 0), '', 0, [bottle_organ], ['You try to play Spring is Here, but... you really need those three keys.', 'Wacha!'])

bibletext = ['"In the beginning Lucas created Heaven, Earth, and Dions. But the earth was without', 'form and void, and darkness was on the face of the deep. And Lucas said,', '\'Let there be light,\"', 'and there was light. And Lucas saw the light, but thought it was a bit too much, so he', 'said, \'Let there be less light, save energy.\'' 'Then the mortal Stav doth spake,', '\'Lucas, it uses the same amount of energy either way.\' And Lucas said...,', '\'Oh, well fuddle sticks you.\'\"']
class bible(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == bible.act1:
            bible.itemmove(bible.count, bible.b1, bible, bible.act1)
            if c_pew.count == 1:
                drop(blhk)
                c_pew.count += 1
        if act == bible.act2:
            read(bibletext)
        clear()
        obj_act(act)
bible = bible('A Bible', '"In the beginning Lucas created Heaven, Earth, and Dions..."', 'You take the good word... but what\'s that? There was another book behind it!', 'You read some holy words.', 'You take the good word.', 'I mean wasn\'t The Bible pro slavery or something?', (65, 535), 'Take', (225, 535), 'Read', (0, 0), '', (0, 0), '', 0)

blhktext = ['A flip to page one reveals the words \"Irv, Bob, Cyrus\"', 'Each name has a picture beside it. Most of the other pages are blank,', 'perhaps for when Lucas meets more bears.']
class blhk(Object):
    def __init__(self, name, look_at, act1, act2, act3, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == blhk.act1:
            blhk.itemmove(blhk.count, blhk.b1, blhk, blhk.act1)
        if act == blhk.act2:
            read(blhktext)
        if act == blhk.act3:
            blhk.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if rname == art_gall:
            if picframe.count != 2:
                picframe.count += 1
                blhk.itemreacts[0] = used
        elif rname == ebyard_porch and bob.count == 0:
            bob.count += 1
            bob.name = 'Bob the Bear'
            bob.look_at = 'It\'s Bob! Bob\'s a good guy.'
            bob.act1 = 'Bob looks concerned'
            bob.b1 = 'Speak to'
            bob.b1center = (45, 535)
            Ernie.b2 = 'Ask About'
            read(bobtxt1)
            render()
            blhk.itemreacts[1] = used
blhk = blhk('Bears Lucas Has Known', 'Lucas and three bears pose on the cover of this book. You\'ve never seen Lucas this happy...', 'How could you not?', 'Pulsing with excitement, you open the book...', usemsg, '\'Bout time. Can\'t belive you droped it.', 'Probably a mistake, but okay...', (65, 535), 'Take',  (225, 535), 'Read', (390, 535), 'Use', (0, 0), '', 0, [picframe, bob], ['Of course! Lucas\' three bear friends! You type in the names and hear a click to the north...', 'You look through Bears Lucas Has Known. This bear looks most like Bob.'])

#Epic Beard Dunkin Man
ebdmantxt1 = ['EBDM: Oh, hey dude! What\'s up? So Lucas is missing, huh?', 'He promised me a banjo! He said it was done, but forgot to get it to me', 'before the Microwave Dave concert. Can you find it?', 'I\'ll go open up the lab if you do.']
class ebdman(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if ebdman.count == 0:
            read(ebdmantxt1)
            ebdman.count += 1
        clear()
        obj_act(act)
ebdman = ebdman('Epic Beard Dman', 'His beard is still long and slicked into a point.', 'It\'s supposed to be the sickest banjo ever!', 'EBDM: Thanks for finding this bad sas banjo for me!', (45, 535), 'Speak to', 0)

#Items Origionating in the Jam Room(s):
class ctbanj(Object):
    def __init__(self, name, look_at, act1, act2, act3, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3)
        self.act2 = act2
        self.act3 = act3
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == ctbanj.act1:
            ctbanj.itemmove(ctbanj.count, ctbanj.b1, ctbanj, ctbanj.act1)
        if act == ctbanj.act3:
            ctbanj.use = True
        clear()
        obj_act(act)
    def useaction(self):
        inv.remove(ctbanj)
        render()
ctbanj = ctbanj('Cookie Tin Banjo', 'A quality cookie tin banjo made by Lucas himself!', 'Rock on!', 'You try, you really do...', usemsg, 'Follow your dreams!', 'Are banjos even cool anymore?', (65, 535), 'Take',  (225, 535), 'Play', (390, 535), 'Use', 0, [ebdman], ['EBDM: Nah man that thing\'s basic as fuddle sticks. I\'ll hold onto it for safe keeping, though.'])

class drums(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
drums = drums('Drum Kit', 'A pretty sick drum kit with Lucas\' name in large, block letters on the front.', 'You try to twirl a drumstick around your fingers. It flys up and hits you in the face.', (25, 535), 'Tap Da Rims!', (0, 0), '', (0, 0), '', (0, 0), '')

class hanjo(Object):
    def __init__(self, name, look_at, act1, act2, act3, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3)
        self.act2 = act2
        self.act3 = act3
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == hanjo.act1:
            hanjo.itemmove(hanjo.count, hanjo.b1, hanjo, hanjo.act1)
        if act == hanjo.act3:
            hanjo.use = True
        clear()
        obj_act(act)
    def useaction(self):
        inv.remove(hanjo)
        render()
hanjo = hanjo('Hanjo', 'It\'s a harp-banjo combo!', 'Hell Yeah!', 'You never learned how to give a hanjo...', usemsg, 'Maybe an Angel will want to buy this off you.', 'Aw...', (65, 535), 'Take',  (225, 535), 'Play', (390, 535), 'Use', 0, [ebdman], ['EBDM: Getting there... this thing is sick, but not sick enough. I\'ll hold onto it for safe keeping.'])

#Foyer
class stairway(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
    def action(self, act):
        global rname
        if rname == foyer:
            rname = landing
            render()
            clear()
            obj_act(stairway.act1)
        elif rname == landing:
            rname = smithse
            render()
            clear()
            obj_act(stairway.act2)
stairway = stairway('Stairway', 'A roaring bear head decorates the top of a large stairway.', 'You climb up to the second floor landing...', 'You climb further to... an empty Smith\'s entrance??', (60, 535), 'Climb', (0, 0), '', (0, 0), '', (0, 0), '')

#Candy Cron Pool Room:
class ccpool(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
ccpool = ccpool('Candy Cron Pool', 'A giant pool of candy corn...', 'It\'d mess up your hair.', (50, 535), 'Jump in', (0, 0), '', (0, 0), '', (0, 0), '')

#West Backyard Items:
class b_pedal_p(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
b_pedal_p = b_pedal_p('Broken Pedal Plane', 'The landing gear and the propeller need patching...', 'No can do.', (70, 535), 'Fly', 0)

class scrap(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
scrap = scrap('Scrap', 'Nothing of value here.', 'Nah, you don\'t want this shoot.', (65, 535), 'Take')

#Items in Kitchen(s):

class stove(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
stove = stove('Stove', 'A very nice gas stove.', 'No time for a snack! Gotta find Lucas!', (65, 535), 'Cook', (0, 0), '', (0, 0), '', (0, 0), '')

robotxt1 = ['Robot: Hello, human. I am the cook.', 'The Robot\'s eyes blare red with each word.', 'I am proficient in Ma Pao Tofu,', 'Cheese Pizza in the style of Dions, and Larsghetti.', 'I will also stir fry anything. Now what is thy bidding?'] 
robotxt2 = ['Robot: Spaghetti and sauce, please. All Hail Lucas', '...', 'The Robot goes back into standby.']
robotxt3 = ['Robot: Of course. I can make Larsghetti just the way Lucas does,', 'only I am out of ingredients. Normally I could find them on the third floor,', 'but with the pedal plane out of commission I can do nothing.', 'If you can find spaghetti and sauce, use them on me. All Hail Lucas.', '...', 'The robot goes into standby.']
robotxt4 = ['Robot: Oh good, now I can make Larsghetti.', 'The Robot goes to work like a painter at his easel.', 'You stand back. It is truly, truly a pleasure watching it work.', 'Robot: Here you go. All Hail Lucas.', '...', 'The robot goes back into standby.']
robotxt5 = ['Robot: bring me the other thing... the one I asked for that you haven\'t brought!', 'I could tell you what it is, but coding this game has taken long enough.', 'All Hail Lucas', '...', 'The Robot goes back into standby.']
robotxt6 = ['Robot: I am done cooking for you. Go find Lucas, all hail his name!', '...', 'The Robot goes back into standby.']
class robot(Object):
    def __init__(self, name, look_at, act1, act2, act3, act4, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, a1center, a1, a2center, a2, a3center, a3, a4center, a4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.act4 = act4
        self.count = count
        self.a1center = a1center
        self.a1 = a1
        self.a2center = a2center
        self.a2 = a2
        self.a3center = a3center
        self.a3 = a3
        self.a4center = a4center
        self.a4 = a4
    def action(self, act):
        clear()
        obj_act(act)
        if robot.count == 0 and robot.act2 == '':
            read(robotxt1)
        if robot.count == 1 and robot.act2 == '':
            read(robotxt2)
        if robot.count == 2 and robot.act2 == '':
            read(robotxt5)
        if robot.count == 3:
            read(robotxt6)
        if act == 'This seems to be the question he was looking for...':
            read(robotxt3)
            robot.count += 1
            robot.act1 = 'The robot\'s back straightens and its eyes light up red.'
            robot.act2 = ''
            robot.act3 = ''
            robot.act4 = ''
            robot.b2 = 'Ask About'
            robot.b2center = (200, 535)
            robot.b3 = ''
            robot.b3center = (0, 0)
            robot.b4 = ''
            robot.b4center = (0, 0)
        if robot.act2 != '':
            robot.act1 = 'The robot\'s back straightens and its eyes light up red.'
            robot.act2 = ''
            robot.act3 = ''
            robot.act4 = ''
            robot.b2 = 'Ask About'
            robot.b2center = (200, 535)
            robot.b3 = ''
            robot.b3center = (0, 0)
            robot.b4 = ''
            robot.b4center = (0, 0)
        if act == '':
            robot.act1 = 'This seems to be the question he was looking for...'
            robot.act2 = 'Robot: Only Lucas himself, all hail his name, can request this from me.'
            robot.act3 = 'Soooo... Dions? I actually don\'t want to make pizza anymnore. Want to go to Dions...'
            robot.act4 = 'Robot: Lucas is God. God is Lucas.'
            robot.b2 = robot.a2
            robot.b2center = robot.a2center
            robot.b3 = robot.a3
            robot.b3center = robot.a3center
            robot.b4 = robot.a4 
            robot.b4center = robot.a4center
            robot.click(robot.a1center, robot.a1, robot.a2center, robot.a2, robot.a3center, robot.a3, robot.a4center, robot.a4)
robot = robot('Robot Cheif', 'A humoniod robot with \"Fabrecious-Olson 5,000\" on the back of its head.', 'The robot\'s back straightens and its eyes light up red.', '', '', '', (45, 535), 'Speak to', (200, 535), 'Ask about', (0, 0), '', (0, 0), '', 0, (35, 535), 'Larsghetti', (190, 535), 'Ma Pao Tofu', (355, 535), 'Cheese Pizza', (545, 535), 'Lucas')

class lrsg(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == lrsg.act1:
            lrsg.itemmove(lrsg.count, lrsg.b1, lrsg, lrsg.act1)
        if act == lrsg.act2:
            inv.remove(lrsg)
            render()
        clear()
        obj_act(act)
lrsg = lrsg('Larsghetti', 'Mmmm... just the way Lucas likes it!', 'Don\'t mind if you do!', 'You eat it all. Lvl Up!', 'Why\'d you drop it? It\'s not hot anymore!', 'Um, hope you put it on a table at least...', (65, 535), 'Take', (225, 535), 'Use', 0)

class fridge(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
fridge = fridge('Refrigerator', 'A large, old refrigerator with grimey spots near the handles', 'It\'s filled with cheese, peanut butter, condiments, and sauces. Most of it is expired.', (65, 535), 'Open', (0, 0), '', (0, 0), '', (0, 0), '')  
        
class cabinet(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
    def action(self, act):
        rname.ri.remove(cabinet)
        drop(plate)
        clear()
        obj_act(act)
cabinet = cabinet('Cabinet', 'A dusty cabinet with one of the doors hanging open.', 'You open the other cabinet door to find a single plate.', (65, 535), 'Open', (0, 0), '', (0, 0), '', (0, 0), '')

class drawer(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
    def action(self, act):
        rname.ri.remove(drawer)
        drop(tinfoil)
        drop(pwrap)
        clear()
        obj_act(act)
drawer = drawer('A Drawer', 'A drawer you can slide open and closed. Real exciting!', 'You slide open the drawer to find... some tin foil!', (65, 535), 'Open', (0, 0), '', (0, 0), '', (0, 0), '')
        
class plate(Object):
    def __init__(self, name, look_at, act1, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if plate.b1 == 'Drop':
            inv.remove(plate)
            render()
        elif act == plate.act1:
            plate.itemmove(plate.count, plate.b1, plate, plate.act1)
        clear()
        obj_act(act)
plate = plate('Plate', 'Plate...', 'This would be perfect for eating things off of!', 'You love plate.', 'You droped it, so it broke...', (65, 535), 'Take', (0, 0), '', (0, 0), '', (0, 0), '', 0)
    
class tinfoil(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == tinfoil.act1:
            tinfoil.itemmove(tinfoil.count, tinfoil.b1, tinfoil, tinfoil.act1)
        clear()
        obj_act(act)
        #maybe give this a use as a red herring for pedal plane idk.
tinfoil = tinfoil('Tin Foil', 'A roll of tin foil. It could cover leftovers... but perhaps it has some other use?', 'Never know when you could... use some tine foil...?', usemsg, 'Oh boy. We got dat tin foil again!', 'Like, why were you running around with tin foil?', (65, 535), 'Take', (230, 535), 'Use', (0, 0), '', (0, 0), '', 0)

class pwrap(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.b2center = b2center
        self.b2 = b2
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == pwrap.act1:
            pwrap.itemmove(pwrap.count, pwrap.b1, pwrap, pwrap.act1)
        if act == pwrap.act2:
            pwrap.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if b_pedal_p.name == 'Less Broke Pedal Plane':
            inv.remove(pwrap)
            b_pedal_p.name = 'Pedal Plane'
            b_pedal_p.look_at = 'Lucas\'s pedal plane in all it\'s glory.'
            b_pedal_p.act1 = 'You don\'t know how... ask Irv!'
            b_pedal_p.count += 1
            pwrap.itemreacts[0] = used
            render()
        else:
            pass
pwrap = pwrap('Plastic Wrap', 'Some good ole\' ... plastic wrap...!', 'Might need to cover some leftovers or some shoot.', usemsg, 'You rap about plastic', 'fuddle sticks leftovers', (65, 535), 'Take', (230, 535), 'Use', 0, [b_pedal_p], ['You do not feel the spirit of Lucas... try wood first.'])

#Items in the Laboratory:
swolftxt1 = ['With weary eyes, none other than Stephan Wolfram greets you.', 'Wolfram: Hello. Somehow the way into the Robot Recreation Room has been sealed off...', 'I don\'t know when this could have happened, but I need to get in there.', 'The computer inside has a large portion of my research and it is the only one capable of', 'running the robots in this house.', 'If I had some thermite, I could melt that wall down, but all I have is the magnesium strip', 'If you can find some iron oxide (rust) and aluminum dust, I can ignite them.']
swolftxt2 = ['Wolfram: These will do nicely.', 'Stephen Wolfram goes to work. You stand back in awe as he perfectly sets and ignites', 'the thermite. In a glorious flash of white and flame, the wall crumbles and melts away...']
class swolf(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if swolf.count == 0:
            read(swolftxt1)
            swolf.count += 1
        if swolf.count == 2 and rshavings.act2 == '' and adust.act2 == '':
            swolf.count += 1
            read(swolftxt2)
        clear()
        obj_act(act)
swolf = swolf('Stephen Wolfram', 'This is Stephen Wolfram, the creator of Wolfram Alpha.', 'Wolfram: Your help is highly appretiated.', 'Thanks again for your help. Please get to the bottom of whatever is going on here...', (45, 535), 'Speak to', 0)

class hdgrind(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
hdgrind = hdgrind('Heavy Duty Grinder', 'This device grinds large amounts of metal into dust', 'You don\'t have anything to put in. Maybe find a bunch of rust or aluminium.', 'Your work here is done.', (60, 535), 'Grind')

class adust(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == adust.act1:
            adust.itemmove(adust.count, adust.b1, adust, adust.act1)
        if act == adust.act2:
            adust.use = True
        clear()
        obj_act(act)
    def useaction(self):
        swolf.count += 1
        if adust in inv:
            inv.remove(adust)
        if adust in rname.ri:
            rname.ri.remove(adust)
        adust.act2 = ''
        render()
        if swolf.count == 3:
            read(swolftxt2)
adust = adust('Aluminum Dust', 'Very fine Aluminum.', 'This will be hard to pic up if dropped.', usemsg, 'It\'s tough, but you scrape up a good amount.', 'You let it slip between your fingers...', (65, 535), 'Take', (225, 535), 'Use', 0, [swolf], ['Wolfram: Ah! Thank you!'])

#Items in Guest Bed and Bath 02:
nicktxt1 = ['Nathaniel: Hey, Josh! Lucas gave me enough money to finally start my own business!', 'It\'s not what you think. I\'ve opened Denmark\'s first Cici\'s franchise!', 'Best pizza in Denmark. Wanna go?']
nicktxt2 = ['A bus rolls up outside and Nathaniel climbs aboard. As you board, you notice', 'the driver is a bear. You assume the bear must be a good driver since the bus is full,', 'so you climb on. Stav is on the bus! You talk to him about math', 'and have a good time eating at Cici\'s with Nathaniel.', 'You and Stav both agree that there MUST be better pizza in Denmark.', 'Stav gets off at the airport and the bus drops you of at The Foyer']
nicktxt3 = ['Nathaniel: Reneger... I knew it! You\'re no better than Wes!!', 'You will go to Cici\'s... just wait.']
nicktxt4 = ['You climb aboard, but this time a man is driving the bus.', 'Stav is back in Wisconsin.', 'You wonder why you agreed to this...']
nicktxt5 = ['You regret this immediately. You\'ve had Cici\'s 3 times', 'in one day. Congratulations. Nathaniel seems happy, at least.', 'Your stomach is not.', 'The bus drops you back off at The Foyer.', 'Now stop eating cheap pizza and go find Lucas!']
nicktxt6 = ['Nathaniel: I knew it! I fuddle sticksing knew it!!', 'You\'re not better than Wes after all! RENEGER!!!', 'I\'ll get you!', 'The bust drops you off back at The Foyer']
nicktxt7 = ['You really should have come with me to Cici\'s...', 'but for now why don\'t you join Lucas beyond this door.', 'Nathaniel pushes open the ornate wooden door. Reluctantly, you go inside.',  'This lavish bedroom features a bed with a canopy and an antique desk.', 'At the desk sits...', 'No. No! It can\'t be!!', 'It\'s SAD.']
nicktxt8 = ['SAD stands up, claps his hands, and produces his infamous laugh.', 'SAD: AHUH HUH HUH HUH HUH! It\'s about time, Josh!', 'Have you enjoyed the traps I set up for you? And now, behold your god!!', 'SAD points to Lucas. He is writing on the floor in front of a TV screen.', 'The TV is playing The Nutty Professor\'s transformation back into a fat man on loop.', 'SAD: Remember when you said you\'d make a mansion with a bunch of traps for me?', 'Oohhh how the times CHANGE! SAD claps and laughs again.', 'SAD: This isn\'t Lucas\' mansion. IT\'S MINE! And even if you win, YOU LOSE!!', 'SAD nods to Nathaniel who nods.', 'Nathaniel throws his hat and it knocks you out a window and down into the yard below...', 'Cyrus the Bear barely breaks your fall.']
nicktxt9 = ['Nathaniel: Hey, Josh. Wanna try some of this Il Vicino pizza?', 'I brought it all the way from Albuquerque on the pedal plane! It\'s still hot...', 'You try some. It\'s been a while since you had Il Vicino and it sure beats', 'the hell out of Cici\'s.', 'Nathaniel: HA! That was Cici\'s pizza! This is The Josh Affair, you reneger!!!', 'As you look across the room, everyone is... laughing.', 'Even the robots. Even the bears outside are roaring. This is awful!', 'You\'re finished!']
class Nathaniel(Object):
    def __init__(self, name, look_at, act1, act2, act3, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.count = count
    def action(self, act):
        global rname
        #Setting up yes and no
        if act == Nathaniel.act1 and rname == gbed02:
            Nathaniel.look_at = 'Nathaniel tapps his foot, awaiting your answer...'
            Nathaniel.b1 = 'Yes'
            Nathaniel.b1center = (70, 535)
            Nathaniel.act1 = 'Nathaniel: Awesome! Meet you at The Foyer, we\'ll take a bus.'
            Nathaniel.b2 = 'No'
            Nathaniel.b2center = (235, 535)
            Nathaniel.act2 = 'Nathaniel: You\'re really missing out... I guess you don\'t need this bathroom, then!'
            Nathaniel.click(Nathaniel.b1center, Nathaniel.b1, Nathaniel.b2center, Nathaniel.b2)
            read(nicktxt1)
        #First yes or no
        if act == Nathaniel.act1 and Nathaniel.act2 != '' and rname == gbed02:
            Nathaniel.count += 1
            rname.ri.remove(Nathaniel)
            foyer.ri.insert(foyer.ri.index(nothing), Nathaniel)
            render()
            screen.fill((white), play_screen)
            Nathaniel.act1 = 'Nathaniel: good, the bus is here.'
            Nathaniel.act2 = 'Nathaniel walks away, jilted.'
            Nathaniel.look_at = 'Nathaniel: Ready to go?'
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and rname == gbed02:
            screen.fill((white), play_screen)
            clear()
            obj_act(act)
        #First foyer yes or no
        if act == Nathaniel.act1 and Nathaniel.count == 1 and rname == foyer:
            rname.ri.remove(Nathaniel)
            a2.ri.insert(a2.ri.index(nothing), Nathaniel)
            Nathaniel.count += 1
            Nathaniel.look_at = 'Nathaniel: I was just looking for something to eat, but nothing beats Cici\'s. Wanna go?'
            Nathaniel.act1 = 'Nathaniel: Awesome! I\'ll meet you in The Foyer again.'
            Nathaniel.act2 = 'Nathaniel: Getting cold feet already, huh...?'
            render()
            read(nicktxt2)
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and Nathaniel.count == 1 and rname == foyer:
            rname.ri.remove(Nathaniel)
            rrec_room.ri.insert(rrec_room.ri.index(nothing), Nathaniel)
            Nathaniel.act1 = 'You Lose.'
            Nathaniel.b1 = 'Talk'
            Nathaniel.b1center = (65, 535)
            Nathaniel.b2 = ''
            Nathaniel.look_at = 'It\'s Nathaniel! He\'s wearing his trademark cap.'
            render()
            read(nicktxt3)
            clear()
            obj_act(act)
        #Second yes or no
        if act == Nathaniel.act1 and rname == a2:
            rname.ri.remove(Nathaniel)
            Nathaniel.count += 1
            foyer.ri.insert(foyer.ri.index(nothing), Nathaniel)
            render()
            screen.fill((white), play_screen)
            Nathaniel.act1 = 'Nathaniel: Good, the bus is back.'
            Nathaniel.act2 = 'Nathaniel walks away, jilted.'
            Nathaniel.look_at = 'Nathaniel: Alright, ready to go?'
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and rname == a2:
            rname.ri.remove(Nathaniel)
            render()
            screen.fill((white), play_screen)
            clear()
            obj_act(act)
        #Second Foyer yes or no
        if act == Nathaniel.act1 and Nathaniel.count == 3 and rname == foyer:
            rname.ri.remove(Nathaniel)
            east_jroom.ri.insert(east_jroom.ri.index(nothing), Nathaniel)
            Nathaniel.count += 1
            render()
            screen.fill((white), play_screen)
            read(nicktxt4)
            Nathaniel.look_at = 'Nathaniel: Wanna go to Cici\'s one more time before the game ends?'
            Nathaniel.act1 = 'Nathaniel: Sweet! You know the drill, meet me in The Foyer.'
            Nathaniel.act2 = 'Nathaniel: ... you\'re a better man than most, Josh. At least we won\'t have to have... A Josh Affair.'
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and Nathaniel.count == 3 and rname == foyer:
            rname.ri.remove(Nathaniel)
            rrec_room.ri.insert(rrec_room.ri.index(nothing), Nathaniel)
            Nathaniel.act1 = 'You Lose.'
            Nathaniel.b1 = 'Talk'
            Nathaniel.b1center = (65, 535)
            Nathaniel.look_at = 'It\'s Nathaniel! He\'s wearing his trademark cap.'
            Nathaniel.b2 = ''
            render()
            read(nicktxt3)
            clear()
            obj_act(act)
        #Final non foyer yes or no
        if act == Nathaniel.act1 and rname == east_jroom:
            rname.ri.remove(Nathaniel)
            Nathaniel.count += 1
            foyer.ri.insert(foyer.ri.index(nothing), Nathaniel)
            render()
            screen.fill((white), play_screen)
            Nathaniel.act1 = 'Nathaniel: Awesome! You won\'t regret this, Josh.'
            Nathaniel.act2 = 'Nathaniel walks off infuriated, mumbling a name which sounds all too familiar...'
            Nathaniel.look_at = 'Nathaniel:... I was beginning to think you\'d forgotten your promise. Ready to go?'
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and rname == east_jroom:
            rname.ri.remove(Nathaniel)
            render()
            screen.fill((white), play_screen)
            clear()
            obj_act(act)
        #Final yes or no (Foyer)
        if act == Nathaniel.act1 and Nathaniel.count == 5 and rname == foyer:
            rname.ri.remove(Nathaniel)
            master_b.ri.insert(master_b.ri.index(nothing), Nathaniel)
            Nathaniel.b1 = 'Speak to'
            Nathaniel.b1center = (45, 535)
            Nathaniel.b2 = ''
            Nathaniel.look_at = 'It\'s Nathaniel! He\'s wearing his trademark cap.'
            Nathaniel.act1 = 'Nathaniel shruggs and points to Lucas\'s mom'
            render()
            screen.fill((white), play_screen)
            read(nicktxt5)
            clear()
            obj_act(act)
        if act == Nathaniel.act2 and Nathaniel.count == 5 and rname == foyer:
            master_b.ri.insert(master_b.ri.index(nothing), sad)
            Nathaniel.count += 1
            rname.ri.remove(Nathaniel)
            render()
            screen.fill((white), play_screen)
            read(nicktxt6)
            rrec_room.ri.insert(rrec_room.ri.index(nothing), Nathaniel)
            Nathaniel.act1 = 'Nathaniel: It\'s about time you came here, Josh. Too bad it\'s too late.'
            Nathaniel.act2 = ''
            Nathaniel.look_at = 'Nathaniel: It\'s about time you came here, Josh. Too bad it\'s too late.'
            Nathaniel.b1center = (65, 535)
            Nathaniel.b1 = 'Talk'
            Nathaniel.b2 = ''
            clear()
            obj_act(act)
        if rname == rrec_room and Nathaniel.count == 1 or rname == rrec_room and Nathaniel.count == 3:
            Nathaniel.count += 1
            Nathaniel.act1 = 'Nathaniel: Haha! I bet you thought you\'d actually lost! Go finish the game already.'
            read(nicktxt9)
        if rname == rrec_room and Nathaniel.count == 2 or rname == rrec_room and Nathaniel.count == 4:
            clear()
            obj_act(act)
        if Nathaniel.b1 == 'Oof':
            rname = wbyard_porch
            render()
            screen.fill((white), play_screen)
            clear()
            obj_act('You Fall...')
        if Nathaniel.b1 == 'Continue':
            rname.ri.remove(Nathaniel)
            master_b.ri.insert(master_b.ri.index(nothing), Nathaniel)
            rname = master_b
            render()
            Nathaniel.count += 1
            cyrus.count += 1
            cyrus.act1 = 'Thank you for your time, Mr. Tennison.'
            Nathaniel.b1 = 'Oof'
            Nathaniel.b1center = (70, 535)
            Nathaniel.click(Nathaniel.b1center, Nathaniel.b1)
            read(nicktxt8)
        if rname == rrec_room and Nathaniel.count == 6:
            Nathaniel.b1 = 'Continue'
            Nathaniel.b1center = (45, 535)
            Nathaniel.look_at = 'Nathaniel cackles in the distance'
            Nathaniel.click(Nathaniel.b1center, Nathaniel.b1)
            read(nicktxt7)
        if Nathaniel in master_b.ri and Nathaniel.count == 5:
            clear()
            obj_act(act)
Nathaniel = Nathaniel('Nathaniel', 'It\'s Nathaniel! He\'s wearing his trademark cap.', 'Nathaniel seems happy to see you.', '', '', (45, 535), 'Speak to', (0, 0), '', (0, 0), '', (0, 0), '', 0)

class sink(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
sink = sink('Non-Disgusting Sink', 'This sink works and looks somewhat clean.', 'You wash your hands and have horror flashbacks of 2020...', (50, 535), 'Wash Up', (0, 0), '', (0, 0), '',(0, 0), '')

class toilet(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
toilet = toilet('Toilet', 'This toilet has a slight ring around it, but other than that it appears usable.', 'Guess it has been a while since you had the chance...', (30, 535), 'Take a shoot', (0, 0), '', (0, 0), '', (0, 0), '')

#Items in Guest Room and Bath 01:
class trash(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
trash = trash('Trash', 'You can\'t tell where it begins and where it ends...', 'Not worth it. Sorry Lucas!', (55 ,535), 'Search', (0, 0), '', (0, 0), '', (0, 0), '')

class cupboard(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if cupboard.count == 2:
            cupboard.count -= 1
            cupboard.act1 = 'No time to nap!'
            cupboard.b1 = 'Close'
            cupboard.b1center = (65, 535)
        elif cupboard.count == 1:
            cupboard.count += 1
            cupboard.act1 = 'There is a pillow and some sheets in here. Cozy.'
            cupboard.b1 = 'Open'
            cupboard.b1center = (60, 535)
        elif cupboard.count == 0:
            drop(lg_fbottle)
            cupboard.count += 1
            cupboard.act1 = 'No time to nap!'
            cupboard.b1 = 'Close'
            cupboard.b1center = (60, 535)
        clear()
        obj_act(act)
cupboard = cupboard('Cupboard', 'A long cupboard with a door slightly ajar,', 'There is a pillow and some sheets in here along with a bottle full of an amber liquid.',  'No time to nap!', (65, 535), 'Open', (0, 0), '', (0, 0), '', (0, 0), '', 0)

class rsink(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
rsink = rsink('Rusty Sink', 'The drain does not appear to work. Stagnant water rests at the bottom.', 'Better not add more water. This sink is already disgusting.', (50, 535), 'Wash Up', (0, 0), '', (0, 0), '', (0, 0), '')

class lg_fbottle(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == lg_fbottle.act1:
            lg_fbottle.itemmove(lg_fbottle.count, lg_fbottle.b1, lg_fbottle, lg_fbottle.act1)
        if act == lg_fbottle.act2:
            lg_fbottle.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if rname != gbath01:
            drop(lg_bottle)
            inv.remove(lg_fbottle)
            render()
lg_fbottle = lg_fbottle('Large Full Bottle', 'A large bottle with an amber liquid inside... ', 'This is one of Lucas\' rooms... sure you wanna take this?', usemsg, 'Oh god. You picked up the pee bottle again.', 'Phew.', (65, 535), 'Take', (230, 535), 'Use', (0, 0), '', (0, 0), '', 0, [sink, toilet, rsink], ['You pour piss down the sink, you animal. Everything wreaks now.', 'You hold your nose as you empty the bottle into the toilet and flush. Well done!', 'The last thing this sink needs... is this bottle'])

class lg_bottle(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == lg_bottle.act1:
            lg_bottle.itemmove(lg_bottle.count, lg_bottle.b1, lg_bottle, lg_bottle.act1)
        if act == lg_fbottle.act2:
            lg_bottle.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if bottle_organ.name == 'Partially Broke Bottle Organ':
            inv.remove(lg_bottle)
            bottle_organ.name = 'Another Broke Bottle Organ'
            bottle_organ.look_at = 'Missing just ONE more bottle!'
            bottle_organ.act1 = 'Still missing one note... you glare at it rather than playing.'
            md_bottle.itemreacts[0] = 'You slide the final bottle into place. You fixed the organ!! It sits before you in full glory.'
            render()
        else:
            pass
lg_bottle = lg_bottle('Large Bottle', 'A large bottle. It still kinda stinks...', 'Still pretty gross, yo.', usemsg, 'Still gross.', 'Good riddance!', (65, 535), 'Take', (230, 535), 'Use', (0, 0), '', (0, 0), '', 0, [bottle_organ], ['It\'ll be better if you find the small bottle first...'])

class rshavings(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == rshavings.act1:
            rshavings.itemmove(rshavings.count, rshavings.b1, rshavings, rshavings.act1)
        if act == rshavings.act2:
            rshavings.use = True
        clear()
        obj_act(act)
    def useaction(self):
        swolf.count += 1
        inv.remove(rshavings)
        rshavings.act2 = ''
        render()
        if swolf.count == 3:
            read(swolftxt2)
rshavings = rshavings('Rust Shavings', 'fine rust sits caked around the sink', 'gross... okay.', usemsg, 'I mean... thermite? I guess? Is what you\'re thinking?', 'Now use some purel', (65, 535), 'Take', (225, 535), 'Use', 0, [swolf], ['Wolfram: Ah! Thank you for finding this.'])

class towel(Object):
    def __init__(self, name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
towel = towel('Towel', 'Proof that Lucas can plan!', 'No, leave it. The world must know...', (65, 535), 'Take', (0, 0), '', (0, 0), '', (0, 0), '')


#shoot in Banjo Workshop:
class wood(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == wood.act1:
            wood.itemmove(wood.count, wood.b1, wood, wood.act1)
        if act == wood.act2:
            wood.use = True
        clear()
        obj_act(act)
    def useaction(self):
        inv.remove(wood)
        b_pedal_p.name = 'Less Broke Pedal Plane'
        b_pedal_p.look_at = 'That propeller still needs to patching...'
        pwrap.itemreacts[0] = 'The power of Lucas flows through you as somehow... the plastic wrap makes the plane work.'
        b_pedal_p.count += 1
        render()
wood = wood('Scrap Wood', 'Some pieces of wood varying in length, waiting to be touched by Lucas\' hand.', 'Can\'t ever have too much scrap wood.', usemsg, 'How very Lucas of you to keep this.', 'I mean, why were you just carrying around some wood?', (65, 535), 'Take', (230, 535), 'Use', 0, [b_pedal_p], ['You pray to Lucas for inspiration. Suddenly, you know what to do. The plane looks better.'])

class g_banjo(Object):
    def __init__(self, name, look_at, act1, act2, act3, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3)
        self.act2 = act2
        self.act3 = act3
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == g_banjo.act1:
            g_banjo.itemmove(g_banjo.count, g_banjo.b1, g_banjo, g_banjo.act1)
        if act == g_banjo.act3:
            g_banjo.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if ebdman.count == 0:
            ebdman.count += 1
        ebdman.count += 1
        ebdman.act1 = ebdman.act2
        inv.remove(g_banjo)
        render()
g_banjo = g_banjo('The Golden Banjo', 'A gorgeous, glittering banjo fresh off the workbench.', 'A holy chior sings as you take this beautiful instrument into yoru hands.', 'You pluck a few strings and wonder if you\'ve been a banjo player all along.', usemsg, 'Don\'t drop it again...', 'Don\'t just set this down on the floor!', (65, 535), 'Take', (225, 535), 'Play', (390, 535), 'Use', 0, [ebdman], ['EBDM: "That\'s the one!! fuddle sticks yeah it\'s God-like! Here\'s the lab key... make sure the bum doesn\'t get in.'])

#Cyrus:
cyrustxt1 = ['Cyrus: Sit down, Mr. Tennison. Have some wine.', 'Now, tell me, is madness a shield, or a poison? I think it is a poison,', 'but not for the reason you would think.', 'Cyrus hits his cigar and lets some ashes fall into the tray.', 'Cyrus: Everyone makes their own realities and likes to pretend everyone else agrees.', 'They point out similarities between your their reality, and ostracize anything else.', 'That, Mr. Tennison, is the poison. It doesn\'t come from the madness,', 'it comes from being branded mad.']
cyrustxt2 = ['Cyrus: Welcome, Mr Tennison, to the final chapter.', 'It was I who caught you and saved you from certain death.', 'Now, quickly, let me see your phone.', 'You hand it over.', 'Cyrus: Good morning. How are you?', 'Yes, I\'d like to ask you a bunch of questions and I want them answered immediately.', 'There\'s a pause.', 'Cyrus: Who is ya daddy, and what does he do? Hahahaha! You idiot!', 'Do you know who I am? Mr. Mcfeely!', 'Well whatever your name is, you better get ready for the big surprise.', 'It\'s on the second floor.', 'Cyrus hands you back your phone and sits back down to his cigar.']
class cyrus(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if cyrus.count == 0:
            cyrus.count += 1
            read(cyrustxt1)
            cyrus.act1 = 'Thank you for your time, Mr. Tennison.'
        if Nathaniel.count == 7:
            read(cyrustxt2)
            Nathaniel.count += 1
            sad.count += 1
            master_b.ri.remove(sad)
            landing.ri.insert(landing.ri.index(nothing), sad)
        clear()
        obj_act(act)
cyrus = cyrus('Cyrus the Bear', 'Cyrus is one classy motherfuddle stickser.', 'You sit and learn.', '', (45, 535), 'Speak to', 0)

#East Backyard Items:
irvtxt1 = ['Irv: Hey!','He waves and jumps down.', 'So I guess you heard about the pedal plane. Tell you what,', 'if you can fix it and wait until after I restock the grocery store,', 'I\'ll take you to Pie Town!', 'If you can find some good scrap wood for the plane,', 'that\'d be a good start. I\'d do it, but...', 'I\'m really full right now. Hahahaha', 'Irv takes another hit and climbs further up the tree.']
irvtxt2 = ['Irv appears from a whirwind of wind and leaves.', 'Irv: You fixed the plane?? Yeeeeeeah! Come on!', 'Irv jumps down, shaking the ground upon his landing. You ask if he is too full to fly.', 'He says he flies better while stuffed with sandwitches. The two of you pedal with all of your might', 'You reach The Daily Pie Cafe in Pie Town, NM. Bryan Custer sits at a table.', 'You reminisce the time Bryan, Wes, and Lucas took on the Southwest in a single weekend.', 'Bryan gives you a picture the three of them took with Jesus in Hollywood.', 'You grab a piece of pie, sign the guestbook, and fly back. You miss Lucas more than ever.']
class irv(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
    def action(self, act):
        if b_pedal_p.count != 2:
            read(irvtxt1)
        if b_pedal_p.count ==2:
            read(irvtxt2)
            irv.act1 = irv.act2
            drop(jpic)
        clear()
        obj_act(act)
irv = irv('Irv the Bear', 'You can smell the sandwitches several feet away...', 'You call up a tree to Irv.', 'Irv: Man, I\'m such a great pilot!', (45, 535), 'Speak to') 

#Dunkin Lady
dladytxt1 = ['Dunkin Lady: Oh, hi! I remember you! How\'ve you been?', 'Well, I just realized that I lost the Mother\'s Day gift you boys gave me so many years ago.', 'Do you have a copy of the picture you put inside of it, at least?', 'It really bugs me that I can\'t find it...', 'I\'ll give you the code to the self checkout so you can use the smith\'s if you do!']
dladytxt2 = ['Dunkin Lady: Ohhhh that\'s it! This picture always makes me smile.', 'Thank you! Now, simply respond to the self checkout with "good deal".', 'Thanks again!']
class dlady(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if dlady.count == 0:
            read(dladytxt1)
            dlady.count += 1
        clear()
        obj_act(act)
dlady = dlady('Dunkin Lady', 'Dunkin Lady hasn\'t changed a bit.', 'Dunkin Lady: Good luck!', (54, 535), 'Speak to', 0)

class jpic(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, b3center, b3, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == jpic.act1:
            jpic.itemmove(jpic.count, jpic.b1, jpic, jpic.act1)
        if act == jpic.act2:
            jpic.use = True
        clear()
        obj_act(act)
    def useaction(self):
        scheckout.count += 1
        dlady.act1 = 'Dunkin Lady: Thank you so much for the picture! I put it on my nightstand!'
        inv.remove(jpic)
        scheckout.act1 = scheckout.act2
        render()
        read(dladytxt2)
jpic = jpic('Mother\'s Day Pic', 'The perfect gift for any mother!', 'Taking it makes you a better person', usemsg, 'It hasn\'t forgiven you for dropping it.', 'Really?', (65, 535), 'Take', (230, 535), 'Use', (385, 535), '', 0, [dlady], ['You pull out the picture and Dunkin Lady\'s eyes tear up.'])

#Cleavland House Items:
Cleavlandtxt1 = ['Cleavland: Man, fuddle sticks. shoot. fuddle sticks!! Oh hey, you. You\'re young,', 'do you know how these things work?', 'Cleavland shows you his smart phone.', 'Cleavland: I need someone to delete these stupid fuddle sticksing games off this', 'fuddle sticksing phone,', 'I never even play them. Do you know how to do that?', 'Ernie walks in and waves at you before having a seat and picking up a pipe.']
Cleavlandtxt2 = ['Cleavland: Aw sweet, thanks man!! Here,', 'have this as a token of my gratitude.', 'Cleavland gives you a bag full of sandwitchfixings.', 'Cleavland: That\'s my good shoot! Now sit down, have a juice.', 'Cleavland only has moldy fruit and old capri suns. You loose an hour of your life.']
Cleavlandtxt3 = ['Cleavland: I thought you might know how to help me. Ah well, want a juice, man? Sit down.', 'Cleavland only has moldy fruit and old capri suns', 'You sit down and lose an hour of your life']
Cleavlandtxt4 = ['Cleavland: Hey, man! Thanks again for your help with my phone,', 'that shoot was pissing me off. Want a juice? Sit down.', 'He still only has old capri suns and moldy fruit. You loose an hour of your life.']
class Cleavland(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if Cleavland.count == 0:
            north_chapel.ri.remove(Ernie)
            rname.ri.insert(rname.ri.index(nothing), Ernie)
            Ernie.look_at = 'Ernie!! has red eyes. A old capri sun sits on the table in front of him.'
            Ernie.act1 = 'Ernie: Cleavland is actually quite the individual.'
            Cleavland.b1 = 'Yes'
            Cleavland.b1center = (70, 535)
            Cleavland.act1 = 'You agree.'
            Cleavland.b2 = 'No'
            Cleavland.b2center = (235, 535)
            Cleavland.act2 = 'You dare!'
            Cleavland.count += 1
            render()
            Cleavland.click(Cleavland.b1center, Cleavland.b1, Cleavland.b2center, Cleavland.b2)
            read(Cleavlandtxt1)
        if Cleavland.count == 2:
            read(Cleavlandtxt4)
            clear()
            obj_act(act)
        if Cleavland.count == 1 and act == Cleavland.act1:
            drop(sandwitchfixings)
            screen.fill((white), play_screen)
            pygame.display.update()
            read(Cleavlandtxt2)
            Cleavland.count += 1
            Cleavland.look_at = 'Cleavland is a pretty scary dude, and for and old guy he\'s in good shape.'
            Cleavland.act1 = 'Oh god... you talk to Cleavland.'
            Cleavland.b1 = 'Speak to'
            Cleavland.b1center = (45, 535)
            Cleavland.b2 = ''
            Cleavland.b2center = (0, 0)
        if Cleavland.count == 1 and act == Cleavland.act2:
            screen.fill((white), play_screen)
            pygame.display.update()
            read(Cleavlandtxt3)
            Cleavland.look_at = 'Cleavland: So you wanna help me out?'
Cleavland = Cleavland('Cleavland', 'Cleavland is a pretty scary dude, and for and old guy he\'s in good shape.', 'Oh god... you talk to Cleavland.', '', (45, 535), 'Speak to', 0)

#Smiths Items:
checktxt1 = ['Lucas glares at you from behind the screen.', '', 'Screen Lucas: What\'s the password?']
checktxt2 = ['Screen Lucas asks for the password.', 'You clearly say "good deal"', 'Screen Lucas: Yes. It\'s all good deals because it\'s my Smith\'s!', 'Come in.', '', 'The metal doors slide up.']
class scheckout(Object):
    def __init__(self, name, look_at, act1, act2, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.act2 = act2
        self.count = count
    def action(self, act):
        if scheckout.count == 0:
            read(checktxt1)
        if scheckout.count == 1:
            scheckout.count += 1
            read(checktxt2)
        clear()
        obj_act(act)
scheckout = scheckout('Self Checkout', 'An image of Lucas awaits on the screen...', 'You try a few things. Screen Lucas simply remarks \'Nope.', 'Screen Lucas: Welcome to my Smith\'s, Josh. You\'re gonna enjoy it.', (50, 535), 'Interact', 0)

#Tommy's Room Items:
class t(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
tommy = t('Tommy', 'Let\'s just go all in. His shirt says "How about a toast?" under a Dr Pepper logo.', 'Tommy: I\'m the guy Lucas used to make Dr. Pepper toasts to back in high school. You sure hang on to your inside jokes!', (65, 535), 'Talk')

class esodac(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if esodac.count == 0:
            drop(edp)
            esodac.count += 1
            esodac.act1 = 'Enough empty soda cans for you'
        clear()
        obj_act(act)
esodac = esodac('Empty Soda Cans', 'Empty cans of Dr. Pepper are strewn about the room.', 'Take one if you want, I guess.', (50, 535), 'Examine', 0)

class edp(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == edp.act1:
            edp.itemmove(edp.count, edp.b1, edp, edp.act1)
        if act == edp.act2:
            edp.use = True
        clear()
        obj_act(act)
    def useaction(self):
        inv.remove(edp)
        drop(adust)
        render()
edp = edp('Empty Doctor Pepper', 'An empty can of DP.', 'Who knows, right? Who knows what is a red herring and what isn\'t?!', usemsg, 'Totally useful!', 'At least recycle it...', (65, 535), 'Take', (225, 535), 'Use', 0, [hdgrind], ['You grind the soda can into a fine dust.'])

#Items in Dunkin:
dmantxt = ['Dunkin Man brightens up upon seeing a familiar face.', 'Dunkin Man: Hey, man! It\'s been a while!', 'After Lucas got this mansion he let us all crash here.', 'Then he started paying us just to make his second floor like the old Dunkin on Central,', 'The one across from campus. Anyway, you should probably have this map.']
class dman(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if dman.count == 0:
            read(dmantxt)
            dman.count += 1
            drop(fmap2)
            dman.act1 = 'Dunkin Man: Hey man, apple fritter for you?'
            render()
        clear()
        obj_act(act)
dman = dman('Dunkin Man', 'Dunkin Man stands behind the counter ready to kick some sas.', 'You dare approach Dunkin Man...', (45, 535), 'Speak to', 0)

class fmap2(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == fmap2.act1:
            fmap2.itemmove(fmap2.count, fmap2.b1, fmap2, fmap2.act1)
        if act == fmap2.act2:
            img = pygame.image.load(r'Map of Second Floor-page000123.jpg')
            screen.blit(img, (58, 105))
        clear()
        obj_act(act)
fmap2 = fmap2('Map of Second Floor', 'A map! But of the second floor!', 'Hell yeah! Map!!!!!!!', 'You look', 'Map it up.', 'You meorized it already?', (65, 535), 'Take', (225, 535), 'Look', 0)

class bum(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
bum = bum('Bum', 'This guy is wrapped in a dirty blanket. Wait... is that the yelling bum from college?', 'Bum: SHUT UP! GRAAHHHH!!!', (45, 535), 'Speak to')

#Robot Rec. Room Stuff:
Matthewtxt1 = ['"Beginning download of mansion." says the computer before Matthew.', 'Matthew: Ohhh heya Josh. heh heh heh', 'Berry yells from across the room.', 'Berry: Matthew! I knew it! You wanted to get Lucas out of the picture long enough to download', 'his mansion!! Matthew: WHAT?! No, no.', 'Berry: It\'s true! I\'ve been searching this mansion and it\'s the only thing that makes sense!', 'Matthew: What about you? You\'re jealous that Lucas is richer than you now!', 'You point out that only one part of the mansion remains unexplored, and perhaps', 'all fighting should wait until you all find a way to open that door to the north.', 'Matthew and Berry calm down and agree.', '...', '"Download complete" says the computer.']
class Matthew(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if Matthew.count == 0:
            Matthew.count += 1
            read(Matthewtxt1)
        clear()
        obj_act(act)
Matthew = Matthew('Matthew', 'Matthew! Such a good guy.', 'Matthew: Well, my work here is done.', (45, 535), 'Speak to', 0)

class als(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == als.act1:
            als.itemmove(als.count, als.b1, als, als.act1)
        if act == als.act2:
            als.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if rname == north_chapel and bottle_organ.name == 'Grand Bottle Organ':
            inv.remove(als)
            render()
            bottle_organ.count += 1
        else:
            pass
als = als('Auld Lang Syne','Sheet music to the classic song.', 'Maybe you should find something to play it on', usemsg, 'Let old senation be forgot...', 'And never brought to miinddd!', (65, 535), 'Take', (225, 535), 'Use', 0, [ctbanj, hanjo, g_banjo, bottle_organ], ['You pluck out a shootty rendition. Nothing happens.', 'You still don\'t know how to give a hanjo...', 'The song sounds horrendus on even this banjo... nothing happens.', 'The song won\'t work with so few keys...'])

class robot2(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
robot2 = robot2('Robot 2', 'This guys is bowing, rising, and bowing before a picture of Lucas in a monk\'s robe', '"Lucas is God. God is Lucas." The robot\'s red eyes flicker with every syllable...', (55, 535), 'Say hi')

#Smith's Items:
dptxt = ['You crack your DP and raise it. "TO TOMMY!", you say.', 'Tommy rises, a grin spreading accross his face.', 'He grasps an open can of Dr. Pepper beside him.']
class dp(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == dp.act1:
            dp.itemmove(dp.count, dp.b1, dp, dp.act1)
        if act == dp.act2:
            dp.use = True
        clear()
        obj_act(act)
    def useaction(self):
        read(dptxt)
dp = dp('Dr. Pepper', 'Cool and crisp with 23 flavors!', 'Never know when you might want the refreshing taste of Dr. Pepper.', usemsg, 'That\'s the pepper!', 'You a coke guy or something?', (65, 535), 'Take', (225, 535), 'Use', 0, [tommy], ['"To Tommy", he says, hitting his can against yours. You drink as brothers in Lucas.'])

class nwaf(Object):
    def __init__(self, name, look_at, act1, takemsg, drpmsg, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == nwaf.act1:
            nwaf.itemmove(nwaf.count, nwaf.b1, nwaf, nwaf.act1)
        clear()
        obj_act(act)
nwaf = nwaf('Nilla Wafers', 'Nice. Nilla Wafers!', 'Never hurts to have a snack!', 'Mmmmm...', 'Enough eating. Go find Lucas!', (65, 535), 'Take', 0)

class toc(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
toc = toc('Tons of Candy', 'Most of this aisle is just... sugar candy!', 'Better take advantage of this good deal!', (70, 535), 'Eat')

class pnut(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
pnut = pnut('Peanuts', 'Honey Mustard and Wasabi are both available flavors!', 'As a vegitarian, you gotta keep dat protien up.', (70, 535), 'Eat')

class sseeds(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
sseeds = sseeds('Sunflower Seeds', 'Some normal sunflower seeds. Classic road trip snack!', 'You aren\'t on a road trip...', (70, 535), 'Eat')

class md_sbottle(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == md_sbottle.act1:
            md_sbottle.itemmove(md_sbottle.count, md_sbottle.b1, md_sbottle, md_sbottle.act1)
        if act == md_sbottle.act2:
            md_sbottle.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if robot.count == 0:
            robot.count += 1
        robot.count += 1
        inv.remove(md_sbottle)
        drop(md_bottle)
        render()
        if robot.count == 3:
            drop(lrsg)
            read(robotxt4)
md_sbottle = md_sbottle('Medium Sauce Bottle', 'A Medium-sized bottle of Lucas\' favorite sauce for making Larsghetti.', 'Hey... this might work on the organ too!', usemsg, 'Saucy!', 'Sure, leave a random sauce bottle lying around! As if this place wasn\'t messy enough!', (65, 535), 'Take', (225, 535), 'Use', 0, [robot], ['The robot\'s back straightens and its eyes light up red. It thanks you, empties the sauce bottle, and returns to standby.'])
                        
class md_bottle(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == md_bottle.act1:
            md_bottle.itemmove(md_bottle.count, md_bottle.b1, md_bottle, md_bottle.act1)
        if act == md_bottle.act2:
            md_bottle.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if bottle_organ.name == 'Another Broke Bottle Organ':
            inv.remove(md_bottle)
            bottle_organ.name = 'Grand Bottle Organ'
            bottle_organ.look_at = 'The Grand Bottle Organ in its final form. Mozart died to play on it just once.'
            bottle_organ.act1 = 'The enitre mansion resonates and you can hear bears wailing along outside as you preform a slow, sad version of 409.'
            als.itemreacts[3] = 'Bear and robot alike wail in tune with the glorius old song. You hear a loud noise in the Northwest corner of the mansion.'
            render()
        else:
            pass
md_bottle = md_bottle('Medium Glass Bottle', 'This will definately work on the organ!', 'You wash the bottle, dry it, and put it wherever the hell you\'ve been keeping all this shoot.', usemsg, 'Woohoo a bottle!', 'Bye bye bottle. You are now part of the atmosphere.', (65, 535), 'Take', (225, 535), 'Use', 0, [bottle_organ], ['Best save this one for last...'])

class spg(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == spg.act1:
            spg.itemmove(spg.count, spg.b1, spg, spg.act1)
        if act == spg.act2:
            spg.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if robot.count == 0:
            robot.count += 1
        robot.count += 1
        inv.remove(spg)
        render()
        if robot.count == 3:
            drop(lrsg)
            read(robotxt4)
spg = spg('Spaghetti', 'A few strands of hard, long, uncooked noodles.', 'Gonna go cook it?', usemsg, 'Hopefully they weren\'t on the floor...', 'Will, I guess here is as good a place as any...', (65, 535), 'Take', (225, 535), 'Use', 0, [robot], ['The robot\'s back straightens and its eyes light up red. It thanks you and returns to standby.'])

class ban(Object):
    def __init__(self, name, look_at, act1, takemsg, drpmsg, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
    def action(self, act):
        if act == ban.act1:
            ban.itemmove(ban.count, ban.b1, ban, ban.act1)
        clear()
        obj_act(act)
ban = ban('Bananas', 'Bananas are among the healthiest of fruits!', '+5 to HP', '+3 to HP...', '-5 to HP', (65, 535), 'Take', 0)

#Lucas Room Items:
class dbdy(Object):
    def __init__(self, name, look_at, act1, b1center, b1):
        super().__init__(name, look_at, act1, b1center, b1)
    def action(self, act):
        rname.ri.remove(dbdy)
        drop(Lucas)
        render()
        clear()
        obj_act(act)
dbdy = dbdy('Dead Body', 'Oh god... is it Lucas?? ...', 'The dead body convulses. It\'s Lucas! He\'s alive! "HEEEEEYYYY!!!"', (65, 535), 'Poke')

larstxt1 = ['Lucas: Oh, hey Josh. Sorry about that,', 'I haven\'t been eating all weekend, so I passed out.', 'Wait... I NEED WATER, I NEED WATER!!', 'You fetch Lucas some water.', 'Lucas: Okay, thanks. What\'s up?']
class Lucas(Object):
    def __init__(self, name, look_at, act1, act2, act3, act4, b1center, b1, b2center, b2, b3center, b3, b4center, b4, count, a1, a1center, a2, a2center, a3, a3center, a4, a4center):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2, b3center, b3, b4center, b4)
        self.act2 = act2
        self.act3 = act3
        self.act4 = act4
        self.count = count
        self.a1 = a1
        self.a1center = a1center
        self.a2 = a2
        self.a2center = a2center
        self.a3 = a3
        self.a3center = a3center
        self.a4 = a4
        self.a4center = a4center
    def action(self, act):
        clear()
        obj_act(act)
        if Lucas.act1 != 'Lucas cowers before the one thing in the world that can stop him.':
            if act == 'You give Lucas a firm handshake':
                Lucas.count += 1
                read(larstxt1)
                Lucas.act1 = 'Lucas: Heeeeeyyyy!'
            if Lucas.act2 != '':
                Lucas.act1 = 'Lucas: Heeeeeyyyy!'
                Lucas.act2 = ''
                Lucas.act3 = ''
                Lucas.act4 = ''
                Lucas.b2 = 'Ask About'
                Lucas.b2center = (200, 535)
                Lucas.b3 = ''
                Lucas.b3center = (0, 0)
                Lucas.b4 = ''
                Lucas.b4center = (0, 0)
            if act == '':
                Lucas.act1 = 'Lucas: Uh... in here. Sleeping.'
                Lucas.act2 = 'Lucas: Oh, yeah I have the key. I kinda wanna eat first, though, but I\'m all out of sandwitchfixings...'
                Lucas.act3 = 'Lucas: You know. Make em\', watch em, be their god.'
                Lucas.act4 = 'Ernie\'s a good guy'
                Lucas.b2 = Lucas.a2
                Lucas.b2center = Lucas.a2center
                Lucas.b3 = Lucas.a3
                Lucas.b3center = Lucas.a3center
                Lucas.b4 = Lucas.a4
                Lucas.b4center = Lucas.a4center
                Lucas.click(Lucas.a1center, Lucas.a1, Lucas.a2center, Lucas.a2, Lucas.a3center, Lucas.a3, Lucas.a4center, Lucas.a4) 
Lucas = Lucas('Lucas', 'LLUUUUUUCCCCCAAAAAAASSSS!!!', 'You give Lucas a firm handshake', '', '', '', (45, 535), 'Speak to', (200, 535), 'Ask About', (0, 0), '', (0, 0), '', 0, 'Where He\'s Been', (10, 535), 'Locked Door', (190, 535), 'The Robots', (355, 535), 'Ernie!', (550, 535))

class brknb(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == brknb.act1:
            brknb.itemmove(brknb.count, brknb.b1, brknb, brknb.act1)
        if act == brknb.act2 and brknb.name == 'Sandwitch':
            brknb.use = True
        clear()
        obj_act(act)
    def useaction(self):
        if Lucas.count == 0:
            Lucas.count += 1
        Lucas.count += 1
        rname.ri.remove(Lucas)
        if Nathaniel.count != 6:
            master_b.ri.insert(master_b.ri.index(nothing), Lucas)
            Lucas.act1 = 'Lucas cowers before the one thing in the world that can stop him.'
            Lucas.b2 = ''
            master_b.ri.insert(master_b.ri.index(nothing), lmom)
        render()
brknb = brknb('Plain bread', 'Just some bread!', 'Yum', 'No, man. Is for Lucas.', 'Love sandwitches!', 'Goodbye bread... :(', (65, 535), 'Take', (225, 535), 'Use', 0, [], ['Lucas: Good deal!'])

class sandwitchfixings(Object):
    def __init__(self, name, look_at, act1, act2, takemsg, drpmsg, b1center, b1, b2center, b2, count, useitem, itemreacts):
        super().__init__(name, look_at, act1, b1center, b1, b2center, b2)
        self.act2 = act2
        self.takemsg = takemsg
        self.drpmsg = drpmsg
        self.count = count
        self.useitem = useitem
        self.itemreacts = itemreacts
    def action(self, act):
        if act == sandwitchfixings.act1:
            sandwitchfixings.itemmove(sandwitchfixings.count, sandwitchfixings.b1, sandwitchfixings, sandwitchfixings.act1)
        if act == sandwitchfixings.act2:
            sandwitchfixings.use = True
        clear()
        obj_act(act)
    def useaction(self):
        inv.remove(sandwitchfixings)
        brknb.name = 'Sandwitch'
        brknb.useitem = [Lucas]
        brknb.act2 = usemsg
        render()
sandwitchfixings = sandwitchfixings('sandwitchfixings', 'Fresh!', 'Good quality!', usemsg, 'Good quality', 'You\'re a vegitarian anyway', (65, 535), 'Take', (230, 535), 'Use', 0, [brknb], ['You load the bread. Tight.'])

#Special Characters
sadtxt1 = ['SAD looks like a mole coming out of a dark hole, he snaps upright upon seeing you.', 'SAD: I thought I killed you once and for all! That call was you, wasn\'t it?!', '"SAD," you say. "This isn\'t your mansion. There are talking bears outside. Banjos too.', 'Admit that you just made a deal with Lucas\' parents to troll us."', 'SAD twitches and lunges. You step into Dunkin Doughnuts and SAD falls in after you...', '"And here\'s one last thing you\'d never put in your mansion." you say, smirking.', '"A Dunkin Doughnuts."', 'SAD stands up, his skin emitting luminescence. His face turns to sheer horror.', '"I thought about what I might do if you ever came after me, SAD." You begin,', '"How can you kill someone who attracts all attacks towards himself, but cannot die?', 'Then I remembered how you never wanted to walk to Dunkin with us. It all makes sense."', 'SAD: AUUUUUUUUUUGGGGGGGGGGHH', 'HHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!']
sadtxt2 = ['SAD turns into pure light for a moment and catches flame.', 'All that\'s left when it\'s said and done is a pile of ash on the floor.', '"How..." you say, putting on sunglasses.', '', '"sad."']
class sad(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if sad.count == 3:
            clear()
            obj_act(act)
        if sad.count == 2:
            screen.fill((white), play_screen)
            read(sadtxt2)
            sad.count += 1
            sad.act1 = 'You win. Bye Bye!'
        if sad.count == 0:
            clear()
            obj_act(act)
        if sad.count == 1:
            sad.count += 1
            sad.b1 = 'Continue'
            sad.click(sad.b1center, sad.b1)
            read(sadtxt1)
sad = sad('SAD', 'Sebastian Anthoney Daniels... he has a beard now.', 'SAD: AUUUGGGHHH... why are you cliking on me? Trying to convince me to ditch college algebra with you?!', (45, 535), 'Speak to', 0)

lmomtxt1 = ['Lucas\' Mom turns around in her chair.', 'Lucas\' Mom: Hello, Lucas, Josh. We have much to discus. First of all,', 'Lucas I am horrified to find that you are living in filth!', 'Lucas looks away from his mother\'s gaze.', 'Lucas\' Mom: Even worse, I\'ve noticed that you have TOWELS!', 'That means you\'ve been PLANNING THINGS all along! This is unexceptable!', 'I bet you\'ve even been to PIE TOWN! Leave us, Josh. Lucas and I must talk.']
lmomtxt2 = ['Lucas\' Mom turns around in her chair.', 'Lucas\' Mom: Hello, Lucas, Josh. We have much to discus. First of all, Lucas', 'I am horrified to find that you are living in filth!', 'Lucas looks away from his mother\'s gaze.', 'Lucas\' Mom: Even worse, I\'ve noticed that you have TOWELS!', 'That means you\'ve been PLANNING THINGS all along! This is unacceptable!', 'I bet you\'ve even been to PIE TOWN! Leave us, Josh. Lucas and I must talk.', 'NO! A voice comes from the other end of the bedroom. It\'s Nathaniel!']
lmomtxt3 = ['Nathaniel: I used to think Josh was a bad guy, but no one who eats at Cici\'s three times in one', 'day can be all that bad, so I can\'t let this go on any longer!', 'Nathaniel looks at you.', 'Nathaniel: Josh, you\'re supposed to use Lucas\' Dad\'s number to call him on your phone.', 'He\'ll show up on the pedal plane and reveal some bullshoot about how we\'re all robots', 'except for Lucas, Lucas\' Mom, and himself. He\'ll say this world has been', 'one big experiment to the test limits of AI by presenting it with their son,', 'but don\'t believe it! Behold!']
lmomtxt4 = ['Nathaniel takes off Lucas\' Mom\'s face. Gears and wires lie under.', 'Nathaniel: You may think we\'re all robots but Lucas, but that is also false!!', 'Nathaniel pulls off the robot under-workings to reveal... the face of Lucas.', 'He then does the same with his own face.', 'Nathaniel-Lucas: Can\'t you see, Josh? We\'re all him. We\'re all inside his head.', 'That\'s why he sees us. That\'s why...', 'I see ya.']
class lmom(Object):
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        global rname
        if lmom.b1 == 'Behold':
            screen.fill((white), play_screen)
            read(lmomtxt4)
            clear()
            obj_act(act)
        if lmom.b1 == 'Continue':
            lmom.b1 = 'Behold'
            lmom.b1center = (55, 535)
            lmom.click(lmom.b1center, lmom.b1)
            lmom.act1 = 'You win. Or I do. Or neither of us. God, glad I\'m done coding this for now. 10/9/2020'
            read(lmomtxt3)
        if Nathaniel in rname.ri and lmom.b1 == 'Approach':
            Lucas.count = 0
            lmom.act1 = ''
            lmom.b1 = 'Continue'
            lmom.click(lmom.b1center, lmom.b1)
            read(lmomtxt2)
        if ldad.count == 1:
            Lucas.count = 0
            clear()
            obj_act(act)
        if Lucas.count == 1:
            rname = rrec_room
            render()
            clear()
            obj_act(act)
        if Lucas.count == 2:
            Berry.act1 = 'Berry: We have to stop Lucas\' Mom! Wait, why don\'t you call his dad? He might be able to help!'
            Berry.bact1 = 'Berry: We have to stop Lucas\' Mom! Wait, why don\'t you call his dad? He might be able to help!'
            Lucas.count -= 1
            read(lmomtxt1)
            lmom.count += 1
            lmom.act1 = 'She pushes you out with a glance'
            clear()
            obj_act(act)
lmom = lmom('Lucas\' Mom', 'It\'s Lucas\' Mom! You pray she be trollin\'.', 'You approach...', (45, 535), 'Approach', 0)

ldadtxt1 = ['Lucas\' Dad: Oh, hello Josh.', 'I\'m a little late because I\'d finally gotten the chance to play tennis with my friends after', 'a long week of hard work.', 'You explain the situation.', 'Lucas\' Dad: I see... Well, Josh. Perhaps it\'s time to reveal a few things to Lucas.', 'Come with me.']
ldadtxt2 = ['Lucas\' Dad: Alright, that\'s enough.', 'Lucas\' Mom looks up, confused.', 'Lucas\' Dad: Of course Lucas plans. We always knew that. We made him think that bringing', 'towels was something he would want to hide from us as a joke!', 'Lucas stops cowering and looks up.', 'Lucas\' Mom: Erik, it\'s not time. There is still a lot more we could do...', 'Lucas\' Dad: No, it\'s time Lucas knew. He\'s a full grown man with a mansion.', 'And look at this mansion! He\'d probably hire a fuddle sticksing maid if we hadn\'t gone', 'too far with our pranks.', 'Lucas\' Dad looks at Lucas.', 'Lucas\' Dad: Lucas... your life has been a lie. Our planet was destroyed long ago.']
ldadtxt3 = ['We found this fertile, uninhabited world and filled it with robots to play with our son.', 'Then we saw how easy it was to fuddle sticks with all of you and,', 'well. We wanted to test their programming by raising you.',  'And son, you\'ve made us proud. You\'ve made robots of your own!', 'But let me help.', 'Lucas\' Dad takes off your face.', 'Lucas\' Dad: See this circuitry here? I can show you how to get the AI good enough', 'to create a planet for you.', 'Somehow you wake up in the Chapel.', 'Microwave Dave is back and everyone is pretending to enjoy his show.', '...', 'The credits roll to Ey Bodidly.']
class ldad(Object):#Need to show continue button. also clear out the white space before ldadtxt3. Also ldadtxt3 goes off the screen
    def __init__(self, name, look_at, act1, b1center, b1, count):
        super().__init__(name, look_at, act1, b1center, b1)
        self.count = count
    def action(self, act):
        if ldad.b1 == 'Continue':
            screen.fill((white), play_screen)
            read(ldadtxt3)
            clear()
            obj_act(act)
        if ldad.count == 1:
            ldad.b1 = 'Continue'
            ldad.act1 = 'You win. Go outside!'
            ldad.count += 1
            ldad.click(ldad.b1center, ldad.b1)
            read(ldadtxt2)
        if ldad.count == 0:
            read(ldadtxt1)
            lmom.act1 = 'Lucas\' mom faces her husband with an expert poker face.'
            ldad.act1 = ''
            ldad.count += 1
            rname.ri.remove(ldad)
            master_b.ri.insert(master_b.ri.index(nothing), ldad)
            render()
            if Lucas.count != 2:
                Lucas.count =2
            clear()
            obj_act(act)
ldad = ldad('Lucas\' Dad', 'Erik Fabrecious-Olson!', 'Elated, you approach', (45, 535), 'Approach', 0)
#Function for Opening Sequence
def opening():
    print("""You are Josh. You've been living in Madison, Wisconsin for almost three years now. It's hard to believe so much time has passed. 

Our story begins on a beautiful Wisconsin day. You played Arkham last night, Epic just sent you a whole bunch of money, and a gentle breeze wafts hints of fall down your street. All is well.

You open your mailbox. Credit card offers, coupons, bill reminders, and... wait, what's this? A letter from Denmark? You don't know anyone from Denmark. Who would contact you from there? Your eyes scan up to the name on the return address. It's a name you haven't heard in a long... long time. The name that changes everything. The name above names. Lucas.

The mail drops from your hands and flutters to the ground.
""")
    input('Press Enter')
    print("""Josh, 

I just inherited my uncle's mansion in Denmark. Well, I've been living here for about a year and a half, but Microwave Dave is coming over to give a show so I decided I'd invite some other people too. So come over.

P.S. Remember. The day will soon come when all will be revealed and Lucas will be laid bare before you.

P.P.S. I paid for your plane ticket because I'm rich now.

-Lucas
""")
    input('Your ticket is behind the letter. Your flight leaves today. Press Enter.')

#Room Class, Subclasses, and render functions
    
class Room():
    def __init__(self, name, compas, ri):
        self.name = name
        self.compas = compas
        self.ri = ri

def l_bdrmcomp():
    comp = [no_go, ghallnorth, no_go, no_go]
    return comp

def foyercomp():
    compas = [west_jroom, locked[3], ccpoolr, art_gall]
    return compas

def wjroomcomp():
    compas = [wkitch, foyer, no_go, east_jroom]
    return compas

def ejroomcomp():
    compas = [ekitch, art_gall, west_jroom, south_chapel]
    return compas

def ccpoolcomp():
    if bob.count != 2:
        compas = [locked[2], no_go, no_go, foyer]
    else:
        compas = [bjo_wshp, no_go, no_go, foyer]
    return compas

def art_gallcomp():
    compas = [south_chapel, no_go, foyer, Marty_room]
    return compas

def landcomp():
    if sad in landing.ri:
        comp = [locked[16], locked[16], locked[16], locked[16]]
    else:
        comp = [edunkin_d, foyer, ebdmanr, troom]
    return comp

def wkitchcomp():
    compas = [no_go, west_jroom, ghallsouth, ekitch]
    return compas

def ekitchcomp():
    compas = [no_go, east_jroom, wkitch, lhs]
    return compas

def mroomcomp():
    compas = [no_go, no_go, art_gall, no_go]
    return compas

def ghallnorthcomp():
    if bottle_organ.count == 1:
        compas = [l_bdrm, ghallsouth, gbed02, no_go]
    else:
        compas = [locked[5], ghallsouth, gbed02, no_go]
    return compas

def ghallsouthcomp():
    if bob.count != 2:
        compas = [ghallnorth, locked[4], gbed01, wkitch]
    else:
        compas = [ghallnorth, bjo_wshp, gbed01, wkitch]
    return compas

def lhncomp():
    if picframe.count == 0 or 1:
        comp = [locked[1], lhs, no_go, no_go]
    if picframe.count == 2:
        comp = [ebyard_porch, lhs, no_go, no_go]
    return comp

def lhscomp():
    comp = [lhn, east_jroom, ekitch, north_chapel]
    return comp

def gbed01comp():
    comp = [no_go, no_go, gbath01, ghallsouth]
    return comp

def gbath01comp():
    comp = [no_go, no_go, no_go, gbed01]
    return comp

def gbed02comp():
    if Nathaniel.count == 0:
        comp = [no_go, no_go, locked[6], ghallnorth]
    elif Nathaniel.count == 1:
        comp = [no_go, no_go, gbath02, ghallnorth]
    return comp

def gbath02comp():
    comp = [no_go, no_go, no_go, gbed02]
    return comp

def bjo_wshpcomp():
    comp = [ghallsouth, ccpoolr, no_go, no_go]
    return comp

def wbyard_porchcomp():
    if Nathaniel.count == 7:
        comp = [locked[15], locked[15], locked[15], locked[15]]
    else:
        comp = [wbyard, no_go, no_go, ebyard_porch]
    return comp

def ebyard_porchcomp():
    if bob.name != 'Bob the Bear':
        comp = [locked[7], lhn, locked[7], locked[7]]
    else:
        comp = [ebyard, lhn, wbyard_porch, no_go]
    return comp

def wbyardcomp():
    comp = [no_go, wbyard_porch, no_go, ebyard]
    return comp

def ebyardcomp():
    comp = [no_go, ebyard_porch, wbyard, chouse ]
    return comp

def chousecomp():
    comp = [no_go, no_go, ebyard, no_go]
    return comp

def smithsecomp():
    if scheckout.count == 2:
        comp = [a2, landing, no_go, no_go]
    else:
        comp = [locked[8], landing, no_go, no_go]
    return comp

def a1comp():
    comp = [no_go, no_go, no_go, a2]
    return comp

def a2comp():
    comp = [no_go, smithse, a1, a3]
    return comp

def a3comp():
    comp = [no_go, no_go, a2, no_go]
    return comp

def wdunkin_dcomp():
    if ebdman.count == 2:
        comp = [lab, no_go, dmanr, edunkin_d]
    else:
        comp = [locked[10], no_go, dmanr, edunkin_d]
    return comp

def edunkin_dcomp():
    comp = [locked[9], landing, wdunkin_d, dladyr]
    return comp

def dladyrcomp():
    comp = [no_go, no_go, edunkin_d, no_go]
    return comp

def troomcomp():
    comp = [no_go, no_go, landing, no_go]
    return comp

def ebdmanrcomp():
    comp = [no_go, no_go, no_go, landing]
    return comp

def dmanrcomp():
    comp = [no_go, no_go, no_go, wdunkin_d]
    return comp

def labcomp():
    if swolf.count == 3:
        comp = [no_go, wdunkin_d, no_go, rrec_room]
    else:
        comp = [no_go, wdunkin_d, no_go, locked[11]]
    return comp

def master_bcomp():
    if ldad.count == 1:
        comp = [locked[17], locked[17], locked[17], locked[17]]
    else:
        comp = [no_go, rrec_room, no_go, no_go]
    return comp

def rrec_roomcomp():
    if Nathaniel.count == 6:
        comp = [locked[14], locked[14], locked[14], locked[14]]
    elif Lucas.count == 2:
        comp = [master_b, locked[13], lab, no_go]
    else:
        comp = [locked[12], locked[13], lab, no_go]
    return comp

def sccomp():
    comp = [north_chapel, art_gall, east_jroom, no_go]
    return comp

def nccomp():
    comp = [no_go, south_chapel, lhs, no_go]
    return comp


#Room variables
north_chapel = Room('North Chapel', nccomp, [bottle_organ, Ernie, Berry, nothing, nothing, nothing])
south_chapel = Room('South Chapel', sccomp, [pew, c_pew, nothing, nothing])
art_gall = Room('Art Gallery', art_gallcomp, [larsport, cardpile, bearpaint, nothing, nothing])
Marty_room = Room('Marty\'s Room', mroomcomp, [Marty, nothing, nothing, nothing])
lhn = Room('Long Hall (N)', lhncomp, [nothing, nothing, nothing, nothing])
lhs = Room('Long Hall (S)', lhscomp, [nothing, nothing, nothing, nothing])
east_jroom = Room('East Jam Room', ejroomcomp, [ctbanj, drums, nothing, nothing, nothing])
west_jroom = Room('West Jam Room', wjroomcomp, [hanjo, nothing, nothing, nothing, nothing])
foyer = Room('Foyer', foyercomp, [stairway, nothing, nothing, nothing, nothing])
ccpoolr = Room('Candy Cron Pool', ccpoolcomp, [ccpool, nothing, nothing, nothing, nothing])
ekitch = Room('East Kitchen', ekitchcomp, [robot, stove, nothing, nothing])
wkitch = Room('West Kitchen', wkitchcomp, [fridge, cabinet, drawer, nothing, nothing, nothing])
ghallnorth = Room('Guest Hall (N)', ghallnorthcomp, [nothing, nothing, nothing, nothing])
ghallsouth = Room('Guest Hall (S)', ghallsouthcomp, [nothing, nothing, nothing, nothing])
gbed01 = Room('Guest Bed 1', gbed01comp, [trash, cupboard, nothing, nothing])
gbath01 = Room('Guest Bath 1', gbath01comp, [rsink, rshavings, towel, nothing, nothing, nothing])
gbed02 = Room('Guest Bed 2', gbed02comp, [Nathaniel, nothing, nothing, nothing, nothing])
gbath02 = Room('Guest Bath 2', gbath02comp, [sink, toilet, nothing, nothing])
bjo_wshp = Room('Banjo Workshop', bjo_wshpcomp, [wood, g_banjo, nothing, nothing, nothing, nothing])
ebyard_porch = Room('Back Porch (E)', ebyard_porchcomp, [bob, nothing, nothing, nothing, nothing])
wbyard_porch = Room('Back Porch (W)', wbyard_porchcomp, [cyrus, nothing, nothing, nothing])
ebyard = Room('East Backyard', ebyardcomp, [irv, nothing, nothing, nothing, nothing])
wbyard = Room('West Backyard', wbyardcomp, [b_pedal_p, scrap, nothing, nothing])
chouse = Room('Cleavland\' House', chousecomp, [Cleavland, nothing, nothing, nothing])
landing = Room('Landing', landcomp, [stairway, gware, nothing, nothing, nothing, nothing])
troom = Room('Tommy\'s Room', troomcomp, [tommy, esodac, nothing, nothing, nothing])
ebdmanr = Room('E Beard Dman Rm', ebdmanrcomp, [ebdman, nothing, nothing, nothing])
edunkin_d = Room('Dunkin D\'s (E)', edunkin_dcomp, [dman, nothing, nothing, nothing])
wdunkin_d = Room('Dunkin D\'s (W)', wdunkin_dcomp, [bum, nothing, nothing, nothing])
dladyr = Room('Dunkin Lady Rm', dladyrcomp, [dlady, nothing, nothing, nothing])
dmanr = Room('Dunkin Man Rm', dmanrcomp, [nothing, nothing, nothing, nothing])
lab = Room('Laboratory', labcomp, [swolf, hdgrind, nothing, nothing])
rrec_room = Room('Robot Rec. Room', rrec_roomcomp, [Matthew, als, robot2, nothing, nothing])
master_b = Room('Master Bedroom', master_bcomp, [nothing, nothing, nothing, nothing])
smithse = Room('Smith\'s Entry', smithsecomp, [scheckout, nothing, nothing, nothing])
a1 = Room('Aisle One', a1comp, [dp, nwaf, toc, nothing, nothing, nothing])
a2 = Room('Aisle Two', a2comp, [pnut, sseeds, nothing, nothing])
a3 = Room('Aisle Three', a3comp, [md_sbottle, spg, ban, nothing, nothing, nothing, nothing])
l_bdrm = Room('Lucas\' Bedroom', l_bdrmcomp, [brknb, dbdy, nothing, nothing, nothing])

no_go = 'You can\'t go that way.'
locked = ['That way leads to a door. You try the handle, but it\'s locked', 'A large metal door with no knob blocks the way. A sign over the door says "To the Wild"', 'Too much candy cron in the way, but maybe Lucas got an iPhone with the money he saved!', 'You turn toward the large, gorgeous door. You can\'t leave until you find Lucas!', 'A plaque over this door reads "Banjos Under Construction" The door is locked.', '\"Let Old Acquaintance Be Forgot\" is engraved on the wall near the roof. You feel weird', 'Nathaniel loudly clears his throat', 'You\'d have to get past the bear... no thanks.', 'A large metal sheet blocks the way...', 'Dunkin Man would die before letting you behind that counter. He stares you down.', 'A door labeld "Laboratory" is locked. Perhaps because of that the bum over there.', 'There is a discolored place in the wall. A door was sealed over.', 'This solid, carved wooden door won\'t budge.', 'You would never dream of disturbing dunkin man behind his counter.', 'The robot blocks your path. You look to Nathaniel who smirks.', 'Cyrus waves you over', 'Destiny dictacts you confront the one they call SAD...', 'You must stay and hear the words of Lucas\' dad']
#up to locked[17]

#Game Loop

#opening()
click = cphone
item = fmap
rname = north_chapel
render()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            #Keys for typing commands into a place on screen:
            #if e.key == pygame.K_BACKSPACE:
                #user_text = user_text[:-1]
            #else:
                #user_text += e.unicode
            if e.key == pygame.K_UP:
                if rname.compas()[0] != no_go and rname.compas()[0] not in locked:
                    rname = rname.compas()[0]
                    render()
                else:
                    #proooobly need to make a writing text function...
                    clear()
                    screen_text = font.render(rname.compas()[0], True, white)
                    screen.blit(screen_text, (nar))
                    pygame.display.update()
            if e.key == pygame.K_DOWN:
                if rname.compas()[1] != no_go and rname.compas()[1] not in locked:
                    rname = rname.compas()[1]
                    render()
                else:
                    clear()
                    screen_text = font.render(rname.compas()[1], True, white)
                    screen.blit(screen_text, (nar))
                    pygame.display.update()
            if e.key == pygame.K_LEFT:
                if rname.compas()[2] != no_go and rname.compas()[2] not in locked:
                    rname = rname.compas()[2]
                    render()
                else:
                    clear()
                    screen_text = font.render(rname.compas()[2], True, white)
                    screen.blit(screen_text, (nar))
                    pygame.display.update()
            if e.key == pygame.K_RIGHT:
                if rname.compas()[3] != no_go and rname.compas()[3] not in locked:
                    rname = rname.compas()[3]
                    render()
                else:
                    clear()
                    screen_text = font.render(rname.compas()[3], True, white)
                    screen.blit(screen_text, (nar))
                    pygame.display.update()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            #Clicks for Room Items
            if mx >= 750 and my <= 80 and my > 50:
                clickwithuse(rname.ri[0], item, click, rname.ri[0].b1center, rname.ri[0].b1)
                click = rname.ri[0]
            if mx >= 750 and my <= 110 and my > 80:
                clickwithuse(rname.ri[1], item, click, rname.ri[1].b1center, rname.ri[1].b1)
                click = rname.ri[1]
            if mx >= 750 and my <= 140 and my > 110:
                clickwithuse(rname.ri[2], item, click, rname.ri[2].b1center, rname.ri[2].b1)
                click = rname.ri[2]
            if mx >= 750 and my <= 170 and my > 140:
                clickwithuse(rname.ri[3], item, click, rname.ri[3].b1center, rname.ri[3].b1)
                click = rname.ri[3]
                    
            #Clicks for Inventory Items
            if mx >= 750 and my <= 240 and my > 210:
                clickwithuse(inv[0], item, click, inv[0].b1center, inv[0].b1)
                click = inv[0].name
                item = inv[0]
            if mx >= 750 and my <= 270 and my > 240:
                clickwithuse(inv[1], item, click, inv[1].b1center, inv[1].b1)
                click = inv[1].name
                item = inv[1]
            if mx >= 750 and my <= 300 and my > 270:
                clickwithuse(inv[2], item, click, inv[2].b1center, inv[2].b1)
                click = inv[2].name
                item = inv[2]
            if mx >= 750 and my <= 330 and my > 300:
                clickwithuse(inv[3], item, click, inv[3].b1center, inv[3].b1)
                click = inv[3].name
                item = inv[3]
            if mx >= 750 and my <= 360 and my > 330:
                clickwithuse(inv[4], item, click, inv[4].b1center, inv[4].b1)
                click = inv[4].name
                item = inv[4]
            if mx >= 750 and my <= 390 and my > 360:
                clickwithuse(inv[5], item, click, inv[5].b1center, inv[5].b1)
                click = inv[5].name
                item = inv[5]
            if mx >= 750 and my <= 420 and my > 390:
                clickwithuse(inv[6], item, click, inv[6].b1center, inv[6].b1)
                click = inv[6].name
                item = inv[6]
            if mx >= 750 and my <= 450 and my > 420:
                clickwithuse(inv[7], item, click, inv[7].b1center, inv[7].b1)
                click = inv[7].name
                item = inv[7]
            if mx >= 750 and my <= 480 and my > 450:
                clickwithuse(inv[8], item, click, inv[8].b1center, inv[8].b1)
                click = inv[8].name
                item = inv[8]
            
            #Action 1 for all 4 Room Items:
            if click == rname.ri[0] and mx >= 10 and mx <=160 and my >= 500 and my <= 580:
                rname.ri[0].action(rname.ri[0].act1)
            if click == rname.ri[1] and mx >= 10 and mx <=160 and my >= 500 and my <= 580:
                rname.ri[1].action(rname.ri[1].act1)
            if click == rname.ri[2] and mx >= 10 and mx <=160 and my >= 500 and my <= 580:
                rname.ri[2].action(rname.ri[2].act1)
            if click == rname.ri[3] and mx >= 10 and mx <=160 and my >= 500 and my <= 580:
                rname.ri[3].action(rname.ri[3].act1)
            #Action 2 for all 4 Room Items:
            if click == rname.ri[0] and mx >= 170 and mx <= 320 and my >= 500 and my <= 580:
                rname.ri[0].action(rname.ri[0].act2)#perhaps a try and except with attributeerror causing a pass will stop the stupid sas glitch if you click the black space... or give all items a '' act 1-4.
            if click == rname.ri[1] and mx >= 170 and mx <= 320 and my >= 500 and my <= 580:
                rname.ri[1].action(rname.ri[1].act2)
            if click == rname.ri[2] and mx >= 170 and mx <= 320 and my >= 500 and my <= 580:
                rname.ri[2].action(rname.ri[2].act2)
            if click == rname.ri[3] and mx >= 170 and mx <= 320 and my >= 500 and my <= 580:
                rname.ri[3].action(rname.ri[3].act2)
            #Action 3 for all 4 Room Items:
            if click == rname.ri[0] and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                rname.ri[0].action(rname.ri[0].act3)
            if click == rname.ri[1] and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                rname.ri[1].action(rname.ri[1].act3)
            if click == rname.ri[2] and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                rname.ri[2].action(rname.ri[2].act3)
            if click == rname.ri[3] and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                rname.ri[3].action(rname.ri[3].act3)
            #Action 4 for all 4 Room Items:
            if click == rname.ri[0] and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                rname.ri[0].action(rname.ri[0].act4)
            if click == rname.ri[1] and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                rname.ri[1].action(rname.ri[1].act4)
            if click == rname.ri[2] and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                rname.ri[2].action(rname.ri[2].act4)
            if click == rname.ri[3] and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                rname.ri[3].action(rname.ri[3].act4)
            #Action 1 for all 9 Inv Items
            if click == inv[0].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[0].action(inv[0].act1)
            if click == inv[1].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[1].action(inv[1].act1)
            if click == inv[2].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[2].action(inv[2].act1)
            if click == inv[3].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[3].action(inv[3].act1)
            if click == inv[4].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[4].action(inv[4].act1)
            if click == inv[5].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[5].action(inv[5].act1)
            if click == inv[6].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[6].action(inv[6].act1)
            if click == inv[7].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[7].action(inv[7].act1)
            if click == inv[8].name and mx >= 10 and mx <= 160 and my >= 500 and my <= 580:
                inv[8].action(inv[8].act1)
            #Action 2 for all 9 Inv Items
            if click == inv[0].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[0].action(inv[0].act2)
            if click == inv[1].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[1].action(inv[1].act2)
            if click == inv[2].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[2].action(inv[2].act2)
            if click == inv[3].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[3].action(inv[3].act2)
            if click == inv[4].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[4].action(inv[4].act2)
            if click == inv[5].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[5].action(inv[5].act2)
            if click == inv[6].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[6].action(inv[6].act2)
            if click == inv[7].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[7].action(inv[7].act2)
            if click == inv[8].name and mx >= 170 and mx <=320 and my >= 500 and my <= 580:
                inv[8].action(inv[8].act2)
            #Action 3 for all 9 Inv Items
            if click == inv[0].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[0].action(inv[0].act3)
            if click == inv[1].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[1].action(inv[1].act3)
            if click == inv[2].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[2].action(inv[2].act3)
            if click == inv[3].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[3].action(inv[3].act3)
            if click == inv[4].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[4].action(inv[4].act3)
            if click == inv[5].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[5].action(inv[5].act3)
            if click == inv[6].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[6].action(inv[6].act3)
            if click == inv[7].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[7].action(inv[7].act3)
            if click == inv[8].name and mx >= 330 and mx <=480 and my >= 500 and my <= 580:
                inv[8].action(inv[8].act3)
            #Action 4 for all 9 Inv Items
            if click == inv[0].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[0].action(inv[0].act4)
            if click == inv[1].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[1].action(inv[1].act4)
            if click == inv[2].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[2].action(inv[2].act4)
            if click == inv[3].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[3].action(inv[3].act4)
            if click == inv[4].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[4].action(inv[4].act4)
            if click == inv[5].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[5].action(inv[5].act4)
            if click == inv[6].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[6].action(inv[6].act4)
            if click == inv[7].name and mx >= 490 and mx <=640 and my >= 500 and my <= 580:
                inv[7].action(inv[7].act4)
            if click == inv[8].name and mx >= 490 and mx <=2640 and my >= 500 and my <= 580:
                inv[8].action(inv[8].act4)
                
