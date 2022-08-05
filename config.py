#StartPage='/home/plof/Documents/startpages/Minimo-Homepage/index.html'
StartPage='/home/plof/Documents/startpages/Starter/homepage.html'
c.downloads.position = 'bottom'
c.tabs.background = True
c.url.default_page = StartPage
config.set('url.start_pages',StartPage)
config.load_autoconfig(False)

c.downloads.location.directory = "~/Downloads"

config.bind("mv", "spawn mpv -v {url}")
config.bind("xv", "spawn st -e youtube-dl {url}")
config.bind("xa", "spawn st -e youtube-dl -x --audio-format mp3 {url}")
config.set("colors.webpage.darkmode.enabled",True)
config.source('qutewal.py')

c.auto_save.interval = 15000
c.aliases = {'w': 'session-save', 'q': 'close', 'qa': 'quit', 'wq': 'quit --save', 'wqa': 'quit --save'}
##c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.hints.radius = 10
c.tabs.width = '80%'
c.url.searchengines = {'DEFAULT': 'https://google.com/search?q={}'}
