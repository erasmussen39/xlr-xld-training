# XL Release/Deploy Plugin Training
The intent of this repository is to give you the basic plugin structure for both XL Release and XL Deploy, as well as a simple/advanced problem for each tool. In each case, you are given a problem statement. See below for links to resources that will help you in solving the described problems.

- [XL Release Simple Plugin](xlr/simple/)
- [XL Release Advanced Plugin](xlr/advanced/)
- [XL Deploy Simple Plugin](xld/simple/)
- [XL Deploy Advanced Plugin](xld/advanced/)

## Building/Packaging
Each plugin can be built, packaged, and delivered to the corresponding tool in the exact same fashion. You will find the following directory structure under this repository:
```
.
├── xld
│   ├── advanced
│   │   ├── gradle
│   │   │   └── wrapper
│   │   └── src
│   │       └── main
│   │           └── resources
│   │               └── scripts
│   └── simple
│       ├── gradle
│       │   └── wrapper
│       └── src
│           └── main
│               └── resources
│                   └── scripts
└── xlr
    ├── advanced
    │   ├── gradle
    │   │   └── wrapper
    │   ├── src
    │   │   └── main
    │   │       └── resources
    │   │           └── advanced
    │   └── templates
    └── simple
        ├── gradle
        │   └── wrapper
        ├── src
        │   └── main
        │       └── resources
        │           └── simple
        └── templates
```
There are four distinct plugins provided with this repository. The advanced & simple directories under each tool (xlr/xld) represents an independent and stand-alone plugin that can be built and delivered to your tool. So, for example, if we take the xlr/simple plugin, we will find the following inside the base directory:
```
build.gradle  gradle  gradlew  gradlew.bat  README.md  settings.gradle  src  templates
```
You can see that a [Gradle](https://gradle.org/) wrapper is provided with each plugin. This is the mechanism that will be utilized to build and package your code. All you need to do in order to build/package is execute: `./gradlew build` from the main directory of the plugin (in this case: `xlr-xld-training/xlr/simple`). Executing this will result in a jar file being built for you under the `build/libs` directory. The name of the jar file that gets created in that directory is based on the project name, which is defined in the `settings.gradle` file:
```
rootProject.name = 'xlr-training-simple-plugin'
```
and the version that is defined in your `build.gradle` file:
```
defaultTasks 'build'

apply plugin: 'java'

version='1.0.0'
```
So, in this example, after running `./gradlew build` from the base plugin directory, you will see the following in your `build/libs` directory:
```
xlr-training-simple-plugin-1.0.0.jar
```
Adding this plugin to your tool is as simple as copying it to the `plugins` directory of the tool that the plugin is intended for. For example `/opt/xl-release/plugins`. After copying the file to the appropriate location, simply re-start the tool, and you will see the functionality within the corresponding tool that is implemented in your plugin.

### XL Release Resources
- [XL Release Main Documentation](https://docs.xebialabs.com/xl-release/)
- [XL Release Concepts](https://docs.xebialabs.com/xl-release/concept/)
- [XL Release Custom Tasks](https://docs.xebialabs.com/xl-release/how-to/create-custom-task-types.html)
- [XL Release Rest API](https://docs.xebialabs.com/xl-release/latest/rest-api/)
- [XL Release Jython API](https://docs.xebialabs.com/xl-release/latest/jython-api/index.html)

### XL Deploy Resources
- [XL Deploy Main Documentation](https://docs.xebialabs.com/xl-deploy/)
- [XL Deploy Concepts](https://docs.xebialabs.com/xl-deploy/concept/)
- [XL Deploy Custom Plugin](https://docs.xebialabs.com/xl-deploy/how-to/create-an-xl-deploy-plugin.html)
- [XL Deploy Rest API](https://docs.xebialabs.com/xl-deploy/latest/rest-api/)

### Plugin Resources
- [XL Community Plugin Standards](http://xebialabs-community.github.io/)
- [Plugin Creation Plugin](https://github.com/xebialabs-community/xlr-plugin-plugin)

### Git Resources
- [Git Command Line](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)
