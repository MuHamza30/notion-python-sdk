# Users

All actions in a Notion workspace are associated to a [user](https://developers.notion.com/reference/user), whether it be a bot via a [Notion integration](https://developers.notion.com/docs/getting-started) or a person interacting with Notion’s UI.

These endpoints allow developers to interact with users programmatically by [listing all users](https://developers.notion.com/reference/get-user), [retrieving information about your integration’s bot](https://developers.notion.com/reference/get-self), or [retrieving a specific user](https://developers.notion.com/reference/get-user) in your Notion workspace.

To learn more, read [Notion’s official documentation](https://developers.notion.com/reference/user) for endpoints related to users.

```python
users_controller = client.users
```

## Class Name

`UsersController`

## Methods

* [Retrieve a User](../../doc/controllers/users.md#retrieve-a-user)
* [List All Users](../../doc/controllers/users.md#list-all-users)
* [Retrieve Your Token S Bot User](../../doc/controllers/users.md#retrieve-your-token-s-bot-user)


# Retrieve a User

Retrieve a user object using the ID specified in the request path.

```python
def retrieve_a_user(self,
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
id = '{{USER_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = users_controller.retrieve_a_user(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "user",
  "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a",
  "name": "Aman Gupta",
  "avatar_url": null,
  "type": "person",
  "person": {
    "email": "XXXXXXXXXXX"
  }
}
```


# List All Users

Returns a paginated list of user objects for a workspace

```python
def list_all_users(self,
                  notion_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Optional | - |

## Response Type

`Any`

## Example Usage

```python
notion_version = '{{NOTION_VERSION}}'

result = users_controller.list_all_users(
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
      "object": "user",
      "id": "6794760a-1f15-45cd-9c65-0dfe42f5135a",
      "name": "Aman Gupta",
      "avatar_url": null,
      "type": "person",
      "person": {
        "email": "XXXXXXXXXX"
      }
    },
    {
      "object": "user",
      "id": "92a680bb-6970-4726-952b-4f4c03bff617",
      "name": "Leotastic",
      "avatar_url": null,
      "type": "bot",
      "bot": {
        "owner": {
          "type": "workspace",
          "workspace": true
        }
      }
    }
  ],
  "next_cursor": null,
  "has_more": false
}
```


# Retrieve Your Token S Bot User

```python
def retrieve_your_token_s_bot_user(self,
                                  notion_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notion_version` | `str` | Header, Optional | - |

## Response Type

`Any`

## Example Usage

```python
notion_version = '{{NOTION_VERSION}}'

result = users_controller.retrieve_your_token_s_bot_user(
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "user",
  "id": "92a680bb-6970-4726-952b-4f4c03bff617",
  "name": "Leotastic",
  "avatar_url": null,
  "type": "bot",
  "bot": {
    "owner": {
      "type": "workspace",
      "workspace": true
    }
  }
}
```

