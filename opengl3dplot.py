from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import umap.umap_ as umap 
import numpy as np
from PyQt6 import QtWidgets

embedding = np.load('data/map_data_3d_10000_5_manhattan_01.npy') # dataset to map/graph

app = QtWidgets.QApplication([]) #pyqtgraph event loop init 
w = gl.GLViewWidget() # create a 3d view widget isntance to render graphs in the app 
w.opts['distance'] = 20 # initial distance of the camera from the center of the scene 
w.show() # shows the instantiated widget. only needs to be called once upon instantiation  

'''
xgrid = gl.GLGridItem()
ygrid = gl.GLGridItem()
zgrid = gl.GLGridItem()
    # creates grid item
w.addItem(xgrid)
w.addItem(ygrid)
w.addItem(zgrid)

xgrid.rotate(90, 0, 1, 0)
ygrid.rotate(90, 1, 0, 0)
    # rotate grids to face the right direction
'''
# glgridviewwidget camera opts
    # azimuth -> horizontal rotation
    # elevation -> vertical rotation
    # distance -> distance of camera from the center
    # center -> camera's point of orbit -> vectorN input 

color = np.array([(1*x, 0.2+0.5*x, 1) for x in np.linspace(0, 1, embedding.shape[0])])
    # color is assigned based on index. creates a gradient affect to differentiate points 

sp1 = gl.GLScatterPlotItem(pos=embedding, size=np.ones(embedding.shape[0])*0.1, color=color, pxMode=False)
    # creates a 3d scatterplot item. pos is the data.
    # every single datapoint has been set to a size of 0.1. takes in an array to determine size
        # of each point.
    # pxMode=False makes point size is in scene coordinates rather than screen coordinates
        # scales with window size
sp1.translate(0, 0, 0) # moves points on axes (x, y, z) by amount 
w.addItem(sp1)

if __name__ == "__main__":
    import sys
    if (sys.flags.interactive !=1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec()
        
