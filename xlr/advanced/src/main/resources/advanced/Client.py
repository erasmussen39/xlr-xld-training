    #
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

class Client(object):
    def __init__(self, current_release, release_api, current_phase, phase_api, task_api):
        self.currentRelease = current_release
        self.releaseApi = release_api
        self.currentPhase = current_phase
        self.phaseApi = phase_api
        self.taskApi = task_api

    @staticmethod
    def get_client(current_release, release_api, current_phase, phase_api, task_api):
        return Client(current_release, release_api, current_phase, phase_api, task_api)

    @staticmethod
    def find_task_with_title(title, tasks):
        for task in tasks:
            if task.getTitle() == title:
                return task

    @staticmethod
    def find_variable_with_key(key, variables):
        for variable in variables:
            if variable.getKey() == key:
                return variable

    def create_task(self, name, container_id):
        task = self.taskApi.newTask("xlrelease.GateTask")
        task.title = "%s" % name
        task.owner = "admin"
        self.taskApi.addTask(container_id, task)

    def advanced_createuatgates(self, variables):
        for task in self.currentPhase.getTasks():
            print "task type: %s" % task.getType()
        parallel_group = Client.find_task_with_title("Execute UAT Gates", self.currentPhase.getTasks())
        print "Found Parallel Group: %s" % parallel_group
        categories_variable = Client.find_variable_with_key(variables['variable_name'], self.currentRelease.getVariables())
        print "Found UAT Categories Variable: %s" % categories_variable
        for category in categories_variable.getValue():
            print "Creating task for UAT Category: %s" % category
            self.create_task(category, parallel_group.getId())
        return {"output" : variables['variable_name']}

