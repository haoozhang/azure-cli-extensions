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
    "network firewall policy update",
)
class Update(AAZCommand):
    """Update an Azure firewall policy.
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/firewallpolicies/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the Firewall Policy.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sku = AAZStrArg(
            options=["--sku"],
            help="SKU of Firewall policy.",
            is_preview=True,
            nullable=True,
            enum={"Basic": "Basic", "Premium": "Premium", "Standard": "Standard"},
        )
        _args_schema.sql = AAZBoolArg(
            options=["--sql"],
            help="A flag to indicate if SQL Redirect traffic filtering is enabled.",
            is_preview=True,
            nullable=True,
        )
        _args_schema.threat_intel_mode = AAZStrArg(
            options=["--threat-intel-mode"],
            help="The operation mode for Threat Intelligence.",
            nullable=True,
            enum={"Alert": "Alert", "Deny": "Deny", "Off": "Off"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...]. Use \"\" to clear existing tags.",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "DNS"

        _args_schema = cls._args_schema
        _args_schema.enable_dns_proxy = AAZBoolArg(
            options=["--enable-dns-proxy"],
            arg_group="DNS",
            help="Enable DNS Proxy.",
            nullable=True,
        )
        _args_schema.dns_servers = AAZListArg(
            options=["--dns-servers"],
            arg_group="DNS",
            help="Space-separated list of DNS server IP addresses.",
            nullable=True,
        )

        dns_servers = cls._args_schema.dns_servers
        dns_servers.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "DnsSettings"

        # define Arg Group "Identity Instance"

        _args_schema = cls._args_schema
        _args_schema.identity_type = AAZStrArg(
            options=["--identity-type"],
            arg_group="Identity Instance",
            help="The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the virtual machine.",
            nullable=True,
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned, UserAssigned": "SystemAssigned, UserAssigned", "UserAssigned": "UserAssigned"},
        )
        _args_schema.user_assigned_identities = AAZDictArg(
            options=["--user-assigned-identities"],
            arg_group="Identity Instance",
            help="The list of user identities associated with resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        # define Arg Group "IntrusionDetection"

        # define Arg Group "Intrustion Detection"

        _args_schema = cls._args_schema
        _args_schema.idps_mode = AAZStrArg(
            options=["--idps-mode"],
            arg_group="Intrustion Detection",
            help="IDPS mode.",
            is_preview=True,
            nullable=True,
            enum={"Alert": "Alert", "Deny": "Deny", "Off": "Off"},
        )

        # define Arg Group "Parameters"

        # define Arg Group "Properties"

        # define Arg Group "Snat"

        _args_schema = cls._args_schema
        _args_schema.auto_learn_private_ranges = AAZStrArg(
            options=["--learn-ranges", "--auto-learn-private-ranges"],
            arg_group="Snat",
            help="The operation mode for automatically learning private ranges to not be SNAT",
            nullable=True,
            enum={"Disabled": "Disabled", "Enabled": "Enabled"},
        )
        _args_schema.private_ranges = AAZListArg(
            options=["--private-ranges"],
            arg_group="Snat",
            help="List of private IP addresses/IP address ranges to not be SNAT.",
            nullable=True,
        )

        private_ranges = cls._args_schema.private_ranges
        private_ranges.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "TLS Inspection"

        _args_schema = cls._args_schema
        _args_schema.key_vault_secret_id = AAZStrArg(
            options=["--key-vault-secret-id"],
            arg_group="TLS Inspection",
            help="Secret Id of (base-64 encoded unencrypted pfx) Secret or Certificate object stored in KeyVault.",
            is_preview=True,
            nullable=True,
        )
        _args_schema.cert_name = AAZStrArg(
            options=["--cert-name"],
            arg_group="TLS Inspection",
            help="Name of the CA certificate.",
            is_preview=True,
            nullable=True,
        )

        # define Arg Group "Threat Intel Allowlist"

        _args_schema = cls._args_schema
        _args_schema.fqdns = AAZListArg(
            options=["--fqdns"],
            arg_group="Threat Intel Allowlist",
            help="Space-separated list of FQDNs.",
            nullable=True,
        )
        _args_schema.ip_addresses = AAZListArg(
            options=["--ip-addresses"],
            arg_group="Threat Intel Allowlist",
            help="Space-separated list of IPv4 addresses.",
            nullable=True,
        )

        fqdns = cls._args_schema.fqdns
        fqdns.Element = AAZStrArg(
            nullable=True,
        )

        ip_addresses = cls._args_schema.ip_addresses
        ip_addresses.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.FirewallPoliciesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.FirewallPoliciesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FirewallPoliciesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallPolicyName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
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
            _UpdateHelper._build_schema_firewall_policy_read(cls._schema_on_200)

            return cls._schema_on_200

    class FirewallPoliciesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallPolicyName", self.ctx.args.name,
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
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_firewall_policy_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType)
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".identity_type")
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("basePolicy", AAZObjectType)
                properties.set_prop("dnsSettings", AAZObjectType)
                properties.set_prop("intrusionDetection", AAZObjectType)
                properties.set_prop("sku", AAZObjectType)
                properties.set_prop("snat", AAZObjectType)
                properties.set_prop("sql", AAZObjectType)
                properties.set_prop("threatIntelMode", AAZStrType, ".threat_intel_mode")
                properties.set_prop("threatIntelWhitelist", AAZObjectType)
                properties.set_prop("transportSecurity", AAZObjectType)

            dns_settings = _builder.get(".properties.dnsSettings")
            if dns_settings is not None:
                dns_settings.set_prop("enableProxy", AAZBoolType, ".enable_dns_proxy")
                dns_settings.set_prop("servers", AAZListType, ".dns_servers")

            servers = _builder.get(".properties.dnsSettings.servers")
            if servers is not None:
                servers.set_elements(AAZStrType, ".")

            intrusion_detection = _builder.get(".properties.intrusionDetection")
            if intrusion_detection is not None:
                intrusion_detection.set_prop("mode", AAZStrType, ".idps_mode")

            sku = _builder.get(".properties.sku")
            if sku is not None:
                sku.set_prop("tier", AAZStrType, ".sku")

            snat = _builder.get(".properties.snat")
            if snat is not None:
                snat.set_prop("autoLearnPrivateRanges", AAZStrType, ".auto_learn_private_ranges")
                snat.set_prop("privateRanges", AAZListType, ".private_ranges")

            private_ranges = _builder.get(".properties.snat.privateRanges")
            if private_ranges is not None:
                private_ranges.set_elements(AAZStrType, ".")

            sql = _builder.get(".properties.sql")
            if sql is not None:
                sql.set_prop("allowSqlRedirect", AAZBoolType, ".sql")

            threat_intel_whitelist = _builder.get(".properties.threatIntelWhitelist")
            if threat_intel_whitelist is not None:
                threat_intel_whitelist.set_prop("fqdns", AAZListType, ".fqdns")
                threat_intel_whitelist.set_prop("ipAddresses", AAZListType, ".ip_addresses")

            fqdns = _builder.get(".properties.threatIntelWhitelist.fqdns")
            if fqdns is not None:
                fqdns.set_elements(AAZStrType, ".")

            ip_addresses = _builder.get(".properties.threatIntelWhitelist.ipAddresses")
            if ip_addresses is not None:
                ip_addresses.set_elements(AAZStrType, ".")

            transport_security = _builder.get(".properties.transportSecurity")
            if transport_security is not None:
                transport_security.set_prop("certificateAuthority", AAZObjectType)

            certificate_authority = _builder.get(".properties.transportSecurity.certificateAuthority")
            if certificate_authority is not None:
                certificate_authority.set_prop("keyVaultSecretId", AAZStrType, ".key_vault_secret_id")
                certificate_authority.set_prop("name", AAZStrType, ".cert_name")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_firewall_policy_read = None

    @classmethod
    def _build_schema_firewall_policy_read(cls, _schema):
        if cls._schema_firewall_policy_read is not None:
            _schema.etag = cls._schema_firewall_policy_read.etag
            _schema.id = cls._schema_firewall_policy_read.id
            _schema.identity = cls._schema_firewall_policy_read.identity
            _schema.location = cls._schema_firewall_policy_read.location
            _schema.name = cls._schema_firewall_policy_read.name
            _schema.properties = cls._schema_firewall_policy_read.properties
            _schema.tags = cls._schema_firewall_policy_read.tags
            _schema.type = cls._schema_firewall_policy_read.type
            return

        cls._schema_firewall_policy_read = _schema_firewall_policy_read = AAZObjectType()

        firewall_policy_read = _schema_firewall_policy_read
        firewall_policy_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        firewall_policy_read.id = AAZStrType()
        firewall_policy_read.identity = AAZObjectType()
        firewall_policy_read.location = AAZStrType()
        firewall_policy_read.name = AAZStrType(
            flags={"read_only": True},
        )
        firewall_policy_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        firewall_policy_read.tags = AAZDictType()
        firewall_policy_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_firewall_policy_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType()
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_firewall_policy_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType()

        _element = _schema_firewall_policy_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_firewall_policy_read.properties
        properties.base_policy = AAZObjectType(
            serialized_name="basePolicy",
        )
        cls._build_schema_sub_resource_read(properties.base_policy)
        properties.child_policies = AAZListType(
            serialized_name="childPolicies",
            flags={"read_only": True},
        )
        properties.dns_settings = AAZObjectType(
            serialized_name="dnsSettings",
        )
        properties.explicit_proxy = AAZObjectType(
            serialized_name="explicitProxy",
        )
        properties.firewalls = AAZListType(
            flags={"read_only": True},
        )
        properties.insights = AAZObjectType()
        properties.intrusion_detection = AAZObjectType(
            serialized_name="intrusionDetection",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.rule_collection_groups = AAZListType(
            serialized_name="ruleCollectionGroups",
            flags={"read_only": True},
        )
        properties.sku = AAZObjectType()
        properties.snat = AAZObjectType()
        properties.sql = AAZObjectType()
        properties.threat_intel_mode = AAZStrType(
            serialized_name="threatIntelMode",
        )
        properties.threat_intel_whitelist = AAZObjectType(
            serialized_name="threatIntelWhitelist",
        )
        properties.transport_security = AAZObjectType(
            serialized_name="transportSecurity",
        )

        child_policies = _schema_firewall_policy_read.properties.child_policies
        child_policies.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(child_policies.Element)

        dns_settings = _schema_firewall_policy_read.properties.dns_settings
        dns_settings.enable_proxy = AAZBoolType(
            serialized_name="enableProxy",
        )
        dns_settings.require_proxy_for_network_rules = AAZBoolType(
            serialized_name="requireProxyForNetworkRules",
            nullable=True,
        )
        dns_settings.servers = AAZListType()

        servers = _schema_firewall_policy_read.properties.dns_settings.servers
        servers.Element = AAZStrType()

        explicit_proxy = _schema_firewall_policy_read.properties.explicit_proxy
        explicit_proxy.enable_explicit_proxy = AAZBoolType(
            serialized_name="enableExplicitProxy",
            nullable=True,
        )
        explicit_proxy.enable_pac_file = AAZBoolType(
            serialized_name="enablePacFile",
            nullable=True,
        )
        explicit_proxy.http_port = AAZIntType(
            serialized_name="httpPort",
        )
        explicit_proxy.https_port = AAZIntType(
            serialized_name="httpsPort",
        )
        explicit_proxy.pac_file = AAZStrType(
            serialized_name="pacFile",
        )
        explicit_proxy.pac_file_port = AAZIntType(
            serialized_name="pacFilePort",
        )

        firewalls = _schema_firewall_policy_read.properties.firewalls
        firewalls.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(firewalls.Element)

        insights = _schema_firewall_policy_read.properties.insights
        insights.is_enabled = AAZBoolType(
            serialized_name="isEnabled",
        )
        insights.log_analytics_resources = AAZObjectType(
            serialized_name="logAnalyticsResources",
        )
        insights.retention_days = AAZIntType(
            serialized_name="retentionDays",
        )

        log_analytics_resources = _schema_firewall_policy_read.properties.insights.log_analytics_resources
        log_analytics_resources.default_workspace_id = AAZObjectType(
            serialized_name="defaultWorkspaceId",
        )
        cls._build_schema_sub_resource_read(log_analytics_resources.default_workspace_id)
        log_analytics_resources.workspaces = AAZListType()

        workspaces = _schema_firewall_policy_read.properties.insights.log_analytics_resources.workspaces
        workspaces.Element = AAZObjectType()

        _element = _schema_firewall_policy_read.properties.insights.log_analytics_resources.workspaces.Element
        _element.region = AAZStrType()
        _element.workspace_id = AAZObjectType(
            serialized_name="workspaceId",
        )
        cls._build_schema_sub_resource_read(_element.workspace_id)

        intrusion_detection = _schema_firewall_policy_read.properties.intrusion_detection
        intrusion_detection.configuration = AAZObjectType()
        intrusion_detection.mode = AAZStrType()

        configuration = _schema_firewall_policy_read.properties.intrusion_detection.configuration
        configuration.bypass_traffic_settings = AAZListType(
            serialized_name="bypassTrafficSettings",
        )
        configuration.private_ranges = AAZListType(
            serialized_name="privateRanges",
        )
        configuration.signature_overrides = AAZListType(
            serialized_name="signatureOverrides",
        )

        bypass_traffic_settings = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings
        bypass_traffic_settings.Element = AAZObjectType()

        _element = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element
        _element.description = AAZStrType()
        _element.destination_addresses = AAZListType(
            serialized_name="destinationAddresses",
        )
        _element.destination_ip_groups = AAZListType(
            serialized_name="destinationIpGroups",
        )
        _element.destination_ports = AAZListType(
            serialized_name="destinationPorts",
        )
        _element.name = AAZStrType()
        _element.protocol = AAZStrType()
        _element.source_addresses = AAZListType(
            serialized_name="sourceAddresses",
        )
        _element.source_ip_groups = AAZListType(
            serialized_name="sourceIpGroups",
        )

        destination_addresses = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_addresses
        destination_addresses.Element = AAZStrType()

        destination_ip_groups = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_ip_groups
        destination_ip_groups.Element = AAZStrType()

        destination_ports = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.destination_ports
        destination_ports.Element = AAZStrType()

        source_addresses = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.source_addresses
        source_addresses.Element = AAZStrType()

        source_ip_groups = _schema_firewall_policy_read.properties.intrusion_detection.configuration.bypass_traffic_settings.Element.source_ip_groups
        source_ip_groups.Element = AAZStrType()

        private_ranges = _schema_firewall_policy_read.properties.intrusion_detection.configuration.private_ranges
        private_ranges.Element = AAZStrType()

        signature_overrides = _schema_firewall_policy_read.properties.intrusion_detection.configuration.signature_overrides
        signature_overrides.Element = AAZObjectType()

        _element = _schema_firewall_policy_read.properties.intrusion_detection.configuration.signature_overrides.Element
        _element.id = AAZStrType()
        _element.mode = AAZStrType()

        rule_collection_groups = _schema_firewall_policy_read.properties.rule_collection_groups
        rule_collection_groups.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(rule_collection_groups.Element)

        sku = _schema_firewall_policy_read.properties.sku
        sku.tier = AAZStrType()

        snat = _schema_firewall_policy_read.properties.snat
        snat.auto_learn_private_ranges = AAZStrType(
            serialized_name="autoLearnPrivateRanges",
        )
        snat.private_ranges = AAZListType(
            serialized_name="privateRanges",
        )

        private_ranges = _schema_firewall_policy_read.properties.snat.private_ranges
        private_ranges.Element = AAZStrType()

        sql = _schema_firewall_policy_read.properties.sql
        sql.allow_sql_redirect = AAZBoolType(
            serialized_name="allowSqlRedirect",
        )

        threat_intel_whitelist = _schema_firewall_policy_read.properties.threat_intel_whitelist
        threat_intel_whitelist.fqdns = AAZListType()
        threat_intel_whitelist.ip_addresses = AAZListType(
            serialized_name="ipAddresses",
        )

        fqdns = _schema_firewall_policy_read.properties.threat_intel_whitelist.fqdns
        fqdns.Element = AAZStrType()

        ip_addresses = _schema_firewall_policy_read.properties.threat_intel_whitelist.ip_addresses
        ip_addresses.Element = AAZStrType()

        transport_security = _schema_firewall_policy_read.properties.transport_security
        transport_security.certificate_authority = AAZObjectType(
            serialized_name="certificateAuthority",
        )

        certificate_authority = _schema_firewall_policy_read.properties.transport_security.certificate_authority
        certificate_authority.key_vault_secret_id = AAZStrType(
            serialized_name="keyVaultSecretId",
        )
        certificate_authority.name = AAZStrType()

        tags = _schema_firewall_policy_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_firewall_policy_read.etag
        _schema.id = cls._schema_firewall_policy_read.id
        _schema.identity = cls._schema_firewall_policy_read.identity
        _schema.location = cls._schema_firewall_policy_read.location
        _schema.name = cls._schema_firewall_policy_read.name
        _schema.properties = cls._schema_firewall_policy_read.properties
        _schema.tags = cls._schema_firewall_policy_read.tags
        _schema.type = cls._schema_firewall_policy_read.type

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id


__all__ = ["Update"]
