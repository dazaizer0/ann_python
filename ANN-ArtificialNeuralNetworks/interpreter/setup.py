from cx_Freeze import setup, Executable

setup(
    name="ANN IDE",
    version="0.1.0",
    description="ann lang ide",
    executables=[Executable("IDE.py")],
)
