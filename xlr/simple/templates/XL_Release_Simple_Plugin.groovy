// Exported from:        http://shadow.hunyuk.org:5516/#/templates/Folder840512222-Release590441828/xfile
// XL Release version:   7.1.0
// Date created:         Tue Sep 12 10:40:59 MDT 2017

xlr {
  release('XL_Release_Simple_Plugin') {
    scheduledStartDate Date.parse("yyyy-MM-dd'T'HH:mm:ssZ", '2017-09-12T09:00:00-0600')
    phases {
      phase('Simple Phase') {
        color '#009CDB'
        tasks {
          custom('Simple Example Task') {
            script {
              type 'simple.ExampleTask'
              example_property 'FOO'
            }
          }
        }
      }
    }
  }
}