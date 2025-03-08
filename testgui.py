import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from io import BytesIO
import base64

# Cyberpunk-style colors
CYBERPUNK_COLORS = ['#ff00ff', '#00ffff', '#ff8800', '#44ff44', '#8888ff']

class CyberpunkGraphApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyberpunk Graph Viewer")
        self.setGeometry(100, 100, 1000, 600)
        
        # Main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        # Layout
        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)
        
        # Button to generate a new graph
        self.button = QPushButton("Generate Cyberpunk Graph")
        self.button.clicked.connect(self.update_graph)
        layout.addWidget(self.button)
        
        # Quit button
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)
        
        # WebEngineView to display graphs
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        self.update_graph()

    def generate_graph(self):
        """Generate a random cyberpunk-style graph and return as HTML-embedded image."""
        df = pd.DataFrame({
            'X': np.linspace(0, 10, 100),
            'Y': np.sin(np.linspace(0, 10, 100)) + np.random.rand(100) * 0.5
        })
        
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(df['X'], df['Y'], color=np.random.choice(CYBERPUNK_COLORS), linewidth=2, alpha=0.9)
        ax.set_facecolor('#101018')
        ax.spines['bottom'].set_color('#00ffff')
        ax.spines['left'].set_color('#ff00ff')
        ax.spines['right'].set_color('#444')
        ax.spines['top'].set_color('#444')
        ax.grid(color='#ff8800', linestyle='dotted', linewidth=0.5)
        
        # Convert plot to base64 image
        buffer = BytesIO()
        plt.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
        plt.close(fig)
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return f'<img src="data:image/png;base64,{image_base64}" style="width:100%; border-radius:10px; box-shadow: 0 0 10px #ff00ff;">'

    def update_graph(self):
        """Update the web view with a new cyberpunk graph."""
        html_template = f"""
        <html>
        <head>
            <style>
                body {{ background-color: #101018; color: #00ffff; text-align: center; font-family: Arial, sans-serif; }}
                h2 {{ color: #ff00ff; }}
            </style>
        </head>
        <body>
            <h2>Test Gui</h2>
            {self.generate_graph()}
        </body>
        </html>
        """
        self.web_view.setHtml(html_template)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CyberpunkGraphApp()
    window.show()
    sys.exit(app.exec())