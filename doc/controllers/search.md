# Search

Search all pages and databases shared with your Notion integration. To learn more, read Notion’s [official documentation](https://developers.notion.com/reference/post-search) for the Public API endpoints.

```python
search_controller = client.search
```

## Class Name

`SearchController`


# Search

```python
def search(self,
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

result = search_controller.search(
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
      "id": "ae1905c3-b77b-475b-b98f-7596c242137f",
      "created_time": "2021-05-21T16:41:00.000Z",
      "last_edited_time": "2021-05-21T16:41:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
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
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
                "bold": true,
                "italic": true,
                "strikethrough": true,
                "underline": true,
                "code": true,
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
            "start": "2020-12-08T12:00:00.000+00:00",
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-ae1905c3b77b475bb98f7596c242137f"
    },
    {
      "object": "page",
      "id": "8f16061d-4b77-4dbc-bf04-e8b0b4319b5a",
      "created_time": "2021-05-21T16:42:00.000Z",
      "last_edited_time": "2021-05-21T16:42:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
                "bold": true,
                "italic": true,
                "strikethrough": true,
                "underline": true,
                "code": true,
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-8f16061d4b774dbcbf04e8b0b4319b5a"
    },
    {
      "object": "page",
      "id": "dc2a9117-163d-4075-907e-604b2f04c504",
      "created_time": "2021-06-15T17:23:00.000Z",
      "last_edited_time": "2021-06-15T17:23:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-dc2a9117163d4075907e604b2f04c504"
    },
    {
      "object": "page",
      "id": "c443c084-4637-4df2-ba37-b3c8a7e3d062",
      "created_time": "2021-06-15T17:23:00.000Z",
      "last_edited_time": "2021-06-15T17:23:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-c443c08446374df2ba37b3c8a7e3d062"
    },
    {
      "object": "page",
      "id": "0ac85319-05c5-4b5b-b812-7ea0f6476ea0",
      "created_time": "2021-06-15T17:23:00.000Z",
      "last_edited_time": "2021-06-15T17:23:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-0ac8531905c54b5bb8127ea0f6476ea0"
    },
    {
      "object": "page",
      "id": "794fc25a-7f59-419d-a6e5-d9f0b516ecc7",
      "created_time": "2021-06-15T17:24:00.000Z",
      "last_edited_time": "2021-06-15T17:24:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-794fc25a7f59419da6e5d9f0b516ecc7"
    },
    {
      "object": "page",
      "id": "41ad30b7-98e7-4c55-bf21-7ac7f09c2fd5",
      "created_time": "2021-06-15T17:24:00.000Z",
      "last_edited_time": "2021-06-15T17:24:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
            "id": "b598e780-263b-4b02-862c-9bf7a91859ac",
            "name": "New Option",
            "color": "orange"
          }
        },
        "Author": {
          "id": "qNw_",
          "type": "multi_select",
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-41ad30b798e74c55bf217ac7f09c2fd5"
    },
    {
      "object": "page",
      "id": "6a313bae-fdd3-4617-9bd6-5b132f23be35",
      "created_time": "2021-06-15T17:24:00.000Z",
      "last_edited_time": "2021-06-15T17:24:00.000Z",
      "created_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "last_edited_by": {
        "object": "user",
        "id": "92a680bb-6970-4726-952b-4f4c03bff617"
      },
      "cover": null,
      "icon": null,
      "parent": {
        "type": "database_id",
        "database_id": "7a94f22f-59ae-484d-90ac-4aeddd667641"
      },
      "archived": false,
      "properties": {
        "Score /5": {
          "id": ")Y7%22",
          "type": "select",
          "select": {
            "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
            "name": "⭐️⭐️⭐️⭐️⭐️",
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
            "id": "01f82d08-aa1f-4884-a4e0-3bc32f909ec4",
            "name": "The Atlantic",
            "color": "red"
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
            "start": "2020-12-08T12:00:00.000+00:00",
            "end": null,
            "time_zone": null
          }
        },
        "date": {
          "id": "Lpwp",
          "type": "date",
          "date": null
        },
        "Link": {
          "id": "VVMi",
          "type": "url",
          "url": "https://www.nytimes.com/2018/10/21/opinion/who-will-teach-silicon-valley-to-be-ethical.html"
        },
        "Wine Pairing": {
          "id": "WO%40Z",
          "type": "rich_text",
          "rich_text": []
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
            "id": "ad038109-97d3-4b5d-a93a-3b88229b1b58",
            "name": "New Option 3",
            "color": "purple"
          }
        },
        "Author": {
          "id": "qNw_",
          "type": "multi_select",
          "multi_select": []
        },
        "Name": {
          "id": "title",
          "type": "title",
          "title": [
            {
              "type": "text",
              "text": {
                "content": "New Media Article",
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
              "plain_text": "New Media Article",
              "href": null
            }
          ]
        }
      },
      "url": "https://www.notion.so/New-Media-Article-6a313baefdd346179bd65b132f23be35"
    }
  ],
  "next_cursor": null,
  "has_more": false
}
```

