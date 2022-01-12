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

        if values['-1-'] == True: ## HTML
            
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

            #print( str1 ) 

            path1 = os.path.dirname(__file__) + "/" 
            file1 = path1 + values[1] + ".html"
            write1( file1, str1 ) 
            print(values)

        elif values==['-2-']: # TXT
            """for entry in d['entries']:
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

            #print( str1 ) 

            path1 = os.path.dirname(__file__) + "/" 
            file1 = path1 + values[1] + ".html"
            write1( file1, str1 ) 
            print(values)"""
        print('-2-に到達')
    elif values['-3-'] == True:
        print('-3-に到達')
    elif values['-4-'] == True:
        print('-4-に到達')


        
window.close()