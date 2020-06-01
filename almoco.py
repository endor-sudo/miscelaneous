import PyPDF2
import re
import pprint

with open("/Users/iamthesenate/Desktop/Horário_TETPSI_CET_2020_Fevereiro_versao2.pdf",'rb') as pdf_object:
    pdf_lido = PyPDF2.PdfFileReader(pdf_object)
    page_object=pdf_lido.getPage(0)
    text=page_object.extractText()

dia_mes = re.compile(r'\d/fev|\d\d/fev|\d/mar|\d\d/mar')
matches=dia_mes.findall(text)
print(matches)

text_clean=text.replace('\n','-')

print(text_clean)