import PySimpleGUI as sg

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
radio_dic = {
    '-1-' : 'HTML',
    '-2-' : 'テキストファイル',
    '-3-' : 'CSV形式',
}

layout = [  [sg.Text('RSSからHTMLを出力するジェネレーター')],
            [sg.Text('RSS URL'), sg.InputText()],
            [sg.Text('ファイル名'), sg.InputText()],
            [sg.Radio(item[1], key=item[0], group_id='0') for item in radio_dic.items()],
            [sg.Button('OK'), sg.Button('終了')] ]

# ウィンドウの生成
window = sg.Window('Tlooks RSS to file', layout,font=('Arial',20))

# 処理
def output(str1 ,filetype): # 出力処理
    path1 = os.path.dirname(__file__) + "/" 
    file1 = path1 + values[1] + filetype
    write1( file1, str1 ) 
    print(values)
    print(path1 + ' に '+ values[1]+ filetype + ' を出力')

def write1( file1, str1 ): # ファイルの編集処理
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0

def time_split(date): # 時間の修正処理
    timex = date.split("T")
    timex2 = timex[1].split("+")
    datex = timex[0].split("-")
    publish = datex[0] + "/" + datex[1] + "/" + datex[2] + " " + timex2[0]
    return publish     

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '終了':
        break
    elif event == 'OK': 
        import os
        import feedparser

        # 変数の用意        
        rssurl= values[0] # URLの取得
        d = feedparser.parse(rssurl) # URLからRSSを取得
        outx = ""

        # RSSフィードの有効性の確認
        if 'title' not in d.feed:
            print('このURLはRSSフィードのものではありません。最初からやり直してください') 
            import sys
            sys.exit()

        # 実際の処理部分
        if values['-1-'] == True: ## HTML
            filetype = ".html"
            tt = d.feed.title
            for entry in d['entries']:
                outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
                outx += time_split(entry.published) + "<br><br>"
                

            # 出力用の記述
            str1 = '''
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>{title1}</title>
                </head>
                <body>
                    <h1>{title2}</h1>
                    {body1} 
                </body>
            </html>'''.format( title1 = "output", title2 = tt , body1 = outx ) 
        
            output( str1 ,filetype) # 出力
        

        elif values['-2-']== True: # TXT
            filetype = ".txt"
            for entry in d['entries']:
                outx += entry.title + '\n' + 'link : '+ entry.link + '\n' 
                outx += time_split(entry.published) + '\n' + '\n'

            str1 = '''{body1}'''.format( title1 = "output", body1 = outx ) 

            output( str1 ,filetype)
        

        elif values['-3-'] == True: # CSV
            filetype= ".csv"
            outx += 'タイトル,日付,時間,リンク' + '\n'
            for entry in d['entries']:
                date = time_split(entry.published).split(" ")
                outx += entry.title + ',' + date[0] + ',' + date[1] + ',' + entry.link + '\n'

            str1 = '''{body1}'''.format(body1 = outx)
            output(str1,filetype)


window.close() # ウィンドウを閉じる（ただし、キャンセル時）