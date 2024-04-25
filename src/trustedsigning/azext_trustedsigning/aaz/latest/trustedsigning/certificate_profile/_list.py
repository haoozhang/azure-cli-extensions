# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "trustedsigning certificate-profile list",
    is_preview=True,
)
class List(AAZCommand):
    """List certificate profiles under a trusted signing account.

    :example: Lists certificate profile under a trusted signing account
        az trustedsigning certificate-profile list -g MyResourceGroup --account-name
    """

    _aaz_info = {
        "version": "2024-02-05-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.codesigning/codesigningaccounts/{}/certificateprofiles", "2024-02-05-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.account_name = AAZStrArg(
            options=["--account-name"],
            help="Trusted Signing account name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^(?=.{3,24}$)[^0-9][A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CertificateProfilesListByCodeSigningAccount(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class CertificateProfilesListByCodeSigningAccount(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CodeSigning/codeSigningAccounts/{accountName}/certificateProfiles",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "accountName", self.ctx.args.account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-02-05-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.certificates = AAZListType(
                flags={"read_only": True},
            )
            properties.city = AAZStrType(
                flags={"read_only": True},
            )
            properties.common_name = AAZStrType(
                serialized_name="commonName",
                flags={"read_only": True},
            )
            properties.country = AAZStrType(
                flags={"read_only": True},
            )
            properties.enhanced_key_usage = AAZStrType(
                serialized_name="enhancedKeyUsage",
                flags={"read_only": True},
            )
            properties.identity_validation_id = AAZStrType(
                serialized_name="identityValidationId",
            )
            properties.include_city = AAZBoolType(
                serialized_name="includeCity",
            )
            properties.include_country = AAZBoolType(
                serialized_name="includeCountry",
            )
            properties.include_postal_code = AAZBoolType(
                serialized_name="includePostalCode",
            )
            properties.include_state = AAZBoolType(
                serialized_name="includeState",
            )
            properties.include_street_address = AAZBoolType(
                serialized_name="includeStreetAddress",
            )
            properties.organization = AAZStrType(
                flags={"read_only": True},
            )
            properties.organization_unit = AAZStrType(
                serialized_name="organizationUnit",
                flags={"read_only": True},
            )
            properties.postal_code = AAZStrType(
                serialized_name="postalCode",
                flags={"read_only": True},
            )
            properties.profile_type = AAZStrType(
                serialized_name="profileType",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.state = AAZStrType(
                flags={"read_only": True},
            )
            properties.status = AAZStrType()
            properties.street_address = AAZStrType(
                serialized_name="streetAddress",
                flags={"read_only": True},
            )

            certificates = cls._schema_on_200.value.Element.properties.certificates
            certificates.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.certificates.Element
            _element.created_date = AAZStrType(
                serialized_name="createdDate",
            )
            _element.expiry_date = AAZStrType(
                serialized_name="expiryDate",
            )
            _element.revocation = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.serial_number = AAZStrType(
                serialized_name="serialNumber",
            )
            _element.status = AAZStrType()
            _element.subject_name = AAZStrType(
                serialized_name="subjectName",
            )
            _element.thumbprint = AAZStrType()

            revocation = cls._schema_on_200.value.Element.properties.certificates.Element.revocation
            revocation.effective_at = AAZStrType(
                serialized_name="effectiveAt",
            )
            revocation.failure_reason = AAZStrType(
                serialized_name="failureReason",
            )
            revocation.reason = AAZStrType()
            revocation.remarks = AAZStrType()
            revocation.requested_at = AAZStrType(
                serialized_name="requestedAt",
            )
            revocation.status = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
