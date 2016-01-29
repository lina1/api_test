__author__ = 'lina'

import os
import random

import yaml
from metacomm.combinatorics.all_pairs2 import all_pairs2

import generate_case
import helper
from config import const
from libs._logging import _logging
from parameters.input import para_input

# from config.const import test_user, base_url
from config_parse import Config


def yaml_load_all(file_path, version="v2.2", default_method="ALL"):

    load_logging = _logging()

    new_mtime = os.path.getmtime(file_path)

    time_config = Config()

    mtime = time_config.get("time", "mtime")

    if new_mtime > float(mtime):

        time_config.set("time", "mtime", 1453880617)

        stream = file(file_path, "r")

        data = yaml.load(stream)

        # base_url = data["configuration"]["uri"]
        # access_url = const.base_url
        methods = data["versions"].get(version)["methods"]

        if default_method != "ALL":
            load_logging._info("Specify method: %s" % default_method)

            if default_method not in methods.keys():
                load_logging._error("Method Wrong!!!")
                raise Exception
                #todo
            else:
                print 1, default_method
                generate_case_by_method(methods, default_method, load_logging)

        else:

            load_logging._info("Total methods: %d" % len(methods.keys()))
            # token = login()
            # methods_list = list()
            index = 1
            for method in methods.keys():
                print index, method
                generate_case_by_method(methods, method, load_logging)
                index += 1
    else:
        load_logging._info("Yaml file has not been modified since last loading...No generating...")

def format_url_with_para(url):

    #todo
    #it is just a test now
    if url.find("@id:\d+") != -1:
        type = helper.get_id_type(url, '@id')

        # print url
        # print type
        if type in ('flight', 'hotel', "topic", "membership"):
            url = url.replace("@id:\d+", random.choice(str(para_input[type]["valid"])))

        if type in ('feed', 'weibo'):
            if url.find("delete") != -1:
                url = url.replace("@id:\d+", random.choice(str(para_input["feed_id"]["to_delete"])))
            else:
                url = url.replace("@id:\d+", random.choice(str(para_input["wid"]["valid"])))

        if type in ('comment'):
            if url.find("delete") != -1:
                url = url.replace("@id:\d+", random.choice(str(para_input["comment_id"]["to_delete"])))
    #
    if url.find("@wid:\d+") != -1 :
        url = url.replace("@wid:\d+", random.choice(str(para_input["wid"]["valid"])))
    #
    if url.find("@type:\d+") != -1:
        url = url.replace("@type:\d+", "1")
    #
    if url.find("@uid:\d+") != -1 :
         url = url.replace("@uid:\d+", const.test_user["wuid"])

    return url


def generate_params(url, key_list, optional_key_list=[]):

    params_lists = list()

    # if len(key_list) >= 2:

    for param in generate_valid_param(url, key_list):
        param_dict = dict()
        for item in param:
            for k, v in item.items():
                param_dict[k] = v
        params_lists.append({"valid": param_dict})
    if params_lists:
        valid_param = params_lists[0]["valid"]
    else:
        valid_param = dict()

    for param in generate_optional_param(valid_param, optional_key_list):
        params_lists.append(param)

    for no_data_param in generate_no_data_param(key_list):
        params_lists.append({"no_data": no_data_param})

    for invalid_param in generate_invalid_param(url, key_list):
        if "poi_invalid" in invalid_param.keys():
            invalid_param["poi"] = invalid_param.pop("poi_invalid")
            params_lists.append({"poi_invalid": invalid_param})
        else:
            params_lists.append({"invalid": invalid_param})

    if len(key_list) >= 2:
        for single_param in generate_incomplete_params(key_list):
            params_lists.append({"invalid": single_param})

    return params_lists


def generate_case_by_method(methods, method, load_logging):
    load_logging._info("Begin to parse method %s" % method)
    key_list = []
    optional_key_list = []
    uri = methods[method].get("uri")
    # url = const.base_url % (uri, const.test_user["version"])
    url = const.base_url + uri + const.url_param % const.specify_version

    url = format_url_with_para(url)

    request_parameters = methods[method].get("request_parameters")
    need_token = False
    # data = dict()
    if not request_parameters:
        load_logging._info("Method %s has no parameters." % method)
        generate_case.generate_test_data(method, url=url, need_token=need_token)
        load_logging._info("Generate Done!")
    else:
        for para in request_parameters.keys():
            if not request_parameters[para].get("optional"):
                if not para == 'token':
                    key_list.append(para)

                else:
                    need_token = True
            else:
                optional_key_list.append(para)
        param_lists = generate_params(url, key_list, optional_key_list=optional_key_list)
        # print param_lists
        generate_case.generate_test_data(method, url=url, para_list=param_lists, need_token=need_token)
        load_logging._info("Generate Done!")

