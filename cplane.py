#!/usr/bin/env python3

import abscplane as cp

"""This is the Class ComplexPlane.  It is built from the Abstract Class AbsComplexPlane.
This Class serves as a simplistic pan/zoom over a 2D complex plane, where each point in the
plane undergoes a transformation through the function f(), where the value at the coordinate
point is:
    value = f( x + yj )
"""

class ComplexPlane(cp.AbsComplexPlane):
    def __init__(self,newXmin,newXmax,newYmin,newYmax):
        """This is the creator.  It must be passed the the min/max X and Y values for the plane, and creates a 2D plane filled with the
        X & Y complex number coordinates of the specified plane.  Note that the initial function f() for computing the values in the plane
        is the identity function, so the values at the coordinate location are the coordinates themselves.  Note also that the number of
        points in each axis is always forced to be 20."""
        self.xmin  = newXmin
        self.xmax  = newXmax
        self.xlen  = 20  #make sure this is never able to be 0
        self.ymin  = newYmin
        self.ymax  = newYmax
        self.ylen  = 20  #make sure this can never be 0
        #  must add 1 to get the correct actual step size, otherwise last element does not equal x or y max
        self.xstep = (self.xmax - self.xmin + 1)/self.xlen
        self.ystep = (self.ymax - self.ymin + 1)/self.ylen
        self.f     = lambda x: x
        #  compute the value at each of the coordinate points in the plane
        self.plane = [[self.f(( j*self.xstep + self.xmin ) + ( i*self.ystep + self.ymin )*1j) for i in range(self.ylen)] for j in range(self.xlen)]

    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
        #  using the current function f(), re-compute the value at each of the coordinate points in the plane
        self.plane = [[self.f(( j*self.xstep + self.xmin ) + ( i*self.ystep + self.ymin )*1j) for i in range(self.ylen)] for j in range(self.xlen)]

    def zoom(self, newXmin, newXmax, newYmin, newYmax):
        """Reset self.xmin, self.xmax, and/or self.xlen.
        Also reset self.ymin, self.ymax, and/or self.ylen.
        Zoom into the indicated range of the x- and y-axes.
        Refresh the plane as needed."""
        self.xmin  = newXmin
        self.xmax  = newXmax
        self.ymin  = newYmin
        self.ymax  = newYmax
        #  must add 1 to get the correct actual step size, otherwise last element does not equal x or y max
        self.xstep = (self.xmax - self.xmin + 1)/self.xlen
        self.ystep = (self.ymax - self.ymin + 1)/self.ylen
        self.refresh()

    def set_f(self, newF):
        """Reset the transformation function f.
        Refresh the plane as needed."""
        self.f = newF
        self.refresh()

#  unit testing functions beyond this point
def test_init_no_params():
    """Test the creator by passing no parameters.  Should cause a TypeError exception"""
    success = False

    try:
        testPlane = ComplexPlane()
    except TypeError:
        """test passes"""
        success = True

    message = 'Creator should have generated a TypeError exception, as no required parameters were passed'
    assert success, message


def test_init():
    """Test the creator by passing the required parameters.  The passed in values should match the object's values"""
    success = True

    try:
        xmin = 2
        xmax = 6
        ymin = -6
        ymax = -2
        testPlane = ComplexPlane( xmin, xmax, ymin, ymax )

        #  this line is to force an error to prov the test can fail
        # xmin = xmin + 1

        #  check that the parameters are all correctly stored
        if testPlane.xmin != xmin or testPlane.xmax != xmax or testPlane.ymin != ymin or testPlane.ymax != ymax:
           message = 'Init parameter mismatch: expected %d %d %d %d, actual %d %d %d %d' % (xmin, xmax, ymin, ymax, testPlane.xmin, testPlane.xmax, testPlane.ymin, testPlane.ymax)
           success = False

    except TypeError:
        """Test fails, should not have generated an exception"""
        message = 'Creator generated an exception when correct number of parameters were passed in'
        success = False

    assert success, message


def f2x(x):
    """function is only used for testing purposes"""
    return( 2*x )

def test_setf1():
    """Test that setting the function to a new function updates the plane with the new transformation values"""
    #  create a plane
    tp = ComplexPlane( 1, 10, 1, 10 )
    #  set the function to be f(x) = 2*x
    tp.set_f( f2x )

    # set up the expected plane
    xmin = 1
    xmax = 10
    xstep = 0.5
    xlen = 20
    ymin = 1
    ymax = 10
    ystep = 0.5
    ylen = 20
    eplane = [[2*(( j*xstep + xmin ) + ( i*ystep + ymin )*1j) for i in range(ylen)] for j in range(xlen)]

    #  this line is to force an error to prove the test can fail
    #eplane[1][1] = 5

    #  do the expected and actual planes match?
    success = tp.plane == eplane
    message = 'set_f() did not correctly transform the plane to double the coordinate values'
    assert success, message



def test_setf2():
    """Set the transformation function to be something other than a function(), which should fail,
    meaning the test was successful"""
    #  create a plane
    tp = ComplexPlane( 1, 10, 1, 10 )

    try:
        #  set the function to be f(x) = 2*x
        tp.set_f( tp )
        message = 'Test Failed, succeeded in setting function to a non-function value'
        success = False
    except TypeError:
        """Test succeeds, exception generated"""
        success = True

    assert success, message

def test_zoom1():
    """Test the zoom function with valid values.  Zoom should move/reset the 2D plane to a known configuration"""
    # set up the expected plane
    xmin = 1
    xmax = 10
    xstep = 0.5
    xlen = 20
    ymin = 1
    ymax = 10
    ystep = 0.5
    ylen = 20
    eplane = [[(( j*xstep + xmin ) + ( i*ystep + ymin )*1j) for i in range(ylen)] for j in range(xlen)]

    #  create a plane
    tp = ComplexPlane( 100, 200, -100, 0 )
    tp.zoom(xmin, xmax, ymin, ymax)

    #  do the expected and actual planes match?
    success = tp.plane == eplane
    message = 'zoom() did not correctly transform the plane to the new coordinate values'
    assert success, message

def test_zoom2():
    """Test the zoom function with invalid values.  Zoom should generate an exception"""
    #  create a plane
    tp = ComplexPlane( 100, 200, -100, 0 )
    try:
        tp.zoom( "one", 100, -1, 3)
        message = 'Test Failed, zoom did not catch use of an invalid parameter'
        success = False
    except TypeError:
        """Test succeeds, exception generated"""
        success = True

    assert success, message



def test_refresh1():
    """Test the refresh function.  Create a plane, corrupt the data in the plane, refresh and verify the data is once again correct"""
    #  create a plane
    tp = ComplexPlane( 100, 200, -100, 0 )
    #  create a duplicate plane
    ep = ComplexPlane( 100, 200, -100, 0 )

    #  corrupt the original test plane
    tp.plane = [[(-1 +  -1j) for i in range(tp.ylen)] for j in range(tp.xlen)]

    # refresh the plane
    tp.refresh()

    #  this line is to force an error to prove the test can fail
    #ep.plane[1][1] = -1

    #  do the expected and actual planes match?
    success = tp.plane == ep.plane
    message = 'refresh() did not correctly retore the plane to the expected coordinate values'
    assert success, message

