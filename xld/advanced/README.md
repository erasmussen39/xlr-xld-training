# XL Deploy Advanced Plugin

## Problem Statement
Acme Corporation has a complex application they package in a .zip that contains two folders, foo & bar, that contain the runtime artifacts for the application. During deployment of the application, the following must occur:
- The target folders for foo & bar must be defined. They will potentially be different in every target environment.
- The first time the application is deployed the target folders to copy foo & bar to must be created on the target system.
- Subsequent deployments of the application should follow these rules:
  - New files should be copied to the appropriate location in foo/bar.
  - Modified files should be updated in the appropriate location.
  - Deleted files should be removed from the target location.
  - A report should be displayed listing all three categories.
  - The deployment should work on a Unix or Windows system.
- Undeploying the application should result in the target folders in the target environment being completely removed.

In this exercise, create a custom XL Deploy plugin that does the following:
- Defines a custom deployed/deployable type for these deployments.
- Defines a custom container type for these deployments.
- Obeys all the specified requirements for deployments defined above.
