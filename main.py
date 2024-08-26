from website import create_website
from flask import render_template

website = create_website()

@website.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    website.run(debug=True, host='0.0.0.0', port=5000)