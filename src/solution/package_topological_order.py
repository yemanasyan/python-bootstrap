from typing import Optional


def get_package_installation_order(dependencies: list) -> Optional[list[str]]:
    graph = dict()
    for package, dependency in dependencies:
        if package not in graph:
            graph[package] = (set(), set())

        if dependency not in graph:
            graph[dependency] = (set(), set())

        # second item in the tuple is the dependencies
        graph[package][1].add(dependency)
        # first item in the tuple is the dependents
        graph[dependency][0].add(package)

    package_installation_order = list()
    for package in list(graph.keys()):
        if package not in graph:
            continue

        dependents, dependencies = graph[package]
        if len(dependencies) == 0:
            _remove_package(package, graph, dependents, package_installation_order)

    return package_installation_order if len(graph) == 0 else None


def _remove_package(package, grap, dependents, package_installation_order):
    grap.pop(package)
    package_installation_order.append(package)

    for dependent in dependents:
        dependent_dependents, dependent_dependencies = grap[dependent]
        dependent_dependencies.remove(package)
        if len(dependent_dependencies) == 0:
            _remove_package(dependent, grap, dependent_dependents, package_installation_order)

