from burp import IBurpExtender, ITab
from javax.swing import JPanel, BoxLayout, JSplitPane, JTextField, JButton, JTable
from javax.swing.table import DefaultTableModel
from java.awt import BorderLayout

class BurpExtender(IBurpExtender, ITab):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("hello woorld")
        callbacks.printOutput("hello")
        callbacks.addSuiteTab(self)
        return

    # tab name
    def getTabCaption(self):
        return "Hello world 2"
    
    def clicked(self, e):
        self.textField.setText("test 123") 

    # GUI details
    def getUiComponent(self):
        panel = JPanel(BorderLayout())
        
        panel2 = JPanel()
        # for vertical alignment of components of panel 2:
        panel2.setLayout(BoxLayout(panel2, BoxLayout.Y_AXIS))

        spl = JSplitPane(JSplitPane.HORIZONTAL_SPLIT)
        spl.setDividerLocation(100)

        # contents of left side
        self.textField = JTextField()
        spl.leftComponent = self.textField

        # contents of right side
        self.data = [['1', '2', '3'], ['4', '5', '6']]
        colNames = ('Col 1', 'Col 2', 'Col 3')

        dataModel = DefaultTableModel(self.data, colNames)
        panel2.add(JButton("hello", actionPerformed = self.clicked))
        panel2.add(JTable(dataModel))
        spl.rightComponent = panel2

        panel.add(spl)
        return panel


        return panel
