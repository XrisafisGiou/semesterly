"""This file contains all dicts which map a school to its associated object"""
import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "semesterly.settings")
django.setup()

# the smallest block size (in minutes) needed to describe start/end times
# e.g. uoft classes only start on the hour or half hour, so granularity is 30min
school_to_granularity = {
    'jhu': 5,
    'uoft': 30,
    'umd': 5,
    'rutgers': 5,
    'uo': 5,
    'queens': 5,
    'vandy': 5,
    'gw': 5,
    'umich': 5,
    'chapman': 5,
    'salisbury': 5,
}

VALID_SCHOOLS = [
    "uoft",
    "jhu",
    "umd",
    # "uo",
    # "rutgers",
    "queens",
    "vandy",
    "gw",
    "umich",
    "chapman",
    "salisbury",
]

AM_PM_SCHOOLS = [
    "jhu",
    "umd",
    "rutgers",
    "vandy",
    "gw",
    "umich",
    "chapman",
    "salisbury",
]

school_code_to_name = {
    'jhu': 'Johns Hopkins University',
    'uoft': 'University of Toronto',
    'umd': 'University of Maryland',
    'rutgers': 'Rutgers University',
    'uo': 'University of Ottawa',
    'queens': 'Queens University',
    'vandy': 'Vanderbilt University',
    'gw': 'George Washington University',
    'umich': 'University of Michigan',
    'chapman': 'Chapman University',
    'salisbury': 'Salisbury University',
}

_sem = lambda term, year: {'name': term, 'year': year}

school_to_semesters = {
    'jhu': [_sem('Fall', '2017'), _sem('Summer', '2017'), _sem('Spring', '2017'),
            _sem('Fall', '2016')],
    'uoft': [_sem('Winter', '2018'), _sem('Fall', '2017'), _sem('Winter', '2017'), _sem('Fall', '2016')],
    'umd': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    'rutgers': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    # 'uo': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    'queens': [_sem('Winter', '2017'), _sem('Fall', '2016')],
    'vandy': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Fall', '2016')],
    'gw': [_sem('Fall', '2017'), _sem('Spring', '2017')],
    'umich': [_sem('Fall', '2017'), _sem('Winter', '2017'), _sem('Fall', '2016')],
    'chapman': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Fall', '2016')],
    'salisbury': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Winter', '2017'),
                  _sem('Fall', '2016'), _sem('Summer', '2017'), _sem('Interterm', '2017')],
}

old_school_to_semesters = {
    'jhu': [_sem('Fall', '2017'), _sem('Summer', '2017'), _sem('Spring', '2017'),
            _sem('Fall', '2016')],
    'uoft': [_sem('Winter', '2017'), _sem('Fall', '2016')],
    'umd': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    'rutgers': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    # 'uo': [_sem('Spring', '2017'), _sem('Fall', '2016')],
    'queens': [_sem('Winter', '2017'), _sem('Fall', '2016')],
    'vandy': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Fall', '2016')],
    'gw': [_sem('Fall', '2017'), _sem('Spring', '2017')],
    'umich': [_sem('Fall', '2017'), _sem('Winter', '2017'), _sem('Fall', '2016')],
    'chapman': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Fall', '2016')],
    'salisbury': [_sem('Fall', '2017'), _sem('Spring', '2017'), _sem('Winter', '2017'),
                  _sem('Fall', '2016'), _sem('Summer', '2017'), _sem('Interterm', '2017')],
}

# do the imports: assumes all parser follow the same naming conventions:
# schoolname_parsertype where parsertype can be courses, evals, or textbooks
types = ['courses', 'evals', 'textbooks']
for school in VALID_SCHOOLS:
    for p_type in types:
        exec "from scripts.{0}.{0}_{1} import *".format(school, p_type)

# use lambdas to call constructor in a lazy fashion
course_parsers = {
    'uoft': lambda: UofTParser().start(),
    # 'rutgers': parse_rutgers,
    # 'uo': parse_ottawa,
    'gw': lambda: GWParser().parse(),
}

new_course_parsers = {
    'chapman': lambda *args, **kwargs: ChapmanParser(**kwargs),
    'jhu': lambda *args, **kwargs: HopkinsParser(**kwargs),
    'umich': lambda *args, **kwargs: UmichParser(**kwargs),
    'queens': lambda *args, **kwargs: QueensParser(**kwargs),
    'salisbury': lambda *args, **kwargs: SalisburyParser(**kwargs),
    'vandy': lambda *args, **kwargs: VandyParser(**kwargs),
    'umd': lambda *args, **kwargs: UMDParser(**kwargs),
}

new_textbook_parsers = {
    'chapman': lambda *args, **kwargs: ChapmanParser(**kwargs),
    'gw': lambda *args, **kwargs: GWTextbookParser(**kwargs),
    'jhu': lambda *args, **kwargs: JHUTextbookParser(**kwargs),
    'umd': lambda *args, **kwargs: UMDTextbookParser(**kwargs),
    'umich': lambda *args, **kwargs: UmichTextbookParser(**kwargs),
    'vandy': lambda *args, **kwargs: VandyTextbookParser(**kwargs),
}

eval_parsers = {
    'jhu': lambda: HopkinsEvalParser().parse_evals(),
    'uoft': lambda: None,
    'umd': lambda: umdReview().parse_reviews,
    'rutgers': lambda: None,
    'uo': lambda: None,
    'queens': lambda: None,
}

textbook_parsers = {
    'uoft': parse_uoft_textbooks,
    'rutgers': lambda: None,
    'uo': lambda: None,
    'queens': parse_queens_textbooks,
}

final_exams_available = {
    'jhu': [_sem('Spring', '2017')]
}
