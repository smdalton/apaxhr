permissions_groups = {
    # access to only their own documents and Employee Profile info
    'tier1': [
        'Applicants',
        'Trainees',
        'Teachers', ],
    # Access to centers, rooms, classes, and
    'tier2': [
        'Head Teachers',
        'Faculty Managers',
    ],
    # Acess to modify employee placements (move employees to new positions)
    'tier3': [
        'Area Managers',
        'HR Managers',
    ],
    'tier4': [
        'Teacher Management Directors',
        'Training Directors',
        'Recruiting Directors',
    ],
    # Access to modify permissions, payroll data, employee positions
    'tier5': [
        'HR Directors',
        # this one is just for development
        'Developers'
    ]
}


def get_all_permissions_groups():
    return [item for sublist in permissions_groups.values() for item in sublist]
