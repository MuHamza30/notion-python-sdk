# Comments

[Comments](https://developers.notion.com/reference/comment-object) can be added to a page or inline (i.e., to blocks).  
These comment-related endpoints allow developers to work with comments programmatically by [creating](https://developers.notion.com/reference/create-a-comment) and [retrieving](https://developers.notion.com/reference/retrieve-a-block) them.

To learn more, read [Notion’s official documentation](https://developers.notion.com/reference/comment-object) for endpoints related to comments. We also recommend reading the official Notion guide for [working with comments](https://developers.notion.com/docs/working-with-comments).

```python
comments_controller = client.comments
```

## Class Name

`CommentsController`

## Methods

* [Retrieve Comments](../../doc/controllers/comments.md#retrieve-comments)
* [Add Comment to Discussion](../../doc/controllers/comments.md#add-comment-to-discussion)


# Retrieve Comments

Retrieve a user object using the ID specified in the request path.

```python
def retrieve_comments(self,
                     notion_version=None,
                     block_id=None,
                     page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Optional | - |
| `block_id` | `str` | Query, Optional | - |
| `page_size` | `int` | Query, Optional | - |

## Response Type

`Any`

## Example Usage

```python
notion_version = '{{NOTION_VERSION}}'

block_id = '{{BLOCK_ID}}'

page_size = 100

result = comments_controller.retrieve_comments(
    notion_version=notion_version,
    block_id=block_id,
    page_size=page_size
)
print(result)
```

## Example Response

```
{
  "object": "list",
  "results": [
    {
      "object": "comment",
      "id": "ed4c62f2-c0ad-4081-b6b8-dad025637741",
      "parent": {
        "type": "block_id",
        "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
      },
      "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
      "created_time": "2022-07-15T21:38:00.000Z",
      "last_edited_time": "2022-07-15T21:38:00.000Z",
      "created_by": {
        "object": "user",
        "id": "952f41bb-da96-4d36-9c2e-74924eee8ef1"
      },
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "Please cite your source",
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
          "plain_text": "Please cite your source",
          "href": null
        }
      ]
    },
    {
      "object": "comment",
      "id": "8949cb38-aee6-4c62-ba96-6ef7df9b4cf2",
      "parent": {
        "type": "block_id",
        "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
      },
      "discussion_id": "e63f446f-a84a-4cab-8f5a-b9e7779ecb67",
      "created_time": "2022-07-15T21:38:00.000Z",
      "last_edited_time": "2022-07-15T21:38:00.000Z",
      "created_by": {
        "object": "user",
        "id": "952f41bb-da96-4d36-9c2e-74924eee8ef1"
      },
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "What other nutrients does kale have?",
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
          "plain_text": "What other nutrients does kale have?",
          "href": null
        }
      ]
    },
    {
      "object": "comment",
      "id": "6cd52483-6d55-4f8a-a724-4adb1c17ed43",
      "parent": {
        "type": "block_id",
        "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
      },
      "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
      "created_time": "2022-07-18T21:48:00.000Z",
      "last_edited_time": "2022-07-18T21:48:00.000Z",
      "created_by": {
        "object": "user",
        "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
      },
      "rich_text": [
        {
          "type": "text",
          "text": {
            "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
            "link": {
              "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
            }
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
          "href": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
        }
      ]
    }
  ],
  "next_cursor": null,
  "has_more": false,
  "type": "comment",
  "comment": {}
}
```


# Add Comment to Discussion

```python
def add_comment_to_discussion(self,
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

result = comments_controller.add_comment_to_discussion(
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "comment",
  "id": "6cd52483-6d55-4f8a-a724-4adb1c17ed43",
  "parent": {
    "type": "block_id",
    "block_id": "5d4ca33c-d6b7-4675-93d9-84b70af45d1c"
  },
  "discussion_id": "ce18f8c6-ef2a-427f-b416-43531fc7c117",
  "created_time": "2022-07-18T21:48:00.000Z",
  "last_edited_time": "2022-07-18T21:48:00.000Z",
  "created_by": {
    "object": "user",
    "id": "e450a39e-9051-4d36-bc4e-8581611fc592"
  },
  "rich_text": [
    {
      "type": "text",
      "text": {
        "content": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
        "link": {
          "url": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
        }
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale",
      "href": "https://www.healthline.com/nutrition/10-proven-benefits-of-kale"
    }
  ]
}
```

