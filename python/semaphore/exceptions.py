# !usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-12-05 12:01:21
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-12-05 12:19:32

from __future__ import print_function, division, absolute_import


class SemaphoreError(Exception):
    """A custom core Semaphore exception"""

    def __init__(self, message=None):

        message = 'There has been an error' \
            if not message else message

        super(SemaphoreError, self).__init__(message)


class SemaphoreNotImplemented(SemaphoreError):
    """A custom exception for not yet implemented features."""

    def __init__(self, message=None):

        message = 'This feature is not implemented yet.' \
            if not message else message

        super(SemaphoreNotImplemented, self).__init__(message)


class SemaphoreAPIError(SemaphoreError):
    """A custom exception for API errors"""

    def __init__(self, message=None):
        if not message:
            message = 'Error with Http Response from Semaphore API'
        else:
            message = 'Http response error from Semaphore API. {0}'.format(message)

        super(SemaphoreAPIError, self).__init__(message)


class SemaphoreApiAuthError(SemaphoreAPIError):
    """A custom exception for API authentication errors"""
    pass


class SemaphoreMissingDependency(SemaphoreError):
    """A custom exception for missing dependencies."""
    pass


class SemaphoreWarning(Warning):
    """Base warning for Semaphore."""


class SemaphoreUserWarning(UserWarning, SemaphoreWarning):
    """The primary warning class."""
    pass


class SemaphoreSkippedTestWarning(SemaphoreUserWarning):
    """A warning for when a test is skipped."""
    pass


class SemaphoreDeprecationWarning(SemaphoreUserWarning):
    """A warning for deprecated features."""
    pass
