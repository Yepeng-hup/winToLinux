import yaml
import os
import traceback
import sys

yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.yaml")


def read_yaml():
    try:
        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except:
        print(traceback.format_exc())
        sys.exit(1)
y = read_yaml()

_win = y.get("win")
win_src_path = _win.get("mv_data_src_path")
win_data_tmp = _win.get("win_data_tmp")

_linux = y.get("linux")
linux_use_key = _linux.get("use_key")
linux_ssh_host = _linux.get("ssh_host")
linux_ssh_port = _linux.get("ssh_port")
linux_ssh_user = _linux.get("ssh_user")
linux_ssh_passwd = _linux.get("ssh_passwd")
linux_ssh_key_path = _linux.get("ssh_key_path")
linux_mv_data_dest_path = _linux.get("mv_data_dest_path")

_log = y.get("log")
log_use_log = _log.get("use_log")