from flask import Flask, Blueprint


class NodeServer(Flask):
    """ Override for future overriding """


class NodeModule(Blueprint):
    """ Override default blueprint """


class StackApp(Flask):
    """ Base class for application """


class StackAppModule(Blueprint):
    """ Base class for applications module """