import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

NEWS_DATA = [
    ["NASA FINDS NEW EARTH LIKE PLANET", "https://images.unsplash.com/photo-1446776877081-d282a0f896e2", "NASA discovered a new Earth-like planet 100 light-years away."],
    ["INDIA WINS CRICKET WORLD CUP MATCH", "https://images.unsplash.com/photo-1540747913346-19e32dc3e97e", "India won a thrilling match against Australia."],
    ["NEW AI ROBOT CAN DO ALL HOMEWORK", "https://images.unsplash.com/photo-1485827404703-89b55fcc595e", "A new AI robot can help students with all their homework."],
    ["BMW LAUNCHES FASTEST M5 EVER", "https://images.unsplash.com/photo-1555215695-3004980ad54e", "BMW launched its fastest M5 car ever with 1000 horsepower."],
    ["SCHOOLS TO GET FREE LAPTOPS FOR CODING", "https://images.unsplash.com/photo-1496181133206-80ce9b88a853", "Government will give free laptops to students to learn coding."],
    ["HUGE DISCOVERY IN MINECRAFT UPDATE", "https://images.unsplash.com/photo-1511512578047-dfb367046420", "Minecraft released a huge new update with new worlds."],
    ["ELON MUSK SENDS NEW ROCKET TO MARS", "https://images.unsplash.com/photo-1517976487492-5750f3195933", "SpaceX sent a new rocket towards Mars."],
    ["PYTHON BECOMES NUMBER 1 LANGUAGE", "https://images.unsplash.com/photo-1526379095098-d400fd0bf935", "Python became number one coding language in 2026."],
    ["NEW UNDERWATER CITY FOUND", "https://images.unsplash.com/photo-1551244072-5d12893278ab", "Divers found an ancient city deep under the ocean."],
    ["FREE INTERNET FOR ALL STUDENTS", "https://images.unsplash.com/photo-1451187580459-43490279c0fa", "Free high-speed internet for all students in India."],
    ["WORLD'S BIGGEST GAMING TOURNAMENT", "https://images.unsplash.com/photo-1542751371-adc38448a05e", "Biggest gaming tournament started in Delhi."],
    ["NEW FLYING BIKE INVENTED", "https://images.unsplash.com/photo-1558981806-ec527fa84c39", "Japan invented a real flying bike."],
    ["INDIAN KID MAKES BROWSER AT 10", "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d", "10-year-old Navyug made his own browser NAVYUG WORLD."],
]

def get_home_html():
    cards = ""
    for i, (title, img, text) in enumerate(NEWS_DATA):
        cards += f"""<div class="card"><img src="{img}?w=400&h=250&fit=crop" class="news-img"><h2 class="news-title">{title}</h2><button class="icon-btn" onclick="toggleText({i})">◉</button><p id="full-{i}" class="full-text">{text} Full details only on NAVYUG WORLD.</p></div>"""
    return f"""<html><head><style>
        body{{background:#000;color:white;font-family:Arial;margin:0;padding:15px;}}
       .header{{text-align:center;padding:10px;}}
       .header h1{{font-family:'Broadway',Impact;letter-spacing:4px;font-size:50px;color:white;margin:0;}}
       .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px;margin-top:15px;}}
       .card{{background:#0a0a0a;border:1px solid #1a1a1a;border-radius:12px;padding:12px;}}
       .news-img{{width:100%;height:180px;object-fit:cover;border-radius:8px;}}
       .news-title{{font-family:'Broadway',Impact;font-size:18px;color:white;margin:10px 0;}}
       .icon-btn{{background:white;color:black;border:none;width:28px;height:28px;border-radius:50%;cursor:pointer;}}
       .full-text{{display:none;color:#888;background:#111;padding:10px;border-radius:8px;margin-top:10px;}}
       .full-text.show{{display:block;}}
    </style><script>function toggleText(id){{document.getElementById('full-'+id).classList.toggle('show');}}</script>
    </head><body><div class="header"><h1>NAVYUG WORLD</h1></div><div class="grid">{cards}</div></body></html>"""

class NavyugWorldBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NAVYUG WORLD")
        self.setGeometry(100,100,1250,800)
        self.setStyleSheet("QMainWindow{background:black;} QToolBar{background:#000;border:none;spacing:10px;} QLineEdit{background:#111;color:white;border:1px solid #222;border-radius:18px;padding:8px 15px;}")
        
        self.browser = QWebEngineView()
        self.browser.setHtml(get_home_html())
        self.setCentralWidget(self.browser)

        nav = QToolBar()
        self.addToolBar(nav)
        nav.addAction("⌂ Home", lambda: self.browser.setHtml(get_home_html()))
        nav.addAction("👤 Profile", self.go_profile)
        nav.addAction("💙 About Inventor", self.go_about)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText(" Search anything... ")
        self.url_bar.returnPressed.connect(self.do_search)
        nav.addWidget(self.url_bar)
        
        self.browser.loadFinished.connect(self.hide_google)

    def do_search(self):
        q = self.url_bar.text().strip()
        if not q: return
        if "." in q and " " not in q and len(q) > 3:
            url = q if q.startswith("http") else "https://" + q
            self.browser.setUrl(QUrl(url))
        else:
            self.browser.setUrl(QUrl("https://www.google.com/search?q=" + q.replace(" ", "+")))

    def hide_google(self):
        js = """
        try {
            let style = document.createElement('style');
            style.innerHTML = `body{background:#000 !important;color:white !important;} header,#top_nav,#searchform,.logo,#logo,form[role='search']{display:none !important;} #center_col,#main{background:#000 !important;} a{color:#38bdf8 !important;} .g{background:#0a0a0a !important;border:1px solid #1a1a1a !important;border-radius:12px !important;padding:15px !important;margin-bottom:15px !important;}`;
            document.head.appendChild(style);
            if(!document.getElementById('navyug-ai-bar')){
                let bar=document.createElement('div'); bar.id='navyug-ai-bar';
                bar.innerHTML="🤖 NAVYUG WORLD AI - Result";
                bar.style.cssText="position:fixed;top:0;left:0;width:100%;background:#111;border-bottom:1px solid #222;color:white;padding:12px 20px;z-index:99999;font-family:Arial;";
                document.body.prepend(bar); document.body.style.paddingTop="50px";
            }
        } catch(e) {}
        """
        self.browser.page().runJavaScript(js)

    def go_profile(self):
        html = """
        <html><body style="background:black;color:white;font-family:Arial;padding:40px;">
        <div style="max-width:700px;margin:auto;background:#0a0a0a;border:1px solid #222;padding:30px;border-radius:20px;">
            <h1 style="font-family:'Broadway',Impact;text-align:center;">👤 PROFILE</h1><hr style="border-color:#222;">
            <p><b>Browser:</b> NAVYUG WORLD</p>
            <p><b>Version:</b> 1.0 Black Edition</p>
            <p><b>User:</b> Navyug (Admin - 10 Years Old)</p>
            <p><b>Engine:</b> Python + PyQt5</p>
            <p><b>Status:</b> Private & Secure 🔒</p>
            <br><p style="color:#666;">All data is hidden and private. Only you can see it.</p>
        </div></body></html>
        """
        self.browser.setHtml(html)

    def go_about(self):
        html = """
        <html><body style="background:black;color:white;font-family:Arial;padding:40px;">
        <div style="max-width:800px;margin:auto;background:#0a0a0a;border:1px solid #38bdf8;padding:40px;border-radius:20px;">
            <h1 style="font-family:'Broadway',Impact;font-size:38px;text-align:center;color:#38bdf8;">ABOUT THE INVENTOR</h1><hr style="border-color:#222;">
            <p style="font-size:18px;line-height:1.9;text-align:justify;color:#ccc;">
            Hello, my name is Navyug and I am 10 years old. From my childhood, I had a deep passion and strong determination in my heart to learn coding, especially Python programming. I always dreamed of creating something big and useful for the world with my own hands. I did not want to just use browsers made by others, I wanted to build my own browser, and that dream became NAVYUG WORLD. This browser is the result of my hard work, curiosity and love for technology. In this beautiful journey, my father was my biggest strength. He always supported me, he never scolded me and he never stopped me from learning. Instead, he guided me, helped me when I was stuck in errors and encouraged me to never give up. My father taught me that age does not matter if your passion is true. I am just 10, but I believe I can make many more apps and browsers in the future. NAVYUG WORLD is just the beginning of my coding journey, and I dedicate this browser to my father and to all young dreamers like me who want to code and create their own world.
            </p>
            <p style="color:#facc15;text-align:center;margin-top:20px;font-weight:bold;">- Navyug, Founder of NAVYUG WORLD 🌍</p>
        </div></body></html>
        """
        self.browser.setHtml(html)

app = QApplication(sys.argv)
window = NavyugWorldBrowser()
window.show()
sys.exit(app.exec_())