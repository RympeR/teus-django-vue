
"""
    @api {POST} /api/user/create-profile/ 1.1 Login / authorize
    @apiName 1.2 Login / authorize
    @apiGroup User
    @apiParam {String} phone User phone number
    @apiParam {String} first_name User first name (not required)
    @apiParam {String} last_name User last name (not required)
    @apiParam {String} company User company (not required)
    @apiParam {String} image User avatar file (not required)
    @apiParam {String} code Code from sms (not required)

    @apiSuccess {String} status ok or error
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "status": "ok",
        "token": "5d337cbe8657d42515363e15cc2c9e3a720a77118d8fef54ee677d8e706f89d4"
    }
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 202 Accepted
    {
        "user": [
            "This phone is not confirmed, we sent SMS with a confirmation code"
        ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "error"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 500 Not Found
    {
        "code": [
            "The code is incorrect or expired"
        ]
    }
"""

"""
    @api {GET} /api/user/api-profile-get/ 1.3 Get user
    @apiName 1.3 Get user
    @apiGroup User
    @apiHeader {String} Authorization Users unique token


    @apiSuccess {Number} user_id User id
    @apiSuccess {String} first_name User first name
    @apiSuccess {String} last_name User last name
    @apiSuccess {String} image User avatar image
    @apiSuccess {String} company User company

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "user_id": 2,
        "phone": "09303943493",
        "image": "http://api-teus.maximusapp.com/media/test_Xj5iHa6.jpg",
        "first_name": "test",
        "last_name": "test",
        "company": "test"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }

"""


"""
    @api {PUT} /api/user/api-profile-update/ 1.4 Update user
    @apiName 1.4 Update user
    @apiGroup User
    @apiHeader {String} Authorization Users unique token

    @apiParam {String} phone User phone number
    @apiParam {String} code User code from sms
    @apiParam {String} first_name User first name (not required)
    @apiParam {String} last_name User last name (not required)
    @apiParam {String} company User company (not required)
    @apiParam {object} image User avatar file

    @apiSuccess {Number} user_id User id
    @apiSuccess {String} first_name User first name
    @apiSuccess {String} last_name User last name
    @apiSuccess {String} image User avatar image
    @apiSuccess {String} company User company

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "user_id": 1,
        "image": "http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg",
        "phone": "wefewf",
        "first_name": "test1",
        "last_name": "tset",
        "company": "test"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/containers/get-apidoc-api-proposition/ 2.0 Get user propositions
    @apiName 2.0 Get user propositions
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} limit Pagination limit (not required)
    @apiParam {Number} offset Pagination offset (not required)
    @apiParam {Boolean} is_active 1 or 0(not required)
    

    @apiSuccess {Object} proposition objects list
    @apiSuccess {Number} id Proposition id
    @apiSuccess {Object} user User object
    @apiSuccess {Object} city city objects list
    @apiSuccess {Object} container Container object
    @apiSuccess {Object} line Line object
    @apiSuccess {Number} request_date Request date timestamp 
    @apiSuccess {Number} end_date End date timestamp 


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
        {
            "id": 1,
            "user": {
                "id": 3,
                "name": "test2",
                "phone": "03495345455",
                "image": null
            },
            "amount": 7,
            "city": [
                {
                    "id": 1,
                    "name": "test"
                },
                {
                    "id": 2,
                    "name": "retwh"
                }
            ],
            "container": {
                "id": 2,
                "name": "34t34t",
                "image": "http://api-teus.maximusapp.com/media/testF_iNKjXSm.jpg"
            },
            "line": {
                "id": 1,
                "name": "test loe"
            },
            "start_date": 1615410000.0,
            "end_date": 1615410000.0
        }
    ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }
"""
"""
    @api {GET} /api/containers/proposition-list/ 2.1 Get propositions
    @apiName 2.1 Get propositions
    @apiGroup Propositions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} limit Pagination limit (not required)
    @apiParam {Number} offset Pagination offset (not required)
    @apiParam {id} id Request id to filter (not required)

    @apiSuccess {Object} results result objects list
    @apiSuccess {Number} id Proposition id
    @apiSuccess {Object} user User object
    @apiSuccess {Object} city city objects list
    @apiSuccess {Object} container Container object
    @apiSuccess {Object} line Line object
    @apiSuccess {Number} amount Request amount 
    @apiSuccess {Number} request_date Request date timestamp 
    @apiSuccess {Object} date End date timestamp 
    @apiSuccess {Number} start_date End date timestamp 
    @apiSuccess {Number} end_date End date timestamp 


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 1,
                "user": {
                    "id": 1,
                    "name": "test1",
                    "image": "http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg"
                },
                "line": {
                    "id": 1,
                    "name": "test loe"
                },
                "city": {
                    "id": 1,
                    "name": "test"
                },
                "container": {
                    "id": 1,
                    "name": "t34t",
                    "image": "http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg"
                },
                "amount": 3,
                "date": {
                    "start_date": 1615410000,
                    "end_date": 1615410000
                }
            },
            {
                "id": 6,
                "user": {
                    "id": 1,
                    "name": "test1",
                    "image": "http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg"
                },
                "line": {
                    "id": 1,
                    "name": "test loe"
                },
                "city": {
                    "id": 2,
                    "name": "retwh"
                },
                "amount": 2,
                "container": {
                    "id": 1,
                    "name": "t34t",
                    "image": "http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg"
                },
                "date": {
                    "start_date": 1615410000,
                    "end_date": 1583096400
                }
            }
        ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }

"""

