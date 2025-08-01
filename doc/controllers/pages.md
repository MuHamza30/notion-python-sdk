# Pages

Pages represent documents in Notion workspaces that can be created in a workspace directly or organized within in a Notion database.

These page-related endpoints allow developers to work with pages programmatically by [creating](https://developers.notion.com/reference/post-page), [retrieving](https://developers.notion.com/reference/retrieve-a-page), [updating](https://developers.notion.com/reference/patch-page), and [archiving](https://developers.notion.com/reference/archive-a-page) them.

To learn more, read [Notion’s official documentation](https://developers.notion.com/reference/page) for endpoints related to pages. We also recommend reading the official Notion guide for [working with page content](https://developers.notion.com/docs/working-with-page-content).

```python
pages_controller = client.pages
```

## Class Name

`PagesController`

## Methods

* [Create a Page With Content](../../doc/controllers/pages.md#create-a-page-with-content)
* [Retrieve a Page](../../doc/controllers/pages.md#retrieve-a-page)
* [Archive a Page](../../doc/controllers/pages.md#archive-a-page)
* [Retrieve a Page Property Item](../../doc/controllers/pages.md#retrieve-a-page-property-item)


# Create a Page With Content

```python
def create_a_page_with_content(self,
                              authorization=None,
                              notion_version=None,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Optional | - |
| `notion_version` | `str` | Header, Optional | - |
| `body` | `str` | Body, Optional | - |

## Response Type

`Any`

## Example Usage

```python
authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns'

notion_version = '{{NOTION_VERSION}}'

result = pages_controller.create_a_page_with_content(
    authorization=authorization,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "page",
  "id": "672b014a-2626-4ada-9211-fb3613d07ae2",
  "created_time": "2022-03-02T05:24:00.000Z",
  "last_edited_time": "2022-03-02T05:24:00.000Z",
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
        "id": "672b014a-2626-4ada-9211-fb3613d07ae2",
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
  "url": "https://www.notion.so/New-Media-Article-672b014a26264ada9211fb3613d07ae2"
}
```


# Retrieve a Page

Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content.

```python
def retrieve_a_page(self,
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
id = '{{PAGE_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = pages_controller.retrieve_a_page(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "page",
  "id": "c4d39556-6364-46a1-8a61-ebbb668f7445",
  "created_time": "2021-04-27T20:38:00.000Z",
  "last_edited_time": "2022-03-02T05:22:00.000Z",
  "created_by": {
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
  },
  "last_edited_by": {
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617"
  },
  "cover": null,
  "icon": {
    "type": "emoji",
    "emoji": "📕"
  },
  "parent": {
    "type": "page_id",
    "page_id": "c1218692-102d-4b47-ab38-c21900b3557b"
  },
  "archived": false,
  "properties": {
    "title": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "Reading List",
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
          "plain_text": "Reading List",
          "href": null
        }
      ]
    }
  },
  "url": "https://www.notion.so/Reading-List-c4d39556636446a18a61ebbb668f7445"
}
```


# Archive a Page

```python
def archive_a_page(self,
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
id = '{{PAGE_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = pages_controller.archive_a_page(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "block",
  "id": "2646ac0d-df90-4bab-bb4e-75e3cb972ed1",
  "created_time": "2022-02-24T22:14:00.000Z",
  "last_edited_time": "2022-02-24T22:15:00.000Z",
  "created_by": {
    "object": "user",
    "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a"
  },
  "last_edited_by": {
    "object": "user",
    "id": "92a680bb-6970-4726-952b-4f4c03bff617"
  },
  "has_children": false,
  "archived": true,
  "type": "child_page",
  "child_page": {
    "title": ""
  }
}
```


# Retrieve a Page Property Item

```python
def retrieve_a_page_property_item(self,
                                 page_id,
                                 property_id,
                                 notion_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_id` | `str` | Template, Required | - |
| `property_id` | `str` | Template, Required | - |
| `notion_version` | `str` | Header, Optional | - |

## Response Type

`Any`

## Example Usage

```python
page_id = '{{PAGE_ID}}'

property_id = 'property_id0'

notion_version = '{{NOTION_VERSION}}'

result = pages_controller.retrieve_a_page_property_item(
    page_id,
    property_id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "property_item",
  "type": "select",
  "select": {
    "id": "5c944de7-3f4b-4567-b3a1-fa2c71c540b6",
    "name": "⭐️⭐️⭐️⭐️⭐️",
    "color": "default"
  }
}
```

