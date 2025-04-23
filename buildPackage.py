import os
import shutil
import subprocess

def clean_build_artifacts():
    """Remove old build artifacts."""
    print("Cleaning old build artifacts...")
    for folder in ["dist", "build", "*.egg-info"]:
        if os.path.exists(folder):
            shutil.rmtree(folder, ignore_errors=True)
            print(f"Removed {folder}")
        else:
            print(f"{folder} not found, skipping.")

def build_package():
    """Build the package."""
    print("Building the package...")
    subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])

def install_package():
    """Install the package locally."""
    print("Installing the package locally...")
    dist_folder = "dist"
    files = [f for f in os.listdir(dist_folder) if f.endswith(".whl")]
    if files:
        latest_wheel = os.path.join(dist_folder, files[-1])
        subprocess.check_call(["pip", "install", "--force-reinstall", latest_wheel])
    else:
        print("No .whl file found in dist folder.")

def upload_to_pypi(test=False):
    """Upload the package to PyPI or TestPyPI."""
    print("Uploading the package...")
    print("Use : twine upload dist/*")
    repository_url = "https://test.pypi.org/legacy/" if test else "https://upload.pypi.org/legacy/"
    #subprocess.check_call(["twine", "upload", "dist/*"])

if __name__ == "__main__":
    print("Starting release process...")
    clean_build_artifacts()
    build_package()
    install_package()
    # Change `test=True` to `test=False` to upload to the real PyPI
    upload_to_pypi(test=False)
    print("Release process completed!")