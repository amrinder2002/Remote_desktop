import os
import sys
from unittest import mock
import pytest

# Mock pyautogui before importing Server to avoid DISPLAY issues
sys.modules['pyautogui'] = mock.MagicMock()

from Server import executeCommand


def test_execute_command_echo_hello():
    output = executeCommand('echo hello')
    assert 'hello' in output.lower()
