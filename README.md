# CloudWatchLogs

This plugin for [Sublime Text](https://www.sublimetext.com) allows you to view
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) logs in a tab.

## Features

* View log events from the last 60 minutes


## Prerequisites

This plugin requires AWS credentials that provide the ability to list and view
your CloudWatch logs.

    {
      ...
      "logs:describeLog*",
      "logs:getLogEvents"
      ...
    }


## Installation

#### [Package Control](https://github.com/wbond/sublime_package_control) (Recommended)

CloudWatchLogs is included in the default repository channel for [Package Control](https://github.com/wbond/sublime_package_control)
and is installed just as any other package would be.  There are no special commands or settings
to configure.

## Key Binding

CloudWatchLogs has no default key binding.

## Command Palette

CloudWatchLogs appears as "CloudWatch: View Logs"
