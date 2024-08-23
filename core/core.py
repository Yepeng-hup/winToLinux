import sys, os, time, shutil
from core import config

dates = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def FailLog(log_info):
    open_file = open(config.log_use_log, 'a')
    open_file.write(log_info)
    open_file.write('\n')
    open_file.close()
    sys.exit(1)

def SuccessLog(log_info):
    open_file = open(config.log_use_log, 'a')
    open_file.write(log_info)
    open_file.write('\n')
    open_file.close()

# def JudgeDir(path_dir):
#     if os.path.exists("/") == False:
#         os.mkdir(path_dir)
#     else:
#         SuccessLog(dates+" "+"function JudgeDir print: file and dir already exists!")

def DeleteFileDir(windows_path):
    del_list = os.listdir(windows_path)
    for f in del_list:
        file_dir_path = os.path.join(windows_path, f)
        try:
            if os.path.isfile(file_dir_path):
                os.remove(file_dir_path)
            elif os.path.isdir(file_dir_path):
                shutil.rmtree(file_dir_path)
        except:
            FailLog(dates+" "+"function DeleteFileDir print ERROR:delete is file and dir fail !!!")
