def server(type, title) {
    def cis = configurationApi.searchByTypeAndTitle(type, title)
    if (cis.isEmpty()) {
        throw new RuntimeException("No CI found for the type '${type}' and title '${title}'")
    }
    if (cis.size() > 1) {
        throw new RuntimeException("More than one CI found for the type '${type}' and title '${title}'")
    }
    cis.get(0)
}
def server1 = server('xldeploy.Server','XL Deploy')
xlr {
  release('XL_Release_Simple_Plugin') {
    variables {
      stringVariable('BUILD_RELEASE_ID') {
        required false
        showOnReleaseStart false
      }
    }
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2017-09-12T09:00:00-0600')
    phases {
      phase('Build') {
        color '#009CDB'
        tasks {
          manual('Find Release Template') {
            owner 'admin'
          }
          createRelease('Start Build Sub-Release') {
            createdReleaseId '${BUILD_RELEASE_ID}'
          }
          gate('Wait For Build') {
            description 'Wait for build sub-release to complete.'
            dependencies {
              dependency {
                variable 'BUILD_RELEASE_ID'
              }
            }
          }
        }
      }
      phase('Test') {
        color '#009CDB'
        tasks {
          custom('Deploy to Test') {
            script {
              type 'xldeploy.Deploy'
              server server1
            }
          }
          manual('Test Code') {
            owner 'admin'
          }
        }
      }
    }
  }
}
