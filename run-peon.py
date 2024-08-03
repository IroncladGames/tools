"""
Script to make running Peon more convienent.
"""

import os
import argparse
import subprocess

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
OUT_FOLDER = os.path.join(CURRENT_PATH, r".out")
PEON_FOLDER = os.path.join(CURRENT_PATH, r"Peon")
PEON_EXE_PATH = os.path.join(PEON_FOLDER, "bin", r"Peon.exe")
CONFIG_FOLDER = PEON_FOLDER

def run_peon(verb, src_folder, dst_folder, texconv_exe_path, fxc_exe_path):
    if not os.path.exists(PEON_EXE_PATH):
        raise Exception(f"{PEON_EXE_PATH} does not exist")
    
    command_line = f"{PEON_EXE_PATH} {verb} -s {src_folder} -d {dst_folder} -c {CONFIG_FOLDER} -w {OUT_FOLDER} --package-mod --delete-unknown"
    if texconv_exe_path:
        command_line += f" --texconv-exe-path {texconv_exe_path}"
    if fxc_exe_path:
        command_line += f" --fxc-exe-path {fxc_exe_path}"
    print("\n{} (cwd={})\n".format(command_line, CURRENT_PATH))
    subprocess.call(command_line, cwd=CURRENT_PATH)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src_folder", required=True)
    parser.add_argument("-d", "--dst_folder", required=True)
    parser.add_argument("-t", "--texconv_exe_path", default="", required=False)
    parser.add_argument("-f", "--fxc_exe_path", default="", required=False)
    args = parser.parse_args()

    run_peon(
        "build",
        args.src_folder,
        args.dst_folder,
        args.texconv_exe_path,
        args.fxc_exe_path
    )
