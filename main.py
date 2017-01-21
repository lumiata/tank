from campi.bot import CamPi
import os

if __name__ == '__main__':
    campi = CamPi(os.environ["READ_FROM_CHANNEL"])
    campi.run()
