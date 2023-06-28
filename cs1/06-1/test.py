#問題: Webブラウザで検索しよう

import webbrowser

def google(s):
    
    webbrowser.open('http://www.google.com/search?q=' + s)


google('python')