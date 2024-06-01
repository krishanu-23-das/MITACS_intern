# -*- coding: utf-8 -*-
"""htmlTemplates

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vX7lxKk4ixQ6lO857kCPG_cBmLTY07KP
"""

user_template = '''
    <div class="chat-message user" style="padding: 0.5rem; border-radius: 2rem; margin-bottom: 0.25rem; display: flex;">
        <div class="avatar">
            <img src="https://th.bing.com/th/id/OIP.7G6XwS4BzQWHQl-VoyvCFgHaHa?rs=1&pid=ImgDetMain" style="width: 60px; height: 60px;">
        </div>
        <div class="message" style="background-color: #FFFFFF;">
            {message}
        </div>
    </div>
    '''

bot_template = '''
    <div class="chat-message bot" style="padding: 1rem; border-radius: 2rem; margin-bottom: 0.25rem; display: flex;">
        <div class="avatar">
            <img src="https://th.bing.com/th/id/OIP.j21DfVny1Hush30Nvo-oGAHaHa?rs=1&pid=ImgDetMain" style="width: 60px; height: 60px;">
        </div>
        <div class="message" style="background-color: #FFFFFF;">
            {message}
        </div>
    </div>
    '''