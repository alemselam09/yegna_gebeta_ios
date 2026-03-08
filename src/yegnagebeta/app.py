import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class YegnaGebetaApp(toga.App):
    def startup(self):
        # ዋናውን መስኮት ፍጠር
        self.main_window = toga.MainWindow(title=self.formal_name)

        # የዌብ እይታ (Web View) ክፍል ፍጠር
        web_view = toga.WebView(style=Pack(flex=1))

        # የኛ ገበታ ድረ-ገጽን ጫን
        web_view.url = 'https://test.mychurch.com.et/yegna_gebeta/'

        # የዌብ እይታውን በዋናው መስኮት ላይ አስቀምጥ
        self.main_window.content = web_view

        # መስኮቱን አሳይ
        self.main_window.show()

def main():
    return YegnaGebetaApp('የኛ ገበታ', 'com.alemselam09.yegnagebeta')

if __name__ == '__main__':
    main()
