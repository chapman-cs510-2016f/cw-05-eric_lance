#!/usr/bin/env python3

import abscplane as cp

class ComplexPlane(cp.AbsComplexPlane):
    
    def __init__(self):
        self.xmin  = -100.
        self.xmax  = 100.
        self.xlen  = 200. #make sure this is never able to be 0
        self.ymin  = -100.
        self.ymax  = 100.
        self.ylen  = 200. #make sure this can never be 0
        self.xstep = (self.xmax - self.xmin)/self.xlen
        self.ystep = (self.ymax - self.ymin)/self.ylen
        self.f     = lambda x: 2*x
        self.plane = [[(( j*xstep + xmin ) + ( i*ystep + ymin )*1j) for i in range(ylen)] for j in range(xmin,xmax)]

    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
        self.plane = [[self.f(( j*xstep + xmin ) + ( i*ystep + ymin )*1j) for i in range(ylen)] for j in range(xmin,xmax)]

    def zoom(self):
        """Reset self.xmin, self.xmax, and/or self.xlen.
        Also reset self.ymin, self.ymax, and/or self.ylen.
        Zoom into the indicated range of the x- and y-axes.
        Refresh the plane as needed."""
        pass
    
    def set_f(self):
        """Reset the transformation function f.
        Refresh the plane as needed."""
        pass

