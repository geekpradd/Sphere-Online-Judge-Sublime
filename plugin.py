import sublime, sublime_plugin, json, threading
try:
    from urllib2 import urlopen 
except ImportError:
    from urllib.request import urlopen 
try:
    from utils import cache 
except:
    from .utils import cache 
@cache 
def get_text(id):
    return (urlopen("http://sphereonlinejudge.herokuapp.com/problem/%s" % id).read().decode("utf-8").replace("\r", ""))

class SphereOnlineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.holder = None
        self.window = sublime.active_window()
        if not self.holder:
            self.window.show_input_panel(
                "Sphere Online Judge Problem ID:", '', lambda s: self.display(s), None, None)
        else:
            self.window.show_input_panel(
                "Sphere Online Judge Problem ID:", HOLDER, lambda s: self.display(s), None, None)
    def display(self, id):
        self.holder = id
        self.id = id
        thread = threading.Thread(target=self.display_content)
        thread.start() 
    def display_content(self):
        string = get_text(self.id)
        print (string)
        self.show_text(string)

    def show_text(self,msg):
        self.output_view = self.window.get_output_panel("textarea")
        self.window.run_command("show_panel", {"panel": "output.textarea"})
        self.output_view.set_read_only(False)
        self.output_view.run_command("append", {"characters": msg})
        self.output_view.set_read_only(True)