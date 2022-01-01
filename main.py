import PySimpleGUI as sg

sg.theme('DarkAmber')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('RSSからHTMLを出力するジェネレーター')],
            [sg.Text('RSS URL'), sg.InputText()],
            [sg.Text('ファイル名'), sg.InputText()],
            [sg.Button('OK'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('サンプルプログラム', layout,font=('Arial',20))

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK':
        import os
        import feedparser
        import datetime
        
        rssurl= values[0]
        d = feedparser.parse(rssurl)
        outx = ""

        for entry in d['entries']:
            outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
            outx += entry.published + "<br><br>"

        def write1( file1, str1 ): 
            with open( file1, 'w', encoding='utf-8' ) as f1: 
                f1.write( str1 ) 
            return 0 

        

        str1 = '''
        <html>
        <head>
        <meta charset="utf-8">
        <title>{title1}</title>
        </head>
        <body>
        {body1} 
        </body>
        </html>
        '''.format( title1 = "output", body1 = outx ) 

        print( str1 ) 

        path1 = os.path.dirname(__file__) + "/" 
        file1 = path1 + values[1] + ".html"
        write1( file1, str1 ) 

window.close()