__author__ = 'lina'

import shutil

from config import case_config
from libs._logging import _logging


def generate_test_data(method_name, url, para_list=None, need_token=True):

    gen_logging = _logging()

    try:
        gen_logging._info("Start creating robot file for %s..." % method_name)
        case_path = "../robot/TEST_" + method_name + ".robot"

        gen_logging._info(case_path)

        # if os.path.exists(case_path):
        #     os.remove(case_path)

        shutil.copy("../robot/Base_Robot_Suite.robot", case_path)
        case_file = open(case_path, "a+")

        # for line in case_file.readlines():
        #     pass

        index = 1

        # para_list is NONE
        if not para_list:

            case_name = method_name + "_00000"

            if not need_token:
                gen_logging._info("Method %s has no parameters." % method_name)
                test_case_template = case_config.base_case_template % (case_name, url, "", "need_token=False")
                case_file.write(test_case_template)
                case_file.write(case_config.response_validate_template % (method_name, "normal"))

            else:
                gen_logging._info("Method %s has one parameter:token." % method_name)
                test_case_template = case_config.base_case_template % (case_name, url, "", "need_token=True")
                case_file.write(test_case_template)
                case_file.write(case_config.response_validate_template % (method_name, "normal"))

                case_name = method_name + "_00000_bad_token"
                write_test_token_case(case_file, case_name, method_name, url, test_token=True)

                case_name = method_name + "_00000_no_token"
                write_test_token_case(case_file, case_name, method_name, url, test_no_token=True)

        # para_list is not NONE
        else:
            test_token_param = para_list[0]["valid"]

            for para in para_list:
                case_name = method_name + "_" + "%05d" % index

                is_valid = para.has_key("valid")
                is_poi_invalid = para.has_key("poi_invalid")
                no_data_tag = para.has_key("no_data")
                if need_token:
                    test_case_template = case_config.base_case_template % (case_name, url, para.popitem()[1], "need_token=True")
                else:
                    test_case_template = case_config.base_case_template % (case_name, url, para.popitem()[1], "need_token=False")
                case_file.write(test_case_template)
                if is_valid:
                    case_file.write(case_config.response_validate_template % (method_name, "normal"))
                elif is_poi_invalid:
                    case_file.write(case_config.response_validate_template % (method_name, "invalid_position"))
                elif no_data_tag:
                    case_file.write(case_config.response_validate_template % (method_name, "no_data"))
                else:
                    case_file.write(case_config.response_validate_template % (method_name, "para_error"))

                index += 1

            # test case: bad token
            if need_token:
                case_name = method_name + "_" + "%05d" % index
                write_test_token_case(case_file, case_name, method_name, url, test_token_param=test_token_param, test_token=True)

                # test case: no token
                case_name = method_name + "_" + "%05d" % (index+1)
                write_test_token_case(case_file, case_name, method_name, url, test_token_param=test_token_param, test_no_token=True)

        gen_logging._info("Create TEST_%s.robot successfully!" % method_name)

        case_file.close()
    except Exception,e:
        gen_logging._exception(e)

def write_test_token_case(case_file, case_name, method_name, url, test_token_param="", test_token=False, test_no_token=False):

    if test_token:
        test_case_template_bad_token = case_config.base_case_template_test_token % (case_name, url, test_token_param, "test_token=True")
        tag = "login_required"
    if test_no_token:
        test_case_template_bad_token = case_config.base_case_template_test_token % (case_name, url, test_token_param, "test_no_token=True")
        tag = "access_denied"

    case_file.write(test_case_template_bad_token)
    case_file.write(case_config.response_validate_template % (method_name, tag))


# generate_test_data("IAIRLINE", "http://www.baidu.com", [{"a":1},{"b":2}])


