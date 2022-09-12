from asyncio import Lock
from shutil import get_unpack_formats
import threading
import time
lock = threading.Lock()
lock  = threading.Lock()
def show_info(name,age):
    print(name,'is',age)
def task1():
    lock.acquire()
    for i in range(1000000):
        global gum
        gum = gum+1
    print("task1:",gum)






if __name__ == '__main__':  
    # sub_thread  = threading.Thread(target=show_info,kwargs={'name':'mojiajian', 'age':'18'})
    # sub_thread.start()
    #
    sub_thread = threading.Thread(target=task1)
    sub_thread.start()
   