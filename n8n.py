{
  "name": "My workflow",
  "nodes": [
    {
      "parameters": {
        "formTitle": "Registration",
        "formFields": {
          "values": [
            {
              "fieldLabel": "User_Name"
            },
            {
              "fieldLabel": "User_Email",
              "fieldType": "email"
            },
            {
              "fieldLabel": "Mobile_Number",
              "fieldType": "number"
            },
            {
              "fieldLabel": "Gender",
              "fieldType": "radio",
              "fieldOptions": {
                "values": [
                  {
                    "option": "Male"
                  },
                  {
                    "option": "Female"
                  }
                ]
              }
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.formTrigger",
      "typeVersion": 2.5,
      "position": [
        0,
        0
      ],
      "id": "98b063de-32a5-453a-bfc4-3873ac1df91d",
      "name": "On form submission",
      "webhookId": "0fc3bcc7-0acb-40de-965b-8fbe8151d569"
    },
    {
      "parameters": {
        "operation": "append",
        "documentId": {
          "__rl": true,
          "value": "12BnQeDWhibcfoHJpkWaGcLH51QGxoVYe1eipYdQ90m0",
          "mode": "list",
          "cachedResultName": "D10_registrations",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/12BnQeDWhibcfoHJpkWaGcLH51QGxoVYe1eipYdQ90m0/edit?usp=drivesdk"
        },
        "sheetName": {
          "__rl": true,
          "value": "gid=0",
          "mode": "list",
          "cachedResultName": "N8n_workflow",
          "cachedResultUrl": "https://docs.google.com/spreadsheets/d/12BnQeDWhibcfoHJpkWaGcLH51QGxoVYe1eipYdQ90m0/edit#gid=0"
        },
        "columns": {
          "mappingMode": "autoMapInputData",
          "value": {},
          "matchingColumns": [],
          "schema": [],
          "attemptToConvertTypes": false,
          "convertFieldsToString": false
        },
        "options": {}
      },
      "type": "n8n-nodes-base.googleSheets",
      "typeVersion": 4.7,
      "position": [
        208,
        0
      ],
      "id": "c47277d8-c696-47ce-8850-fb1cc68ce575",
      "name": "Append row in sheet",
      "credentials": {
        "googleSheetsOAuth2Api": {
          "id": "vAIl0zteX1AdJP2Q",
          "name": "Google Sheets account"
        }
      }
    },
    {
      "parameters": {
        "sendTo": "={{ $json.User_Email }}",
        "subject": "N8n_registration",
        "message": "=n8n_regisrtation successfully {{ $json.User_Name }}",
        "options": {}
      },
      "type": "n8n-nodes-base.gmail",
      "typeVersion": 2.2,
      "position": [
        496,
        0
      ],
      "id": "4f6b701d-5097-4895-94f5-5f1869548f14",
      "name": "Send a message",
      "webhookId": "a0aad1c8-5909-4129-a6a9-ef97106b41dc",
      "credentials": {
        "gmailOAuth2": {
          "id": "CLh9Zmi1JmsWVbv2",
          "name": "Gmail account"
        }
      }
    }
  ],
  "pinData": {},
  "connections": {
    "On form submission": {
      "main": [
        [
          {
            "node": "Append row in sheet",
            "type": "main",
            "index": 0
          },
          {
            "node": "Send a message",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1",
    "binaryMode": "separate",
    "availableInMCP": false
  },
  "versionId": "ef3e8276-1eb3-49a2-9880-d138f674ffe2",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "585fd230445415f1e7a1ffe01fd58043c0920cc77cc621493011a39dd1ce7b2e"
  },
  "id": "RsrRvqEEiHlUGPmS",
  "tags": []
}