from flask import (
    Flask, redirect, render_template, request, flash
)

from contacts_model import Contact

Contact.load_db()

# ========================================================
# Flask App
# ========================================================

app = Flask(__name__)

app.secret_key = b'hypermedia rocks'


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    search = request.args.get("q")
    if search:
        contacts = Contact.search(search)
    else:
        contacts = Contact.all()
    return render_template("index.html", contacts=contacts)


@app.route("/contacts/new", methods=['POST', 'GET'])
def contacts_new():
    if request.method == 'POST':
        c = Contact(None, request.form['first_name'], request.form['last_name'], request.form['phone'],
                    request.form['email'])
        c.save()
        flash("Created New Contact!")
        return redirect("/contacts")
    else:
        return render_template("new.html")


@app.route("/contacts/<contact_id>")
def contacts_view(contact_id=0):
    contact = Contact.find(contact_id)
    return render_template("show.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["POST", "GET"])
def contacts_edit(contact_id=0):
    contact = Contact.find(contact_id)
    if request.method == 'POST':
        contact.update(request.form['first_name'], request.form['last_name'], request.form['phone'],
                       request.form['email'])
        flash("Updated Contact!")
        return redirect("/contacts/" + str(contact_id))
    else:
        return render_template("edit.html", contact=contact)


@app.route("/contacts/<contact_id>/delete", methods=["POST"])
def contacts_delete(contact_id=0):
    contact = Contact.find(contact_id)
    contact.delete()
    flash("Deleted Contact!")
    return redirect("/contacts")


if __name__ == "__main__":
    app.run()
