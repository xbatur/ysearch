from bs4 import BeautifulSoup
import requests
import os

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PINK = '\033[95m'
class PlayR:
    def __init__(self):
        self.list_url = []
        self.list_names = []
        
        
    def get_track(self,num):
        strname = self.list_names[num]
        strnamen = strname.replace(" ","\ ")
        strnamen2 = strnamen.replace("(","x")
        strnamen3 = strnamen2.replace(")","x")
        strnamen3 = strnamen3.replace("|","x")
        strnamen3 = strnamen3.replace("{","x")
        strnamen3 = strnamen3.replace("}","x")
        strnamen3 = strnamen3.replace(";","x")
        strnamen3 = strnamen3.replace("&","x")
        cmd = 'youtube-dl --extract-audio --audio-format mp3 -o'+' "%(autonumber)s.%(ext)s"'+" https://www.youtube.com"+self.list_url[num]
        print(colors.PINK)
        os.system(cmd)
        print(colors.ENDC)
        os.system("mv 00001.mp3 "+strnamen3+".mp3")
    def search(self,query):
        r = requests.get("https://www.youtube.com/results?search_query="+query)
        x = r.content.decode("utf-8")
        link_n = 0
        link_f = 0
        title_z = 0
        title_f = 0
        while(1):
            link_n = x.find('<a href="/watch?',link_n)
            if (link_n == -1):
                break
            link_f = x.find('"',link_n+9)
            title_z = x.find('title="',link_n+9)
            title_f = x.find('"',title_z+7)
            self.list_url.append(x[link_n+9:link_f])
            self.list_names.append(x[title_z+7:title_f])
            print("TRACK NAME: "+colors.FAIL+self.list_names[len(self.list_names)-1]+colors.ENDC)
            print(colors.BOLD+colors.OKBLUE+"["+str(len(self.list_url)-1)+"]"+colors.ENDC+" URL = "+colors.WARNING+"www.youtube.com"+self.list_url[len(self.list_url)-1]+colors.ENDC)
            link_n += 9
                                   
def main():
    inp = ""
    q = ""
    play = PlayR()
    col = colors()
    print("please use q for quit")
    q = input(colors.OKGREEN+"search..> "+colors.ENDC)
    q.replace(" ","+")
    if(q.lower() == 'q'):
        exit(0)
    play.search(q)
    try:
        inp = input(colors.HEADER+"track num> "+colors.ENDC)
        if (inp.lower() == 'q'):
            exit(0)
    except KeyboardInterrupt:
        del play.list_url[:]
        del play.list_names[:]
        print("")
        main()
    if(inp.isdigit()):
        inp_i = int(inp)
        if(inp_i > -1 and inp_i < len(play.list_url)):
                play.get_track(inp_i)
    
main()
