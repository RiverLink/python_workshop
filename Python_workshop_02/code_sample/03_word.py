from docx.shared import Inches
from docx import Document

pic_data = './Python_workshop_02/code_sample/sample_graph.png'

docx_file = './Python_workshop_02/code_sample/sample_word.docx'

document = Document()

document.add_picture(pic_data, width=Inches(3.6))

document.save(docx_file)
