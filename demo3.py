from burp import IBurpExtender

class BurpExtender(IBurpExtender):

    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Requests")
        import platform
        callbacks.printOutput(platform.python_version())
        import requests
        a = requests.get("http://meta.com")
        callbacks.printOutput(a.text)
        return
