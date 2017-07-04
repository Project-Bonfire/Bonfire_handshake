
#    The idea here is to make some lists of the necessary files for each scenario
#    in order to make the code a little more organized!

#---------------------------------------------------------
#
#        Hand shaking related files
#
#---------------------------------------------------------
# Files for the base-line hand shaking router!
handshaking_files = ["Arbiter.vhd", "FIFO_one_hot_handshaking.vhd", "LBDR.vhd", "xbar.vhd"]

#---------------------------------------------------------
#
#        Checker's files
#
#---------------------------------------------------------

# HS
HS_Arbiter_one_hot_with_checkers =["Arbiter_checkers.vhd", "Arbiter_one_hot_with_checkers.vhd"]
HS_FIFO_one_hot_with_checkers =["FIFO_control_part_checkers.vhd", "FIFO_one_hot_with_checkers.vhd"]
HS_LBDR_with_checkers =["LBDR_checkers.vhd", "LBDR_with_checkers.vhd"]
