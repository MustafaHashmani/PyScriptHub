import PyPDF2
import sys

pdfs = sys.argv[1:]  # get all files to merge


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")


pdf_merger(pdfs)
