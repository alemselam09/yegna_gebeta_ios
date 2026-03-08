import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class YegnaGebetaApp(toga.App):

    def startup(self):

        self.main_window = toga.MainWindow(title=self.formal_name)

        webview = toga.WebView(
            url="https://test.mychurch.com.et/yegna_gebeta/",
            style=Pack(flex=1)
        )

        box = toga.Box(
            children=[webview],
            style=Pack(direction=COLUMN)
        )

        self.main_window.content = box
        self.main_window.show()


def main():
    return YegnaGebetaApp()
