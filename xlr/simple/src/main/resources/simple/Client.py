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
        self.currentRelease = current_release
        self.releaseApi = release_api

    @staticmethod
    def get_client(current_release, release_api):
        return Client(current_release, release_api)

    def simple_updatetitle(self, variables):
        release_title = self.currentRelease.getTitle()
        sha1 = ""
        for tag in self.currentRelease.getTags():
            if not tag.startsWith('Trigger') and tag.startsWith('Release'):
                sha1 = tag
        new_release_title = "%s - %s" % (release_title, sha1)
        self.currentRelease.setTitle(new_release_title)
        self.releaseApi.updateRelease(self.currentRelease)
