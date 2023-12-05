from burp import IBurpExtender
from burp import IContextMenuFactory
# lContextMenuFactory returns a list of JMenuItems (returned by createMenuItems)
from javax.swing import JMenuItem, JMenu
from java.util import List, ArrayList

class BurpExtender(IBurpExtender, IContextMenuFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.helpers
        callbacks.setExtensionName("Get data")
        callbacks.registerContextMenuFactory(self)
        return

    def createMenuItems(self, context_menu):
        self.context = context_menu
        submenu = JMenu("Get Data")
        menu_list = ArrayList()
        menu_list.add(submenu)
        submenu.add(JMenuItem("Get Hosts", actionPerformed=self.new_menu_1))
        submenu.add(JMenuItem("Get Protocols", actionPerformed=self.new_menu_2))
        submenu.add(JMenuItem("Get Requests", actionPerformed=self.new_menu_3))
        submenu.add(JMenuItem("Get Responses", actionPerformed=self.new_menu_4))
        return menu_list

    def new_menu_1(self, event):
        http_traffic = self.context.getSelectedMessages()
        print('+++ HOSTS +++')
        for traffic in http_traffic:
            host1 = traffic.getHttpService().getHost()
            print("Host: " + host1)
        return
    
    def new_menu_2(self, event):
        http_traffic = self.context.getSelectedMessages()
        print('+++ PROTOCOLS +++')
        for traffic in http_traffic:
            host1 = traffic.getHttpService().getProtocol()
            print("Protocol: " + host1)
        return

    def new_menu_3(self, event):
        http_traffic = self.context.getSelectedMessages()
        print('+++ REQUESTS +++')
        for traffic in http_traffic:
            print(self._helpers.bytesToString(traffic.getRequest()))
            print("-" * 60)
        return

    def new_menu_4(self, event):
        http_traffic = self.context.getSelectedMessages()
        print('+++ RESPONSES +++')
        for traffic in http_traffic:
            print(self._helpers.bytesToString(traffic.getResponse()))
            print("*" * 60)
        return
