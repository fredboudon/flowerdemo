
def oldmain():
    from cambridgedemo import main
    main()

from PyQt4.Qt import QApplication,QMainWindow
from base import DemoWidget, SceneView
from starter import MenuView
from naked import NakedView
from abcmodel import ABCView
from bouquet import BouquetView
from geneshape import GeneShapeView
from about import AboutView

def main(args = None):
    if args is None:
        import sys
        args = sys.argv
    
    
    app = QApplication(args)
    
    mainwindow = QMainWindow()
    window = DemoWidget()
    mainwindow.setCentralWidget(window)
    panels = []
    pid = window.appendView(NakedView(window))
    panels += [(pid,'deshabillezmoi.png')]
    pid = window.appendView(GeneShapeView(window))
    panels += [(pid,'formegene.png')]
    pid = window.appendView(ABCView(window))
    panels += [(pid,'abc.png')]
    if '-3' not in args:
        pid = window.appendView(BouquetView(window))
        panels += [(pid,'bouquet.png')]
    #pid = window.appendView(SceneView(window))
    #panels += [(pid,'fleuralautre.png')]
    menu = MenuView(window)
    menuid = window.appendInitialView(menu)
    menu.setPanels(panels)
    window.appendAboutView(AboutView(window))
    #window.setCurrentViewId(1)
    print 'show'
    #mainwindow.resize(800,600)
    #mainwindow.show()
    mainwindow.showFullScreen()   
    app.exec_()
    
    
if __name__ == '__main__':
    import sys
    main(sys.argv)