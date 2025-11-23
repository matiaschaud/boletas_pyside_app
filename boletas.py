import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QFileDialog,
    QMessageBox,
    QLineEdit,
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPalette, QColor, QIcon
import fitz  # PyMuPDF

from ui_boletas import Ui_MainWindow
from datetime import datetime
import pandas as pd
from pathlib import Path
import re
import os
import shutil


def extraer_numeros(cadena):
    # Utilizar expresión regular para encontrar todos los números en la cadena
    numeros = re.findall(r"\d+", cadena)
    # Unir los números encontrados en una sola cadena
    numeros_concatenados = "".join(numeros)
    return numeros_concatenados


formato_original_fecha = "%d de %B de %Y"
meses = {
    "Enero": "January",
    "Febrero": "February",
    "Marzo": "March",
    "Abril": "April",
    "Mayo": "May",
    "Junio": "June",
    "Julio": "July",
    "Agosto": "August",
    "Septiembre": "September",
    "Octubre": "October",
    "Noviembre": "November",
    "Diciembre": "December",
}


def month_to_mes(fecha_str):
    # Reemplazar el mes en español por su equivalente en inglés
    for mes_es, mes_en in meses.items():
        if mes_es in fecha_str:
            return fecha_str.replace(mes_es, mes_en)


def get_pdf_text(pdf_document_path):
    # Abrir un archivo PDF
    # pdf_document = "bhe_16610440-24.pdf"
    doc = fitz.open(pdf_document_path)

    # Extraer texto de la primera página
    pagina = doc[0]  # Acceder a la primera página
    texto = pagina.get_text()

    # Cerrar el documento
    doc.close()

    return texto


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Franchu's App")
        self.setWindowIcon(
            QIcon(
                str(
                    Path(os.path.abspath(__file__)).parent
                    / "resources"
                    / "logo_franchu_fitness_head.png"
                )
            )
        )

        self.folder_path = ""
        self.rut_empleador = "776017809"
        self.event_date = ""

        # Setea por defecto el rut más comunmente usado
        self.rutEmpleadorEditText.setText("776017809")

        # Configura el modelo de la lista
        self.modelListView = QStandardItemModel()
        self.pdfsListView.setModel(self.modelListView)

        # Conexiones
        self.folderPathButton.clicked.connect(self.cargar_pdfs_en_listview)
        # self.pdfsListView.clicked.connect(self.on_item_clicked)
        self.generateScrapTableButton.clicked.connect(self.create_report)
        self.rutEmpleadorEditText.textChanged.connect(self.update_rut_empleador)
        self.fechaEventoDateEdit.dateChanged.connect(self.update_date)
        self.changeNamesButton.clicked.connect(self.update_pdf_names)

        # Conectar la señal currentChanged a la función on_item_changed
        selection_model = self.pdfsListView.selectionModel()
        selection_model.currentChanged.connect(self.on_item_changed)

        # Añade los datos leidos por el pdf seleccionado en el groupBox
        # Hace que el formulario izquierdo ocupe mas espacio que el derecho dentro del horizontal layout
        self.horizontalLayout_4.setStretch(
            0, 3
        )  # El formulario izquierdo ocupará 3 partes
        self.horizontalLayout_4.setStretch(
            1, 1
        )  # El formulario derecho ocupará 1 parte

        # Layout izquierdo
        self.nro_boleta_line_edit = QLineEdit()
        self.nro_boleta_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow("N° boleta:", self.nro_boleta_line_edit)
        self.nombre_line_edit = QLineEdit()
        self.nombre_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow("Nombre:", self.nombre_line_edit)
        self.rut_empleado_line_edit = QLineEdit()
        self.rut_empleado_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow("Rut empleado:", self.rut_empleado_line_edit)
        self.rut_empleador_line_edit = QLineEdit()
        self.rut_empleador_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow("Rut empleador:", self.rut_empleador_line_edit)
        self.fecha_evento_line_edit = QLineEdit()
        self.fecha_evento_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow("Fecha evento:", self.fecha_evento_line_edit)
        self.atencion_profesional_line_edit = QLineEdit()
        self.atencion_profesional_line_edit.setEnabled(False)
        self.formLayoutLeft.addRow(
            "Atención profesional:", self.atencion_profesional_line_edit
        )
        # Layout derecho
        self.total_honorarios_line_edit = QLineEdit()
        self.total_honorarios_line_edit.setEnabled(False)
        self.formLayoutRight.addRow(
            "Total honorarios:", self.total_honorarios_line_edit
        )
        self.impuesto_retenido_line_edit = QLineEdit()
        self.impuesto_retenido_line_edit.setEnabled(False)
        self.formLayoutRight.addRow(
            "Impuesto retenido:", self.impuesto_retenido_line_edit
        )
        self.neto_honorarios_line_edit = QLineEdit()
        self.neto_honorarios_line_edit.setEnabled(False)
        self.formLayoutRight.addRow("Neto honorarios:", self.neto_honorarios_line_edit)

    def on_item_changed(self, current, previous):
        item = self.modelListView.itemFromIndex(current)
        pdf_path = f"{self.folder_path}/{item.text()}"
        self.load_pdf(pdf_path)
        boleta = self.get_boleta_info(pdf_path)

        self.nro_boleta_line_edit.setText(boleta["nro_boleta"])
        self.nombre_line_edit.setText(boleta["nombre"])
        self.fecha_evento_line_edit.setText(boleta["fecha_evento"])
        self.rut_empleado_line_edit.setText(boleta["rut_empleado"])
        self.rut_empleador_line_edit.setText(boleta["rut_empleador"])
        self.atencion_profesional_line_edit.setText(boleta["atencion_profesional"])
        self.total_honorarios_line_edit.setText(boleta["total_honorarios"])
        self.neto_honorarios_line_edit.setText(boleta["neto_honorarios"])
        self.impuesto_retenido_line_edit.setText(boleta["impuesto_retenido"])

    def update_pdf_names(self):

        items = self.listar_archivos_pdf()
        boletas_repetidas = []
        for item in items:
            pdf_path = f"{self.folder_path}/{item}"
            boleta = self.get_boleta_info(pdf_path)
            try:
                os.rename(pdf_path, f"{self.folder_path}/{boleta['nombre']}.pdf")
            except FileExistsError:
                boletas_repetidas.append(pdf_path)

        if boletas_repetidas:
            print(boletas_repetidas)
            export_folder = f"{self.folder_path}/boletas_repetidas"

            os.makedirs(f"{export_folder}", exist_ok=True)

            for boleta_repetida in boletas_repetidas:
                shutil.copy2(
                    boleta_repetida,
                    export_folder + f'/{boleta_repetida.split("/")[-1]}',
                )
                os.remove(boleta_repetida)
            mensaje = QMessageBox()
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setText(
                f"Algunas boletas estaban repetidas, se copiaron a la carpeta 'boletas_repetidas'"
            )
            mensaje.setWindowTitle("Alerta")
            mensaje.setStandardButtons(QMessageBox.Ok)
            mensaje.exec()

        self._cargar_pdfs_en_listview(items)

    #    def on_item_clicked(self, index):
    #        item = self.modelListView.itemFromIndex(index)
    #        pdf_path = f"{self.folder_path}/{item.text()}"
    #        self.load_pdf(pdf_path)
    #        boleta = self.get_boleta_info(pdf_path)
    #
    #        self.nro_boleta_line_edit.setText(boleta["nro_boleta"])
    #        self.nombre_line_edit.setText(boleta["nombre"])
    #        self.fecha_evento_line_edit.setText(boleta["fecha_evento"])
    #        self.rut_empleado_line_edit.setText(boleta["rut_empleado"])
    #        self.rut_empleador_line_edit.setText(boleta["rut_empleador"])
    #        self.atencion_profesional_line_edit.setText(boleta["atencion_profesional"])
    #        self.total_honorarios_line_edit.setText(boleta["total_honorarios"])
    #        self.neto_honorarios_line_edit.setText(boleta["neto_honorarios"])
    #        self.impuesto_retenido_line_edit.setText(boleta["impuesto_retenido"])

    def get_boleta_info(self, pdf_document_path):
        boleta = {}
        inicio_atencion_profesional = 0
        final_atencion_profesional = 0

        texto = get_pdf_text(pdf_document_path)
        boleta_txt = texto.split("\n")
        boleta["nombre"] = boleta_txt[0].title()
        for i, txt in enumerate(boleta_txt):
            if txt.startswith("N ° "):
                boleta["nro_boleta"] = txt.split(" ")[-1]
                continue

            if txt.startswith("RUT:"):
                boleta["rut_empleado"] = (
                    txt.split(":")[-1].replace(" ", "").replace("−", "-")
                )
                continue

            if txt.startswith("Fecha:"):
                fecha_str = month_to_mes(txt.split(":")[-1].strip())
                fecha_obj = datetime.strptime(fecha_str, formato_original_fecha)
                boleta["fecha_evento"] = fecha_obj.strftime("%d/%m/%Y")
                continue

            if txt.startswith("Rut:"):
                boleta["rut_empleador"] = (
                    txt.split(":")[-1].replace(" ", "").replace("−", "-")
                )

            if txt.startswith("Por atención profesional:"):
                inicio_atencion_profesional = i + 1
                continue

            if txt.startswith("Total Honorarios:"):
                final_atencion_profesional = i - 1
                boleta["total_honorarios"] = boleta_txt[i + 1]
                continue

            if txt.endswith("Impto. Retenido:"):
                boleta["impuesto_retenido"] = boleta_txt[i + 1]
                continue

            if txt.startswith("Total:"):
                boleta["neto_honorarios"] = boleta_txt[i + 1]
                continue

        boleta["atencion_profesional"] = " ".join(
            boleta_txt[inicio_atencion_profesional:final_atencion_profesional]
        )

        return boleta

    def add_checks(self, boleta, rut_empleador, fecha_evento):
        boleta["rut_emplaedor_check"] = (
            extraer_numeros(boleta["rut_empleador"]) == rut_empleador
        )
        boleta["fecha_evento_check"] = boleta["fecha_evento"] == fecha_evento

    def create_report(self):

        if self.modelListView.rowCount() == 0:
            QMessageBox.warning(
                self,
                "No hay PDFs cargados.",
                "Por favor selecciona la carpeta que contiene los PDFs de las boletas.",
            )
            return

        if self.rut_empleador == "":
            QMessageBox.warning(
                self,
                "RUT empleador no agregado.",
                "Por favor coloque el rut del empleador antes de continuar, será utilizado para el chequeo de las boletas.",
            )
            return

        if self.event_date == "":
            QMessageBox.warning(
                self,
                f"Fecha del evento no especificada, aún la default está seteada {self.fechaEventoDateEdit.date()}",
                "Por favor especifique la fecha del evento, será utilizado para el chequeo de las boletas.",
            )
            return

        pdfs = self.listar_archivos_pdf()

        boletas = []
        for pdf in pdfs:
            boleta = self.get_boleta_info(self.folder_path + "/" + pdf)
            self.add_checks(boleta, self.rut_empleador, self.event_date)
            boletas.append(boleta)

        boletas_report = pd.DataFrame(boletas)
        fields_order = [
            "rut_empleado",
            "nombre",
            "nro_boleta",
            "fecha_evento",
            "rut_empleador",
            "total_honorarios",
            "impuesto_retenido",
            "neto_honorarios",
            "atencion_profesional",
            "rut_emplaedor_check",
            "fecha_evento_check",
        ]
        datetime_now = (
            str(datetime.now())
            .split(".")[0]
            .replace(" ", "_")
            .replace(":", "")
            .replace(".", "")
            .replace("-", "")
        )

        export_folder_name = "Data exports"
        os.makedirs(f"{self.folder_path}/{export_folder_name}", exist_ok=True)

        float_fields = ["total_honorarios", "impuesto_retenido", "neto_honorarios"]

        for field in float_fields:
            boletas_report[field] = boletas_report[field].astype(float)

        boletas_report[fields_order].to_csv(
            f"{self.folder_path}/{export_folder_name}/boletas_report_{datetime_now}.csv"
        )
        boletas_report[fields_order].to_excel(
            f"{self.folder_path}/{export_folder_name}/boletas_report_{datetime_now}.xlsx"
        )

        QMessageBox.information(
            self,
            "Tablas creadas con éxito!",
            "Las tablas en formato csv y excel fueron creadas con éxito dentro de la carpeta 'Data exports'.",
        )
        return

    def listar_archivos_pdf(self):
        # Verificar si la carpeta existe
        if not os.path.exists(self.folder_path):
            print("La carpeta no existe.")
            return []

        # Lista para almacenar los archivos PDF
        archivos_pdf = []

        # Recorrer los archivos en la carpeta
        for nombre_archivo in os.listdir(self.folder_path):
            # Verificar si el archivo tiene la extensión .pdf
            if nombre_archivo.lower().endswith(".pdf"):
                archivos_pdf.append(nombre_archivo)

        return archivos_pdf

    def _cargar_pdfs_en_listview(self, items):

        self.modelListView.clear()

        for item in items:
            standard_item = QStandardItem(item)
            self.modelListView.appendRow(standard_item)

    def cargar_pdfs_en_listview(self):
        # Selecciona la carpeta
        self.folder_path = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta")
        self.folderPathLineEdit.setText(self.folder_path)

        # Obtiene los archivos pdfs de la carpeta seleccionada
        items = self.listar_archivos_pdf()

        # Añadir datos al modelo
        self._cargar_pdfs_en_listview(items)

    def load_pdf(self, file_path):
        if file_path:
            doc = fitz.open(file_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                image = QImage(
                    pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888
                )
                qt_image = QPixmap.fromImage(image)
                label = QLabel()
                label.setPixmap(qt_image)
                self.pdfImageViewScrollArea.setWidget(label)

    def update_rut_empleador(self):
        palette = self.rutEmpleadorEditText.palette()
        if self.rutEmpleadorEditText.hasAcceptableInput():
            self.rut_empleador = extraer_numeros(self.rutEmpleadorEditText.text())
            palette.setColor(QPalette.Text, QColor(Qt.black))
        else:
            palette.setColor(QPalette.Text, QColor(Qt.red))
        self.rutEmpleadorEditText.setPalette(palette)

    def update_date(self):
        self.event_date = self.fechaEventoDateEdit.date().toString("dd/MM/yyyy")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
