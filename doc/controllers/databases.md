# Databases

Databases represent collections of Notion pages that can be [sorted](https://developers.notion.com/reference/post-database-query-sort) and [queried](https://developers.notion.com/reference/post-database-query). Each database will have a schema (or properties) that represent the columns in the database table. Notion offers several types of properties, as described in the [official documentation](https://developers.notion.com/reference/property-object).

These database-related endpoints allow developers to work with databases programmatically by [creating](https://developers.notion.com/reference/create-a-database), [retrieving](https://developers.notion.com/reference/retrieve-a-database), and [updating](https://developers.notion.com/reference/update-a-database) them.

To learn more, read [Notion’s official documentation](https://developers.notion.com/reference/database) for endpoints related to databases. We also recommend reading the official Notion guide for [working with databases](https://developers.notion.com/docs/working-with-page-content).

```python
databases_controller = client.databases
```

## Class Name

`DatabasesController`

## Methods

* [Retrieve a Database](../../doc/controllers/databases.md#retrieve-a-database)
* [Update Database Properties](../../doc/controllers/databases.md#update-database-properties)
* [Filter a Database](../../doc/controllers/databases.md#filter-a-database)
* [Create a Database](../../doc/controllers/databases.md#create-a-database)


# Retrieve a Database

Retrieves a database object using the ID specified in the request path.

```python
def retrieve_a_database(self,
                       id,
                       notion_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `notion_version` | `str` | Header, Optional | - |

## Response Type

`Any`

## Example Usage

```python
id = '{{DATABASE_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = databases_controller.retrieve_a_database(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "database",
  "id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae",
  "cover": null,
  "icon": null,
  "created_time": "2021-04-27T20:38:00.000Z",
  "created_by": {
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
  },
  "last_edited_by": {
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
  },
  "last_edited_time": "2022-02-24T22:14:00.000Z",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Ever Better Reading List Title",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Ever Better Reading List Title",
      "href": null
    }
  ],
  "properties": {
    "Score /5": {
      "id": ")Y7%22",
      "name": "Score /5",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
            "name": "⭐️⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "9b1e1349-8e24-40ba-bbca-84a61296bc81",
            "name": "⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
            "name": "⭐️⭐️",
            "color": "default"
          },
          {
            "id": "d3782c76-0396-467f-928e-46bf0c9d5fba",
            "name": "⭐️",
            "color": "default"
          }
        ]
      }
    },
    "Type": {
      "id": "%2F7eo",
      "name": "Type",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
            "name": "Article",
            "color": "default"
          },
          {
            "id": "4ac85597-5db1-4e0a-9c02-445575c38f76",
            "name": "TV Series",
            "color": "default"
          },
          {
            "id": "2991748a-5745-4c3b-9c9b-2d6846a6fa1f",
            "name": "Film",
            "color": "default"
          },
          {
            "id": "82f3bace-be25-410d-87fe-561c9c22492f",
            "name": "Podcast",
            "color": "default"
          },
          {
            "id": "861f1076-1cc4-429a-a781-54947d727a4a",
            "name": "Academic Journal",
            "color": "default"
          },
          {
            "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
            "name": "Essay Resource",
            "color": "default"
          }
        ]
      }
    },
    "Publisher": {
      "id": "%3E%24Pb",
      "name": "Publisher",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
            "name": "NYT",
            "color": "default"
          },
          {
            "id": "1b9b0c0c-17b0-4292-ad12-1364a51849de",
            "name": "Netflix",
            "color": "blue"
          },
          {
            "id": "f3533637-278f-4501-b394-d9753bf3c101",
            "name": "Indie",
            "color": "brown"
          },
          {
            "id": "e70d713c-4be4-4b40-a44d-fb413c8b9d7e",
            "name": "Bon Appetit",
            "color": "yellow"
          },
          {
            "id": "9c2bd667-0a10-4be4-a044-35a537a14ab9",
            "name": "Franklin Institute",
            "color": "pink"
          },
          {
            "id": "6849b5f0-e641-4ec5-83cb-1ffe23011060",
            "name": "Springer",
            "color": "orange"
          },
          {
            "id": "6a5bff63-a72d-4464-a5d0-1a601af2adf6",
            "name": "Emerald Group",
            "color": "gray"
          },
          {
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
          }
        ]
      }
    },
    "Summary": {
      "id": "%3F%5C25",
      "name": "Summary",
      "type": "rich_text",
      "rich_text": {}
    },
    "Publishing/Release Date": {
      "id": "%3Fex%2B",
      "name": "Publishing/Release Date",
      "type": "date",
      "date": {}
    },
    "Link": {
      "id": "VVMi",
      "name": "Link",
      "type": "url",
      "url": {}
    },
    "Read": {
      "id": "_MWJ",
      "name": "Read",
      "type": "checkbox",
      "checkbox": {}
    },
    "Status": {
      "id": "%60zz5",
      "name": "Status",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
            "name": "Ready to Start",
            "color": "yellow"
          },
          {
            "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
            "name": "Reading",
            "color": "red"
          },
          {
            "id": "59aa9043-07b4-4bf4-8734-3164b13af44a",
            "name": "Finished",
            "color": "blue"
          },
          {
            "id": "f961978d-02eb-4998-933a-33c2ec378564",
            "name": "Listening",
            "color": "red"
          },
          {
            "id": "1d450853-b27a-45e2-979f-448aa1bd35de",
            "name": "Watching",
            "color": "red"
          }
        ]
      }
    },
    "Author": {
      "id": "qNw_",
      "name": "Author",
      "type": "multi_select",
      "multi_select": {
        "options": [
          {
            "id": "15592971-7b30-43d5-9406-2eb69b13fcae",
            "name": "Spencer Greenberg",
            "color": "default"
          },
          {
            "id": "b80a988e-dccf-4f74-b764-6ca0e49ed1b8",
            "name": "Seth Stephens-Davidowitz",
            "color": "default"
          },
          {
            "id": "0e71ee06-199d-46a4-834c-01084c8f76cb",
            "name": "Andrew Russell",
            "color": "default"
          },
          {
            "id": "5807ec38-4879-4455-9f30-5352e90e8b79",
            "name": "Lee Vinsel",
            "color": "default"
          },
          {
            "id": "4cf10a64-f3da-449c-8e04-ce6e338bbdbd",
            "name": "Megan Greenwell",
            "color": "default"
          },
          {
            "id": "833e2c78-35ed-4601-badc-50c323341d76",
            "name": "Kara Swisher",
            "color": "default"
          },
          {
            "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
            "name": "Paul Romer",
            "color": "default"
          },
          {
            "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
            "name": "Karen Swallow Prior",
            "color": "default"
          },
          {
            "id": "da068e78-dfe2-4434-9fd7-b7450b3e5830",
            "name": "Judith Shulevitz",
            "color": "default"
          }
        ]
      }
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "page_id",
    "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
  },
  "url": "https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae",
  "archived": false
}
```


# Update Database Properties

```python
def update_database_properties(self,
                              id,
                              notion_version=None,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `notion_version` | `str` | Header, Optional | - |
| `body` | `Any` | Body, Optional | - |

## Response Type

`Any`

## Example Usage

```python
id = '{{DATABASE_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = databases_controller.update_database_properties(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "database",
  "id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae",
  "cover": null,
  "icon": null,
  "created_time": "2021-04-27T20:38:00.000Z",
  "created_by": {
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
  },
  "last_edited_by": {
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617"
  },
  "last_edited_time": "2022-02-24T22:08:00.000Z",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Ever Better Reading List Title",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Ever Better Reading List Title",
      "href": null
    }
  ],
  "properties": {
    "Score /5": {
      "id": ")Y7\"",
      "name": "Score /5",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
            "name": "⭐️⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "9b1e1349-8e24-40ba-bbca-84a61296bc81",
            "name": "⭐️⭐️⭐️",
            "color": "default"
          },
          {
            "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
            "name": "⭐️⭐️",
            "color": "default"
          },
          {
            "id": "d3782c76-0396-467f-928e-46bf0c9d5fba",
            "name": "⭐️",
            "color": "default"
          }
        ]
      }
    },
    "Type": {
      "id": "/7eo",
      "name": "Type",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
            "name": "Article",
            "color": "default"
          },
          {
            "id": "4ac85597-5db1-4e0a-9c02-445575c38f76",
            "name": "TV Series",
            "color": "default"
          },
          {
            "id": "2991748a-5745-4c3b-9c9b-2d6846a6fa1f",
            "name": "Film",
            "color": "default"
          },
          {
            "id": "82f3bace-be25-410d-87fe-561c9c22492f",
            "name": "Podcast",
            "color": "default"
          },
          {
            "id": "861f1076-1cc4-429a-a781-54947d727a4a",
            "name": "Academic Journal",
            "color": "default"
          },
          {
            "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
            "name": "Essay Resource",
            "color": "default"
          }
        ]
      }
    },
    "Publisher": {
      "id": ">$Pb",
      "name": "Publisher",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
            "name": "NYT",
            "color": "default"
          },
          {
            "id": "1b9b0c0c-17b0-4292-ad12-1364a51849de",
            "name": "Netflix",
            "color": "blue"
          },
          {
            "id": "f3533637-278f-4501-b394-d9753bf3c101",
            "name": "Indie",
            "color": "brown"
          },
          {
            "id": "e70d713c-4be4-4b40-a44d-fb413c8b9d7e",
            "name": "Bon Appetit",
            "color": "yellow"
          },
          {
            "id": "9c2bd667-0a10-4be4-a044-35a537a14ab9",
            "name": "Franklin Institute",
            "color": "pink"
          },
          {
            "id": "6849b5f0-e641-4ec5-83cb-1ffe23011060",
            "name": "Springer",
            "color": "orange"
          },
          {
            "id": "6a5bff63-a72d-4464-a5d0-1a601af2adf6",
            "name": "Emerald Group",
            "color": "gray"
          },
          {
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
          }
        ]
      }
    },
    "Summary": {
      "id": "?\\25",
      "name": "Summary",
      "type": "rich_text",
      "rich_text": {}
    },
    "Publishing/Release Date": {
      "id": "?ex+",
      "name": "Publishing/Release Date",
      "type": "date",
      "date": {}
    },
    "Link": {
      "id": "VVMi",
      "name": "Link",
      "type": "url",
      "url": {}
    },
    "Wine Pairing": {
      "id": "Y=H]",
      "name": "Wine Pairing",
      "type": "rich_text",
      "rich_text": {}
    },
    "Read": {
      "id": "_MWJ",
      "name": "Read",
      "type": "checkbox",
      "checkbox": {}
    },
    "Status": {
      "id": "`zz5",
      "name": "Status",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
            "name": "Ready to Start",
            "color": "yellow"
          },
          {
            "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
            "name": "Reading",
            "color": "red"
          },
          {
            "id": "59aa9043-07b4-4bf4-8734-3164b13af44a",
            "name": "Finished",
            "color": "blue"
          },
          {
            "id": "f961978d-02eb-4998-933a-33c2ec378564",
            "name": "Listening",
            "color": "red"
          },
          {
            "id": "1d450853-b27a-45e2-979f-448aa1bd35de",
            "name": "Watching",
            "color": "red"
          }
        ]
      }
    },
    "Author": {
      "id": "qNw_",
      "name": "Author",
      "type": "multi_select",
      "multi_select": {
        "options": [
          {
            "id": "15592971-7b30-43d5-9406-2eb69b13fcae",
            "name": "Spencer Greenberg",
            "color": "default"
          },
          {
            "id": "b80a988e-dccf-4f74-b764-6ca0e49ed1b8",
            "name": "Seth Stephens-Davidowitz",
            "color": "default"
          },
          {
            "id": "0e71ee06-199d-46a4-834c-01084c8f76cb",
            "name": "Andrew Russell",
            "color": "default"
          },
          {
            "id": "5807ec38-4879-4455-9f30-5352e90e8b79",
            "name": "Lee Vinsel",
            "color": "default"
          },
          {
            "id": "4cf10a64-f3da-449c-8e04-ce6e338bbdbd",
            "name": "Megan Greenwell",
            "color": "default"
          },
          {
            "id": "833e2c78-35ed-4601-badc-50c323341d76",
            "name": "Kara Swisher",
            "color": "default"
          },
          {
            "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
            "name": "Paul Romer",
            "color": "default"
          },
          {
            "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
            "name": "Karen Swallow Prior",
            "color": "default"
          },
          {
            "id": "da068e78-dfe2-4434-9fd7-b7450b3e5830",
            "name": "Judith Shulevitz",
            "color": "default"
          }
        ]
      }
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "page_id",
    "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
  },
  "url": "https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae",
  "archived": false
}
```


# Filter a Database

```python
def filter_a_database(self,
                     id,
                     authorization=None,
                     notion_version=None,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `authorization` | `str` | Header, Optional | - |
| `notion_version` | `str` | Header, Optional | - |
| `body` | `str` | Body, Optional | - |

## Response Type

`Any`

## Example Usage

```python
id = '{{DATABASE_ID}}'

authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns'

notion_version = '{{NOTION_VERSION}}'

result = databases_controller.filter_a_database(
    id,
    authorization=authorization,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "list",
  "results": [
    {
      "object": "page",
      "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
      "created_time": "2021-04-27T20:38:00.000Z",
      "last_edited_time": "2021-05-12T06:07:00.000Z",
      "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "b7307e35-c80a-4cb5-bb6b-6054523b394a",
            "name": "⭐️⭐️⭐️⭐️",
            "color": "default"
          }
        },
        "Type": {
          "id": "%2F7eo",
          "type": "select",
          "select": {
            "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
            "name": "Article",
            "color": "default"
          }
        },
        "Publisher": {
          "id": "%3E%24Pb",
          "type": "select",
          "select": {
            "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
            "name": "NYT",
            "color": "default"
          }
        },
        "Summary": {
          "id": "%3F%5C25",
          "type": "rich_text",
          "rich_text": [
            {
              "type": "text",
              "text": {
                "content": "Some think chief ethics officers could help technology companies navigate political and social questions.",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Some think chief ethics officers could help technology companies navigate political and social questions.",
              "href": null
            }
          ]
        },
        "Publishing/Release Date": {
          "id": "%3Fex%2B",
          "type": "date",
          "date": {
            "start": "2018-10-21",
            "end": null,
            "time_zone": null
          }
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Read": {
          "id": "_MWJ",
          "type": "checkbox",
          "checkbox": true
        },
        "Status": {
          "id": "%60zz5",
          "type": "select",
          "select": {
            "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
            "name": "Reading",
            "color": "red"
          }
        },
        "Author": {
          "id": "qNw_",
          "type": "multi_select",
          "multi_select": [
            {
              "id": "833e2c78-35ed-4601-badc-50c323341d76",
              "name": "Kara Swisher",
              "color": "default"
            }
          ]
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Who Will Teach Silicon Valley to Be Ethical? ",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Who Will Teach Silicon Valley to Be Ethical? ",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/Who-Will-Teach-Silicon-Valley-to-Be-Ethical-a1712d5453e44893a69d4d581cd2c845"
    },
    {
      "object": "page",
      "id": "557ef501-bfdb-4586-918e-4434f31bca8c",
      "created_time": "2021-04-27T20:38:00.000Z",
      "last_edited_time": "2021-04-27T20:38:00.000Z",
      "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
      },
      "last_edited_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "66d3d050-086c-4a91-8c56-d55dc67e7789",
            "name": "⭐️⭐️",
            "color": "default"
          }
        },
        "Type": {
          "id": "%2F7eo",
          "type": "select",
          "select": {
            "id": "9cc30548-59d6-4cd3-94bc-d234081525c4",
            "name": "Essay Resource",
            "color": "default"
          }
        },
        "Publisher": {
          "id": "%3E%24Pb",
          "type": "select",
          "select": {
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
          }
        },
        "Summary": {
          "id": "%3F%5C25",
          "type": "rich_text",
          "rich_text": []
        },
        "Publishing/Release Date": {
          "id": "%3Fex%2B",
          "type": "date",
          "date": {
            "start": "2016-10-03",
            "end": null,
            "time_zone": null
          }
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.theatlantic.com/entertainment/archive/2016/03/how-jane-eyre-created-the-modern-self/460461/"
        },
        "Read": {
          "id": "_MWJ",
          "type": "checkbox",
          "checkbox": false
        },
        "Status": {
          "id": "%60zz5",
          "type": "select",
          "select": {
            "id": "5925ba22-0126-4b58-90c7-b8bbb2c3c895",
            "name": "Reading",
            "color": "red"
          }
        },
        "Author": {
          "id": "qNw_",
          "type": "multi_select",
          "multi_select": [
            {
              "id": "ae3a2cbe-1fc9-4376-be35-331628b34623",
              "name": "Karen Swallow Prior",
              "color": "default"
            }
          ]
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "Jane Eyre",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": true,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Jane Eyre",
              "href": null
            },
            {
              "type": "text",
              "text": {
                "content": " and the Invention of Self",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": " and the Invention of Self",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/Jane-Eyre-and-the-Invention-of-Self-557ef501bfdb4586918e4434f31bca8c"
    },
    {
      "object": "page",
      "id": "7ea694fa-93bb-43ba-b342-90a7706e55aa",
      "created_time": "2021-04-27T20:38:00.000Z",
      "last_edited_time": "2021-04-27T20:38:00.000Z",
      "created_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
      },
      "last_edited_by": {
        "object": "user",
        "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "8e2c2b76-9e1d-47d2-87b9-ed3035d607ae"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": null
        },
        "Type": {
          "id": "%2F7eo",
          "type": "select",
          "select": {
            "id": "f96d0d0a-5564-4a20-ab15-5f040d49759e",
            "name": "Article",
            "color": "default"
          }
        },
        "Publisher": {
          "id": "%3E%24Pb",
          "type": "select",
          "select": {
            "id": "c5ee409a-f307-4176-99ee-6e424fa89afa",
            "name": "NYT",
            "color": "default"
          }
        },
        "Summary": {
          "id": "%3F%5C25",
          "type": "rich_text",
          "rich_text": [
            {
              "type": "text",
              "text": {
                "content": "Putting a levy on targeted ad revenue would give Facebook and Google a real incentive to change their dangerous business models.",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "Putting a levy on targeted ad revenue would give Facebook and Google a real incentive to change their dangerous business models.",
              "href": null
            }
          ]
        },
        "Publishing/Release Date": {
          "id": "%3Fex%2B",
          "type": "date",
          "date": {
            "start": "2019-10-06",
            "end": null,
            "time_zone": null
          }
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2019/05/06/opinion/tax-facebook-google.html"
        },
        "Read": {
          "id": "_MWJ",
          "type": "checkbox",
          "checkbox": false
        },
        "Status": {
          "id": "%60zz5",
          "type": "select",
          "select": {
            "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
            "name": "Ready to Start",
            "color": "yellow"
          }
        },
        "Author": {
          "id": "qNw_",
          "type": "multi_select",
          "multi_select": [
            {
              "id": "82e594e2-b1c5-4271-ac19-1a723a94a533",
              "name": "Paul Romer",
              "color": "default"
            }
          ]
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "A Tax That Could Fix Big Tech ",
                "link": null
              },
              "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
              },
              "plain_text": "A Tax That Could Fix Big Tech ",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/A-Tax-That-Could-Fix-Big-Tech-7ea694fa93bb43bab34290a7706e55aa"
    }
  ],
  "next_cursor": null,
  "has_more": false
}
```


# Create a Database

```python
def create_a_database(self,
                     notion_version=None,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Optional | - |
| `body` | `str` | Body, Optional | - |

## Response Type

`Any`

## Example Usage

```python
notion_version = '{{NOTION_VERSION}}'

result = databases_controller.create_a_database(
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "database",
  "id": "23cde96c-0ad8-41d8-bfa2-b477c63dd52a",
  "cover": null,
  "icon": null,
  "created_time": "2022-02-24T22:06:00.000Z",
  "created_by": {
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617"
  },
  "last_edited_by": {
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617"
  },
  "last_edited_time": "2022-02-24T22:06:00.000Z",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Grocery List",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Grocery List",
      "href": null
    }
  ],
  "properties": {
    "Description": {
      "id": "%3EWW~",
      "name": "Description",
      "type": "rich_text",
      "rich_text": {}
    },
    "Last ordered": {
      "id": "O%5C%3BK",
      "name": "Last ordered",
      "type": "date",
      "date": {}
    },
    "In stock": {
      "id": "Pya%5C",
      "name": "In stock",
      "type": "checkbox",
      "checkbox": {}
    },
    "+1": {
      "id": "%5CSky",
      "name": "+1",
      "type": "people",
      "people": {}
    },
    "Photo": {
      "id": "dSrT",
      "name": "Photo",
      "type": "files",
      "files": {}
    },
    "Store availability": {
      "id": "jRd%3E",
      "name": "Store availability",
      "type": "multi_select",
      "multi_select": {
        "options": [
          {
            "id": "8e6441ee-8f17-4833-a2fe-68af5dced24f",
            "name": "Duc Loi Market",
            "color": "blue"
          },
          {
            "id": "64a9da77-9805-461f-9773-1e176fdbd203",
            "name": "Rainbow Grocery",
            "color": "gray"
          },
          {
            "id": "012d0436-66a1-4613-a1bd-314b1d1d059b",
            "name": "Nijiya Market",
            "color": "purple"
          },
          {
            "id": "63ab31f9-8cbd-4d02-8688-752376f455ea",
            "name": "Gus's Community Market",
            "color": "yellow"
          }
        ]
      }
    },
    "Food group": {
      "id": "q%5DO%5B",
      "name": "Food group",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "392af858-f42f-43ea-a171-7c0ca5c0a683",
            "name": "🥦Vegetable",
            "color": "green"
          },
          {
            "id": "df461a24-14c6-494a-8c61-55775fedbdcd",
            "name": "🍎Fruit",
            "color": "red"
          },
          {
            "id": "0ff22aaa-348e-4194-83c2-67a76dfb10fc",
            "name": "💪Protein",
            "color": "yellow"
          }
        ]
      }
    },
    "Price": {
      "id": "t%60jj",
      "name": "Price",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "page_id",
    "page_id": "c4d39556-6364-46a1-8a61-ebbb668f7445"
  },
  "url": "https://www.notion.so/23cde96c0ad841d8bfa2b477c63dd52a",
  "archived": false
}
```

