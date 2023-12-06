#######################################
# LAB 9 - Wind Turbine Placement OOP  #
#######################################

import csv

class Point:
    """
    A point in a two-dimensional coordinate plane
    """
    
    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Rectangle Class
############################
class Rectangle:
    """
    A rectangle in a two-dimensional coordinate plane
    """
    
    def __init__(self, bottom_left_x, bottom_left_y, top_right_x, top_right_y):
        """
        Create a rectangle defined by its bottom left and top right corner
        coordinates
        """
        self.bottom_left = Point(bottom_left_x, bottom_left_y)
        self.top_right = Point(top_right_x, top_right_y)
        
    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Rectangle with corner coordinates " + 
                str(self.bottom_left) + ", " + str(self.top_right))
    
    def move(self, horizontal_translation, vertical_translation):
        """
        (Rectangle, int, int) -> None
        
        Alters the location of a rectangle by translating the coordinates
        of its bottom left and top right corner coordinates.
        """
        # TODO your code here (~4 lines of code)
        self.bottom_left.x=self.bottom_left.x+horizontal_translation
        self.bottom_left.y=self.bottom_left.y+vertical_translation
        self.top_right.x=self.top_right.x+horizontal_translation
        self.top_right.y=self.top_right.y+vertical_translation
        
        

    def overlap(self, rectB):
        """
        (Rectangle, Rectangle) -> bool
        
        Checks whether two rectangles overlap
        """
        
        # check if one rectangle is on the left side of the other
        horizontal_clearance = ((self.bottom_left.x >= rectB.top_right.x) or
                                (self.top_right.x <= rectB.bottom_left.x))
        
        # check if one rectangle is above the other
        vertical_clearance = ((self.bottom_left.y >= rectB.top_right.y) or
                              (self.top_right.y <= rectB.bottom_left.y))
        
        return not (horizontal_clearance or vertical_clearance)

##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """
    
    def __init__(self, id_number, placement_bottom_left_x, placement_bottom_left_y,
                 placement_top_right_x, placement_top_right_y):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Rectangle(placement_bottom_left_x,placement_bottom_left_y,
                                   placement_top_right_x, placement_top_right_y)
        
        self.overlapping_turbines = []
    
    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

        
    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None
        
        Alters the location of a wind turbine by translating the coordinates
        of its bottom left and top right corner coordinates. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.
        
        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        # TODO your code here (~2 lines of code)
        self.placement.move(horizontal_translation,vertical_translation)
    
    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool
        
        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        # TODO your code here (~1 line of code)
        return (self.placement.overlap(turbineB.placement))
    
    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None
        
        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        # TODO your code here
        for i in turbines:
            if self.overlap(i):
                if self.id_number!=i.id_number:
                    self.overlapping_turbines.append(i)

##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (corner coordinates) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """

    # TODO your code here
    windturbine_lst=list()
    with open(turbine_filename, "r") as myfile:
        next(myfile)
        r_myfile=csv.reader(myfile, delimiter=',')
        for row in r_myfile:
            i = int(row[0])
            x1 = int(row[1])
            y1 = int(row[2])
            x2 = int(row[3])
            y2 = int(row[4]) 
            windturbine_lst.append(WindTurbine(i, x1, y1, x2,y2))
    myfile.close
    return windturbine_lst
        

##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int
    
    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.
    
    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    
    # TODO your code here
    counter=0
    for item in turbines:
        item.validate_placement(turbines)
        if len(item.overlapping_turbines)>0:
            counter+=1
    return counter
