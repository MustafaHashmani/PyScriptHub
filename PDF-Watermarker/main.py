import PyPDF2

template = PyPDF2.PdfReader(open("PDF/super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("PDF/wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

# loop through the number of pages in the template and merge with watermark
for i in range(len(template.pages)):
    page = template.pages[i]  # get each page in the template
    page.merge_page(watermark.pages[0])  # merge with watermark
    output.add_page(page)  # add merged page in output

    # save the output object in a file
    with open("watermarked_output.pdf", "wb") as file:
        output.write(file)
