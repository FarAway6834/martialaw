#!/usr/bin/python3 python

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
    '''
    # `pip_installer`

    yes. it will makes you yell "Bloody Hell!!"
    it fucking disgusting.
    well. use pyenv.
    '''
    if must_do_pip_update: pip_installer('pip', must_do_pip_update = False, with_update = False, only_update = False, __update_cmd__ = True)
    elif __updatecmd__: return pip_installer(f'--upgrade {x}', must_do_pip_update = False, with_update = with_update, only_update = only_update)
    if only_update: return pip_installer(x, must_do_pip_update = False, with_update = with_update, only_update = False, __update_cmd__ = True)
    elif with_update: return (pip_installer(must_do_pip_update = False, with_update = False, only_update = False), pip_installer(x, must_do_pip_update = False, with_update = False, only_update = True))
    else: return s(f'pip install {x}')

def depens_getting_state(x):
    try: return __import__(x)
    except: return pip_installer(x)

def building():
    return (depends_getting_states('setuptools'), depends_getting_states('wheel'), s('python setup.py sdist bdist_wheel'))

main = building

#SUcK!!!!!!!!!!!!!!!FUCK!!

if __name__ == "__main__": main()
