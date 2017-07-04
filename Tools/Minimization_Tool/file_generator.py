# copyright 2016 Siavoosh Payandeh Azad and Behrad Niazmand

import os

import package_file
from vhdl_generators import gen_lbdr_cheker_files, gen_lbdr_checker_top
from vhdl_generators import gen_fifo_checker_top, gen_fifo_cheker_files
from vhdl_generators import gen_arbiter_checker_top, gen_arbiter_cheker_files
import gen_unit_synth_script


def make_folders():
    synth_script_folder = "synthesis_scripts"
    if not os.path.isdir(synth_script_folder):
        os.makedirs(synth_script_folder)

    file_list = [script_file for script_file in os.listdir(synth_script_folder) if script_file.endswith(".script")]
    for script_file in file_list:
        os.remove(synth_script_folder+'/'+script_file)

    checkers_vhdl_directory = "checker_vhdl"
    if not os.path.isdir(checkers_vhdl_directory):
        os.makedirs(checkers_vhdl_directory)

    file_list = [vhd_file for vhd_file in os.listdir(checkers_vhdl_directory) if vhd_file.endswith(".vhd")]
    for vhd_file in file_list:
        os.remove(checkers_vhdl_directory+'/'+vhd_file)

    log_folder = "logs"
    if not os.path.isdir(log_folder):
        os.makedirs(log_folder)

    file_list = [log_file for log_file in os.listdir(log_folder) if log_file.endswith(".log")]
    for log_file in file_list:
        os.remove(log_folder+'/'+log_file)


def generate_specific_file(current_selected_list):
    if len(current_selected_list) == 0:
        return None
    else:
        gen_unit_synth_script.gen_unit_checker_script(current_selected_list)


    if package_file.unit_under_test == "LBDR":
        gen_lbdr_cheker_files.gen_lbdr_checkers(current_selected_list)
        gen_lbdr_checker_top.gen_lbdr_checker_top(current_selected_list)

    elif package_file.unit_under_test == "FIFO_control_part":
        gen_fifo_cheker_files.gen_fifo_checkers(current_selected_list)
        gen_fifo_checker_top.gen_fifo_checker_top(current_selected_list)

    elif package_file.unit_under_test == "Arbiter":
        gen_arbiter_cheker_files.gen_arbiter_checkers(current_selected_list)
        gen_arbiter_checker_top.gen_arbiter_checker_top(current_selected_list)


def generate_initial_files():
    for i in package_file.list_of_checkers:
        list_of_checkers = [i]
        generate_specific_file(list_of_checkers)