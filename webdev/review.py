from flask import Flask, render_template, request, session, redirect, url_for, flash

import random
import time

import data

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("reviews"))

    
@app.route("/review")
def reviews():
    return render_template("submit.html", the_title="Please enter your login")

@app.route("/processgame", methods=["POST"])
def process_game():
    gameName = request.form["the_name"]
    gamestudio = request.form["the_studio"]
    gamegenre = request.form["the_genre"]
    gamerelease= request.form["the_releasedate"]
    data.add_game(gameName,gamestudio,gamegenre,gamerelease)
    return redirect(url_for("display_leaderboard"))

@app.route("/gamereviews")
def display_leaderboard():
    gameData = data.get_reviews()
    return render_template("showgames.html" , the_title="Games Table",
        the_data =gameData,)

@app.route("/processreview", methods=["POST"])
def process_game_review():

    
    noOfLikes = request.form["the_name"]
    noOfDisLikes = request.form["the_studio"]
    ranks = request.form["the_genre"]
    comments= request.form["the_releasedate"]

    
    data.add_review(noOfLikes,noOfDisLikes,ranks,comments)
    return redirect(url_for("display_leaderboard"))
