// Exported from:        http://shadow.hunyuk.org:5516/#/templates/Folder840512222-Release435561834/xfile
// XL Release version:   7.1.0
// Date created:         Tue Sep 12 14:43:38 MDT 2017

xlr {
  release('XL_Release_Advanced_Plugin') {
    variables {
      listVariable('UAT_TEST_CATEGORIES') {
        required false
        showOnReleaseStart false
      }
    }
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2017-09-12T09:00:00-0600')
    phases {
      phase('Dev') {
        color '#009CDB'
        tasks {
          manual('Deploy To Dev Environment') {
            owner 'admin'
          }
        }
      }
      phase('Test') {
        color '#009CDB'
        tasks {
          manual('Run Unit Tests') {
            owner 'admin'
          }
          userInput('Define UAT Categories') {
            description 'Please enter the required information below.'
            owner 'admin'
            variables {
              variable 'UAT_TEST_CATEGORIES'
            }
          }
        }
      }
      phase('UAT') {
        color '#009CDB'
        tasks {
          manual('Create UAT Gates') {
            description 'Manually create a Gate Task for each UAT Category defined in the UAT_TEST_CATEGORIES list variable. Place each Gate Task in the existing "Execute UAT Gates" Parallel Group defined in this phase.'
            owner 'admin'
          }
          parallelGroup('Execute UAT Gates') {
            
          }
        }
      }
      phase('Prod') {
        color '#009CDB'
        tasks {
          manual('Deploy To Production') {
            owner 'admin'
          }
        }
      }
    }
  }
}