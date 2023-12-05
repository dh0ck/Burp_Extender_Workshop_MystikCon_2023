from burp import IBurpExtender

class BurpExtender1(IBurpExtender):
    # Function indicated in IBurpExtender interface
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("hello woorld")
        callbacks.printOutput("Hello!")
        return

