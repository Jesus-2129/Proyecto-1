from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
from os import system, scandir, environ
from shutil import move
from PIL import Image, ImageDraw, ImageFont
import datetime

from PIL import Image, ImageDraw, ImageFont
import datetime
def name_image(original_image, author, im_height=800, im_width=600):
    image = Image.open(original_image)
    image = image.resize((im_height, im_width))
    image_name = original_image.split("/")[-1]
    move(original_image, f'./designs_library/source/{image_name}')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=16)
    designer_name = author
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # starting position of the message
    (x, y) = (int(image.size[0]*0.35), int(image.size[1]*0.95))
    message = f"{designer_name} - {date}"
    color = 'rgb(255, 255, 255)'
   
    # draw the message on the background
    draw.text((x, y), message, fill=color, font=font)
    
    # save the edited image
    return image.save(f'./designs_library/converted/{image_name}')    

# @shared_task
def conversion_design():
    from .models import Design
    processing_path_videos = 'designs_library/processing'
    converted_path_videos = 'designs_library/converted'
    source_path_video = 'designs_library/source'
    files = [obj.name for obj in scandir(processing_path_videos) if obj.is_file()]

    if len( files ) > 0:
        for file in files:
            design = Design.objects.get( pk = file.split('.')[0] )
            name_image(f'./designs_library/processing/{file}', design.designer_first_name)
            design.design_status = 'CONVERTED'
            design.save()
            print ("\n *** Diseño: {} Convertido! ***\n".format(file))
        response = "Diseños Convertidos!"

    else:
        response = "No hay videos para convertir!"

    return response