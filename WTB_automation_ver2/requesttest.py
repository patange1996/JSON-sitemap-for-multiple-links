'''
import requests

#v = input("URL:")
r = requests.get(
    "https://track.app.channeliq.com:443/api/wtb/redirect/8597af67-4f2a-4836-b8ae-1ec8fe402ec6/4?rurl=aHR0cDovL2dvLnJlZGlyZWN0aW5nYXQuY29tLz9pZD04MjA1MFgxNTMzNTU5JnhzPTEmdXJsPWh0dHBzJTNBJTJGJTJGd3d3LmNvc3Rjby5jb20lMkZwcmVtaWVyLTMwZy1wcm90ZWluLXNoYWtlcy0xMS1mbC4tb3ouJTI1MmMtMTgtcGFjay5wcm9kdWN0LjEwMDMwODcyNC5odG1sJnhjdXN0PTRjOTQyMmVlYmNmNDhmYWFmNGI3N2U3ZTExNjczZDJm&cpid=00000000-5c09-8328-a1df-aa11f0207e46&mpid=962ce664-0b4e-4a5d-a201-227acf8f60b3&osk=00000000-0000-0000-0000-000000000501&zp=&vs=",
    allow_redirects=True,
    headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
print(r.url)
'''
import json
from tkinter import *

def des():
    win.destroy()
def runfunction():
    start_urls = {}
    url = e.get(1.0, END)
    final_urls = url.split("\n")
    for i in final_urls:
        if i == "":
            final_urls.pop(final_urls.index(i))
    start_urls["startUrl"] = final_urls
    print(len(final_urls))
    with open('C:\\Users\\shubhan.patange\\Desktop\\python files\\JSON.txt', 'w') as file:
        file.write(json.dumps(start_urls))
    done_message = Label(win, text=f"Done {len(final_urls)} URL's ")
    done_message.grid(row=4, column=1)

    exit = Button(win, text="Exit", command=des)
    exit.grid(row=5, column=1)

win = Tk()
win.title("JSON Creator for multiple urls")

label = Label(win, text="Enter upto 10,000 URLS")
label.grid(row=0, column=0)

e = Text(win, width=100, height=25, borderwidth=5)
e.grid(row=0, column=1)

b = Button(win, text='create JSON', command=runfunction, borderwidth=5, width=10)
b.grid(row=2, column=1)

win.mainloop()

'''
import urllib3
import certifi

url_encoded = "https://track.app.channeliq.com:443/api/wtb/redirect/8597af67-4f2a-4836-b8ae-1ec8fe402ec6/4?rurl=aHR0cDovL2dvLnJlZGlyZWN0aW5nYXQuY29tLz9pZD04MjA1MFgxNTMzNTU5JnhzPTEmdXJsPWh0dHBzJTNBJTJGJTJGd3d3LmNvc3Rjby5jb20lMkZwcmVtaWVyLTMwZy1wcm90ZWluLXNoYWtlcy0xMS1mbC4tb3ouJTI1MmMtMTgtcGFjay5wcm9kdWN0LjEwMDMwODcyNC5odG1sJnhjdXN0PTRjOTQyMmVlYmNmNDhmYWFmNGI3N2U3ZTExNjczZDJm&amp;cpid=00000000-5c09-8328-a1df-aa11f0207e46&amp;mpid=962ce664-0b4e-4a5d-a201-227acf8f60b3&amp;osk=00000000-0000-0000-0000-000000000501&amp;zp=&amp;vs="
split = url_encoded.split("&")
decode =[]
print(split)
print("decode")
for i in split:
    c = i.replace("amp;","&")
    decode.append(c)
final =''.join(map(str, decode))
print(final)


http = urllib3.PoolManager(ca_certs=certifi.where())

url = final
try:
    resp = http.urlopen('GET', url)

except(urllib3.exceptions.MaxRetryError):
    print(resp.status)
'''