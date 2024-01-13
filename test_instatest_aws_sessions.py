import unittest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone

from instatest_aws_sessions import EnvironmentMock, Wrapper, ProjectConfiguration


class TestWrapper(unittest.TestCase):

    def setUp(self):
        self.env1 = EnvironmentMock()
        self.mock_sts_client_response = {
            'Credentials': {
                'AccessKeyId': 'test_AccessKeyId',
                'SecretAccessKey': 'test_SecretAccessKey',
                'SessionToken': 'test_SessionToken',
                'Expiration': datetime.now(timezone.utc) + timedelta(
                    seconds=ProjectConfiguration.Wrapper_DEFAULT_CACHE_DURATION)
            }
        }

    def tearDown(self):
        Wrapper._clean_cached_session()

    def is_valid_session(self, session):
        self.assertIsNotNone(session.get_credentials())
        self.assertIsNotNone(session.get_credentials().token)
        self.assertEquals(self.mock_sts_client_response['Credentials']['SessionToken'], session.get_credentials().token)

    def test_init_class(self):
        pass

    @patch('boto3.Session.client')
    def test_get_session_without_mfa(self, mock_client):
        mock_client.return_value.get_session_token.return_value = self.mock_sts_client_response
        mock_client.return_value.assume_role.return_value = self.mock_sts_client_response

        session = Wrapper.get_session(self.env1)
        self.assertTrue(mock_client.called)
        self.is_valid_session(session)

    @patch('boto3.Session.client')
    def test_get_disk_cache_without_mfa_session(self, mock_client):
        mock_client.return_value.get_session_token.return_value = self.mock_sts_client_response
        mock_client.return_value.assume_role.return_value = self.mock_sts_client_response

        without_mfa_session = Wrapper.get_session(self.env1)
        cached_session = Wrapper.get_session(self.env1)
        self.is_valid_session(without_mfa_session)
        self.is_valid_session(cached_session)
        self.assertTrue(Wrapper._role_session_cache)
        self.assertEquals(without_mfa_session.get_credentials().token, cached_session.get_credentials().token)

    def test_get_session_with_mfa(self):
        pass

    def test_get_disk_cache_with_mfa_session(self):
        pass

    def test_renew_disk_cache_when_session_expire(self):
        pass


if __name__ == '__main__':
    unittest.main()
