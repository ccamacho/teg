#!/usr/bin/python

"""
Copyright 2019 Pystol (pystol.org).

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at:

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


import os
from kubernetes import config


def load_kubernetes_config():
    """
    Load the initial config details.
    We load the config depending where we execute the code from
    """
    try:
        if 'KUBERNETES_PORT' in os.environ:
            # We set up the client from within a k8s pod
            config.load_incluster_config()
        elif 'KUBECONFIG' in os.environ:
            config.load_kube_config(os.getenv('KUBECONFIG'))
        else:
            config.load_kube_config()
    except Exception as e:
        message = ("---\n"
                   "The Python Kubernetes client could not be configured "
                   "at this time.\n"
                   "You need a working Kubernetes deployment to make "
                   "Pystol work.\n"
                   "Check the following:\n"
                   "Use the env var KUBECONFIG with the path to your K8s "
                   "config file like:\n"
                   "    export KUBECONFIG=~/.kube/config\n"
                   "Or run Pystol from within the cluster to make use of "
                   "load_incluster_config.\n"
                   "Error: ")
        print(message)
        raise e
