import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from database import create_database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Control de Asistencia")
        self.setGeometry(100, 100, 1000, 800)

        # Crear un QWebEngineView para mostrar el contenido HTML
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        # Obtener la ruta absoluta del archivo HTML
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, "index.html")
        
        # Verificar si el archivo HTML existe
        if not os.path.exists(html_path):
            QMessageBox.critical(self, "Error", f"No se pudo encontrar el archivo HTML en: {html_path}")
            sys.exit(1)

        # Cargar el archivo HTML local
        self.web_view.setUrl(QUrl.fromLocalFile(html_path))

        # Conectar las funciones de Python con JavaScript
        self.web_view.loadFinished.connect(self.onLoadFinished)

    def onLoadFinished(self, ok):
        if ok:
            self.web_view.page().runJavaScript("""
                var pyqtBridge = {
                    openAttendanceRegister: function() { console.log("Abriendo registro de asistencia"); },
                    openStatisticsView: function() { console.log("Abriendo vista de estadísticas"); },
                    generateReport: function() { console.log("Generando informe"); },
                    openAdminPanel: function() { console.log("Abriendo panel de administración"); }
                };
            """)
        else:
            QMessageBox.warning(self, "Error", "No se pudo cargar el archivo HTML")

if __name__ == "__main__":
    create_database()  # Crear la base de datos si no existe
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())