def generate_no_data_param(key_list):

    invalid_no_data_param_list = list()

    for key in key_list:

        if para_input[key].has_key("no_data"):

            for item in para_input[key]["no_data"]:
                invalid_param = dict()
                invalid_param[key] = item

                #if key is poi, add a tag
                # if key == 'poi':
                #     invalid_param[key+"_invalid"] = item
                # else:
                #     invalid_param[key] = item
                key_s = set()
                key_s.add(key)
                other_key_list = list(set(key_list).difference(key_s))
                for other_key in other_key_list:
                    # invalid_param.append({other_key: random.choice(para_input[other_key]["valid"])})
                    invalid_param[other_key] = random.choice(para_input[other_key]["valid"])
                # invalid_param["valid"] = False
                invalid_no_data_param_list.append(invalid_param)

    return invalid_no_data_param_list


def generate_optional_param(valid_param={}, optional_key_list=[]):
    param_list = []
    for key in optional_key_list:

        # if(key == "token"):
        #     token =
        #     param_list.append({"valid": login()})

        param = dict(valid_param)
        if para_input[key]["valid"]:
            param[key] = random.choice(para_input[key]["valid"])
            param_list.append({"valid": param})
        else:
            _logging()._warn("%s has no valid value" % key)

        if para_input[key].has_key("invalid"):

            for item in para_input[key]["invalid"]:
                inparam = dict(valid_param)
                inparam[key] = item
                if key == 'poi':
                    param_list.append({"poi_invalid": inparam})
                else:
                    param_list.append({"invalid": inparam})

        if para_input[key].has_key("no_data"):

            for item in para_input[key]["no_data"]:
                inparam = dict(valid_param)
                inparam[key] = item

                param_list.append({"no_data": inparam})
    para_with_all_option = dict(valid_param)
    for key in optional_key_list:
        para_with_all_option[key] = random.choice(para_input["key"]["valid"])
    param_list.append({"valid": para_with_all_option})
        # else:
        #     _logging()._warn("%s has no invalid value" % key)

    return param_list


def generate_incomplete_params(key_list):
    incomplete_paras_list = []
    for key in key_list:
        key_s = set()
        key_s.add(key)
        other_key_list = list(set(key_list).difference(key_s))
        key_param = {}
        for other_key in other_key_list:
            key_param[other_key] = random.choice(para_input[other_key]["valid"])
        incomplete_paras_list.append(key_param)

    return incomplete_paras_list


def generate_single_params(key_list):

    single_param_list = []
    for key in key_list:
        # print key
        for valid in para_input[key].get("valid"):
            single_param_list.append(valid)
        # single_param_list.append({key: random.choice(para_input[key]["valid"])})

    return single_param_list


def generate_valid_param(url, key_list):

    valid_param_list = []
    valid_param_list_all = []

    for key in key_list:

        key_pair = {}

        if key == "id":

            # id category
            type = helper.get_id_type(url, "")
            new_key = type + "_id"
            key_pair[key] = new_key
        else:
            key_pair[key] = key

        valid_param = list()
        new = key_pair[key]
        for item in para_input[new]["valid"]:
            valid_param.append({key: item})
            # valid_param.append({"valid": True})
        valid_param_list_all.append(valid_param)
    if len(key_list) >= 2:
        # print key_list
        # print valid_param_list_all
        pairwise = all_pairs2(valid_param_list_all)

        for i, v in enumerate(pairwise):
            valid_param_list.append(v)

        return valid_param_list
    else:
        return valid_param_list_all


def generate_invalid_param(url, key_list):

    invalid_param_list = list()

    for key in key_list:

        key_pair = {}

        if key == "id":

            # id category
            type = helper.get_id_type(url, "")
            new_key = type + "_id"
            key_pair[key] = new_key
        else:
            key_pair[key] = key

        # print key

        # print key

        new = key_pair[key]

        for item in para_input[new]["invalid"]:
            invalid_param = dict()
            # invalid_param.append({key: item})

            #if key is poi, add a tag
            if key == 'poi':
                invalid_param[key+"_invalid"] = item
            else:
                invalid_param[key] = item
            key_s = set()
            key_s.add(key)
            other_key_list = list(set(key_list).difference(key_s))
            for other_key in other_key_list:
                # invalid_param.append({other_key: random.choice(para_input[other_key]["valid"])})
                invalid_param[other_key] = random.choice(para_input[other_key]["valid"])
            # invalid_param["valid"] = False
            invalid_param_list.append(invalid_param)

    return invalid_param_list



# generate_params("departure", "arrival", "airport")
file_path = "/Users/lina/Documents/api_2016-01-27.yml"
# print os.path.getmtime(file_path)
yaml_load_all(file_path, default_method="ICollectionAdd")
