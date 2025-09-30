from cx_Freeze import setup, Executable
import sys

# 基础设置
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# 构建选项
build_exe_options = {
    "packages": ["PyQt5"],
    "excludes": ["PyQt5.QtQml", "PyQt5.QtQuick"],  # 排除QML相关模块
    "include_files": []
}

# 设置
setup(
    name="表格转换工具",
    version="1.0",
    description="表格转换工具",
    options={"build_exe": build_exe_options},
    executables=[Executable("table_converter.py", base=base)]
)
