from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler

check_in_route_bp = Blueprint("check_in_route", __name__)

@check_in_route_bp.route("/attendees/<attendee_id>/check-in", methods=["POST"])
def create_check_in(attendee_id):
    check_in_handler = CheckInHandler()
    Http_request = HttpRequest(param={"attendee_id": attendee_id })
    http_response = check_in_handler.registry(Http_request)

    return jsonify(http_response.body), http_response.status_code