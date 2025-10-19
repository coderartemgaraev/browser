import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Создаем веб-виджет
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        # Создаем панель навигации
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)
        
        # Кнопка "Назад"
        back_btn = QAction("←", self)
        back_btn.triggered.connect(self.browser.back)
        nav_bar.addAction(back_btn)
        
        # Кнопка "Вперед"
        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_btn)
        
        # Кнопка "Обновить"
        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_btn)
        
        # Кнопка "Домой"
        home_btn = QAction("🏠", self)
        home_btn.triggered.connect(self.navigate_home)
        nav_bar.addAction(home_btn)
        
        # Адресная строка
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)
        
        # Кнопка "Перейти"
        go_btn = QAction("➤", self)
        go_btn.triggered.connect(self.navigate_to_url)
        nav_bar.addAction(go_btn)
        
        # Обновление URL в адресной строке при навигации
        self.browser.urlChanged.connect(self.update_url)
        
        # Устанавливаем браузер как центральный виджет
        self.setCentralWidget(self.browser)
        
        # Настройки окна
        self.setWindowTitle("Max = Loser! (Google Chrome 2.0 (by ARTEMKA inc.) - Linux Edition)")
        self.setGeometry(100, 100, 1200, 800)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        self.browser.setUrl(QUrl(url))
        
    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Настройка настроек для лучшей совместимости
    QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
    QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
    
    browser = SimpleBrowser()
    browser.show()
    
    sys.exit(app.exec_())