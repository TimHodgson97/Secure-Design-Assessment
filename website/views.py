from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Service, Upgrade, Repair, Safety
from . import db
import json

views = Blueprint('views', __name__)

#function for home page
@views.route('/', methods=['GET', 'POST'])
#require user to be logged in to see this
@login_required
def home():
    if request.method == 'POST':
        #set note, service, upgrade, repair and safety to be user input from forms
        note = request.form.get('note')
        service = request.form.get('service')
        upgrade = request.form.get('upgrade')
        repair = request.form.get('repair')
        safety = request.form.get('safety')

        #if a opperational note is made add to opperational checks database
        if note:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Opperational Check added!', category='success')
        #if a service note is made add to service records database
        elif service:
            new_service = Service(data=service, user_id=current_user.id)
            db.session.add(new_service)
            db.session.commit()
            flash('Service Record added!', category='success')
        #if an upgrade note is made add to software upgrade database
        elif upgrade:
            new_upgrade = Upgrade(data=upgrade, user_id=current_user.id)
            db.session.add(new_upgrade)
            db.session.commit()
            flash('Software Upgrade added!', category='success')
        #if a repair note is made add to vessel repair database
        elif repair:
            new_repair = Repair(data=repair, user_id=current_user.id)
            db.session.add(new_repair)
            db.session.commit()
            flash('Vessel Repair added!', category='success')
        #if a safety note is made add to safety inspaction database
        elif safety:
            new_safety = Safety(data=safety, user_id=current_user.id)
            db.session.add(new_safety)
            db.session.commit()
            flash('Vessel Safety Inspection added!', category='success')
        else:
            flash('Input not valid!', category='error')


    return render_template("home.html", user=current_user)


#function to delete opperational check note
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        #only allow specific user to delete note
        if note.user_id == current_user.id:
            #update db
            db.session.delete(note)
            db.session.commit()
            flash('Opperational Check deleted!', category='success')

    return jsonify({})

#function to delete service record note
@views.route('/delete-service', methods=['POST'])
def delete_service():
    service = json.loads(request.data)
    serviceId = service['serviceId']
    service = Service.query.get(serviceId)
    if service:
        #only allow specific user to delete note
        if service.user_id == current_user.id:
            #update db
            db.session.delete(service)
            db.session.commit()
            flash('Service record deleted!', category='success')

    return jsonify({})

#function to delete software upgrade note
@views.route('/delete-upgrade', methods=['POST'])
def delete_upgrade():
    upgrade = json.loads(request.data)
    upgradeId = upgrade['upgradeId']
    upgrade = Upgrade.query.get(upgradeId)
    if upgrade:
        #only allow specific user to delete note
        if upgrade.user_id == current_user.id:
            #update db
            db.session.delete(upgrade)
            db.session.commit()
            flash('Software Upgrade record deleted!', category='success')

    return jsonify({})

#function to delete vessel repair note
@views.route('/delete-repair', methods=['POST'])
def delete_repair():
    repair = json.loads(request.data)
    repairId = repair['repairId']
    repair = Repair.query.get(repairId)
    if repair:
        #only allow specific user to delete note
        if repair.user_id == current_user.id:
            #update db
            db.session.delete(repair)
            db.session.commit()
            flash('Vessel Repair deleted!', category='success')

    return jsonify({})

#function to delete safety inspection note
@views.route('/delete-safety', methods=['POST'])
def delete_safety():
    safety = json.loads(request.data)
    safetyId = safety['safetyId']
    safety = Safety.query.get(safetyId)
    if safety:
        #only allow specific user to delete note
        if safety.user_id == current_user.id:
            #update db
            db.session.delete(safety)
            db.session.commit()
            flash('Vessel Safety Inspection deleted!', category='success')

    return jsonify({})