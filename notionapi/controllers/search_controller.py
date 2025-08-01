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


class SearchController(BaseController):

    """A Controller to access Endpoints in the notionapi API."""
    def __init__(self, config):
        super(SearchController, self).__init__(config)

    def search(self,
               notion_version=None,
               body=None):
        """Does a POST request to /v1/search.

        Args:
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
            .path('/v1/search')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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
