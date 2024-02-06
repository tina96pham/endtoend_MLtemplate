import setuptools

with open ("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME= "endtoend_MLtemplate"
AUTHOR_USER_NAME= "tina96pham"
SRC_REPO="mlProject"
GITHUB_URL=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
AUTHOR_EMAIL= "tina96pham@gmail.com"

setuptools.setup(
    name=f"{REPO_NAME}-src",
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="Source code of ml app",
    long_description=  long_description,
    url=  GITHUB_URL,
    project_urls= {
        'Bug Tracker': f'{GITHUB_URL}/issues',
        'Documentation': f'{GITHUB_URL}/blob/main/docs/documentation.md',
        'Source Code': f'{GITHUB_URL}'
    },
    package_dir=  {'':'src'},
    packages= setuptools.find_packages(where='src'),
)
