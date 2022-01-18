from pyrogram import Client,filters
import requests,os
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")

@app.on_message((filters.me) & filters.regex("!down "))
def gif(client,message):
    text=message.text    
    message_id=message.message_id
    chat_id=message.chat.id
    url=text[6:]
    response=requests.get(url)
    size=int(response.headers["content-length"])/1024/1024
    size=str(size)[:5]
    x=len(url)
    m=url[x-4:]
    if m[0]!='.':
        m=url[x-5:]
    client.edit_message_text(chat_id,message_id,"downloding...")
    with open(f"@REZABZ2{m}","wb") as f:
        f.write(response.content)
    client.edit_message_text(chat_id,message_id,"downloding complate\n\nuploading now...")
    client.send_document(chat_id,f"@REZABZ2{m}",caption=f"\n**NAME:** @REZABZ2{m}\n**SAIZE:** {size} MB")
    os.remove(f"@REZABZ2{m}")

app.run()
