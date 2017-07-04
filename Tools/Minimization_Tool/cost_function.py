# copyright 2016 Siavoosh Payandeh Azad and Behrad Niazmand

import package_file
from file_generator import generate_specific_file
from area_coverage_calc import calculate_coverage


def calculate_coverage_cost(current_selected_list):
    # this cost would be the fault coverage of a set of checkers
    coverage = 0
    print "\t------------------"
    print "\tcalculating cost function for items:", current_selected_list
    # i want to use this part for initializing the  dictionary
    new_key = None
    if len(current_selected_list) == 1:
        new_key = current_selected_list[0]
    elif len(current_selected_list) > 1:
        new_key = ""
        for i in sorted(current_selected_list):
            new_key += i + "_"
        new_key = new_key[:len(new_key) - 1]

    if new_key not in package_file.list_of_candidates.keys():
        # this is actually how it should be!
        generate_specific_file(current_selected_list)
        coverage = calculate_coverage(current_selected_list)
        package_file.list_of_candidates[new_key] = [coverage, None]
    else:
            # this is for the time being
        if package_file.list_of_candidates[new_key][0] is None:
            coverage = calculate_coverage(current_selected_list)
            package_file.list_of_candidates[new_key][0] = coverage
        else:
            coverage = package_file.list_of_candidates[new_key][0]

    print "\t\tcoverage:", coverage
    print "\t------------------"
    return coverage


def calculate_value_density(current_selected_list):
    # this cost would be the fault coverage of a set of checkers
    coverage = 0
    print "\t------------------"
    print "\tcalculating cost function for items:", current_selected_list
    # i want to use this part for initializing the  dictionary
    new_key = None
    if len(current_selected_list) == 1:
        new_key = current_selected_list[0]
    elif len(current_selected_list) > 1:
        new_key = ""
        for i in sorted(current_selected_list):
            new_key += i + "_"
        new_key = new_key[:len(new_key) - 1]

    if new_key not in package_file.list_of_candidates.keys():
        # this is actually how it should be!
        generate_specific_file(current_selected_list)
        coverage = calculate_coverage(current_selected_list)
        package_file.list_of_candidates[new_key] = [coverage, None]
    else:
            # this is for the time being
        if package_file.list_of_candidates[new_key][0] is None:
            coverage = calculate_coverage(current_selected_list)
            package_file.list_of_candidates[new_key][0] = coverage
        else:

            print "\tvalue density:", package_file.list_of_candidates[new_key][0]
            print "\t------------------"
            return package_file.list_of_candidates[new_key][0]

    print "\tcoverage:", coverage
    print "\tarea:", package_file.list_of_candidates[new_key][1]
    value_density = float(coverage)/package_file.list_of_candidates[new_key][1]
    print "\tvalue density:", value_density
    print "\t------------------"
    return value_density


def calculate_cost(current_selected_list):
    # this cost would be the fault coverage of a set of checkers
    coverage = 0
    print "\t------------------"
    print "\tcalculating cost function for items:", current_selected_list
    # i want to use this part for initializing the  dictionary
    new_key = None
    if len(current_selected_list) == 1:
        new_key = current_selected_list[0]
    elif len(current_selected_list) > 1:
        new_key = ""
        for i in sorted(current_selected_list):
            new_key += i + "_"
        new_key = new_key[:len(new_key) - 1]
    else:
        return coverage

    if new_key not in package_file.list_of_candidates.keys():
        # this is actually how it should be!
        generate_specific_file(current_selected_list)
        coverage = calculate_coverage(current_selected_list)
        package_file.list_of_candidates[new_key] = [coverage, None]
    else:
            # this is for the time being
        if package_file.list_of_candidates[new_key][0] is None:
            coverage = calculate_coverage(current_selected_list)
            package_file.list_of_candidates[new_key][0] = coverage
        else:
            coverage = package_file.list_of_candidates[new_key][0]

    print "\t\tcoverage:", coverage
    print "\t------------------"
    return coverage
