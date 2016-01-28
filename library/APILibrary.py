__author__ = 'lina'

import os
import sys

file_path = os.path.dirname(os.path.realpath(__file__))

project_path = os.path.pardir
project_path = os.path.abspath(os.path.join(file_path, project_path))

library_path = os.path.join(project_path, "libs")
sys.path.insert(0, library_path)

import requests
import demjson
from config import const
from libs._logging import _logging
from jsonschema import validate
from _jsonschema_format import IFormatChecker
import simplejson
from config import schema_conf
from robot.errors import DataError


class APILibrary(_logging):

    ROBOT_LIBRARY_SCOPE = 'Global'

    def get_response(self, url, params=None, test_login=False, test_token=False, test_no_token=False, need_token=True):
        # self._info("************" + params)

        if params is not None:
            params = eval(params)

        if not isinstance(need_token, bool):
            need_token = eval(need_token)

        if need_token:

            if params is None:
                params = dict()

            if test_no_token:
                self._info("Test no token...")
            elif test_token:
                self._info("Test wrong token...")
                params["token"] = const.test_token
            elif not test_login:
                self._info("Get login token...")
                params["token"] = self._login()

        self._info("url: " + url)
        self._info("params: " + str(params))

        try:

            resp = requests.post(url=url, data=params)
            status_code = resp.status_code

            if status_code == 404:
                # self._error("NOT FOUND 404: %s" % url)
                raise DataError("NOT FOUND 404: %s" % url)
                # raise UrlError, 'url not found'
            elif status_code == 403:
                # self._error("Forbidden 403: %s" % url)
                raise ValueError("Forbidden 403: %s" % url)
                # raise UrlError
            elif status_code == 500:
                raise ValueError("Internal Server Error 500")
            else:
                return resp.text

        except Exception, e:

            self._exception(e)

    def _login(self):

        try:

            url = const.weibo_login_url
            login_resp = requests.post(url, data=const.test_user)

            self._info("Login status code: " + str(login_resp.status_code))
            return str(demjson.decode(login_resp.text)["data"]["token"])
        except Exception:
            self._error("Login error!!!")
            # self._exception(e)
            # assert False

    def result_should_be_true(self, response_data):

        result = eval(response_data)["result"]
        assert result == 1

    def result_should_be_false(self, response_data):

        result = eval(response_data)["result"]
        assert result == -1

    def json_validate(self, response_data, method_name, schema_type="normal"):

        # expect = schema.method_name

        # expect = IAIRLINE.IAIRLINE_SCHEMA_NORMAL
        # if schema_type == "NORMAL":
        #     expect = IAIRLINE.IAIRLINE_SCHEMA_NORMAL
        # if schema_type == "PARAM_ERROR":
        #     expect = IAIRLINE.IAIRLINE_SCHEMA_PARM_ERROR
        # validate(eval(response_data), expect)
        true = True
        false = False
        if schema_type in schema_conf.json_template_list:
            expect = self._get_schema(schema_type)
        else:
            f = open("../schema/%s.json" % method_name, "r")

            json_data = simplejson.load(f)
            expect = json_data[schema_type]

        # Default: if required is not given, all is required.
        self._add_required(expect)

        # self._info(expect)
        # self._info(response_data)
        validate(self._process_response_data(eval(response_data)), expect, format_checker=IFormatChecker())

    def database_validate(self, sql, expect="no_data"):
        #todo
        pass

    def _get_schema(self, schema_type):

        f = open('../schema/%s.json' % schema_type, "r")
        expect = simplejson.load(f)
        return expect

    def _process_response_data(self, response_data):

        # response_data = eval(response_data)

        if isinstance(response_data, dict):
            for k, v in response_data.items():
                if isinstance(v, str) and v.isdigit():
                    self._info("Change %s to integer: " % k + v)
                    response_data[k] = eval(v)
                else:
                    self._process_response_data(v)
        if isinstance(response_data, list):
            for item in response_data:
                self._process_response_data(item)

        return response_data

    def _add_required(self, expect):
        pass

