#!/usr/bin/env python3

import abscplane as cp

class ComplexPlane(cp.AbsComplexPlane):
    def __init__(self,newXmin,newXmax,newYmin,newYmax):
        self.xmin  = newXmin
        self.xmax  = newXmax
        self.xlen  = 20  #make sure this is never able to be 0
        self.ymin  = newYmin
        self.ymax  = newYmax
        self.ylen  = 20  #make sure this can never be 0
        self.xstep = (self.xmax - self.xmin)/self.xlen
        self.ystep = (self.ymax - self.ymin)/self.ylen
        self.f     = lambda x: x
        self.plane = [[self.f(( j*self.xstep + self.xmin ) + ( i*self.ystep + self.ymin )*1j) for i in range(self.ylen)] for j in range(self.xlen)]
    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
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
        self.xstep = (self.xmax - self.xmin)/self.xlen
        self.ystep = (self.ymax - self.ymin)/self.ylen
        self.refresh()
    def set_f(self, newF):
        """Reset the transformation function f.
        Refresh the plane as needed."""
        self.f = newF
        self.refresh()

