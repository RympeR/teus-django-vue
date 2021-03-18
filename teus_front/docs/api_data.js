define({ "api": [
  {
    "type": "POST",
    "url": "/api/chat/create-room/",
    "title": "5.1 Create room",
    "name": "5.1_Create_room",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "request_id",
            "description": "<p>Id of request</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "proposition_id",
            "description": "<p>Id of proposition</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "number",
            "optional": false,
            "field": "id",
            "description": "<p>room id</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "date",
            "description": "<p>datetime of creating room timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "first_mark",
            "description": "<p>handshake first mark</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "second_mark",
            "description": "<p>handshake second mark</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "request_id",
            "description": "<p>Id of request</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "proposition_id",
            "description": "<p>Id of proposition</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 6,\n    \"date\": 1615979863.412638,\n    \"first_mark\": false,\n    \"second_mark\": false,\n    \"request_id\": 2,\n    \"proposition_id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "PUT",
    "url": "/api/chat/update-room/{int:pk}",
    "title": "5.2 Update room",
    "name": "5.2_Update_room",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Room id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "request_id",
            "description": "<p>Id of request</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "proposition_id",
            "description": "<p>Id of proposition</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "number",
            "optional": false,
            "field": "id",
            "description": "<p>room id</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "date",
            "description": "<p>datetime of creating room timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "first_mark",
            "description": "<p>handshake first mark</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "second_mark",
            "description": "<p>handshake second mark</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "request_id",
            "description": "<p>Id of request</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "proposition_id",
            "description": "<p>Id of proposition</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 6,\n    \"date\": 1615979863.412638,\n    \"first_mark\": false,\n    \"second_mark\": false,\n    \"request_id\": 2,\n    \"proposition_id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "DELETE",
    "url": "/api/chat/delete-room/{int:pk}",
    "title": "5.3 Delete room",
    "name": "5.3_Delete_room",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Room id</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 204 No Content\n{\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "POST",
    "url": "/api/chat/create-message/",
    "title": "5.4 Create message",
    "name": "5.4_Create_message",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "room",
            "description": "<p>Id of room</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user",
            "description": "<p>Id of user</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "text",
            "description": "<p>messgge text (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "object",
            "optional": false,
            "field": "attachment",
            "description": "<p>File attachment (not required)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "number",
            "optional": false,
            "field": "id",
            "description": "<p>message id</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "date",
            "description": "<p>datetime of creating room timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "text",
            "description": "<p>text message ( can be null )</p>"
          },
          {
            "group": "Success 200",
            "type": "boolean",
            "optional": false,
            "field": "attachment",
            "description": "<p>attachemnt file link ( can be null )</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "room",
            "description": "<p>Id of room</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "user",
            "description": "<p>Id of sender user</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2,\n    \"date\": 1615911583.265012,\n    \"text\": null,\n    \"attachment\": \"http://api-teus.maximusapp.com/media/PHZ_0733_XRWHViz.jpg\",\n    \"room\": 4,\n    \"user\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "GET",
    "url": "api/chat/messages/{int:pk}",
    "title": "5.5 Get messages in chat",
    "name": "5.5_Get_messages_in_chat",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Room id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>list of message objects</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n     \"results\": [\n        {\n            \"id\": 2,\n            \"room_id\": 4,\n            \"user_id\": 2,\n            \"text\": null,\n            \"attachment\": \"http://api-teus.maximusapp.com/media/PHZ_0733_XRWHViz.jpg\",\n            \"date\": 1615845600.0\n        },\n        {\n            \"id\": 1,\n            \"room_id\": 4,\n            \"user_id\": 1,\n            \"text\": \"teste\",\n            \"attachment\": null,\n            \"date\": 1615845600.0\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "GET",
    "url": "api/chat/rooms-proposition/{int:pk}",
    "title": "5.6 Get chats by proposition id",
    "name": "5.6_Get_chats_by_proposition_id",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Proposition id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>list of chat objects</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n        {\n            \"id\": 4,\n            \"user_request_id\": 1,\n            \"user_proposition_id\": 1,\n            \"date\": 1615845600.0,\n            \"first_mark\": false,\n            \"second_mark\": false\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "GET",
    "url": "api/chat/rooms-request/{int:pk}",
    "title": "5.6 Get chats by request id",
    "name": "5.6_Get_chats_by_request_id",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Request id</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>list of chat objects</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n        {\n            \"id\": 4,\n            \"user_request_id\": 1,\n            \"user_proposition_id\": 1,\n            \"date\": 1615845600.0,\n            \"first_mark\": false,\n            \"second_mark\": false\n        }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "POST",
    "url": "ws://api/chat/ws/chat/{int:room_name}/",
    "title": "5.7 Send message ( works with sockets )",
    "name": "5.7_Send_message",
    "group": "Chat",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "room",
            "description": "<p>room id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>message text</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user",
            "description": "<p>user id</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "PUT",
    "url": "/api/chat/handshake/{int:pk}",
    "title": "5.8 Handshake",
    "name": "5.8_Handshake",
    "group": "Chat",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "pk",
            "description": "<p>Room id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "handshake",
            "description": "<p>First or second user (1 | 2)&lt;- values</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 but needs handshake\n{\n    \"status\": \"needs second handshake\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"success\": 200,\n    \"status\": \"processed\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Chat"
  },
  {
    "type": "GET",
    "url": "/api/info/get-containers-list/",
    "title": "4.1 Get containers",
    "name": "4.1_Get_containers",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>Containers list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>container id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>container name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>container image</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n    {\n    \"results\": [\n        {\n            \"id\": 1,\n            \"name\": \"test\",\n            \"image\": \"http://api-teus.maximusapp.com/media/tes_img.jpg\"\n        },\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-cities-list/",
    "title": "4.2 Get cities",
    "name": "4.2_Get_cities",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>Cities list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>city id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>city name</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n        {\n            \"id\": 1,\n            \"name\": \"test\"\n        },\n        {\n            \"id\": 2,\n            \"name\": \"test2\"\n        },\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/info/get-lines-list/",
    "title": "4.3 Get lines",
    "name": "4.3_Get_containers",
    "group": "Info",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "object",
            "optional": false,
            "field": "results",
            "description": "<p>Lines list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>line id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>line name</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n        {\n            \"id\": 1,\n            \"name\": \"test\"\n        },\n        {\n            \"id\": 2,\n            \"name\": \"test2\"\n        },\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Info"
  },
  {
    "type": "GET",
    "url": "/api/containers/proposition-list/",
    "title": "2.1 Get propositions",
    "name": "2.1_Get_propositions",
    "group": "Propositions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "limit",
            "description": "<p>Pagination limit (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "offset",
            "description": "<p>Pagination offset (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "id",
            "optional": false,
            "field": "id",
            "description": "<p>Request id to filter (not required)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "results",
            "description": "<p>result objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Proposition id</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "user",
            "description": "<p>User object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>city objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "container",
            "description": "<p>Container object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "line",
            "description": "<p>Line object</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "request_date",
            "description": "<p>Request date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "date",
            "description": "<p>End date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "start_date",
            "description": "<p>End date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date timestamp</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n\"results\": [\n    {\n        \"id\": 1,\n        \"user\": {\n            \"id\": 1,\n            \"name\": \"test1\",\n            \"image\": \"http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg\"\n        },\n        \"line\": {\n            \"id\": 1,\n            \"name\": \"test loe\"\n        },\n        \"city\": {\n            \"id\": 1,\n            \"name\": \"test\"\n        },\n        \"container\": {\n            \"id\": 1,\n            \"name\": \"t34t\",\n            \"image\": \"http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg\"\n        },\n        \"date\": {\n            \"start_date\": 1615410000.0,\n            \"end_date\": 1615410000.0\n        }\n    },\n    {\n        \"id\": 6,\n        \"user\": {\n            \"id\": 1,\n            \"name\": \"test1\",\n            \"image\": \"http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg\"\n        },\n        \"line\": {\n            \"id\": 1,\n            \"name\": \"test loe\"\n        },\n        \"city\": {\n            \"id\": 2,\n            \"name\": \"retwh\"\n        },\n        \"container\": {\n            \"id\": 1,\n            \"name\": \"t34t\",\n            \"image\": \"http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg\"\n        },\n        \"date\": {\n            \"start_date\": 1615410000.0,\n            \"end_date\": 1583096400.0\n        }\n    }\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Propositions"
  },
  {
    "type": "POST",
    "url": "/api/containers/create-api-proposition/",
    "title": "2.2 Create user proposition",
    "name": "2.2_Create_user_proposition",
    "group": "Propositions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "container",
            "description": "<p>Container id</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>Array of city id's</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "line",
            "description": "<p>Line id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>amount int</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "start_date",
            "description": "<p>timestamp format</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>timestamp format</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Reques id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Propositions"
  },
  {
    "type": "PUT",
    "url": "/api/containers/update-api-proposition/",
    "title": "2.3 Update user proposition",
    "name": "2.3_Update_user_proposition",
    "group": "Propositions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Proposition id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "container",
            "description": "<p>Container id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "city",
            "description": "<p>City id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "line",
            "description": "<p>Line id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>amount int</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "start_date",
            "description": "<p>timestamp format</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>timestamp format</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Reques id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Propositions"
  },
  {
    "type": "GET",
    "url": "/api/containers/get-proposition/{proposition_id}/",
    "title": "2.4 Get user proposition by id",
    "name": "2.4_Get_user_proposition_by_id",
    "group": "Propositions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Proposition id</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>Containers amount</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "user",
            "description": "<p>User object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>city objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "container",
            "description": "<p>Container object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "line",
            "description": "<p>Line object</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "start_date",
            "description": "<p>Request date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date timestamp</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"user\": {\n        \"id\": 1,\n        \"name\": \"test46655\",\n        \"phone\": \"094093409\"\n    },\n    \"amount\": 5,\n    \"city\": {\n        \"id\": 1,\n        \"name\": \"test23\"\n    },\n    \"container\": {\n        \"id\": 1,\n        \"name\": \"tests5\"\n    },\n    \"line\": {\n        \"id\": 1,\n        \"name\": \"test277\"\n    },\n    \"start_date\": 1615410000.0,\n    \"end_date\": 1615410000.0\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Propositions"
  },
  {
    "type": "PUT",
    "url": "/api/containers/mark-proposition-status/",
    "title": "2.5 Mark proposition status by id",
    "name": "3.5_Mark_proposition_status_by_id",
    "group": "Propositions",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Proposition id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>Proposition status one of в работе | в архиве | удален</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Request id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>Proposition status</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"status\": \"в архиве\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Propositions"
  },
  {
    "type": "GET",
    "url": "/api/containers/get-api-request/",
    "title": "3.1 Get user requests",
    "name": "3.1_Get_user_requests",
    "group": "Requests",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "limit",
            "description": "<p>Pagination limit (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "offset",
            "description": "<p>Pagination offset (not required)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "results",
            "description": "<p>result objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Request id</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "user",
            "description": "<p>User object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>city objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "container",
            "description": "<p>Container object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "line",
            "description": "<p>Line object</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "request_date",
            "description": "<p>Request date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date timestamp</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"results\": [\n    {\n        \"id\": 1,\n        \"user\": {\n            \"id\": 3,\n            \"name\": \"test2\",\n            \"phone\": \"03495345455\",\n            \"image\": null\n        },\n        \"amount\": 7,\n        \"city\": [\n            {\n                \"id\": 1,\n                \"name\": \"test\"\n            },\n            {\n                \"id\": 2,\n                \"name\": \"retwh\"\n            }\n        ],\n        \"container\": {\n            \"id\": 2,\n            \"name\": \"34t34t\",\n            \"image\": \"http://api-teus.maximusapp.com/media/testF_iNKjXSm.jpg\"\n        },\n        \"line\": {\n            \"id\": 1,\n            \"name\": \"test loe\"\n        },\n        \"request_date\": 1615410000.0,\n        \"end_date\": 1615410000.0\n    }\n]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Requests"
  },
  {
    "type": "POST",
    "url": "/api/containers/create-api-request/",
    "title": "3.2 Create user requests",
    "name": "3.2_Create_user_requests",
    "group": "Requests",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "container",
            "description": "<p>Container id</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>Array of city id's</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "line",
            "description": "<p>Line id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>amount int</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "request_date",
            "description": "<p>timestamp format</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>timestamp format</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Reques id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Requests"
  },
  {
    "type": "PUT",
    "url": "/api/containers/update-api-request/",
    "title": "3.3 Update user request",
    "name": "3.3_Update_user_request",
    "group": "Requests",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "container",
            "description": "<p>Container id</p>"
          },
          {
            "group": "Parameter",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>Array of city id's</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "line",
            "description": "<p>Line id</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>amount int</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "request_date",
            "description": "<p>timestamp format</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>timestamp format</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Reques id</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 2\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Requests"
  },
  {
    "type": "GET",
    "url": "/api/containers/get-request/{request_id}/",
    "title": "3.4 Get user request by id",
    "name": "3.4_Get_user_request_by_id",
    "group": "Requests",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Request id</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "amount",
            "description": "<p>Containers amount</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "user",
            "description": "<p>User object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "city",
            "description": "<p>city objects list</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "container",
            "description": "<p>Container object</p>"
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "line",
            "description": "<p>Line object</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "request_date",
            "description": "<p>Request date timestamp</p>"
          },
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "end_date",
            "description": "<p>End date timestamp</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"user\": {\n        \"id\": 1,\n        \"name\": \"test46655\",\n        \"phone\": \"094093409\"\n    },\n    \"amount\": 5,\n    \"city\": {\n        \"id\": 1,\n        \"name\": \"test23\"\n    },\n    \"container\": {\n        \"id\": 1,\n        \"name\": \"tests5\"\n    },\n    \"line\": {\n        \"id\": 1,\n        \"name\": \"test277\"\n    },\n    \"request_date\": 1615410000.0,\n    \"end_date\": 1615410000.0\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Requests"
  },
  {
    "type": "PUT",
    "url": "/api/containers/mark-request-status/",
    "title": "3.5 Mark request status by id",
    "name": "3.5_Mark_request_status_by_id",
    "group": "Requests",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Request id</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>Request status one of в работе | в архиве | удален</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Request id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>Proposition status</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"id\": 1,\n    \"status\": \"в архиве\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 without token\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "Requests"
  },
  {
    "type": "POST",
    "url": "/api/user/login/",
    "title": "1.2 Login",
    "name": "1.2_Login",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>User phone number</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "company",
            "description": "<p>User company (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar file</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>Code from sms (not required)</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "status",
            "description": "<p>ok or error</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": \"ok\",\n    \"token\": \"5d337cbe8657d42515363e15cc2c9e3a720a77118d8fef54ee677d8e706f89d4\"\n}",
          "type": "json"
        },
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 202 Accepted\n{\n    \"user\": [\n        \"This phone is not confirmed, we sent SMS with a confirmation code\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"error\"\n}",
          "type": "json"
        },
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 500 Not Found\n{\n    \"code\": [\n        \"The code is incorrect or expired\"\n    ]\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  },
  {
    "type": "GET",
    "url": "/api/user/api-profile-get/",
    "title": "1.3 Get user",
    "name": "1.3_Get_user",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "user_id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar image</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "company",
            "description": "<p>User company</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"user_id\": 2,\n    \"phone\": \"09303943493\",\n    \"image\": \"http://api-teus.maximusapp.com/media/test_Xj5iHa6.jpg\",\n    \"first_name\": \"test\",\n    \"last_name\": \"test\",\n    \"company\": \"test\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  },
  {
    "type": "PUT",
    "url": "/api/user/update-user/",
    "title": "1.4 Update user",
    "name": "1.4_Update_user",
    "group": "User",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Users unique token</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "phone",
            "description": "<p>User phone number</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>User code from sms</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "company",
            "description": "<p>User company (not required)</p>"
          },
          {
            "group": "Parameter",
            "type": "object",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar file</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "user_id",
            "description": "<p>User id</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "first_name",
            "description": "<p>User first name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "last_name",
            "description": "<p>User last name</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "image",
            "description": "<p>User avatar image</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "company",
            "description": "<p>User company</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"user_id\": 1,\n    \"image\": \"http://api-teus.maximusapp.com/media/kotik_JDk7Aog.jpg\",\n    \"phone\": \"wefewf\",\n    \"first_name\": \"test1\",\n    \"last_name\": \"tset\",\n    \"company\": \"test\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "examples": [
        {
          "title": "Error-Response:",
          "content": "HTTP/1.1 200 Not Found\n{\n    \"status\": \"invalid token\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "apidoc/rules.py",
    "groupTitle": "User"
  }
] });
