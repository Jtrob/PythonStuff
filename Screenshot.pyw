###This was created to test the pyscreenshot library
###Libraries  
import pyscreenshot, datetime
###Main action
if __name__ == "__main__":
    im=pyscreenshot.grab()
    im.save('screenshot{:%Y-%m-%d}.png'.format(datetime.datetime.now()))
    im.show()
