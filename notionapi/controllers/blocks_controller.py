# -*- coding: utf-8 -*-

"""
notionapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from notionapi.api_helper import APIHelper
from notionapi.configuration import Server
from notionapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from notionapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class BlocksController(BaseController):

    """A Controller to access Endpoints in the notionapi API."""
    def __init__(self, config):
        super(BlocksController, self).__init__(config)

    def retrieve_block_children(self,
                                id,
                                notion_version=None,
                                page_size=None):
        """Does a GET request to /v1/blocks/{id}/children.

        Args:
            id (str): The request template parameter.
            notion_version (str, optional): The request header parameter.
            page_size (int, optional): The request query parameter.

        Returns:
            Any: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/blocks/{id}/children')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Notion-Version')
                          .value(notion_version))
            .query_param(Parameter()
                         .key('page_size')
                         .value(page_size))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('bearerAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def append_block_children(self,
                              id,
                              authorization=None,
                              notion_version=None,
                              body=None):
        """Does a PATCH request to /v1/blocks/{id}/children.

        Args:
            id (str): The request template parameter.
            authorization (str, optional): The request header parameter.
            notion_version (str, optional): The request header parameter.
            body (str, optional): The request body parameter.

        Returns:
            Any: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/blocks/{id}/children')
            .http_method(HttpMethodEnum.PATCH)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Authorization')
                          .value(authorization))
            .header_param(Parameter()
                          .key('Notion-Version')
                          .value(notion_version))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('bearerAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def update_a_block(self,
                       id,
                       notion_version=None,
                       body=None):
        """Does a PATCH request to /v1/blocks/{id}.

        This endpoint allows you to update block content. [See Full
        Documentation](https://developers.notion.com/reference/update-a-block)

        Args:
            id (str): The request template parameter.
            notion_version (str, optional): The request header parameter.
            body (Any, optional): The request body parameter.

        Returns:
            Any: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/blocks/{id}')
            .http_method(HttpMethodEnum.PATCH)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('Notion-Version')
                          .value(notion_version))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('bearerAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def retrieve_a_block(self,
                         id,
                         notion_version=None):
        """Does a GET request to /v1/blocks/{id}.

        Args:
            id (str): The request template parameter.
            notion_version (str, optional): The request header parameter.

        Returns:
            Any: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/blocks/{id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Notion-Version')
                          .value(notion_version))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('bearerAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def delete_a_block(self,
                       id,
                       notion_version=None):
        """Does a DELETE request to /v1/blocks/{id}.

        Args:
            id (str): The request template parameter.
            notion_version (str, optional): The request header parameter.

        Returns:
            Any: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/v1/blocks/{id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Notion-Version')
                          .value(notion_version))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('bearerAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
        ).execute()
