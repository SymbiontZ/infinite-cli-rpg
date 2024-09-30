DATA_SCHEME = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Scheme for the data of infinite-cli-rpg",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "difficulty": {
      "type": "number"
    },
    "level": {
      "type": "number"
    },
    "stats": {
      "type": "object",
      "properties": {
        "base": {
          "type": "object",
          "properties": {
            "hp": {
              "type": "number"
            },
            "atk": {
              "type": "number"
            },
            "def": {
              "type": "number"
            }
          },
          "required": [
            "hp",
            "atk",
            "def"
          ]
        },
        "gained": {
          "type": "object",
          "properties": {
            "hp": {
              "type": "number"
            },
            "atk": {
              "type": "number"
            },
            "def": {
              "type": "number"
            }
          },
          "required": [
            "hp",
            "atk",
            "def"
          ]
        }
      },
      "required": [
        "base",
        "gained"
      ]
    },
    "items": {
      "type": "array",
      "items": []
    }
  },
  "required": [
    "name",
    "difficulty",
    "level",
    "stats",
    "items"
  ]
}