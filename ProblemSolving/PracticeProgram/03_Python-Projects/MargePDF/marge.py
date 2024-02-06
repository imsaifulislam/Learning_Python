from PyPDF2 import PdfFileMerger
import os

# Create an instance of pdfFileMerger() class
merger = PdfFileMerger()

# pdf_files = ['./pdfFile/sample_page1.pdf',
#              './pdfFile/sample_page2.pdf', './pdfFile/sample_page3.pdf']

path_to_files = r"../MargePDF/pdfFile/"

# for pdf_file in pdf_files:
#     merger.appedn(pdf_file)

for root, dirs, file_names in os.walk(path_to_files):
    for file_name in file_names:
        merger.append(path_to_files+file_name)


merger.write("Merged_3Pages.pdf")
merger.close()