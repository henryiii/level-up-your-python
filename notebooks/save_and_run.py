from IPython.core.magic import Magics, magics_class, cell_magic

import sys
import subprocess


@magics_class
class AutoMagics(Magics):
    @cell_magic
    def save_and_run(self, line, cell, local_ns=None):
        commands = line.split()
        filename = "tmp.py"
        with open(filename, "w") as f:
            f.write(cell)

        subprocess.run(
            [sys.executable, "-m", *commands, filename],
            env={"FORCE_COLOR": "1", "MYPY_FORCE_COLOR": "1", "TERM": "xterm-color"},
        )


# Why sys.executable here?
#
# We are running inside a virtual environment, which also has mypy installed. However, this is a shell command (the starting `!`), so it will not  necessarily run in the same environment. So we'll use the current python interpreter `sys.executable` and use the `python -m mypy` expression  instead of plain `mypy` to make sure we get our installed MyPy. You don't usually run mypy from a notebook.


def load_ipython_extension(ipython):
    ipython.register_magics(AutoMagics)
