from burp import IBurpExtender
from burp import IContextMenuFactory
from javax.swing import JMenuItem, JMenu
from java.util import List, ArrayList

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        callbacks.setExtensionName("New menus")
        callbacks.registerContextMenuFactory(self)
        return

    def createMenuItems(self, context_menu):
        self.context = context_menu
        submenu = JMenu("Submenu")
        menu_list = ArrayList()
        menu_list.add(JMenuItem("Item 1", actionPerformed=self.new_menu_1))
        menu_list.add(submenu)
        submenu.add(JMenuItem("Item 2", actionPerformed=self.new_menu_2))
        return menu_list

    def new_menu_1(self, event):
        print("xxx")
        pass

    def new_menu_2(self, event):
        print("yyy")
        pass
