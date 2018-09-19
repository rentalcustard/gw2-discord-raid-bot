BUILDS = {
        'thief': {
                'cdps': 'https://snowcrows.com/raids/builds/thief/daredevil/condition/',
                'pdps': 'https://snowcrows.com/raids/builds/thief/daredevil/power/'
                #insert deadeye here. Should probably have arrays for each role so we can offer alternatives.
            }
        }

def get_build(spec, role):
    downcased_spec = spec.lower()
    downcased_role = role.lower()
    if downcased_spec in BUILDS:
        if downcased_role in BUILDS[downcased_spec]:
            return BUILDS[downcased_spec][downcased_role]
        else:
            return ""
    else:
        return ""
