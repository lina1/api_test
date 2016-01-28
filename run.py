__author__ = 'lina'

import os

if __name__ == "__main__":

    #step1: load python env: changers_api
    # os.system("source /opt/python_virtual/changers_api/bin/activate")

    #step2: insert current path to sys path
    library_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "library")

    #step3: run cases
    os.chdir("/Users/lina/PycharmProjects/api_test_demo/robot/")
    # os.system("cd ")

    # print os.system("pwd")
    os.system("pybot --pythonpath " + library_path + " -d ../output/ TEST_IAirline.robot ")
    # robot.run()
