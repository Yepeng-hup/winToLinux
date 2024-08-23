import time, os
from core import core, config


def FilePush(win_src_path):
    time_start=time.time()
    for i in win_src_path:
        os.system("xcopy"+" "+i+" "+config.win_data_tmp+" /e")
    if config.linux_use_key:
        err = os.system(f"pscp -r -P {config.linux_ssh_port} -i {config.linux_ssh_key_path} {config.win_data_tmp} {config.linux_ssh_user}@{config.linux_ssh_host}:{config.linux_mv_data_dest_path}")
        if err != 0 :
            core.DeleteFileDir(config.win_data_tmp)
            core.FailLog(core.dates+" "+'ERROR: key function FilePush technical documentation data cp to Linux fail.')
        else:
            core.SuccessLog(core.dates+" "+'INFO: key function FilePush technical documentation data cp to Linux successful.')
    else:
        err = os.system(f"pscp -r -P {config.linux_ssh_port} -pw {config.linux_ssh_passwd} {config.win_data_tmp} {config.linux_ssh_user}@{config.linux_ssh_host}:{config.linux_mv_data_dest_path}")
        if err != 0 :
            core.DeleteFileDir(config.win_data_tmp)
            core.FailLog(core.dates+" "+'ERROR: passwd function FilePush technical documentation data cp to aliyun fail.')
        else:
            core.SuccessLog(core.dates+" "+'INFO: passwd function FilePush technical documentation data cp to Linux successful.')
    time_end=time.time()
    code_run_time = time_end-time_start
    core.SuccessLog(core.dates+" "+"code is runtime: {time}s".format(time=code_run_time))
    core.DeleteFileDir(config.win_data_tmp)

if __name__ == "__main__":
    FilePush(config.win_src_path)