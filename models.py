"""Data models for github_v3_rest_api."""
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class Root(BaseModel):
    """Root schema from the OpenAPI specification."""
    current_user_url: str = Field(alias="current_user_url")
    current_user_authorizations_html_url: str = Field(alias="current_user_authorizations_html_url")
    authorizations_url: str = Field(alias="authorizations_url")
    code_search_url: str = Field(alias="code_search_url")
    commit_search_url: str = Field(alias="commit_search_url")
    emails_url: str = Field(alias="emails_url")
    emojis_url: str = Field(alias="emojis_url")
    events_url: str = Field(alias="events_url")
    feeds_url: str = Field(alias="feeds_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    hub_url: str = Field(alias="hub_url")
    issue_search_url: str = Field(alias="issue_search_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    label_search_url: str = Field(alias="label_search_url")
    notifications_url: str = Field(alias="notifications_url")
    organization_url: str = Field(alias="organization_url")
    organization_repositories_url: str = Field(alias="organization_repositories_url")
    organization_teams_url: str = Field(alias="organization_teams_url")
    public_gists_url: str = Field(alias="public_gists_url")
    rate_limit_url: str = Field(alias="rate_limit_url")
    repository_url: str = Field(alias="repository_url")
    repository_search_url: str = Field(alias="repository_search_url")
    current_user_repositories_url: str = Field(alias="current_user_repositories_url")
    starred_url: str = Field(alias="starred_url")
    starred_gists_url: str = Field(alias="starred_gists_url")
    topic_search_url: str = Field(alias="topic_search_url")
    user_url: str = Field(alias="user_url")
    user_organizations_url: str = Field(alias="user_organizations_url")
    user_repositories_url: str = Field(alias="user_repositories_url")
    user_search_url: str = Field(alias="user_search_url")
    
    class Config:
        populate_by_name = True


class Vulnerability(BaseModel):
    """Vulnerability schema from the OpenAPI specification."""
    package: Dict[str, Any] = Field(alias="package")  # The name of the package affected by the vulnerability.
    vulnerable_version_range: str = Field(alias="vulnerable_version_range")  # The range of the package versions affected by the vulnerability.
    first_patched_version: str = Field(alias="first_patched_version")  # The package version that resolves the vulnerability.
    vulnerable_functions: List[str] = Field(alias="vulnerable_functions")  # The functions in the package that are affected by the vulnerability.
    
    class Config:
        populate_by_name = True


class CvssSeverities(BaseModel):
    """CvssSeverities schema from the OpenAPI specification."""
    cvss_v3: Dict[str, Any] = Field(alias="cvss_v3")
    cvss_v4: Dict[str, Any] = Field(alias="cvss_v4")
    
    class Config:
        populate_by_name = True


class SecurityAdvisoryEpss(BaseModel):
    """SecurityAdvisoryEpss schema from the OpenAPI specification."""
    percentage: float = Field(alias="percentage")
    percentile: float = Field(alias="percentile")
    
    class Config:
        populate_by_name = True


class SimpleUser(BaseModel):
    """SimpleUser schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    starred_at: str = Field(alias="starred_at")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class GlobalAdvisory(BaseModel):
    """GlobalAdvisory schema from the OpenAPI specification."""
    ghsa_id: str = Field(alias="ghsa_id")  # The GitHub Security Advisory ID.
    cve_id: str = Field(alias="cve_id")  # The Common Vulnerabilities and Exposures (CVE) ID.
    url: str = Field(alias="url")  # The API URL for the advisory.
    html_url: str = Field(alias="html_url")  # The URL for the advisory.
    repository_advisory_url: str = Field(alias="repository_advisory_url")  # The API URL for the repository advisory.
    summary: str = Field(alias="summary")  # A short summary of the advisory.
    description: str = Field(alias="description")  # A detailed description of what the advisory entails.
    type_field: str = Field(alias="type")  # The type of advisory.
    severity: str = Field(alias="severity")  # The severity of the advisory.
    source_code_location: str = Field(alias="source_code_location")  # The URL of the advisory\'s source code.
    identifiers: List[Dict[str, Any]] = Field(alias="identifiers")
    references: List[str] = Field(alias="references")
    published_at: str = Field(alias="published_at")  # The date and time of when the advisory was published, in ISO 8601 format.
    updated_at: str = Field(alias="updated_at")  # The date and time of when the advisory was last updated, in ISO 8601 format.
    github_reviewed_at: str = Field(alias="github_reviewed_at")  # The date and time of when the advisory was reviewed by GitHub, in ISO 8601 format.
    nvd_published_at: str = Field(alias="nvd_published_at")  # The date and time when the advisory was published in the National Vulnerability Database, in ISO 8601 format.
This field is only populated when the advisory is imported from the National Vulnerability Database.
    withdrawn_at: str = Field(alias="withdrawn_at")  # The date and time of when the advisory was withdrawn, in ISO 8601 format.
    vulnerabilities: List[Vulnerability] = Field(alias="vulnerabilities")  # The products and respective version ranges affected by the advisory.
    cvss: Dict[str, Any] = Field(alias="cvss")
    cvss_severities: CvssSeverities = Field(alias="cvss_severities")
    epss: SecurityAdvisoryEpss = Field(alias="epss")  # The EPSS scores as calculated by the [Exploit Prediction Scoring System](https://www.first.org/epss).
    cwes: List[Dict[str, Any]] = Field(alias="cwes")
    credits: List[Dict[str, Any]] = Field(alias="credits")  # The users who contributed to the advisory.
    
    class Config:
        populate_by_name = True


class BasicError(BaseModel):
    """BasicError schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    documentation_url: str = Field(alias="documentation_url")
    url: str = Field(alias="url")
    status: str = Field(alias="status")
    
    class Config:
        populate_by_name = True


class ValidationErrorSimple(BaseModel):
    """ValidationErrorSimple schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    documentation_url: str = Field(alias="documentation_url")
    errors: List[str] = Field(alias="errors")
    
    class Config:
        populate_by_name = True


class Enterprise(BaseModel):
    """Enterprise schema from the OpenAPI specification."""
    description: str = Field(alias="description")  # A short description of the enterprise.
    html_url: str = Field(alias="html_url")
    website_url: str = Field(alias="website_url")  # The enterprise\'s website URL.
    id_field: int = Field(alias="id")  # Unique identifier of the enterprise
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the enterprise.
    slug: str = Field(alias="slug")  # The slug url identifier for the enterprise.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    avatar_url: str = Field(alias="avatar_url")
    
    class Config:
        populate_by_name = True


class Integration(BaseModel):
    """Integration schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the GitHub app
    slug: str = Field(alias="slug")  # The slug name of the GitHub app
    node_id: str = Field(alias="node_id")
    client_id: str = Field(alias="client_id")
    owner: Any = Field(alias="owner")
    name: str = Field(alias="name")  # The name of the GitHub app
    description: str = Field(alias="description")
    external_url: str = Field(alias="external_url")
    html_url: str = Field(alias="html_url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    permissions: Dict[str, Any] = Field(alias="permissions")  # The set of permissions for the GitHub app
    events: List[str] = Field(alias="events")  # The list of events for the GitHub app. Note that the `installation_target`, `security_advisory`, and `meta` events are not included because they are global events and not specific to an installation.
    installations_count: int = Field(alias="installations_count")  # The number of installations associated with the GitHub app. Only returned when the integration is requesting details about itself.
    
    class Config:
        populate_by_name = True


class WebhookConfig(BaseModel):
    """WebhookConfig schema from the OpenAPI specification."""
    url: str = Field(alias="url")  # The URL to which the payloads will be delivered.
    content_type: str = Field(alias="content_type")  # The media type used to serialize the payloads. Supported values include `json` and `form`. The default is `form`.
    secret: str = Field(alias="secret")  # If provided, the `secret` will be used as the `key` to generate the HMAC hex digest value for [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
    insecure_ssl: str = Field(alias="insecure_ssl")
    
    class Config:
        populate_by_name = True


class HookDeliveryItem(BaseModel):
    """HookDeliveryItem schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the webhook delivery.
    guid: str = Field(alias="guid")  # Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event).
    delivered_at: str = Field(alias="delivered_at")  # Time when the webhook delivery occurred.
    redelivery: bool = Field(alias="redelivery")  # Whether the webhook delivery is a redelivery.
    duration: float = Field(alias="duration")  # Time spent delivering.
    status: str = Field(alias="status")  # Describes the response returned after attempting the delivery.
    status_code: int = Field(alias="status_code")  # Status code received when delivery was made.
    event: str = Field(alias="event")  # The event that triggered the delivery.
    action: str = Field(alias="action")  # The type of activity for the event that triggered the delivery.
    installation_id: int = Field(alias="installation_id")  # The id of the GitHub App installation associated with this event.
    repository_id: int = Field(alias="repository_id")  # The id of the repository associated with this event.
    throttled_at: str = Field(alias="throttled_at")  # Time when the webhook delivery was throttled.
    
    class Config:
        populate_by_name = True


class ScimError(BaseModel):
    """ScimError schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    documentation_url: str = Field(alias="documentation_url")
    detail: str = Field(alias="detail")
    status: int = Field(alias="status")
    scim_type: str = Field(alias="scimType")
    schemas: List[str] = Field(alias="schemas")
    
    class Config:
        populate_by_name = True


class ValidationError(BaseModel):
    """ValidationError schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    documentation_url: str = Field(alias="documentation_url")
    errors: List[Dict[str, Any]] = Field(alias="errors")
    
    class Config:
        populate_by_name = True


class HookDelivery(BaseModel):
    """HookDelivery schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the delivery.
    guid: str = Field(alias="guid")  # Unique identifier for the event (shared with all deliveries for all webhooks that subscribe to this event).
    delivered_at: str = Field(alias="delivered_at")  # Time when the delivery was delivered.
    redelivery: bool = Field(alias="redelivery")  # Whether the delivery is a redelivery.
    duration: float = Field(alias="duration")  # Time spent delivering.
    status: str = Field(alias="status")  # Description of the status of the attempted delivery
    status_code: int = Field(alias="status_code")  # Status code received when delivery was made.
    event: str = Field(alias="event")  # The event that triggered the delivery.
    action: str = Field(alias="action")  # The type of activity for the event that triggered the delivery.
    installation_id: int = Field(alias="installation_id")  # The id of the GitHub App installation associated with this event.
    repository_id: int = Field(alias="repository_id")  # The id of the repository associated with this event.
    throttled_at: str = Field(alias="throttled_at")  # Time when the webhook delivery was throttled.
    url: str = Field(alias="url")  # The URL target of the delivery.
    request: Dict[str, Any] = Field(alias="request")
    response: Dict[str, Any] = Field(alias="response")
    
    class Config:
        populate_by_name = True


class IntegrationInstallationRequest(BaseModel):
    """IntegrationInstallationRequest schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the request installation.
    node_id: str = Field(alias="node_id")
    account: Any = Field(alias="account")
    requester: SimpleUser = Field(alias="requester")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class AppPermissions(BaseModel):
    """AppPermissions schema from the OpenAPI specification."""
    actions: str = Field(alias="actions")  # The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.
    administration: str = Field(alias="administration")  # The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.
    checks: str = Field(alias="checks")  # The level of permission to grant the access token for checks on code.
    codespaces: str = Field(alias="codespaces")  # The level of permission to grant the access token to create, edit, delete, and list Codespaces.
    contents: str = Field(alias="contents")  # The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.
    dependabot_secrets: str = Field(alias="dependabot_secrets")  # The level of permission to grant the access token to manage Dependabot secrets.
    deployments: str = Field(alias="deployments")  # The level of permission to grant the access token for deployments and deployment statuses.
    environments: str = Field(alias="environments")  # The level of permission to grant the access token for managing repository environments.
    issues: str = Field(alias="issues")  # The level of permission to grant the access token for issues and related comments, assignees, labels, and milestones.
    metadata: str = Field(alias="metadata")  # The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.
    packages: str = Field(alias="packages")  # The level of permission to grant the access token for packages published to GitHub Packages.
    pages: str = Field(alias="pages")  # The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.
    pull_requests: str = Field(alias="pull_requests")  # The level of permission to grant the access token for pull requests and related comments, assignees, labels, milestones, and merges.
    repository_custom_properties: str = Field(alias="repository_custom_properties")  # The level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.
    repository_hooks: str = Field(alias="repository_hooks")  # The level of permission to grant the access token to manage the post-receive hooks for a repository.
    repository_projects: str = Field(alias="repository_projects")  # The level of permission to grant the access token to manage repository projects, columns, and cards.
    secret_scanning_alerts: str = Field(alias="secret_scanning_alerts")  # The level of permission to grant the access token to view and manage secret scanning alerts.
    secrets: str = Field(alias="secrets")  # The level of permission to grant the access token to manage repository secrets.
    security_events: str = Field(alias="security_events")  # The level of permission to grant the access token to view and manage security events like code scanning alerts.
    single_file: str = Field(alias="single_file")  # The level of permission to grant the access token to manage just a single file.
    statuses: str = Field(alias="statuses")  # The level of permission to grant the access token for commit statuses.
    vulnerability_alerts: str = Field(alias="vulnerability_alerts")  # The level of permission to grant the access token to manage Dependabot alerts.
    workflows: str = Field(alias="workflows")  # The level of permission to grant the access token to update GitHub Actions workflow files.
    members: str = Field(alias="members")  # The level of permission to grant the access token for organization teams and members.
    organization_administration: str = Field(alias="organization_administration")  # The level of permission to grant the access token to manage access to an organization.
    organization_custom_roles: str = Field(alias="organization_custom_roles")  # The level of permission to grant the access token for custom repository roles management.
    organization_custom_org_roles: str = Field(alias="organization_custom_org_roles")  # The level of permission to grant the access token for custom organization roles management.
    organization_custom_properties: str = Field(alias="organization_custom_properties")  # The level of permission to grant the access token for custom property management.
    organization_copilot_seat_management: str = Field(alias="organization_copilot_seat_management")  # The level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.
    organization_announcement_banners: str = Field(alias="organization_announcement_banners")  # The level of permission to grant the access token to view and manage announcement banners for an organization.
    organization_events: str = Field(alias="organization_events")  # The level of permission to grant the access token to view events triggered by an activity in an organization.
    organization_hooks: str = Field(alias="organization_hooks")  # The level of permission to grant the access token to manage the post-receive hooks for an organization.
    organization_personal_access_tokens: str = Field(alias="organization_personal_access_tokens")  # The level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.
    organization_personal_access_token_requests: str = Field(alias="organization_personal_access_token_requests")  # The level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.
    organization_plan: str = Field(alias="organization_plan")  # The level of permission to grant the access token for viewing an organization\'s plan.
    organization_projects: str = Field(alias="organization_projects")  # The level of permission to grant the access token to manage organization projects and projects public preview (where available).
    organization_packages: str = Field(alias="organization_packages")  # The level of permission to grant the access token for organization packages published to GitHub Packages.
    organization_secrets: str = Field(alias="organization_secrets")  # The level of permission to grant the access token to manage organization secrets.
    organization_self_hosted_runners: str = Field(alias="organization_self_hosted_runners")  # The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.
    organization_user_blocking: str = Field(alias="organization_user_blocking")  # The level of permission to grant the access token to view and manage users blocked by the organization.
    team_discussions: str = Field(alias="team_discussions")  # The level of permission to grant the access token to manage team discussions and related comments.
    email_addresses: str = Field(alias="email_addresses")  # The level of permission to grant the access token to manage the email addresses belonging to a user.
    followers: str = Field(alias="followers")  # The level of permission to grant the access token to manage the followers belonging to a user.
    git_ssh_keys: str = Field(alias="git_ssh_keys")  # The level of permission to grant the access token to manage git SSH keys.
    gpg_keys: str = Field(alias="gpg_keys")  # The level of permission to grant the access token to view and manage GPG keys belonging to a user.
    interaction_limits: str = Field(alias="interaction_limits")  # The level of permission to grant the access token to view and manage interaction limits on a repository.
    profile: str = Field(alias="profile")  # The level of permission to grant the access token to manage the profile settings belonging to a user.
    starring: str = Field(alias="starring")  # The level of permission to grant the access token to list and manage repositories a user is starring.
    
    class Config:
        populate_by_name = True


class NullableSimpleUser(BaseModel):
    """NullableSimpleUser schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    starred_at: str = Field(alias="starred_at")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class Installation(BaseModel):
    """Installation schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the installation.
    account: Any = Field(alias="account")
    repository_selection: str = Field(alias="repository_selection")  # Describe whether all repositories have been selected or there\'s a selection involved
    access_tokens_url: str = Field(alias="access_tokens_url")
    repositories_url: str = Field(alias="repositories_url")
    html_url: str = Field(alias="html_url")
    app_id: int = Field(alias="app_id")
    target_id: int = Field(alias="target_id")  # The ID of the user or organization this token is being scoped to.
    target_type: str = Field(alias="target_type")
    permissions: AppPermissions = Field(alias="permissions")  # The permissions granted to the user access token.
    events: List[str] = Field(alias="events")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    single_file_name: str = Field(alias="single_file_name")
    has_multiple_single_files: bool = Field(alias="has_multiple_single_files")
    single_file_paths: List[str] = Field(alias="single_file_paths")
    app_slug: str = Field(alias="app_slug")
    suspended_by: NullableSimpleUser = Field(alias="suspended_by")  # A GitHub user.
    suspended_at: str = Field(alias="suspended_at")
    contact_email: str = Field(alias="contact_email")
    
    class Config:
        populate_by_name = True


class NullableLicenseSimple(BaseModel):
    """NullableLicenseSimple schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    url: str = Field(alias="url")
    spdx_id: str = Field(alias="spdx_id")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class Repository(BaseModel):
    """Repository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    forks: int = Field(alias="forks")
    permissions: Dict[str, Any] = Field(alias="permissions")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private or public.
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")  # The default branch of the repository.
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")  # Whether this repository acts as a template that can be used to generate new repositories.
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")  # Whether issues are enabled.
    has_projects: bool = Field(alias="has_projects")  # Whether projects are enabled.
    has_wiki: bool = Field(alias="has_wiki")  # Whether the wiki is enabled.
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")  # Whether downloads are enabled.
    has_discussions: bool = Field(alias="has_discussions")  # Whether discussions are enabled.
    archived: bool = Field(alias="archived")  # Whether the repository is archived.
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")  # Whether to allow rebase merges for pull requests.
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")  # Whether to allow squash merges for pull requests.
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow Auto-merge to be used on pull requests.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged
    allow_update_branch: bool = Field(alias="allow_update_branch")  # Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")  # Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:

- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:

- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.

- `PR_TITLE` - default to the pull request\'s title.
- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.

- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    allow_merge_commit: bool = Field(alias="allow_merge_commit")  # Whether to allow merge commits for pull requests.
    allow_forking: bool = Field(alias="allow_forking")  # Whether to allow forking this repo
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")  # Whether to require contributors to sign off on web-based commits
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    master_branch: str = Field(alias="master_branch")
    starred_at: str = Field(alias="starred_at")
    anonymous_access_enabled: bool = Field(alias="anonymous_access_enabled")  # Whether anonymous git access is enabled for this repository
    code_search_index_status: Dict[str, Any] = Field(alias="code_search_index_status")  # The status of the code search index for this repository
    
    class Config:
        populate_by_name = True


class InstallationToken(BaseModel):
    """InstallationToken schema from the OpenAPI specification."""
    token: str = Field(alias="token")
    expires_at: str = Field(alias="expires_at")
    permissions: AppPermissions = Field(alias="permissions")  # The permissions granted to the user access token.
    repository_selection: str = Field(alias="repository_selection")
    repositories: List[Repository] = Field(alias="repositories")
    single_file: str = Field(alias="single_file")
    has_multiple_single_files: bool = Field(alias="has_multiple_single_files")
    single_file_paths: List[str] = Field(alias="single_file_paths")
    
    class Config:
        populate_by_name = True


class NullableScopedInstallation(BaseModel):
    """NullableScopedInstallation schema from the OpenAPI specification."""
    permissions: AppPermissions = Field(alias="permissions")  # The permissions granted to the user access token.
    repository_selection: str = Field(alias="repository_selection")  # Describe whether all repositories have been selected or there\'s a selection involved
    single_file_name: str = Field(alias="single_file_name")
    has_multiple_single_files: bool = Field(alias="has_multiple_single_files")
    single_file_paths: List[str] = Field(alias="single_file_paths")
    repositories_url: str = Field(alias="repositories_url")
    account: SimpleUser = Field(alias="account")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class Authorization(BaseModel):
    """Authorization schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    url: str = Field(alias="url")
    scopes: List[str] = Field(alias="scopes")  # A list of scopes that this authorization is in.
    token: str = Field(alias="token")
    token_last_eight: str = Field(alias="token_last_eight")
    hashed_token: str = Field(alias="hashed_token")
    app: Dict[str, Any] = Field(alias="app")
    note: str = Field(alias="note")
    note_url: str = Field(alias="note_url")
    updated_at: str = Field(alias="updated_at")
    created_at: str = Field(alias="created_at")
    fingerprint: str = Field(alias="fingerprint")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    installation: NullableScopedInstallation = Field(alias="installation")
    expires_at: str = Field(alias="expires_at")
    
    class Config:
        populate_by_name = True


class SimpleClassroomRepository(BaseModel):
    """SimpleClassroomRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # A unique identifier of the repository.
    full_name: str = Field(alias="full_name")  # The full, globally unique name of the repository.
    html_url: str = Field(alias="html_url")  # The URL to view the repository on GitHub.com.
    node_id: str = Field(alias="node_id")  # The GraphQL identifier of the repository.
    private: bool = Field(alias="private")  # Whether the repository is private.
    default_branch: str = Field(alias="default_branch")  # The default branch for the repository.
    
    class Config:
        populate_by_name = True


class SimpleClassroomOrganization(BaseModel):
    """SimpleClassroomOrganization schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    name: str = Field(alias="name")
    avatar_url: str = Field(alias="avatar_url")
    
    class Config:
        populate_by_name = True


class Classroom(BaseModel):
    """Classroom schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the classroom.
    name: str = Field(alias="name")  # The name of the classroom.
    archived: bool = Field(alias="archived")  # Whether classroom is archived.
    organization: SimpleClassroomOrganization = Field(alias="organization")  # A GitHub organization.
    url: str = Field(alias="url")  # The URL of the classroom on GitHub Classroom.
    
    class Config:
        populate_by_name = True


class ClassroomAssignment(BaseModel):
    """ClassroomAssignment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository.
    public_repo: bool = Field(alias="public_repo")  # Whether an accepted assignment creates a public repository.
    title: str = Field(alias="title")  # Assignment title.
    type_field: str = Field(alias="type")  # Whether it\'s a group assignment or individual assignment.
    invite_link: str = Field(alias="invite_link")  # The link that a student can use to accept the assignment.
    invitations_enabled: bool = Field(alias="invitations_enabled")  # Whether the invitation link is enabled. Visiting an enabled invitation link will accept the assignment.
    slug: str = Field(alias="slug")  # Sluggified name of the assignment.
    students_are_repo_admins: bool = Field(alias="students_are_repo_admins")  # Whether students are admins on created repository when a student accepts the assignment.
    feedback_pull_requests_enabled: bool = Field(alias="feedback_pull_requests_enabled")  # Whether feedback pull request will be created when a student accepts the assignment.
    max_teams: int = Field(alias="max_teams")  # The maximum allowable teams for the assignment.
    max_members: int = Field(alias="max_members")  # The maximum allowable members per team.
    editor: str = Field(alias="editor")  # The selected editor for the assignment.
    accepted: int = Field(alias="accepted")  # The number of students that have accepted the assignment.
    submitted: int = Field(alias="submitted")  # The number of students that have submitted the assignment.
    passing: int = Field(alias="passing")  # The number of students that have passed the assignment.
    language: str = Field(alias="language")  # The programming language used in the assignment.
    deadline: str = Field(alias="deadline")  # The time at which the assignment is due.
    starter_code_repository: SimpleClassroomRepository = Field(alias="starter_code_repository")  # A GitHub repository view for Classroom
    classroom: Classroom = Field(alias="classroom")  # A GitHub Classroom classroom
    
    class Config:
        populate_by_name = True


class SimpleClassroomUser(BaseModel):
    """SimpleClassroomUser schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    avatar_url: str = Field(alias="avatar_url")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class SimpleClassroom(BaseModel):
    """SimpleClassroom schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the classroom.
    name: str = Field(alias="name")  # The name of the classroom.
    archived: bool = Field(alias="archived")  # Returns whether classroom is archived or not.
    url: str = Field(alias="url")  # The url of the classroom on GitHub Classroom.
    
    class Config:
        populate_by_name = True


class SimpleClassroomAssignment(BaseModel):
    """SimpleClassroomAssignment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository.
    public_repo: bool = Field(alias="public_repo")  # Whether an accepted assignment creates a public repository.
    title: str = Field(alias="title")  # Assignment title.
    type_field: str = Field(alias="type")  # Whether it\'s a Group Assignment or Individual Assignment.
    invite_link: str = Field(alias="invite_link")  # The link that a student can use to accept the assignment.
    invitations_enabled: bool = Field(alias="invitations_enabled")  # Whether the invitation link is enabled. Visiting an enabled invitation link will accept the assignment.
    slug: str = Field(alias="slug")  # Sluggified name of the assignment.
    students_are_repo_admins: bool = Field(alias="students_are_repo_admins")  # Whether students are admins on created repository on accepted assignment.
    feedback_pull_requests_enabled: bool = Field(alias="feedback_pull_requests_enabled")  # Whether feedback pull request will be created on assignment acceptance.
    max_teams: int = Field(alias="max_teams")  # The maximum allowable teams for the assignment.
    max_members: int = Field(alias="max_members")  # The maximum allowable members per team.
    editor: str = Field(alias="editor")  # The selected editor for the assignment.
    accepted: int = Field(alias="accepted")  # The number of students that have accepted the assignment.
    submitted: int = Field(alias="submitted")  # The number of students that have submitted the assignment.
    passing: int = Field(alias="passing")  # The number of students that have passed the assignment.
    language: str = Field(alias="language")  # The programming language used in the assignment.
    deadline: str = Field(alias="deadline")  # The time at which the assignment is due.
    classroom: SimpleClassroom = Field(alias="classroom")  # A GitHub Classroom classroom
    
    class Config:
        populate_by_name = True


class ClassroomAcceptedAssignment(BaseModel):
    """ClassroomAcceptedAssignment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository.
    submitted: bool = Field(alias="submitted")  # Whether an accepted assignment has been submitted.
    passing: bool = Field(alias="passing")  # Whether a submission passed.
    commit_count: int = Field(alias="commit_count")  # Count of student commits.
    grade: str = Field(alias="grade")  # Most recent grade.
    students: List[SimpleClassroomUser] = Field(alias="students")
    repository: SimpleClassroomRepository = Field(alias="repository")  # A GitHub repository view for Classroom
    assignment: SimpleClassroomAssignment = Field(alias="assignment")  # A GitHub Classroom assignment
    
    class Config:
        populate_by_name = True


class ClassroomAssignmentGrade(BaseModel):
    """ClassroomAssignmentGrade schema from the OpenAPI specification."""
    assignment_name: str = Field(alias="assignment_name")  # Name of the assignment
    assignment_url: str = Field(alias="assignment_url")  # URL of the assignment
    starter_code_url: str = Field(alias="starter_code_url")  # URL of the starter code for the assignment
    github_username: str = Field(alias="github_username")  # GitHub username of the student
    roster_identifier: str = Field(alias="roster_identifier")  # Roster identifier of the student
    student_repository_name: str = Field(alias="student_repository_name")  # Name of the student\'s assignment repository
    student_repository_url: str = Field(alias="student_repository_url")  # URL of the student\'s assignment repository
    submission_timestamp: str = Field(alias="submission_timestamp")  # Timestamp of the student\'s assignment submission
    points_awarded: int = Field(alias="points_awarded")  # Number of points awarded to the student
    points_available: int = Field(alias="points_available")  # Number of points available for the assignment
    group_name: str = Field(alias="group_name")  # If a group assignment, name of the group the student is in
    
    class Config:
        populate_by_name = True


class CodeOfConduct(BaseModel):
    """CodeOfConduct schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    url: str = Field(alias="url")
    body: str = Field(alias="body")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class CodeSecurityConfiguration(BaseModel):
    """CodeSecurityConfiguration schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the code security configuration
    name: str = Field(alias="name")  # The name of the code security configuration. Must be unique within the organization.
    target_type: str = Field(alias="target_type")  # The type of the code security configuration.
    description: str = Field(alias="description")  # A description of the code security configuration
    advanced_security: str = Field(alias="advanced_security")  # The enablement status of GitHub Advanced Security
    dependency_graph: str = Field(alias="dependency_graph")  # The enablement status of Dependency Graph
    dependency_graph_autosubmit_action: str = Field(alias="dependency_graph_autosubmit_action")  # The enablement status of Automatic dependency submission
    dependency_graph_autosubmit_action_options: Dict[str, Any] = Field(alias="dependency_graph_autosubmit_action_options")  # Feature options for Automatic dependency submission
    dependabot_alerts: str = Field(alias="dependabot_alerts")  # The enablement status of Dependabot alerts
    dependabot_security_updates: str = Field(alias="dependabot_security_updates")  # The enablement status of Dependabot security updates
    code_scanning_options: Dict[str, Any] = Field(alias="code_scanning_options")  # Feature options for code scanning
    code_scanning_default_setup: str = Field(alias="code_scanning_default_setup")  # The enablement status of code scanning default setup
    code_scanning_default_setup_options: Dict[str, Any] = Field(alias="code_scanning_default_setup_options")  # Feature options for code scanning default setup
    code_scanning_delegated_alert_dismissal: str = Field(alias="code_scanning_delegated_alert_dismissal")  # The enablement status of code scanning delegated alert dismissal
    secret_scanning: str = Field(alias="secret_scanning")  # The enablement status of secret scanning
    secret_scanning_push_protection: str = Field(alias="secret_scanning_push_protection")  # The enablement status of secret scanning push protection
    secret_scanning_delegated_bypass: str = Field(alias="secret_scanning_delegated_bypass")  # The enablement status of secret scanning delegated bypass
    secret_scanning_delegated_bypass_options: Dict[str, Any] = Field(alias="secret_scanning_delegated_bypass_options")  # Feature options for secret scanning delegated bypass
    secret_scanning_validity_checks: str = Field(alias="secret_scanning_validity_checks")  # The enablement status of secret scanning validity checks
    secret_scanning_non_provider_patterns: str = Field(alias="secret_scanning_non_provider_patterns")  # The enablement status of secret scanning non-provider patterns
    secret_scanning_generic_secrets: str = Field(alias="secret_scanning_generic_secrets")  # The enablement status of Copilot secret scanning
    secret_scanning_delegated_alert_dismissal: str = Field(alias="secret_scanning_delegated_alert_dismissal")  # The enablement status of secret scanning delegated alert dismissal
    private_vulnerability_reporting: str = Field(alias="private_vulnerability_reporting")  # The enablement status of private vulnerability reporting
    enforcement: str = Field(alias="enforcement")  # The enforcement status for a security configuration
    url: str = Field(alias="url")  # The URL of the configuration
    html_url: str = Field(alias="html_url")  # The URL of the configuration
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class CodeScanningDefaultSetupOptions(BaseModel):
    """CodeScanningDefaultSetupOptions schema from the OpenAPI specification."""
    runner_type: str = Field(alias="runner_type")  # Whether to use labeled runners or standard GitHub runners.
    runner_label: str = Field(alias="runner_label")  # The label of the runner to use for code scanning default setup when runner_type is \'labeled\'.
    
    class Config:
        populate_by_name = True


class SimpleRepository(BaseModel):
    """SimpleRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # A unique identifier of the repository.
    node_id: str = Field(alias="node_id")  # The GraphQL identifier of the repository.
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")  # The full, globally unique, name of the repository.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private.
    html_url: str = Field(alias="html_url")  # The URL to view the repository on GitHub.com.
    description: str = Field(alias="description")  # The repository description.
    fork: bool = Field(alias="fork")  # Whether the repository is a fork.
    url: str = Field(alias="url")  # The URL to get more information about the repository from the GitHub API.
    archive_url: str = Field(alias="archive_url")  # A template for the API URL to download the repository as an archive.
    assignees_url: str = Field(alias="assignees_url")  # A template for the API URL to list the available assignees for issues in the repository.
    blobs_url: str = Field(alias="blobs_url")  # A template for the API URL to create or retrieve a raw Git blob in the repository.
    branches_url: str = Field(alias="branches_url")  # A template for the API URL to get information about branches in the repository.
    collaborators_url: str = Field(alias="collaborators_url")  # A template for the API URL to get information about collaborators of the repository.
    comments_url: str = Field(alias="comments_url")  # A template for the API URL to get information about comments on the repository.
    commits_url: str = Field(alias="commits_url")  # A template for the API URL to get information about commits on the repository.
    compare_url: str = Field(alias="compare_url")  # A template for the API URL to compare two commits or refs.
    contents_url: str = Field(alias="contents_url")  # A template for the API URL to get the contents of the repository.
    contributors_url: str = Field(alias="contributors_url")  # A template for the API URL to list the contributors to the repository.
    deployments_url: str = Field(alias="deployments_url")  # The API URL to list the deployments of the repository.
    downloads_url: str = Field(alias="downloads_url")  # The API URL to list the downloads on the repository.
    events_url: str = Field(alias="events_url")  # The API URL to list the events of the repository.
    forks_url: str = Field(alias="forks_url")  # The API URL to list the forks of the repository.
    git_commits_url: str = Field(alias="git_commits_url")  # A template for the API URL to get information about Git commits of the repository.
    git_refs_url: str = Field(alias="git_refs_url")  # A template for the API URL to get information about Git refs of the repository.
    git_tags_url: str = Field(alias="git_tags_url")  # A template for the API URL to get information about Git tags of the repository.
    issue_comment_url: str = Field(alias="issue_comment_url")  # A template for the API URL to get information about issue comments on the repository.
    issue_events_url: str = Field(alias="issue_events_url")  # A template for the API URL to get information about issue events on the repository.
    issues_url: str = Field(alias="issues_url")  # A template for the API URL to get information about issues on the repository.
    keys_url: str = Field(alias="keys_url")  # A template for the API URL to get information about deploy keys on the repository.
    labels_url: str = Field(alias="labels_url")  # A template for the API URL to get information about labels of the repository.
    languages_url: str = Field(alias="languages_url")  # The API URL to get information about the languages of the repository.
    merges_url: str = Field(alias="merges_url")  # The API URL to merge branches in the repository.
    milestones_url: str = Field(alias="milestones_url")  # A template for the API URL to get information about milestones of the repository.
    notifications_url: str = Field(alias="notifications_url")  # A template for the API URL to get information about notifications on the repository.
    pulls_url: str = Field(alias="pulls_url")  # A template for the API URL to get information about pull requests on the repository.
    releases_url: str = Field(alias="releases_url")  # A template for the API URL to get information about releases on the repository.
    stargazers_url: str = Field(alias="stargazers_url")  # The API URL to list the stargazers on the repository.
    statuses_url: str = Field(alias="statuses_url")  # A template for the API URL to get information about statuses of a commit.
    subscribers_url: str = Field(alias="subscribers_url")  # The API URL to list the subscribers on the repository.
    subscription_url: str = Field(alias="subscription_url")  # The API URL to subscribe to notifications for this repository.
    tags_url: str = Field(alias="tags_url")  # The API URL to get information about tags on the repository.
    teams_url: str = Field(alias="teams_url")  # The API URL to list the teams on the repository.
    trees_url: str = Field(alias="trees_url")  # A template for the API URL to create or retrieve a raw Git tree of the repository.
    hooks_url: str = Field(alias="hooks_url")  # The API URL to list the hooks on the repository.
    
    class Config:
        populate_by_name = True


class CodeSecurityConfigurationRepositories(BaseModel):
    """CodeSecurityConfigurationRepositories schema from the OpenAPI specification."""
    status: str = Field(alias="status")  # The attachment status of the code security configuration on the repository.
    repository: SimpleRepository = Field(alias="repository")  # A GitHub repository.
    
    class Config:
        populate_by_name = True


class DependabotAlertPackage(BaseModel):
    """DependabotAlertPackage schema from the OpenAPI specification."""
    ecosystem: str = Field(alias="ecosystem")  # The package\'s language or package management ecosystem.
    name: str = Field(alias="name")  # The unique package name within its ecosystem.
    
    class Config:
        populate_by_name = True


class DependabotAlertSecurityVulnerability(BaseModel):
    """DependabotAlertSecurityVulnerability schema from the OpenAPI specification."""
    package: DependabotAlertPackage = Field(alias="package")  # Details for the vulnerable package.
    severity: str = Field(alias="severity")  # The severity of the vulnerability.
    vulnerable_version_range: str = Field(alias="vulnerable_version_range")  # Conditions that identify vulnerable versions of this vulnerability\'s package.
    first_patched_version: Dict[str, Any] = Field(alias="first_patched_version")  # Details pertaining to the package version that patches this vulnerability.
    
    class Config:
        populate_by_name = True


class DependabotAlertSecurityAdvisory(BaseModel):
    """DependabotAlertSecurityAdvisory schema from the OpenAPI specification."""
    ghsa_id: str = Field(alias="ghsa_id")  # The unique GitHub Security Advisory ID assigned to the advisory.
    cve_id: str = Field(alias="cve_id")  # The unique CVE ID assigned to the advisory.
    summary: str = Field(alias="summary")  # A short, plain text summary of the advisory.
    description: str = Field(alias="description")  # A long-form Markdown-supported description of the advisory.
    vulnerabilities: List[DependabotAlertSecurityVulnerability] = Field(alias="vulnerabilities")  # Vulnerable version range information for the advisory.
    severity: str = Field(alias="severity")  # The severity of the advisory.
    cvss: Dict[str, Any] = Field(alias="cvss")  # Details for the advisory pertaining to the Common Vulnerability Scoring System.
    cvss_severities: CvssSeverities = Field(alias="cvss_severities")
    epss: SecurityAdvisoryEpss = Field(alias="epss")  # The EPSS scores as calculated by the [Exploit Prediction Scoring System](https://www.first.org/epss).
    cwes: List[Dict[str, Any]] = Field(alias="cwes")  # Details for the advisory pertaining to Common Weakness Enumeration.
    identifiers: List[Dict[str, Any]] = Field(alias="identifiers")  # Values that identify this advisory among security information sources.
    references: List[Dict[str, Any]] = Field(alias="references")  # Links to additional advisory information.
    published_at: str = Field(alias="published_at")  # The time that the advisory was published in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the advisory was last modified in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    withdrawn_at: str = Field(alias="withdrawn_at")  # The time that the advisory was withdrawn in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    
    class Config:
        populate_by_name = True


class DependabotAlertWithRepository(BaseModel):
    """DependabotAlertWithRepository schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    state: str = Field(alias="state")  # The state of the Dependabot alert.
    dependency: Dict[str, Any] = Field(alias="dependency")  # Details for the vulnerable dependency.
    security_advisory: DependabotAlertSecurityAdvisory = Field(alias="security_advisory")  # Details for the GitHub Security Advisory.
    security_vulnerability: DependabotAlertSecurityVulnerability = Field(alias="security_vulnerability")  # Details pertaining to one vulnerable version range for the advisory.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_at: str = Field(alias="dismissed_at")  # The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_by: NullableSimpleUser = Field(alias="dismissed_by")  # A GitHub user.
    dismissed_reason: str = Field(alias="dismissed_reason")  # The reason that the alert was dismissed.
    dismissed_comment: str = Field(alias="dismissed_comment")  # An optional comment associated with the alert\'s dismissal.
    fixed_at: str = Field(alias="fixed_at")  # The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    auto_dismissed_at: str = Field(alias="auto_dismissed_at")  # The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    repository: SimpleRepository = Field(alias="repository")  # A GitHub repository.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationCommit(BaseModel):
    """SecretScanningLocationCommit schema from the OpenAPI specification."""
    path: str = Field(alias="path")  # The file path in the repository
    start_line: float = Field(alias="start_line")  # Line number at which the secret starts in the file
    end_line: float = Field(alias="end_line")  # Line number at which the secret ends in the file
    start_column: float = Field(alias="start_column")  # The column at which the secret starts within the start line when the file is interpreted as 8BIT ASCII
    end_column: float = Field(alias="end_column")  # The column at which the secret ends within the end line when the file is interpreted as 8BIT ASCII
    blob_sha: str = Field(alias="blob_sha")  # SHA-1 hash ID of the associated blob
    blob_url: str = Field(alias="blob_url")  # The API URL to get the associated blob resource
    commit_sha: str = Field(alias="commit_sha")  # SHA-1 hash ID of the associated commit
    commit_url: str = Field(alias="commit_url")  # The API URL to get the associated commit resource
    
    class Config:
        populate_by_name = True


class SecretScanningLocationWikiCommit(BaseModel):
    """SecretScanningLocationWikiCommit schema from the OpenAPI specification."""
    path: str = Field(alias="path")  # The file path of the wiki page
    start_line: float = Field(alias="start_line")  # Line number at which the secret starts in the file
    end_line: float = Field(alias="end_line")  # Line number at which the secret ends in the file
    start_column: float = Field(alias="start_column")  # The column at which the secret starts within the start line when the file is interpreted as 8-bit ASCII.
    end_column: float = Field(alias="end_column")  # The column at which the secret ends within the end line when the file is interpreted as 8-bit ASCII.
    blob_sha: str = Field(alias="blob_sha")  # SHA-1 hash ID of the associated blob
    page_url: str = Field(alias="page_url")  # The GitHub URL to get the associated wiki page
    commit_sha: str = Field(alias="commit_sha")  # SHA-1 hash ID of the associated commit
    commit_url: str = Field(alias="commit_url")  # The GitHub URL to get the associated wiki commit
    
    class Config:
        populate_by_name = True


class SecretScanningLocationIssueTitle(BaseModel):
    """SecretScanningLocationIssueTitle schema from the OpenAPI specification."""
    issue_title_url: str = Field(alias="issue_title_url")  # The API URL to get the issue where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationIssueBody(BaseModel):
    """SecretScanningLocationIssueBody schema from the OpenAPI specification."""
    issue_body_url: str = Field(alias="issue_body_url")  # The API URL to get the issue where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationIssueComment(BaseModel):
    """SecretScanningLocationIssueComment schema from the OpenAPI specification."""
    issue_comment_url: str = Field(alias="issue_comment_url")  # The API URL to get the issue comment where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationDiscussionTitle(BaseModel):
    """SecretScanningLocationDiscussionTitle schema from the OpenAPI specification."""
    discussion_title_url: str = Field(alias="discussion_title_url")  # The URL to the discussion where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationDiscussionBody(BaseModel):
    """SecretScanningLocationDiscussionBody schema from the OpenAPI specification."""
    discussion_body_url: str = Field(alias="discussion_body_url")  # The URL to the discussion where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationDiscussionComment(BaseModel):
    """SecretScanningLocationDiscussionComment schema from the OpenAPI specification."""
    discussion_comment_url: str = Field(alias="discussion_comment_url")  # The API URL to get the discussion comment where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationPullRequestTitle(BaseModel):
    """SecretScanningLocationPullRequestTitle schema from the OpenAPI specification."""
    pull_request_title_url: str = Field(alias="pull_request_title_url")  # The API URL to get the pull request where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationPullRequestBody(BaseModel):
    """SecretScanningLocationPullRequestBody schema from the OpenAPI specification."""
    pull_request_body_url: str = Field(alias="pull_request_body_url")  # The API URL to get the pull request where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationPullRequestComment(BaseModel):
    """SecretScanningLocationPullRequestComment schema from the OpenAPI specification."""
    pull_request_comment_url: str = Field(alias="pull_request_comment_url")  # The API URL to get the pull request comment where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationPullRequestReview(BaseModel):
    """SecretScanningLocationPullRequestReview schema from the OpenAPI specification."""
    pull_request_review_url: str = Field(alias="pull_request_review_url")  # The API URL to get the pull request review where the secret was detected.
    
    class Config:
        populate_by_name = True


class SecretScanningLocationPullRequestReviewComment(BaseModel):
    """SecretScanningLocationPullRequestReviewComment schema from the OpenAPI specification."""
    pull_request_review_comment_url: str = Field(alias="pull_request_review_comment_url")  # The API URL to get the pull request review comment where the secret was detected.
    
    class Config:
        populate_by_name = True


class OrganizationSecretScanningAlert(BaseModel):
    """OrganizationSecretScanningAlert schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    locations_url: str = Field(alias="locations_url")  # The REST API URL of the code locations for this alert.
    state: str = Field(alias="state")  # Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`.
    resolution: str = Field(alias="resolution")  # **Required when the `state` is `resolved`.** The reason for resolving the alert.
    resolved_at: str = Field(alias="resolved_at")  # The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    resolved_by: NullableSimpleUser = Field(alias="resolved_by")  # A GitHub user.
    secret_type: str = Field(alias="secret_type")  # The type of secret that secret scanning detected.
    secret_type_display_name: str = Field(alias="secret_type_display_name")  # User-friendly name for the detected secret, matching the `secret_type`.
For a list of built-in patterns, see \"[Supported secret scanning patterns](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).\"
    secret: str = Field(alias="secret")  # The secret that was detected.
    repository: SimpleRepository = Field(alias="repository")  # A GitHub repository.
    push_protection_bypassed: bool = Field(alias="push_protection_bypassed")  # Whether push protection was bypassed for the detected secret.
    push_protection_bypassed_by: NullableSimpleUser = Field(alias="push_protection_bypassed_by")  # A GitHub user.
    push_protection_bypassed_at: str = Field(alias="push_protection_bypassed_at")  # The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    push_protection_bypass_request_reviewer: NullableSimpleUser = Field(alias="push_protection_bypass_request_reviewer")  # A GitHub user.
    push_protection_bypass_request_reviewer_comment: str = Field(alias="push_protection_bypass_request_reviewer_comment")  # An optional comment when reviewing a push protection bypass.
    push_protection_bypass_request_comment: str = Field(alias="push_protection_bypass_request_comment")  # An optional comment when requesting a push protection bypass.
    push_protection_bypass_request_html_url: str = Field(alias="push_protection_bypass_request_html_url")  # The URL to a push protection bypass request.
    resolution_comment: str = Field(alias="resolution_comment")  # The comment that was optionally added when this alert was closed
    validity: str = Field(alias="validity")  # The token status as of the latest validity check.
    publicly_leaked: bool = Field(alias="publicly_leaked")  # Whether the secret was publicly leaked.
    multi_repo: bool = Field(alias="multi_repo")  # Whether the detected secret was found in multiple repositories in the same organization or enterprise.
    is_base64_encoded: bool = Field(alias="is_base64_encoded")  # A boolean value representing whether or not alert is base64 encoded
    first_location_detected: Any = Field(alias="first_location_detected")  # Details on the location where the token was initially detected. This can be a commit, wiki commit, issue, discussion, pull request.
    has_more_locations: bool = Field(alias="has_more_locations")  # A boolean value representing whether or not the token in the alert was detected in more than one location.
    
    class Config:
        populate_by_name = True


class Actor(BaseModel):
    """Actor schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    display_login: str = Field(alias="display_login")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    avatar_url: str = Field(alias="avatar_url")
    
    class Config:
        populate_by_name = True


class NullableMilestone(BaseModel):
    """NullableMilestone schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    labels_url: str = Field(alias="labels_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The number of the milestone.
    state: str = Field(alias="state")  # The state of the milestone.
    title: str = Field(alias="title")  # The title of the milestone.
    description: str = Field(alias="description")
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    open_issues: int = Field(alias="open_issues")
    closed_issues: int = Field(alias="closed_issues")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    due_on: str = Field(alias="due_on")
    
    class Config:
        populate_by_name = True


class IssueType(BaseModel):
    """IssueType schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the issue type.
    node_id: str = Field(alias="node_id")  # The node identifier of the issue type.
    name: str = Field(alias="name")  # The name of the issue type.
    description: str = Field(alias="description")  # The description of the issue type.
    color: str = Field(alias="color")  # The color of the issue type.
    created_at: str = Field(alias="created_at")  # The time the issue type created.
    updated_at: str = Field(alias="updated_at")  # The time the issue type last updated.
    is_enabled: bool = Field(alias="is_enabled")  # The enabled state of the issue type.
    
    class Config:
        populate_by_name = True


class NullableIntegration(BaseModel):
    """NullableIntegration schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the GitHub app
    slug: str = Field(alias="slug")  # The slug name of the GitHub app
    node_id: str = Field(alias="node_id")
    client_id: str = Field(alias="client_id")
    owner: Any = Field(alias="owner")
    name: str = Field(alias="name")  # The name of the GitHub app
    description: str = Field(alias="description")
    external_url: str = Field(alias="external_url")
    html_url: str = Field(alias="html_url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    permissions: Dict[str, Any] = Field(alias="permissions")  # The set of permissions for the GitHub app
    events: List[str] = Field(alias="events")  # The list of events for the GitHub app. Note that the `installation_target`, `security_advisory`, and `meta` events are not included because they are global events and not specific to an installation.
    installations_count: int = Field(alias="installations_count")  # The number of installations associated with the GitHub app. Only returned when the integration is requesting details about itself.
    
    class Config:
        populate_by_name = True


class ReactionRollup(BaseModel):
    """ReactionRollup schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    total_count: int = Field(alias="total_count")
    field_1: int = Field(alias="+1")
    field_1_1: int = Field(alias="-1")
    laugh: int = Field(alias="laugh")
    confused: int = Field(alias="confused")
    heart: int = Field(alias="heart")
    hooray: int = Field(alias="hooray")
    eyes: int = Field(alias="eyes")
    rocket: int = Field(alias="rocket")
    
    class Config:
        populate_by_name = True


class SubIssuesSummary(BaseModel):
    """SubIssuesSummary schema from the OpenAPI specification."""
    total: int = Field(alias="total")
    completed: int = Field(alias="completed")
    percent_completed: int = Field(alias="percent_completed")
    
    class Config:
        populate_by_name = True


class Issue(BaseModel):
    """Issue schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the issue
    repository_url: str = Field(alias="repository_url")
    labels_url: str = Field(alias="labels_url")
    comments_url: str = Field(alias="comments_url")
    events_url: str = Field(alias="events_url")
    html_url: str = Field(alias="html_url")
    number: int = Field(alias="number")  # Number uniquely identifying the issue within its repository
    state: str = Field(alias="state")  # State of the issue; either \'open\' or \'closed\'
    state_reason: str = Field(alias="state_reason")  # The reason for the current state
    title: str = Field(alias="title")  # Title of the issue
    body: str = Field(alias="body")  # Contents of the issue
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    labels: List[Any] = Field(alias="labels")  # Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assignees: List[SimpleUser] = Field(alias="assignees")
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    locked: bool = Field(alias="locked")
    active_lock_reason: str = Field(alias="active_lock_reason")
    comments: int = Field(alias="comments")
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    closed_at: str = Field(alias="closed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    draft: bool = Field(alias="draft")
    closed_by: NullableSimpleUser = Field(alias="closed_by")  # A GitHub user.
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    timeline_url: str = Field(alias="timeline_url")
    type_field: IssueType = Field(alias="type")  # The type of issue.
    repository: Repository = Field(alias="repository")  # A repository on GitHub.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    reactions: ReactionRollup = Field(alias="reactions")
    sub_issues_summary: SubIssuesSummary = Field(alias="sub_issues_summary")
    
    class Config:
        populate_by_name = True


class IssueComment(BaseModel):
    """IssueComment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the issue comment
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the issue comment
    body: str = Field(alias="body")  # Contents of the issue comment
    body_text: str = Field(alias="body_text")
    body_html: str = Field(alias="body_html")
    html_url: str = Field(alias="html_url")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    issue_url: str = Field(alias="issue_url")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class Event(BaseModel):
    """Event schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")
    type_field: str = Field(alias="type")
    actor: Actor = Field(alias="actor")  # Actor
    repo: Dict[str, Any] = Field(alias="repo")
    org: Actor = Field(alias="org")  # Actor
    payload: Dict[str, Any] = Field(alias="payload")
    public: bool = Field(alias="public")
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class LinkWithType(BaseModel):
    """LinkWithType schema from the OpenAPI specification."""
    href: str = Field(alias="href")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class Feed(BaseModel):
    """Feed schema from the OpenAPI specification."""
    timeline_url: str = Field(alias="timeline_url")
    user_url: str = Field(alias="user_url")
    current_user_public_url: str = Field(alias="current_user_public_url")
    current_user_url: str = Field(alias="current_user_url")
    current_user_actor_url: str = Field(alias="current_user_actor_url")
    current_user_organization_url: str = Field(alias="current_user_organization_url")
    current_user_organization_urls: List[str] = Field(alias="current_user_organization_urls")
    security_advisories_url: str = Field(alias="security_advisories_url")
    repository_discussions_url: str = Field(alias="repository_discussions_url")  # A feed of discussions for a given repository.
    repository_discussions_category_url: str = Field(alias="repository_discussions_category_url")  # A feed of discussions for a given repository and category.
    links: Dict[str, Any] = Field(alias="_links")
    
    class Config:
        populate_by_name = True


class BaseGist(BaseModel):
    """BaseGist schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    forks_url: str = Field(alias="forks_url")
    commits_url: str = Field(alias="commits_url")
    id_field: str = Field(alias="id")
    node_id: str = Field(alias="node_id")
    git_pull_url: str = Field(alias="git_pull_url")
    git_push_url: str = Field(alias="git_push_url")
    html_url: str = Field(alias="html_url")
    files: Dict[str, Any] = Field(alias="files")
    public: bool = Field(alias="public")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    description: str = Field(alias="description")
    comments: int = Field(alias="comments")
    comments_enabled: bool = Field(alias="comments_enabled")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    comments_url: str = Field(alias="comments_url")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    truncated: bool = Field(alias="truncated")
    forks: List[Any] = Field(alias="forks")
    history: List[Any] = Field(alias="history")
    
    class Config:
        populate_by_name = True


class PublicUser(BaseModel):
    """PublicUser schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    user_view_type: str = Field(alias="user_view_type")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    name: str = Field(alias="name")
    company: str = Field(alias="company")
    blog: str = Field(alias="blog")
    location: str = Field(alias="location")
    email: str = Field(alias="email")
    notification_email: str = Field(alias="notification_email")
    hireable: bool = Field(alias="hireable")
    bio: str = Field(alias="bio")
    twitter_username: str = Field(alias="twitter_username")
    public_repos: int = Field(alias="public_repos")
    public_gists: int = Field(alias="public_gists")
    followers: int = Field(alias="followers")
    following: int = Field(alias="following")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    plan: Dict[str, Any] = Field(alias="plan")
    private_gists: int = Field(alias="private_gists")
    total_private_repos: int = Field(alias="total_private_repos")
    owned_private_repos: int = Field(alias="owned_private_repos")
    disk_usage: int = Field(alias="disk_usage")
    collaborators: int = Field(alias="collaborators")
    
    class Config:
        populate_by_name = True


class GistHistory(BaseModel):
    """GistHistory schema from the OpenAPI specification."""
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    version: str = Field(alias="version")
    committed_at: str = Field(alias="committed_at")
    change_status: Dict[str, Any] = Field(alias="change_status")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class GistSimple(BaseModel):
    """GistSimple schema from the OpenAPI specification."""
    forks: List[Dict[str, Any]] = Field(alias="forks")
    history: List[GistHistory] = Field(alias="history")
    fork_of: Dict[str, Any] = Field(alias="fork_of")  # Gist
    url: str = Field(alias="url")
    forks_url: str = Field(alias="forks_url")
    commits_url: str = Field(alias="commits_url")
    id_field: str = Field(alias="id")
    node_id: str = Field(alias="node_id")
    git_pull_url: str = Field(alias="git_pull_url")
    git_push_url: str = Field(alias="git_push_url")
    html_url: str = Field(alias="html_url")
    files: Dict[str, Any] = Field(alias="files")
    public: bool = Field(alias="public")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    description: str = Field(alias="description")
    comments: int = Field(alias="comments")
    comments_enabled: bool = Field(alias="comments_enabled")
    user: str = Field(alias="user")
    comments_url: str = Field(alias="comments_url")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    truncated: bool = Field(alias="truncated")
    
    class Config:
        populate_by_name = True


class GistComment(BaseModel):
    """GistComment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    body: str = Field(alias="body")  # The comment text.
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    
    class Config:
        populate_by_name = True


class GistCommit(BaseModel):
    """GistCommit schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    version: str = Field(alias="version")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    change_status: Dict[str, Any] = Field(alias="change_status")
    committed_at: str = Field(alias="committed_at")
    
    class Config:
        populate_by_name = True


class GitignoreTemplate(BaseModel):
    """GitignoreTemplate schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    source: str = Field(alias="source")
    
    class Config:
        populate_by_name = True


class LicenseSimple(BaseModel):
    """LicenseSimple schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    url: str = Field(alias="url")
    spdx_id: str = Field(alias="spdx_id")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class License(BaseModel):
    """License schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    spdx_id: str = Field(alias="spdx_id")
    url: str = Field(alias="url")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    implementation: str = Field(alias="implementation")
    permissions: List[str] = Field(alias="permissions")
    conditions: List[str] = Field(alias="conditions")
    limitations: List[str] = Field(alias="limitations")
    body: str = Field(alias="body")
    featured: bool = Field(alias="featured")
    
    class Config:
        populate_by_name = True


class MarketplaceListingPlan(BaseModel):
    """MarketplaceListingPlan schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    accounts_url: str = Field(alias="accounts_url")
    id_field: int = Field(alias="id")
    number: int = Field(alias="number")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    monthly_price_in_cents: int = Field(alias="monthly_price_in_cents")
    yearly_price_in_cents: int = Field(alias="yearly_price_in_cents")
    price_model: str = Field(alias="price_model")
    has_free_trial: bool = Field(alias="has_free_trial")
    unit_name: str = Field(alias="unit_name")
    state: str = Field(alias="state")
    bullets: List[str] = Field(alias="bullets")
    
    class Config:
        populate_by_name = True


class MarketplacePurchase(BaseModel):
    """MarketplacePurchase schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    type_field: str = Field(alias="type")
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    organization_billing_email: str = Field(alias="organization_billing_email")
    email: str = Field(alias="email")
    marketplace_pending_change: Dict[str, Any] = Field(alias="marketplace_pending_change")
    marketplace_purchase: Dict[str, Any] = Field(alias="marketplace_purchase")
    
    class Config:
        populate_by_name = True


class ApiOverview(BaseModel):
    """ApiOverview schema from the OpenAPI specification."""
    verifiable_password_authentication: bool = Field(alias="verifiable_password_authentication")
    ssh_key_fingerprints: Dict[str, Any] = Field(alias="ssh_key_fingerprints")
    ssh_keys: List[str] = Field(alias="ssh_keys")
    hooks: List[str] = Field(alias="hooks")
    github_enterprise_importer: List[str] = Field(alias="github_enterprise_importer")
    web: List[str] = Field(alias="web")
    api: List[str] = Field(alias="api")
    git: List[str] = Field(alias="git")
    packages: List[str] = Field(alias="packages")
    pages: List[str] = Field(alias="pages")
    importer: List[str] = Field(alias="importer")
    actions: List[str] = Field(alias="actions")
    actions_macos: List[str] = Field(alias="actions_macos")
    codespaces: List[str] = Field(alias="codespaces")
    dependabot: List[str] = Field(alias="dependabot")
    copilot: List[str] = Field(alias="copilot")
    domains: Dict[str, Any] = Field(alias="domains")
    
    class Config:
        populate_by_name = True


class SecurityAndAnalysis(BaseModel):
    """SecurityAndAnalysis schema from the OpenAPI specification."""
    advanced_security: Dict[str, Any] = Field(alias="advanced_security")
    code_security: Dict[str, Any] = Field(alias="code_security")
    dependabot_security_updates: Dict[str, Any] = Field(alias="dependabot_security_updates")  # Enable or disable Dependabot security updates for the repository.
    secret_scanning: Dict[str, Any] = Field(alias="secret_scanning")
    secret_scanning_push_protection: Dict[str, Any] = Field(alias="secret_scanning_push_protection")
    secret_scanning_non_provider_patterns: Dict[str, Any] = Field(alias="secret_scanning_non_provider_patterns")
    secret_scanning_ai_detection: Dict[str, Any] = Field(alias="secret_scanning_ai_detection")
    
    class Config:
        populate_by_name = True


class MinimalRepository(BaseModel):
    """MinimalRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    full_name: str = Field(alias="full_name")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")
    has_projects: bool = Field(alias="has_projects")
    has_wiki: bool = Field(alias="has_wiki")
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")
    has_discussions: bool = Field(alias="has_discussions")
    archived: bool = Field(alias="archived")
    disabled: bool = Field(alias="disabled")
    visibility: str = Field(alias="visibility")
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    permissions: Dict[str, Any] = Field(alias="permissions")
    role_name: str = Field(alias="role_name")
    temp_clone_token: str = Field(alias="temp_clone_token")
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    code_of_conduct: CodeOfConduct = Field(alias="code_of_conduct")  # Code Of Conduct
    license: Dict[str, Any] = Field(alias="license")
    forks: int = Field(alias="forks")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    allow_forking: bool = Field(alias="allow_forking")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    security_and_analysis: SecurityAndAnalysis = Field(alias="security_and_analysis")
    custom_properties: Dict[str, Any] = Field(alias="custom_properties")  # The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.
    
    class Config:
        populate_by_name = True


class Thread(BaseModel):
    """Thread schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    subject: Dict[str, Any] = Field(alias="subject")
    reason: str = Field(alias="reason")
    unread: bool = Field(alias="unread")
    updated_at: str = Field(alias="updated_at")
    last_read_at: str = Field(alias="last_read_at")
    url: str = Field(alias="url")
    subscription_url: str = Field(alias="subscription_url")
    
    class Config:
        populate_by_name = True


class ThreadSubscription(BaseModel):
    """ThreadSubscription schema from the OpenAPI specification."""
    subscribed: bool = Field(alias="subscribed")
    ignored: bool = Field(alias="ignored")
    reason: str = Field(alias="reason")
    created_at: str = Field(alias="created_at")
    url: str = Field(alias="url")
    thread_url: str = Field(alias="thread_url")
    repository_url: str = Field(alias="repository_url")
    
    class Config:
        populate_by_name = True


class OrganizationSimple(BaseModel):
    """OrganizationSimple schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    hooks_url: str = Field(alias="hooks_url")
    issues_url: str = Field(alias="issues_url")
    members_url: str = Field(alias="members_url")
    public_members_url: str = Field(alias="public_members_url")
    avatar_url: str = Field(alias="avatar_url")
    description: str = Field(alias="description")
    
    class Config:
        populate_by_name = True


class NullableSimpleRepository(BaseModel):
    """NullableSimpleRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # A unique identifier of the repository.
    node_id: str = Field(alias="node_id")  # The GraphQL identifier of the repository.
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")  # The full, globally unique, name of the repository.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private.
    html_url: str = Field(alias="html_url")  # The URL to view the repository on GitHub.com.
    description: str = Field(alias="description")  # The repository description.
    fork: bool = Field(alias="fork")  # Whether the repository is a fork.
    url: str = Field(alias="url")  # The URL to get more information about the repository from the GitHub API.
    archive_url: str = Field(alias="archive_url")  # A template for the API URL to download the repository as an archive.
    assignees_url: str = Field(alias="assignees_url")  # A template for the API URL to list the available assignees for issues in the repository.
    blobs_url: str = Field(alias="blobs_url")  # A template for the API URL to create or retrieve a raw Git blob in the repository.
    branches_url: str = Field(alias="branches_url")  # A template for the API URL to get information about branches in the repository.
    collaborators_url: str = Field(alias="collaborators_url")  # A template for the API URL to get information about collaborators of the repository.
    comments_url: str = Field(alias="comments_url")  # A template for the API URL to get information about comments on the repository.
    commits_url: str = Field(alias="commits_url")  # A template for the API URL to get information about commits on the repository.
    compare_url: str = Field(alias="compare_url")  # A template for the API URL to compare two commits or refs.
    contents_url: str = Field(alias="contents_url")  # A template for the API URL to get the contents of the repository.
    contributors_url: str = Field(alias="contributors_url")  # A template for the API URL to list the contributors to the repository.
    deployments_url: str = Field(alias="deployments_url")  # The API URL to list the deployments of the repository.
    downloads_url: str = Field(alias="downloads_url")  # The API URL to list the downloads on the repository.
    events_url: str = Field(alias="events_url")  # The API URL to list the events of the repository.
    forks_url: str = Field(alias="forks_url")  # The API URL to list the forks of the repository.
    git_commits_url: str = Field(alias="git_commits_url")  # A template for the API URL to get information about Git commits of the repository.
    git_refs_url: str = Field(alias="git_refs_url")  # A template for the API URL to get information about Git refs of the repository.
    git_tags_url: str = Field(alias="git_tags_url")  # A template for the API URL to get information about Git tags of the repository.
    issue_comment_url: str = Field(alias="issue_comment_url")  # A template for the API URL to get information about issue comments on the repository.
    issue_events_url: str = Field(alias="issue_events_url")  # A template for the API URL to get information about issue events on the repository.
    issues_url: str = Field(alias="issues_url")  # A template for the API URL to get information about issues on the repository.
    keys_url: str = Field(alias="keys_url")  # A template for the API URL to get information about deploy keys on the repository.
    labels_url: str = Field(alias="labels_url")  # A template for the API URL to get information about labels of the repository.
    languages_url: str = Field(alias="languages_url")  # The API URL to get information about the languages of the repository.
    merges_url: str = Field(alias="merges_url")  # The API URL to merge branches in the repository.
    milestones_url: str = Field(alias="milestones_url")  # A template for the API URL to get information about milestones of the repository.
    notifications_url: str = Field(alias="notifications_url")  # A template for the API URL to get information about notifications on the repository.
    pulls_url: str = Field(alias="pulls_url")  # A template for the API URL to get information about pull requests on the repository.
    releases_url: str = Field(alias="releases_url")  # A template for the API URL to get information about releases on the repository.
    stargazers_url: str = Field(alias="stargazers_url")  # The API URL to list the stargazers on the repository.
    statuses_url: str = Field(alias="statuses_url")  # A template for the API URL to get information about statuses of a commit.
    subscribers_url: str = Field(alias="subscribers_url")  # The API URL to list the subscribers on the repository.
    subscription_url: str = Field(alias="subscription_url")  # The API URL to subscribe to notifications for this repository.
    tags_url: str = Field(alias="tags_url")  # The API URL to get information about tags on the repository.
    teams_url: str = Field(alias="teams_url")  # The API URL to list the teams on the repository.
    trees_url: str = Field(alias="trees_url")  # A template for the API URL to create or retrieve a raw Git tree of the repository.
    hooks_url: str = Field(alias="hooks_url")  # The API URL to list the hooks on the repository.
    
    class Config:
        populate_by_name = True


class DependabotRepositoryAccessDetails(BaseModel):
    """DependabotRepositoryAccessDetails schema from the OpenAPI specification."""
    default_level: str = Field(alias="default_level")  # The default repository access level for Dependabot updates.
    accessible_repositories: List[NullableSimpleRepository] = Field(alias="accessible_repositories")
    
    class Config:
        populate_by_name = True


class BillingUsageReport(BaseModel):
    """BillingUsageReport schema from the OpenAPI specification."""
    usage_items: List[Dict[str, Any]] = Field(alias="usageItems")
    
    class Config:
        populate_by_name = True


class OrganizationFull(BaseModel):
    """OrganizationFull schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    hooks_url: str = Field(alias="hooks_url")
    issues_url: str = Field(alias="issues_url")
    members_url: str = Field(alias="members_url")
    public_members_url: str = Field(alias="public_members_url")
    avatar_url: str = Field(alias="avatar_url")
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    company: str = Field(alias="company")
    blog: str = Field(alias="blog")
    location: str = Field(alias="location")
    email: str = Field(alias="email")
    twitter_username: str = Field(alias="twitter_username")
    is_verified: bool = Field(alias="is_verified")
    has_organization_projects: bool = Field(alias="has_organization_projects")
    has_repository_projects: bool = Field(alias="has_repository_projects")
    public_repos: int = Field(alias="public_repos")
    public_gists: int = Field(alias="public_gists")
    followers: int = Field(alias="followers")
    following: int = Field(alias="following")
    html_url: str = Field(alias="html_url")
    type_field: str = Field(alias="type")
    total_private_repos: int = Field(alias="total_private_repos")
    owned_private_repos: int = Field(alias="owned_private_repos")
    private_gists: int = Field(alias="private_gists")
    disk_usage: int = Field(alias="disk_usage")
    collaborators: int = Field(alias="collaborators")  # The number of collaborators on private repositories.

This field may be null if the number of private repositories is over 50,000.
    billing_email: str = Field(alias="billing_email")
    plan: Dict[str, Any] = Field(alias="plan")
    default_repository_permission: str = Field(alias="default_repository_permission")
    default_repository_branch: str = Field(alias="default_repository_branch")  # The default branch for repositories created in this organization.
    members_can_create_repositories: bool = Field(alias="members_can_create_repositories")
    two_factor_requirement_enabled: bool = Field(alias="two_factor_requirement_enabled")
    members_allowed_repository_creation_type: str = Field(alias="members_allowed_repository_creation_type")
    members_can_create_public_repositories: bool = Field(alias="members_can_create_public_repositories")
    members_can_create_private_repositories: bool = Field(alias="members_can_create_private_repositories")
    members_can_create_internal_repositories: bool = Field(alias="members_can_create_internal_repositories")
    members_can_create_pages: bool = Field(alias="members_can_create_pages")
    members_can_create_public_pages: bool = Field(alias="members_can_create_public_pages")
    members_can_create_private_pages: bool = Field(alias="members_can_create_private_pages")
    members_can_delete_repositories: bool = Field(alias="members_can_delete_repositories")
    members_can_change_repo_visibility: bool = Field(alias="members_can_change_repo_visibility")
    members_can_invite_outside_collaborators: bool = Field(alias="members_can_invite_outside_collaborators")
    members_can_delete_issues: bool = Field(alias="members_can_delete_issues")
    display_commenter_full_name_setting_enabled: bool = Field(alias="display_commenter_full_name_setting_enabled")
    readers_can_create_discussions: bool = Field(alias="readers_can_create_discussions")
    members_can_create_teams: bool = Field(alias="members_can_create_teams")
    members_can_view_dependency_insights: bool = Field(alias="members_can_view_dependency_insights")
    members_can_fork_private_repositories: bool = Field(alias="members_can_fork_private_repositories")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    advanced_security_enabled_for_new_repositories: bool = Field(alias="advanced_security_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether GitHub Advanced Security is enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    dependabot_alerts_enabled_for_new_repositories: bool = Field(alias="dependabot_alerts_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether Dependabot alerts are automatically enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    dependabot_security_updates_enabled_for_new_repositories: bool = Field(alias="dependabot_security_updates_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether Dependabot security updates are automatically enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    dependency_graph_enabled_for_new_repositories: bool = Field(alias="dependency_graph_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether dependency graph is automatically enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    secret_scanning_enabled_for_new_repositories: bool = Field(alias="secret_scanning_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether secret scanning is automatically enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    secret_scanning_push_protection_enabled_for_new_repositories: bool = Field(alias="secret_scanning_push_protection_enabled_for_new_repositories")  # **Endpoint closing down notice.** Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead.

Whether secret scanning push protection is automatically enabled for new repositories and repositories transferred to this organization.

This field is only visible to organization owners or members of a team with the security manager role.
    secret_scanning_push_protection_custom_link_enabled: bool = Field(alias="secret_scanning_push_protection_custom_link_enabled")  # Whether a custom link is shown to contributors who are blocked from pushing a secret by push protection.
    secret_scanning_push_protection_custom_link: str = Field(alias="secret_scanning_push_protection_custom_link")  # An optional URL string to display to contributors who are blocked from pushing a secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    archived_at: str = Field(alias="archived_at")
    deploy_keys_enabled_for_repositories: bool = Field(alias="deploy_keys_enabled_for_repositories")  # Controls whether or not deploy keys may be added and used for repositories in the organization.
    
    class Config:
        populate_by_name = True


class ActionsCacheUsageOrgEnterprise(BaseModel):
    """ActionsCacheUsageOrgEnterprise schema from the OpenAPI specification."""
    total_active_caches_count: int = Field(alias="total_active_caches_count")  # The count of active caches across all repositories of an enterprise or an organization.
    total_active_caches_size_in_bytes: int = Field(alias="total_active_caches_size_in_bytes")  # The total size in bytes of all active cache items across all repositories of an enterprise or an organization.
    
    class Config:
        populate_by_name = True


class ActionsCacheUsageByRepository(BaseModel):
    """ActionsCacheUsageByRepository schema from the OpenAPI specification."""
    full_name: str = Field(alias="full_name")  # The repository owner and name for the cache usage being shown.
    active_caches_size_in_bytes: int = Field(alias="active_caches_size_in_bytes")  # The sum of the size in bytes of all the active cache items in the repository.
    active_caches_count: int = Field(alias="active_caches_count")  # The number of active caches in the repository.
    
    class Config:
        populate_by_name = True


class NullableActionsHostedRunnerPoolImage(BaseModel):
    """NullableActionsHostedRunnerPoolImage schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The ID of the image. Use this ID for the `image` parameter when creating a new larger runner.
    size_gb: int = Field(alias="size_gb")  # Image size in GB.
    display_name: str = Field(alias="display_name")  # Display name for this image.
    source: str = Field(alias="source")  # The image provider.
    
    class Config:
        populate_by_name = True


class ActionsHostedRunnerMachineSpec(BaseModel):
    """ActionsHostedRunnerMachineSpec schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The ID used for the `size` parameter when creating a new runner.
    cpu_cores: int = Field(alias="cpu_cores")  # The number of cores.
    memory_gb: int = Field(alias="memory_gb")  # The available RAM for the machine spec.
    storage_gb: int = Field(alias="storage_gb")  # The available SSD storage for the machine spec.
    
    class Config:
        populate_by_name = True


class PublicIp(BaseModel):
    """PublicIp schema from the OpenAPI specification."""
    enabled: bool = Field(alias="enabled")  # Whether public IP is enabled.
    prefix: str = Field(alias="prefix")  # The prefix for the public IP.
    length: int = Field(alias="length")  # The length of the IP prefix.
    
    class Config:
        populate_by_name = True


class ActionsHostedRunner(BaseModel):
    """ActionsHostedRunner schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the hosted runner.
    name: str = Field(alias="name")  # The name of the hosted runner.
    runner_group_id: int = Field(alias="runner_group_id")  # The unique identifier of the group that the hosted runner belongs to.
    image_details: NullableActionsHostedRunnerPoolImage = Field(alias="image_details")  # Provides details of a hosted runner image
    machine_size_details: ActionsHostedRunnerMachineSpec = Field(alias="machine_size_details")  # Provides details of a particular machine spec.
    status: str = Field(alias="status")  # The status of the runner.
    platform: str = Field(alias="platform")  # The operating system of the image.
    maximum_runners: int = Field(alias="maximum_runners")  # The maximum amount of hosted runners. Runners will not scale automatically above this number. Use this setting to limit your cost.
    public_ip_enabled: bool = Field(alias="public_ip_enabled")  # Whether public IP is enabled for the hosted runners.
    public_ips: List[PublicIp] = Field(alias="public_ips")  # The public IP ranges when public IP is enabled for the hosted runners.
    last_active_on: str = Field(alias="last_active_on")  # The time at which the runner was last used, in ISO 8601 format.
    
    class Config:
        populate_by_name = True


class ActionsHostedRunnerImage(BaseModel):
    """ActionsHostedRunnerImage schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The ID of the image. Use this ID for the `image` parameter when creating a new larger runner.
    platform: str = Field(alias="platform")  # The operating system of the image.
    size_gb: int = Field(alias="size_gb")  # Image size in GB.
    display_name: str = Field(alias="display_name")  # Display name for this image.
    source: str = Field(alias="source")  # The image provider.
    
    class Config:
        populate_by_name = True


class ActionsHostedRunnerLimits(BaseModel):
    """ActionsHostedRunnerLimits schema from the OpenAPI specification."""
    public_ips: Dict[str, Any] = Field(alias="public_ips")  # Provides details of static public IP limits for GitHub-hosted Hosted Runners
    
    class Config:
        populate_by_name = True


class OidcCustomSub(BaseModel):
    """OidcCustomSub schema from the OpenAPI specification."""
    include_claim_keys: List[str] = Field(alias="include_claim_keys")  # Array of unique strings. Each claim key can only contain alphanumeric characters and underscores.
    
    class Config:
        populate_by_name = True


class EmptyObject(BaseModel):
    """EmptyObject schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class ActionsOrganizationPermissions(BaseModel):
    """ActionsOrganizationPermissions schema from the OpenAPI specification."""
    enabled_repositories: str = Field(alias="enabled_repositories")  # The policy that controls the repositories in the organization that are allowed to run GitHub Actions.
    selected_repositories_url: str = Field(alias="selected_repositories_url")  # The API URL to use to get or set the selected repositories that are allowed to run GitHub Actions, when `enabled_repositories` is set to `selected`.
    allowed_actions: str = Field(alias="allowed_actions")  # The permissions policy that controls the actions and reusable workflows that are allowed to run.
    selected_actions_url: str = Field(alias="selected_actions_url")  # The API URL to use to get or set the actions and reusable workflows that are allowed to run, when `allowed_actions` is set to `selected`.
    
    class Config:
        populate_by_name = True


class SelectedActions(BaseModel):
    """SelectedActions schema from the OpenAPI specification."""
    github_owned_allowed: bool = Field(alias="github_owned_allowed")  # Whether GitHub-owned actions are allowed. For example, this includes the actions in the `actions` organization.
    verified_allowed: bool = Field(alias="verified_allowed")  # Whether actions from GitHub Marketplace verified creators are allowed. Set to `true` to allow all actions by GitHub Marketplace verified creators.
    patterns_allowed: List[str] = Field(alias="patterns_allowed")  # Specifies a list of string-matching patterns to allow specific action(s) and reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example, `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.

> [!NOTE]
> The `patterns_allowed` setting only applies to public repositories.
    
    class Config:
        populate_by_name = True


class ActionsGetDefaultWorkflowPermissions(BaseModel):
    """ActionsGetDefaultWorkflowPermissions schema from the OpenAPI specification."""
    default_workflow_permissions: str = Field(alias="default_workflow_permissions")  # The default workflow permissions granted to the GITHUB_TOKEN when running workflows.
    can_approve_pull_request_reviews: bool = Field(alias="can_approve_pull_request_reviews")  # Whether GitHub Actions can approve pull requests. Enabling this can be a security risk.
    
    class Config:
        populate_by_name = True


class ActionsSetDefaultWorkflowPermissions(BaseModel):
    """ActionsSetDefaultWorkflowPermissions schema from the OpenAPI specification."""
    default_workflow_permissions: str = Field(alias="default_workflow_permissions")  # The default workflow permissions granted to the GITHUB_TOKEN when running workflows.
    can_approve_pull_request_reviews: bool = Field(alias="can_approve_pull_request_reviews")  # Whether GitHub Actions can approve pull requests. Enabling this can be a security risk.
    
    class Config:
        populate_by_name = True


class RunnerGroupsOrg(BaseModel):
    """RunnerGroupsOrg schema from the OpenAPI specification."""
    id_field: float = Field(alias="id")
    name: str = Field(alias="name")
    visibility: str = Field(alias="visibility")
    default: bool = Field(alias="default")
    selected_repositories_url: str = Field(alias="selected_repositories_url")  # Link to the selected repositories resource for this runner group. Not present unless visibility was set to `selected`
    runners_url: str = Field(alias="runners_url")
    hosted_runners_url: str = Field(alias="hosted_runners_url")
    network_configuration_id: str = Field(alias="network_configuration_id")  # The identifier of a hosted compute network configuration.
    inherited: bool = Field(alias="inherited")
    inherited_allows_public_repositories: bool = Field(alias="inherited_allows_public_repositories")
    allows_public_repositories: bool = Field(alias="allows_public_repositories")
    workflow_restrictions_read_only: bool = Field(alias="workflow_restrictions_read_only")  # If `true`, the `restricted_to_workflows` and `selected_workflows` fields cannot be modified.
    restricted_to_workflows: bool = Field(alias="restricted_to_workflows")  # If `true`, the runner group will be restricted to running only the workflows specified in the `selected_workflows` array.
    selected_workflows: List[str] = Field(alias="selected_workflows")  # List of workflows the runner group should be allowed to run. This setting will be ignored unless `restricted_to_workflows` is set to `true`.
    
    class Config:
        populate_by_name = True


class RunnerLabel(BaseModel):
    """RunnerLabel schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the label.
    name: str = Field(alias="name")  # Name of the label.
    type_field: str = Field(alias="type")  # The type of label. Read-only labels are applied automatically when the runner is configured.
    
    class Config:
        populate_by_name = True


class Runner(BaseModel):
    """Runner schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the runner.
    runner_group_id: int = Field(alias="runner_group_id")  # The ID of the runner group.
    name: str = Field(alias="name")  # The name of the runner.
    os: str = Field(alias="os")  # The Operating System of the runner.
    status: str = Field(alias="status")  # The status of the runner.
    busy: bool = Field(alias="busy")
    labels: List[RunnerLabel] = Field(alias="labels")
    ephemeral: bool = Field(alias="ephemeral")
    
    class Config:
        populate_by_name = True


class RunnerApplication(BaseModel):
    """RunnerApplication schema from the OpenAPI specification."""
    os: str = Field(alias="os")
    architecture: str = Field(alias="architecture")
    download_url: str = Field(alias="download_url")
    filename: str = Field(alias="filename")
    temp_download_token: str = Field(alias="temp_download_token")  # A short lived bearer token used to download the runner, if needed.
    sha256_checksum: str = Field(alias="sha256_checksum")
    
    class Config:
        populate_by_name = True


class AuthenticationToken(BaseModel):
    """AuthenticationToken schema from the OpenAPI specification."""
    token: str = Field(alias="token")  # The token used for authentication
    expires_at: str = Field(alias="expires_at")  # The time this token expires
    permissions: Dict[str, Any] = Field(alias="permissions")
    repositories: List[Repository] = Field(alias="repositories")  # The repositories this token has access to
    single_file: str = Field(alias="single_file")
    repository_selection: str = Field(alias="repository_selection")  # Describe whether all repositories have been selected or there\'s a selection involved
    
    class Config:
        populate_by_name = True


class OrganizationActionsSecret(BaseModel):
    """OrganizationActionsSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    visibility: str = Field(alias="visibility")  # Visibility of a secret
    selected_repositories_url: str = Field(alias="selected_repositories_url")
    
    class Config:
        populate_by_name = True


class ActionsPublicKey(BaseModel):
    """ActionsPublicKey schema from the OpenAPI specification."""
    key_id: str = Field(alias="key_id")  # The identifier for the key.
    key: str = Field(alias="key")  # The Base64 encoded public key.
    id_field: int = Field(alias="id")
    url: str = Field(alias="url")
    title: str = Field(alias="title")
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class OrganizationActionsVariable(BaseModel):
    """OrganizationActionsVariable schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the variable.
    value: str = Field(alias="value")  # The value of the variable.
    created_at: str = Field(alias="created_at")  # The date and time at which the variable was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the variable was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    visibility: str = Field(alias="visibility")  # Visibility of a variable
    selected_repositories_url: str = Field(alias="selected_repositories_url")
    
    class Config:
        populate_by_name = True


class NullableTeamSimple(BaseModel):
    """NullableTeamSimple schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the team
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the team
    members_url: str = Field(alias="members_url")
    name: str = Field(alias="name")  # Name of the team
    description: str = Field(alias="description")  # Description of the team
    permission: str = Field(alias="permission")  # Permission that the team will have for its repositories
    privacy: str = Field(alias="privacy")  # The level of privacy this team should have
    notification_setting: str = Field(alias="notification_setting")  # The notification setting the team has set
    html_url: str = Field(alias="html_url")
    repositories_url: str = Field(alias="repositories_url")
    slug: str = Field(alias="slug")
    ldap_dn: str = Field(alias="ldap_dn")  # Distinguished Name (DN) that team maps to within LDAP environment
    
    class Config:
        populate_by_name = True


class Team(BaseModel):
    """Team schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    description: str = Field(alias="description")
    privacy: str = Field(alias="privacy")
    notification_setting: str = Field(alias="notification_setting")
    permission: str = Field(alias="permission")
    permissions: Dict[str, Any] = Field(alias="permissions")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    members_url: str = Field(alias="members_url")
    repositories_url: str = Field(alias="repositories_url")
    parent: NullableTeamSimple = Field(alias="parent")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class CampaignSummary(BaseModel):
    """CampaignSummary schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The number of the newly created campaign
    created_at: str = Field(alias="created_at")  # The date and time the campaign was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time the campaign was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    name: str = Field(alias="name")  # The campaign name
    description: str = Field(alias="description")  # The campaign description
    managers: List[SimpleUser] = Field(alias="managers")  # The campaign managers
    team_managers: List[Team] = Field(alias="team_managers")  # The campaign team managers
    published_at: str = Field(alias="published_at")  # The date and time the campaign was published, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    ends_at: str = Field(alias="ends_at")  # The date and time the campaign has ended, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    closed_at: str = Field(alias="closed_at")  # The date and time the campaign was closed, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ. Will be null if the campaign is still open.
    state: str = Field(alias="state")  # Indicates whether a campaign is open or closed
    contact_link: str = Field(alias="contact_link")  # The contact link of the campaign.
    alert_stats: Dict[str, Any] = Field(alias="alert_stats")
    
    class Config:
        populate_by_name = True


class CodeScanningAlertRuleSummary(BaseModel):
    """CodeScanningAlertRuleSummary schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # A unique identifier for the rule used to detect the alert.
    name: str = Field(alias="name")  # The name of the rule used to detect the alert.
    severity: str = Field(alias="severity")  # The severity of the alert.
    security_severity_level: str = Field(alias="security_severity_level")  # The security severity of the alert.
    description: str = Field(alias="description")  # A short description of the rule used to detect the alert.
    full_description: str = Field(alias="full_description")  # A description of the rule used to detect the alert.
    tags: List[str] = Field(alias="tags")  # A set of tags applicable for the rule.
    help: str = Field(alias="help")  # Detailed documentation for the rule as GitHub Flavored Markdown.
    help_uri: str = Field(alias="help_uri")  # A link to the documentation for the rule used to detect the alert.
    
    class Config:
        populate_by_name = True


class CodeScanningAnalysisTool(BaseModel):
    """CodeScanningAnalysisTool schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the tool used to generate the code scanning analysis.
    version: str = Field(alias="version")  # The version of the tool used to generate the code scanning analysis.
    guid: str = Field(alias="guid")  # The GUID of the tool used to generate the code scanning analysis, if provided in the uploaded SARIF data.
    
    class Config:
        populate_by_name = True


class CodeScanningAlertLocation(BaseModel):
    """CodeScanningAlertLocation schema from the OpenAPI specification."""
    path: str = Field(alias="path")
    start_line: int = Field(alias="start_line")
    end_line: int = Field(alias="end_line")
    start_column: int = Field(alias="start_column")
    end_column: int = Field(alias="end_column")
    
    class Config:
        populate_by_name = True


class CodeScanningAlertInstance(BaseModel):
    """CodeScanningAlertInstance schema from the OpenAPI specification."""
    ref: str = Field(alias="ref")  # The Git reference, formatted as `refs/pull/<number>/merge`, `refs/pull/<number>/head`,
`refs/heads/<branch name>` or simply `<branch name>`.
    analysis_key: str = Field(alias="analysis_key")  # Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name.
    environment: str = Field(alias="environment")  # Identifies the variable values associated with the environment in which the analysis that generated this alert instance was performed, such as the language that was analyzed.
    category: str = Field(alias="category")  # Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code.
    state: str = Field(alias="state")  # State of a code scanning alert.
    commit_sha: str = Field(alias="commit_sha")
    message: Dict[str, Any] = Field(alias="message")
    location: CodeScanningAlertLocation = Field(alias="location")  # Describe a region within a file for the alert.
    html_url: str = Field(alias="html_url")
    classifications: List[str] = Field(alias="classifications")  # Classifications that have been applied to the file that triggered the alert.
For example identifying it as documentation, or a generated file.
    
    class Config:
        populate_by_name = True


class CodeScanningOrganizationAlertItems(BaseModel):
    """CodeScanningOrganizationAlertItems schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    instances_url: str = Field(alias="instances_url")  # The REST API URL for fetching the list of instances for an alert.
    state: str = Field(alias="state")  # State of a code scanning alert.
    fixed_at: str = Field(alias="fixed_at")  # The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_by: NullableSimpleUser = Field(alias="dismissed_by")  # A GitHub user.
    dismissed_at: str = Field(alias="dismissed_at")  # The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_reason: str = Field(alias="dismissed_reason")  # **Required when the state is dismissed.** The reason for dismissing or closing the alert.
    dismissed_comment: str = Field(alias="dismissed_comment")  # The dismissal comment associated with the dismissal of the alert.
    rule: CodeScanningAlertRuleSummary = Field(alias="rule")
    tool: CodeScanningAnalysisTool = Field(alias="tool")
    most_recent_instance: CodeScanningAlertInstance = Field(alias="most_recent_instance")
    repository: SimpleRepository = Field(alias="repository")  # A GitHub repository.
    dismissal_approved_by: NullableSimpleUser = Field(alias="dismissal_approved_by")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class NullableCodespaceMachine(BaseModel):
    """NullableCodespaceMachine schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the machine.
    display_name: str = Field(alias="display_name")  # The display name of the machine includes cores, memory, and storage.
    operating_system: str = Field(alias="operating_system")  # The operating system of the machine.
    storage_in_bytes: int = Field(alias="storage_in_bytes")  # How much storage is available to the codespace.
    memory_in_bytes: int = Field(alias="memory_in_bytes")  # How much memory is available to the codespace.
    cpus: int = Field(alias="cpus")  # How many cores are available to the codespace.
    prebuild_availability: str = Field(alias="prebuild_availability")  # Whether a prebuild is currently available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the default branch will be assumed. Value will be \"null\" if prebuilds are not supported or prebuild availability could not be determined. Value will be \"none\" if no prebuild is available. Latest values \"ready\" and \"in_progress\" indicate the prebuild availability status.
    
    class Config:
        populate_by_name = True


class Codespace(BaseModel):
    """Codespace schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")  # Automatically generated name of this codespace.
    display_name: str = Field(alias="display_name")  # Display name for this codespace.
    environment_id: str = Field(alias="environment_id")  # UUID identifying this codespace\'s environment.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    billable_owner: SimpleUser = Field(alias="billable_owner")  # A GitHub user.
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    machine: NullableCodespaceMachine = Field(alias="machine")  # A description of the machine powering a codespace.
    devcontainer_path: str = Field(alias="devcontainer_path")  # Path to devcontainer.json from repo root used to create Codespace.
    prebuild: bool = Field(alias="prebuild")  # Whether the codespace was created from a prebuild.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    last_used_at: str = Field(alias="last_used_at")  # Last known time this codespace was started.
    state: str = Field(alias="state")  # State of this codespace.
    url: str = Field(alias="url")  # API URL for this codespace.
    git_status: Dict[str, Any] = Field(alias="git_status")  # Details about the codespace\'s git repository.
    location: str = Field(alias="location")  # The initally assigned location of a new codespace.
    idle_timeout_minutes: int = Field(alias="idle_timeout_minutes")  # The number of minutes of inactivity after which this codespace will be automatically stopped.
    web_url: str = Field(alias="web_url")  # URL to access this codespace on the web.
    machines_url: str = Field(alias="machines_url")  # API URL to access available alternate machine types for this codespace.
    start_url: str = Field(alias="start_url")  # API URL to start this codespace.
    stop_url: str = Field(alias="stop_url")  # API URL to stop this codespace.
    publish_url: str = Field(alias="publish_url")  # API URL to publish this codespace to a new repository.
    pulls_url: str = Field(alias="pulls_url")  # API URL for the Pull Request associated with this codespace, if any.
    recent_folders: List[str] = Field(alias="recent_folders")
    runtime_constraints: Dict[str, Any] = Field(alias="runtime_constraints")
    pending_operation: bool = Field(alias="pending_operation")  # Whether or not a codespace has a pending async operation. This would mean that the codespace is temporarily unavailable. The only thing that you can do with a codespace in this state is delete it.
    pending_operation_disabled_reason: str = Field(alias="pending_operation_disabled_reason")  # Text to show user when codespace is disabled by a pending operation
    idle_timeout_notice: str = Field(alias="idle_timeout_notice")  # Text to show user when codespace idle timeout minutes has been overriden by an organization policy
    retention_period_minutes: int = Field(alias="retention_period_minutes")  # Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).
    retention_expires_at: str = Field(alias="retention_expires_at")  # When a codespace will be auto-deleted based on the \"retention_period_minutes\" and \"last_used_at\"
    last_known_stop_notice: str = Field(alias="last_known_stop_notice")  # The text to display to a user when a codespace has been stopped for a potentially actionable reason.
    
    class Config:
        populate_by_name = True


class CodespacesOrgSecret(BaseModel):
    """CodespacesOrgSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret
    created_at: str = Field(alias="created_at")  # The date and time at which the secret was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the secret was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    visibility: str = Field(alias="visibility")  # The type of repositories in the organization that the secret is visible to
    selected_repositories_url: str = Field(alias="selected_repositories_url")  # The API URL at which the list of repositories this secret is visible to can be retrieved
    
    class Config:
        populate_by_name = True


class CodespacesPublicKey(BaseModel):
    """CodespacesPublicKey schema from the OpenAPI specification."""
    key_id: str = Field(alias="key_id")  # The identifier for the key.
    key: str = Field(alias="key")  # The Base64 encoded public key.
    id_field: int = Field(alias="id")
    url: str = Field(alias="url")
    title: str = Field(alias="title")
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class CopilotOrganizationSeatBreakdown(BaseModel):
    """CopilotOrganizationSeatBreakdown schema from the OpenAPI specification."""
    total: int = Field(alias="total")  # The total number of seats being billed for the organization as of the current billing cycle.
    added_this_cycle: int = Field(alias="added_this_cycle")  # Seats added during the current billing cycle.
    pending_cancellation: int = Field(alias="pending_cancellation")  # The number of seats that are pending cancellation at the end of the current billing cycle.
    pending_invitation: int = Field(alias="pending_invitation")  # The number of users who have been invited to receive a Copilot seat through this organization.
    active_this_cycle: int = Field(alias="active_this_cycle")  # The number of seats that have used Copilot during the current billing cycle.
    inactive_this_cycle: int = Field(alias="inactive_this_cycle")  # The number of seats that have not used Copilot during the current billing cycle.
    
    class Config:
        populate_by_name = True


class CopilotOrganizationDetails(BaseModel):
    """CopilotOrganizationDetails schema from the OpenAPI specification."""
    seat_breakdown: CopilotOrganizationSeatBreakdown = Field(alias="seat_breakdown")  # The breakdown of Copilot Business seats for the organization.
    public_code_suggestions: str = Field(alias="public_code_suggestions")  # The organization policy for allowing or blocking suggestions matching public code (duplication detection filter).
    ide_chat: str = Field(alias="ide_chat")  # The organization policy for allowing or disallowing Copilot Chat in the IDE.
    platform_chat: str = Field(alias="platform_chat")  # The organization policy for allowing or disallowing Copilot features on GitHub.com.
    cli: str = Field(alias="cli")  # The organization policy for allowing or disallowing Copilot in the CLI.
    seat_management_setting: str = Field(alias="seat_management_setting")  # The mode of assigning new seats.
    plan_type: str = Field(alias="plan_type")  # The Copilot plan of the organization, or the parent enterprise, when applicable.
    
    class Config:
        populate_by_name = True


class NullableOrganizationSimple(BaseModel):
    """NullableOrganizationSimple schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    hooks_url: str = Field(alias="hooks_url")
    issues_url: str = Field(alias="issues_url")
    members_url: str = Field(alias="members_url")
    public_members_url: str = Field(alias="public_members_url")
    avatar_url: str = Field(alias="avatar_url")
    description: str = Field(alias="description")
    
    class Config:
        populate_by_name = True


class EnterpriseTeam(BaseModel):
    """EnterpriseTeam schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    slug: str = Field(alias="slug")
    url: str = Field(alias="url")
    sync_to_organizations: str = Field(alias="sync_to_organizations")
    organization_selection_type: str = Field(alias="organization_selection_type")
    group_id: str = Field(alias="group_id")
    group_name: str = Field(alias="group_name")
    html_url: str = Field(alias="html_url")
    members_url: str = Field(alias="members_url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class CopilotSeatDetails(BaseModel):
    """CopilotSeatDetails schema from the OpenAPI specification."""
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    organization: NullableOrganizationSimple = Field(alias="organization")  # A GitHub organization.
    assigning_team: Any = Field(alias="assigning_team")  # The team through which the assignee is granted access to GitHub Copilot, if applicable.
    pending_cancellation_date: str = Field(alias="pending_cancellation_date")  # The pending cancellation date for the seat, in `YYYY-MM-DD` format. This will be null unless the assignee\'s Copilot access has been canceled during the current billing cycle. If the seat has been cancelled, this corresponds to the start of the organization\'s next billing cycle.
    last_activity_at: str = Field(alias="last_activity_at")  # Timestamp of user\'s last GitHub Copilot activity, in ISO 8601 format.
    last_activity_editor: str = Field(alias="last_activity_editor")  # Last editor that was used by the user for a GitHub Copilot completion.
    created_at: str = Field(alias="created_at")  # Timestamp of when the assignee was last granted access to GitHub Copilot, in ISO 8601 format.
    updated_at: str = Field(alias="updated_at")  # **Closing down notice:** This field is no longer relevant and is closing down. Use the `created_at` field to determine when the assignee was last granted access to GitHub Copilot. Timestamp of when the assignee\'s GitHub Copilot access was last updated, in ISO 8601 format.
    plan_type: str = Field(alias="plan_type")  # The Copilot plan of the organization, or the parent enterprise, when applicable.
    
    class Config:
        populate_by_name = True


class CopilotIdeCodeCompletions(BaseModel):
    """CopilotIdeCodeCompletions schema from the OpenAPI specification."""
    total_engaged_users: int = Field(alias="total_engaged_users")  # Number of users who accepted at least one Copilot code suggestion, across all active editors. Includes both full and partial acceptances.
    languages: List[Dict[str, Any]] = Field(alias="languages")  # Code completion metrics for active languages.
    editors: List[Dict[str, Any]] = Field(alias="editors")
    
    class Config:
        populate_by_name = True


class CopilotIdeChat(BaseModel):
    """CopilotIdeChat schema from the OpenAPI specification."""
    total_engaged_users: int = Field(alias="total_engaged_users")  # Total number of users who prompted Copilot Chat in the IDE.
    editors: List[Dict[str, Any]] = Field(alias="editors")
    
    class Config:
        populate_by_name = True


class CopilotDotcomChat(BaseModel):
    """CopilotDotcomChat schema from the OpenAPI specification."""
    total_engaged_users: int = Field(alias="total_engaged_users")  # Total number of users who prompted Copilot Chat on github.com at least once.
    models: List[Dict[str, Any]] = Field(alias="models")  # List of model metrics for a custom models and the default model.
    
    class Config:
        populate_by_name = True


class CopilotDotcomPullRequests(BaseModel):
    """CopilotDotcomPullRequests schema from the OpenAPI specification."""
    total_engaged_users: int = Field(alias="total_engaged_users")  # The number of users who used Copilot for Pull Requests on github.com to generate a pull request summary at least once.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # Repositories in which users used Copilot for Pull Requests to generate pull request summaries
    
    class Config:
        populate_by_name = True


class CopilotUsageMetricsDay(BaseModel):
    """CopilotUsageMetricsDay schema from the OpenAPI specification."""
    date: str = Field(alias="date")  # The date for which the usage metrics are aggregated, in `YYYY-MM-DD` format.
    total_active_users: int = Field(alias="total_active_users")  # The total number of Copilot users with activity belonging to any Copilot feature, globally, for the given day. Includes passive activity such as receiving a code suggestion, as well as engagement activity such as accepting a code suggestion or prompting chat. Does not include authentication events. Is not limited to the individual features detailed on the endpoint.
    total_engaged_users: int = Field(alias="total_engaged_users")  # The total number of Copilot users who engaged with any Copilot feature, for the given day. Examples include but are not limited to accepting a code suggestion, prompting Copilot chat, or triggering a PR Summary. Does not include authentication events. Is not limited to the individual features detailed on the endpoint.
    copilot_ide_code_completions: CopilotIdeCodeCompletions = Field(alias="copilot_ide_code_completions")  # Usage metrics for Copilot editor code completions in the IDE.
    copilot_ide_chat: CopilotIdeChat = Field(alias="copilot_ide_chat")  # Usage metrics for Copilot Chat in the IDE.
    copilot_dotcom_chat: CopilotDotcomChat = Field(alias="copilot_dotcom_chat")  # Usage metrics for Copilot Chat in GitHub.com
    copilot_dotcom_pull_requests: CopilotDotcomPullRequests = Field(alias="copilot_dotcom_pull_requests")  # Usage metrics for Copilot for pull requests.
    
    class Config:
        populate_by_name = True


class OrganizationDependabotSecret(BaseModel):
    """OrganizationDependabotSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    visibility: str = Field(alias="visibility")  # Visibility of a secret
    selected_repositories_url: str = Field(alias="selected_repositories_url")
    
    class Config:
        populate_by_name = True


class DependabotPublicKey(BaseModel):
    """DependabotPublicKey schema from the OpenAPI specification."""
    key_id: str = Field(alias="key_id")  # The identifier for the key.
    key: str = Field(alias="key")  # The Base64 encoded public key.
    
    class Config:
        populate_by_name = True


class NullableMinimalRepository(BaseModel):
    """NullableMinimalRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    full_name: str = Field(alias="full_name")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")
    has_projects: bool = Field(alias="has_projects")
    has_wiki: bool = Field(alias="has_wiki")
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")
    has_discussions: bool = Field(alias="has_discussions")
    archived: bool = Field(alias="archived")
    disabled: bool = Field(alias="disabled")
    visibility: str = Field(alias="visibility")
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    permissions: Dict[str, Any] = Field(alias="permissions")
    role_name: str = Field(alias="role_name")
    temp_clone_token: str = Field(alias="temp_clone_token")
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    code_of_conduct: CodeOfConduct = Field(alias="code_of_conduct")  # Code Of Conduct
    license: Dict[str, Any] = Field(alias="license")
    forks: int = Field(alias="forks")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    allow_forking: bool = Field(alias="allow_forking")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    security_and_analysis: SecurityAndAnalysis = Field(alias="security_and_analysis")
    custom_properties: Dict[str, Any] = Field(alias="custom_properties")  # The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.
    
    class Config:
        populate_by_name = True


class Package(BaseModel):
    """Package schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the package.
    name: str = Field(alias="name")  # The name of the package.
    package_type: str = Field(alias="package_type")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    version_count: int = Field(alias="version_count")  # The number of versions of the package.
    visibility: str = Field(alias="visibility")
    owner: NullableSimpleUser = Field(alias="owner")  # A GitHub user.
    repository: NullableMinimalRepository = Field(alias="repository")  # Minimal Repository
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class OrganizationInvitation(BaseModel):
    """OrganizationInvitation schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    email: str = Field(alias="email")
    role: str = Field(alias="role")
    created_at: str = Field(alias="created_at")
    failed_at: str = Field(alias="failed_at")
    failed_reason: str = Field(alias="failed_reason")
    inviter: SimpleUser = Field(alias="inviter")  # A GitHub user.
    team_count: int = Field(alias="team_count")
    node_id: str = Field(alias="node_id")
    invitation_teams_url: str = Field(alias="invitation_teams_url")
    invitation_source: str = Field(alias="invitation_source")
    
    class Config:
        populate_by_name = True


class OrgHook(BaseModel):
    """OrgHook schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    url: str = Field(alias="url")
    ping_url: str = Field(alias="ping_url")
    deliveries_url: str = Field(alias="deliveries_url")
    name: str = Field(alias="name")
    events: List[str] = Field(alias="events")
    active: bool = Field(alias="active")
    config: Dict[str, Any] = Field(alias="config")
    updated_at: str = Field(alias="updated_at")
    created_at: str = Field(alias="created_at")
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class ApiInsightsSummaryStats(BaseModel):
    """ApiInsightsSummaryStats schema from the OpenAPI specification."""
    total_request_count: int = Field(alias="total_request_count")  # The total number of requests within the queried time period
    rate_limited_request_count: int = Field(alias="rate_limited_request_count")  # The total number of requests that were rate limited within the queried time period
    
    class Config:
        populate_by_name = True


class InteractionLimitResponse(BaseModel):
    """InteractionLimitResponse schema from the OpenAPI specification."""
    limit: str = Field(alias="limit")  # The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect.
    origin: str = Field(alias="origin")
    expires_at: str = Field(alias="expires_at")
    
    class Config:
        populate_by_name = True


class InteractionLimit(BaseModel):
    """InteractionLimit schema from the OpenAPI specification."""
    limit: str = Field(alias="limit")  # The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect.
    expiry: str = Field(alias="expiry")  # The duration of the interaction restriction. Default: `one_day`.
    
    class Config:
        populate_by_name = True


class OrganizationCreateIssueType(BaseModel):
    """OrganizationCreateIssueType schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # Name of the issue type.
    is_enabled: bool = Field(alias="is_enabled")  # Whether or not the issue type is enabled at the organization level.
    description: str = Field(alias="description")  # Description of the issue type.
    color: str = Field(alias="color")  # Color for the issue type.
    
    class Config:
        populate_by_name = True


class OrganizationUpdateIssueType(BaseModel):
    """OrganizationUpdateIssueType schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # Name of the issue type.
    is_enabled: bool = Field(alias="is_enabled")  # Whether or not the issue type is enabled at the organization level.
    description: str = Field(alias="description")  # Description of the issue type.
    color: str = Field(alias="color")  # Color for the issue type.
    
    class Config:
        populate_by_name = True


class OrgMembership(BaseModel):
    """OrgMembership schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    state: str = Field(alias="state")  # The state of the member in the organization. The `pending` state indicates the user has not yet accepted an invitation.
    role: str = Field(alias="role")  # The user\'s membership type in the organization.
    organization_url: str = Field(alias="organization_url")
    organization: OrganizationSimple = Field(alias="organization")  # A GitHub organization.
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    permissions: Dict[str, Any] = Field(alias="permissions")
    
    class Config:
        populate_by_name = True


class Migration(BaseModel):
    """Migration schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    owner: NullableSimpleUser = Field(alias="owner")  # A GitHub user.
    guid: str = Field(alias="guid")
    state: str = Field(alias="state")
    lock_repositories: bool = Field(alias="lock_repositories")
    exclude_metadata: bool = Field(alias="exclude_metadata")
    exclude_git_data: bool = Field(alias="exclude_git_data")
    exclude_attachments: bool = Field(alias="exclude_attachments")
    exclude_releases: bool = Field(alias="exclude_releases")
    exclude_owner_projects: bool = Field(alias="exclude_owner_projects")
    org_metadata_only: bool = Field(alias="org_metadata_only")
    repositories: List[Repository] = Field(alias="repositories")  # The repositories included in the migration. Only returned for export migrations.
    url: str = Field(alias="url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    node_id: str = Field(alias="node_id")
    archive_url: str = Field(alias="archive_url")
    exclude: List[str] = Field(alias="exclude")  # Exclude related items from being returned in the response in order to improve performance of the request. The array can include any of: `\"repositories\"`.
    
    class Config:
        populate_by_name = True


class OrganizationRole(BaseModel):
    """OrganizationRole schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the role.
    name: str = Field(alias="name")  # The name of the role.
    description: str = Field(alias="description")  # A short description about who this role is for or what permissions it grants.
    base_role: str = Field(alias="base_role")  # The system role from which this role inherits permissions.
    source: str = Field(alias="source")  # Source answers the question, \"where did this role come from?\"
    permissions: List[str] = Field(alias="permissions")  # A list of permissions included in this role.
    organization: NullableSimpleUser = Field(alias="organization")  # A GitHub user.
    created_at: str = Field(alias="created_at")  # The date and time the role was created.
    updated_at: str = Field(alias="updated_at")  # The date and time the role was last updated.
    
    class Config:
        populate_by_name = True


class TeamRoleAssignment(BaseModel):
    """TeamRoleAssignment schema from the OpenAPI specification."""
    assignment: str = Field(alias="assignment")  # Determines if the team has a direct, indirect, or mixed relationship to a role
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    description: str = Field(alias="description")
    privacy: str = Field(alias="privacy")
    notification_setting: str = Field(alias="notification_setting")
    permission: str = Field(alias="permission")
    permissions: Dict[str, Any] = Field(alias="permissions")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    members_url: str = Field(alias="members_url")
    repositories_url: str = Field(alias="repositories_url")
    parent: NullableTeamSimple = Field(alias="parent")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class TeamSimple(BaseModel):
    """TeamSimple schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the team
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the team
    members_url: str = Field(alias="members_url")
    name: str = Field(alias="name")  # Name of the team
    description: str = Field(alias="description")  # Description of the team
    permission: str = Field(alias="permission")  # Permission that the team will have for its repositories
    privacy: str = Field(alias="privacy")  # The level of privacy this team should have
    notification_setting: str = Field(alias="notification_setting")  # The notification setting the team has set
    html_url: str = Field(alias="html_url")
    repositories_url: str = Field(alias="repositories_url")
    slug: str = Field(alias="slug")
    ldap_dn: str = Field(alias="ldap_dn")  # Distinguished Name (DN) that team maps to within LDAP environment
    
    class Config:
        populate_by_name = True


class UserRoleAssignment(BaseModel):
    """UserRoleAssignment schema from the OpenAPI specification."""
    assignment: str = Field(alias="assignment")  # Determines if the user has a direct, indirect, or mixed relationship to a role
    inherited_from: List[TeamSimple] = Field(alias="inherited_from")  # Team the user has gotten the role through
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    starred_at: str = Field(alias="starred_at")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class PackageVersion(BaseModel):
    """PackageVersion schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the package version.
    name: str = Field(alias="name")  # The name of the package version.
    url: str = Field(alias="url")
    package_html_url: str = Field(alias="package_html_url")
    html_url: str = Field(alias="html_url")
    license: str = Field(alias="license")
    description: str = Field(alias="description")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    deleted_at: str = Field(alias="deleted_at")
    metadata: Dict[str, Any] = Field(alias="metadata")
    
    class Config:
        populate_by_name = True


class OrganizationProgrammaticAccessGrantRequest(BaseModel):
    """OrganizationProgrammaticAccessGrantRequest schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the request for access via fine-grained personal access token. The `pat_request_id` used to review PAT requests.
    reason: str = Field(alias="reason")  # Reason for requesting access.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    repository_selection: str = Field(alias="repository_selection")  # Type of repository selection requested.
    repositories_url: str = Field(alias="repositories_url")  # URL to the list of repositories requested to be accessed via fine-grained personal access token. Should only be followed when `repository_selection` is `subset`.
    permissions: Dict[str, Any] = Field(alias="permissions")  # Permissions requested, categorized by type of permission.
    created_at: str = Field(alias="created_at")  # Date and time when the request for access was created.
    token_id: int = Field(alias="token_id")  # Unique identifier of the user\'s token. This field can also be found in audit log events and the organization\'s settings for their PAT grants.
    token_name: str = Field(alias="token_name")  # The name given to the user\'s token. This field can also be found in an organization\'s settings page for Active Tokens.
    token_expired: bool = Field(alias="token_expired")  # Whether the associated fine-grained personal access token has expired.
    token_expires_at: str = Field(alias="token_expires_at")  # Date and time when the associated fine-grained personal access token expires.
    token_last_used_at: str = Field(alias="token_last_used_at")  # Date and time when the associated fine-grained personal access token was last used for authentication.
    
    class Config:
        populate_by_name = True


class OrganizationProgrammaticAccessGrant(BaseModel):
    """OrganizationProgrammaticAccessGrant schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the fine-grained personal access token grant. The `pat_id` used to get details about an approved fine-grained personal access token.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    repository_selection: str = Field(alias="repository_selection")  # Type of repository selection requested.
    repositories_url: str = Field(alias="repositories_url")  # URL to the list of repositories the fine-grained personal access token can access. Only follow when `repository_selection` is `subset`.
    permissions: Dict[str, Any] = Field(alias="permissions")  # Permissions requested, categorized by type of permission.
    access_granted_at: str = Field(alias="access_granted_at")  # Date and time when the fine-grained personal access token was approved to access the organization.
    token_id: int = Field(alias="token_id")  # Unique identifier of the user\'s token. This field can also be found in audit log events and the organization\'s settings for their PAT grants.
    token_name: str = Field(alias="token_name")  # The name given to the user\'s token. This field can also be found in an organization\'s settings page for Active Tokens.
    token_expired: bool = Field(alias="token_expired")  # Whether the associated fine-grained personal access token has expired.
    token_expires_at: str = Field(alias="token_expires_at")  # Date and time when the associated fine-grained personal access token expires.
    token_last_used_at: str = Field(alias="token_last_used_at")  # Date and time when the associated fine-grained personal access token was last used for authentication.
    
    class Config:
        populate_by_name = True


class OrgPrivateRegistryConfiguration(BaseModel):
    """OrgPrivateRegistryConfiguration schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the private registry configuration.
    registry_type: str = Field(alias="registry_type")  # The registry type.
    username: str = Field(alias="username")  # The username to use when authenticating with the private registry.
    visibility: str = Field(alias="visibility")  # Which type of organization repositories have access to the private registry.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class OrgPrivateRegistryConfigurationWithSelectedRepositories(BaseModel):
    """OrgPrivateRegistryConfigurationWithSelectedRepositories schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the private registry configuration.
    registry_type: str = Field(alias="registry_type")  # The registry type.
    username: str = Field(alias="username")  # The username to use when authenticating with the private registry.
    visibility: str = Field(alias="visibility")  # Which type of organization repositories have access to the private registry. `selected` means only the repositories specified by `selected_repository_ids` can access the private registry.
    selected_repository_ids: List[int] = Field(alias="selected_repository_ids")  # An array of repository IDs that can access the organization private registry when `visibility` is set to `selected`.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class Project(BaseModel):
    """Project schema from the OpenAPI specification."""
    owner_url: str = Field(alias="owner_url")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    columns_url: str = Field(alias="columns_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # Name of the project
    body: str = Field(alias="body")  # Body of the project
    number: int = Field(alias="number")
    state: str = Field(alias="state")  # State of the project; either \'open\' or \'closed\'
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    organization_permission: str = Field(alias="organization_permission")  # The baseline permission that all organization members have on this project. Only present if owner is an organization.
    private: bool = Field(alias="private")  # Whether or not this project can be seen by everyone. Only present if owner is an organization.
    
    class Config:
        populate_by_name = True


class CustomProperty(BaseModel):
    """CustomProperty schema from the OpenAPI specification."""
    property_name: str = Field(alias="property_name")  # The name of the property
    url: str = Field(alias="url")  # The URL that can be used to fetch, update, or delete info about this property via the API.
    source_type: str = Field(alias="source_type")  # The source type of the property
    value_type: str = Field(alias="value_type")  # The type of the value for the property
    required: bool = Field(alias="required")  # Whether the property is required.
    default_value: str = Field(alias="default_value")  # Default value of the property
    description: str = Field(alias="description")  # Short description of the property
    allowed_values: List[str] = Field(alias="allowed_values")  # An ordered list of the allowed values of the property.
The property can have up to 200 allowed values.
    values_editable_by: str = Field(alias="values_editable_by")  # Who can edit the values of the property
    
    class Config:
        populate_by_name = True


class CustomPropertySetPayload(BaseModel):
    """CustomPropertySetPayload schema from the OpenAPI specification."""
    value_type: str = Field(alias="value_type")  # The type of the value for the property
    required: bool = Field(alias="required")  # Whether the property is required.
    default_value: str = Field(alias="default_value")  # Default value of the property
    description: str = Field(alias="description")  # Short description of the property
    allowed_values: List[str] = Field(alias="allowed_values")  # An ordered list of the allowed values of the property.
The property can have up to 200 allowed values.
    values_editable_by: str = Field(alias="values_editable_by")  # Who can edit the values of the property
    
    class Config:
        populate_by_name = True


class CustomPropertyValue(BaseModel):
    """CustomPropertyValue schema from the OpenAPI specification."""
    property_name: str = Field(alias="property_name")  # The name of the property
    value: str = Field(alias="value")  # The value assigned to the property
    
    class Config:
        populate_by_name = True


class OrgRepoCustomPropertyValues(BaseModel):
    """OrgRepoCustomPropertyValues schema from the OpenAPI specification."""
    repository_id: int = Field(alias="repository_id")
    repository_name: str = Field(alias="repository_name")
    repository_full_name: str = Field(alias="repository_full_name")
    properties: List[CustomPropertyValue] = Field(alias="properties")  # List of custom property names and associated values
    
    class Config:
        populate_by_name = True


class NullableRepository(BaseModel):
    """NullableRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    forks: int = Field(alias="forks")
    permissions: Dict[str, Any] = Field(alias="permissions")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private or public.
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")  # The default branch of the repository.
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")  # Whether this repository acts as a template that can be used to generate new repositories.
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")  # Whether issues are enabled.
    has_projects: bool = Field(alias="has_projects")  # Whether projects are enabled.
    has_wiki: bool = Field(alias="has_wiki")  # Whether the wiki is enabled.
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")  # Whether downloads are enabled.
    has_discussions: bool = Field(alias="has_discussions")  # Whether discussions are enabled.
    archived: bool = Field(alias="archived")  # Whether the repository is archived.
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")  # Whether to allow rebase merges for pull requests.
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")  # Whether to allow squash merges for pull requests.
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow Auto-merge to be used on pull requests.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged
    allow_update_branch: bool = Field(alias="allow_update_branch")  # Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")  # Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:

- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:

- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.

- `PR_TITLE` - default to the pull request\'s title.
- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.

- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    allow_merge_commit: bool = Field(alias="allow_merge_commit")  # Whether to allow merge commits for pull requests.
    allow_forking: bool = Field(alias="allow_forking")  # Whether to allow forking this repo
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")  # Whether to require contributors to sign off on web-based commits
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    master_branch: str = Field(alias="master_branch")
    starred_at: str = Field(alias="starred_at")
    anonymous_access_enabled: bool = Field(alias="anonymous_access_enabled")  # Whether anonymous git access is enabled for this repository
    code_search_index_status: Dict[str, Any] = Field(alias="code_search_index_status")  # The status of the code search index for this repository
    
    class Config:
        populate_by_name = True


class CodeOfConductSimple(BaseModel):
    """CodeOfConductSimple schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class FullRepository(BaseModel):
    """FullRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    full_name: str = Field(alias="full_name")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")
    has_projects: bool = Field(alias="has_projects")
    has_wiki: bool = Field(alias="has_wiki")
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")
    has_discussions: bool = Field(alias="has_discussions")
    archived: bool = Field(alias="archived")
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    permissions: Dict[str, Any] = Field(alias="permissions")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")
    template_repository: NullableRepository = Field(alias="template_repository")  # A repository on GitHub.
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")
    allow_auto_merge: bool = Field(alias="allow_auto_merge")
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")
    allow_merge_commit: bool = Field(alias="allow_merge_commit")
    allow_update_branch: bool = Field(alias="allow_update_branch")
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:

- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:

- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.

  - `PR_TITLE` - default to the pull request\'s title.
  - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.

- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    allow_forking: bool = Field(alias="allow_forking")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    organization: NullableSimpleUser = Field(alias="organization")  # A GitHub user.
    parent: Repository = Field(alias="parent")  # A repository on GitHub.
    source: Repository = Field(alias="source")  # A repository on GitHub.
    forks: int = Field(alias="forks")
    master_branch: str = Field(alias="master_branch")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    anonymous_access_enabled: bool = Field(alias="anonymous_access_enabled")  # Whether anonymous git access is allowed.
    code_of_conduct: CodeOfConductSimple = Field(alias="code_of_conduct")  # Code of Conduct Simple
    security_and_analysis: SecurityAndAnalysis = Field(alias="security_and_analysis")
    custom_properties: Dict[str, Any] = Field(alias="custom_properties")  # The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.
    
    class Config:
        populate_by_name = True


class RepositoryRulesetBypassActor(BaseModel):
    """RepositoryRulesetBypassActor schema from the OpenAPI specification."""
    actor_id: int = Field(alias="actor_id")  # The ID of the actor that can bypass a ruleset. If `actor_type` is `OrganizationAdmin`, this should be `1`. If `actor_type` is `DeployKey`, this should be null. `OrganizationAdmin` is not applicable for personal repositories.
    actor_type: str = Field(alias="actor_type")  # The type of actor that can bypass a ruleset.
    bypass_mode: str = Field(alias="bypass_mode")  # When the specified actor can bypass the ruleset. `pull_request` means that an actor can only bypass rules on pull requests. `pull_request` is not applicable for the `DeployKey` actor type. Also, `pull_request` is only applicable to branch rulesets.
    
    class Config:
        populate_by_name = True


class RepositoryRulesetConditions(BaseModel):
    """RepositoryRulesetConditions schema from the OpenAPI specification."""
    ref_name: Dict[str, Any] = Field(alias="ref_name")
    
    class Config:
        populate_by_name = True


class RepositoryRulesetConditionsRepositoryNameTarget(BaseModel):
    """RepositoryRulesetConditionsRepositoryNameTarget schema from the OpenAPI specification."""
    repository_name: Dict[str, Any] = Field(alias="repository_name")
    
    class Config:
        populate_by_name = True


class RepositoryRulesetConditionsRepositoryIdTarget(BaseModel):
    """RepositoryRulesetConditionsRepositoryIdTarget schema from the OpenAPI specification."""
    repository_id: Dict[str, Any] = Field(alias="repository_id")
    
    class Config:
        populate_by_name = True


class RepositoryRulesetConditionsRepositoryPropertySpec(BaseModel):
    """RepositoryRulesetConditionsRepositoryPropertySpec schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the repository property to target
    property_values: List[str] = Field(alias="property_values")  # The values to match for the repository property
    source: str = Field(alias="source")  # The source of the repository property. Defaults to \'custom\' if not specified.
    
    class Config:
        populate_by_name = True


class RepositoryRulesetConditionsRepositoryPropertyTarget(BaseModel):
    """RepositoryRulesetConditionsRepositoryPropertyTarget schema from the OpenAPI specification."""
    repository_property: Dict[str, Any] = Field(alias="repository_property")
    
    class Config:
        populate_by_name = True


class OrgRulesetConditions(BaseModel):
    """OrgRulesetConditions schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class RepositoryRuleCreation(BaseModel):
    """RepositoryRuleCreation schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class RepositoryRuleUpdate(BaseModel):
    """RepositoryRuleUpdate schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleDeletion(BaseModel):
    """RepositoryRuleDeletion schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class RepositoryRuleRequiredLinearHistory(BaseModel):
    """RepositoryRuleRequiredLinearHistory schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class RepositoryRuleMergeQueue(BaseModel):
    """RepositoryRuleMergeQueue schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleRequiredDeployments(BaseModel):
    """RepositoryRuleRequiredDeployments schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleRequiredSignatures(BaseModel):
    """RepositoryRuleRequiredSignatures schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsReviewer(BaseModel):
    """RepositoryRuleParamsReviewer schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # ID of the reviewer which must review changes to matching files.
    type_field: str = Field(alias="type")  # The type of the reviewer
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsRequiredReviewerConfiguration(BaseModel):
    """RepositoryRuleParamsRequiredReviewerConfiguration schema from the OpenAPI specification."""
    file_patterns: List[str] = Field(alias="file_patterns")  # Array of file patterns. Pull requests which change matching files must be approved by the specified team. File patterns use the same syntax as `.gitignore` files.
    minimum_approvals: int = Field(alias="minimum_approvals")  # Minimum number of approvals required from the specified team. If set to zero, the team will be added to the pull request but approval is optional.
    reviewer: RepositoryRuleParamsReviewer = Field(alias="reviewer")  # A required reviewing team
    
    class Config:
        populate_by_name = True


class RepositoryRulePullRequest(BaseModel):
    """RepositoryRulePullRequest schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsStatusCheckConfiguration(BaseModel):
    """RepositoryRuleParamsStatusCheckConfiguration schema from the OpenAPI specification."""
    context: str = Field(alias="context")  # The status check context name that must be present on the commit.
    integration_id: int = Field(alias="integration_id")  # The optional integration ID that this status check must originate from.
    
    class Config:
        populate_by_name = True


class RepositoryRuleRequiredStatusChecks(BaseModel):
    """RepositoryRuleRequiredStatusChecks schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleNonFastForward(BaseModel):
    """RepositoryRuleNonFastForward schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    
    class Config:
        populate_by_name = True


class RepositoryRuleCommitMessagePattern(BaseModel):
    """RepositoryRuleCommitMessagePattern schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleCommitAuthorEmailPattern(BaseModel):
    """RepositoryRuleCommitAuthorEmailPattern schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleCommitterEmailPattern(BaseModel):
    """RepositoryRuleCommitterEmailPattern schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleBranchNamePattern(BaseModel):
    """RepositoryRuleBranchNamePattern schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleTagNamePattern(BaseModel):
    """RepositoryRuleTagNamePattern schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleFilePathRestriction(BaseModel):
    """RepositoryRuleFilePathRestriction schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleMaxFilePathLength(BaseModel):
    """RepositoryRuleMaxFilePathLength schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleFileExtensionRestriction(BaseModel):
    """RepositoryRuleFileExtensionRestriction schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleMaxFileSize(BaseModel):
    """RepositoryRuleMaxFileSize schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsRestrictedCommits(BaseModel):
    """RepositoryRuleParamsRestrictedCommits schema from the OpenAPI specification."""
    oid: str = Field(alias="oid")  # Full or abbreviated commit hash to reject
    reason: str = Field(alias="reason")  # Reason for restriction
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsWorkflowFileReference(BaseModel):
    """RepositoryRuleParamsWorkflowFileReference schema from the OpenAPI specification."""
    path: str = Field(alias="path")  # The path to the workflow file
    ref: str = Field(alias="ref")  # The ref (branch or tag) of the workflow file to use
    repository_id: int = Field(alias="repository_id")  # The ID of the repository where the workflow is defined
    sha: str = Field(alias="sha")  # The commit SHA of the workflow file to use
    
    class Config:
        populate_by_name = True


class RepositoryRuleWorkflows(BaseModel):
    """RepositoryRuleWorkflows schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRuleParamsCodeScanningTool(BaseModel):
    """RepositoryRuleParamsCodeScanningTool schema from the OpenAPI specification."""
    alerts_threshold: str = Field(alias="alerts_threshold")  # The severity level at which code scanning results that raise alerts block a reference update. For more information on alert severity levels, see \"[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).\"
    security_alerts_threshold: str = Field(alias="security_alerts_threshold")  # The severity level at which code scanning results that raise security alerts block a reference update. For more information on security severity levels, see \"[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels).\"
    tool: str = Field(alias="tool")  # The name of a code scanning tool
    
    class Config:
        populate_by_name = True


class RepositoryRuleCodeScanning(BaseModel):
    """RepositoryRuleCodeScanning schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    parameters: Dict[str, Any] = Field(alias="parameters")
    
    class Config:
        populate_by_name = True


class RepositoryRule(BaseModel):
    """RepositoryRule schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class RepositoryRuleset(BaseModel):
    """RepositoryRuleset schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the ruleset
    name: str = Field(alias="name")  # The name of the ruleset
    target: str = Field(alias="target")  # The target of the ruleset
    source_type: str = Field(alias="source_type")  # The type of the source of the ruleset
    source: str = Field(alias="source")  # The name of the source
    enforcement: str = Field(alias="enforcement")  # The enforcement level of the ruleset. `evaluate` allows admins to test rules before enforcing them. Admins can view insights on the Rule Insights page (`evaluate` is only available with GitHub Enterprise).
    bypass_actors: List[RepositoryRulesetBypassActor] = Field(alias="bypass_actors")  # The actors that can bypass the rules in this ruleset
    current_user_can_bypass: str = Field(alias="current_user_can_bypass")  # The bypass type of the user making the API request for this ruleset. This field is only returned when
querying the repository-level endpoint.
    node_id: str = Field(alias="node_id")
    links: Dict[str, Any] = Field(alias="_links")
    conditions: Any = Field(alias="conditions")
    rules: List[RepositoryRule] = Field(alias="rules")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class RuleSuite(BaseModel):
    """RuleSuite schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the rule insight.
    actor_id: int = Field(alias="actor_id")  # The number that identifies the user.
    actor_name: str = Field(alias="actor_name")  # The handle for the GitHub user account.
    before_sha: str = Field(alias="before_sha")  # The first commit sha before the push evaluation.
    after_sha: str = Field(alias="after_sha")  # The last commit sha in the push evaluation.
    ref: str = Field(alias="ref")  # The ref name that the evaluation ran on.
    repository_id: int = Field(alias="repository_id")  # The ID of the repository associated with the rule evaluation.
    repository_name: str = Field(alias="repository_name")  # The name of the repository without the `.git` extension.
    pushed_at: str = Field(alias="pushed_at")
    result: str = Field(alias="result")  # The result of the rule evaluations for rules with the `active` enforcement status.
    evaluation_result: str = Field(alias="evaluation_result")  # The result of the rule evaluations for rules with the `active` and `evaluate` enforcement statuses, demonstrating whether rules would pass or fail if all rules in the rule suite were `active`. Null if no rules with `evaluate` enforcement status were run.
    rule_evaluations: List[Dict[str, Any]] = Field(alias="rule_evaluations")  # Details on the evaluated rules.
    
    class Config:
        populate_by_name = True


class RulesetVersion(BaseModel):
    """RulesetVersion schema from the OpenAPI specification."""
    version_id: int = Field(alias="version_id")  # The ID of the previous version of the ruleset
    actor: Dict[str, Any] = Field(alias="actor")  # The actor who updated the ruleset
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class RulesetVersionWithState(BaseModel):
    """RulesetVersionWithState schema from the OpenAPI specification."""
    version_id: int = Field(alias="version_id")  # The ID of the previous version of the ruleset
    actor: Dict[str, Any] = Field(alias="actor")  # The actor who updated the ruleset
    updated_at: str = Field(alias="updated_at")
    state: Dict[str, Any] = Field(alias="state")  # The state of the ruleset version
    
    class Config:
        populate_by_name = True


class RepositoryAdvisoryVulnerability(BaseModel):
    """RepositoryAdvisoryVulnerability schema from the OpenAPI specification."""
    package: Dict[str, Any] = Field(alias="package")  # The name of the package affected by the vulnerability.
    vulnerable_version_range: str = Field(alias="vulnerable_version_range")  # The range of the package versions affected by the vulnerability.
    patched_versions: str = Field(alias="patched_versions")  # The package version(s) that resolve the vulnerability.
    vulnerable_functions: List[str] = Field(alias="vulnerable_functions")  # The functions in the package that are affected.
    
    class Config:
        populate_by_name = True


class RepositoryAdvisoryCredit(BaseModel):
    """RepositoryAdvisoryCredit schema from the OpenAPI specification."""
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    type_field: str = Field(alias="type")  # The type of credit the user is receiving.
    state: str = Field(alias="state")  # The state of the user\'s acceptance of the credit.
    
    class Config:
        populate_by_name = True


class RepositoryAdvisory(BaseModel):
    """RepositoryAdvisory schema from the OpenAPI specification."""
    ghsa_id: str = Field(alias="ghsa_id")  # The GitHub Security Advisory ID.
    cve_id: str = Field(alias="cve_id")  # The Common Vulnerabilities and Exposures (CVE) ID.
    url: str = Field(alias="url")  # The API URL for the advisory.
    html_url: str = Field(alias="html_url")  # The URL for the advisory.
    summary: str = Field(alias="summary")  # A short summary of the advisory.
    description: str = Field(alias="description")  # A detailed description of what the advisory entails.
    severity: str = Field(alias="severity")  # The severity of the advisory.
    author: Any = Field(alias="author")  # The author of the advisory.
    publisher: Any = Field(alias="publisher")  # The publisher of the advisory.
    identifiers: List[Dict[str, Any]] = Field(alias="identifiers")
    state: str = Field(alias="state")  # The state of the advisory.
    created_at: str = Field(alias="created_at")  # The date and time of when the advisory was created, in ISO 8601 format.
    updated_at: str = Field(alias="updated_at")  # The date and time of when the advisory was last updated, in ISO 8601 format.
    published_at: str = Field(alias="published_at")  # The date and time of when the advisory was published, in ISO 8601 format.
    closed_at: str = Field(alias="closed_at")  # The date and time of when the advisory was closed, in ISO 8601 format.
    withdrawn_at: str = Field(alias="withdrawn_at")  # The date and time of when the advisory was withdrawn, in ISO 8601 format.
    submission: Dict[str, Any] = Field(alias="submission")
    vulnerabilities: List[RepositoryAdvisoryVulnerability] = Field(alias="vulnerabilities")
    cvss: Dict[str, Any] = Field(alias="cvss")
    cvss_severities: CvssSeverities = Field(alias="cvss_severities")
    cwes: List[Dict[str, Any]] = Field(alias="cwes")
    cwe_ids: List[str] = Field(alias="cwe_ids")  # A list of only the CWE IDs.
    credits: List[Dict[str, Any]] = Field(alias="credits")
    credits_detailed: List[RepositoryAdvisoryCredit] = Field(alias="credits_detailed")
    collaborating_users: List[SimpleUser] = Field(alias="collaborating_users")  # A list of users that collaborate on the advisory.
    collaborating_teams: List[Team] = Field(alias="collaborating_teams")  # A list of teams that collaborate on the advisory.
    private_fork: Any = Field(alias="private_fork")  # A temporary private fork of the advisory\'s repository for collaborating on a fix.
    
    class Config:
        populate_by_name = True


class ActionsBillingUsage(BaseModel):
    """ActionsBillingUsage schema from the OpenAPI specification."""
    total_minutes_used: int = Field(alias="total_minutes_used")  # The sum of the free and paid GitHub Actions minutes used.
    total_paid_minutes_used: int = Field(alias="total_paid_minutes_used")  # The total paid GitHub Actions minutes used.
    included_minutes: int = Field(alias="included_minutes")  # The amount of free GitHub Actions minutes available.
    minutes_used_breakdown: Dict[str, Any] = Field(alias="minutes_used_breakdown")
    
    class Config:
        populate_by_name = True


class PackagesBillingUsage(BaseModel):
    """PackagesBillingUsage schema from the OpenAPI specification."""
    total_gigabytes_bandwidth_used: int = Field(alias="total_gigabytes_bandwidth_used")  # Sum of the free and paid storage space (GB) for GitHuub Packages.
    total_paid_gigabytes_bandwidth_used: int = Field(alias="total_paid_gigabytes_bandwidth_used")  # Total paid storage space (GB) for GitHuub Packages.
    included_gigabytes_bandwidth: int = Field(alias="included_gigabytes_bandwidth")  # Free storage space (GB) for GitHub Packages.
    
    class Config:
        populate_by_name = True


class CombinedBillingUsage(BaseModel):
    """CombinedBillingUsage schema from the OpenAPI specification."""
    days_left_in_billing_cycle: int = Field(alias="days_left_in_billing_cycle")  # Numbers of days left in billing cycle.
    estimated_paid_storage_for_month: int = Field(alias="estimated_paid_storage_for_month")  # Estimated storage space (GB) used in billing cycle.
    estimated_storage_for_month: int = Field(alias="estimated_storage_for_month")  # Estimated sum of free and paid storage space (GB) used in billing cycle.
    
    class Config:
        populate_by_name = True


class NetworkConfiguration(BaseModel):
    """NetworkConfiguration schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The unique identifier of the network configuration.
    name: str = Field(alias="name")  # The name of the network configuration.
    compute_service: str = Field(alias="compute_service")  # The hosted compute service the network configuration supports.
    network_settings_ids: List[str] = Field(alias="network_settings_ids")  # The unique identifier of each network settings in the configuration.
    created_on: str = Field(alias="created_on")  # The time at which the network configuration was created, in ISO 8601 format.
    
    class Config:
        populate_by_name = True


class NetworkSettings(BaseModel):
    """NetworkSettings schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The unique identifier of the network settings resource.
    network_configuration_id: str = Field(alias="network_configuration_id")  # The identifier of the network configuration that is using this settings resource.
    name: str = Field(alias="name")  # The name of the network settings resource.
    subnet_id: str = Field(alias="subnet_id")  # The subnet this network settings resource is configured for.
    region: str = Field(alias="region")  # The location of the subnet this network settings resource is configured for.
    
    class Config:
        populate_by_name = True


class TeamOrganization(BaseModel):
    """TeamOrganization schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    hooks_url: str = Field(alias="hooks_url")
    issues_url: str = Field(alias="issues_url")
    members_url: str = Field(alias="members_url")
    public_members_url: str = Field(alias="public_members_url")
    avatar_url: str = Field(alias="avatar_url")
    description: str = Field(alias="description")
    name: str = Field(alias="name")
    company: str = Field(alias="company")
    blog: str = Field(alias="blog")
    location: str = Field(alias="location")
    email: str = Field(alias="email")
    twitter_username: str = Field(alias="twitter_username")
    is_verified: bool = Field(alias="is_verified")
    has_organization_projects: bool = Field(alias="has_organization_projects")
    has_repository_projects: bool = Field(alias="has_repository_projects")
    public_repos: int = Field(alias="public_repos")
    public_gists: int = Field(alias="public_gists")
    followers: int = Field(alias="followers")
    following: int = Field(alias="following")
    html_url: str = Field(alias="html_url")
    created_at: str = Field(alias="created_at")
    type_field: str = Field(alias="type")
    total_private_repos: int = Field(alias="total_private_repos")
    owned_private_repos: int = Field(alias="owned_private_repos")
    private_gists: int = Field(alias="private_gists")
    disk_usage: int = Field(alias="disk_usage")
    collaborators: int = Field(alias="collaborators")
    billing_email: str = Field(alias="billing_email")
    plan: Dict[str, Any] = Field(alias="plan")
    default_repository_permission: str = Field(alias="default_repository_permission")
    members_can_create_repositories: bool = Field(alias="members_can_create_repositories")
    two_factor_requirement_enabled: bool = Field(alias="two_factor_requirement_enabled")
    members_allowed_repository_creation_type: str = Field(alias="members_allowed_repository_creation_type")
    members_can_create_public_repositories: bool = Field(alias="members_can_create_public_repositories")
    members_can_create_private_repositories: bool = Field(alias="members_can_create_private_repositories")
    members_can_create_internal_repositories: bool = Field(alias="members_can_create_internal_repositories")
    members_can_create_pages: bool = Field(alias="members_can_create_pages")
    members_can_create_public_pages: bool = Field(alias="members_can_create_public_pages")
    members_can_create_private_pages: bool = Field(alias="members_can_create_private_pages")
    members_can_fork_private_repositories: bool = Field(alias="members_can_fork_private_repositories")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    updated_at: str = Field(alias="updated_at")
    archived_at: str = Field(alias="archived_at")
    
    class Config:
        populate_by_name = True


class TeamFull(BaseModel):
    """TeamFull schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the team
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the team
    html_url: str = Field(alias="html_url")
    name: str = Field(alias="name")  # Name of the team
    slug: str = Field(alias="slug")
    description: str = Field(alias="description")
    privacy: str = Field(alias="privacy")  # The level of privacy this team should have
    notification_setting: str = Field(alias="notification_setting")  # The notification setting the team has set
    permission: str = Field(alias="permission")  # Permission that the team will have for its repositories
    members_url: str = Field(alias="members_url")
    repositories_url: str = Field(alias="repositories_url")
    parent: NullableTeamSimple = Field(alias="parent")  # Groups of organization members that gives permissions on specified repositories.
    members_count: int = Field(alias="members_count")
    repos_count: int = Field(alias="repos_count")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    organization: TeamOrganization = Field(alias="organization")  # Team Organization
    ldap_dn: str = Field(alias="ldap_dn")  # Distinguished Name (DN) that team maps to within LDAP environment
    
    class Config:
        populate_by_name = True


class TeamDiscussion(BaseModel):
    """TeamDiscussion schema from the OpenAPI specification."""
    author: NullableSimpleUser = Field(alias="author")  # A GitHub user.
    body: str = Field(alias="body")  # The main text of the discussion.
    body_html: str = Field(alias="body_html")
    body_version: str = Field(alias="body_version")  # The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server.
    comments_count: int = Field(alias="comments_count")
    comments_url: str = Field(alias="comments_url")
    created_at: str = Field(alias="created_at")
    last_edited_at: str = Field(alias="last_edited_at")
    html_url: str = Field(alias="html_url")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The unique sequence number of a team discussion.
    pinned: bool = Field(alias="pinned")  # Whether or not this discussion should be pinned for easy retrieval.
    private: bool = Field(alias="private")  # Whether or not this discussion should be restricted to team members and organization owners.
    team_url: str = Field(alias="team_url")
    title: str = Field(alias="title")  # The title of the discussion.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class TeamDiscussionComment(BaseModel):
    """TeamDiscussionComment schema from the OpenAPI specification."""
    author: NullableSimpleUser = Field(alias="author")  # A GitHub user.
    body: str = Field(alias="body")  # The main text of the comment.
    body_html: str = Field(alias="body_html")
    body_version: str = Field(alias="body_version")  # The current version of the body content. If provided, this update operation will be rejected if the given version does not match the latest version on the server.
    created_at: str = Field(alias="created_at")
    last_edited_at: str = Field(alias="last_edited_at")
    discussion_url: str = Field(alias="discussion_url")
    html_url: str = Field(alias="html_url")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The unique sequence number of a team discussion comment.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class Reaction(BaseModel):
    """Reaction schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    content: str = Field(alias="content")  # The reaction to use
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class TeamMembership(BaseModel):
    """TeamMembership schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    role: str = Field(alias="role")  # The role of the user in the team.
    state: str = Field(alias="state")  # The state of the user\'s membership in the team.
    
    class Config:
        populate_by_name = True


class TeamProject(BaseModel):
    """TeamProject schema from the OpenAPI specification."""
    owner_url: str = Field(alias="owner_url")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    columns_url: str = Field(alias="columns_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    body: str = Field(alias="body")
    number: int = Field(alias="number")
    state: str = Field(alias="state")
    creator: SimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    organization_permission: str = Field(alias="organization_permission")  # The organization permission for this project. Only present when owner is an organization.
    private: bool = Field(alias="private")  # Whether the project is private or not. Only present when owner is an organization.
    permissions: Dict[str, Any] = Field(alias="permissions")
    
    class Config:
        populate_by_name = True


class TeamRepository(BaseModel):
    """TeamRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    forks: int = Field(alias="forks")
    permissions: Dict[str, Any] = Field(alias="permissions")
    role_name: str = Field(alias="role_name")
    owner: NullableSimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private or public.
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")
    default_branch: str = Field(alias="default_branch")  # The default branch of the repository.
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")  # Whether this repository acts as a template that can be used to generate new repositories.
    topics: List[str] = Field(alias="topics")
    has_issues: bool = Field(alias="has_issues")  # Whether issues are enabled.
    has_projects: bool = Field(alias="has_projects")  # Whether projects are enabled.
    has_wiki: bool = Field(alias="has_wiki")  # Whether the wiki is enabled.
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")  # Whether downloads are enabled.
    archived: bool = Field(alias="archived")  # Whether the repository is archived.
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")  # Whether to allow rebase merges for pull requests.
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")  # Whether to allow squash merges for pull requests.
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow Auto-merge to be used on pull requests.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged
    allow_merge_commit: bool = Field(alias="allow_merge_commit")  # Whether to allow merge commits for pull requests.
    allow_forking: bool = Field(alias="allow_forking")  # Whether to allow forking this repo
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")  # Whether to require contributors to sign off on web-based commits
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    master_branch: str = Field(alias="master_branch")
    
    class Config:
        populate_by_name = True


class ProjectCard(BaseModel):
    """ProjectCard schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")  # The project card\'s ID
    node_id: str = Field(alias="node_id")
    note: str = Field(alias="note")
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    archived: bool = Field(alias="archived")  # Whether or not the card is archived
    column_name: str = Field(alias="column_name")
    project_id: str = Field(alias="project_id")
    column_url: str = Field(alias="column_url")
    content_url: str = Field(alias="content_url")
    project_url: str = Field(alias="project_url")
    
    class Config:
        populate_by_name = True


class ProjectColumn(BaseModel):
    """ProjectColumn schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    project_url: str = Field(alias="project_url")
    cards_url: str = Field(alias="cards_url")
    id_field: int = Field(alias="id")  # The unique identifier of the project column
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # Name of the project column
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class ProjectCollaboratorPermission(BaseModel):
    """ProjectCollaboratorPermission schema from the OpenAPI specification."""
    permission: str = Field(alias="permission")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class RateLimit(BaseModel):
    """RateLimit schema from the OpenAPI specification."""
    limit: int = Field(alias="limit")
    remaining: int = Field(alias="remaining")
    reset: int = Field(alias="reset")
    used: int = Field(alias="used")
    
    class Config:
        populate_by_name = True


class RateLimitOverview(BaseModel):
    """RateLimitOverview schema from the OpenAPI specification."""
    resources: Dict[str, Any] = Field(alias="resources")
    rate: RateLimit = Field(alias="rate")
    
    class Config:
        populate_by_name = True


class Artifact(BaseModel):
    """Artifact schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the artifact.
    size_in_bytes: int = Field(alias="size_in_bytes")  # The size in bytes of the artifact.
    url: str = Field(alias="url")
    archive_download_url: str = Field(alias="archive_download_url")
    expired: bool = Field(alias="expired")  # Whether or not the artifact has expired.
    created_at: str = Field(alias="created_at")
    expires_at: str = Field(alias="expires_at")
    updated_at: str = Field(alias="updated_at")
    digest: str = Field(alias="digest")  # The SHA256 digest of the artifact. This field will only be populated on artifacts uploaded with upload-artifact v4 or newer. For older versions, this field will be null.
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class ActionsCacheList(BaseModel):
    """ActionsCacheList schema from the OpenAPI specification."""
    total_count: int = Field(alias="total_count")  # Total number of caches
    actions_caches: List[Dict[str, Any]] = Field(alias="actions_caches")  # Array of caches
    
    class Config:
        populate_by_name = True


class Job(BaseModel):
    """Job schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The id of the job.
    run_id: int = Field(alias="run_id")  # The id of the associated workflow run.
    run_url: str = Field(alias="run_url")
    run_attempt: int = Field(alias="run_attempt")  # Attempt number of the associated workflow run, 1 for first attempt and higher if the workflow was re-run.
    node_id: str = Field(alias="node_id")
    head_sha: str = Field(alias="head_sha")  # The SHA of the commit that is being run.
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    status: str = Field(alias="status")  # The phase of the lifecycle that the job is currently in.
    conclusion: str = Field(alias="conclusion")  # The outcome of the job.
    created_at: str = Field(alias="created_at")  # The time that the job created, in ISO 8601 format.
    started_at: str = Field(alias="started_at")  # The time that the job started, in ISO 8601 format.
    completed_at: str = Field(alias="completed_at")  # The time that the job finished, in ISO 8601 format.
    name: str = Field(alias="name")  # The name of the job.
    steps: List[Dict[str, Any]] = Field(alias="steps")  # Steps in this job.
    check_run_url: str = Field(alias="check_run_url")
    labels: List[str] = Field(alias="labels")  # Labels for the workflow job. Specified by the \"runs_on\" attribute in the action\'s workflow file.
    runner_id: int = Field(alias="runner_id")  # The ID of the runner to which this job has been assigned. (If a runner hasn\'t yet been assigned, this will be null.)
    runner_name: str = Field(alias="runner_name")  # The name of the runner to which this job has been assigned. (If a runner hasn\'t yet been assigned, this will be null.)
    runner_group_id: int = Field(alias="runner_group_id")  # The ID of the runner group to which this job has been assigned. (If a runner hasn\'t yet been assigned, this will be null.)
    runner_group_name: str = Field(alias="runner_group_name")  # The name of the runner group to which this job has been assigned. (If a runner hasn\'t yet been assigned, this will be null.)
    workflow_name: str = Field(alias="workflow_name")  # The name of the workflow.
    head_branch: str = Field(alias="head_branch")  # The name of the current branch.
    
    class Config:
        populate_by_name = True


class OidcCustomSubRepo(BaseModel):
    """OidcCustomSubRepo schema from the OpenAPI specification."""
    use_default: bool = Field(alias="use_default")  # Whether to use the default template or not. If `true`, the `include_claim_keys` field is ignored.
    include_claim_keys: List[str] = Field(alias="include_claim_keys")  # Array of unique strings. Each claim key can only contain alphanumeric characters and underscores.
    
    class Config:
        populate_by_name = True


class ActionsSecret(BaseModel):
    """ActionsSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class ActionsVariable(BaseModel):
    """ActionsVariable schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the variable.
    value: str = Field(alias="value")  # The value of the variable.
    created_at: str = Field(alias="created_at")  # The date and time at which the variable was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the variable was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    
    class Config:
        populate_by_name = True


class ActionsRepositoryPermissions(BaseModel):
    """ActionsRepositoryPermissions schema from the OpenAPI specification."""
    enabled: bool = Field(alias="enabled")  # Whether GitHub Actions is enabled on the repository.
    allowed_actions: str = Field(alias="allowed_actions")  # The permissions policy that controls the actions and reusable workflows that are allowed to run.
    selected_actions_url: str = Field(alias="selected_actions_url")  # The API URL to use to get or set the actions and reusable workflows that are allowed to run, when `allowed_actions` is set to `selected`.
    
    class Config:
        populate_by_name = True


class ActionsWorkflowAccessToRepository(BaseModel):
    """ActionsWorkflowAccessToRepository schema from the OpenAPI specification."""
    access_level: str = Field(alias="access_level")  # Defines the level of access that workflows outside of the repository have to actions and reusable workflows within the
repository.

`none` means the access is only possible from workflows in this repository. `user` level access allows sharing across user owned private repositories only. `organization` level access allows sharing across the organization.
    
    class Config:
        populate_by_name = True


class ReferencedWorkflow(BaseModel):
    """ReferencedWorkflow schema from the OpenAPI specification."""
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    ref: str = Field(alias="ref")
    
    class Config:
        populate_by_name = True


class PullRequestMinimal(BaseModel):
    """PullRequestMinimal schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    number: int = Field(alias="number")
    url: str = Field(alias="url")
    head: Dict[str, Any] = Field(alias="head")
    base: Dict[str, Any] = Field(alias="base")
    
    class Config:
        populate_by_name = True


class NullableSimpleCommit(BaseModel):
    """NullableSimpleCommit schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # SHA for the commit
    tree_id: str = Field(alias="tree_id")  # SHA for the commit\'s tree
    message: str = Field(alias="message")  # Message describing the purpose of the commit
    timestamp: str = Field(alias="timestamp")  # Timestamp of the commit
    author: Dict[str, Any] = Field(alias="author")  # Information about the Git author
    committer: Dict[str, Any] = Field(alias="committer")  # Information about the Git committer
    
    class Config:
        populate_by_name = True


class WorkflowRun(BaseModel):
    """WorkflowRun schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the workflow run.
    name: str = Field(alias="name")  # The name of the workflow run.
    node_id: str = Field(alias="node_id")
    check_suite_id: int = Field(alias="check_suite_id")  # The ID of the associated check suite.
    check_suite_node_id: str = Field(alias="check_suite_node_id")  # The node ID of the associated check suite.
    head_branch: str = Field(alias="head_branch")
    head_sha: str = Field(alias="head_sha")  # The SHA of the head commit that points to the version of the workflow being run.
    path: str = Field(alias="path")  # The full path of the workflow
    run_number: int = Field(alias="run_number")  # The auto incrementing run number for the workflow run.
    run_attempt: int = Field(alias="run_attempt")  # Attempt number of the run, 1 for first attempt and higher if the workflow was re-run.
    referenced_workflows: List[ReferencedWorkflow] = Field(alias="referenced_workflows")
    event: str = Field(alias="event")
    status: str = Field(alias="status")
    conclusion: str = Field(alias="conclusion")
    workflow_id: int = Field(alias="workflow_id")  # The ID of the parent workflow.
    url: str = Field(alias="url")  # The URL to the workflow run.
    html_url: str = Field(alias="html_url")
    pull_requests: List[PullRequestMinimal] = Field(alias="pull_requests")  # Pull requests that are open with a `head_sha` or `head_branch` that matches the workflow run. The returned pull requests do not necessarily indicate pull requests that triggered the run.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    triggering_actor: SimpleUser = Field(alias="triggering_actor")  # A GitHub user.
    run_started_at: str = Field(alias="run_started_at")  # The start time of the latest run. Resets on re-run.
    jobs_url: str = Field(alias="jobs_url")  # The URL to the jobs for the workflow run.
    logs_url: str = Field(alias="logs_url")  # The URL to download the logs for the workflow run.
    check_suite_url: str = Field(alias="check_suite_url")  # The URL to the associated check suite.
    artifacts_url: str = Field(alias="artifacts_url")  # The URL to the artifacts for the workflow run.
    cancel_url: str = Field(alias="cancel_url")  # The URL to cancel the workflow run.
    rerun_url: str = Field(alias="rerun_url")  # The URL to rerun the workflow run.
    previous_attempt_url: str = Field(alias="previous_attempt_url")  # The URL to the previous attempted run of this workflow, if one exists.
    workflow_url: str = Field(alias="workflow_url")  # The URL to the workflow.
    head_commit: NullableSimpleCommit = Field(alias="head_commit")  # A commit.
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    head_repository: MinimalRepository = Field(alias="head_repository")  # Minimal Repository
    head_repository_id: int = Field(alias="head_repository_id")
    display_title: str = Field(alias="display_title")  # The event-specific title associated with the run or the run-name if set, or the value of `run-name` if it is set in the workflow.
    
    class Config:
        populate_by_name = True


class EnvironmentApprovals(BaseModel):
    """EnvironmentApprovals schema from the OpenAPI specification."""
    environments: List[Dict[str, Any]] = Field(alias="environments")  # The list of environments that were approved or rejected
    state: str = Field(alias="state")  # Whether deployment to the environment(s) was approved or rejected or pending (with comments)
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    comment: str = Field(alias="comment")  # The comment submitted with the deployment review
    
    class Config:
        populate_by_name = True


class ReviewCustomGatesCommentRequired(BaseModel):
    """ReviewCustomGatesCommentRequired schema from the OpenAPI specification."""
    environment_name: str = Field(alias="environment_name")  # The name of the environment to approve or reject.
    comment: str = Field(alias="comment")  # Comment associated with the pending deployment protection rule. **Required when state is not provided.**
    
    class Config:
        populate_by_name = True


class ReviewCustomGatesStateRequired(BaseModel):
    """ReviewCustomGatesStateRequired schema from the OpenAPI specification."""
    environment_name: str = Field(alias="environment_name")  # The name of the environment to approve or reject.
    state: str = Field(alias="state")  # Whether to approve or reject deployment to the specified environments.
    comment: str = Field(alias="comment")  # Optional comment to include with the review.
    
    class Config:
        populate_by_name = True


class PendingDeployment(BaseModel):
    """PendingDeployment schema from the OpenAPI specification."""
    environment: Dict[str, Any] = Field(alias="environment")
    wait_timer: int = Field(alias="wait_timer")  # The set duration of the wait timer
    wait_timer_started_at: str = Field(alias="wait_timer_started_at")  # The time that the wait timer began.
    current_user_can_approve: bool = Field(alias="current_user_can_approve")  # Whether the currently authenticated user can approve the deployment
    reviewers: List[Dict[str, Any]] = Field(alias="reviewers")  # The people or teams that may approve jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.
    
    class Config:
        populate_by_name = True


class Deployment(BaseModel):
    """Deployment schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")  # Unique identifier of the deployment
    node_id: str = Field(alias="node_id")
    sha: str = Field(alias="sha")
    ref: str = Field(alias="ref")  # The ref to deploy. This can be a branch, tag, or sha.
    task: str = Field(alias="task")  # Parameter to specify a task to execute
    payload: Any = Field(alias="payload")
    original_environment: str = Field(alias="original_environment")
    environment: str = Field(alias="environment")  # Name for the target deployment environment.
    description: str = Field(alias="description")
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    statuses_url: str = Field(alias="statuses_url")
    repository_url: str = Field(alias="repository_url")
    transient_environment: bool = Field(alias="transient_environment")  # Specifies if the given environment is will no longer exist at some point in the future. Default: false.
    production_environment: bool = Field(alias="production_environment")  # Specifies if the given environment is one that end-users directly interact with. Default: false.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    
    class Config:
        populate_by_name = True


class WorkflowRunUsage(BaseModel):
    """WorkflowRunUsage schema from the OpenAPI specification."""
    billable: Dict[str, Any] = Field(alias="billable")
    run_duration_ms: int = Field(alias="run_duration_ms")
    
    class Config:
        populate_by_name = True


class Workflow(BaseModel):
    """Workflow schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    state: str = Field(alias="state")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    badge_url: str = Field(alias="badge_url")
    deleted_at: str = Field(alias="deleted_at")
    
    class Config:
        populate_by_name = True


class WorkflowUsage(BaseModel):
    """WorkflowUsage schema from the OpenAPI specification."""
    billable: Dict[str, Any] = Field(alias="billable")
    
    class Config:
        populate_by_name = True


class Activity(BaseModel):
    """Activity schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    before: str = Field(alias="before")  # The SHA of the commit before the activity.
    after: str = Field(alias="after")  # The SHA of the commit after the activity.
    ref: str = Field(alias="ref")  # The full Git reference, formatted as `refs/heads/<branch name>`.
    timestamp: str = Field(alias="timestamp")  # The time when the activity occurred.
    activity_type: str = Field(alias="activity_type")  # The type of the activity that was performed.
    actor: NullableSimpleUser = Field(alias="actor")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class Autolink(BaseModel):
    """Autolink schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    key_prefix: str = Field(alias="key_prefix")  # The prefix of a key that is linkified.
    url_template: str = Field(alias="url_template")  # A template for the target URL that is generated if a key was found.
    is_alphanumeric: bool = Field(alias="is_alphanumeric")  # Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters.
    
    class Config:
        populate_by_name = True


class CheckAutomatedSecurityFixes(BaseModel):
    """CheckAutomatedSecurityFixes schema from the OpenAPI specification."""
    enabled: bool = Field(alias="enabled")  # Whether Dependabot security updates are enabled for the repository.
    paused: bool = Field(alias="paused")  # Whether Dependabot security updates are paused for the repository.
    
    class Config:
        populate_by_name = True


class ProtectedBranchRequiredStatusCheck(BaseModel):
    """ProtectedBranchRequiredStatusCheck schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    enforcement_level: str = Field(alias="enforcement_level")
    contexts: List[str] = Field(alias="contexts")
    checks: List[Dict[str, Any]] = Field(alias="checks")
    contexts_url: str = Field(alias="contexts_url")
    strict: bool = Field(alias="strict")
    
    class Config:
        populate_by_name = True


class ProtectedBranchAdminEnforced(BaseModel):
    """ProtectedBranchAdminEnforced schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    enabled: bool = Field(alias="enabled")
    
    class Config:
        populate_by_name = True


class ProtectedBranchPullRequestReview(BaseModel):
    """ProtectedBranchPullRequestReview schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    dismissal_restrictions: Dict[str, Any] = Field(alias="dismissal_restrictions")
    bypass_pull_request_allowances: Dict[str, Any] = Field(alias="bypass_pull_request_allowances")  # Allow specific users, teams, or apps to bypass pull request requirements.
    dismiss_stale_reviews: bool = Field(alias="dismiss_stale_reviews")
    require_code_owner_reviews: bool = Field(alias="require_code_owner_reviews")
    required_approving_review_count: int = Field(alias="required_approving_review_count")
    require_last_push_approval: bool = Field(alias="require_last_push_approval")  # Whether the most recent push must be approved by someone other than the person who pushed it.
    
    class Config:
        populate_by_name = True


class BranchRestrictionPolicy(BaseModel):
    """BranchRestrictionPolicy schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    users_url: str = Field(alias="users_url")
    teams_url: str = Field(alias="teams_url")
    apps_url: str = Field(alias="apps_url")
    users: List[Dict[str, Any]] = Field(alias="users")
    teams: List[Dict[str, Any]] = Field(alias="teams")
    apps: List[Dict[str, Any]] = Field(alias="apps")
    
    class Config:
        populate_by_name = True


class BranchProtection(BaseModel):
    """BranchProtection schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    enabled: bool = Field(alias="enabled")
    required_status_checks: ProtectedBranchRequiredStatusCheck = Field(alias="required_status_checks")  # Protected Branch Required Status Check
    enforce_admins: ProtectedBranchAdminEnforced = Field(alias="enforce_admins")  # Protected Branch Admin Enforced
    required_pull_request_reviews: ProtectedBranchPullRequestReview = Field(alias="required_pull_request_reviews")  # Protected Branch Pull Request Review
    restrictions: BranchRestrictionPolicy = Field(alias="restrictions")  # Branch Restriction Policy
    required_linear_history: Dict[str, Any] = Field(alias="required_linear_history")
    allow_force_pushes: Dict[str, Any] = Field(alias="allow_force_pushes")
    allow_deletions: Dict[str, Any] = Field(alias="allow_deletions")
    block_creations: Dict[str, Any] = Field(alias="block_creations")
    required_conversation_resolution: Dict[str, Any] = Field(alias="required_conversation_resolution")
    name: str = Field(alias="name")
    protection_url: str = Field(alias="protection_url")
    required_signatures: Dict[str, Any] = Field(alias="required_signatures")
    lock_branch: Dict[str, Any] = Field(alias="lock_branch")  # Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.
    allow_fork_syncing: Dict[str, Any] = Field(alias="allow_fork_syncing")  # Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    
    class Config:
        populate_by_name = True


class ShortBranch(BaseModel):
    """ShortBranch schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    commit: Dict[str, Any] = Field(alias="commit")
    protected: bool = Field(alias="protected")
    protection: BranchProtection = Field(alias="protection")  # Branch Protection
    protection_url: str = Field(alias="protection_url")
    
    class Config:
        populate_by_name = True


class NullableGitUser(BaseModel):
    """NullableGitUser schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    email: str = Field(alias="email")
    date: str = Field(alias="date")
    
    class Config:
        populate_by_name = True


class Verification(BaseModel):
    """Verification schema from the OpenAPI specification."""
    verified: bool = Field(alias="verified")
    reason: str = Field(alias="reason")
    payload: str = Field(alias="payload")
    signature: str = Field(alias="signature")
    verified_at: str = Field(alias="verified_at")
    
    class Config:
        populate_by_name = True


class DiffEntry(BaseModel):
    """DiffEntry schema from the OpenAPI specification."""
    sha: str = Field(alias="sha")
    filename: str = Field(alias="filename")
    status: str = Field(alias="status")
    additions: int = Field(alias="additions")
    deletions: int = Field(alias="deletions")
    changes: int = Field(alias="changes")
    blob_url: str = Field(alias="blob_url")
    raw_url: str = Field(alias="raw_url")
    contents_url: str = Field(alias="contents_url")
    patch: str = Field(alias="patch")
    previous_filename: str = Field(alias="previous_filename")
    
    class Config:
        populate_by_name = True


class Commit(BaseModel):
    """Commit schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    sha: str = Field(alias="sha")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    comments_url: str = Field(alias="comments_url")
    commit: Dict[str, Any] = Field(alias="commit")
    author: Any = Field(alias="author")
    committer: Any = Field(alias="committer")
    parents: List[Dict[str, Any]] = Field(alias="parents")
    stats: Dict[str, Any] = Field(alias="stats")
    files: List[DiffEntry] = Field(alias="files")
    
    class Config:
        populate_by_name = True


class BranchWithProtection(BaseModel):
    """BranchWithProtection schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    commit: Commit = Field(alias="commit")  # Commit
    links: Dict[str, Any] = Field(alias="_links")
    protected: bool = Field(alias="protected")
    protection: BranchProtection = Field(alias="protection")  # Branch Protection
    protection_url: str = Field(alias="protection_url")
    pattern: str = Field(alias="pattern")
    required_approving_review_count: int = Field(alias="required_approving_review_count")
    
    class Config:
        populate_by_name = True


class StatusCheckPolicy(BaseModel):
    """StatusCheckPolicy schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    strict: bool = Field(alias="strict")
    contexts: List[str] = Field(alias="contexts")
    checks: List[Dict[str, Any]] = Field(alias="checks")
    contexts_url: str = Field(alias="contexts_url")
    
    class Config:
        populate_by_name = True


class ProtectedBranch(BaseModel):
    """ProtectedBranch schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    required_status_checks: StatusCheckPolicy = Field(alias="required_status_checks")  # Status Check Policy
    required_pull_request_reviews: Dict[str, Any] = Field(alias="required_pull_request_reviews")
    required_signatures: Dict[str, Any] = Field(alias="required_signatures")
    enforce_admins: Dict[str, Any] = Field(alias="enforce_admins")
    required_linear_history: Dict[str, Any] = Field(alias="required_linear_history")
    allow_force_pushes: Dict[str, Any] = Field(alias="allow_force_pushes")
    allow_deletions: Dict[str, Any] = Field(alias="allow_deletions")
    restrictions: BranchRestrictionPolicy = Field(alias="restrictions")  # Branch Restriction Policy
    required_conversation_resolution: Dict[str, Any] = Field(alias="required_conversation_resolution")
    block_creations: Dict[str, Any] = Field(alias="block_creations")
    lock_branch: Dict[str, Any] = Field(alias="lock_branch")  # Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.
    allow_fork_syncing: Dict[str, Any] = Field(alias="allow_fork_syncing")  # Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.
    
    class Config:
        populate_by_name = True


class DeploymentSimple(BaseModel):
    """DeploymentSimple schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")  # Unique identifier of the deployment
    node_id: str = Field(alias="node_id")
    task: str = Field(alias="task")  # Parameter to specify a task to execute
    original_environment: str = Field(alias="original_environment")
    environment: str = Field(alias="environment")  # Name for the target deployment environment.
    description: str = Field(alias="description")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    statuses_url: str = Field(alias="statuses_url")
    repository_url: str = Field(alias="repository_url")
    transient_environment: bool = Field(alias="transient_environment")  # Specifies if the given environment is will no longer exist at some point in the future. Default: false.
    production_environment: bool = Field(alias="production_environment")  # Specifies if the given environment is one that end-users directly interact with. Default: false.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    
    class Config:
        populate_by_name = True


class CheckRun(BaseModel):
    """CheckRun schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The id of the check.
    head_sha: str = Field(alias="head_sha")  # The SHA of the commit that is being checked.
    node_id: str = Field(alias="node_id")
    external_id: str = Field(alias="external_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    details_url: str = Field(alias="details_url")
    status: str = Field(alias="status")  # The phase of the lifecycle that the check is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check runs.
    conclusion: str = Field(alias="conclusion")
    started_at: str = Field(alias="started_at")
    completed_at: str = Field(alias="completed_at")
    output: Dict[str, Any] = Field(alias="output")
    name: str = Field(alias="name")  # The name of the check.
    check_suite: Dict[str, Any] = Field(alias="check_suite")
    app: NullableIntegration = Field(alias="app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    pull_requests: List[PullRequestMinimal] = Field(alias="pull_requests")  # Pull requests that are open with a `head_sha` or `head_branch` that matches the check. The returned pull requests do not necessarily indicate pull requests that triggered the check.
    deployment: DeploymentSimple = Field(alias="deployment")  # A deployment created as the result of an Actions check run from a workflow that references an environment
    
    class Config:
        populate_by_name = True


class CheckAnnotation(BaseModel):
    """CheckAnnotation schema from the OpenAPI specification."""
    path: str = Field(alias="path")
    start_line: int = Field(alias="start_line")
    end_line: int = Field(alias="end_line")
    start_column: int = Field(alias="start_column")
    end_column: int = Field(alias="end_column")
    annotation_level: str = Field(alias="annotation_level")
    title: str = Field(alias="title")
    message: str = Field(alias="message")
    raw_details: str = Field(alias="raw_details")
    blob_href: str = Field(alias="blob_href")
    
    class Config:
        populate_by_name = True


class SimpleCommit(BaseModel):
    """SimpleCommit schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # SHA for the commit
    tree_id: str = Field(alias="tree_id")  # SHA for the commit\'s tree
    message: str = Field(alias="message")  # Message describing the purpose of the commit
    timestamp: str = Field(alias="timestamp")  # Timestamp of the commit
    author: Dict[str, Any] = Field(alias="author")  # Information about the Git author
    committer: Dict[str, Any] = Field(alias="committer")  # Information about the Git committer
    
    class Config:
        populate_by_name = True


class CheckSuite(BaseModel):
    """CheckSuite schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    head_branch: str = Field(alias="head_branch")
    head_sha: str = Field(alias="head_sha")  # The SHA of the head commit that is being checked.
    status: str = Field(alias="status")  # The phase of the lifecycle that the check suite is currently in. Statuses of waiting, requested, and pending are reserved for GitHub Actions check suites.
    conclusion: str = Field(alias="conclusion")
    url: str = Field(alias="url")
    before: str = Field(alias="before")
    after: str = Field(alias="after")
    pull_requests: List[PullRequestMinimal] = Field(alias="pull_requests")
    app: NullableIntegration = Field(alias="app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    head_commit: SimpleCommit = Field(alias="head_commit")  # A commit.
    latest_check_runs_count: int = Field(alias="latest_check_runs_count")
    check_runs_url: str = Field(alias="check_runs_url")
    rerequestable: bool = Field(alias="rerequestable")
    runs_rerequestable: bool = Field(alias="runs_rerequestable")
    
    class Config:
        populate_by_name = True


class CheckSuitePreference(BaseModel):
    """CheckSuitePreference schema from the OpenAPI specification."""
    preferences: Dict[str, Any] = Field(alias="preferences")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    
    class Config:
        populate_by_name = True


class CodeScanningAlertItems(BaseModel):
    """CodeScanningAlertItems schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    instances_url: str = Field(alias="instances_url")  # The REST API URL for fetching the list of instances for an alert.
    state: str = Field(alias="state")  # State of a code scanning alert.
    fixed_at: str = Field(alias="fixed_at")  # The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_by: NullableSimpleUser = Field(alias="dismissed_by")  # A GitHub user.
    dismissed_at: str = Field(alias="dismissed_at")  # The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_reason: str = Field(alias="dismissed_reason")  # **Required when the state is dismissed.** The reason for dismissing or closing the alert.
    dismissed_comment: str = Field(alias="dismissed_comment")  # The dismissal comment associated with the dismissal of the alert.
    rule: CodeScanningAlertRuleSummary = Field(alias="rule")
    tool: CodeScanningAnalysisTool = Field(alias="tool")
    most_recent_instance: CodeScanningAlertInstance = Field(alias="most_recent_instance")
    dismissal_approved_by: NullableSimpleUser = Field(alias="dismissal_approved_by")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class CodeScanningAlertRule(BaseModel):
    """CodeScanningAlertRule schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # A unique identifier for the rule used to detect the alert.
    name: str = Field(alias="name")  # The name of the rule used to detect the alert.
    severity: str = Field(alias="severity")  # The severity of the alert.
    security_severity_level: str = Field(alias="security_severity_level")  # The security severity of the alert.
    description: str = Field(alias="description")  # A short description of the rule used to detect the alert.
    full_description: str = Field(alias="full_description")  # A description of the rule used to detect the alert.
    tags: List[str] = Field(alias="tags")  # A set of tags applicable for the rule.
    help: str = Field(alias="help")  # Detailed documentation for the rule as GitHub Flavored Markdown.
    help_uri: str = Field(alias="help_uri")  # A link to the documentation for the rule used to detect the alert.
    
    class Config:
        populate_by_name = True


class CodeScanningAlert(BaseModel):
    """CodeScanningAlert schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    instances_url: str = Field(alias="instances_url")  # The REST API URL for fetching the list of instances for an alert.
    state: str = Field(alias="state")  # State of a code scanning alert.
    fixed_at: str = Field(alias="fixed_at")  # The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_by: NullableSimpleUser = Field(alias="dismissed_by")  # A GitHub user.
    dismissed_at: str = Field(alias="dismissed_at")  # The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_reason: str = Field(alias="dismissed_reason")  # **Required when the state is dismissed.** The reason for dismissing or closing the alert.
    dismissed_comment: str = Field(alias="dismissed_comment")  # The dismissal comment associated with the dismissal of the alert.
    rule: CodeScanningAlertRule = Field(alias="rule")
    tool: CodeScanningAnalysisTool = Field(alias="tool")
    most_recent_instance: CodeScanningAlertInstance = Field(alias="most_recent_instance")
    dismissal_approved_by: NullableSimpleUser = Field(alias="dismissal_approved_by")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class CodeScanningAutofix(BaseModel):
    """CodeScanningAutofix schema from the OpenAPI specification."""
    status: str = Field(alias="status")  # The status of an autofix.
    description: str = Field(alias="description")  # The description of an autofix.
    started_at: str = Field(alias="started_at")  # The start time of an autofix in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    
    class Config:
        populate_by_name = True


class CodeScanningAutofixCommits(BaseModel):
    """CodeScanningAutofixCommits schema from the OpenAPI specification."""
    target_ref: str = Field(alias="target_ref")  # The Git reference of target branch for the commit. Branch needs to already exist.  For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    message: str = Field(alias="message")  # Commit message to be used.
    
    class Config:
        populate_by_name = True


class CodeScanningAutofixCommitsResponse(BaseModel):
    """CodeScanningAutofixCommitsResponse schema from the OpenAPI specification."""
    target_ref: str = Field(alias="target_ref")  # The Git reference of target branch for the commit. For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    sha: str = Field(alias="sha")  # SHA of commit with autofix.
    
    class Config:
        populate_by_name = True


class CodeScanningAnalysis(BaseModel):
    """CodeScanningAnalysis schema from the OpenAPI specification."""
    ref: str = Field(alias="ref")  # The Git reference, formatted as `refs/pull/<number>/merge`, `refs/pull/<number>/head`,
`refs/heads/<branch name>` or simply `<branch name>`.
    commit_sha: str = Field(alias="commit_sha")  # The SHA of the commit to which the analysis you are uploading relates.
    analysis_key: str = Field(alias="analysis_key")  # Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name.
    environment: str = Field(alias="environment")  # Identifies the variable values associated with the environment in which this analysis was performed.
    category: str = Field(alias="category")  # Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code.
    error: str = Field(alias="error")
    created_at: str = Field(alias="created_at")  # The time that the analysis was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    results_count: int = Field(alias="results_count")  # The total number of results in the analysis.
    rules_count: int = Field(alias="rules_count")  # The total number of rules used in the analysis.
    id_field: int = Field(alias="id")  # Unique identifier for this analysis.
    url: str = Field(alias="url")  # The REST API URL of the analysis resource.
    sarif_id: str = Field(alias="sarif_id")  # An identifier for the upload.
    tool: CodeScanningAnalysisTool = Field(alias="tool")
    deletable: bool = Field(alias="deletable")
    warning: str = Field(alias="warning")  # Warning generated when processing the analysis
    
    class Config:
        populate_by_name = True


class CodeScanningAnalysisDeletion(BaseModel):
    """CodeScanningAnalysisDeletion schema from the OpenAPI specification."""
    next_analysis_url: str = Field(alias="next_analysis_url")  # Next deletable analysis in chain, without last analysis deletion confirmation
    confirm_delete_url: str = Field(alias="confirm_delete_url")  # Next deletable analysis in chain, with last analysis deletion confirmation
    
    class Config:
        populate_by_name = True


class CodeScanningCodeqlDatabase(BaseModel):
    """CodeScanningCodeqlDatabase schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the CodeQL database.
    name: str = Field(alias="name")  # The name of the CodeQL database.
    language: str = Field(alias="language")  # The language of the CodeQL database.
    uploader: SimpleUser = Field(alias="uploader")  # A GitHub user.
    content_type: str = Field(alias="content_type")  # The MIME type of the CodeQL database file.
    size: int = Field(alias="size")  # The size of the CodeQL database file in bytes.
    created_at: str = Field(alias="created_at")  # The date and time at which the CodeQL database was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the CodeQL database was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    url: str = Field(alias="url")  # The URL at which to download the CodeQL database. The `Accept` header must be set to the value of the `content_type` property.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the repository at the time the CodeQL database was created.
    
    class Config:
        populate_by_name = True


class CodeScanningVariantAnalysisRepository(BaseModel):
    """CodeScanningVariantAnalysisRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # A unique identifier of the repository.
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")  # The full, globally unique, name of the repository.
    private: bool = Field(alias="private")  # Whether the repository is private.
    stargazers_count: int = Field(alias="stargazers_count")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class CodeScanningVariantAnalysisSkippedRepoGroup(BaseModel):
    """CodeScanningVariantAnalysisSkippedRepoGroup schema from the OpenAPI specification."""
    repository_count: int = Field(alias="repository_count")  # The total number of repositories that were skipped for this reason.
    repositories: List[CodeScanningVariantAnalysisRepository] = Field(alias="repositories")  # A list of repositories that were skipped. This list may not include all repositories that were skipped. This is only available when the repository was found and the user has access to it.
    
    class Config:
        populate_by_name = True


class CodeScanningVariantAnalysis(BaseModel):
    """CodeScanningVariantAnalysis schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the variant analysis.
    controller_repo: SimpleRepository = Field(alias="controller_repo")  # A GitHub repository.
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    query_language: str = Field(alias="query_language")  # The language targeted by the CodeQL query
    query_pack_url: str = Field(alias="query_pack_url")  # The download url for the query pack.
    created_at: str = Field(alias="created_at")  # The date and time at which the variant analysis was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the variant analysis was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    completed_at: str = Field(alias="completed_at")  # The date and time at which the variant analysis was completed, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ. Will be null if the variant analysis has not yet completed or this information is not available.
    status: str = Field(alias="status")
    actions_workflow_run_id: int = Field(alias="actions_workflow_run_id")  # The GitHub Actions workflow run used to execute this variant analysis. This is only available if the workflow run has started.
    failure_reason: str = Field(alias="failure_reason")  # The reason for a failure of the variant analysis. This is only available if the variant analysis has failed.
    scanned_repositories: List[Dict[str, Any]] = Field(alias="scanned_repositories")
    skipped_repositories: Dict[str, Any] = Field(alias="skipped_repositories")  # Information about repositories that were skipped from processing. This information is only available to the user that initiated the variant analysis.
    
    class Config:
        populate_by_name = True


class CodeScanningVariantAnalysisRepoTask(BaseModel):
    """CodeScanningVariantAnalysisRepoTask schema from the OpenAPI specification."""
    repository: SimpleRepository = Field(alias="repository")  # A GitHub repository.
    analysis_status: str = Field(alias="analysis_status")  # The new status of the CodeQL variant analysis repository task.
    artifact_size_in_bytes: int = Field(alias="artifact_size_in_bytes")  # The size of the artifact. This is only available for successful analyses.
    result_count: int = Field(alias="result_count")  # The number of results in the case of a successful analysis. This is only available for successful analyses.
    failure_message: str = Field(alias="failure_message")  # The reason of the failure of this repo task. This is only available if the repository task has failed.
    database_commit_sha: str = Field(alias="database_commit_sha")  # The SHA of the commit the CodeQL database was built against. This is only available for successful analyses.
    source_location_prefix: str = Field(alias="source_location_prefix")  # The source location prefix to use. This is only available for successful analyses.
    artifact_url: str = Field(alias="artifact_url")  # The URL of the artifact. This is only available for successful analyses.
    
    class Config:
        populate_by_name = True


class CodeScanningDefaultSetup(BaseModel):
    """CodeScanningDefaultSetup schema from the OpenAPI specification."""
    state: str = Field(alias="state")  # Code scanning default setup has been configured or not.
    languages: List[str] = Field(alias="languages")  # Languages to be analyzed.
    runner_type: str = Field(alias="runner_type")  # Runner type to be used.
    runner_label: str = Field(alias="runner_label")  # Runner label to be used if the runner type is labeled.
    query_suite: str = Field(alias="query_suite")  # CodeQL query suite to be used.
    threat_model: str = Field(alias="threat_model")  # Threat model to be used for code scanning analysis. Use `remote` to analyze only network sources and `remote_and_local` to include local sources like filesystem access, command-line arguments, database reads, environment variable and standard input.
    updated_at: str = Field(alias="updated_at")  # Timestamp of latest configuration update.
    schedule: str = Field(alias="schedule")  # The frequency of the periodic analysis.
    
    class Config:
        populate_by_name = True


class CodeScanningDefaultSetupUpdate(BaseModel):
    """CodeScanningDefaultSetupUpdate schema from the OpenAPI specification."""
    state: str = Field(alias="state")  # The desired state of code scanning default setup.
    runner_type: str = Field(alias="runner_type")  # Runner type to be used.
    runner_label: str = Field(alias="runner_label")  # Runner label to be used if the runner type is labeled.
    query_suite: str = Field(alias="query_suite")  # CodeQL query suite to be used.
    threat_model: str = Field(alias="threat_model")  # Threat model to be used for code scanning analysis. Use `remote` to analyze only network sources and `remote_and_local` to include local sources like filesystem access, command-line arguments, database reads, environment variable and standard input.
    languages: List[str] = Field(alias="languages")  # CodeQL languages to be analyzed.
    
    class Config:
        populate_by_name = True


class CodeScanningDefaultSetupUpdateResponse(BaseModel):
    """CodeScanningDefaultSetupUpdateResponse schema from the OpenAPI specification."""
    run_id: int = Field(alias="run_id")  # ID of the corresponding run.
    run_url: str = Field(alias="run_url")  # URL of the corresponding run.
    
    class Config:
        populate_by_name = True


class CodeScanningSarifsReceipt(BaseModel):
    """CodeScanningSarifsReceipt schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # An identifier for the upload.
    url: str = Field(alias="url")  # The REST API URL for checking the status of the upload.
    
    class Config:
        populate_by_name = True


class CodeScanningSarifsStatus(BaseModel):
    """CodeScanningSarifsStatus schema from the OpenAPI specification."""
    processing_status: str = Field(alias="processing_status")  # `pending` files have not yet been processed, while `complete` means results from the SARIF have been stored. `failed` files have either not been processed at all, or could only be partially processed.
    analyses_url: str = Field(alias="analyses_url")  # The REST API URL for getting the analyses associated with the upload.
    errors: List[str] = Field(alias="errors")  # Any errors that ocurred during processing of the delivery.
    
    class Config:
        populate_by_name = True


class CodeSecurityConfigurationForRepository(BaseModel):
    """CodeSecurityConfigurationForRepository schema from the OpenAPI specification."""
    status: str = Field(alias="status")  # The attachment status of the code security configuration on the repository.
    configuration: CodeSecurityConfiguration = Field(alias="configuration")  # A code security configuration
    
    class Config:
        populate_by_name = True


class CodeownersErrors(BaseModel):
    """CodeownersErrors schema from the OpenAPI specification."""
    errors: List[Dict[str, Any]] = Field(alias="errors")
    
    class Config:
        populate_by_name = True


class CodespaceMachine(BaseModel):
    """CodespaceMachine schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the machine.
    display_name: str = Field(alias="display_name")  # The display name of the machine includes cores, memory, and storage.
    operating_system: str = Field(alias="operating_system")  # The operating system of the machine.
    storage_in_bytes: int = Field(alias="storage_in_bytes")  # How much storage is available to the codespace.
    memory_in_bytes: int = Field(alias="memory_in_bytes")  # How much memory is available to the codespace.
    cpus: int = Field(alias="cpus")  # How many cores are available to the codespace.
    prebuild_availability: str = Field(alias="prebuild_availability")  # Whether a prebuild is currently available when creating a codespace for this machine and repository. If a branch was not specified as a ref, the default branch will be assumed. Value will be \"null\" if prebuilds are not supported or prebuild availability could not be determined. Value will be \"none\" if no prebuild is available. Latest values \"ready\" and \"in_progress\" indicate the prebuild availability status.
    
    class Config:
        populate_by_name = True


class CodespacesPermissionsCheckForDevcontainer(BaseModel):
    """CodespacesPermissionsCheckForDevcontainer schema from the OpenAPI specification."""
    accepted: bool = Field(alias="accepted")  # Whether the user has accepted the permissions defined by the devcontainer config
    
    class Config:
        populate_by_name = True


class RepoCodespacesSecret(BaseModel):
    """RepoCodespacesSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class Collaborator(BaseModel):
    """Collaborator schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    email: str = Field(alias="email")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    permissions: Dict[str, Any] = Field(alias="permissions")
    role_name: str = Field(alias="role_name")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class RepositoryInvitation(BaseModel):
    """RepositoryInvitation schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository invitation.
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    invitee: NullableSimpleUser = Field(alias="invitee")  # A GitHub user.
    inviter: NullableSimpleUser = Field(alias="inviter")  # A GitHub user.
    permissions: str = Field(alias="permissions")  # The permission associated with the invitation.
    created_at: str = Field(alias="created_at")
    expired: bool = Field(alias="expired")  # Whether or not the invitation has expired
    url: str = Field(alias="url")  # URL for the repository invitation
    html_url: str = Field(alias="html_url")
    node_id: str = Field(alias="node_id")
    
    class Config:
        populate_by_name = True


class NullableCollaborator(BaseModel):
    """NullableCollaborator schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    email: str = Field(alias="email")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    permissions: Dict[str, Any] = Field(alias="permissions")
    role_name: str = Field(alias="role_name")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class RepositoryCollaboratorPermission(BaseModel):
    """RepositoryCollaboratorPermission schema from the OpenAPI specification."""
    permission: str = Field(alias="permission")
    role_name: str = Field(alias="role_name")
    user: NullableCollaborator = Field(alias="user")  # Collaborator
    
    class Config:
        populate_by_name = True


class CommitComment(BaseModel):
    """CommitComment schema from the OpenAPI specification."""
    html_url: str = Field(alias="html_url")
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    body: str = Field(alias="body")
    path: str = Field(alias="path")
    position: int = Field(alias="position")
    line: int = Field(alias="line")
    commit_id: str = Field(alias="commit_id")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class BranchShort(BaseModel):
    """BranchShort schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    commit: Dict[str, Any] = Field(alias="commit")
    protected: bool = Field(alias="protected")
    
    class Config:
        populate_by_name = True


class Link(BaseModel):
    """Link schema from the OpenAPI specification."""
    href: str = Field(alias="href")
    
    class Config:
        populate_by_name = True


class AutoMerge(BaseModel):
    """AutoMerge schema from the OpenAPI specification."""
    enabled_by: SimpleUser = Field(alias="enabled_by")  # A GitHub user.
    merge_method: str = Field(alias="merge_method")  # The merge method to use.
    commit_title: str = Field(alias="commit_title")  # Title for the merge commit message.
    commit_message: str = Field(alias="commit_message")  # Commit message for the merge commit.
    
    class Config:
        populate_by_name = True


class PullRequestSimple(BaseModel):
    """PullRequestSimple schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    diff_url: str = Field(alias="diff_url")
    patch_url: str = Field(alias="patch_url")
    issue_url: str = Field(alias="issue_url")
    commits_url: str = Field(alias="commits_url")
    review_comments_url: str = Field(alias="review_comments_url")
    review_comment_url: str = Field(alias="review_comment_url")
    comments_url: str = Field(alias="comments_url")
    statuses_url: str = Field(alias="statuses_url")
    number: int = Field(alias="number")
    state: str = Field(alias="state")
    locked: bool = Field(alias="locked")
    title: str = Field(alias="title")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    active_lock_reason: str = Field(alias="active_lock_reason")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    merged_at: str = Field(alias="merged_at")
    merge_commit_sha: str = Field(alias="merge_commit_sha")
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assignees: List[SimpleUser] = Field(alias="assignees")
    requested_reviewers: List[SimpleUser] = Field(alias="requested_reviewers")
    requested_teams: List[Team] = Field(alias="requested_teams")
    head: Dict[str, Any] = Field(alias="head")
    base: Dict[str, Any] = Field(alias="base")
    links: Dict[str, Any] = Field(alias="_links")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    auto_merge: AutoMerge = Field(alias="auto_merge")  # The status of auto merging a pull request.
    draft: bool = Field(alias="draft")  # Indicates whether or not the pull request is a draft.
    
    class Config:
        populate_by_name = True


class SimpleCommitStatus(BaseModel):
    """SimpleCommitStatus schema from the OpenAPI specification."""
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    state: str = Field(alias="state")
    context: str = Field(alias="context")
    target_url: str = Field(alias="target_url")
    required: bool = Field(alias="required")
    avatar_url: str = Field(alias="avatar_url")
    url: str = Field(alias="url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class CombinedCommitStatus(BaseModel):
    """CombinedCommitStatus schema from the OpenAPI specification."""
    state: str = Field(alias="state")
    statuses: List[SimpleCommitStatus] = Field(alias="statuses")
    sha: str = Field(alias="sha")
    total_count: int = Field(alias="total_count")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    commit_url: str = Field(alias="commit_url")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class Status(BaseModel):
    """Status schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    avatar_url: str = Field(alias="avatar_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    state: str = Field(alias="state")
    description: str = Field(alias="description")
    target_url: str = Field(alias="target_url")
    context: str = Field(alias="context")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class NullableCodeOfConductSimple(BaseModel):
    """NullableCodeOfConductSimple schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    key: str = Field(alias="key")
    name: str = Field(alias="name")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class NullableCommunityHealthFile(BaseModel):
    """NullableCommunityHealthFile schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class CommunityProfile(BaseModel):
    """CommunityProfile schema from the OpenAPI specification."""
    health_percentage: int = Field(alias="health_percentage")
    description: str = Field(alias="description")
    documentation: str = Field(alias="documentation")
    files: Dict[str, Any] = Field(alias="files")
    updated_at: str = Field(alias="updated_at")
    content_reports_enabled: bool = Field(alias="content_reports_enabled")
    
    class Config:
        populate_by_name = True


class CommitComparison(BaseModel):
    """CommitComparison schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    permalink_url: str = Field(alias="permalink_url")
    diff_url: str = Field(alias="diff_url")
    patch_url: str = Field(alias="patch_url")
    base_commit: Commit = Field(alias="base_commit")  # Commit
    merge_base_commit: Commit = Field(alias="merge_base_commit")  # Commit
    status: str = Field(alias="status")
    ahead_by: int = Field(alias="ahead_by")
    behind_by: int = Field(alias="behind_by")
    total_commits: int = Field(alias="total_commits")
    commits: List[Commit] = Field(alias="commits")
    files: List[DiffEntry] = Field(alias="files")
    
    class Config:
        populate_by_name = True


class ContentTree(BaseModel):
    """ContentTree schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    size: int = Field(alias="size")
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    content: str = Field(alias="content")
    url: str = Field(alias="url")
    git_url: str = Field(alias="git_url")
    html_url: str = Field(alias="html_url")
    download_url: str = Field(alias="download_url")
    entries: List[Dict[str, Any]] = Field(alias="entries")
    encoding: str = Field(alias="encoding")
    links: Dict[str, Any] = Field(alias="_links")
    
    class Config:
        populate_by_name = True


class ContentFile(BaseModel):
    """ContentFile schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    encoding: str = Field(alias="encoding")
    size: int = Field(alias="size")
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    content: str = Field(alias="content")
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")
    git_url: str = Field(alias="git_url")
    html_url: str = Field(alias="html_url")
    download_url: str = Field(alias="download_url")
    links: Dict[str, Any] = Field(alias="_links")
    target: str = Field(alias="target")
    submodule_git_url: str = Field(alias="submodule_git_url")
    
    class Config:
        populate_by_name = True


class ContentSymlink(BaseModel):
    """ContentSymlink schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    target: str = Field(alias="target")
    size: int = Field(alias="size")
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")
    git_url: str = Field(alias="git_url")
    html_url: str = Field(alias="html_url")
    download_url: str = Field(alias="download_url")
    links: Dict[str, Any] = Field(alias="_links")
    
    class Config:
        populate_by_name = True


class ContentSubmodule(BaseModel):
    """ContentSubmodule schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    submodule_git_url: str = Field(alias="submodule_git_url")
    size: int = Field(alias="size")
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")
    git_url: str = Field(alias="git_url")
    html_url: str = Field(alias="html_url")
    download_url: str = Field(alias="download_url")
    links: Dict[str, Any] = Field(alias="_links")
    
    class Config:
        populate_by_name = True


class FileCommit(BaseModel):
    """FileCommit schema from the OpenAPI specification."""
    content: Dict[str, Any] = Field(alias="content")
    commit: Dict[str, Any] = Field(alias="commit")
    
    class Config:
        populate_by_name = True


class RepositoryRuleViolationError(BaseModel):
    """RepositoryRuleViolationError schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    documentation_url: str = Field(alias="documentation_url")
    status: str = Field(alias="status")
    metadata: Dict[str, Any] = Field(alias="metadata")
    
    class Config:
        populate_by_name = True


class Contributor(BaseModel):
    """Contributor schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    contributions: int = Field(alias="contributions")
    email: str = Field(alias="email")
    name: str = Field(alias="name")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class DependabotAlert(BaseModel):
    """DependabotAlert schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    state: str = Field(alias="state")  # The state of the Dependabot alert.
    dependency: Dict[str, Any] = Field(alias="dependency")  # Details for the vulnerable dependency.
    security_advisory: DependabotAlertSecurityAdvisory = Field(alias="security_advisory")  # Details for the GitHub Security Advisory.
    security_vulnerability: DependabotAlertSecurityVulnerability = Field(alias="security_vulnerability")  # Details pertaining to one vulnerable version range for the advisory.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_at: str = Field(alias="dismissed_at")  # The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    dismissed_by: NullableSimpleUser = Field(alias="dismissed_by")  # A GitHub user.
    dismissed_reason: str = Field(alias="dismissed_reason")  # The reason that the alert was dismissed.
    dismissed_comment: str = Field(alias="dismissed_comment")  # An optional comment associated with the alert\'s dismissal.
    fixed_at: str = Field(alias="fixed_at")  # The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    auto_dismissed_at: str = Field(alias="auto_dismissed_at")  # The time that the alert was auto-dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    
    class Config:
        populate_by_name = True


class DependabotSecret(BaseModel):
    """DependabotSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class DependencyGraphSpdxSbom(BaseModel):
    """DependencyGraphSpdxSbom schema from the OpenAPI specification."""
    sbom: Dict[str, Any] = Field(alias="sbom")
    
    class Config:
        populate_by_name = True


class Metadata(BaseModel):
    """Metadata schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class Dependency(BaseModel):
    """Dependency schema from the OpenAPI specification."""
    package_url: str = Field(alias="package_url")  # Package-url (PURL) of dependency. See https://github.com/package-url/purl-spec for more details.
    metadata: Metadata = Field(alias="metadata")  # User-defined metadata to store domain-specific information limited to 8 keys with scalar values.
    relationship: str = Field(alias="relationship")  # A notation of whether a dependency is requested directly by this manifest or is a dependency of another dependency.
    scope: str = Field(alias="scope")  # A notation of whether the dependency is required for the primary build artifact (runtime) or is only used for development. Future versions of this specification may allow for more granular scopes.
    dependencies: List[str] = Field(alias="dependencies")  # Array of package-url (PURLs) of direct child dependencies.
    
    class Config:
        populate_by_name = True


class Manifest(BaseModel):
    """Manifest schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the manifest.
    file: Dict[str, Any] = Field(alias="file")
    metadata: Metadata = Field(alias="metadata")  # User-defined metadata to store domain-specific information limited to 8 keys with scalar values.
    resolved: Dict[str, Any] = Field(alias="resolved")  # A collection of resolved package dependencies.
    
    class Config:
        populate_by_name = True


class Snapshot(BaseModel):
    """Snapshot schema from the OpenAPI specification."""
    version: int = Field(alias="version")  # The version of the repository snapshot submission.
    job: Dict[str, Any] = Field(alias="job")
    sha: str = Field(alias="sha")  # The commit SHA associated with this dependency snapshot. Maximum length: 40 characters.
    ref: str = Field(alias="ref")  # The repository branch that triggered this snapshot.
    detector: Dict[str, Any] = Field(alias="detector")  # A description of the detector used.
    metadata: Metadata = Field(alias="metadata")  # User-defined metadata to store domain-specific information limited to 8 keys with scalar values.
    manifests: Dict[str, Any] = Field(alias="manifests")  # A collection of package manifests, which are a collection of related dependencies declared in a file or representing a logical group of dependencies.
    scanned: str = Field(alias="scanned")  # The time at which the snapshot was scanned.
    
    class Config:
        populate_by_name = True


class DeploymentStatus(BaseModel):
    """DeploymentStatus schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    state: str = Field(alias="state")  # The state of the status.
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    description: str = Field(alias="description")  # A short description of the status.
    environment: str = Field(alias="environment")  # The environment of the deployment that the status is for.
    target_url: str = Field(alias="target_url")  # Closing down notice: the URL to associate with this status.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    deployment_url: str = Field(alias="deployment_url")
    repository_url: str = Field(alias="repository_url")
    environment_url: str = Field(alias="environment_url")  # The URL for accessing your environment.
    log_url: str = Field(alias="log_url")  # The URL to associate with this status.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    
    class Config:
        populate_by_name = True


class DeploymentBranchPolicySettings(BaseModel):
    """DeploymentBranchPolicySettings schema from the OpenAPI specification."""
    protected_branches: bool = Field(alias="protected_branches")  # Whether only branches with branch protection rules can deploy to this environment. If `protected_branches` is `true`, `custom_branch_policies` must be `false`; if `protected_branches` is `false`, `custom_branch_policies` must be `true`.
    custom_branch_policies: bool = Field(alias="custom_branch_policies")  # Whether only branches that match the specified name patterns can deploy to this environment.  If `custom_branch_policies` is `true`, `protected_branches` must be `false`; if `custom_branch_policies` is `false`, `protected_branches` must be `true`.
    
    class Config:
        populate_by_name = True


class Environment(BaseModel):
    """Environment schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The id of the environment.
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the environment.
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    created_at: str = Field(alias="created_at")  # The time that the environment was created, in ISO 8601 format.
    updated_at: str = Field(alias="updated_at")  # The time that the environment was last updated, in ISO 8601 format.
    protection_rules: List[Any] = Field(alias="protection_rules")  # Built-in deployment protection rules for the environment.
    deployment_branch_policy: DeploymentBranchPolicySettings = Field(alias="deployment_branch_policy")  # The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`.
    
    class Config:
        populate_by_name = True


class DeploymentBranchPolicy(BaseModel):
    """DeploymentBranchPolicy schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the branch or tag policy.
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name pattern that branches or tags must match in order to deploy to the environment.
    type_field: str = Field(alias="type")  # Whether this rule targets a branch or tag.
    
    class Config:
        populate_by_name = True


class DeploymentBranchPolicyNamePatternWithType(BaseModel):
    """DeploymentBranchPolicyNamePatternWithType schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name pattern that branches or tags must match in order to deploy to the environment.

Wildcard characters will not match `/`. For example, to match branches that begin with `release/` and contain an additional single slash, use `release/*/*`.
For more information about pattern matching syntax, see the [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).
    type_field: str = Field(alias="type")  # Whether this rule targets a branch or tag
    
    class Config:
        populate_by_name = True


class DeploymentBranchPolicyNamePattern(BaseModel):
    """DeploymentBranchPolicyNamePattern schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name pattern that branches must match in order to deploy to the environment.

Wildcard characters will not match `/`. For example, to match branches that begin with `release/` and contain an additional single slash, use `release/*/*`.
For more information about pattern matching syntax, see the [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).
    
    class Config:
        populate_by_name = True


class CustomDeploymentRuleApp(BaseModel):
    """CustomDeploymentRuleApp schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier of the deployment protection rule integration.
    slug: str = Field(alias="slug")  # The slugified name of the deployment protection rule integration.
    integration_url: str = Field(alias="integration_url")  # The URL for the endpoint to get details about the app.
    node_id: str = Field(alias="node_id")  # The node ID for the deployment protection rule integration.
    
    class Config:
        populate_by_name = True


class DeploymentProtectionRule(BaseModel):
    """DeploymentProtectionRule schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The unique identifier for the deployment protection rule.
    node_id: str = Field(alias="node_id")  # The node ID for the deployment protection rule.
    enabled: bool = Field(alias="enabled")  # Whether the deployment protection rule is enabled for the environment.
    app: CustomDeploymentRuleApp = Field(alias="app")  # A GitHub App that is providing a custom deployment protection rule.
    
    class Config:
        populate_by_name = True


class ShortBlob(BaseModel):
    """ShortBlob schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    sha: str = Field(alias="sha")
    
    class Config:
        populate_by_name = True


class Blob(BaseModel):
    """Blob schema from the OpenAPI specification."""
    content: str = Field(alias="content")
    encoding: str = Field(alias="encoding")
    url: str = Field(alias="url")
    sha: str = Field(alias="sha")
    size: int = Field(alias="size")
    node_id: str = Field(alias="node_id")
    highlighted_content: str = Field(alias="highlighted_content")
    
    class Config:
        populate_by_name = True


class GitCommit(BaseModel):
    """GitCommit schema from the OpenAPI specification."""
    sha: str = Field(alias="sha")  # SHA for the commit
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    author: Dict[str, Any] = Field(alias="author")  # Identifying information for the git-user
    committer: Dict[str, Any] = Field(alias="committer")  # Identifying information for the git-user
    message: str = Field(alias="message")  # Message describing the purpose of the commit
    tree: Dict[str, Any] = Field(alias="tree")
    parents: List[Dict[str, Any]] = Field(alias="parents")
    verification: Dict[str, Any] = Field(alias="verification")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class GitRef(BaseModel):
    """GitRef schema from the OpenAPI specification."""
    ref: str = Field(alias="ref")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    object_field: Dict[str, Any] = Field(alias="object")
    
    class Config:
        populate_by_name = True


class GitTag(BaseModel):
    """GitTag schema from the OpenAPI specification."""
    node_id: str = Field(alias="node_id")
    tag: str = Field(alias="tag")  # Name of the tag
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")  # URL for the tag
    message: str = Field(alias="message")  # Message describing the purpose of the tag
    tagger: Dict[str, Any] = Field(alias="tagger")
    object_field: Dict[str, Any] = Field(alias="object")
    verification: Verification = Field(alias="verification")
    
    class Config:
        populate_by_name = True


class GitTree(BaseModel):
    """GitTree schema from the OpenAPI specification."""
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")
    truncated: bool = Field(alias="truncated")
    tree: List[Dict[str, Any]] = Field(alias="tree")  # Objects specifying a tree structure
    
    class Config:
        populate_by_name = True


class HookResponse(BaseModel):
    """HookResponse schema from the OpenAPI specification."""
    code: int = Field(alias="code")
    status: str = Field(alias="status")
    message: str = Field(alias="message")
    
    class Config:
        populate_by_name = True


class Hook(BaseModel):
    """Hook schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")
    id_field: int = Field(alias="id")  # Unique identifier of the webhook.
    name: str = Field(alias="name")  # The name of a valid service, use \'web\' for a webhook.
    active: bool = Field(alias="active")  # Determines whether the hook is actually triggered on pushes.
    events: List[str] = Field(alias="events")  # Determines what events the hook is triggered for. Default: [\'push\'].
    config: WebhookConfig = Field(alias="config")  # Configuration object of the webhook
    updated_at: str = Field(alias="updated_at")
    created_at: str = Field(alias="created_at")
    url: str = Field(alias="url")
    test_url: str = Field(alias="test_url")
    ping_url: str = Field(alias="ping_url")
    deliveries_url: str = Field(alias="deliveries_url")
    last_response: HookResponse = Field(alias="last_response")
    
    class Config:
        populate_by_name = True


class Import(BaseModel):
    """Import schema from the OpenAPI specification."""
    vcs: str = Field(alias="vcs")
    use_lfs: bool = Field(alias="use_lfs")
    vcs_url: str = Field(alias="vcs_url")  # The URL of the originating repository.
    svc_root: str = Field(alias="svc_root")
    tfvc_project: str = Field(alias="tfvc_project")
    status: str = Field(alias="status")
    status_text: str = Field(alias="status_text")
    failed_step: str = Field(alias="failed_step")
    error_message: str = Field(alias="error_message")
    import_percent: int = Field(alias="import_percent")
    commit_count: int = Field(alias="commit_count")
    push_percent: int = Field(alias="push_percent")
    has_large_files: bool = Field(alias="has_large_files")
    large_files_size: int = Field(alias="large_files_size")
    large_files_count: int = Field(alias="large_files_count")
    project_choices: List[Dict[str, Any]] = Field(alias="project_choices")
    message: str = Field(alias="message")
    authors_count: int = Field(alias="authors_count")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    authors_url: str = Field(alias="authors_url")
    repository_url: str = Field(alias="repository_url")
    svn_root: str = Field(alias="svn_root")
    
    class Config:
        populate_by_name = True


class PorterAuthor(BaseModel):
    """PorterAuthor schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    remote_id: str = Field(alias="remote_id")
    remote_name: str = Field(alias="remote_name")
    email: str = Field(alias="email")
    name: str = Field(alias="name")
    url: str = Field(alias="url")
    import_url: str = Field(alias="import_url")
    
    class Config:
        populate_by_name = True


class PorterLargeFile(BaseModel):
    """PorterLargeFile schema from the OpenAPI specification."""
    ref_name: str = Field(alias="ref_name")
    path: str = Field(alias="path")
    oid: str = Field(alias="oid")
    size: int = Field(alias="size")
    
    class Config:
        populate_by_name = True


class NullableIssue(BaseModel):
    """NullableIssue schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the issue
    repository_url: str = Field(alias="repository_url")
    labels_url: str = Field(alias="labels_url")
    comments_url: str = Field(alias="comments_url")
    events_url: str = Field(alias="events_url")
    html_url: str = Field(alias="html_url")
    number: int = Field(alias="number")  # Number uniquely identifying the issue within its repository
    state: str = Field(alias="state")  # State of the issue; either \'open\' or \'closed\'
    state_reason: str = Field(alias="state_reason")  # The reason for the current state
    title: str = Field(alias="title")  # Title of the issue
    body: str = Field(alias="body")  # Contents of the issue
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    labels: List[Any] = Field(alias="labels")  # Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assignees: List[SimpleUser] = Field(alias="assignees")
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    locked: bool = Field(alias="locked")
    active_lock_reason: str = Field(alias="active_lock_reason")
    comments: int = Field(alias="comments")
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    closed_at: str = Field(alias="closed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    draft: bool = Field(alias="draft")
    closed_by: NullableSimpleUser = Field(alias="closed_by")  # A GitHub user.
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    timeline_url: str = Field(alias="timeline_url")
    type_field: IssueType = Field(alias="type")  # The type of issue.
    repository: Repository = Field(alias="repository")  # A repository on GitHub.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    reactions: ReactionRollup = Field(alias="reactions")
    sub_issues_summary: SubIssuesSummary = Field(alias="sub_issues_summary")
    
    class Config:
        populate_by_name = True


class IssueEventLabel(BaseModel):
    """IssueEventLabel schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    color: str = Field(alias="color")
    
    class Config:
        populate_by_name = True


class IssueEventDismissedReview(BaseModel):
    """IssueEventDismissedReview schema from the OpenAPI specification."""
    state: str = Field(alias="state")
    review_id: int = Field(alias="review_id")
    dismissal_message: str = Field(alias="dismissal_message")
    dismissal_commit_id: str = Field(alias="dismissal_commit_id")
    
    class Config:
        populate_by_name = True


class IssueEventMilestone(BaseModel):
    """IssueEventMilestone schema from the OpenAPI specification."""
    title: str = Field(alias="title")
    
    class Config:
        populate_by_name = True


class IssueEventProjectCard(BaseModel):
    """IssueEventProjectCard schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    project_url: str = Field(alias="project_url")
    project_id: int = Field(alias="project_id")
    column_name: str = Field(alias="column_name")
    previous_column_name: str = Field(alias="previous_column_name")
    
    class Config:
        populate_by_name = True


class IssueEventRename(BaseModel):
    """IssueEventRename schema from the OpenAPI specification."""
    from_field: str = Field(alias="from")
    to: str = Field(alias="to")
    
    class Config:
        populate_by_name = True


class IssueEvent(BaseModel):
    """IssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: NullableSimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    issue: NullableIssue = Field(alias="issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    label: IssueEventLabel = Field(alias="label")  # Issue Event Label
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assigner: NullableSimpleUser = Field(alias="assigner")  # A GitHub user.
    review_requester: NullableSimpleUser = Field(alias="review_requester")  # A GitHub user.
    requested_reviewer: NullableSimpleUser = Field(alias="requested_reviewer")  # A GitHub user.
    requested_team: Team = Field(alias="requested_team")  # Groups of organization members that gives permissions on specified repositories.
    dismissed_review: IssueEventDismissedReview = Field(alias="dismissed_review")
    milestone: IssueEventMilestone = Field(alias="milestone")  # Issue Event Milestone
    project_card: IssueEventProjectCard = Field(alias="project_card")  # Issue Event Project Card
    rename: IssueEventRename = Field(alias="rename")  # Issue Event Rename
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    lock_reason: str = Field(alias="lock_reason")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    
    class Config:
        populate_by_name = True


class LabeledIssueEvent(BaseModel):
    """LabeledIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    label: Dict[str, Any] = Field(alias="label")
    
    class Config:
        populate_by_name = True


class UnlabeledIssueEvent(BaseModel):
    """UnlabeledIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    label: Dict[str, Any] = Field(alias="label")
    
    class Config:
        populate_by_name = True


class AssignedIssueEvent(BaseModel):
    """AssignedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: Integration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    assignee: SimpleUser = Field(alias="assignee")  # A GitHub user.
    assigner: SimpleUser = Field(alias="assigner")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class UnassignedIssueEvent(BaseModel):
    """UnassignedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    assignee: SimpleUser = Field(alias="assignee")  # A GitHub user.
    assigner: SimpleUser = Field(alias="assigner")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class MilestonedIssueEvent(BaseModel):
    """MilestonedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    milestone: Dict[str, Any] = Field(alias="milestone")
    
    class Config:
        populate_by_name = True


class DemilestonedIssueEvent(BaseModel):
    """DemilestonedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    milestone: Dict[str, Any] = Field(alias="milestone")
    
    class Config:
        populate_by_name = True


class RenamedIssueEvent(BaseModel):
    """RenamedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    rename: Dict[str, Any] = Field(alias="rename")
    
    class Config:
        populate_by_name = True


class ReviewRequestedIssueEvent(BaseModel):
    """ReviewRequestedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    review_requester: SimpleUser = Field(alias="review_requester")  # A GitHub user.
    requested_team: Team = Field(alias="requested_team")  # Groups of organization members that gives permissions on specified repositories.
    requested_reviewer: SimpleUser = Field(alias="requested_reviewer")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class ReviewRequestRemovedIssueEvent(BaseModel):
    """ReviewRequestRemovedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    review_requester: SimpleUser = Field(alias="review_requester")  # A GitHub user.
    requested_team: Team = Field(alias="requested_team")  # Groups of organization members that gives permissions on specified repositories.
    requested_reviewer: SimpleUser = Field(alias="requested_reviewer")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class ReviewDismissedIssueEvent(BaseModel):
    """ReviewDismissedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    dismissed_review: Dict[str, Any] = Field(alias="dismissed_review")
    
    class Config:
        populate_by_name = True


class LockedIssueEvent(BaseModel):
    """LockedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    lock_reason: str = Field(alias="lock_reason")
    
    class Config:
        populate_by_name = True


class AddedToProjectIssueEvent(BaseModel):
    """AddedToProjectIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    project_card: Dict[str, Any] = Field(alias="project_card")
    
    class Config:
        populate_by_name = True


class MovedColumnInProjectIssueEvent(BaseModel):
    """MovedColumnInProjectIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    project_card: Dict[str, Any] = Field(alias="project_card")
    
    class Config:
        populate_by_name = True


class RemovedFromProjectIssueEvent(BaseModel):
    """RemovedFromProjectIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    project_card: Dict[str, Any] = Field(alias="project_card")
    
    class Config:
        populate_by_name = True


class ConvertedNoteToIssueIssueEvent(BaseModel):
    """ConvertedNoteToIssueIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: Integration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    project_card: Dict[str, Any] = Field(alias="project_card")
    
    class Config:
        populate_by_name = True


class Label(BaseModel):
    """Label schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier for the label.
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the label
    name: str = Field(alias="name")  # The name of the label.
    description: str = Field(alias="description")  # Optional description of the label, such as its purpose.
    color: str = Field(alias="color")  # 6-character hex code, without the leading #, identifying the color
    default: bool = Field(alias="default")  # Whether this label comes by default in a new repository.
    
    class Config:
        populate_by_name = True


class TimelineCommentEvent(BaseModel):
    """TimelineCommentEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    id_field: int = Field(alias="id")  # Unique identifier of the issue comment
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the issue comment
    body: str = Field(alias="body")  # Contents of the issue comment
    body_text: str = Field(alias="body_text")
    body_html: str = Field(alias="body_html")
    html_url: str = Field(alias="html_url")
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    issue_url: str = Field(alias="issue_url")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class TimelineCrossReferencedEvent(BaseModel):
    """TimelineCrossReferencedEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    source: Dict[str, Any] = Field(alias="source")
    
    class Config:
        populate_by_name = True


class TimelineCommittedEvent(BaseModel):
    """TimelineCommittedEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    sha: str = Field(alias="sha")  # SHA for the commit
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    author: Dict[str, Any] = Field(alias="author")  # Identifying information for the git-user
    committer: Dict[str, Any] = Field(alias="committer")  # Identifying information for the git-user
    message: str = Field(alias="message")  # Message describing the purpose of the commit
    tree: Dict[str, Any] = Field(alias="tree")
    parents: List[Dict[str, Any]] = Field(alias="parents")
    verification: Dict[str, Any] = Field(alias="verification")
    html_url: str = Field(alias="html_url")
    
    class Config:
        populate_by_name = True


class TimelineReviewedEvent(BaseModel):
    """TimelineReviewedEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    id_field: int = Field(alias="id")  # Unique identifier of the review
    node_id: str = Field(alias="node_id")
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")  # The text of the review.
    state: str = Field(alias="state")
    html_url: str = Field(alias="html_url")
    pull_request_url: str = Field(alias="pull_request_url")
    links: Dict[str, Any] = Field(alias="_links")
    submitted_at: str = Field(alias="submitted_at")
    commit_id: str = Field(alias="commit_id")  # A commit SHA for the review.
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    
    class Config:
        populate_by_name = True


class PullRequestReviewComment(BaseModel):
    """PullRequestReviewComment schema from the OpenAPI specification."""
    url: str = Field(alias="url")  # URL for the pull request review comment
    pull_request_review_id: int = Field(alias="pull_request_review_id")  # The ID of the pull request review to which the comment belongs.
    id_field: int = Field(alias="id")  # The ID of the pull request review comment.
    node_id: str = Field(alias="node_id")  # The node ID of the pull request review comment.
    diff_hunk: str = Field(alias="diff_hunk")  # The diff of the line that the comment refers to.
    path: str = Field(alias="path")  # The relative path of the file to which the comment applies.
    position: int = Field(alias="position")  # The line index in the diff to which the comment applies. This field is closing down; use `line` instead.
    original_position: int = Field(alias="original_position")  # The index of the original line in the diff to which the comment applies. This field is closing down; use `original_line` instead.
    commit_id: str = Field(alias="commit_id")  # The SHA of the commit to which the comment applies.
    original_commit_id: str = Field(alias="original_commit_id")  # The SHA of the original commit to which the comment applies.
    in_reply_to_id: int = Field(alias="in_reply_to_id")  # The comment ID to reply to.
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")  # The text of the comment.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    html_url: str = Field(alias="html_url")  # HTML URL for the pull request review comment.
    pull_request_url: str = Field(alias="pull_request_url")  # URL for the pull request that the review comment belongs to.
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    links: Dict[str, Any] = Field(alias="_links")
    start_line: int = Field(alias="start_line")  # The first line of the range for a multi-line comment.
    original_start_line: int = Field(alias="original_start_line")  # The first line of the range for a multi-line comment.
    start_side: str = Field(alias="start_side")  # The side of the first line of the range for a multi-line comment.
    line: int = Field(alias="line")  # The line of the blob to which the comment applies. The last line of the range for a multi-line comment
    original_line: int = Field(alias="original_line")  # The line of the blob to which the comment applies. The last line of the range for a multi-line comment
    side: str = Field(alias="side")  # The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment
    subject_type: str = Field(alias="subject_type")  # The level at which the comment is targeted, can be a diff line or a file.
    reactions: ReactionRollup = Field(alias="reactions")
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    
    class Config:
        populate_by_name = True


class TimelineLineCommentedEvent(BaseModel):
    """TimelineLineCommentedEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    node_id: str = Field(alias="node_id")
    comments: List[PullRequestReviewComment] = Field(alias="comments")
    
    class Config:
        populate_by_name = True


class TimelineCommitCommentedEvent(BaseModel):
    """TimelineCommitCommentedEvent schema from the OpenAPI specification."""
    event: str = Field(alias="event")
    node_id: str = Field(alias="node_id")
    commit_id: str = Field(alias="commit_id")
    comments: List[CommitComment] = Field(alias="comments")
    
    class Config:
        populate_by_name = True


class TimelineAssignedIssueEvent(BaseModel):
    """TimelineAssignedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    assignee: SimpleUser = Field(alias="assignee")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class TimelineUnassignedIssueEvent(BaseModel):
    """TimelineUnassignedIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    assignee: SimpleUser = Field(alias="assignee")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class StateChangeIssueEvent(BaseModel):
    """StateChangeIssueEvent schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    actor: SimpleUser = Field(alias="actor")  # A GitHub user.
    event: str = Field(alias="event")
    commit_id: str = Field(alias="commit_id")
    commit_url: str = Field(alias="commit_url")
    created_at: str = Field(alias="created_at")
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    state_reason: str = Field(alias="state_reason")
    
    class Config:
        populate_by_name = True


class TimelineIssueEvents(BaseModel):
    """TimelineIssueEvents schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class DeployKey(BaseModel):
    """DeployKey schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    key: str = Field(alias="key")
    url: str = Field(alias="url")
    title: str = Field(alias="title")
    verified: bool = Field(alias="verified")
    created_at: str = Field(alias="created_at")
    read_only: bool = Field(alias="read_only")
    added_by: str = Field(alias="added_by")
    last_used: str = Field(alias="last_used")
    enabled: bool = Field(alias="enabled")
    
    class Config:
        populate_by_name = True


class Language(BaseModel):
    """Language schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class LicenseContent(BaseModel):
    """LicenseContent schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    size: int = Field(alias="size")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    git_url: str = Field(alias="git_url")
    download_url: str = Field(alias="download_url")
    type_field: str = Field(alias="type")
    content: str = Field(alias="content")
    encoding: str = Field(alias="encoding")
    links: Dict[str, Any] = Field(alias="_links")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    
    class Config:
        populate_by_name = True


class MergedUpstream(BaseModel):
    """MergedUpstream schema from the OpenAPI specification."""
    message: str = Field(alias="message")
    merge_type: str = Field(alias="merge_type")
    base_branch: str = Field(alias="base_branch")
    
    class Config:
        populate_by_name = True


class Milestone(BaseModel):
    """Milestone schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    labels_url: str = Field(alias="labels_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The number of the milestone.
    state: str = Field(alias="state")  # The state of the milestone.
    title: str = Field(alias="title")  # The title of the milestone.
    description: str = Field(alias="description")
    creator: NullableSimpleUser = Field(alias="creator")  # A GitHub user.
    open_issues: int = Field(alias="open_issues")
    closed_issues: int = Field(alias="closed_issues")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    due_on: str = Field(alias="due_on")
    
    class Config:
        populate_by_name = True


class PagesSourceHash(BaseModel):
    """PagesSourceHash schema from the OpenAPI specification."""
    branch: str = Field(alias="branch")
    path: str = Field(alias="path")
    
    class Config:
        populate_by_name = True


class PagesHttpsCertificate(BaseModel):
    """PagesHttpsCertificate schema from the OpenAPI specification."""
    state: str = Field(alias="state")
    description: str = Field(alias="description")
    domains: List[str] = Field(alias="domains")  # Array of the domain set and its alternate name (if it is configured)
    expires_at: str = Field(alias="expires_at")
    
    class Config:
        populate_by_name = True


class Page(BaseModel):
    """Page schema from the OpenAPI specification."""
    url: str = Field(alias="url")  # The API address for accessing this Page resource.
    status: str = Field(alias="status")  # The status of the most recent build of the Page.
    cname: str = Field(alias="cname")  # The Pages site\'s custom domain
    protected_domain_state: str = Field(alias="protected_domain_state")  # The state if the domain is verified
    pending_domain_unverified_at: str = Field(alias="pending_domain_unverified_at")  # The timestamp when a pending domain becomes unverified.
    custom_404: bool = Field(alias="custom_404")  # Whether the Page has a custom 404 page.
    html_url: str = Field(alias="html_url")  # The web address the Page can be accessed from.
    build_type: str = Field(alias="build_type")  # The process in which the Page will be built.
    source: PagesSourceHash = Field(alias="source")
    public: bool = Field(alias="public")  # Whether the GitHub Pages site is publicly visible. If set to `true`, the site is accessible to anyone on the internet. If set to `false`, the site will only be accessible to users who have at least `read` access to the repository that published the site.
    https_certificate: PagesHttpsCertificate = Field(alias="https_certificate")
    https_enforced: bool = Field(alias="https_enforced")  # Whether https is enabled on the domain
    
    class Config:
        populate_by_name = True


class PageBuild(BaseModel):
    """PageBuild schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    status: str = Field(alias="status")
    error: Dict[str, Any] = Field(alias="error")
    pusher: NullableSimpleUser = Field(alias="pusher")  # A GitHub user.
    commit: str = Field(alias="commit")
    duration: int = Field(alias="duration")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class PageBuildStatus(BaseModel):
    """PageBuildStatus schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    status: str = Field(alias="status")
    
    class Config:
        populate_by_name = True


class PageDeployment(BaseModel):
    """PageDeployment schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")  # The ID of the GitHub Pages deployment. This is the Git SHA of the deployed commit.
    status_url: str = Field(alias="status_url")  # The URI to monitor GitHub Pages deployment status.
    page_url: str = Field(alias="page_url")  # The URI to the deployed GitHub Pages.
    preview_url: str = Field(alias="preview_url")  # The URI to the deployed GitHub Pages preview.
    
    class Config:
        populate_by_name = True


class PagesDeploymentStatus(BaseModel):
    """PagesDeploymentStatus schema from the OpenAPI specification."""
    status: str = Field(alias="status")  # The current status of the deployment.
    
    class Config:
        populate_by_name = True


class PagesHealthCheck(BaseModel):
    """PagesHealthCheck schema from the OpenAPI specification."""
    domain: Dict[str, Any] = Field(alias="domain")
    alt_domain: Dict[str, Any] = Field(alias="alt_domain")
    
    class Config:
        populate_by_name = True


class PullRequest(BaseModel):
    """PullRequest schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    diff_url: str = Field(alias="diff_url")
    patch_url: str = Field(alias="patch_url")
    issue_url: str = Field(alias="issue_url")
    commits_url: str = Field(alias="commits_url")
    review_comments_url: str = Field(alias="review_comments_url")
    review_comment_url: str = Field(alias="review_comment_url")
    comments_url: str = Field(alias="comments_url")
    statuses_url: str = Field(alias="statuses_url")
    number: int = Field(alias="number")  # Number uniquely identifying the pull request within its repository.
    state: str = Field(alias="state")  # State of this Pull Request. Either `open` or `closed`.
    locked: bool = Field(alias="locked")
    title: str = Field(alias="title")  # The title of the pull request.
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    active_lock_reason: str = Field(alias="active_lock_reason")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    merged_at: str = Field(alias="merged_at")
    merge_commit_sha: str = Field(alias="merge_commit_sha")
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assignees: List[SimpleUser] = Field(alias="assignees")
    requested_reviewers: List[SimpleUser] = Field(alias="requested_reviewers")
    requested_teams: List[TeamSimple] = Field(alias="requested_teams")
    head: Dict[str, Any] = Field(alias="head")
    base: Dict[str, Any] = Field(alias="base")
    links: Dict[str, Any] = Field(alias="_links")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    auto_merge: AutoMerge = Field(alias="auto_merge")  # The status of auto merging a pull request.
    draft: bool = Field(alias="draft")  # Indicates whether or not the pull request is a draft.
    merged: bool = Field(alias="merged")
    mergeable: bool = Field(alias="mergeable")
    rebaseable: bool = Field(alias="rebaseable")
    mergeable_state: str = Field(alias="mergeable_state")
    merged_by: NullableSimpleUser = Field(alias="merged_by")  # A GitHub user.
    comments: int = Field(alias="comments")
    review_comments: int = Field(alias="review_comments")
    maintainer_can_modify: bool = Field(alias="maintainer_can_modify")  # Indicates whether maintainers can modify the pull request.
    commits: int = Field(alias="commits")
    additions: int = Field(alias="additions")
    deletions: int = Field(alias="deletions")
    changed_files: int = Field(alias="changed_files")
    
    class Config:
        populate_by_name = True


class PullRequestMergeResult(BaseModel):
    """PullRequestMergeResult schema from the OpenAPI specification."""
    sha: str = Field(alias="sha")
    merged: bool = Field(alias="merged")
    message: str = Field(alias="message")
    
    class Config:
        populate_by_name = True


class PullRequestReviewRequest(BaseModel):
    """PullRequestReviewRequest schema from the OpenAPI specification."""
    users: List[SimpleUser] = Field(alias="users")
    teams: List[Team] = Field(alias="teams")
    
    class Config:
        populate_by_name = True


class PullRequestReview(BaseModel):
    """PullRequestReview schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the review
    node_id: str = Field(alias="node_id")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")  # The text of the review.
    state: str = Field(alias="state")
    html_url: str = Field(alias="html_url")
    pull_request_url: str = Field(alias="pull_request_url")
    links: Dict[str, Any] = Field(alias="_links")
    submitted_at: str = Field(alias="submitted_at")
    commit_id: str = Field(alias="commit_id")  # A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be `null`.
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    
    class Config:
        populate_by_name = True


class ReviewComment(BaseModel):
    """ReviewComment schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    pull_request_review_id: int = Field(alias="pull_request_review_id")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    diff_hunk: str = Field(alias="diff_hunk")
    path: str = Field(alias="path")
    position: int = Field(alias="position")
    original_position: int = Field(alias="original_position")
    commit_id: str = Field(alias="commit_id")
    original_commit_id: str = Field(alias="original_commit_id")
    in_reply_to_id: int = Field(alias="in_reply_to_id")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    html_url: str = Field(alias="html_url")
    pull_request_url: str = Field(alias="pull_request_url")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    links: Dict[str, Any] = Field(alias="_links")
    body_text: str = Field(alias="body_text")
    body_html: str = Field(alias="body_html")
    reactions: ReactionRollup = Field(alias="reactions")
    side: str = Field(alias="side")  # The side of the first line of the range for a multi-line comment.
    start_side: str = Field(alias="start_side")  # The side of the first line of the range for a multi-line comment.
    line: int = Field(alias="line")  # The line of the blob to which the comment applies. The last line of the range for a multi-line comment
    original_line: int = Field(alias="original_line")  # The original line of the blob to which the comment applies. The last line of the range for a multi-line comment
    start_line: int = Field(alias="start_line")  # The first line of the range for a multi-line comment.
    original_start_line: int = Field(alias="original_start_line")  # The original first line of the range for a multi-line comment.
    subject_type: str = Field(alias="subject_type")  # The level at which the comment is targeted, can be a diff line or a file.
    
    class Config:
        populate_by_name = True


class ReleaseAsset(BaseModel):
    """ReleaseAsset schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    browser_download_url: str = Field(alias="browser_download_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The file name of the asset.
    label: str = Field(alias="label")
    state: str = Field(alias="state")  # State of the release asset.
    content_type: str = Field(alias="content_type")
    size: int = Field(alias="size")
    digest: str = Field(alias="digest")
    download_count: int = Field(alias="download_count")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    uploader: NullableSimpleUser = Field(alias="uploader")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class Release(BaseModel):
    """Release schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    assets_url: str = Field(alias="assets_url")
    upload_url: str = Field(alias="upload_url")
    tarball_url: str = Field(alias="tarball_url")
    zipball_url: str = Field(alias="zipball_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    tag_name: str = Field(alias="tag_name")  # The name of the tag.
    target_commitish: str = Field(alias="target_commitish")  # Specifies the commitish value that determines where the Git tag is created from.
    name: str = Field(alias="name")
    body: str = Field(alias="body")
    draft: bool = Field(alias="draft")  # true to create a draft (unpublished) release, false to create a published one.
    prerelease: bool = Field(alias="prerelease")  # Whether to identify the release as a prerelease or a full release.
    created_at: str = Field(alias="created_at")
    published_at: str = Field(alias="published_at")
    author: SimpleUser = Field(alias="author")  # A GitHub user.
    assets: List[ReleaseAsset] = Field(alias="assets")
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    mentions_count: int = Field(alias="mentions_count")
    discussion_url: str = Field(alias="discussion_url")  # The URL of the release discussion.
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class ReleaseNotesContent(BaseModel):
    """ReleaseNotesContent schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The generated name of the release
    body: str = Field(alias="body")  # The generated body describing the contents of the release supporting markdown formatting
    
    class Config:
        populate_by_name = True


class RepositoryRuleRulesetInfo(BaseModel):
    """RepositoryRuleRulesetInfo schema from the OpenAPI specification."""
    ruleset_source_type: str = Field(alias="ruleset_source_type")  # The type of source for the ruleset that includes this rule.
    ruleset_source: str = Field(alias="ruleset_source")  # The name of the source of the ruleset that includes this rule.
    ruleset_id: int = Field(alias="ruleset_id")  # The ID of the ruleset that includes this rule.
    
    class Config:
        populate_by_name = True


class RepositoryRuleDetailed(BaseModel):
    """RepositoryRuleDetailed schema from the OpenAPI specification."""
    
    class Config:
        populate_by_name = True


class SecretScanningAlert(BaseModel):
    """SecretScanningAlert schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    locations_url: str = Field(alias="locations_url")  # The REST API URL of the code locations for this alert.
    state: str = Field(alias="state")  # Sets the state of the secret scanning alert. You must provide `resolution` when you set the state to `resolved`.
    resolution: str = Field(alias="resolution")  # **Required when the `state` is `resolved`.** The reason for resolving the alert.
    resolved_at: str = Field(alias="resolved_at")  # The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    resolved_by: NullableSimpleUser = Field(alias="resolved_by")  # A GitHub user.
    resolution_comment: str = Field(alias="resolution_comment")  # An optional comment to resolve an alert.
    secret_type: str = Field(alias="secret_type")  # The type of secret that secret scanning detected.
    secret_type_display_name: str = Field(alias="secret_type_display_name")  # User-friendly name for the detected secret, matching the `secret_type`.
For a list of built-in patterns, see \"[Supported secret scanning patterns](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).\"
    secret: str = Field(alias="secret")  # The secret that was detected.
    push_protection_bypassed: bool = Field(alias="push_protection_bypassed")  # Whether push protection was bypassed for the detected secret.
    push_protection_bypassed_by: NullableSimpleUser = Field(alias="push_protection_bypassed_by")  # A GitHub user.
    push_protection_bypassed_at: str = Field(alias="push_protection_bypassed_at")  # The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    push_protection_bypass_request_reviewer: NullableSimpleUser = Field(alias="push_protection_bypass_request_reviewer")  # A GitHub user.
    push_protection_bypass_request_reviewer_comment: str = Field(alias="push_protection_bypass_request_reviewer_comment")  # An optional comment when reviewing a push protection bypass.
    push_protection_bypass_request_comment: str = Field(alias="push_protection_bypass_request_comment")  # An optional comment when requesting a push protection bypass.
    push_protection_bypass_request_html_url: str = Field(alias="push_protection_bypass_request_html_url")  # The URL to a push protection bypass request.
    validity: str = Field(alias="validity")  # The token status as of the latest validity check.
    publicly_leaked: bool = Field(alias="publicly_leaked")  # Whether the detected secret was publicly leaked.
    multi_repo: bool = Field(alias="multi_repo")  # Whether the detected secret was found in multiple repositories under the same organization or enterprise.
    is_base64_encoded: bool = Field(alias="is_base64_encoded")  # A boolean value representing whether or not alert is base64 encoded
    first_location_detected: Any = Field(alias="first_location_detected")  # Details on the location where the token was initially detected. This can be a commit, wiki commit, issue, discussion, pull request.
    has_more_locations: bool = Field(alias="has_more_locations")  # A boolean value representing whether or not the token in the alert was detected in more than one location.
    
    class Config:
        populate_by_name = True


class SecretScanningLocation(BaseModel):
    """SecretScanningLocation schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")  # The location type. Because secrets may be found in different types of resources (ie. code, comments, issues, pull requests, discussions), this field identifies the type of resource where the secret was found.
    details: Any = Field(alias="details")
    
    class Config:
        populate_by_name = True


class SecretScanningPushProtectionBypass(BaseModel):
    """SecretScanningPushProtectionBypass schema from the OpenAPI specification."""
    reason: str = Field(alias="reason")  # The reason for bypassing push protection.
    expire_at: str = Field(alias="expire_at")  # The time that the bypass will expire in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    token_type: str = Field(alias="token_type")  # The token type this bypass is for.
    
    class Config:
        populate_by_name = True


class SecretScanningScan(BaseModel):
    """SecretScanningScan schema from the OpenAPI specification."""
    type_field: str = Field(alias="type")  # The type of scan
    status: str = Field(alias="status")  # The state of the scan. Either \"completed\", \"running\", or \"pending\"
    completed_at: str = Field(alias="completed_at")  # The time that the scan was completed. Empty if the scan is running
    started_at: str = Field(alias="started_at")  # The time that the scan was started. Empty if the scan is pending
    
    class Config:
        populate_by_name = True


class SecretScanningScanHistory(BaseModel):
    """SecretScanningScanHistory schema from the OpenAPI specification."""
    incremental_scans: List[SecretScanningScan] = Field(alias="incremental_scans")
    pattern_update_scans: List[SecretScanningScan] = Field(alias="pattern_update_scans")
    backfill_scans: List[SecretScanningScan] = Field(alias="backfill_scans")
    custom_pattern_backfill_scans: List[Any] = Field(alias="custom_pattern_backfill_scans")
    
    class Config:
        populate_by_name = True


class RepositoryAdvisoryCreate(BaseModel):
    """RepositoryAdvisoryCreate schema from the OpenAPI specification."""
    summary: str = Field(alias="summary")  # A short summary of the advisory.
    description: str = Field(alias="description")  # A detailed description of what the advisory impacts.
    cve_id: str = Field(alias="cve_id")  # The Common Vulnerabilities and Exposures (CVE) ID.
    vulnerabilities: List[Dict[str, Any]] = Field(alias="vulnerabilities")  # A product affected by the vulnerability detailed in a repository security advisory.
    cwe_ids: List[str] = Field(alias="cwe_ids")  # A list of Common Weakness Enumeration (CWE) IDs.
    credits: List[Dict[str, Any]] = Field(alias="credits")  # A list of users receiving credit for their participation in the security advisory.
    severity: str = Field(alias="severity")  # The severity of the advisory. You must choose between setting this field or `cvss_vector_string`.
    cvss_vector_string: str = Field(alias="cvss_vector_string")  # The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or `severity`.
    start_private_fork: bool = Field(alias="start_private_fork")  # Whether to create a temporary private fork of the repository to collaborate on a fix.
    
    class Config:
        populate_by_name = True


class PrivateVulnerabilityReportCreate(BaseModel):
    """PrivateVulnerabilityReportCreate schema from the OpenAPI specification."""
    summary: str = Field(alias="summary")  # A short summary of the advisory.
    description: str = Field(alias="description")  # A detailed description of what the advisory impacts.
    vulnerabilities: List[Dict[str, Any]] = Field(alias="vulnerabilities")  # An array of products affected by the vulnerability detailed in a repository security advisory.
    cwe_ids: List[str] = Field(alias="cwe_ids")  # A list of Common Weakness Enumeration (CWE) IDs.
    severity: str = Field(alias="severity")  # The severity of the advisory. You must choose between setting this field or `cvss_vector_string`.
    cvss_vector_string: str = Field(alias="cvss_vector_string")  # The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or `severity`.
    start_private_fork: bool = Field(alias="start_private_fork")  # Whether to create a temporary private fork of the repository to collaborate on a fix.
    
    class Config:
        populate_by_name = True


class RepositoryAdvisoryUpdate(BaseModel):
    """RepositoryAdvisoryUpdate schema from the OpenAPI specification."""
    summary: str = Field(alias="summary")  # A short summary of the advisory.
    description: str = Field(alias="description")  # A detailed description of what the advisory impacts.
    cve_id: str = Field(alias="cve_id")  # The Common Vulnerabilities and Exposures (CVE) ID.
    vulnerabilities: List[Dict[str, Any]] = Field(alias="vulnerabilities")  # A product affected by the vulnerability detailed in a repository security advisory.
    cwe_ids: List[str] = Field(alias="cwe_ids")  # A list of Common Weakness Enumeration (CWE) IDs.
    credits: List[Dict[str, Any]] = Field(alias="credits")  # A list of users receiving credit for their participation in the security advisory.
    severity: str = Field(alias="severity")  # The severity of the advisory. You must choose between setting this field or `cvss_vector_string`.
    cvss_vector_string: str = Field(alias="cvss_vector_string")  # The CVSS vector that calculates the severity of the advisory. You must choose between setting this field or `severity`.
    state: str = Field(alias="state")  # The state of the advisory.
    collaborating_users: List[str] = Field(alias="collaborating_users")  # A list of usernames who have been granted write access to the advisory.
    collaborating_teams: List[str] = Field(alias="collaborating_teams")  # A list of team slugs which have been granted write access to the advisory.
    
    class Config:
        populate_by_name = True


class Stargazer(BaseModel):
    """Stargazer schema from the OpenAPI specification."""
    starred_at: str = Field(alias="starred_at")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class CommitActivity(BaseModel):
    """CommitActivity schema from the OpenAPI specification."""
    days: List[int] = Field(alias="days")
    total: int = Field(alias="total")
    week: int = Field(alias="week")
    
    class Config:
        populate_by_name = True


class ContributorActivity(BaseModel):
    """ContributorActivity schema from the OpenAPI specification."""
    author: NullableSimpleUser = Field(alias="author")  # A GitHub user.
    total: int = Field(alias="total")
    weeks: List[Dict[str, Any]] = Field(alias="weeks")
    
    class Config:
        populate_by_name = True


class ParticipationStats(BaseModel):
    """ParticipationStats schema from the OpenAPI specification."""
    all: List[int] = Field(alias="all")
    owner: List[int] = Field(alias="owner")
    
    class Config:
        populate_by_name = True


class RepositorySubscription(BaseModel):
    """RepositorySubscription schema from the OpenAPI specification."""
    subscribed: bool = Field(alias="subscribed")  # Determines if notifications should be received from this repository.
    ignored: bool = Field(alias="ignored")  # Determines if all notifications should be blocked from this repository.
    reason: str = Field(alias="reason")
    created_at: str = Field(alias="created_at")
    url: str = Field(alias="url")
    repository_url: str = Field(alias="repository_url")
    
    class Config:
        populate_by_name = True


class Tag(BaseModel):
    """Tag schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    commit: Dict[str, Any] = Field(alias="commit")
    zipball_url: str = Field(alias="zipball_url")
    tarball_url: str = Field(alias="tarball_url")
    node_id: str = Field(alias="node_id")
    
    class Config:
        populate_by_name = True


class TagProtection(BaseModel):
    """TagProtection schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    enabled: bool = Field(alias="enabled")
    pattern: str = Field(alias="pattern")
    
    class Config:
        populate_by_name = True


class Topic(BaseModel):
    """Topic schema from the OpenAPI specification."""
    names: List[str] = Field(alias="names")
    
    class Config:
        populate_by_name = True


class Traffic(BaseModel):
    """Traffic schema from the OpenAPI specification."""
    timestamp: str = Field(alias="timestamp")
    uniques: int = Field(alias="uniques")
    count: int = Field(alias="count")
    
    class Config:
        populate_by_name = True


class CloneTraffic(BaseModel):
    """CloneTraffic schema from the OpenAPI specification."""
    count: int = Field(alias="count")
    uniques: int = Field(alias="uniques")
    clones: List[Traffic] = Field(alias="clones")
    
    class Config:
        populate_by_name = True


class ContentTraffic(BaseModel):
    """ContentTraffic schema from the OpenAPI specification."""
    path: str = Field(alias="path")
    title: str = Field(alias="title")
    count: int = Field(alias="count")
    uniques: int = Field(alias="uniques")
    
    class Config:
        populate_by_name = True


class ReferrerTraffic(BaseModel):
    """ReferrerTraffic schema from the OpenAPI specification."""
    referrer: str = Field(alias="referrer")
    count: int = Field(alias="count")
    uniques: int = Field(alias="uniques")
    
    class Config:
        populate_by_name = True


class ViewTraffic(BaseModel):
    """ViewTraffic schema from the OpenAPI specification."""
    count: int = Field(alias="count")
    uniques: int = Field(alias="uniques")
    views: List[Traffic] = Field(alias="views")
    
    class Config:
        populate_by_name = True


class CodeSearchResultItem(BaseModel):
    """CodeSearchResultItem schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    path: str = Field(alias="path")
    sha: str = Field(alias="sha")
    url: str = Field(alias="url")
    git_url: str = Field(alias="git_url")
    html_url: str = Field(alias="html_url")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    score: float = Field(alias="score")
    file_size: int = Field(alias="file_size")
    language: str = Field(alias="language")
    last_modified_at: str = Field(alias="last_modified_at")
    line_numbers: List[str] = Field(alias="line_numbers")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    
    class Config:
        populate_by_name = True


class CommitSearchResultItem(BaseModel):
    """CommitSearchResultItem schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    sha: str = Field(alias="sha")
    html_url: str = Field(alias="html_url")
    comments_url: str = Field(alias="comments_url")
    commit: Dict[str, Any] = Field(alias="commit")
    author: NullableSimpleUser = Field(alias="author")  # A GitHub user.
    committer: NullableGitUser = Field(alias="committer")  # Metaproperties for Git author/committer information.
    parents: List[Dict[str, Any]] = Field(alias="parents")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    score: float = Field(alias="score")
    node_id: str = Field(alias="node_id")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    
    class Config:
        populate_by_name = True


class IssueSearchResultItem(BaseModel):
    """IssueSearchResultItem schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    repository_url: str = Field(alias="repository_url")
    labels_url: str = Field(alias="labels_url")
    comments_url: str = Field(alias="comments_url")
    events_url: str = Field(alias="events_url")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    title: str = Field(alias="title")
    locked: bool = Field(alias="locked")
    active_lock_reason: str = Field(alias="active_lock_reason")
    assignees: List[SimpleUser] = Field(alias="assignees")
    user: NullableSimpleUser = Field(alias="user")  # A GitHub user.
    labels: List[Dict[str, Any]] = Field(alias="labels")
    sub_issues_summary: Dict[str, Any] = Field(alias="sub_issues_summary")
    state: str = Field(alias="state")
    state_reason: str = Field(alias="state_reason")
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    comments: int = Field(alias="comments")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    body: str = Field(alias="body")
    score: float = Field(alias="score")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    draft: bool = Field(alias="draft")
    repository: Repository = Field(alias="repository")  # A repository on GitHub.
    body_html: str = Field(alias="body_html")
    body_text: str = Field(alias="body_text")
    timeline_url: str = Field(alias="timeline_url")
    type_field: IssueType = Field(alias="type")  # The type of issue.
    performed_via_github_app: NullableIntegration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    reactions: ReactionRollup = Field(alias="reactions")
    
    class Config:
        populate_by_name = True


class LabelSearchResultItem(BaseModel):
    """LabelSearchResultItem schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    name: str = Field(alias="name")
    color: str = Field(alias="color")
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    score: float = Field(alias="score")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    
    class Config:
        populate_by_name = True


class RepoSearchResultItem(BaseModel):
    """RepoSearchResultItem schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")
    full_name: str = Field(alias="full_name")
    owner: NullableSimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    pushed_at: str = Field(alias="pushed_at")
    homepage: str = Field(alias="homepage")
    size: int = Field(alias="size")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    open_issues_count: int = Field(alias="open_issues_count")
    master_branch: str = Field(alias="master_branch")
    default_branch: str = Field(alias="default_branch")
    score: float = Field(alias="score")
    forks_url: str = Field(alias="forks_url")
    keys_url: str = Field(alias="keys_url")
    collaborators_url: str = Field(alias="collaborators_url")
    teams_url: str = Field(alias="teams_url")
    hooks_url: str = Field(alias="hooks_url")
    issue_events_url: str = Field(alias="issue_events_url")
    events_url: str = Field(alias="events_url")
    assignees_url: str = Field(alias="assignees_url")
    branches_url: str = Field(alias="branches_url")
    tags_url: str = Field(alias="tags_url")
    blobs_url: str = Field(alias="blobs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_refs_url: str = Field(alias="git_refs_url")
    trees_url: str = Field(alias="trees_url")
    statuses_url: str = Field(alias="statuses_url")
    languages_url: str = Field(alias="languages_url")
    stargazers_url: str = Field(alias="stargazers_url")
    contributors_url: str = Field(alias="contributors_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    commits_url: str = Field(alias="commits_url")
    git_commits_url: str = Field(alias="git_commits_url")
    comments_url: str = Field(alias="comments_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    contents_url: str = Field(alias="contents_url")
    compare_url: str = Field(alias="compare_url")
    merges_url: str = Field(alias="merges_url")
    archive_url: str = Field(alias="archive_url")
    downloads_url: str = Field(alias="downloads_url")
    issues_url: str = Field(alias="issues_url")
    pulls_url: str = Field(alias="pulls_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    labels_url: str = Field(alias="labels_url")
    releases_url: str = Field(alias="releases_url")
    deployments_url: str = Field(alias="deployments_url")
    git_url: str = Field(alias="git_url")
    ssh_url: str = Field(alias="ssh_url")
    clone_url: str = Field(alias="clone_url")
    svn_url: str = Field(alias="svn_url")
    forks: int = Field(alias="forks")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    topics: List[str] = Field(alias="topics")
    mirror_url: str = Field(alias="mirror_url")
    has_issues: bool = Field(alias="has_issues")
    has_projects: bool = Field(alias="has_projects")
    has_pages: bool = Field(alias="has_pages")
    has_wiki: bool = Field(alias="has_wiki")
    has_downloads: bool = Field(alias="has_downloads")
    has_discussions: bool = Field(alias="has_discussions")
    archived: bool = Field(alias="archived")
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    permissions: Dict[str, Any] = Field(alias="permissions")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_merge_commit: bool = Field(alias="allow_merge_commit")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")
    allow_auto_merge: bool = Field(alias="allow_auto_merge")
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")
    allow_forking: bool = Field(alias="allow_forking")
    is_template: bool = Field(alias="is_template")
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")
    
    class Config:
        populate_by_name = True


class TopicSearchResultItem(BaseModel):
    """TopicSearchResultItem schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    display_name: str = Field(alias="display_name")
    short_description: str = Field(alias="short_description")
    description: str = Field(alias="description")
    created_by: str = Field(alias="created_by")
    released: str = Field(alias="released")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    featured: bool = Field(alias="featured")
    curated: bool = Field(alias="curated")
    score: float = Field(alias="score")
    repository_count: int = Field(alias="repository_count")
    logo_url: str = Field(alias="logo_url")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    related: List[Dict[str, Any]] = Field(alias="related")
    aliases: List[Dict[str, Any]] = Field(alias="aliases")
    
    class Config:
        populate_by_name = True


class UserSearchResultItem(BaseModel):
    """UserSearchResultItem schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    score: float = Field(alias="score")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    events_url: str = Field(alias="events_url")
    public_repos: int = Field(alias="public_repos")
    public_gists: int = Field(alias="public_gists")
    followers: int = Field(alias="followers")
    following: int = Field(alias="following")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    name: str = Field(alias="name")
    bio: str = Field(alias="bio")
    email: str = Field(alias="email")
    location: str = Field(alias="location")
    site_admin: bool = Field(alias="site_admin")
    hireable: bool = Field(alias="hireable")
    text_matches: List[Dict[str, Any]] = Field(alias="text_matches")
    blog: str = Field(alias="blog")
    company: str = Field(alias="company")
    suspended_at: str = Field(alias="suspended_at")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class PrivateUser(BaseModel):
    """PrivateUser schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    user_view_type: str = Field(alias="user_view_type")
    node_id: str = Field(alias="node_id")
    avatar_url: str = Field(alias="avatar_url")
    gravatar_id: str = Field(alias="gravatar_id")
    url: str = Field(alias="url")
    html_url: str = Field(alias="html_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    organizations_url: str = Field(alias="organizations_url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    received_events_url: str = Field(alias="received_events_url")
    type_field: str = Field(alias="type")
    site_admin: bool = Field(alias="site_admin")
    name: str = Field(alias="name")
    company: str = Field(alias="company")
    blog: str = Field(alias="blog")
    location: str = Field(alias="location")
    email: str = Field(alias="email")
    notification_email: str = Field(alias="notification_email")
    hireable: bool = Field(alias="hireable")
    bio: str = Field(alias="bio")
    twitter_username: str = Field(alias="twitter_username")
    public_repos: int = Field(alias="public_repos")
    public_gists: int = Field(alias="public_gists")
    followers: int = Field(alias="followers")
    following: int = Field(alias="following")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    private_gists: int = Field(alias="private_gists")
    total_private_repos: int = Field(alias="total_private_repos")
    owned_private_repos: int = Field(alias="owned_private_repos")
    disk_usage: int = Field(alias="disk_usage")
    collaborators: int = Field(alias="collaborators")
    two_factor_authentication: bool = Field(alias="two_factor_authentication")
    plan: Dict[str, Any] = Field(alias="plan")
    business_plus: bool = Field(alias="business_plus")
    ldap_dn: str = Field(alias="ldap_dn")
    
    class Config:
        populate_by_name = True


class CodespacesSecret(BaseModel):
    """CodespacesSecret schema from the OpenAPI specification."""
    name: str = Field(alias="name")  # The name of the secret
    created_at: str = Field(alias="created_at")  # The date and time at which the secret was created, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    updated_at: str = Field(alias="updated_at")  # The date and time at which the secret was last updated, in ISO 8601 format\':\' YYYY-MM-DDTHH:MM:SSZ.
    visibility: str = Field(alias="visibility")  # The type of repositories in the organization that the secret is visible to
    selected_repositories_url: str = Field(alias="selected_repositories_url")  # The API URL at which the list of repositories this secret is visible to can be retrieved
    
    class Config:
        populate_by_name = True


class CodespacesUserPublicKey(BaseModel):
    """CodespacesUserPublicKey schema from the OpenAPI specification."""
    key_id: str = Field(alias="key_id")  # The identifier for the key.
    key: str = Field(alias="key")  # The Base64 encoded public key.
    
    class Config:
        populate_by_name = True


class CodespaceExportDetails(BaseModel):
    """CodespaceExportDetails schema from the OpenAPI specification."""
    state: str = Field(alias="state")  # State of the latest export
    completed_at: str = Field(alias="completed_at")  # Completion time of the last export operation
    branch: str = Field(alias="branch")  # Name of the exported branch
    sha: str = Field(alias="sha")  # Git commit SHA of the exported branch
    id_field: str = Field(alias="id")  # Id for the export details
    export_url: str = Field(alias="export_url")  # Url for fetching export details
    html_url: str = Field(alias="html_url")  # Web url for the exported branch
    
    class Config:
        populate_by_name = True


class CodespaceWithFullRepository(BaseModel):
    """CodespaceWithFullRepository schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")  # Automatically generated name of this codespace.
    display_name: str = Field(alias="display_name")  # Display name for this codespace.
    environment_id: str = Field(alias="environment_id")  # UUID identifying this codespace\'s environment.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    billable_owner: SimpleUser = Field(alias="billable_owner")  # A GitHub user.
    repository: FullRepository = Field(alias="repository")  # Full Repository
    machine: NullableCodespaceMachine = Field(alias="machine")  # A description of the machine powering a codespace.
    devcontainer_path: str = Field(alias="devcontainer_path")  # Path to devcontainer.json from repo root used to create Codespace.
    prebuild: bool = Field(alias="prebuild")  # Whether the codespace was created from a prebuild.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    last_used_at: str = Field(alias="last_used_at")  # Last known time this codespace was started.
    state: str = Field(alias="state")  # State of this codespace.
    url: str = Field(alias="url")  # API URL for this codespace.
    git_status: Dict[str, Any] = Field(alias="git_status")  # Details about the codespace\'s git repository.
    location: str = Field(alias="location")  # The initally assigned location of a new codespace.
    idle_timeout_minutes: int = Field(alias="idle_timeout_minutes")  # The number of minutes of inactivity after which this codespace will be automatically stopped.
    web_url: str = Field(alias="web_url")  # URL to access this codespace on the web.
    machines_url: str = Field(alias="machines_url")  # API URL to access available alternate machine types for this codespace.
    start_url: str = Field(alias="start_url")  # API URL to start this codespace.
    stop_url: str = Field(alias="stop_url")  # API URL to stop this codespace.
    publish_url: str = Field(alias="publish_url")  # API URL to publish this codespace to a new repository.
    pulls_url: str = Field(alias="pulls_url")  # API URL for the Pull Request associated with this codespace, if any.
    recent_folders: List[str] = Field(alias="recent_folders")
    runtime_constraints: Dict[str, Any] = Field(alias="runtime_constraints")
    pending_operation: bool = Field(alias="pending_operation")  # Whether or not a codespace has a pending async operation. This would mean that the codespace is temporarily unavailable. The only thing that you can do with a codespace in this state is delete it.
    pending_operation_disabled_reason: str = Field(alias="pending_operation_disabled_reason")  # Text to show user when codespace is disabled by a pending operation
    idle_timeout_notice: str = Field(alias="idle_timeout_notice")  # Text to show user when codespace idle timeout minutes has been overriden by an organization policy
    retention_period_minutes: int = Field(alias="retention_period_minutes")  # Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).
    retention_expires_at: str = Field(alias="retention_expires_at")  # When a codespace will be auto-deleted based on the \"retention_period_minutes\" and \"last_used_at\"
    
    class Config:
        populate_by_name = True


class Email(BaseModel):
    """Email schema from the OpenAPI specification."""
    email: str = Field(alias="email")
    primary: bool = Field(alias="primary")
    verified: bool = Field(alias="verified")
    visibility: str = Field(alias="visibility")
    
    class Config:
        populate_by_name = True


class GpgKey(BaseModel):
    """GpgKey schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    primary_key_id: int = Field(alias="primary_key_id")
    key_id: str = Field(alias="key_id")
    public_key: str = Field(alias="public_key")
    emails: List[Dict[str, Any]] = Field(alias="emails")
    subkeys: List[Dict[str, Any]] = Field(alias="subkeys")
    can_sign: bool = Field(alias="can_sign")
    can_encrypt_comms: bool = Field(alias="can_encrypt_comms")
    can_encrypt_storage: bool = Field(alias="can_encrypt_storage")
    can_certify: bool = Field(alias="can_certify")
    created_at: str = Field(alias="created_at")
    expires_at: str = Field(alias="expires_at")
    revoked: bool = Field(alias="revoked")
    raw_key: str = Field(alias="raw_key")
    
    class Config:
        populate_by_name = True


class Key(BaseModel):
    """Key schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    id_field: int = Field(alias="id")
    url: str = Field(alias="url")
    title: str = Field(alias="title")
    created_at: str = Field(alias="created_at")
    verified: bool = Field(alias="verified")
    read_only: bool = Field(alias="read_only")
    
    class Config:
        populate_by_name = True


class MarketplaceAccount(BaseModel):
    """MarketplaceAccount schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    type_field: str = Field(alias="type")
    node_id: str = Field(alias="node_id")
    login: str = Field(alias="login")
    email: str = Field(alias="email")
    organization_billing_email: str = Field(alias="organization_billing_email")
    
    class Config:
        populate_by_name = True


class UserMarketplacePurchase(BaseModel):
    """UserMarketplacePurchase schema from the OpenAPI specification."""
    billing_cycle: str = Field(alias="billing_cycle")
    next_billing_date: str = Field(alias="next_billing_date")
    unit_count: int = Field(alias="unit_count")
    on_free_trial: bool = Field(alias="on_free_trial")
    free_trial_ends_on: str = Field(alias="free_trial_ends_on")
    updated_at: str = Field(alias="updated_at")
    account: MarketplaceAccount = Field(alias="account")
    plan: MarketplaceListingPlan = Field(alias="plan")  # Marketplace Listing Plan
    
    class Config:
        populate_by_name = True


class SocialAccount(BaseModel):
    """SocialAccount schema from the OpenAPI specification."""
    provider: str = Field(alias="provider")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class SshSigningKey(BaseModel):
    """SshSigningKey schema from the OpenAPI specification."""
    key: str = Field(alias="key")
    id_field: int = Field(alias="id")
    title: str = Field(alias="title")
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class StarredRepository(BaseModel):
    """StarredRepository schema from the OpenAPI specification."""
    starred_at: str = Field(alias="starred_at")
    repo: Repository = Field(alias="repo")  # A repository on GitHub.
    
    class Config:
        populate_by_name = True


class Hovercard(BaseModel):
    """Hovercard schema from the OpenAPI specification."""
    contexts: List[Dict[str, Any]] = Field(alias="contexts")
    
    class Config:
        populate_by_name = True


class KeySimple(BaseModel):
    """KeySimple schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")
    key: str = Field(alias="key")
    created_at: str = Field(alias="created_at")
    
    class Config:
        populate_by_name = True


class BillingUsageReportUser(BaseModel):
    """BillingUsageReportUser schema from the OpenAPI specification."""
    usage_items: List[Dict[str, Any]] = Field(alias="usageItems")
    
    class Config:
        populate_by_name = True


class EnterpriseWebhooks(BaseModel):
    """EnterpriseWebhooks schema from the OpenAPI specification."""
    description: str = Field(alias="description")  # A short description of the enterprise.
    html_url: str = Field(alias="html_url")
    website_url: str = Field(alias="website_url")  # The enterprise\'s website URL.
    id_field: int = Field(alias="id")  # Unique identifier of the enterprise
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the enterprise.
    slug: str = Field(alias="slug")  # The slug url identifier for the enterprise.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    avatar_url: str = Field(alias="avatar_url")
    
    class Config:
        populate_by_name = True


class SimpleInstallation(BaseModel):
    """SimpleInstallation schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # The ID of the installation.
    node_id: str = Field(alias="node_id")  # The global node ID of the installation.
    
    class Config:
        populate_by_name = True


class OrganizationSimpleWebhooks(BaseModel):
    """OrganizationSimpleWebhooks schema from the OpenAPI specification."""
    login: str = Field(alias="login")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")
    repos_url: str = Field(alias="repos_url")
    events_url: str = Field(alias="events_url")
    hooks_url: str = Field(alias="hooks_url")
    issues_url: str = Field(alias="issues_url")
    members_url: str = Field(alias="members_url")
    public_members_url: str = Field(alias="public_members_url")
    avatar_url: str = Field(alias="avatar_url")
    description: str = Field(alias="description")
    
    class Config:
        populate_by_name = True


class RepositoryWebhooks(BaseModel):
    """RepositoryWebhooks schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    organization: NullableSimpleUser = Field(alias="organization")  # A GitHub user.
    forks: int = Field(alias="forks")
    permissions: Dict[str, Any] = Field(alias="permissions")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private or public.
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")  # The default branch of the repository.
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")  # Whether this repository acts as a template that can be used to generate new repositories.
    topics: List[str] = Field(alias="topics")
    custom_properties: Dict[str, Any] = Field(alias="custom_properties")  # The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.
    has_issues: bool = Field(alias="has_issues")  # Whether issues are enabled.
    has_projects: bool = Field(alias="has_projects")  # Whether projects are enabled.
    has_wiki: bool = Field(alias="has_wiki")  # Whether the wiki is enabled.
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")  # Whether downloads are enabled.
    has_discussions: bool = Field(alias="has_discussions")  # Whether discussions are enabled.
    archived: bool = Field(alias="archived")  # Whether the repository is archived.
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")  # Whether to allow rebase merges for pull requests.
    template_repository: Dict[str, Any] = Field(alias="template_repository")
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")  # Whether to allow squash merges for pull requests.
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow Auto-merge to be used on pull requests.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged
    allow_update_branch: bool = Field(alias="allow_update_branch")  # Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")  # Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:

- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:

- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.

- `PR_TITLE` - default to the pull request\'s title.
- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.

- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    allow_merge_commit: bool = Field(alias="allow_merge_commit")  # Whether to allow merge commits for pull requests.
    allow_forking: bool = Field(alias="allow_forking")  # Whether to allow forking this repo
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")  # Whether to require contributors to sign off on web-based commits
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    master_branch: str = Field(alias="master_branch")
    starred_at: str = Field(alias="starred_at")
    anonymous_access_enabled: bool = Field(alias="anonymous_access_enabled")  # Whether anonymous git access is enabled for this repository
    
    class Config:
        populate_by_name = True


class WebhooksRule(BaseModel):
    """WebhooksRule schema from the OpenAPI specification."""
    admin_enforced: bool = Field(alias="admin_enforced")
    allow_deletions_enforcement_level: str = Field(alias="allow_deletions_enforcement_level")
    allow_force_pushes_enforcement_level: str = Field(alias="allow_force_pushes_enforcement_level")
    authorized_actor_names: List[str] = Field(alias="authorized_actor_names")
    authorized_actors_only: bool = Field(alias="authorized_actors_only")
    authorized_dismissal_actors_only: bool = Field(alias="authorized_dismissal_actors_only")
    create_protected: bool = Field(alias="create_protected")
    created_at: str = Field(alias="created_at")
    dismiss_stale_reviews_on_push: bool = Field(alias="dismiss_stale_reviews_on_push")
    id_field: int = Field(alias="id")
    ignore_approvals_from_contributors: bool = Field(alias="ignore_approvals_from_contributors")
    linear_history_requirement_enforcement_level: str = Field(alias="linear_history_requirement_enforcement_level")
    lock_branch_enforcement_level: str = Field(alias="lock_branch_enforcement_level")  # The enforcement level of the branch lock setting. `off` means the branch is not locked, `non_admins` means the branch is read-only for non_admins, and `everyone` means the branch is read-only for everyone.
    lock_allows_fork_sync: bool = Field(alias="lock_allows_fork_sync")  # Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow users to pull changes from upstream when the branch is locked. This setting is only applicable for forks.
    merge_queue_enforcement_level: str = Field(alias="merge_queue_enforcement_level")
    name: str = Field(alias="name")
    pull_request_reviews_enforcement_level: str = Field(alias="pull_request_reviews_enforcement_level")
    repository_id: int = Field(alias="repository_id")
    require_code_owner_review: bool = Field(alias="require_code_owner_review")
    require_last_push_approval: bool = Field(alias="require_last_push_approval")  # Whether the most recent push must be approved by someone other than the person who pushed it
    required_approving_review_count: int = Field(alias="required_approving_review_count")
    required_conversation_resolution_level: str = Field(alias="required_conversation_resolution_level")
    required_deployments_enforcement_level: str = Field(alias="required_deployments_enforcement_level")
    required_status_checks: List[str] = Field(alias="required_status_checks")
    required_status_checks_enforcement_level: str = Field(alias="required_status_checks_enforcement_level")
    signature_requirement_enforcement_level: str = Field(alias="signature_requirement_enforcement_level")
    strict_required_status_checks_policy: bool = Field(alias="strict_required_status_checks_policy")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class SimpleCheckSuite(BaseModel):
    """SimpleCheckSuite schema from the OpenAPI specification."""
    after: str = Field(alias="after")
    app: Integration = Field(alias="app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    before: str = Field(alias="before")
    conclusion: str = Field(alias="conclusion")
    created_at: str = Field(alias="created_at")
    head_branch: str = Field(alias="head_branch")
    head_sha: str = Field(alias="head_sha")  # The SHA of the head commit that is being checked.
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    pull_requests: List[PullRequestMinimal] = Field(alias="pull_requests")
    repository: MinimalRepository = Field(alias="repository")  # Minimal Repository
    status: str = Field(alias="status")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class CheckRunWithSimpleCheckSuite(BaseModel):
    """CheckRunWithSimpleCheckSuite schema from the OpenAPI specification."""
    app: Integration = Field(alias="app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    check_suite: SimpleCheckSuite = Field(alias="check_suite")  # A suite of checks performed on the code of a given code change
    completed_at: str = Field(alias="completed_at")
    conclusion: str = Field(alias="conclusion")
    deployment: DeploymentSimple = Field(alias="deployment")  # A deployment created as the result of an Actions check run from a workflow that references an environment
    details_url: str = Field(alias="details_url")
    external_id: str = Field(alias="external_id")
    head_sha: str = Field(alias="head_sha")  # The SHA of the commit that is being checked.
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")  # The id of the check.
    name: str = Field(alias="name")  # The name of the check.
    node_id: str = Field(alias="node_id")
    output: Dict[str, Any] = Field(alias="output")
    pull_requests: List[PullRequestMinimal] = Field(alias="pull_requests")
    started_at: str = Field(alias="started_at")
    status: str = Field(alias="status")  # The phase of the lifecycle that the check is currently in.
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksDeployKey(BaseModel):
    """WebhooksDeployKey schema from the OpenAPI specification."""
    added_by: str = Field(alias="added_by")
    created_at: str = Field(alias="created_at")
    id_field: int = Field(alias="id")
    key: str = Field(alias="key")
    last_used: str = Field(alias="last_used")
    read_only: bool = Field(alias="read_only")
    title: str = Field(alias="title")
    url: str = Field(alias="url")
    verified: bool = Field(alias="verified")
    enabled: bool = Field(alias="enabled")
    
    class Config:
        populate_by_name = True


class WebhooksWorkflow(BaseModel):
    """WebhooksWorkflow schema from the OpenAPI specification."""
    badge_url: str = Field(alias="badge_url")
    created_at: str = Field(alias="created_at")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    path: str = Field(alias="path")
    state: str = Field(alias="state")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksApprover(BaseModel):
    """WebhooksApprover schema from the OpenAPI specification."""
    avatar_url: str = Field(alias="avatar_url")
    events_url: str = Field(alias="events_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    gravatar_id: str = Field(alias="gravatar_id")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    node_id: str = Field(alias="node_id")
    organizations_url: str = Field(alias="organizations_url")
    received_events_url: str = Field(alias="received_events_url")
    repos_url: str = Field(alias="repos_url")
    site_admin: bool = Field(alias="site_admin")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    type_field: str = Field(alias="type")
    url: str = Field(alias="url")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class WebhooksWorkflowJobRun(BaseModel):
    """WebhooksWorkflowJobRun schema from the OpenAPI specification."""
    conclusion: Any = Field(alias="conclusion")
    created_at: str = Field(alias="created_at")
    environment: str = Field(alias="environment")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    name: Any = Field(alias="name")
    status: str = Field(alias="status")
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class WebhooksUser(BaseModel):
    """WebhooksUser schema from the OpenAPI specification."""
    avatar_url: str = Field(alias="avatar_url")
    deleted: bool = Field(alias="deleted")
    email: str = Field(alias="email")
    events_url: str = Field(alias="events_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    gravatar_id: str = Field(alias="gravatar_id")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    organizations_url: str = Field(alias="organizations_url")
    received_events_url: str = Field(alias="received_events_url")
    repos_url: str = Field(alias="repos_url")
    site_admin: bool = Field(alias="site_admin")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    type_field: str = Field(alias="type")
    url: str = Field(alias="url")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class WebhooksAnswer(BaseModel):
    """WebhooksAnswer schema from the OpenAPI specification."""
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")
    child_comment_count: int = Field(alias="child_comment_count")
    created_at: str = Field(alias="created_at")
    discussion_id: int = Field(alias="discussion_id")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    parent_id: Any = Field(alias="parent_id")
    reactions: Dict[str, Any] = Field(alias="reactions")
    repository_url: str = Field(alias="repository_url")
    updated_at: str = Field(alias="updated_at")
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class Discussion(BaseModel):
    """Discussion schema from the OpenAPI specification."""
    active_lock_reason: str = Field(alias="active_lock_reason")
    answer_chosen_at: str = Field(alias="answer_chosen_at")
    answer_chosen_by: Dict[str, Any] = Field(alias="answer_chosen_by")
    answer_html_url: str = Field(alias="answer_html_url")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")
    category: Dict[str, Any] = Field(alias="category")
    comments: int = Field(alias="comments")
    created_at: str = Field(alias="created_at")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    locked: bool = Field(alias="locked")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    reactions: Dict[str, Any] = Field(alias="reactions")
    repository_url: str = Field(alias="repository_url")
    state: str = Field(alias="state")  # The current state of the discussion.
`converting` means that the discussion is being converted from an issue.
`transferring` means that the discussion is being transferred from another repository.
    state_reason: str = Field(alias="state_reason")  # The reason for the current state
    timeline_url: str = Field(alias="timeline_url")
    title: str = Field(alias="title")
    updated_at: str = Field(alias="updated_at")
    user: Dict[str, Any] = Field(alias="user")
    labels: List[Label] = Field(alias="labels")
    
    class Config:
        populate_by_name = True


class WebhooksComment(BaseModel):
    """WebhooksComment schema from the OpenAPI specification."""
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")
    child_comment_count: int = Field(alias="child_comment_count")
    created_at: str = Field(alias="created_at")
    discussion_id: int = Field(alias="discussion_id")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    parent_id: int = Field(alias="parent_id")
    reactions: Dict[str, Any] = Field(alias="reactions")
    repository_url: str = Field(alias="repository_url")
    updated_at: str = Field(alias="updated_at")
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksLabel(BaseModel):
    """WebhooksLabel schema from the OpenAPI specification."""
    color: str = Field(alias="color")  # 6-character hex code, without the leading #, identifying the color
    default: bool = Field(alias="default")
    description: str = Field(alias="description")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")  # The name of the label.
    node_id: str = Field(alias="node_id")
    url: str = Field(alias="url")  # URL for the label
    
    class Config:
        populate_by_name = True


class WebhooksIssueComment(BaseModel):
    """WebhooksIssueComment schema from the OpenAPI specification."""
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")  # Contents of the issue comment
    created_at: str = Field(alias="created_at")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")  # Unique identifier of the issue comment
    issue_url: str = Field(alias="issue_url")
    node_id: str = Field(alias="node_id")
    performed_via_github_app: Integration = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    reactions: Dict[str, Any] = Field(alias="reactions")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")  # URL for the issue comment
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksChanges(BaseModel):
    """WebhooksChanges schema from the OpenAPI specification."""
    body: Dict[str, Any] = Field(alias="body")
    
    class Config:
        populate_by_name = True


class WebhooksIssue(BaseModel):
    """WebhooksIssue schema from the OpenAPI specification."""
    active_lock_reason: str = Field(alias="active_lock_reason")
    assignee: Dict[str, Any] = Field(alias="assignee")
    assignees: List[Dict[str, Any]] = Field(alias="assignees")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")  # Contents of the issue
    closed_at: str = Field(alias="closed_at")
    comments: int = Field(alias="comments")
    comments_url: str = Field(alias="comments_url")
    created_at: str = Field(alias="created_at")
    draft: bool = Field(alias="draft")
    events_url: str = Field(alias="events_url")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    labels_url: str = Field(alias="labels_url")
    locked: bool = Field(alias="locked")
    milestone: Dict[str, Any] = Field(alias="milestone")  # A collection of related issues and pull requests.
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    performed_via_github_app: Dict[str, Any] = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    reactions: Dict[str, Any] = Field(alias="reactions")
    repository_url: str = Field(alias="repository_url")
    sub_issues_summary: Dict[str, Any] = Field(alias="sub_issues_summary")
    state: str = Field(alias="state")  # State of the issue; either \'open\' or \'closed\'
    state_reason: str = Field(alias="state_reason")
    timeline_url: str = Field(alias="timeline_url")
    title: str = Field(alias="title")  # Title of the issue
    type_field: IssueType = Field(alias="type")  # The type of issue.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")  # URL for the issue
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksMilestone(BaseModel):
    """WebhooksMilestone schema from the OpenAPI specification."""
    closed_at: str = Field(alias="closed_at")
    closed_issues: int = Field(alias="closed_issues")
    created_at: str = Field(alias="created_at")
    creator: Dict[str, Any] = Field(alias="creator")
    description: str = Field(alias="description")
    due_on: str = Field(alias="due_on")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    labels_url: str = Field(alias="labels_url")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The number of the milestone.
    open_issues: int = Field(alias="open_issues")
    state: str = Field(alias="state")  # The state of the milestone.
    title: str = Field(alias="title")  # The title of the milestone.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksIssue2(BaseModel):
    """WebhooksIssue2 schema from the OpenAPI specification."""
    active_lock_reason: str = Field(alias="active_lock_reason")
    assignee: Dict[str, Any] = Field(alias="assignee")
    assignees: List[Dict[str, Any]] = Field(alias="assignees")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")  # Contents of the issue
    closed_at: str = Field(alias="closed_at")
    comments: int = Field(alias="comments")
    comments_url: str = Field(alias="comments_url")
    created_at: str = Field(alias="created_at")
    draft: bool = Field(alias="draft")
    events_url: str = Field(alias="events_url")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    labels_url: str = Field(alias="labels_url")
    locked: bool = Field(alias="locked")
    milestone: Dict[str, Any] = Field(alias="milestone")  # A collection of related issues and pull requests.
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    performed_via_github_app: Dict[str, Any] = Field(alias="performed_via_github_app")  # GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    reactions: Dict[str, Any] = Field(alias="reactions")
    repository_url: str = Field(alias="repository_url")
    sub_issues_summary: Dict[str, Any] = Field(alias="sub_issues_summary")
    state: str = Field(alias="state")  # State of the issue; either \'open\' or \'closed\'
    state_reason: str = Field(alias="state_reason")
    timeline_url: str = Field(alias="timeline_url")
    title: str = Field(alias="title")  # Title of the issue
    type_field: IssueType = Field(alias="type")  # The type of issue.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")  # URL for the issue
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksUserMannequin(BaseModel):
    """WebhooksUserMannequin schema from the OpenAPI specification."""
    avatar_url: str = Field(alias="avatar_url")
    deleted: bool = Field(alias="deleted")
    email: str = Field(alias="email")
    events_url: str = Field(alias="events_url")
    followers_url: str = Field(alias="followers_url")
    following_url: str = Field(alias="following_url")
    gists_url: str = Field(alias="gists_url")
    gravatar_id: str = Field(alias="gravatar_id")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    login: str = Field(alias="login")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    organizations_url: str = Field(alias="organizations_url")
    received_events_url: str = Field(alias="received_events_url")
    repos_url: str = Field(alias="repos_url")
    site_admin: bool = Field(alias="site_admin")
    starred_url: str = Field(alias="starred_url")
    subscriptions_url: str = Field(alias="subscriptions_url")
    type_field: str = Field(alias="type")
    url: str = Field(alias="url")
    user_view_type: str = Field(alias="user_view_type")
    
    class Config:
        populate_by_name = True


class WebhooksMarketplacePurchase(BaseModel):
    """WebhooksMarketplacePurchase schema from the OpenAPI specification."""
    account: Dict[str, Any] = Field(alias="account")
    billing_cycle: str = Field(alias="billing_cycle")
    free_trial_ends_on: str = Field(alias="free_trial_ends_on")
    next_billing_date: str = Field(alias="next_billing_date")
    on_free_trial: bool = Field(alias="on_free_trial")
    plan: Dict[str, Any] = Field(alias="plan")
    unit_count: int = Field(alias="unit_count")
    
    class Config:
        populate_by_name = True


class WebhooksPreviousMarketplacePurchase(BaseModel):
    """WebhooksPreviousMarketplacePurchase schema from the OpenAPI specification."""
    account: Dict[str, Any] = Field(alias="account")
    billing_cycle: str = Field(alias="billing_cycle")
    free_trial_ends_on: Any = Field(alias="free_trial_ends_on")
    next_billing_date: str = Field(alias="next_billing_date")
    on_free_trial: bool = Field(alias="on_free_trial")
    plan: Dict[str, Any] = Field(alias="plan")
    unit_count: int = Field(alias="unit_count")
    
    class Config:
        populate_by_name = True


class WebhooksTeam(BaseModel):
    """WebhooksTeam schema from the OpenAPI specification."""
    deleted: bool = Field(alias="deleted")
    description: str = Field(alias="description")  # Description of the team
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")  # Unique identifier of the team
    members_url: str = Field(alias="members_url")
    name: str = Field(alias="name")  # Name of the team
    node_id: str = Field(alias="node_id")
    parent: Dict[str, Any] = Field(alias="parent")
    permission: str = Field(alias="permission")  # Permission that the team will have for its repositories
    privacy: str = Field(alias="privacy")
    notification_setting: str = Field(alias="notification_setting")
    repositories_url: str = Field(alias="repositories_url")
    slug: str = Field(alias="slug")
    url: str = Field(alias="url")  # URL for the team
    
    class Config:
        populate_by_name = True


class MergeGroup(BaseModel):
    """MergeGroup schema from the OpenAPI specification."""
    head_sha: str = Field(alias="head_sha")  # The SHA of the merge group.
    head_ref: str = Field(alias="head_ref")  # The full ref of the merge group.
    base_sha: str = Field(alias="base_sha")  # The SHA of the merge group\'s parent commit.
    base_ref: str = Field(alias="base_ref")  # The full ref of the branch the merge group will be merged into.
    head_commit: SimpleCommit = Field(alias="head_commit")  # A commit.
    
    class Config:
        populate_by_name = True


class NullableRepositoryWebhooks(BaseModel):
    """NullableRepositoryWebhooks schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the repository
    node_id: str = Field(alias="node_id")
    name: str = Field(alias="name")  # The name of the repository.
    full_name: str = Field(alias="full_name")
    license: NullableLicenseSimple = Field(alias="license")  # License Simple
    organization: NullableSimpleUser = Field(alias="organization")  # A GitHub user.
    forks: int = Field(alias="forks")
    permissions: Dict[str, Any] = Field(alias="permissions")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    private: bool = Field(alias="private")  # Whether the repository is private or public.
    html_url: str = Field(alias="html_url")
    description: str = Field(alias="description")
    fork: bool = Field(alias="fork")
    url: str = Field(alias="url")
    archive_url: str = Field(alias="archive_url")
    assignees_url: str = Field(alias="assignees_url")
    blobs_url: str = Field(alias="blobs_url")
    branches_url: str = Field(alias="branches_url")
    collaborators_url: str = Field(alias="collaborators_url")
    comments_url: str = Field(alias="comments_url")
    commits_url: str = Field(alias="commits_url")
    compare_url: str = Field(alias="compare_url")
    contents_url: str = Field(alias="contents_url")
    contributors_url: str = Field(alias="contributors_url")
    deployments_url: str = Field(alias="deployments_url")
    downloads_url: str = Field(alias="downloads_url")
    events_url: str = Field(alias="events_url")
    forks_url: str = Field(alias="forks_url")
    git_commits_url: str = Field(alias="git_commits_url")
    git_refs_url: str = Field(alias="git_refs_url")
    git_tags_url: str = Field(alias="git_tags_url")
    git_url: str = Field(alias="git_url")
    issue_comment_url: str = Field(alias="issue_comment_url")
    issue_events_url: str = Field(alias="issue_events_url")
    issues_url: str = Field(alias="issues_url")
    keys_url: str = Field(alias="keys_url")
    labels_url: str = Field(alias="labels_url")
    languages_url: str = Field(alias="languages_url")
    merges_url: str = Field(alias="merges_url")
    milestones_url: str = Field(alias="milestones_url")
    notifications_url: str = Field(alias="notifications_url")
    pulls_url: str = Field(alias="pulls_url")
    releases_url: str = Field(alias="releases_url")
    ssh_url: str = Field(alias="ssh_url")
    stargazers_url: str = Field(alias="stargazers_url")
    statuses_url: str = Field(alias="statuses_url")
    subscribers_url: str = Field(alias="subscribers_url")
    subscription_url: str = Field(alias="subscription_url")
    tags_url: str = Field(alias="tags_url")
    teams_url: str = Field(alias="teams_url")
    trees_url: str = Field(alias="trees_url")
    clone_url: str = Field(alias="clone_url")
    mirror_url: str = Field(alias="mirror_url")
    hooks_url: str = Field(alias="hooks_url")
    svn_url: str = Field(alias="svn_url")
    homepage: str = Field(alias="homepage")
    language: str = Field(alias="language")
    forks_count: int = Field(alias="forks_count")
    stargazers_count: int = Field(alias="stargazers_count")
    watchers_count: int = Field(alias="watchers_count")
    size: int = Field(alias="size")  # The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0.
    default_branch: str = Field(alias="default_branch")  # The default branch of the repository.
    open_issues_count: int = Field(alias="open_issues_count")
    is_template: bool = Field(alias="is_template")  # Whether this repository acts as a template that can be used to generate new repositories.
    topics: List[str] = Field(alias="topics")
    custom_properties: Dict[str, Any] = Field(alias="custom_properties")  # The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values.
    has_issues: bool = Field(alias="has_issues")  # Whether issues are enabled.
    has_projects: bool = Field(alias="has_projects")  # Whether projects are enabled.
    has_wiki: bool = Field(alias="has_wiki")  # Whether the wiki is enabled.
    has_pages: bool = Field(alias="has_pages")
    has_downloads: bool = Field(alias="has_downloads")  # Whether downloads are enabled.
    has_discussions: bool = Field(alias="has_discussions")  # Whether discussions are enabled.
    archived: bool = Field(alias="archived")  # Whether the repository is archived.
    disabled: bool = Field(alias="disabled")  # Returns whether or not this repository disabled.
    visibility: str = Field(alias="visibility")  # The repository visibility: public, private, or internal.
    pushed_at: str = Field(alias="pushed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    allow_rebase_merge: bool = Field(alias="allow_rebase_merge")  # Whether to allow rebase merges for pull requests.
    template_repository: Dict[str, Any] = Field(alias="template_repository")
    temp_clone_token: str = Field(alias="temp_clone_token")
    allow_squash_merge: bool = Field(alias="allow_squash_merge")  # Whether to allow squash merges for pull requests.
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow Auto-merge to be used on pull requests.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged
    allow_update_branch: bool = Field(alias="allow_update_branch")  # Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging.
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")  # Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:

- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:

- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.

- `PR_TITLE` - default to the pull request\'s title.
- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name).
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.

- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    allow_merge_commit: bool = Field(alias="allow_merge_commit")  # Whether to allow merge commits for pull requests.
    allow_forking: bool = Field(alias="allow_forking")  # Whether to allow forking this repo
    web_commit_signoff_required: bool = Field(alias="web_commit_signoff_required")  # Whether to require contributors to sign off on web-based commits
    subscribers_count: int = Field(alias="subscribers_count")
    network_count: int = Field(alias="network_count")
    open_issues: int = Field(alias="open_issues")
    watchers: int = Field(alias="watchers")
    master_branch: str = Field(alias="master_branch")
    starred_at: str = Field(alias="starred_at")
    anonymous_access_enabled: bool = Field(alias="anonymous_access_enabled")  # Whether anonymous git access is enabled for this repository
    
    class Config:
        populate_by_name = True


class WebhooksMilestone3(BaseModel):
    """WebhooksMilestone3 schema from the OpenAPI specification."""
    closed_at: str = Field(alias="closed_at")
    closed_issues: int = Field(alias="closed_issues")
    created_at: str = Field(alias="created_at")
    creator: Dict[str, Any] = Field(alias="creator")
    description: str = Field(alias="description")
    due_on: str = Field(alias="due_on")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    labels_url: str = Field(alias="labels_url")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # The number of the milestone.
    open_issues: int = Field(alias="open_issues")
    state: str = Field(alias="state")  # The state of the milestone.
    title: str = Field(alias="title")  # The title of the milestone.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksMembership(BaseModel):
    """WebhooksMembership schema from the OpenAPI specification."""
    organization_url: str = Field(alias="organization_url")
    role: str = Field(alias="role")
    state: str = Field(alias="state")
    url: str = Field(alias="url")
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class PersonalAccessTokenRequest(BaseModel):
    """PersonalAccessTokenRequest schema from the OpenAPI specification."""
    id_field: int = Field(alias="id")  # Unique identifier of the request for access via fine-grained personal access token. Used as the `pat_request_id` parameter in the list and review API calls.
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    permissions_added: Dict[str, Any] = Field(alias="permissions_added")  # New requested permissions, categorized by type of permission.
    permissions_upgraded: Dict[str, Any] = Field(alias="permissions_upgraded")  # Requested permissions that elevate access for a previously approved request for access, categorized by type of permission.
    permissions_result: Dict[str, Any] = Field(alias="permissions_result")  # Permissions requested, categorized by type of permission. This field incorporates `permissions_added` and `permissions_upgraded`.
    repository_selection: str = Field(alias="repository_selection")  # Type of repository selection requested.
    repository_count: int = Field(alias="repository_count")  # The number of repositories the token is requesting access to. This field is only populated when `repository_selection` is `subset`.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects the token is requesting access to. This field is only populated when `repository_selection` is `subset`.
    created_at: str = Field(alias="created_at")  # Date and time when the request for access was created.
    token_id: int = Field(alias="token_id")  # Unique identifier of the user\'s token. This field can also be found in audit log events and the organization\'s settings for their PAT grants.
    token_name: str = Field(alias="token_name")  # The name given to the user\'s token. This field can also be found in an organization\'s settings page for Active Tokens.
    token_expired: bool = Field(alias="token_expired")  # Whether the associated fine-grained personal access token has expired.
    token_expires_at: str = Field(alias="token_expires_at")  # Date and time when the associated fine-grained personal access token expires.
    token_last_used_at: str = Field(alias="token_last_used_at")  # Date and time when the associated fine-grained personal access token was last used for authentication.
    
    class Config:
        populate_by_name = True


class WebhooksProjectCard(BaseModel):
    """WebhooksProjectCard schema from the OpenAPI specification."""
    after_id: int = Field(alias="after_id")
    archived: bool = Field(alias="archived")  # Whether or not the card is archived
    column_id: int = Field(alias="column_id")
    column_url: str = Field(alias="column_url")
    content_url: str = Field(alias="content_url")
    created_at: str = Field(alias="created_at")
    creator: Dict[str, Any] = Field(alias="creator")
    id_field: int = Field(alias="id")  # The project card\'s ID
    node_id: str = Field(alias="node_id")
    note: str = Field(alias="note")
    project_url: str = Field(alias="project_url")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksProject(BaseModel):
    """WebhooksProject schema from the OpenAPI specification."""
    body: str = Field(alias="body")  # Body of the project
    columns_url: str = Field(alias="columns_url")
    created_at: str = Field(alias="created_at")
    creator: Dict[str, Any] = Field(alias="creator")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")  # Name of the project
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    owner_url: str = Field(alias="owner_url")
    state: str = Field(alias="state")  # State of the project; either \'open\' or \'closed\'
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class WebhooksProjectColumn(BaseModel):
    """WebhooksProjectColumn schema from the OpenAPI specification."""
    after_id: int = Field(alias="after_id")
    cards_url: str = Field(alias="cards_url")
    created_at: str = Field(alias="created_at")
    id_field: int = Field(alias="id")  # The unique identifier of the project column
    name: str = Field(alias="name")  # Name of the project column
    node_id: str = Field(alias="node_id")
    project_url: str = Field(alias="project_url")
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    
    class Config:
        populate_by_name = True


class ProjectsV2(BaseModel):
    """ProjectsV2 schema from the OpenAPI specification."""
    id_field: float = Field(alias="id")
    node_id: str = Field(alias="node_id")
    owner: SimpleUser = Field(alias="owner")  # A GitHub user.
    creator: SimpleUser = Field(alias="creator")  # A GitHub user.
    title: str = Field(alias="title")
    description: str = Field(alias="description")
    public: bool = Field(alias="public")
    closed_at: str = Field(alias="closed_at")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    number: int = Field(alias="number")
    short_description: str = Field(alias="short_description")
    deleted_at: str = Field(alias="deleted_at")
    deleted_by: NullableSimpleUser = Field(alias="deleted_by")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhooksProjectChanges(BaseModel):
    """WebhooksProjectChanges schema from the OpenAPI specification."""
    archived_at: Dict[str, Any] = Field(alias="archived_at")
    
    class Config:
        populate_by_name = True


class ProjectsV2Item(BaseModel):
    """ProjectsV2Item schema from the OpenAPI specification."""
    id_field: float = Field(alias="id")
    node_id: str = Field(alias="node_id")
    project_node_id: str = Field(alias="project_node_id")
    content_node_id: str = Field(alias="content_node_id")
    content_type: str = Field(alias="content_type")  # The type of content tracked in a project item
    creator: SimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    archived_at: str = Field(alias="archived_at")
    
    class Config:
        populate_by_name = True


class ProjectsV2SingleSelectOption(BaseModel):
    """ProjectsV2SingleSelectOption schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")
    name: str = Field(alias="name")
    color: str = Field(alias="color")
    description: str = Field(alias="description")
    
    class Config:
        populate_by_name = True


class ProjectsV2IterationSetting(BaseModel):
    """ProjectsV2IterationSetting schema from the OpenAPI specification."""
    id_field: str = Field(alias="id")
    title: str = Field(alias="title")
    duration: float = Field(alias="duration")
    start_date: str = Field(alias="start_date")
    
    class Config:
        populate_by_name = True


class ProjectsV2StatusUpdate(BaseModel):
    """ProjectsV2StatusUpdate schema from the OpenAPI specification."""
    id_field: float = Field(alias="id")
    node_id: str = Field(alias="node_id")
    project_node_id: str = Field(alias="project_node_id")
    creator: SimpleUser = Field(alias="creator")  # A GitHub user.
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    status: str = Field(alias="status")
    start_date: str = Field(alias="start_date")
    target_date: str = Field(alias="target_date")
    body: str = Field(alias="body")  # Body of the status update
    
    class Config:
        populate_by_name = True


class PullRequestWebhook(BaseModel):
    """PullRequestWebhook schema from the OpenAPI specification."""
    url: str = Field(alias="url")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    html_url: str = Field(alias="html_url")
    diff_url: str = Field(alias="diff_url")
    patch_url: str = Field(alias="patch_url")
    issue_url: str = Field(alias="issue_url")
    commits_url: str = Field(alias="commits_url")
    review_comments_url: str = Field(alias="review_comments_url")
    review_comment_url: str = Field(alias="review_comment_url")
    comments_url: str = Field(alias="comments_url")
    statuses_url: str = Field(alias="statuses_url")
    number: int = Field(alias="number")  # Number uniquely identifying the pull request within its repository.
    state: str = Field(alias="state")  # State of this Pull Request. Either `open` or `closed`.
    locked: bool = Field(alias="locked")
    title: str = Field(alias="title")  # The title of the pull request.
    user: SimpleUser = Field(alias="user")  # A GitHub user.
    body: str = Field(alias="body")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    milestone: NullableMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    active_lock_reason: str = Field(alias="active_lock_reason")
    created_at: str = Field(alias="created_at")
    updated_at: str = Field(alias="updated_at")
    closed_at: str = Field(alias="closed_at")
    merged_at: str = Field(alias="merged_at")
    merge_commit_sha: str = Field(alias="merge_commit_sha")
    assignee: NullableSimpleUser = Field(alias="assignee")  # A GitHub user.
    assignees: List[SimpleUser] = Field(alias="assignees")
    requested_reviewers: List[SimpleUser] = Field(alias="requested_reviewers")
    requested_teams: List[TeamSimple] = Field(alias="requested_teams")
    head: Dict[str, Any] = Field(alias="head")
    base: Dict[str, Any] = Field(alias="base")
    links: Dict[str, Any] = Field(alias="_links")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    auto_merge: AutoMerge = Field(alias="auto_merge")  # The status of auto merging a pull request.
    draft: bool = Field(alias="draft")  # Indicates whether or not the pull request is a draft.
    merged: bool = Field(alias="merged")
    mergeable: bool = Field(alias="mergeable")
    rebaseable: bool = Field(alias="rebaseable")
    mergeable_state: str = Field(alias="mergeable_state")
    merged_by: NullableSimpleUser = Field(alias="merged_by")  # A GitHub user.
    comments: int = Field(alias="comments")
    review_comments: int = Field(alias="review_comments")
    maintainer_can_modify: bool = Field(alias="maintainer_can_modify")  # Indicates whether maintainers can modify the pull request.
    commits: int = Field(alias="commits")
    additions: int = Field(alias="additions")
    deletions: int = Field(alias="deletions")
    changed_files: int = Field(alias="changed_files")
    allow_auto_merge: bool = Field(alias="allow_auto_merge")  # Whether to allow auto-merge for pull requests.
    allow_update_branch: bool = Field(alias="allow_update_branch")  # Whether to allow updating the pull request\'s branch.
    delete_branch_on_merge: bool = Field(alias="delete_branch_on_merge")  # Whether to delete head branches when pull requests are merged.
    merge_commit_message: str = Field(alias="merge_commit_message")  # The default value for a merge commit message.
- `PR_TITLE` - default to the pull request\'s title.
- `PR_BODY` - default to the pull request\'s body.
- `BLANK` - default to a blank commit message.
    merge_commit_title: str = Field(alias="merge_commit_title")  # The default value for a merge commit title.
- `PR_TITLE` - default to the pull request\'s title.
- `MERGE_MESSAGE` - default to the classic title for a merge message (e.g., \"Merge pull request #123 from branch-name\").
    squash_merge_commit_message: str = Field(alias="squash_merge_commit_message")  # The default value for a squash merge commit message:
- `PR_BODY` - default to the pull request\'s body.
- `COMMIT_MESSAGES` - default to the branch\'s commit messages.
- `BLANK` - default to a blank commit message.
    squash_merge_commit_title: str = Field(alias="squash_merge_commit_title")  # The default value for a squash merge commit title:
- `PR_TITLE` - default to the pull request\'s title.
- `COMMIT_OR_PR_TITLE` - default to the commit\'s title (if only one commit) or the pull request\'s title (when more than one commit).
    use_squash_pr_title_as_default: bool = Field(alias="use_squash_pr_title_as_default")  # Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use `squash_merge_commit_title` instead.**
    
    class Config:
        populate_by_name = True


class WebhooksPullRequest5(BaseModel):
    """WebhooksPullRequest5 schema from the OpenAPI specification."""
    links: Dict[str, Any] = Field(alias="_links")
    active_lock_reason: str = Field(alias="active_lock_reason")
    additions: int = Field(alias="additions")
    assignee: Dict[str, Any] = Field(alias="assignee")
    assignees: List[Dict[str, Any]] = Field(alias="assignees")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    auto_merge: Dict[str, Any] = Field(alias="auto_merge")  # The status of auto merging a pull request.
    base: Dict[str, Any] = Field(alias="base")
    body: str = Field(alias="body")
    changed_files: int = Field(alias="changed_files")
    closed_at: str = Field(alias="closed_at")
    comments: int = Field(alias="comments")
    comments_url: str = Field(alias="comments_url")
    commits: int = Field(alias="commits")
    commits_url: str = Field(alias="commits_url")
    created_at: str = Field(alias="created_at")
    deletions: int = Field(alias="deletions")
    diff_url: str = Field(alias="diff_url")
    draft: bool = Field(alias="draft")  # Indicates whether or not the pull request is a draft.
    head: Dict[str, Any] = Field(alias="head")
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    issue_url: str = Field(alias="issue_url")
    labels: List[Dict[str, Any]] = Field(alias="labels")
    locked: bool = Field(alias="locked")
    maintainer_can_modify: bool = Field(alias="maintainer_can_modify")  # Indicates whether maintainers can modify the pull request.
    merge_commit_sha: str = Field(alias="merge_commit_sha")
    mergeable: bool = Field(alias="mergeable")
    mergeable_state: str = Field(alias="mergeable_state")
    merged: bool = Field(alias="merged")
    merged_at: str = Field(alias="merged_at")
    merged_by: Dict[str, Any] = Field(alias="merged_by")
    milestone: Dict[str, Any] = Field(alias="milestone")  # A collection of related issues and pull requests.
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")  # Number uniquely identifying the pull request within its repository.
    patch_url: str = Field(alias="patch_url")
    rebaseable: bool = Field(alias="rebaseable")
    requested_reviewers: List[Any] = Field(alias="requested_reviewers")
    requested_teams: List[Dict[str, Any]] = Field(alias="requested_teams")
    review_comment_url: str = Field(alias="review_comment_url")
    review_comments: int = Field(alias="review_comments")
    review_comments_url: str = Field(alias="review_comments_url")
    state: str = Field(alias="state")  # State of this Pull Request. Either `open` or `closed`.
    statuses_url: str = Field(alias="statuses_url")
    title: str = Field(alias="title")  # The title of the pull request.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksReviewComment(BaseModel):
    """WebhooksReviewComment schema from the OpenAPI specification."""
    links: Dict[str, Any] = Field(alias="_links")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")  # The text of the comment.
    commit_id: str = Field(alias="commit_id")  # The SHA of the commit to which the comment applies.
    created_at: str = Field(alias="created_at")
    diff_hunk: str = Field(alias="diff_hunk")  # The diff of the line that the comment refers to.
    html_url: str = Field(alias="html_url")  # HTML URL for the pull request review comment.
    id_field: int = Field(alias="id")  # The ID of the pull request review comment.
    in_reply_to_id: int = Field(alias="in_reply_to_id")  # The comment ID to reply to.
    line: int = Field(alias="line")  # The line of the blob to which the comment applies. The last line of the range for a multi-line comment
    node_id: str = Field(alias="node_id")  # The node ID of the pull request review comment.
    original_commit_id: str = Field(alias="original_commit_id")  # The SHA of the original commit to which the comment applies.
    original_line: int = Field(alias="original_line")  # The line of the blob to which the comment applies. The last line of the range for a multi-line comment
    original_position: int = Field(alias="original_position")  # The index of the original line in the diff to which the comment applies.
    original_start_line: int = Field(alias="original_start_line")  # The first line of the range for a multi-line comment.
    path: str = Field(alias="path")  # The relative path of the file to which the comment applies.
    position: int = Field(alias="position")  # The line index in the diff to which the comment applies.
    pull_request_review_id: int = Field(alias="pull_request_review_id")  # The ID of the pull request review to which the comment belongs.
    pull_request_url: str = Field(alias="pull_request_url")  # URL for the pull request that the review comment belongs to.
    reactions: Dict[str, Any] = Field(alias="reactions")
    side: str = Field(alias="side")  # The side of the first line of the range for a multi-line comment.
    start_line: int = Field(alias="start_line")  # The first line of the range for a multi-line comment.
    start_side: str = Field(alias="start_side")  # The side of the first line of the range for a multi-line comment.
    subject_type: str = Field(alias="subject_type")  # The level at which the comment is targeted, can be a diff line or a file.
    updated_at: str = Field(alias="updated_at")
    url: str = Field(alias="url")  # URL for the pull request review comment
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksReview(BaseModel):
    """WebhooksReview schema from the OpenAPI specification."""
    links: Dict[str, Any] = Field(alias="_links")
    author_association: str = Field(alias="author_association")  # How the author is associated with the repository.
    body: str = Field(alias="body")  # The text of the review.
    commit_id: str = Field(alias="commit_id")  # A commit SHA for the review.
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")  # Unique identifier of the review
    node_id: str = Field(alias="node_id")
    pull_request_url: str = Field(alias="pull_request_url")
    state: str = Field(alias="state")
    submitted_at: str = Field(alias="submitted_at")
    user: Dict[str, Any] = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhooksRelease(BaseModel):
    """WebhooksRelease schema from the OpenAPI specification."""
    assets: List[Dict[str, Any]] = Field(alias="assets")
    assets_url: str = Field(alias="assets_url")
    author: Dict[str, Any] = Field(alias="author")
    body: str = Field(alias="body")
    created_at: str = Field(alias="created_at")
    discussion_url: str = Field(alias="discussion_url")
    draft: bool = Field(alias="draft")  # Whether the release is a draft or published
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    prerelease: bool = Field(alias="prerelease")  # Whether the release is identified as a prerelease or a full release.
    published_at: str = Field(alias="published_at")
    reactions: Dict[str, Any] = Field(alias="reactions")
    tag_name: str = Field(alias="tag_name")  # The name of the tag.
    tarball_url: str = Field(alias="tarball_url")
    target_commitish: str = Field(alias="target_commitish")  # Specifies the commitish value that determines where the Git tag is created from.
    upload_url: str = Field(alias="upload_url")
    url: str = Field(alias="url")
    zipball_url: str = Field(alias="zipball_url")
    
    class Config:
        populate_by_name = True


class WebhooksRelease1(BaseModel):
    """WebhooksRelease1 schema from the OpenAPI specification."""
    assets: List[Dict[str, Any]] = Field(alias="assets")
    assets_url: str = Field(alias="assets_url")
    author: Dict[str, Any] = Field(alias="author")
    body: str = Field(alias="body")
    created_at: str = Field(alias="created_at")
    discussion_url: str = Field(alias="discussion_url")
    draft: bool = Field(alias="draft")  # Whether the release is a draft or published
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")
    name: str = Field(alias="name")
    node_id: str = Field(alias="node_id")
    prerelease: bool = Field(alias="prerelease")  # Whether the release is identified as a prerelease or a full release.
    published_at: str = Field(alias="published_at")
    reactions: Dict[str, Any] = Field(alias="reactions")
    tag_name: str = Field(alias="tag_name")  # The name of the tag.
    tarball_url: str = Field(alias="tarball_url")
    target_commitish: str = Field(alias="target_commitish")  # Specifies the commitish value that determines where the Git tag is created from.
    upload_url: str = Field(alias="upload_url")
    url: str = Field(alias="url")
    zipball_url: str = Field(alias="zipball_url")
    
    class Config:
        populate_by_name = True


class WebhooksAlert(BaseModel):
    """WebhooksAlert schema from the OpenAPI specification."""
    affected_package_name: str = Field(alias="affected_package_name")
    affected_range: str = Field(alias="affected_range")
    created_at: str = Field(alias="created_at")
    dismiss_reason: str = Field(alias="dismiss_reason")
    dismissed_at: str = Field(alias="dismissed_at")
    dismisser: Dict[str, Any] = Field(alias="dismisser")
    external_identifier: str = Field(alias="external_identifier")
    external_reference: str = Field(alias="external_reference")
    fix_reason: str = Field(alias="fix_reason")
    fixed_at: str = Field(alias="fixed_at")
    fixed_in: str = Field(alias="fixed_in")
    ghsa_id: str = Field(alias="ghsa_id")
    id_field: int = Field(alias="id")
    node_id: str = Field(alias="node_id")
    number: int = Field(alias="number")
    severity: str = Field(alias="severity")
    state: str = Field(alias="state")
    
    class Config:
        populate_by_name = True


class SecretScanningAlertWebhook(BaseModel):
    """SecretScanningAlertWebhook schema from the OpenAPI specification."""
    number: int = Field(alias="number")  # The security alert number.
    created_at: str = Field(alias="created_at")  # The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    updated_at: str = Field(alias="updated_at")  # The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    url: str = Field(alias="url")  # The REST API URL of the alert resource.
    html_url: str = Field(alias="html_url")  # The GitHub URL of the alert resource.
    locations_url: str = Field(alias="locations_url")  # The REST API URL of the code locations for this alert.
    resolution: str = Field(alias="resolution")  # The reason for resolving the alert.
    resolved_at: str = Field(alias="resolved_at")  # The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    resolved_by: NullableSimpleUser = Field(alias="resolved_by")  # A GitHub user.
    resolution_comment: str = Field(alias="resolution_comment")  # An optional comment to resolve an alert.
    secret_type: str = Field(alias="secret_type")  # The type of secret that secret scanning detected.
    secret_type_display_name: str = Field(alias="secret_type_display_name")  # User-friendly name for the detected secret, matching the `secret_type`.
For a list of built-in patterns, see \"[Supported secret scanning patterns](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).\"
    validity: str = Field(alias="validity")  # The token status as of the latest validity check.
    push_protection_bypassed: bool = Field(alias="push_protection_bypassed")  # Whether push protection was bypassed for the detected secret.
    push_protection_bypassed_by: NullableSimpleUser = Field(alias="push_protection_bypassed_by")  # A GitHub user.
    push_protection_bypassed_at: str = Field(alias="push_protection_bypassed_at")  # The time that push protection was bypassed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    push_protection_bypass_request_reviewer: NullableSimpleUser = Field(alias="push_protection_bypass_request_reviewer")  # A GitHub user.
    push_protection_bypass_request_reviewer_comment: str = Field(alias="push_protection_bypass_request_reviewer_comment")  # An optional comment when reviewing a push protection bypass.
    push_protection_bypass_request_comment: str = Field(alias="push_protection_bypass_request_comment")  # An optional comment when requesting a push protection bypass.
    push_protection_bypass_request_html_url: str = Field(alias="push_protection_bypass_request_html_url")  # The URL to a push protection bypass request.
    publicly_leaked: bool = Field(alias="publicly_leaked")  # Whether the detected secret was publicly leaked.
    multi_repo: bool = Field(alias="multi_repo")  # Whether the detected secret was found in multiple repositories in the same organization or business.
    
    class Config:
        populate_by_name = True


class WebhooksSecurityAdvisory(BaseModel):
    """WebhooksSecurityAdvisory schema from the OpenAPI specification."""
    cvss: Dict[str, Any] = Field(alias="cvss")
    cvss_severities: CvssSeverities = Field(alias="cvss_severities")
    cwes: List[Dict[str, Any]] = Field(alias="cwes")
    description: str = Field(alias="description")
    ghsa_id: str = Field(alias="ghsa_id")
    identifiers: List[Dict[str, Any]] = Field(alias="identifiers")
    published_at: str = Field(alias="published_at")
    references: List[Dict[str, Any]] = Field(alias="references")
    severity: str = Field(alias="severity")
    summary: str = Field(alias="summary")
    updated_at: str = Field(alias="updated_at")
    vulnerabilities: List[Dict[str, Any]] = Field(alias="vulnerabilities")
    withdrawn_at: str = Field(alias="withdrawn_at")
    
    class Config:
        populate_by_name = True


class WebhooksSponsorship(BaseModel):
    """WebhooksSponsorship schema from the OpenAPI specification."""
    created_at: str = Field(alias="created_at")
    maintainer: Dict[str, Any] = Field(alias="maintainer")
    node_id: str = Field(alias="node_id")
    privacy_level: str = Field(alias="privacy_level")
    sponsor: Dict[str, Any] = Field(alias="sponsor")
    sponsorable: Dict[str, Any] = Field(alias="sponsorable")
    tier: Dict[str, Any] = Field(alias="tier")  # The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.
    
    class Config:
        populate_by_name = True


class WebhooksChanges8(BaseModel):
    """WebhooksChanges8 schema from the OpenAPI specification."""
    tier: Dict[str, Any] = Field(alias="tier")
    
    class Config:
        populate_by_name = True


class WebhooksTeam1(BaseModel):
    """WebhooksTeam1 schema from the OpenAPI specification."""
    deleted: bool = Field(alias="deleted")
    description: str = Field(alias="description")  # Description of the team
    html_url: str = Field(alias="html_url")
    id_field: int = Field(alias="id")  # Unique identifier of the team
    members_url: str = Field(alias="members_url")
    name: str = Field(alias="name")  # Name of the team
    node_id: str = Field(alias="node_id")
    parent: Dict[str, Any] = Field(alias="parent")
    permission: str = Field(alias="permission")  # Permission that the team will have for its repositories
    privacy: str = Field(alias="privacy")
    notification_setting: str = Field(alias="notification_setting")  # Whether team members will receive notifications when their team is @mentioned
    repositories_url: str = Field(alias="repositories_url")
    slug: str = Field(alias="slug")
    url: str = Field(alias="url")  # URL for the team
    
    class Config:
        populate_by_name = True


class WebhookBranchProtectionConfigurationDisabled(BaseModel):
    """WebhookBranchProtectionConfigurationDisabled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookBranchProtectionConfigurationEnabled(BaseModel):
    """WebhookBranchProtectionConfigurationEnabled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookBranchProtectionRuleCreated(BaseModel):
    """WebhookBranchProtectionRuleCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    rule: WebhooksRule = Field(alias="rule")  # The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookBranchProtectionRuleDeleted(BaseModel):
    """WebhookBranchProtectionRuleDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    rule: WebhooksRule = Field(alias="rule")  # The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookBranchProtectionRuleEdited(BaseModel):
    """WebhookBranchProtectionRuleEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # If the action was `edited`, the changes to the rule.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    rule: WebhooksRule = Field(alias="rule")  # The branch protection rule. Includes a `name` and all the [branch protection settings](https://docs.github.com/github/administering-a-repository/defining-the-mergeability-of-pull-requests/about-protected-branches#about-branch-protection-settings) applied to branches that match the name. Binary settings are boolean. Multi-level configurations are one of `off`, `non_admins`, or `everyone`. Actor and build lists are arrays of strings.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunCompleted(BaseModel):
    """WebhookCheckRunCompleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_run: CheckRunWithSimpleCheckSuite = Field(alias="check_run")  # A check performed on the code of a given code change
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunCompletedFormEncoded(BaseModel):
    """WebhookCheckRunCompletedFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the check_run.completed JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunCreated(BaseModel):
    """WebhookCheckRunCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_run: CheckRunWithSimpleCheckSuite = Field(alias="check_run")  # A check performed on the code of a given code change
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunCreatedFormEncoded(BaseModel):
    """WebhookCheckRunCreatedFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the check_run.created JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunRequestedAction(BaseModel):
    """WebhookCheckRunRequestedAction schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_run: CheckRunWithSimpleCheckSuite = Field(alias="check_run")  # A check performed on the code of a given code change
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requested_action: Dict[str, Any] = Field(alias="requested_action")  # The action requested by the user.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunRequestedActionFormEncoded(BaseModel):
    """WebhookCheckRunRequestedActionFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the check_run.requested_action JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunRerequested(BaseModel):
    """WebhookCheckRunRerequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_run: CheckRunWithSimpleCheckSuite = Field(alias="check_run")  # A check performed on the code of a given code change
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckRunRerequestedFormEncoded(BaseModel):
    """WebhookCheckRunRerequestedFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the check_run.rerequested JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookCheckSuiteCompleted(BaseModel):
    """WebhookCheckSuiteCompleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_suite: Dict[str, Any] = Field(alias="check_suite")  # The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckSuiteRequested(BaseModel):
    """WebhookCheckSuiteRequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_suite: Dict[str, Any] = Field(alias="check_suite")  # The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCheckSuiteRerequested(BaseModel):
    """WebhookCheckSuiteRerequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_suite: Dict[str, Any] = Field(alias="check_suite")  # The [check_suite](https://docs.github.com/rest/checks/suites#get-a-check-suite).
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertAppearedInBranch(BaseModel):
    """WebhookCodeScanningAlertAppearedInBranch schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertClosedByUser(BaseModel):
    """WebhookCodeScanningAlertClosedByUser schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertCreated(BaseModel):
    """WebhookCodeScanningAlertCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertFixed(BaseModel):
    """WebhookCodeScanningAlertFixed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertReopened(BaseModel):
    """WebhookCodeScanningAlertReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCodeScanningAlertReopenedByUser(BaseModel):
    """WebhookCodeScanningAlertReopenedByUser schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The code scanning alert involved in the event.
    commit_oid: str = Field(alias="commit_oid")  # The commit SHA of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")  # The Git reference of the code scanning alert. When the action is `reopened_by_user` or `closed_by_user`, the event was triggered by the `sender` and this value will be empty.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCommitCommentCreated(BaseModel):
    """WebhookCommitCommentCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")  # The action performed. Can be `created`.
    comment: Dict[str, Any] = Field(alias="comment")  # The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCreate(BaseModel):
    """WebhookCreate schema from the OpenAPI specification."""
    description: str = Field(alias="description")  # The repository\'s current description.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    master_branch: str = Field(alias="master_branch")  # The name of the repository\'s default branch (usually `main`).
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pusher_type: str = Field(alias="pusher_type")  # The pusher type for the event. Can be either `user` or a deploy key.
    ref: str = Field(alias="ref")  # The [`git ref`](https://docs.github.com/rest/git/refs#get-a-reference) resource.
    ref_type: str = Field(alias="ref_type")  # The type of Git ref object created in the repository.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCustomPropertyCreated(BaseModel):
    """WebhookCustomPropertyCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    definition: CustomProperty = Field(alias="definition")  # Custom property defined on an organization
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCustomPropertyDeleted(BaseModel):
    """WebhookCustomPropertyDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    definition: Dict[str, Any] = Field(alias="definition")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCustomPropertyPromotedToEnterprise(BaseModel):
    """WebhookCustomPropertyPromotedToEnterprise schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    definition: CustomProperty = Field(alias="definition")  # Custom property defined on an organization
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCustomPropertyUpdated(BaseModel):
    """WebhookCustomPropertyUpdated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    definition: CustomProperty = Field(alias="definition")  # Custom property defined on an organization
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookCustomPropertyValuesUpdated(BaseModel):
    """WebhookCustomPropertyValuesUpdated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    new_property_values: List[CustomPropertyValue] = Field(alias="new_property_values")  # The new custom property values for the repository.
    old_property_values: List[CustomPropertyValue] = Field(alias="old_property_values")  # The old custom property values for the repository.
    
    class Config:
        populate_by_name = True


class WebhookDelete(BaseModel):
    """WebhookDelete schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pusher_type: str = Field(alias="pusher_type")  # The pusher type for the event. Can be either `user` or a deploy key.
    ref: str = Field(alias="ref")  # The [`git ref`](https://docs.github.com/rest/git/refs#get-a-reference) resource.
    ref_type: str = Field(alias="ref_type")  # The type of Git ref object deleted in the repository.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertAutoDismissed(BaseModel):
    """WebhookDependabotAlertAutoDismissed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertAutoReopened(BaseModel):
    """WebhookDependabotAlertAutoReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertCreated(BaseModel):
    """WebhookDependabotAlertCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertDismissed(BaseModel):
    """WebhookDependabotAlertDismissed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertFixed(BaseModel):
    """WebhookDependabotAlertFixed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertReintroduced(BaseModel):
    """WebhookDependabotAlertReintroduced schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDependabotAlertReopened(BaseModel):
    """WebhookDependabotAlertReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: DependabotAlert = Field(alias="alert")  # A Dependabot alert.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDeployKeyCreated(BaseModel):
    """WebhookDeployKeyCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    key: WebhooksDeployKey = Field(alias="key")  # The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) resource.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDeployKeyDeleted(BaseModel):
    """WebhookDeployKeyDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    key: WebhooksDeployKey = Field(alias="key")  # The [`deploy key`](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) resource.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDeploymentCreated(BaseModel):
    """WebhookDeploymentCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    deployment: Dict[str, Any] = Field(alias="deployment")  # The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments).
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: WebhooksWorkflow = Field(alias="workflow")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookDeploymentProtectionRuleRequested(BaseModel):
    """WebhookDeploymentProtectionRuleRequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    environment: str = Field(alias="environment")  # The name of the environment that has the deployment protection rule.
    event: str = Field(alias="event")  # The event that triggered the deployment protection rule.
    deployment_callback_url: str = Field(alias="deployment_callback_url")  # The URL to review the deployment protection rule.
    deployment: Deployment = Field(alias="deployment")  # A request for a specific ref(branch,sha,tag) to be deployed
    pull_requests: List[PullRequest] = Field(alias="pull_requests")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDeploymentReviewApproved(BaseModel):
    """WebhookDeploymentReviewApproved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    approver: WebhooksApprover = Field(alias="approver")
    comment: str = Field(alias="comment")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    reviewers: List[Dict[str, Any]] = Field(alias="reviewers")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    since: str = Field(alias="since")
    workflow_job_run: WebhooksWorkflowJobRun = Field(alias="workflow_job_run")
    workflow_job_runs: List[Dict[str, Any]] = Field(alias="workflow_job_runs")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookDeploymentReviewRejected(BaseModel):
    """WebhookDeploymentReviewRejected schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    approver: WebhooksApprover = Field(alias="approver")
    comment: str = Field(alias="comment")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    reviewers: List[Dict[str, Any]] = Field(alias="reviewers")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    since: str = Field(alias="since")
    workflow_job_run: WebhooksWorkflowJobRun = Field(alias="workflow_job_run")
    workflow_job_runs: List[Dict[str, Any]] = Field(alias="workflow_job_runs")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookDeploymentReviewRequested(BaseModel):
    """WebhookDeploymentReviewRequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    environment: str = Field(alias="environment")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requestor: WebhooksUser = Field(alias="requestor")
    reviewers: List[Dict[str, Any]] = Field(alias="reviewers")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    since: str = Field(alias="since")
    workflow_job_run: Dict[str, Any] = Field(alias="workflow_job_run")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookDeploymentStatusCreated(BaseModel):
    """WebhookDeploymentStatusCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    check_run: Dict[str, Any] = Field(alias="check_run")
    deployment: Dict[str, Any] = Field(alias="deployment")  # The [deployment](https://docs.github.com/rest/deployments/deployments#list-deployments).
    deployment_status: Dict[str, Any] = Field(alias="deployment_status")  # The [deployment status](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses).
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: WebhooksWorkflow = Field(alias="workflow")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookDiscussionAnswered(BaseModel):
    """WebhookDiscussionAnswered schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    answer: WebhooksAnswer = Field(alias="answer")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionCategoryChanged(BaseModel):
    """WebhookDiscussionCategoryChanged schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionClosed(BaseModel):
    """WebhookDiscussionClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionCommentCreated(BaseModel):
    """WebhookDiscussionCommentCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: WebhooksComment = Field(alias="comment")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionCommentDeleted(BaseModel):
    """WebhookDiscussionCommentDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: WebhooksComment = Field(alias="comment")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionCommentEdited(BaseModel):
    """WebhookDiscussionCommentEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    comment: WebhooksComment = Field(alias="comment")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionCreated(BaseModel):
    """WebhookDiscussionCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionDeleted(BaseModel):
    """WebhookDiscussionDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionEdited(BaseModel):
    """WebhookDiscussionEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionLabeled(BaseModel):
    """WebhookDiscussionLabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionLocked(BaseModel):
    """WebhookDiscussionLocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionPinned(BaseModel):
    """WebhookDiscussionPinned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionReopened(BaseModel):
    """WebhookDiscussionReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionTransferred(BaseModel):
    """WebhookDiscussionTransferred schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionUnanswered(BaseModel):
    """WebhookDiscussionUnanswered schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    old_answer: WebhooksAnswer = Field(alias="old_answer")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionUnlabeled(BaseModel):
    """WebhookDiscussionUnlabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionUnlocked(BaseModel):
    """WebhookDiscussionUnlocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookDiscussionUnpinned(BaseModel):
    """WebhookDiscussionUnpinned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    discussion: Discussion = Field(alias="discussion")  # A Discussion in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookFork(BaseModel):
    """WebhookFork schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    forkee: Any = Field(alias="forkee")  # The created [`repository`](https://docs.github.com/rest/repos/repos#get-a-repository) resource.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookGithubAppAuthorizationRevoked(BaseModel):
    """WebhookGithubAppAuthorizationRevoked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookGollum(BaseModel):
    """WebhookGollum schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pages: List[Dict[str, Any]] = Field(alias="pages")  # The pages that were updated.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationCreated(BaseModel):
    """WebhookInstallationCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects that the installation can access.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requester: WebhooksUser = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationDeleted(BaseModel):
    """WebhookInstallationDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects that the installation can access.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requester: Any = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationNewPermissionsAccepted(BaseModel):
    """WebhookInstallationNewPermissionsAccepted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects that the installation can access.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requester: Any = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationRepositoriesAdded(BaseModel):
    """WebhookInstallationRepositoriesAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories_added: List[Dict[str, Any]] = Field(alias="repositories_added")  # An array of repository objects, which were added to the installation.
    repositories_removed: List[Dict[str, Any]] = Field(alias="repositories_removed")  # An array of repository objects, which were removed from the installation.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_selection: str = Field(alias="repository_selection")  # Describe whether all repositories have been selected or there\'s a selection involved
    requester: WebhooksUser = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationRepositoriesRemoved(BaseModel):
    """WebhookInstallationRepositoriesRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories_added: List[Dict[str, Any]] = Field(alias="repositories_added")  # An array of repository objects, which were added to the installation.
    repositories_removed: List[Dict[str, Any]] = Field(alias="repositories_removed")  # An array of repository objects, which were removed from the installation.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_selection: str = Field(alias="repository_selection")  # Describe whether all repositories have been selected or there\'s a selection involved
    requester: WebhooksUser = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationSuspend(BaseModel):
    """WebhookInstallationSuspend schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects that the installation can access.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requester: Any = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookInstallationTargetRenamed(BaseModel):
    """WebhookInstallationTargetRenamed schema from the OpenAPI specification."""
    account: Dict[str, Any] = Field(alias="account")
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    target_type: str = Field(alias="target_type")
    
    class Config:
        populate_by_name = True


class WebhookInstallationUnsuspend(BaseModel):
    """WebhookInstallationUnsuspend schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: Installation = Field(alias="installation")  # Installation
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repositories: List[Dict[str, Any]] = Field(alias="repositories")  # An array of repository objects that the installation can access.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    requester: Any = Field(alias="requester")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssueCommentCreated(BaseModel):
    """WebhookIssueCommentCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: Dict[str, Any] = Field(alias="comment")  # The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Any = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) the comment belongs to.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssueCommentDeleted(BaseModel):
    """WebhookIssueCommentDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: WebhooksIssueComment = Field(alias="comment")  # The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Any = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) the comment belongs to.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssueCommentEdited(BaseModel):
    """WebhookIssueCommentEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksChanges = Field(alias="changes")  # The changes to the comment.
    comment: WebhooksIssueComment = Field(alias="comment")  # The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Any = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) the comment belongs to.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesAssigned(BaseModel):
    """WebhookIssuesAssigned schema from the OpenAPI specification."""
    action: str = Field(alias="action")  # The action that was performed.
    assignee: WebhooksUser = Field(alias="assignee")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesClosed(BaseModel):
    """WebhookIssuesClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")  # The action that was performed.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Any = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesDeleted(BaseModel):
    """WebhookIssuesDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesDemilestoned(BaseModel):
    """WebhookIssuesDemilestoned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    milestone: WebhooksMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesEdited(BaseModel):
    """WebhookIssuesEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the issue.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesLabeled(BaseModel):
    """WebhookIssuesLabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesLocked(BaseModel):
    """WebhookIssuesLocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesMilestoned(BaseModel):
    """WebhookIssuesMilestoned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    milestone: WebhooksMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesOpened(BaseModel):
    """WebhookIssuesOpened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesPinned(BaseModel):
    """WebhookIssuesPinned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue2 = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesReopened(BaseModel):
    """WebhookIssuesReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesTransferred(BaseModel):
    """WebhookIssuesTransferred schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue2 = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesTyped(BaseModel):
    """WebhookIssuesTyped schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    type_field: IssueType = Field(alias="type")  # The type of issue.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesUnassigned(BaseModel):
    """WebhookIssuesUnassigned schema from the OpenAPI specification."""
    action: str = Field(alias="action")  # The action that was performed.
    assignee: WebhooksUserMannequin = Field(alias="assignee")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesUnlabeled(BaseModel):
    """WebhookIssuesUnlabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesUnlocked(BaseModel):
    """WebhookIssuesUnlocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: Dict[str, Any] = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesUnpinned(BaseModel):
    """WebhookIssuesUnpinned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue2 = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookIssuesUntyped(BaseModel):
    """WebhookIssuesUntyped schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    issue: WebhooksIssue = Field(alias="issue")  # The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.
    type_field: IssueType = Field(alias="type")  # The type of issue.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookLabelCreated(BaseModel):
    """WebhookLabelCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookLabelDeleted(BaseModel):
    """WebhookLabelDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookLabelEdited(BaseModel):
    """WebhookLabelEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the label if the action was `edited`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMarketplacePurchaseCancelled(BaseModel):
    """WebhookMarketplacePurchaseCancelled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    marketplace_purchase: WebhooksMarketplacePurchase = Field(alias="marketplace_purchase")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase = Field(alias="previous_marketplace_purchase")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMarketplacePurchaseChanged(BaseModel):
    """WebhookMarketplacePurchaseChanged schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    marketplace_purchase: WebhooksMarketplacePurchase = Field(alias="marketplace_purchase")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    previous_marketplace_purchase: Dict[str, Any] = Field(alias="previous_marketplace_purchase")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMarketplacePurchasePendingChange(BaseModel):
    """WebhookMarketplacePurchasePendingChange schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    marketplace_purchase: WebhooksMarketplacePurchase = Field(alias="marketplace_purchase")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    previous_marketplace_purchase: Dict[str, Any] = Field(alias="previous_marketplace_purchase")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMarketplacePurchasePendingChangeCancelled(BaseModel):
    """WebhookMarketplacePurchasePendingChangeCancelled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    marketplace_purchase: Dict[str, Any] = Field(alias="marketplace_purchase")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase = Field(alias="previous_marketplace_purchase")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMarketplacePurchasePurchased(BaseModel):
    """WebhookMarketplacePurchasePurchased schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    marketplace_purchase: WebhooksMarketplacePurchase = Field(alias="marketplace_purchase")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    previous_marketplace_purchase: WebhooksPreviousMarketplacePurchase = Field(alias="previous_marketplace_purchase")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMemberAdded(BaseModel):
    """WebhookMemberAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    member: WebhooksUser = Field(alias="member")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMemberEdited(BaseModel):
    """WebhookMemberEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the collaborator permissions
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    member: WebhooksUser = Field(alias="member")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMemberRemoved(BaseModel):
    """WebhookMemberRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    member: WebhooksUser = Field(alias="member")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMembershipAdded(BaseModel):
    """WebhookMembershipAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    member: WebhooksUser = Field(alias="member")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    scope: str = Field(alias="scope")  # The scope of the membership. Currently, can only be `team`.
    sender: Dict[str, Any] = Field(alias="sender")
    team: WebhooksTeam = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookMembershipRemoved(BaseModel):
    """WebhookMembershipRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    member: WebhooksUser = Field(alias="member")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    scope: str = Field(alias="scope")  # The scope of the membership. Currently, can only be `team`.
    sender: Dict[str, Any] = Field(alias="sender")
    team: WebhooksTeam = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookMergeGroupChecksRequested(BaseModel):
    """WebhookMergeGroupChecksRequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    merge_group: MergeGroup = Field(alias="merge_group")  # A group of pull requests that the merge queue has grouped together to be merged.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMergeGroupDestroyed(BaseModel):
    """WebhookMergeGroupDestroyed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    reason: str = Field(alias="reason")  # Explains why the merge group is being destroyed. The group could have been merged, removed from the queue (dequeued), or invalidated by an earlier queue entry being dequeued (invalidated).
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    merge_group: MergeGroup = Field(alias="merge_group")  # A group of pull requests that the merge queue has grouped together to be merged.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMetaDeleted(BaseModel):
    """WebhookMetaDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    hook: Dict[str, Any] = Field(alias="hook")  # The deleted webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace.
    hook_id: int = Field(alias="hook_id")  # The id of the modified webhook.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: NullableRepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMilestoneClosed(BaseModel):
    """WebhookMilestoneClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    milestone: WebhooksMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMilestoneCreated(BaseModel):
    """WebhookMilestoneCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    milestone: WebhooksMilestone3 = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMilestoneDeleted(BaseModel):
    """WebhookMilestoneDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    milestone: WebhooksMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMilestoneEdited(BaseModel):
    """WebhookMilestoneEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the milestone if the action was `edited`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    milestone: WebhooksMilestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookMilestoneOpened(BaseModel):
    """WebhookMilestoneOpened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    milestone: WebhooksMilestone3 = Field(alias="milestone")  # A collection of related issues and pull requests.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrgBlockBlocked(BaseModel):
    """WebhookOrgBlockBlocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    blocked_user: WebhooksUser = Field(alias="blocked_user")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrgBlockUnblocked(BaseModel):
    """WebhookOrgBlockUnblocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    blocked_user: WebhooksUser = Field(alias="blocked_user")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrganizationDeleted(BaseModel):
    """WebhookOrganizationDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    membership: WebhooksMembership = Field(alias="membership")  # The membership between the user and the organization. Not present when the action is `member_invited`.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrganizationMemberAdded(BaseModel):
    """WebhookOrganizationMemberAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    membership: WebhooksMembership = Field(alias="membership")  # The membership between the user and the organization. Not present when the action is `member_invited`.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrganizationMemberInvited(BaseModel):
    """WebhookOrganizationMemberInvited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    invitation: Dict[str, Any] = Field(alias="invitation")  # The invitation for the user or email if the action is `member_invited`.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    user: WebhooksUser = Field(alias="user")
    
    class Config:
        populate_by_name = True


class WebhookOrganizationMemberRemoved(BaseModel):
    """WebhookOrganizationMemberRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    membership: WebhooksMembership = Field(alias="membership")  # The membership between the user and the organization. Not present when the action is `member_invited`.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookOrganizationRenamed(BaseModel):
    """WebhookOrganizationRenamed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    membership: WebhooksMembership = Field(alias="membership")  # The membership between the user and the organization. Not present when the action is `member_invited`.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRubygemsMetadata(BaseModel):
    """WebhookRubygemsMetadata schema from the OpenAPI specification."""
    name: str = Field(alias="name")
    description: str = Field(alias="description")
    readme: str = Field(alias="readme")
    homepage: str = Field(alias="homepage")
    version_info: Dict[str, Any] = Field(alias="version_info")
    platform: str = Field(alias="platform")
    metadata: Dict[str, Any] = Field(alias="metadata")
    repo: str = Field(alias="repo")
    dependencies: List[Dict[str, Any]] = Field(alias="dependencies")
    commit_oid: str = Field(alias="commit_oid")
    
    class Config:
        populate_by_name = True


class WebhookPackagePublished(BaseModel):
    """WebhookPackagePublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    package: Dict[str, Any] = Field(alias="package")  # Information about the package.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPackageUpdated(BaseModel):
    """WebhookPackageUpdated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    package: Dict[str, Any] = Field(alias="package")  # Information about the package.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPageBuild(BaseModel):
    """WebhookPageBuild schema from the OpenAPI specification."""
    build: Dict[str, Any] = Field(alias="build")  # The [List GitHub Pages builds](https://docs.github.com/rest/pages/pages#list-github-pages-builds) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    id_field: int = Field(alias="id")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPersonalAccessTokenRequestApproved(BaseModel):
    """WebhookPersonalAccessTokenRequestApproved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    personal_access_token_request: PersonalAccessTokenRequest = Field(alias="personal_access_token_request")  # Details of a Personal Access Token Request.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    
    class Config:
        populate_by_name = True


class WebhookPersonalAccessTokenRequestCancelled(BaseModel):
    """WebhookPersonalAccessTokenRequestCancelled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    personal_access_token_request: PersonalAccessTokenRequest = Field(alias="personal_access_token_request")  # Details of a Personal Access Token Request.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    
    class Config:
        populate_by_name = True


class WebhookPersonalAccessTokenRequestCreated(BaseModel):
    """WebhookPersonalAccessTokenRequestCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    personal_access_token_request: PersonalAccessTokenRequest = Field(alias="personal_access_token_request")  # Details of a Personal Access Token Request.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    
    class Config:
        populate_by_name = True


class WebhookPersonalAccessTokenRequestDenied(BaseModel):
    """WebhookPersonalAccessTokenRequestDenied schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    personal_access_token_request: PersonalAccessTokenRequest = Field(alias="personal_access_token_request")  # Details of a Personal Access Token Request.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    
    class Config:
        populate_by_name = True


class WebhookPing(BaseModel):
    """WebhookPing schema from the OpenAPI specification."""
    hook: Dict[str, Any] = Field(alias="hook")  # The webhook that is being pinged
    hook_id: int = Field(alias="hook_id")  # The ID of the webhook that triggered the ping.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    zen: str = Field(alias="zen")  # Random string of GitHub zen.
    
    class Config:
        populate_by_name = True


class WebhookPingFormEncoded(BaseModel):
    """WebhookPingFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the ping JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookProjectCardConverted(BaseModel):
    """WebhookProjectCardConverted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_card: WebhooksProjectCard = Field(alias="project_card")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectCardCreated(BaseModel):
    """WebhookProjectCardCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_card: WebhooksProjectCard = Field(alias="project_card")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectCardDeleted(BaseModel):
    """WebhookProjectCardDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_card: Dict[str, Any] = Field(alias="project_card")
    repository: NullableRepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectCardEdited(BaseModel):
    """WebhookProjectCardEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_card: WebhooksProjectCard = Field(alias="project_card")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectCardMoved(BaseModel):
    """WebhookProjectCardMoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_card: Any = Field(alias="project_card")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectClosed(BaseModel):
    """WebhookProjectClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project: WebhooksProject = Field(alias="project")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectColumnCreated(BaseModel):
    """WebhookProjectColumnCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_column: WebhooksProjectColumn = Field(alias="project_column")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectColumnDeleted(BaseModel):
    """WebhookProjectColumnDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_column: WebhooksProjectColumn = Field(alias="project_column")
    repository: NullableRepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectColumnEdited(BaseModel):
    """WebhookProjectColumnEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_column: WebhooksProjectColumn = Field(alias="project_column")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectColumnMoved(BaseModel):
    """WebhookProjectColumnMoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project_column: WebhooksProjectColumn = Field(alias="project_column")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectCreated(BaseModel):
    """WebhookProjectCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project: WebhooksProject = Field(alias="project")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectDeleted(BaseModel):
    """WebhookProjectDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project: WebhooksProject = Field(alias="project")
    repository: NullableRepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectEdited(BaseModel):
    """WebhookProjectEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the project if the action was `edited`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project: WebhooksProject = Field(alias="project")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectReopened(BaseModel):
    """WebhookProjectReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    project: WebhooksProject = Field(alias="project")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ProjectClosed(BaseModel):
    """WebhookProjectsV2ProjectClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2: ProjectsV2 = Field(alias="projects_v2")  # A projects v2 project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ProjectCreated(BaseModel):
    """WebhookProjectsV2ProjectCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2: ProjectsV2 = Field(alias="projects_v2")  # A projects v2 project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ProjectDeleted(BaseModel):
    """WebhookProjectsV2ProjectDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2: ProjectsV2 = Field(alias="projects_v2")  # A projects v2 project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ProjectEdited(BaseModel):
    """WebhookProjectsV2ProjectEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2: ProjectsV2 = Field(alias="projects_v2")  # A projects v2 project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemArchived(BaseModel):
    """WebhookProjectsV2ItemArchived schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksProjectChanges = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemConverted(BaseModel):
    """WebhookProjectsV2ItemConverted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemCreated(BaseModel):
    """WebhookProjectsV2ItemCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemDeleted(BaseModel):
    """WebhookProjectsV2ItemDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemEdited(BaseModel):
    """WebhookProjectsV2ItemEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Any = Field(alias="changes")  # The changes made to the item may involve modifications in the item\'s fields and draft issue body.
It includes altered values for text, number, date, single select, and iteration fields, along with the GraphQL node ID of the changed field.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemReordered(BaseModel):
    """WebhookProjectsV2ItemReordered schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ItemRestored(BaseModel):
    """WebhookProjectsV2ItemRestored schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksProjectChanges = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_item: ProjectsV2Item = Field(alias="projects_v2_item")  # An item belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2ProjectReopened(BaseModel):
    """WebhookProjectsV2ProjectReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2: ProjectsV2 = Field(alias="projects_v2")  # A projects v2 project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2StatusUpdateCreated(BaseModel):
    """WebhookProjectsV2StatusUpdateCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_status_update: ProjectsV2StatusUpdate = Field(alias="projects_v2_status_update")  # An status update belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2StatusUpdateDeleted(BaseModel):
    """WebhookProjectsV2StatusUpdateDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_status_update: ProjectsV2StatusUpdate = Field(alias="projects_v2_status_update")  # An status update belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookProjectsV2StatusUpdateEdited(BaseModel):
    """WebhookProjectsV2StatusUpdateEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    projects_v2_status_update: ProjectsV2StatusUpdate = Field(alias="projects_v2_status_update")  # An status update belonging to a project
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPublic(BaseModel):
    """WebhookPublic schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestAssigned(BaseModel):
    """WebhookPullRequestAssigned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    assignee: WebhooksUser = Field(alias="assignee")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestAutoMergeDisabled(BaseModel):
    """WebhookPullRequestAutoMergeDisabled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    reason: str = Field(alias="reason")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestAutoMergeEnabled(BaseModel):
    """WebhookPullRequestAutoMergeEnabled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    reason: str = Field(alias="reason")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestClosed(BaseModel):
    """WebhookPullRequestClosed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestConvertedToDraft(BaseModel):
    """WebhookPullRequestConvertedToDraft schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestDemilestoned(BaseModel):
    """WebhookPullRequestDemilestoned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    milestone: Milestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: WebhooksPullRequest5 = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestDequeued(BaseModel):
    """WebhookPullRequestDequeued schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    reason: str = Field(alias="reason")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestEdited(BaseModel):
    """WebhookPullRequestEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the comment if the action was `edited`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestEnqueued(BaseModel):
    """WebhookPullRequestEnqueued schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestLabeled(BaseModel):
    """WebhookPullRequestLabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestLocked(BaseModel):
    """WebhookPullRequestLocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestMilestoned(BaseModel):
    """WebhookPullRequestMilestoned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    milestone: Milestone = Field(alias="milestone")  # A collection of related issues and pull requests.
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: WebhooksPullRequest5 = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestOpened(BaseModel):
    """WebhookPullRequestOpened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReadyForReview(BaseModel):
    """WebhookPullRequestReadyForReview schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReopened(BaseModel):
    """WebhookPullRequestReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: PullRequestWebhook = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewCommentCreated(BaseModel):
    """WebhookPullRequestReviewCommentCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: Dict[str, Any] = Field(alias="comment")  # The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewCommentDeleted(BaseModel):
    """WebhookPullRequestReviewCommentDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    comment: WebhooksReviewComment = Field(alias="comment")  # The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewCommentEdited(BaseModel):
    """WebhookPullRequestReviewCommentEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksChanges = Field(alias="changes")  # The changes to the comment.
    comment: WebhooksReviewComment = Field(alias="comment")  # The [comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) itself.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewDismissed(BaseModel):
    """WebhookPullRequestReviewDismissed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    review: Dict[str, Any] = Field(alias="review")  # The review that was affected.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewEdited(BaseModel):
    """WebhookPullRequestReviewEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    review: WebhooksReview = Field(alias="review")  # The review that was affected.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewSubmitted(BaseModel):
    """WebhookPullRequestReviewSubmitted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    review: WebhooksReview = Field(alias="review")  # The review that was affected.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewThreadResolved(BaseModel):
    """WebhookPullRequestReviewThreadResolved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    thread: Dict[str, Any] = Field(alias="thread")
    
    class Config:
        populate_by_name = True


class WebhookPullRequestReviewThreadUnresolved(BaseModel):
    """WebhookPullRequestReviewThreadUnresolved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    thread: Dict[str, Any] = Field(alias="thread")
    
    class Config:
        populate_by_name = True


class WebhookPullRequestSynchronize(BaseModel):
    """WebhookPullRequestSynchronize schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    after: str = Field(alias="after")
    before: str = Field(alias="before")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestUnassigned(BaseModel):
    """WebhookPullRequestUnassigned schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    assignee: WebhooksUserMannequin = Field(alias="assignee")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestUnlabeled(BaseModel):
    """WebhookPullRequestUnlabeled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    label: WebhooksLabel = Field(alias="label")
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPullRequestUnlocked(BaseModel):
    """WebhookPullRequestUnlocked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    number: int = Field(alias="number")  # The pull request number.
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pull_request: Dict[str, Any] = Field(alias="pull_request")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookPush(BaseModel):
    """WebhookPush schema from the OpenAPI specification."""
    after: str = Field(alias="after")  # The SHA of the most recent commit on `ref` after the push.
    base_ref: str = Field(alias="base_ref")
    before: str = Field(alias="before")  # The SHA of the most recent commit on `ref` before the push.
    commits: List[Dict[str, Any]] = Field(alias="commits")  # An array of commit objects describing the pushed commits. (Pushed commits are all commits that are included in the `compare` between the `before` commit and the `after` commit.) The array includes a maximum of 2048 commits. If necessary, you can use the [Commits API](https://docs.github.com/rest/commits) to fetch additional commits.
    compare: str = Field(alias="compare")  # URL that shows the changes in this `ref` update, from the `before` commit to the `after` commit. For a newly created `ref` that is directly based on the default branch, this is the comparison between the head of the default branch and the `after` commit. Otherwise, this shows all commits until the `after` commit.
    created: bool = Field(alias="created")  # Whether this push created the `ref`.
    deleted: bool = Field(alias="deleted")  # Whether this push deleted the `ref`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    forced: bool = Field(alias="forced")  # Whether this push was a force push of the `ref`.
    head_commit: Dict[str, Any] = Field(alias="head_commit")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    pusher: Dict[str, Any] = Field(alias="pusher")  # Metaproperties for Git author/committer information.
    ref: str = Field(alias="ref")  # The full git ref that was pushed. Example: `refs/heads/main` or `refs/tags/v3.14.1`.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRegistryPackagePublished(BaseModel):
    """WebhookRegistryPackagePublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    registry_package: Dict[str, Any] = Field(alias="registry_package")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRegistryPackageUpdated(BaseModel):
    """WebhookRegistryPackageUpdated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    registry_package: Dict[str, Any] = Field(alias="registry_package")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleaseCreated(BaseModel):
    """WebhookReleaseCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleaseDeleted(BaseModel):
    """WebhookReleaseDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleaseEdited(BaseModel):
    """WebhookReleaseEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleasePrereleased(BaseModel):
    """WebhookReleasePrereleased schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: Dict[str, Any] = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleasePublished(BaseModel):
    """WebhookReleasePublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease1 = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleaseReleased(BaseModel):
    """WebhookReleaseReleased schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookReleaseUnpublished(BaseModel):
    """WebhookReleaseUnpublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    release: WebhooksRelease1 = Field(alias="release")  # The [release](https://docs.github.com/rest/releases/releases/#get-a-release) object.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryAdvisoryPublished(BaseModel):
    """WebhookRepositoryAdvisoryPublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_advisory: RepositoryAdvisory = Field(alias="repository_advisory")  # A repository security advisory.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryAdvisoryReported(BaseModel):
    """WebhookRepositoryAdvisoryReported schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_advisory: RepositoryAdvisory = Field(alias="repository_advisory")  # A repository security advisory.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryArchived(BaseModel):
    """WebhookRepositoryArchived schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryCreated(BaseModel):
    """WebhookRepositoryCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryDeleted(BaseModel):
    """WebhookRepositoryDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryDispatchSample(BaseModel):
    """WebhookRepositoryDispatchSample schema from the OpenAPI specification."""
    action: str = Field(alias="action")  # The `event_type` that was specified in the `POST /repos/{owner}/{repo}/dispatches` request body.
    branch: str = Field(alias="branch")
    client_payload: Dict[str, Any] = Field(alias="client_payload")  # The `client_payload` that was specified in the `POST /repos/{owner}/{repo}/dispatches` request body.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryEdited(BaseModel):
    """WebhookRepositoryEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryImport(BaseModel):
    """WebhookRepositoryImport schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    status: str = Field(alias="status")
    
    class Config:
        populate_by_name = True


class WebhookRepositoryPrivatized(BaseModel):
    """WebhookRepositoryPrivatized schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryPublicized(BaseModel):
    """WebhookRepositoryPublicized schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryRenamed(BaseModel):
    """WebhookRepositoryRenamed schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryRulesetCreated(BaseModel):
    """WebhookRepositoryRulesetCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_ruleset: RepositoryRuleset = Field(alias="repository_ruleset")  # A set of rules to apply when specified conditions are met.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryRulesetDeleted(BaseModel):
    """WebhookRepositoryRulesetDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_ruleset: RepositoryRuleset = Field(alias="repository_ruleset")  # A set of rules to apply when specified conditions are met.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryRulesetEdited(BaseModel):
    """WebhookRepositoryRulesetEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    repository_ruleset: RepositoryRuleset = Field(alias="repository_ruleset")  # A set of rules to apply when specified conditions are met.
    changes: Dict[str, Any] = Field(alias="changes")
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryTransferred(BaseModel):
    """WebhookRepositoryTransferred schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryUnarchived(BaseModel):
    """WebhookRepositoryUnarchived schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryVulnerabilityAlertCreate(BaseModel):
    """WebhookRepositoryVulnerabilityAlertCreate schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: WebhooksAlert = Field(alias="alert")  # The security alert of the vulnerable dependency.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryVulnerabilityAlertDismiss(BaseModel):
    """WebhookRepositoryVulnerabilityAlertDismiss schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The security alert of the vulnerable dependency.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryVulnerabilityAlertReopen(BaseModel):
    """WebhookRepositoryVulnerabilityAlertReopen schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: WebhooksAlert = Field(alias="alert")  # The security alert of the vulnerable dependency.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookRepositoryVulnerabilityAlertResolve(BaseModel):
    """WebhookRepositoryVulnerabilityAlertResolve schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: Dict[str, Any] = Field(alias="alert")  # The security alert of the vulnerable dependency.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertCreated(BaseModel):
    """WebhookSecretScanningAlertCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertLocationCreated(BaseModel):
    """WebhookSecretScanningAlertLocationCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    location: SecretScanningLocation = Field(alias="location")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertLocationCreatedFormEncoded(BaseModel):
    """WebhookSecretScanningAlertLocationCreatedFormEncoded schema from the OpenAPI specification."""
    payload: str = Field(alias="payload")  # A URL-encoded string of the secret_scanning_alert_location.created JSON payload. The decoded payload is a JSON object.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertPubliclyLeaked(BaseModel):
    """WebhookSecretScanningAlertPubliclyLeaked schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertReopened(BaseModel):
    """WebhookSecretScanningAlertReopened schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertResolved(BaseModel):
    """WebhookSecretScanningAlertResolved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningAlertValidated(BaseModel):
    """WebhookSecretScanningAlertValidated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    alert: SecretScanningAlertWebhook = Field(alias="alert")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecretScanningScanCompleted(BaseModel):
    """WebhookSecretScanningScanCompleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    type_field: str = Field(alias="type")  # What type of scan was completed
    source: str = Field(alias="source")  # What type of content was scanned
    started_at: str = Field(alias="started_at")  # The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    completed_at: str = Field(alias="completed_at")  # The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    secret_types: List[str] = Field(alias="secret_types")  # List of patterns that were updated. This will be empty for normal backfill scans or custom pattern updates
    custom_pattern_name: str = Field(alias="custom_pattern_name")  # If the scan was triggered by a custom pattern update, this will be the name of the pattern that was updated
    custom_pattern_scope: str = Field(alias="custom_pattern_scope")  # If the scan was triggered by a custom pattern update, this will be the scope of the pattern that was updated
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecurityAdvisoryPublished(BaseModel):
    """WebhookSecurityAdvisoryPublished schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    security_advisory: WebhooksSecurityAdvisory = Field(alias="security_advisory")  # The details of the security advisory, including summary, description, and severity.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecurityAdvisoryUpdated(BaseModel):
    """WebhookSecurityAdvisoryUpdated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    security_advisory: WebhooksSecurityAdvisory = Field(alias="security_advisory")  # The details of the security advisory, including summary, description, and severity.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecurityAdvisoryWithdrawn(BaseModel):
    """WebhookSecurityAdvisoryWithdrawn schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    security_advisory: Dict[str, Any] = Field(alias="security_advisory")  # The details of the security advisory, including summary, description, and severity.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSecurityAndAnalysis(BaseModel):
    """WebhookSecurityAndAnalysis schema from the OpenAPI specification."""
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: FullRepository = Field(alias="repository")  # Full Repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipCancelled(BaseModel):
    """WebhookSponsorshipCancelled schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipCreated(BaseModel):
    """WebhookSponsorshipCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipEdited(BaseModel):
    """WebhookSponsorshipEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipPendingCancellation(BaseModel):
    """WebhookSponsorshipPendingCancellation schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    effective_date: str = Field(alias="effective_date")  # The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipPendingTierChange(BaseModel):
    """WebhookSponsorshipPendingTierChange schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksChanges8 = Field(alias="changes")
    effective_date: str = Field(alias="effective_date")  # The `pending_cancellation` and `pending_tier_change` event types will include the date the cancellation or tier change will take effect.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookSponsorshipTierChanged(BaseModel):
    """WebhookSponsorshipTierChanged schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: WebhooksChanges8 = Field(alias="changes")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sponsorship: WebhooksSponsorship = Field(alias="sponsorship")
    
    class Config:
        populate_by_name = True


class WebhookStarCreated(BaseModel):
    """WebhookStarCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    starred_at: str = Field(alias="starred_at")  # The time the star was created. This is a timestamp in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. Will be `null` for the `deleted` action.
    
    class Config:
        populate_by_name = True


class WebhookStarDeleted(BaseModel):
    """WebhookStarDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    starred_at: Any = Field(alias="starred_at")  # The time the star was created. This is a timestamp in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. Will be `null` for the `deleted` action.
    
    class Config:
        populate_by_name = True


class WebhookStatus(BaseModel):
    """WebhookStatus schema from the OpenAPI specification."""
    avatar_url: str = Field(alias="avatar_url")
    branches: List[Dict[str, Any]] = Field(alias="branches")  # An array of branch objects containing the status\' SHA. Each branch contains the given SHA, but the SHA may or may not be the head of the branch. The array includes a maximum of 10 branches.
    commit: Dict[str, Any] = Field(alias="commit")
    context: str = Field(alias="context")
    created_at: str = Field(alias="created_at")
    description: str = Field(alias="description")  # The optional human-readable description added to the status.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    id_field: int = Field(alias="id")  # The unique identifier of the status.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    name: str = Field(alias="name")
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    sha: str = Field(alias="sha")  # The Commit SHA.
    state: str = Field(alias="state")  # The new state. Can be `pending`, `success`, `failure`, or `error`.
    target_url: str = Field(alias="target_url")  # The optional link added to the status.
    updated_at: str = Field(alias="updated_at")
    
    class Config:
        populate_by_name = True


class WebhookSubIssuesParentIssueAdded(BaseModel):
    """WebhookSubIssuesParentIssueAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    parent_issue_id: float = Field(alias="parent_issue_id")  # The ID of the parent issue.
    parent_issue: Issue = Field(alias="parent_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    parent_issue_repo: Repository = Field(alias="parent_issue_repo")  # A repository on GitHub.
    sub_issue_id: float = Field(alias="sub_issue_id")  # The ID of the sub-issue.
    sub_issue: Issue = Field(alias="sub_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSubIssuesParentIssueRemoved(BaseModel):
    """WebhookSubIssuesParentIssueRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    parent_issue_id: float = Field(alias="parent_issue_id")  # The ID of the parent issue.
    parent_issue: Issue = Field(alias="parent_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    parent_issue_repo: Repository = Field(alias="parent_issue_repo")  # A repository on GitHub.
    sub_issue_id: float = Field(alias="sub_issue_id")  # The ID of the sub-issue.
    sub_issue: Issue = Field(alias="sub_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSubIssuesSubIssueAdded(BaseModel):
    """WebhookSubIssuesSubIssueAdded schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    sub_issue_id: float = Field(alias="sub_issue_id")  # The ID of the sub-issue.
    sub_issue: Issue = Field(alias="sub_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    sub_issue_repo: Repository = Field(alias="sub_issue_repo")  # A repository on GitHub.
    parent_issue_id: float = Field(alias="parent_issue_id")  # The ID of the parent issue.
    parent_issue: Issue = Field(alias="parent_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookSubIssuesSubIssueRemoved(BaseModel):
    """WebhookSubIssuesSubIssueRemoved schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    sub_issue_id: float = Field(alias="sub_issue_id")  # The ID of the sub-issue.
    sub_issue: Issue = Field(alias="sub_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    sub_issue_repo: Repository = Field(alias="sub_issue_repo")  # A repository on GitHub.
    parent_issue_id: float = Field(alias="parent_issue_id")  # The ID of the parent issue.
    parent_issue: Issue = Field(alias="parent_issue")  # Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookTeamAdd(BaseModel):
    """WebhookTeamAdd schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookTeamAddedToRepository(BaseModel):
    """WebhookTeamAddedToRepository schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookTeamCreated(BaseModel):
    """WebhookTeamCreated schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookTeamDeleted(BaseModel):
    """WebhookTeamDeleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookTeamEdited(BaseModel):
    """WebhookTeamEdited schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    changes: Dict[str, Any] = Field(alias="changes")  # The changes to the team if the action was `edited`.
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookTeamRemovedFromRepository(BaseModel):
    """WebhookTeamRemovedFromRepository schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: Dict[str, Any] = Field(alias="repository")  # A git repository
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    team: WebhooksTeam1 = Field(alias="team")  # Groups of organization members that gives permissions on specified repositories.
    
    class Config:
        populate_by_name = True


class WebhookWatchStarted(BaseModel):
    """WebhookWatchStarted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    
    class Config:
        populate_by_name = True


class WebhookWorkflowDispatch(BaseModel):
    """WebhookWorkflowDispatch schema from the OpenAPI specification."""
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    inputs: Dict[str, Any] = Field(alias="inputs")
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    ref: str = Field(alias="ref")
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: str = Field(alias="workflow")
    
    class Config:
        populate_by_name = True


class WebhookWorkflowJobCompleted(BaseModel):
    """WebhookWorkflowJobCompleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow_job: Any = Field(alias="workflow_job")
    deployment: Deployment = Field(alias="deployment")  # A request for a specific ref(branch,sha,tag) to be deployed
    
    class Config:
        populate_by_name = True


class WebhookWorkflowJobInProgress(BaseModel):
    """WebhookWorkflowJobInProgress schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow_job: Any = Field(alias="workflow_job")
    deployment: Deployment = Field(alias="deployment")  # A request for a specific ref(branch,sha,tag) to be deployed
    
    class Config:
        populate_by_name = True


class WebhookWorkflowJobQueued(BaseModel):
    """WebhookWorkflowJobQueued schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow_job: Dict[str, Any] = Field(alias="workflow_job")
    deployment: Deployment = Field(alias="deployment")  # A request for a specific ref(branch,sha,tag) to be deployed
    
    class Config:
        populate_by_name = True


class WebhookWorkflowJobWaiting(BaseModel):
    """WebhookWorkflowJobWaiting schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow_job: Dict[str, Any] = Field(alias="workflow_job")
    deployment: Deployment = Field(alias="deployment")  # A request for a specific ref(branch,sha,tag) to be deployed
    
    class Config:
        populate_by_name = True


class WebhookWorkflowRunCompleted(BaseModel):
    """WebhookWorkflowRunCompleted schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: WebhooksWorkflow = Field(alias="workflow")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookWorkflowRunInProgress(BaseModel):
    """WebhookWorkflowRunInProgress schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: WebhooksWorkflow = Field(alias="workflow")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True


class WebhookWorkflowRunRequested(BaseModel):
    """WebhookWorkflowRunRequested schema from the OpenAPI specification."""
    action: str = Field(alias="action")
    enterprise: EnterpriseWebhooks = Field(alias="enterprise")  # An enterprise on GitHub. Webhook payloads contain the `enterprise` property when the webhook is configured
on an enterprise account or an organization that\'s part of an enterprise account. For more information,
see \"[About enterprise accounts](https://docs.github.com/admin/overview/about-enterprise-accounts).\"
    installation: SimpleInstallation = Field(alias="installation")  # The GitHub App installation. Webhook payloads contain the `installation` property when the event is configured
for and sent to a GitHub App. For more information,
see \"[Using webhooks with GitHub Apps](https://docs.github.com/apps/creating-github-apps/registering-a-github-app/using-webhooks-with-github-apps).\"
    organization: OrganizationSimpleWebhooks = Field(alias="organization")  # A GitHub organization. Webhook payloads contain the `organization` property when the webhook is configured for an
organization, or when the event occurs from activity in a repository owned by an organization.
    repository: RepositoryWebhooks = Field(alias="repository")  # The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property
when the event occurs from activity in a repository.
    sender: SimpleUser = Field(alias="sender")  # A GitHub user.
    workflow: WebhooksWorkflow = Field(alias="workflow")
    workflow_run: Dict[str, Any] = Field(alias="workflow_run")
    
    class Config:
        populate_by_name = True