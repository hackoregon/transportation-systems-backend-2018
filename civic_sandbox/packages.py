packages = {   
  'Transportation': {
    'description': '',
    #'Transporation Package',
    'foundations' : ['042'],
    'default_foundation' : '042',
    'slides' : ['031', '032', '015'],
    'default_slide' : ['031', '032', '015',]
    },
}

slides = {
  '015': {
    'name': 'Change in Ridership by Route',
    'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/routechange/',
    'visualization': 'PathMap',
  },
  '031': {
    'name': 'Safety Hotline',
    'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/safetyhotline/',
    'visualization': 'ScatterPlotMap',
  },
  '032': {
    'name': 'Crashes',
    'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/crashes/',
    'visualization': 'ScatterPlotMap',
  },
}

foundations = {
  '042': {
    'name': 'Change in Ridership by Census Block',
    'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/foundations/blockchange/',
    'visualization': 'ChoroplethMap',
  },
}

package_info = {
    'packages' : packages,
    'slides' : slides,
    'foundations' : foundations
    }