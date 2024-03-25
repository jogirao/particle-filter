from src.structures.map import Map

class Square():
    
    def __init__(self, coords=(0,0), width=1, height=1, corner_score=((1,1),(1,1))):
        self.coords=coords
        self.width=width
        self.height=height
        self.corners=score
    
    def split(self, grid):
        # Get map
        world_map=grid.background
        
        # Split self in 4 equal squares
        w=self.width/2
        h=self.height/2
        c_scores=self.corners
        x,y=*self.coords
        
        # Compute new point scores
        center=world_map.contains(x+w,y+h)
        left=world_map.contains(x,y+h)
        right=world_map.contains(x+(2*w),y+h)
        up=world_map.contains(x+w,y+(2*h))
        down=world_map.contains(x+w,y)
        
        # Update current square parameters
        self.corners=((c_score[0,0],down),(left,center))
        
        # Generate new squares
        
        
class Grid():
    
    def __init__(self, borders=(((0,0),(0,1),(1,1),(1,0)))):
        if len(borders)>1:
            self.map=Map(borders[0],borders[1:])
        else:
            self.map=Map(borders[0])
        self.grid=[[Square]]


Borders=[[(0.2, 0.2), (0.1, 0.7), (0.5, 0.9), (0.8, 0.6), (0.7, 0.3)],
                    [(0.3, 0.35), (0.5, 0.35), (0.5, 0.45), (0.3, 0.45)], [(0.3, 0.7), (0.4, 0.78), (0.42, 0.65)],
                    [(0.5, 0.7), (0.7, 0.6), (0.7, 0.45), (0.6, 0.46), (0.65, 0.57)]]
m=Map(Borders[0], Borders[1:])

def split_square(square):
    # Splits square area into 4 equal square areas
    width=square.width/2
    height=square.height/2
    

    square1=[coords,width,height,new_wall_prob(coords,width,height)]
    square2=[(coords[0],coords[1]+width),width,height,new_wall_prob((coords[0],coords[1]+width),width,height)]
    square3=[(coords[0]+height,coords[1]),width,height,new_wall_prob((coords[0]+height,coords[1]),width,height)]
    square4=[(coords[0]+height,coords[1]+width),width,height,new_wall_prob((coords[0]+height,coords[1]+width),width,height)]
    
    
def new_wall_prob(world_map, point, width, height):
    # Checks probability of area containing an obstacle
    corners=[point, (point[0],point[1]+height), (point[0]+width,point[1]), (point[0]+width,point[1]+height)]
    score=4
    for corner in corners:
        score-=world_map.contains(*corner)
    return score/4

def 
    
  