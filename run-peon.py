"""
Script to make running Peon more convienent.
"""

import os
import argparse
import subprocess
import shlex

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
OUT_FOLDER = os.path.join(CURRENT_PATH, r".out")
PEON_FOLDER = os.path.join(CURRENT_PATH, r"Peon")
PEON_EXE_PATH = os.path.join(PEON_FOLDER, "bin", r"Peon.exe")
CONFIG_FOLDER = PEON_FOLDER

def run_peon(verb, src_folder, dst_folder, texconv_exe_path, fxc_exe_path, package_mod, verbose):
    if not os.path.exists(PEON_EXE_PATH):
        raise Exception(f"{PEON_EXE_PATH} does not exist")
    
    args = [f"{PEON_EXE_PATH}", f"{verb}"]
    args.extend([f'--source-folder="{src_folder}"'])
    args.extend([f'--destination-folder="{dst_folder}"'])
    args.extend([f'--config-folder="{CONFIG_FOLDER}"'])
    args.extend([f'--work-folder="{OUT_FOLDER}"'])
    args.append(f'--delete-unknown')    
    if texconv_exe_path:
        args.extend([f'--texconv-exe-path="{texconv_exe_path}"'])
    if fxc_exe_path:
        args.extend([f'--fxc-exe-path="{fxc_exe_path}"'])
    if package_mod:
        args.append("--package-mod")
    if verbose:
        args.append(f"--verbose")
    command_line = str.join(" ", args)
    print("\n{} (cwd={})\n".format(command_line, CURRENT_PATH))
    subprocess.call(command_line, cwd=CURRENT_PATH)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--src_folder", required=True)
    parser.add_argument("-d", "--dst_folder", required=True)
    parser.add_argument("-t", "--texconv_exe_path", default="", required=False)
    parser.add_argument("-f", "--fxc_exe_path", default="", required=False)
    parser.add_argument("-p", "--package_mod", action="store_true")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    run_peon(
        "build",
        args.src_folder,
        args.dst_folder,
        args.texconv_exe_path,
        args.fxc_exe_path,
        args.package_mod,
        args.verbose
    )
