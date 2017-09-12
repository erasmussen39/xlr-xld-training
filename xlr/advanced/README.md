# XL Release Advanced Plugin

## Problem Statement
Acme Corporation has a release process that includes four phases ([See/Import Template](templates/XL_Release_Advanced_Plugin.groovy)):
- Dev
- Test
- UAT
- Prod

At the end of the Test phase they have defined a user input task where a list of the UAT categories they want performed for this application is input. For example:
- Alpha Testing
- Beta Testing
- Contract Acceptance Testing
- Regulation Acceptance Testing
- Operational Acceptance Testing
- Black Box Testing

In the current process, they have a single manual task at the beginning the UAT phase where the assigned user looks at the value provided in the user input task and then manually creates corresponding gate tasks that execute in parallel for each UAT testing category that was defined in the user input list.

Create a plugin with a custom task that take the value provided from the user input task in the test phase and dynamically create a Gate Task for each UAT category that was input. The Gate Tasks should run in parallel within the Parallel Group that was already defined in the UAT Phase of the provided template. Assign each dynamically created Gate Task to the admin user.
