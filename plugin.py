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
    try:
        return (urlopen("http://sphereonlinejudge.herokuapp.com/problem/%s" % id.upper()).read().decode("utf-8").replace("\r", ""))
    except:
        return None
class SphereOnlineCommand(sublime_plugin.TextCommand):

    def fetch_text(self):
        region = sublime.Region(0,self.view.size())
        content = self.view.substr(region)
        return content
    def check_for_doc(self):
        array = self.fetch_text().split("\n")[:5:]
        for i, e in enumerate(array):
            if "@problem:" in e:
                return e.split("@problem:")[-1].strip() 
        return None
    def run(self, edit, types=None):
        self.holder = None
        self.window = sublime.active_window()
        id = self.check_for_doc()
        if id and types=="read":
            self.display(id)
        else:
            if not self.holder:
                self.window.show_input_panel(
                    "Sphere Online Judge Problem ID:", '', lambda s: self.display(s), None, None)
            else:
                self.window.show_input_panel(
                    "Sphere Online Judge Problem ID:", HOLDER, lambda s: self.display(s), None, None)

    def display(self, id):
        sublime.status_message("Fetching problem content..")
        self.holder = id
        self.id = id
        thread = threading.Thread(target=self.display_content)
        thread.start() 

    def display_content(self):
        string = get_text(self.id)
        if string is None:
            sublime.status_message("Invalid Code")
            sublime.error_message("Invalid Problem Code")
        else:
            self.show_text(string)
            sublime.status_message("")

    def show_text(self,msg):
        self.output_view = self.window.get_output_panel("textarea")
        self.window.run_command("show_panel", {"panel": "output.textarea"})
        
        s = self.output_view.settings()
        s.set("word_wrap", True)
        
        self.output_view.set_read_only(False)
        
        self.output_view.run_command("append", {"characters": msg})
        self.output_view.set_read_only(True)