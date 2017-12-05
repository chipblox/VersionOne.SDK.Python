
import urllib
import yaml

def encode_v1_whereterm(input):
    return input.replace("'", "''").replace('"', '""')

def single_or_list(input, separator=','):
    if isinstance(input, list):
        return separator.join(input)
    else:
        return str(input)

def where_terms(data):
    if "where" in data.keys():
        for attrname, value in data['where'].items(): 
            yield("%s='%s'"%(attrname, encode_v1_whereterm(value)))

    if "filter" in data.keys():
        filter = data['filter']
        if isinstance(filter, list):
          for term in filter:
            yield(term)
        else:
          yield(filter)

def query_params(data):
    wherestring = ';'.join(where_terms(data))
    if wherestring:
        yield('where', wherestring)

    if "select" in data.keys():
        yield('sel', single_or_list(data['select']))

    if 'asof' in data.keys():
        yield('asof', data['asof'])

    if 'sort' in data.keys():
        yield('sort', single_or_list(data['sort']))

    if 'page' in data.keys():
        yield('page', "%(size)d,%(start)d"%data['page'])

    if 'find' in data.keys():
        yield('find', data['find'])

    if 'findin' in data.keys():
        yield('findin', single_or_list(data['findin']))

    if 'op' in data.keys():
        yield('op', data['op'])  


def query_from_yaml(yamlstring):
    data = yaml.load(yamlstring)
    if data and 'from' in data.keys():
        path = '/' + urllib.quote(data['from'])
        url = path + '?' + urllib.urlencode(list(query_params(data)))
        return url
    raise Exception("Invalid yaml output: " + str(data))



code = """
  from: Story
  select:
    - Scope.Name
    - Name
    - Estimate
    - CreateDateUTC
    - Owner[OwnedWorkitems.@Count<'']
  where:
    SuperMeAndUp.Name: All Projects
  filter:
    - Estimate>='5'
  asof: 2012-01-01 01:01:01
  sort:
    - +Name
    - -Estimate
  page:
    size: 100
    start: 0
  find: Joe
  findin:
    - Name
    - Description
  op: Delete
"""

print query_from_yaml(code)

