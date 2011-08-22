from setuptools import find_packages, setup

setup(
    name='TracEBGanttPlugin', version='0.1',
    packages=find_packages(exclude=['*.tests*']),
    entry_points = """
        [trac.plugins]
        ebgantt.ticketgantt = ebgantt.ticketgantt
    """,
    package_data={'ebgantt': ['templates/*.html']},
)
