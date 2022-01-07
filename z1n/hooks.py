from . import __version__ as app_version

app_name = "z1n"
app_title = "Z1N"
app_publisher = "Zirrus One"
app_description = "Find Your Peace. Find Your Z1N."
app_icon = "octicon octicon-rocket"
app_color = "blue"
app_email = "z1n@zirrusone.com"
app_license = "MIT"

website_context = {
    "favicon": "/assets/z1n/images/z1n-favicon.png",
    "splash_image": "/assets/z1n/images/z1n-logo.png"
}

after_migrate = ["z1n.after_migrate.install.execute"]
home_page = "login"

# include js, css files in header of desk.html
app_include_css = "/assets/z1n/css/z1n.css"

web_include_css = "/assets/css/z1n_website.css"


# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "z1n/public/scss/website"

fixtures = [
    {"dt": "Workspace Menus"}
]