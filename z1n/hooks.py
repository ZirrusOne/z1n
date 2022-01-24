from . import __version__ as app_version

app_name = "z1n"
app_title = "Z1N"
app_publisher = "Zirrus One"
app_description = "Find Your Peace. Find Your Z1N."
app_icon = "octicon octicon-rocket"
app_color = "blue"
app_email = "z1n@zirrusone.com"
app_license = "MIT"
app_logo_url = "/assets/install_manager/images/z1n-logo.png"
website_context = {
    "favicon": "/assets/z1n/images/z1n-favicon.png",
    "splash_image": "/assets/z1n/images/z1n-logo.png"
}

after_migrate = ["z1n.after_migrate.install.execute"]
home_page = "login"

# include js, css files in header of desk.html
app_include_css = "/assets/css/z1n.css"

web_include_css = "/assets/css/z1n_website.css"

app_include_js = "/assets/js/z1n.js"

web_include_js = [
    "/assets/js/z1n_website.js"
]
