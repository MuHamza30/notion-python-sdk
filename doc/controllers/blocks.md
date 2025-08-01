# Blocks

A block represents a piece of content in a Notion workspace. All Notion pages are composed of a series of blocks. Blocks can vary in type, including (but not limited to) headers, styled text, images, tables, and more. To see a complete list of block types, refer to Notion’s [official documentation](https://developers.notion.com/reference/page-property-values#type-objects).

These block-related endpoints allow developers to work with blocks programmatically by [creating](https://developers.notion.com/reference/patch-block-children), [retrieving](https://developers.notion.com/reference/retrieve-a-block), [updating](https://developers.notion.com/reference/update-a-block), and [deleting](https://developers.notion.com/reference/delete-a-block) them from Notion pages.

To learn more, read [Notion’s official documentation](https://developers.notion.com/reference/block) for endpoints related to blocks. We also recommend reading the official Notion guides for [working with page content](https://developers.notion.com/docs/working-with-page-content) (a.k.a. blocks) and [working with files and media](https://developers.notion.com/docs/working-with-files-and-media).

```python
blocks_controller = client.blocks
```

## Class Name

`BlocksController`

## Methods

* [Retrieve Block Children](../../doc/controllers/blocks.md#retrieve-block-children)
* [Append Block Children](../../doc/controllers/blocks.md#append-block-children)
* [Update a Block](../../doc/controllers/blocks.md#update-a-block)
* [Retrieve a Block](../../doc/controllers/blocks.md#retrieve-a-block)
* [Delete a Block](../../doc/controllers/blocks.md#delete-a-block)


# Retrieve Block Children

```python
def retrieve_block_children(self,
                           id,
                           notion_version=None,
                           page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | - |
| `notion_version` | `str` | Header, Optional | - |
| `page_size` | `int` | Query, Optional | - |

## Response Type

`Any`

## Example Usage

```python
id = '{{PAGE_ID}}'

notion_version = '{{NOTION_VERSION}}'

page_size = 100

result = blocks_controller.retrieve_block_children(
    id,
    notion_version=notion_version,
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
      "object": "block",
      "id": "48c1ffb5-2789-4025-937b-2c35eaaaab3f",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "unsupported",
      "unsupported": {}
    },
    {
      "object": "block",
      "id": "e381a0a3-4efb-4ba9-aa93-45b70fa9ce7f",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "I think we can all agree that Silicon Valley needs more adult supervision right about now.",
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
            "plain_text": "I think we can all agree that Silicon Valley needs more adult supervision right about now.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "ce5f79ac-8145-44ab-be3b-8ad143d6f8a7",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Is the solution for its companies to hire a chief ethics officer?",
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
            "plain_text": "Is the solution for its companies to hire a chief ethics officer?",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "0387b374-7847-4ddc-bc53-6b0813ce4ed4",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "While some tech companies like Google have top compliance officers and others turn to legal teams to police themselves, no big tech companies that I know of have yet taken this step. But a lot of them seem to be talking about it, and I’ve discussed the idea with several chief executives recently. Why? Because slowly, then all at once, it feels like too many digital leaders have lost their minds.",
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
            "plain_text": "While some tech companies like Google have top compliance officers and others turn to legal teams to police themselves, no big tech companies that I know of have yet taken this step. But a lot of them seem to be talking about it, and I’ve discussed the idea with several chief executives recently. Why? Because slowly, then all at once, it feels like too many digital leaders have lost their minds.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "da035311-5af3-48bc-8279-d28d9f4ef2e2",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "It’s probably no surprise, considering the complex problems the tech industry faces. As one ethical quandary after another has hit its profoundly ill-prepared executives, their once-pristine reputations have fallen like palm trees in a hurricane. These last two weeks alone show how tech is stumbling to react to big world issues armed with only bubble world skills:",
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
            "plain_text": "It’s probably no surprise, considering the complex problems the tech industry faces. As one ethical quandary after another has hit its profoundly ill-prepared executives, their once-pristine reputations have fallen like palm trees in a hurricane. These last two weeks alone show how tech is stumbling to react to big world issues armed with only bubble world skills:",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "63a60fca-4a11-43eb-8773-c5f0164a3117",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "As a journalist is beheaded and dismembered at the direction of Saudi Arabian leaders (allegedly, but the killers did bring a bone saw), Silicon Valley is swimming in oceans of money from the kingdom’s Public Investment Fund. Saudi funding includes hundreds of millions for Magic Leap, and huge investments in hot public companies like Tesla. Most significantly: Saudis have invested about $45 billion in SoftBank’s giant Vision Fund, which has in turn doused the tech landscape — $4.4 billion to WeWork, $250 million to Slack, and $300 million to the dog-walking app Wag. In total Uber has gotten almost $14 billion, either through direct investments from the Public Investment Fund or through the Saudis’ funding of the Vision Fund. A billion here, a billion there and it all adds up.",
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
            "plain_text": "As a journalist is beheaded and dismembered at the direction of Saudi Arabian leaders (allegedly, but the killers did bring a bone saw), Silicon Valley is swimming in oceans of money from the kingdom’s Public Investment Fund. Saudi funding includes hundreds of millions for Magic Leap, and huge investments in hot public companies like Tesla. Most significantly: Saudis have invested about $45 billion in SoftBank’s giant Vision Fund, which has in turn doused the tech landscape — $4.4 billion to WeWork, $250 million to Slack, and $300 million to the dog-walking app Wag. In total Uber has gotten almost $14 billion, either through direct investments from the Public Investment Fund or through the Saudis’ funding of the Vision Fund. A billion here, a billion there and it all adds up.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "8c58c8f1-86ae-4a14-b6b9-74f5fa579620",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "[",
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
            "plain_text": "[",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "Kara Swisher answered your questions about her column ",
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
            "plain_text": "Kara Swisher answered your questions about her column ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "on Twitter",
              "link": {
                "url": "https://twitter.com/karaswisher/status/1054842303922298880"
              }
            },
            "annotations": {
              "bold": false,
              "italic": true,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "on Twitter",
            "href": "https://twitter.com/karaswisher/status/1054842303922298880"
          },
          {
            "type": "text",
            "text": {
              "content": ".",
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
            "plain_text": ".",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "]",
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
            "plain_text": "]",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "875d3aff-086b-45da-9ed1-bc3ddb185229",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Facebook introduced a new home video device called Portal, and promised that what could be seen as a surveillance tool would not share data for the sake of ad targeting. Soon after, as ",
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
            "plain_text": "Facebook introduced a new home video device called Portal, and promised that what could be seen as a surveillance tool would not share data for the sake of ad targeting. Soon after, as ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "reported by Recode",
              "link": {
                "url": "https://www.recode.net/2018/10/16/17966102/facebook-portal-ad-targeting-data-collection"
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
            "plain_text": "reported by Recode",
            "href": "https://www.recode.net/2018/10/16/17966102/facebook-portal-ad-targeting-data-collection"
          },
          {
            "type": "text",
            "text": {
              "content": ", Facebook admitted that “data about who you call and data about which apps you use on Portal ",
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
            "plain_text": ", Facebook admitted that “data about who you call and data about which apps you use on Portal ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "can",
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
            "plain_text": "can",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": " be used to target you with ads on other Facebook-owned properties.” Oh. Um. That’s awkward.",
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
            "plain_text": " be used to target you with ads on other Facebook-owned properties.” Oh. Um. That’s awkward.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "306ab0fb-6daa-4c5b-b1f7-f51a5f92b6ff",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "After agreeing to pay $20 million to the Securities and Exchange Commission for an ill-advised tweet about possible funding (from the Saudis, by the way), the Tesla co-founder Elon Musk proceeded to troll the regulatory agency on, you got it, Twitter. And even though the ",
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
            "plain_text": "After agreeing to pay $20 million to the Securities and Exchange Commission for an ill-advised tweet about possible funding (from the Saudis, by the way), the Tesla co-founder Elon Musk proceeded to troll the regulatory agency on, you got it, Twitter. And even though the ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "settlement called for some kind of control of his communications",
              "link": {
                "url": "https://www.sec.gov/news/press-release/2018-226"
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
            "plain_text": "settlement called for some kind of control of his communications",
            "href": "https://www.sec.gov/news/press-release/2018-226"
          },
          {
            "type": "text",
            "text": {
              "content": ", it appears that Mr. Musk will continue tweeting until someone steals his phone.",
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
            "plain_text": ", it appears that Mr. Musk will continue tweeting until someone steals his phone.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "122b1457-4129-4513-abaa-7cce7d66e4a1",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Finally, Google took six months to make public that user data on its social network, Google Plus, ",
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
            "plain_text": "Finally, Google took six months to make public that user data on its social network, Google Plus, ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "had been exposed",
              "link": {
                "url": "https://www.nytimes.com/2018/10/08/technology/google-plus-security-disclosure.html?module=inline"
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
            "plain_text": "had been exposed",
            "href": "https://www.nytimes.com/2018/10/08/technology/google-plus-security-disclosure.html?module=inline"
          },
          {
            "type": "text",
            "text": {
              "content": " and that profiles of up to 500,000 users may have been compromised. While the service failed long ago, because it was pretty much designed by antisocial people, this lack of concern for privacy was profound.",
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
            "plain_text": " and that profiles of up to 500,000 users may have been compromised. While the service failed long ago, because it was pretty much designed by antisocial people, this lack of concern for privacy was profound.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "4d4af599-556f-4d8b-af8e-4d01ebe2aa27",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Grappling with what to say and do about the disasters they themselves create is only the beginning. Then there are the broader issues that the denizens of Silicon Valley expect their employers to have a stance on: immigration, income inequality, artificial intelligence, automation, transgender rights, climate change, privacy, data rights and whether tech companies should be helping the government do controversial things. It’s an ethical swamp out there.",
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
            "plain_text": "Grappling with what to say and do about the disasters they themselves create is only the beginning. Then there are the broader issues that the denizens of Silicon Valley expect their employers to have a stance on: immigration, income inequality, artificial intelligence, automation, transgender rights, climate change, privacy, data rights and whether tech companies should be helping the government do controversial things. It’s an ethical swamp out there.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "f5775df5-59eb-4533-a2cb-e150412ec4f6",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "That’s why, in a recent interview, Marc Benioff, the co-chief executive and a founder of Salesforce, told me he was in the process of hiring a chief ethical officer to help anticipate and address any thorny conundrums it might encounter as a business — like the decision it had to make a few months back about whether it should stop providing recruitment software for Customs and Border Protection because of the government’s policy of separating immigrant families at the border.",
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
            "plain_text": "That’s why, in a recent interview, Marc Benioff, the co-chief executive and a founder of Salesforce, told me he was in the process of hiring a chief ethical officer to help anticipate and address any thorny conundrums it might encounter as a business — like the decision it had to make a few months back about whether it should stop providing recruitment software for Customs and Border Protection because of the government’s policy of separating immigrant families at the border.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "31405c6e-7ece-4667-8c4d-36c9d79a0bfa",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Amid much criticism, Mr. Benioff decided to keep the contract, but said he would focus more on social and political issues.",
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
            "plain_text": "Amid much criticism, Mr. Benioff decided to keep the contract, but said he would focus more on social and political issues.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "a2ab7e8a-d521-401d-89ae-9eb27efb9990",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "At a recent company event, he elaborated: “We can have a structured conversation not just with our own employees myopically, but by bringing in the key advisers, supporters and pundits and philosophers and everybody necessary to ask the question if what we are doing today is ethical and humane.”",
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
            "plain_text": "At a recent company event, he elaborated: “We can have a structured conversation not just with our own employees myopically, but by bringing in the key advisers, supporters and pundits and philosophers and everybody necessary to ask the question if what we are doing today is ethical and humane.”",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "a4498e1e-8b85-48d7-802a-db447ca7d1ac",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "23andMe has also toyed with the idea of hiring a chief ethics officer. In an interview I did this week with its chief executive, Anne Wojcicki, she said the genetics company had even interviewed candidates, but that many of them wanted to remain in academia to be freer to ponder these issues. She acknowledged that the collection of DNA data is rife with ethical considerations, but said, “I think it has to be our management and leaders who have to add this to our skill set, rather than just hire one person to determine this.”",
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
            "plain_text": "23andMe has also toyed with the idea of hiring a chief ethics officer. In an interview I did this week with its chief executive, Anne Wojcicki, she said the genetics company had even interviewed candidates, but that many of them wanted to remain in academia to be freer to ponder these issues. She acknowledged that the collection of DNA data is rife with ethical considerations, but said, “I think it has to be our management and leaders who have to add this to our skill set, rather than just hire one person to determine this.”",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "cbf7e7e0-5552-4b3f-b09e-9dcca120931c",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "When asked about the idea of a single source of wisdom on ethics, some point out that legal or diversity/inclusion departments are designed for that purpose and that the ethics should really come from the top — the chief executive.",
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
            "plain_text": "When asked about the idea of a single source of wisdom on ethics, some point out that legal or diversity/inclusion departments are designed for that purpose and that the ethics should really come from the top — the chief executive.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "d24b2887-0f1f-4e91-99c1-c295bed8ad65",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Also of concern is the possibility that a single person would not get listened to or, worse, get steamrollered. And, if the person was bad at the job, of course, it could drag the whole thing down.",
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
            "plain_text": "Also of concern is the possibility that a single person would not get listened to or, worse, get steamrollered. And, if the person was bad at the job, of course, it could drag the whole thing down.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "78c55f65-c8b8-4364-a369-c40699968e90",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Others are more worried that the move would be nothing but window dressing. One consultant who focuses on ethics, but did not want to be named, told me: “We haven’t even defined ethics, so what even is ethical use, especially for Silicon Valley companies that are babies in this game?”",
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
            "plain_text": "Others are more worried that the move would be nothing but window dressing. One consultant who focuses on ethics, but did not want to be named, told me: “We haven’t even defined ethics, so what even is ethical use, especially for Silicon Valley companies that are babies in this game?”",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "0b492111-1586-4a73-8848-04f0c391aadc",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "How can an industry that, unlike other business sectors, persistently promotes itself as doing good, learn to do that in reality? Do you want to not do harm, or do you want to do good? These are two totally different things.",
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
            "plain_text": "How can an industry that, unlike other business sectors, persistently promotes itself as doing good, learn to do that in reality? Do you want to not do harm, or do you want to do good? These are two totally different things.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "302f8229-2404-460b-8c3c-e7058b4365e5",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "And how do you put an official ethical system in place without it seeming like you’re telling everyone how to behave? Who gets to decide those rules anyway, setting a moral path for the industry and — considering tech companies’ enormous power — the world.",
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
            "plain_text": "And how do you put an official ethical system in place without it seeming like you’re telling everyone how to behave? Who gets to decide those rules anyway, setting a moral path for the industry and — considering tech companies’ enormous power — the world.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "8f9bc91c-5662-4b3f-a110-809f46b79f49",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Like I said, adult supervision. Or maybe, better still, Silicon Valley itself has to grow up.",
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
            "plain_text": "Like I said, adult supervision. Or maybe, better still, Silicon Valley itself has to grow up.",
            "href": null
          }
        ]
      }
    },
    {
      "object": "block",
      "id": "7bea1831-a25c-4b3e-8c9b-b37de814f948",
      "created_time": "2021-04-27T20:38:19.437Z",
      "last_edited_time": "2021-04-27T20:38:19.437Z",
      "has_children": false,
      "type": "paragraph",
      "paragraph": {
        "text": [
          {
            "type": "text",
            "text": {
              "content": "Follow The New York Times Opinion section on ",
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
            "plain_text": "Follow The New York Times Opinion section on ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "Facebook",
              "link": {
                "url": "https://www.facebook.com/nytopinion"
              }
            },
            "annotations": {
              "bold": false,
              "italic": true,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Facebook",
            "href": "https://www.facebook.com/nytopinion"
          },
          {
            "type": "text",
            "text": {
              "content": ", ",
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
            "plain_text": ", ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "Twitter (@NYTopinion)",
              "link": {
                "url": "http://twitter.com/NYTOpinion"
              }
            },
            "annotations": {
              "bold": false,
              "italic": true,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Twitter (@NYTopinion)",
            "href": "http://twitter.com/NYTOpinion"
          },
          {
            "type": "text",
            "text": {
              "content": " and ",
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
            "plain_text": " and ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "Instagram",
              "link": {
                "url": "https://www.instagram.com/nytopinion/"
              }
            },
            "annotations": {
              "bold": false,
              "italic": true,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Instagram",
            "href": "https://www.instagram.com/nytopinion/"
          },
          {
            "type": "text",
            "text": {
              "content": ", and sign up for the ",
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
            "plain_text": ", and sign up for the ",
            "href": null
          },
          {
            "type": "text",
            "text": {
              "content": "Opinion Today newsletter",
              "link": {
                "url": "http://www.nytimes.com/newsletters/opiniontoday/"
              }
            },
            "annotations": {
              "bold": false,
              "italic": true,
              "strikethrough": false,
              "underline": false,
              "code": false,
              "color": "default"
            },
            "plain_text": "Opinion Today newsletter",
            "href": "http://www.nytimes.com/newsletters/opiniontoday/"
          },
          {
            "type": "text",
            "text": {
              "content": ".",
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
            "plain_text": ".",
            "href": null
          }
        ]
      }
    }
  ],
  "next_cursor": null,
  "has_more": false
}
```


# Append Block Children

```python
def append_block_children(self,
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
id = '{{PAGE_ID}}'

authorization = 'Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns'

notion_version = '{{NOTION_VERSION}}'

result = blocks_controller.append_block_children(
    id,
    authorization=authorization,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "block",
  "id": "a1712d54-53e4-4893-a69d-4d581cd2c845",
  "created_time": "2021-04-27T20:38:19.437Z",
  "last_edited_time": "2021-05-12T06:07:37.724Z",
  "has_children": true,
  "type": "child_page",
  "child_page": {
    "title": "Who Will Teach Silicon Valley to Be Ethical? "
  }
}
```


# Update a Block

This endpoint allows you to update block content. [See Full Documentation](https://developers.notion.com/reference/update-a-block)

```python
def update_a_block(self,
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
id = '{{BLOCK_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = blocks_controller.update_a_block(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "block",
  "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
  "created_time": "2021-08-06T17:46:00.000Z",
  "last_edited_time": "2021-08-12T00:12:00.000Z",
  "has_children": false,
  "type": "paragraph",
  "paragraph": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "hello to you",
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
        "plain_text": "hello to you",
        "href": null
      }
    ]
  }
}
```


# Retrieve a Block

```python
def retrieve_a_block(self,
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
id = '{{BLOCK_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = blocks_controller.retrieve_a_block(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "block",
  "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
  "created_time": "2021-08-06T17:46:00.000Z",
  "last_edited_time": "2021-08-12T00:12:00.000Z",
  "has_children": false,
  "type": "paragraph",
  "paragraph": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "hello to you",
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
        "plain_text": "hello to you",
        "href": null
      }
    ]
  }
}
```


# Delete a Block

```python
def delete_a_block(self,
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
id = '{{BLOCK_ID}}'

notion_version = '{{NOTION_VERSION}}'

result = blocks_controller.delete_a_block(
    id,
    notion_version=notion_version
)
print(result)
```

## Example Response

```
{
  "object": "block",
  "id": "4868767d-9029-4b9d-a41b-652ef4c9c7b9",
  "created_time": "2021-08-06T17:46:00.000Z",
  "last_edited_time": "2022-02-24T22:26:00.000Z",
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
  "type": "paragraph",
  "paragraph": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "hello to you",
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
        "plain_text": "hello to you",
        "href": null
      }
    ]
  }
}
```

