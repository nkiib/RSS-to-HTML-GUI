import PySimpleGUI as sg

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
radio_dic = {
    '-1-' : 'HTML',
    '-2-' : 'テキストファイル',
    '-3-' : 'CSV形式',
    '-4-' : 'XML形式'
}

layout = [  [sg.Text('RSSからHTMLを出力するジェネレーター')],
            [sg.Text('RSS URL'), sg.InputText()],
            [sg.Text('ファイル名'), sg.InputText()],
            [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_dic.items()],
            [sg.Button('OK'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('Tlooks RSS to file', layout,font=('Arial',20))

# イベントループ
def output(values, write1, str1 ,filetype):
    path1 = os.path.dirname(__file__) + "/" 
    file1 = path1 + values[1] + filetype
    write1( file1, str1 ) 
    print(values)
    print(path1 + ' に '+ values[1]+ filetype + ' を出力')

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0

def time_split(date):
    timex = date.split("T")
    print(timex)
    return timex     

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK': 
        import os
        import feedparser
                
        rssurl= values[0]
        d = feedparser.parse(rssurl)
        outx = ""

        if 'title' not in d.feed:
            print('このURLはRSSフィードのものではありません。最初からやり直してください') 
            import sys
            sys.exit()            

        if values['-1-'] == True: ## HTML
            filetype = ".html"
            for entry in d['entries']:
                outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
                timey = time_split(entry.published)
                outx += timey[1] + "<br><br>"

            str1 = '''
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>{title1}</title>
                </head>
                <body>
                    {body1} 
                </body>
            </html>'''.format( title1 = "output", body1 = outx ) 
        
            output(values, write1, str1 ,filetype) # 出力
        

        elif values['-2-']== True: # TXT
            filetype = ".txt"
            for entry in d['entries']:
                outx += entry.title + '\n' + 'link : '+ entry.link + '\n' 
                outx += entry.published + '\n' + '\n'

            str1 = '''{body1}'''.format( title1 = "output", body1 = outx ) 
            output(values, write1, str1 ,filetype)
        

        elif values['-3-'] == True: # CSV
            filetype= ".csv"
            outx += 'タイトル,日付,リンク' + '\n'
            for entry in d['entries']:
                outx += entry.title + ',' + entry.published + ',' + entry.link + '\n'

            str1 = '''{body1}'''.format(body1 = outx)
            output(values,write1,str1,filetype)
        
        elif values['-4-'] == True: # XML
            print('-4-に到達')
            print(values) # 未実装

window.close() # ウィンドウを閉じる（ただし、キャンセル時）