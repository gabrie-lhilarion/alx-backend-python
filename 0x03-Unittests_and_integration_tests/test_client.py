#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class in client module."""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_result, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_result
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self):
        """
            Test that GithubOrgClient._public_repos_url
            returns the correct URL.
        """
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            client = GithubOrgClient("google")

            result = client._public_repos_url

            self.assertEqual(
                result, "https://api.github.com/orgs/google/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
            Test that GithubOrgClient.public_repos
            returns the correct list of repos.
        """
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = mock_payload

        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_public_repos_url:
            the_url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = the_url
            client = GithubOrgClient("google")

            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
            Test that GithubOrgClient.has_license
            returns the correct boolean value.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test case for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class by mocking requests.get."""
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.get_side_effect
        )
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """
            Side effect function for requests.get
            to return the correct payloads.
        """
        if url == f"https://api.github.com/orgs/google":
            return Mock(**{'json.return_value': fixtures.org_payload})
        elif url == fixtures.org_payload["repos_url"]:
            return Mock(**{'json.return_value': fixtures.repos_payload})
        return Mock(**{'json.return_value': {}})

    def test_public_repos(self):
        """
            Test the public_repos method returns
            the correct list of repos.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(), fixtures.expected_repos
        )

    def test_public_repos_with_license(self):
        """
            Test the public_repos method returns
            repos with a specific license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), fixtures.apache2_repos
        )
