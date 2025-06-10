import sys
import os
from docx import Document

from PySide6.QtCore import QFile
from PySide6.QtWidgets import QApplication, QDialog, QPlainTextEdit, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PySide6.QtUiTools import QUiLoader

# ──────────────────────── Shared Constants ────────────────────────
FISH_SEQUENCES = {
    "BIGHEAD CARP": (
        "AACTTAAATAAACAGATTATTCCACTAACAATTGATTCTCAAATTTATTACTGAATTATTAACTAAAATCTAACTCAAGTATATTATTAAAGTAAGAGACCACCTACTTATTTATATTAAGGTATTATATTCATGATAAGATCAAGGACAATAACAGTGGGGGTGGCGCAAAATGAACTATTACTTGCATCTGGTTTGGAATCTCACGGACATGGCTACAAAATTCCACCCCCGTTACATTATAACTGGCATATGGTTAAATGATGTGAGTACATACTCCTCATTAACCCCACATGCCGAGCATTCTTTTAT"
    ),
    "SILVER CARP": (
        "CCTGAGAAAAGAGTTGTTCCACTATAATTGGTTCTCAAATATTTCCTTGAAATATTAACTTCTATTTAATTTAACTATATTAATGTAGTAAGAAACCACCTACTGGTTTATATTAAGGTATTCTATTCATGATAAGATCAGGGACAATAATCGTGGGGGTGGCGCAGAATGAACTATTACTTGCATTTGGC"
    ),
    "GRASS CARP": (
        "GAGTTTCTGACTTCTACCCCCTTCTTTCCTCCTACTATTAGCCTCTTCTGGTGTTGAGGCCGGAGCTGGAACAGGGTGAACAG"
    ),
    "BLACK CARP": (
        "ACACCACGTTCTTTGACCCAGCAGGCGGAGGAGACCCAATCCTATATCAACACCTGTTCTGATTCTTCGGCCACCCAGAAGTTTACATTCTTATTTTACCCGGGTTTGGGATCATTTCAC"
    ),
}
# ──────────────────────── Failsafe Dialog ────────────────────────

class EDNA_FAIL_SAFE(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()

        ui_path = os.path.join(os.path.dirname(__file__), "..", "..", "ui", "e_dna_fail_safe_dialog.ui")
        ui_path = os.path.normpath(ui_path)
        file = QFile(ui_path)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file)

        # Set the layout of this QDialog to hold the loaded UI
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)

        self.adjustSize()
        self.setWindowTitle("eDNA Fail-Safe Program")

        self.eDNAInput = self.ui.findChild(QPlainTextEdit, "eDNAInput")
        self.sampleDisplay = self.ui.findChild(QLabel, "eDNA_sample_display")

        self.finishButton = self.ui.findChild(QPushButton, "finishButton")
        self.finishButton.clicked.connect(self.identify_invasive_carp_failsafe)

    def identify_invasive_carp_failsafe(self):
        sample = self.eDNAInput.toPlainText().replace(" ", "").replace("\n", "")
        found = False
        for name, sequence in FISH_SEQUENCES.items():
            if sequence in sample:
                self.sampleDisplay.setStyleSheet("color: red;")
                self.sampleDisplay.setText(f"{name} DETECTED")
                found = True
                break
        if not found:
            self.sampleDisplay.setStyleSheet("color: #84eab3;")
            self.sampleDisplay.setText("NO INVASIVE SPECIES DETECTED")
        
    def closeEvent(self, event):
        self.sampleDisplay.setText("-----")     # Reset display label
        self.eDNAInput.clear()                  # Clear the input box
        self.sampleDisplay.setStyleSheet("color: #fafafa")    # Optional: remove previous styling
        event.accept()


# ──────────────────────── DOCX Paragraph Reader ────────────────────────

def get_paragraphs_from_docx(docx_path):
    try:
        doc = Document(docx_path)
    except Exception as e:
        print(f"❌ Error opening docx file: {e}")
        return []

    paragraphs = []
    current_para = []

    for para in doc.paragraphs:
        text = para.text.replace(" ", "")
        if text:
            current_para.append(text)
        else:
            if current_para:
                paragraphs.append("".join(current_para))
                current_para = []

    if paragraphs:
        del paragraphs[0]  # Delete header
    return paragraphs

# ──────────────────────── Logic Class ────────────────────────

class EDNA_LOGIC:
    def __init__(self, parent, labels):
        self.parent = parent
        self.labels = labels
        self.failsafe_dialog = EDNA_FAIL_SAFE(self.parent)

    def identify_invasive_carp(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent, "Select a .docx File", "", "docx Files (*.docx);;All Files (*)"
        )
        if not file_path:
            return

        paragraphs = get_paragraphs_from_docx(file_path)

        for i, label in enumerate(self.labels):
            if i >= len(paragraphs):
                label.setText("No data.")
                continue

            paragraph = paragraphs[i].replace(" ", "").replace("\n", "").upper()
            found = False
            for name, sequence in FISH_SEQUENCES.items():
                if sequence in paragraph:
                    label.setStyleSheet("background-color: red;")
                    label.setText(f"{name} DETECTED")
                    found = True
                    break
            if not found:
                label.setStyleSheet("background-color: green;")
                label.setText("NO INVASIVE SPECIES DETECTED")

    def identify_invasive_carp_failsafe(self):
        self.failsafe_dialog.show()

    def clear_results(self):
        for label in self.labels:
            label.setStyleSheet("background-color: transparent;")
            label.setText("-----")
