from flask import Flask, request,jsonify
import pymysql
import json
import datetime
import Config.envConfig as envConfig
from flask_sqlalchemy import SQLAlchemy
from Models.models import *

application = app = Flask(__name__)

app.config.from_object(envConfig.Config)

db = SQLAlchemy(app)

# create new user
@app.route('/user',methods=['POST'])
def create_user():
    print("user called")
    data = request.get_json()
    print(data)
    if ( UserInfo.query.filter_by(user_id = data['user_id']).first()):
        response = {"status":"UserId Already Exists!!"}
    else:
        new_user = UserInfo(user_id = data['user_id'],
                            first_name = data['first_name'],
                            last_name = data['last_name'],
                            age = data['age'])

        db.session.add(new_user)
        db.session.commit()
        db.session.delete(new_user)
        
        response = {"status":"User Added"}
    return jsonify(response)

#Display all users
@app.route('/users',methods=['GET'])
def get_all_users():
    # all_users = UserInfo.query.order_by(Countries.country_name.asc()).all()
    all_users = UserInfo.query.order_by(UserInfo.user_id.asc()).all()
    if all_users :
        print(all_users)
        output = []
        for user in all_users:
            user_data = {}
            user_data['user_id'] = user.user_id
            user_data['user_name'] = user.first_name+" "+user.last_name
            user_data['age'] = user.age
            output.append(user_data)
        response = {"Data":output}
        return jsonify(response)
    else:
        response = {"status":"No Users in Database !!"}
        return jsonify(response)

# search user by id
@app.route('/searchbyid/<user_id>',methods=['GET'])
def get_user_by_id(user_id):
    user = UserInfo.query.filter_by(user_id = user_id).first()
    if user :
            user.user   
            return jsonify(response)
    else:
        response = {"message":"No user found !!"}
        return jsonify(response)
        

# get response by first_name , last_name or full name
@app.route('/search',methods=['POST'])
def get_user_by_name():
    data = request.get_json()
    name = data['user']
    searchname = name.split(" ")[0]
    print(searchname)

    all_users = UserInfo.query.filter_by(first_name = searchname).all()
    if all_users :
        output = []
        for user in all_users:
            user_data = {}
            user_data['user_id'] = user.user_id
            user_data['user_name'] = user.first_name+" "+user.last_name
            user_data['age'] = user.age
            output.append(user_data)
        response = {"Data":output}
        return jsonify(response)
    else:
        response = {"message":"No user found !!"}
        return jsonify(response)

# update user details by filtering on the basis of user_id
@app.route('/update',methods=['POST'])
def update_user_details():
    data = request.get_json()
    print(data)
    user_id = data['user_id']  
    
    update_user = UserInfo.query.filter_by(user_id = user_id).first()
    print(update_user)
    if update_user :
        print("Hello to update!!")
        update_user.first_name = data['first_name'] 
        update_user.last_name = data['last_name']
        update_user.age = data['age']
        db.session.commit()
        db.session.delete(update_user)
        response = {"Data":"Data updated succesfully!!"}
        return jsonify(response)
    else:
        response = {"message":"No user found !! You need to add the user !!"}
        return jsonify(response)


@app.route('/delete',methods=['PUT'])
def delete_user_by_id():
    data = request.get_json()
    user_id = data['user_id']
    user_to_delete = UserInfo.query.filter_by(user_id = user_id).first()
    if user_to_delete :
        db.session.delete(user_to_delete)
        db.session.commit()
        response = {"status":"Record Deleted!!"}
        return jsonify(response)
    else:
        response = {"status":"No Record found to delete"}
        return response
        
    

if __name__ == '__main__':
    app.run()






