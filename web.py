import shutil
from pyrogram import Client,filters
import requests,os
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")

@app.on_message((filters.me) & filters.regex("!down "))
def gif(client,message):
    text=message.text    
    message_id=message.message_id
    chat_id=message.chat.id
    url=text[6:]
    file_name=os.path.basename(url)
    response=requests.get(url)
    size=int(response.headers["content-length"])/1024/1024
    size=str(size)[:5]
    x=len(url)
    client.edit_message_text(chat_id,message_id,"downloding...")
    with open(file_name,"wb") as f:
        shutil.copyfileobj(response.raw,f)
    client.edit_message_text(chat_id,message_id,"downloding complate\n\nuploading now...")
    client.send_document(chat_id,file_name,caption=f"\n**NAME:** {file_name}\n**SAIZE:** {size} MB")
    del response

app.run()
