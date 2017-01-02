import sublime
import sublime_plugin

class OpenFolderCommand(sublime_plugin.WindowCommand):
    def run(self, **args):
        dir = args["dirs"][0]
        self.window.run_command("exec", {"cmd": ["start", dir], "shell": True, "working_dir": dir})
        self.window.run_command("hide_panel", {"panel": "output.exec"})

    def is_visible(self, **args):
        return len(args["dirs"]) > 0