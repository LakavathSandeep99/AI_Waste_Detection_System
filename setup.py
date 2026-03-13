from setuptools import setup, find_packages

# Function to read requirements.txt
def get_requirements(file_path: str):
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="AI_Waste_Detection_System",
    version="0.0.1",
    author="Lakavath Sandeep",
    author_email="lakavathsandeep31@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)