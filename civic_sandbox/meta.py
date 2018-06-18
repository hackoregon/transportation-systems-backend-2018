
safety_hotline_meta = {
  'attributes': {
    'primary': {
      'field': 'description',
      'name': 'Description',
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': 'date_created',
    'date_granularity': 'year',
    'default_date_filter': '2017',
    'min_date': '2008', 
    'max_date': '2018'
    },
  }


crash_meta = {
  'attributes': {
    'primary': {
      'field': None,
      'name': None,
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': 'crash_dt',
    'date_granularity': 'year',
    'default_date_filter': '2014',
    'min_date': '2004', 
    'max_date': '2014'
    },
  }

block_change_meta = {
  'attributes': {
    'primary': {
      'field': 'pct_change',
      'name': 'Ridership Change from 2009 to 2017',
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None,
    'date_granularity': None,
    'default_date_filter': '2017',
    'min_date': None, 
    'max_date': None
    },
  }

route_change_meta = {
  'attributes': {
    'primary': {
      'field': 'stops_pct_change',
      'name': 'Ridership Change from 2009 to 2017',
    },
    'secondary': {
      'field': None,
      'name': None,
    },
  },
    'dates': {
    'date_attribute': None,
    'date_granularity': None,
    'default_date_filter': '2017',
    'min_date': None, 
    'max_date': None
    },
  }