"""
    @api {POST} /api/containers/create-api-proposition/ 2.2 Create user proposition
    @apiName 2.2 Create user proposition
    @apiGroup Propositions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} container Container id
    @apiParam {Object} city Array of city id's
    @apiParam {Number} line Line id
    @apiParam {Number} amount amount int
    @apiParam {Number} start_date timestamp format
    @apiParam {Number} end_date timestamp format

    @apiSuccess {Number} id Reques id

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 2
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {PUT} /api/containers/update-api-proposition/ 2.3 Update user proposition
    @apiName 2.3 Update user proposition
    @apiGroup Propositions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} id Proposition id
    @apiParam {Number} container Container id
    @apiParam {Number} city City id
    @apiParam {Number} line Line id
    @apiParam {Number} amount amount int
    @apiParam {Number} start_date timestamp format
    @apiParam {Number} end_date timestamp format

    @apiSuccess {Number} id Reques id

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 2
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/containers/get-proposition/{proposition_id}/ 2.4 Get user proposition by id
    @apiName 2.4 Get user proposition by id
    @apiGroup Propositions
    @apiHeader {String} Authorization Users unique token

    @apiSuccess {Number} id Proposition id
    @apiSuccess {Number} amount Containers amount
    @apiSuccess {Object} user User object
    @apiSuccess {Object} city city objects list
    @apiSuccess {Object} container Container object
    @apiSuccess {Object} line Line object
    @apiSuccess {Number} start_date Request date timestamp 
    @apiSuccess {Number} end_date End date timestamp 


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "user": {
            "id": 1,
            "name": "test46655",
            "phone": "094093409"
        },
        "amount": 5,
        "city": {
            "id": 1,
            "name": "test23"
        },
        "container": {
            "id": 1,
            "name": "tests5"
        },
        "line": {
            "id": 1,
            "name": "test277"
        },
        "start_date": 1615410000.0,
        "end_date": 1615410000.0
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {PUT} /api/containers/mark-proposition-status/ 2.5 Mark proposition status by id
    @apiName 3.5 Mark proposition status by id
    @apiGroup Propositions
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} id Proposition id
    @apiParam {String} status Proposition status one of в работе | в архиве | удален

    @apiSuccess {Number} id Request id
    @apiSuccess {String} status Proposition status


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "status": "в архиве"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/containers/get-apidoc-api-request/ 3.1 Get user requests
    @apiName 3.1 Get user requests
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} limit Pagination limit (not required)
    @apiParam {Number} offset Pagination offset (not required)
    @apiParam {Boolean} is_active 1 or 0(not required)
    

    @apiSuccess {Object} results result objects list
    @apiSuccess {Number} id Request id
    @apiSuccess {Object} user User object
    @apiSuccess {Object} city city objects list
    @apiSuccess {Object} container Container object
    @apiSuccess {Object} line Line object
    @apiSuccess {Number} request_date Request date timestamp 
    @apiSuccess {Number} end_date End date timestamp 


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
        {
            "id": 1,
            "user": {
                "id": 3,
                "name": "test2",
                "phone": "03495345455",
                "image": null
            },
            "amount": 7,
            "city": [
                {
                    "id": 1,
                    "name": "test"
                },
                {
                    "id": 2,
                    "name": "retwh"
                }
            ],
            "container": {
                "id": 2,
                "name": "34t34t",
                "image": "http://api-teus.maximusapp.com/media/testF_iNKjXSm.jpg"
            },
            "line": {
                "id": 1,
                "name": "test loe"
            },
            "request_date": 1615410000.0,
            "end_date": 1615410000.0
        }
    ]
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 Not Found
    {
        "status": "invalid token"
    }
"""

