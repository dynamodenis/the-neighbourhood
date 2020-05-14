import secrets
from PIL import Image
import os
from flask import current_app
def save_picture(data):
    secret_hex=secrets.token_hex(6)
    _,f_exe=os.path.splitext(data.filename)
    pic_path=secret_hex+f_exe
    pic_dir=os.path.join(current_app.root_path+'/static/profile/'+pic_path)
    # data.save(pic_dir)

    size=(400,400)
    pic_size=Image.open(data)
    pic_size.thumbnail(size)
    pic_size.save(pic_dir)

    
    return pic_path

def post_image(data):
    random_hex=secrets.token_hex(5)
    _,f_exe=os.path.splitext(data.filename)
    pic_name=random_hex+f_exe
    pic_url=os.path.join(current_app.root_path+'/static/images/'+pic_name)

    size=(400,400)
    size_cut=Image.open(data)
    size_cut.thumbnail(size)
    size_cut.save(pic_url)

    return pic_name