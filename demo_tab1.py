from burp import IBurpExtender, ITab
from javax.swing import JPanel
from java.awt import BorderLayout

class BurpExtender(IBurpExtender, ITab):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("hello woorld")
        callbacks.printOutput("hello")
        callbacks.addSuiteTab(self)
        return

    # tab name
    def getTabCaption(self):
        return "Hello world"
    
    # GUI details
    def getUiComponent(self):
        panel = JPanel(BorderLayout())
        return panel