"""
    @api {POST} /api/containers/create-api-request/ 3.2 Create user requests
    @apiName 3.2 Create user requests
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} container Container id
    @apiParam {Object} city Array of city id's
    @apiParam {Number} line Line id
    @apiParam {Number} amount amount int
    @apiParam {Number} request_date timestamp format
    @apiParam {Number} end_date timestamp format

    @apiSuccess {Number} id Reques id

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 2
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {PUT} /api/containers/update-api-request/ 3.3 Update user request
    @apiName 3.3 Update user request
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} container Container id
    @apiParam {Object} city Array of city id's
    @apiParam {Number} line Line id
    @apiParam {Number} amount amount int
    @apiParam {Number} request_date timestamp format
    @apiParam {Number} end_date timestamp format

    @apiSuccess {Number} id Reques id

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 2
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/containers/get-request/{request_id}/ 3.4 Get user request by id
    @apiName 3.4 Get user request by id
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiSuccess {Number} id Request id
    @apiSuccess {Number} amount Containers amount
    @apiSuccess {Object} user User object
    @apiSuccess {Object} city city objects list
    @apiSuccess {Object} container Container object
    @apiSuccess {Object} line Line object
    @apiSuccess {Number} request_date Request date timestamp 
    @apiSuccess {Number} end_date End date timestamp 


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "user": {
            "id": 1,
            "name": "test46655",
            "phone": "094093409"
        },
        "amount": 5,
        "city": {
            "id": 1,
            "name": "test23"
        },
        "container": {
            "id": 1,
            "name": "tests5"
        },
        "line": {
            "id": 1,
            "name": "test277"
        },
        "request_date": 1615410000.0,
        "end_date": 1615410000.0
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {PUT} /api/containers/mark-request-status/ 3.5 Mark request status by id
    @apiName 3.5 Mark request status by id
    @apiGroup Requests
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} id Request id
    @apiParam {String} status Request status one of в работе | в архиве | удален

    @apiSuccess {Number} id Request id
    @apiSuccess {String} status Proposition status


    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "status": "в архиве"
    }
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/info/get-containers-list-api/ 4.1 Get containers    
    @apiName 4.1 Get containers
    @apiGroup Info
    @apiSuccess {object} results Containers list
    @apiSuccess {Number} id container id
    @apiSuccess {String} name container name
    @apiSuccess {String} image container image
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
        {
            [
                {
                    "id": 1,
                    "name": "test",
                    "image": "http://api-teus.maximusapp.com/media/tes_img.jpg"
                },
            ]
        }
"""

"""
    @api {GET} /api/info/get-cities-list-api/ 4.2 Get cities    
    @apiName 4.2 Get cities
    @apiGroup Info
    @apiSuccess {object} results Cities list
    @apiSuccess {Number} id city id
    @apiSuccess {String} name city name
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 1,
                "name": "test"
            },
            {
                "id": 2,
                "name": "test2"
            },
        ]
    }
"""
"""
    @api {GET} /api/info/get-lines-list-api/ 4.3 Get lines    
    @apiName 4.3 Get containers
    @apiGroup Info
    @apiSuccess {object} results Lines list
    @apiSuccess {Number} id line id
    @apiSuccess {String} name line name
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 1,
                "name": "test"
            },
            {
                "id": 2,
                "name": "test2"
            },
        ]
    }
"""


