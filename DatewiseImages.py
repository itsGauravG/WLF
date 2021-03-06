import time

import pywikibot
from pywikibot import pagegenerators
from datetime import date
import datetime


def main(year,month,d,m_num):

    site = pywikibot.Site(fam='commons', code='commons')
    site.throttle.setDelays(10)
    cat = pywikibot.Category(site,'Category:Images from Wiki Loves Folklore 2022')
    date = datetime.date(int(year),int(m_num),int(d))

    #page_name = pywikibot.Page(site, "User:Rockpeterson/WLF/+"+str(a_date)+"-Feb-2022")
    page_name = pywikibot.Page(site, "User:Rockpeterson/WLF/"+str(d)+"-"+str(month)+"-"+
    str(year))
    gen = pagegenerators.CategorizedPageGenerator(cat)

    pages= [page for page in gen if page.is_filepage() and page.oldest_file_info['timestamp'].date() == date]

    temp = "<b>Total Images</b> : "+ str(len(pages))
    temp +="<gallery>"

    for img in pages:
        img = str(img)
        text = img[10:len(img)-2]
        temp+='\n'
        temp= temp+text+'|'+img[15:len(img)-6]

    temp+="</gallery>"



    #print(temp)
    #print(page_name)

    page_name.text = temp
    page_name.save('Creating or updating daily gallery for WLF 2022')
    time.sleep(10)
    page_datewise = pywikibot.Page(site,"User:Rockpeterson/WLF/Datewise")

    page_txt = page_datewise.text
    ls = page_txt.split("</br>")
    print(ls)
    new_ls=[]
    for link in ls:
        new_ls.append(link[2:len(link)-2])
    print(new_ls)
    print(page_name)

    buff = str(page_name)
    buff= buff[10:len(buff)-2]

    if buff in new_ls:
        return
    page_datewise_text =""
    for link in ls:
        page_datewise_text= page_datewise_text+link+"</br>"

    page_datewise_text=page_datewise_text+"[["+buff+"]]"

    page_datewise.text=page_datewise_text
    page_datewise.save("ok")
    

if __name__ == '__main__':


    while(1):
        #t = date.today()
        year = datetime.date.today().strftime("%Y")
        month = datetime.date.today().strftime("%b")
        date = datetime.date.today().strftime("%d")
        m_num = datetime.date.today().strftime("%m")
        main(year,month,date,m_num)
        time.sleep(10)

    #day = list(range(1,32))
    #print(day)
    #for a_date in day:
       #main(a_date)


#<div style="text-align: center;">Flaming Fellowship</div>
