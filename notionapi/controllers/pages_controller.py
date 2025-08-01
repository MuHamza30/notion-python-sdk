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


class PagesController(BaseController):

    """A Controller to access Endpoints in the notionapi API."""
    def __init__(self, config):
        super(PagesController, self).__init__(config)

    def create_a_page_with_content(self,
                                   authorization=None,
                                   notion_version=None,
                                   body=None):
        """Does a POST request to /v1/pages/.

        Args:
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
            .path('/v1/pages/')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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

    def retrieve_a_page(self,
                        id,
                        notion_version=None):
        """Does a GET request to /v1/pages/{id}.

        Retrieves a Page object using the ID in the request path. This
        endpoint exposes page properties, not page content. 

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
            .path('/v1/pages/{id}')
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

    def archive_a_page(self,
                       id,
                       notion_version=None,
                       body=None):
        """Does a PATCH request to /v1/pages/{id}.

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
            .path('/v1/pages/{id}')
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

    def retrieve_a_page_property_item(self,
                                      page_id,
                                      property_id,
                                      notion_version=None):
        """Does a GET request to /v1/pages/{page_id}/properties/{property_id}.

        Args:
            page_id (str): The request template parameter.
            property_id (str): The request template parameter.
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
            .path('/v1/pages/{page_id}/properties/{property_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('page_id')
                            .value(page_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('property_id')
                            .value(property_id)
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
