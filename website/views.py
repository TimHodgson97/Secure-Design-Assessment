from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Service, Upgrade, Repair, Safety
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        service = request.form.get('service')
        upgrade = request.form.get('upgrade')
        repair = request.form.get('repair')
        safety = request.form.get('safety')


        if note:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Opperational Check added!', category='success')
        elif service:
            new_service = Service(data=service, user_id=current_user.id)
            db.session.add(new_service)
            db.session.commit()
            flash('Service Record added!', category='success')
        elif upgrade:
            new_upgrade = Upgrade(data=upgrade, user_id=current_user.id)
            db.session.add(new_upgrade)
            db.session.commit()
            flash('Software Upgrade added!', category='success')
        elif repair:
            new_repair = Repair(data=repair, user_id=current_user.id)
            db.session.add(new_repair)
            db.session.commit()
            flash('Vessel Repair added!', category='success')
        elif safety:
            new_safety = Safety(data=safety, user_id=current_user.id)
            db.session.add(new_safety)
            db.session.commit()
            flash('Vessel Safety Inspection added!', category='success')
        else:
            flash('Input not valid!', category='error')


    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Opperational Check deleted!', category='success')

    return jsonify({})

@views.route('/delete-service', methods=['POST'])
def delete_service():
    service = json.loads(request.data)
    serviceId = service['serviceId']
    service = Service.query.get(serviceId)
    if service:
        if service.user_id == current_user.id:
            db.session.delete(service)
            db.session.commit()
            flash('Service record deleted!', category='success')

    return jsonify({})

@views.route('/delete-upgrade', methods=['POST'])
def delete_upgrade():
    upgrade = json.loads(request.data)
    upgradeId = upgrade['upgradeId']
    upgrade = Upgrade.query.get(upgradeId)
    if upgrade:
        if upgrade.user_id == current_user.id:
            db.session.delete(upgrade)
            db.session.commit()
            flash('Software Upgrade record deleted!', category='success')

    return jsonify({})

@views.route('/delete-repair', methods=['POST'])
def delete_repair():
    repair = json.loads(request.data)
    repairId = repair['repairId']
    repair = Repair.query.get(repairId)
    if repair:
        if repair.user_id == current_user.id:
            db.session.delete(repair)
            db.session.commit()
            flash('Vessel Repair deleted!', category='success')

    return jsonify({})

@views.route('/delete-safety', methods=['POST'])
def delete_safety():
    safety = json.loads(request.data)
    safetyId = safety['serviceId']
    safety = Safety.query.get(safetyId)
    if safety:
        if safety.user_id == current_user.id:
            db.session.delete(safety)
            db.session.commit()
            flash('Vessel Safety Inspection deleted!', category='success')

    return jsonify({})