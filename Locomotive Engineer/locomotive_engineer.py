"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagon_list):
    return list(wagon_list)

#---------------------------------------------------------------------------------------

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    first_two = each_wagons_id[:2]
    each_wagons_id = each_wagons_id[2:]
    new_wagon_id = [*each_wagons_id, *first_two]

    new_wagon_id[1:1] = missing_wagons

    return new_wagon_id

#---------------------------------------------------------------------------------------

def add_missing_stops(route, **stops):
    stop = []
    for k, v in stops.items():
        stop.append(v)

    route["stops"] = stop
    return route

#---------------------------------------------------------------------------------------

def extend_route_information(route, more_route_information):
    route.update(more_route_information)
    return route

#---------------------------------------------------------------------------------------

def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]
