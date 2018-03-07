"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Noelle Hale.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500, 400)

    centerpoint1 = rg.Point(100, 100)
    radius1 = 50
    circle1 = rg.Circle(centerpoint1, radius1)
    circle1.fill_color = 'plum3'
    circle1.attach_to(window)

    centerpoint2 = rg.Point(300,200)
    radius2 = 25
    circle2 = rg.Circle(centerpoint2, radius2)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()

    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window = rg.RoseWindow(700,500)

    center = rg.Point(150,400)
    radius = 100
    circle = rg.Circle(center, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    circle_outline = circle.outline_thickness
    circle_fill = circle.fill_color
    circle_center = circle.center
    center_x = center.x
    center_y = center.y

    print("circle outline thickness:", circle_outline)
    print("fill color:", circle_fill)
    print("center:", circle_center)
    print("center x-coordinate:", center_x)
    print("center y-coordinate:", center_y)

    #start rectangle
    r1 = rg.Point(425,50)
    r2 = rg.Point(690,175)
    rectangle = rg.Rectangle(r1, r2)
    rectangle.attach_to(window)

    rect_outline = rectangle.outline_thickness
    rect_fill = rectangle.fill_color
    rect_center = rect_cent_x, rect_cent_y
    rect_cent_x = (r1.x +r2.x)/2
    rect_cent_y = (r1.y +r2.y)/2

    window.render()



    window.close_on_mouse_click()
    # -------------------------------------------------------------------------
    # TODO: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
