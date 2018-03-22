import random

class Piece(object):
    def __init__(self, name='object'):
        self.name = name
        self.position_x, self.position_y = self.__init_position__()
        self.limit = 4
    
    def __init_position__(self):
        return random.randrange(0,5), random.randrange(0,5)
        
    def __str__(self):
        position = str(self.position_x)+ ',' + str(self.position_y)
        name = self.name
        string = position + ' ' + name
        return string
        
    def __repr__(self):
        return self.__str__()
        
    def move_piece(self, direction, n=1):
        if direction == 'up':
            self.position_y += n
        if direction == 'down':
            self.position_y -= n
        if direction == 'left':
            self.position_x -= n
        if direction == 'right':
            self.position_x += n
        if direction == 'y':
            self.position_y += n
        if direction == 'x':
            self.position_x += n
        
        
class Mouse(Piece):
    def __init__(self):
        self.name = 'Mouse'
        self.position_x, self.position_y = self.__init_position__()
        self.limit = 4
        
    def __movement_decision__(self,y ,x):
        if abs(x - self.position_x) > abs(y - self.position_y) and \
        x != self.position_x:
            if x - self.position_x > 0 and self.position_x < self.limit:
                return(True, 'right')
            else:
                if self.position_x > -1:
                    return(True, 'left')
        elif abs(y - self.position_y) > abs(x - self.position_x) and \
        y != self.position_y:
            if y - self.position_y >= 0 and self.position_y < self.limit:
                    return(True, 'up')
            else:
                if self.position_y > -1:
                    return(True, 'down')

        return(False, 'nowhere')
                
                
    def __movement__(self):
        correct_move = False
        while correct_move == False:
            y = (random.randrange(0,17)/2)-2
            x = (random.randrange(0,17)/2)-2
            correct_move, direction = self.__movement_decision__(y,x)
        self.move_piece(direction)
            
                
                     
        
        
        #for movement take a random number assign it to up and down choose the
        #bigger number, then compare it with the current position in that axis
        #if the number is less move down/left, if it is more move up/right
        #if they are equal use the other axis
        #if both axises are equal reroll
        #it can also nevr move into the cat
        
        
class Cat(Piece):
    
    def __init__(self):
        self.name = 'Cat'
        self.position_x, self.position_y = self.__init_position__()
        self.limit = 4
        
        
    def move(self, direction, n=1):
            if abs(n) > 2:
                raise RuntimeError("You can't move more than two spaces at once")
            elif direction == 'y':
                if self.position_y + n <= self.limit and self.position_y + n\
                > -1:
                    self.move_piece(direction, n)
                else:
                    raise RuntimeError("This would move you out of bounds")
            elif direction == 'x':
                if self.position_x + n <= self.limit and self.position_x + n\
                > -1:
                    self.move_piece(direction, n)
                else:
                    raise RuntimeError("This would move you out of bounds")
            else:
                raise RuntimeError("You did not input the command correctly")
    def search(self):
        '''
        Finds the current position of the mouse.
        :return: The x and y coordinate of the mouse
        '''
        return(mouse.position_x, mouse.position_y)
                
cat = Cat()
mouse = Mouse() 
game = True

print('Hello! Welcome to the game of Cat and Mouse! This game will test your\
searching skills as you track down an artificially controlled mouse in a\
small 4x4 field.')
print('To get started, choose a direction to move (either x for horizontal or\
 y or vertical) and then choose a number of places to move (no more than 2\
at a time).\nThis will move the Cat in that direction of the field.')
while game == True:
    try:
        choice = input('Would you like to search or Move or quit or check? \n') #allowss player to choose action
        if choice.lower() == 'quit':
                print('Quitting game...')
                game = False
                continue       
        if choice.lower() == 'check':
            print('Your current position is', cat.position_x, cat.position_y)
            continue
        if choice.lower() == 'move':
            direction = input('Give a direction to move or hit q to quit: ')
            number = input('How far would you like to move?: ')
            cat.move(direction,int(number))
            if mouse.position_x == cat.position_x and mouse.position_y == cat.position_y:
                print('You caught the Mouse! Congratulations!')
                game = False
                break
            mouse.__movement__()                
            continue
        if choice.lower() == 'search':
            pos_x, pos_y = cat.search()
            print('The mouse is at position:', pos_x, pos_y)
            continue
        if mouse.position_x == cat.position_x and mouse.position_y == cat.position_y:
            print('You caught the Mouse! Congratulations!')
            game = False
        else:
            print('That is not a possible action')
            
    except RuntimeError:
        print('Try again')
    
print ('Game Over\nRerun the game to play again!')