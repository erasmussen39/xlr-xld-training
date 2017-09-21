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
    def __init__(self, current_release, release_api):
        self.current_release = current_release
        self.release_api = release_api
        return 

    @staticmethod
    def get_client(current_release, release_api):
        return Client(current_release, release_api)

    def simple_exampletask(self, variables):
        return {"output" : variables['example_property']}

    def simple_addgithash(self, variables):
        git_hash = variables['GIT_HASH']
        release_name = self.current_release.title
        new_release_name = release_name + git_hash

        #Update the name of the release here and submit via jython API
        self.current_release.setTitle(new_release_name)
        self.release_api.updateRelease(self.current_release)
        return {"git_hash": git_hash, "new_release_name": new_release_name}
