
import plugins.webbrowser_commands
import plugins.clipboard_commands
import plugins.aws_utility_commands
import plugins.hyperpod_commands

class Config:    

    plugins = [
        plugins.webbrowser_commands.WebBrowserCommands,
        plugins.clipboard_commands.ClipboardCommands,
        plugins.aws_utility_commands.AwsUtilityCommands,
        plugins.hyperpod_commands.HyperPodCommands,
    ]

    cmd_aws = ["aws"]
