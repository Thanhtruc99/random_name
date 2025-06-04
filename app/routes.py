from flask import Blueprint, render_template, request, session
import random

from .data_loader import load_names, load_surnames
from .generator import generate_name, build_markov_model, generate_surname

main = Blueprint("main", __name__)


@main.route("/")
def index():
    genre = request.args.get("genre", "mixte")
    count = int(request.args.get("nombre", 10))
    court = request.args.get("court") is not None
    long_ = request.args.get("long") is not None
    voyelle = request.args.get("voyelle") is not None
    court_nom = request.args.get("court_nom") is not None
    long_nom = request.args.get("long_nom") is not None
    voyelle_nom = request.args.get("voyelle_nom") is not None
    prenoms = session.get("prenoms", ["—"] * count)
    noms = session.get("noms", ["—"] * count)
    names = [f"{p} {n}" for p, n in zip(prenoms, noms)]
    return render_template(
        "index.html",
        names=names,
        genre=genre,
        count=count,
        court=court,
        long=long_,
        voyelle=voyelle,
        court_nom=court_nom,
        long_nom=long_nom,
        voyelle_nom=voyelle_nom,
    )

@main.route("/generer_prenoms")
def generer_prenoms():
    genre = request.args.get("genre", "mixte")
    count = int(request.args.get("nombre", 10))
    court = request.args.get("court") is not None
    long_ = request.args.get("long") is not None
    voyelle = request.args.get("voyelle") is not None
    court_nom = request.args.get("court_nom") is not None
    long_nom = request.args.get("long_nom") is not None
    voyelle_nom = request.args.get("voyelle_nom") is not None
    raw_corpus = load_names(genre)
    model = build_markov_model(raw_corpus)

    def filtrer(prenom):
        if court and not (3 <= len(prenom) <= 5):
            return False
        if long_ and not (len(prenom) >= 6):
            return False
        if voyelle and prenom[-1].lower() not in "aeiouy":
            return False
        return True

    prenoms = []
    while len(prenoms) < count:
        p = generate_name(model)
        if filtrer(p):
            prenoms.append(p)

    noms = session.get("noms", ["—"] * count)
    session["prenoms"] = prenoms
    session["noms"] = noms
    session["genre"] = genre
    names = [f"{p} {n}" for p, n in zip(prenoms, noms)]
    return render_template(
        "index.html",
        names=names,
        genre=genre,
        count=count,
        court=court,
        long=long_,
        voyelle=voyelle,
        court_nom=court_nom,
        long_nom=long_nom,
        voyelle_nom=voyelle_nom,
    )

@main.route("/generer_noms")
def generer_noms():
    count = int(request.args.get("nombre", 10))
    court = request.args.get("court") is not None
    long_ = request.args.get("long") is not None
    voyelle = request.args.get("voyelle") is not None
    court_nom = request.args.get("court_nom") is not None
    long_nom = request.args.get("long_nom") is not None
    voyelle_nom = request.args.get("voyelle_nom") is not None

    def filtrer_nom(nom):
        if court_nom and not (3 <= len(nom) <= 5):
            return False
        if long_nom and not (len(nom) >= 6):
            return False
        if voyelle_nom and nom[-1].lower() not in "aeiouy":
            return False
        return True

    noms = []
    while len(noms) < count:
        n = generate_surname()
        if filtrer_nom(n):
            noms.append(n)

    prenoms = session.get("prenoms", ["—"] * count)
    genre = session.get("genre", "mixte")
    session["prenoms"] = prenoms
    session["noms"] = noms
    names = [f"{p} {n}" for p, n in zip(prenoms, noms)]
    return render_template(
        "index.html",
        names=names,
        genre=genre,
        count=count,
        court=court,
        long=long_,
        voyelle=voyelle,
        court_nom=court_nom,
        long_nom=long_nom,
        voyelle_nom=voyelle_nom,
    )

@main.route("/generer_tout")
def generer_tout():
    genre = request.args.get("genre", "mixte")
    count = int(request.args.get("nombre", 10))
    court = request.args.get("court") is not None
    long_ = request.args.get("long") is not None
    voyelle = request.args.get("voyelle") is not None
    court_nom = request.args.get("court_nom") is not None
    long_nom = request.args.get("long_nom") is not None
    voyelle_nom = request.args.get("voyelle_nom") is not None
    raw_corpus = load_names(genre)
    model = build_markov_model(raw_corpus)

    def filtrer_nom(nom):
        if court_nom and not (3 <= len(nom) <= 5):
            return False
        if long_nom and not (len(nom) >= 6):
            return False
        if voyelle_nom and nom[-1].lower() not in "aeiouy":
            return False
        return True

    def filtrer(prenom):
        if court and not (3 <= len(prenom) <= 5):
            return False
        if long_ and not (len(prenom) >= 7):
            return False
        if voyelle and prenom[-1].lower() not in "aeiouy":
            return False
        return True

    prenoms = []
    while len(prenoms) < count:
        p = generate_name(model)
        if filtrer(p):
            prenoms.append(p)

    noms = []
    while len(noms) < count:
        n = generate_surname()
        if filtrer_nom(n):
            noms.append(n)

    session["prenoms"] = prenoms
    session["noms"] = noms
    session["genre"] = genre
    session["count"] = count
    names = [f"{p} {n}" for p, n in zip(prenoms, noms)]
    return render_template(
        "index.html",
        names=names,
        genre=genre,
        count=count,
        court=court,
        long=long_,
        voyelle=voyelle,
        court_nom=court_nom,
        long_nom=long_nom,
        voyelle_nom=voyelle_nom,
    )