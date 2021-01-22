'''
need to create test_papers folder to place the downloaded files
'''

import requests
import time

schools = ["Raffles", "Nanyang", "ACS", "Henry_Park", "Red_Swastika", "Rosyth", "SCGS", "Tao_Nan"]
exam = "SA2"
subject = ["Chinese", "English", "Maths", "HChinese", "Science"]
year = 2020
level = 6

#https://www.testpapersfree.com/pdfs/P6_HChinese_SA2_2020_Raffles_Exam_Papers.pdf
#https://www.testpapersfree.com/pdfs/P6_English_SA2_2020_Nanyang_Exam_Papers.pdf

for school in schools:
    for subj in subject:
        filename = "P"+str(level)+"_"+subj+"_"+exam+"_"+str(year)+"_"+school+"_Exam_Papers.pdf"
        try:
            url = 'https://www.testpapersfree.com/pdfs/'+filename
            print(url)
            r = requests.get(url, stream=True)
            chunk_size = 2048
            
            #folder to save in: test_papers, need to change accordingly. 
            # folder has to be created beforehand
            with open("test_papers/"+filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size):
                    fd.write(chunk)
            
            print("Done:"+filename)
        except Exception as e:
            print("Exception " ,type(e), ": ", e.args)
        time.sleep(10) 
        #delay after each round, please set at least 10sec or you will risk crashing their server and get into trouble :p
