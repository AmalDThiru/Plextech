import json
from flask import Flask
import os
from flask import request
from reset_data import reset
import uuid
import time

Reviews = []

@app.route("/pleets/<pleet_id>", methods=["DELETE"])
def delete_review(review_id):
    index = 0
    for review in Reviews:
        # index += 1
        if review["_id"] == review_id:
            Reviews.remove(review)
            update()
            return {"message": "Review succesfully deleted"}, 200
    return {"message": "Review not found!"}, 404


@app.route("/users/<user_id>", methods=["PUT"])
def put_review(review_id):
    data = request.json
    for review in Reviews:
        if review["_id"] == review_id:
            review["display name"] = data["display name"]
            update()
            return {"message": "User Profile Successfully edited!"}, 200
    return {"message": "User not found!"}, 404






