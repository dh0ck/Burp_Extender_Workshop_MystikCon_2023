from burp import IBurpExtender

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        a = callbacks.getHelpers()
        print(dir(a))
