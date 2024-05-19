import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images')
fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fonts')
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
#if os.path.exists(libdir):
#    sys.path.append(libdir)

import logging
from modules.eink import epd4in2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from utilities import OSUtils


osutils = OSUtils.OSUtils()

def draw_bitmap(draw, image, x, y):
    draw.bitmap((x, y), Image.open(os.path.join(picdir, image)), fill=0)

def draw_header(draw, title):
    draw.rectangle((0, 0, 400, 30), fill = 0)
    draw.text((10, 10), title, font = font24, fill = 255)

def footer(draw, page, total_pages):
    draw.rectangle((0, 270, 400, 300), fill = 0)
    #Arrow left
    draw.rounded_rectangle((7, 274, 47, 296), fill = 255, radius=10)
    draw.polygon([(10,285),(40,275),(40,295),(10,285)], fill = 0)
    #Arrow right
    draw.rounded_rectangle((354, 274, 393, 296), fill = 255, radius=10)
    draw.polygon([(390,285),(360,275),(360,295),(390,285)], fill = 0)
    #Debug Button
    draw.rounded_rectangle((260, 274, 334, 296), fill = 255, radius=10)
    draw.text((264, 278), 'Debug', font = font24, fill = 0)
    #Home Button
    draw.rounded_rectangle((67, 274, 127, 296), fill = 255, radius=10)
    draw.text((72, 278), 'Home', font = font24, fill = 0)
    #Page mumber
    draw.text((180, 280), str(page)+'/'+str(total_pages), font = font24, fill = 255)
#Image size is ~80PX max width and ~220PX max height
#Max Text is 12 lines
def draw_body_with_image(draw, image, x, y, texts):
    draw_bitmap(draw, image, x, y)
    index = 0
    for text in texts:
        draw.text((x+80, y+(index*20)), text, font = font18, fill = 0)
        index += 1
def draw_body(draw, x, y, texts):
    index = 0
    for text in texts:
        draw.text((x, y+(index*20)), text, font = font18, fill = 0)
        index += 1


logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd4in2 Demo")
    
    epd = epd4in2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font24 = ImageFont.truetype(os.path.join(fontdir, 'WhiteRabbit.ttf'), 24)
    font18 = ImageFont.truetype(os.path.join(fontdir, 'WhiteRabbit.ttf'), 18)
    font35 = ImageFont.truetype(os.path.join(fontdir, 'WhiteRabbit.ttf'), 35)
    indexx = 0
    index_max = 3

    while True:
    # test Debug draw
        Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage2)
        data = []
        if indexx == 0:
            draw_header(draw,'Debug: System information')
            data.append('Distro: '+osutils.get_distribution())
            data.append('Hostname: '+osutils.get_hostname())
            data.append('IP:'+osutils.get_ip_address())
            data.append('CPU:'+osutils.get_cpu_information())
            data.append('Memory: '+osutils.get_memory())
            data.append('Temperature: '+str(osutils.get_cpu_temperature())+'C')
            data.append('Uptime: '+osutils.get_uptime())
            data.append('SSH: '+osutils.get_service_status('sshd'))
            data.append('Postgre: '+osutils.get_service_status('postgresql'))
            draw_body_with_image(draw, 'Raspberry_Pi-Logo.wine.bmp', 0, 40, data)
            footer(draw,indexx+1,index_max)
        elif indexx == 1:
            draw_header(draw,'Debug: System information')
            data.append('Main  Yuuka Program     : Offline')
            data.append('Yuuka Sub systems:')
            data.append('Plant Data Logging      : Offline')
            data.append('Plant Control           : Offline')
            data.append('Plant Analysis System   : Offline')
            data.append('Database Interface      : Offline')
            data.append('Arduino Interface       : Offline')
            data.append('External Debuging screen: Offline')
            data.append('Web Sub Systems:')
            data.append('Web Yuuka Web Interface : Offline')
            data.append('Web Yuuka Plant API     : Offline')
            draw_body(draw, 0, 40, data)
            footer(draw,indexx+1,index_max)
        elif indexx == 2:
            draw_header(draw,'Debug: System information')
            data.append('Data 8Bit IO        : 0X00')
            data.append('Data 8Bit Shift     : 0X00')
            data.append('Data Light          : OFF')
            data.append('Data External Pump  : OFF')
            data.append('Data Window A       : Closed')
            data.append('Data Window B       : Closed')
            data.append('Info Temp Address   : 0X5C')
            data.append('Info 8Bit IO Addr   : 0X20')
            data.append('Info Window A GPIO  : 20,21')
            data.append('Info Window A GPIO  : 22,23')
            data.append('Info Button Controls: 24,25,26,27')
            data.append('Info 8Bit Shhit GPIO: 28,29,30')
            draw_body(draw, 0, 40, data)
            footer(draw,indexx+1,index_max)
        if indexx > index_max:
            break
        epd.display(epd.getbuffer(Himage2))
        indexx += 1    
        time.sleep(20)

    #Himage4 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    #draw3 = ImageDraw.Draw(Himage4)
    #footer(draw3,3,3)
    #epd.display(epd.getbuffer(Himage4))  
    #epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd4in2.epdconfig.module_exit(cleanup=True)
    exit()
