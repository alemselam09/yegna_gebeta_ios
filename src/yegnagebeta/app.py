import toga
from toga.style import Pack

class YegnaGebetaApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        web_view = toga.WebView(style=Pack(flex=1))
        web_view.url = 'https://test.mychurch.com.et/yegna_gebeta/'
        self.main_window.content = web_view
        self.main_window.show()

def main():
    return YegnaGebetaApp('Yegna Gebeta', 'com.alemselam09.yegnagebeta')

if __name__ == '__main__':
    main()
