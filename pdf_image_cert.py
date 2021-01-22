import fpdf
import datetime

nameList = ["Mary", "John", "Betty"]

for name in nameList:
    
    #create a new pdf
    document = fpdf.FPDF(orientation = 'L', unit = 'mm', format='A4')
    
    #define font and color for title and add the first page
    document.set_font("Times","B", 14)
    document.set_text_color(19,83,173)
    document.add_page()
    
    #add a image
    document.image("medal.jpg", x=130, y=70, w=50)
    document.rect(10, 10, 280, 180, 'D');
    document.set_y(40)
    
    #write the title of the document
    document.set_font("Times", "B", 40)
    document.cell(0,5,"Certificate of Good Behaviour", align="C")
    document.ln()
    document.ln()
    document.ln()
    #write a long paragraph
    document.set_xy(20, 150)
    
    document.set_font("Times", "I", 22)
    document.set_text_color(0)
    document.multi_cell(0,5, "This award is presented to "+name+" for displaying good conduct.")
    document.ln()
    document.set_xy(20, 170)
    
    #date
    document.set_font("Times", "", 12)
    document.set_text_color(0)
    dated = "Dated: "+str(datetime.datetime.now().strftime("%d-%B-%y"))
    
    document.multi_cell(0,5, dated)
    
    
    #save the document
    document.output("pdf_image_cert_"+name+".pdf")
print("Done")