"""
    @api {POST} /api/chat/create-room/ 5.1 Create room    
    @apiName 5.1 Create room
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} request_id Id of request
    @apiParam {Number} proposition_id Id of proposition

    @apiSuccess {number} id room id
    @apiSuccess {Number} date datetime of creating room timestamp
    @apiSuccess {boolean} first_mark handshake first mark
    @apiSuccess {boolean} second_mark handshake second mark
    @apiSuccess {Number} request_id Id of request
    @apiSuccess {Number} proposition_id Id of proposition

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 6,
        "date": 1615979863.412638,
        "first_mark": false,
        "second_mark": false,
        "request_id": 2,
        "proposition_id": 2
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {PUT} /api/chat/update-room/{int:pk} 5.2 Update room    
    @apiName 5.2 Update room
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Room id
    @apiParam {Number} request_id Id of request
    @apiParam {Number} proposition_id Id of proposition
    
    @apiSuccess {number} id room id
    @apiSuccess {Number} date datetime of creating room timestamp
    @apiSuccess {boolean} first_mark handshake first mark
    @apiSuccess {boolean} second_mark handshake second mark
    @apiSuccess {Number} request_id Id of request
    @apiSuccess {Number} proposition_id Id of proposition

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 6,
        "date": 1615979863.412638,
        "first_mark": false,
        "second_mark": false,
        "request_id": 2,
        "proposition_id": 2
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {DELETE} /api/chat/delete-room/{int:pk} 5.3 Delete room    
    @apiName 5.3 Delete room
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Room id

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 204 No Content
    {
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {POST} /api/chat/create-message/ 5.4 Create message    
    @apiName 5.4 Create message
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} room Id of room
    @apiParam {Number} user Id of user
    @apiParam {String} text messgge text (not required)
    @apiParam {object} attachment File attachment (not required)

    @apiSuccess {number} id message id
    @apiSuccess {Number} date datetime of creating room timestamp
    @apiSuccess {boolean} text text message ( can be null )
    @apiSuccess {boolean} attachment attachemnt file link ( can be null )
    @apiSuccess {Number} room Id of room
    @apiSuccess {Number} user Id of sender user

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 2,
        "date": 1615911583.265012,
        "text": null,
        "attachment": "http://api-teus.maximusapp.com/media/PHZ_0733_XRWHViz.jpg",
        "room": 4,
        "user": 2
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/chat/messages/{int:pk} 5.5 Get messages in chat
    @apiName 5.5 Get messages in chat
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Room id
    @apiParam {Number} limit Messages Limit ( not required )
    @apiParam {Number} offset Messages offset ( not required )

    @apiSuccess {object} results list of message objects

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 2,
                "room_id": 4,
                "user_id": 2,
                "text": null,
                "attachment": "http://api-teus.maximusapp.com/media/PHZ_0733_XRWHViz.jpg",
                "date": 1615845600.0
            },
            {
                "id": 1,
                "room_id": 4,
                "user_id": 1,
                "text": "teste",
                "attachment": null,
                "date": 1615845600.0
            }
        ]
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/chat/rooms-request/{int:pk} 5.6 Get chats by request id
    @apiName 5.6 Get chats by request id
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Request id

    @apiSuccess {object} results list of chat objects

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 7,
                "line": {
                    "name": "testl2"
                },
                "contianer": {
                    "name": "test24",
                    "image": "http://127.0.0.1:8000/media/Ellipse_10.png"
                },
                "user_request": {
                    "id": 1,
                    "first_name": "admin",
                    "last_name": "admin",
                    "image": null
                },
                "user_proposition": {
                    "id": 1,
                    "first_name": "admin",
                    "last_name": "admin",
                    "image": null
                },
                "user_request_id": 6,
                "user_proposition_id": 9,
                "date": 1618572308,
                "first_mark": false,
                "second_mark": false
            }
        ]
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {GET} /api/chat/rooms-proposition/{int:pk} 5.6 Get chats by proposition id
    @apiName 5.6 Get chats by proposition id
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Proposition id

    @apiSuccess {object} results list of chat objects

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        [
            {
                "id": 7,
                "line": {
                    "name": "testl2"
                },
                "contianer": {
                    "name": "test24",
                    "image": "http://127.0.0.1:8000/media/Ellipse_10.png"
                },
                "user_request": {
                    "id": 1,
                    "first_name": "admin",
                    "last_name": "admin",
                    "image": null
                },
                "user_proposition": {
                    "id": 1,
                    "first_name": "admin",
                    "last_name": "admin",
                    "image": null
                },
                "user_request_id": 6,
                "user_proposition_id": 9,
                "date": 1618572308,
                "first_mark": false,
                "second_mark": false
            }
        ]
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""

"""
    @api {POST} ws://api/chat/ws/chat/{int:room_name}/ 5.7 Send message ( works with sockets )
    @apiName 5.7 Send message
    @apiGroup Chat

    @apiParam {Number} room room id
    @apiParam {String} message message text or empty string ''
    @apiParam {Number} user user id 
    @apiParam {Number} file id of message with file attachment or None
"""

"""
    @api {PUT} /api/chat/handshake/{int:pk} 5.8 Handshake
    @apiName 5.8 Handshake
    @apiGroup Chat
    @apiHeader {String} Authorization Users unique token

    @apiParam {Number} pk Room id
    @apiParam {Number} handshake First or second user (1 | 2)<- values

    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 but needs handshake
    {
        "status": "needs second handshake"
    }
    @apiSuccessExample {json} Success-Response:
    HTTP/1.1 200 OK
    {
        "success": 200,
        "status": "processed"
    }
    
    @apiErrorExample {json} Error-Response:
    HTTP/1.1 200 without token
    {
        "status": "invalid token"
    }
"""
