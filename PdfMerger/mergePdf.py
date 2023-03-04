# import os
# # import PyPDF2 as pdf
# from PyPDF2 import PdfWriter

# # source_dir = os.getcwd()
# merger = PdfWriter()

# for item in ["a.pdf","b.pdf"]:
#     # if item.endswith('.pdf'):
#     merger.append(item)

# merger.write('completed_file.pdf')
# merger.close()

from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["a.pdf", "b.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()