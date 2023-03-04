import os
from PyPDF2 import PdfMerger
PdfFiles =  os.listdir("PdfMerger")
print(PdfFiles)

# x = [i for i in PdfFiles if i.endswith(".pdf")]
# print(x)

# merger = PdfMerger()

# for pdf in x: 
#     merger.append(pdf)
#     # print(pdf)

# merger.write("CodeWithHarryExercise/PdfMerger/Result.pdf")
# merger.close()

