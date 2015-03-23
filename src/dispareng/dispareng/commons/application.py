from flask import Flask, Blueprint


class DServer(Flask):
    """ Override for future overriding """


class DServerModule(Blueprint):
    """ Override default blueprint """


class DApp(Flask):
    """ Base class for application """


class DAppModule(Blueprint):
    """ Base class for applications module """