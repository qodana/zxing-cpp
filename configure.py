#!/usr/bin/env python3
import shutil
import subprocess as sp
from pathlib import Path

shutil.copy2("CMakeLists.txt.disabled", "CMakeLists.txt")
sp.run(["cmake", "--preset", "default"], check=True)
Path("CMakeLists.txt").unlink()
Path("build/compile_commands.json").rename("compile_commands.json")
Path("build/CMakeCache.txt").unlink()
