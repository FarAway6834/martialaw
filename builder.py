#!/usr/bin/python3 python

from sys import argv as _a
from subprocess import run as _r
import yes_and_no
from option import pip_update, with_update, only_update

'''
# builder.py

# ===== [ ITEMS ] ===== #
#  ==== [ FUNCS ] ====  #
    - shell (read docs plz (well... as like; for ex.. using help() function or.. just using functions __doc__ attribute... any way...)
#  ==== [ DATAS ] ====  #
    s = shell
'''

def shell(x : str) -> any:
  '''
  # `shell(your os terminal cmd : str) -> any` execute terminal code.
  by subprocess.run(x, shell=True) (read python's docs plz)
  '''
  return _r(x, shell=True)

s = shell

def pip_installer(x, must_do_pip_update = pip_update, with_update = with_update, only_update = only_update, __updatecmd__ = False):
  if must_do_pip_update: pip_installer('pip', must_do_pip_update = False, with_update = False, only_update = False, __update_cmd__ = True)
  elif __updatecmd__: pip_installer(f'--upgrade {x}', must_do_pip_update = must_do_pip_update, with_update = with_update, only_update = only_update)
  if only_update: pip_installer(x, must_do_pip_update = must_do_pip_update, with_update = with_update, only_update = False, __update_cmd__ = True)
  elif with_update: (pip_installer(must_do_pip_update = must_do_pip_update, with_update = False, only_update = False), pip_installer(x, must_do_pip_update = must_do_pip_update, with_update = False, only_update = True))
  else:
