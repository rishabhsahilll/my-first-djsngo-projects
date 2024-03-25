#!/bin/bash

# Displaying pip help
echo "Pip Help"
python3.9 -m pip freeze
python3.9 --version

echo "New Env"
python3.9 -m venv venvpy
venvpy\Scripts\activate

# Starting build process
echo "BUILD START"

# Installing dependencies
python3.9 -m pip install -r requirements.txt || { echo "Failed to install dependencies"; exit 1; }

# Making migrations
echo "Make Migration"
python3.9 manage.py makemigrations --noinput || { echo "Failed to make migrations"; exit 1; }
python3.9 manage.py migrate --noinput || { echo "Failed to migrate database"; exit 1; }

# Collecting static files
echo "Collect Static"
python3.9 manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

echo "Build process completed successfully"

# pip install virtualenv
# virtualenv myenv
# source myenv/bin/activate
python3.9 pip install urllib3==1.26.7

# Step 1: Python Version Check
python_version=$(python3 --version | awk '{print $2}')
if [[ ${python_version%%.*} -lt 3 || (${python_version%%.*} -eq 3 && ${python_version#*.} -lt 6) ]]; then
    echo "Error: Python version must be 3.6 or above."
    exit 1
fi

# Step 2: OpenSSL Version Check
openssl_version=$(openssl version | awk '{print $2}')
if [[ "${openssl_version}" < "1.1.1" ]]; then
    echo "Error: OpenSSL version must be 1.1.1 or above."
    exit 1
fi

# Step 3: Update Dependencies
python3.9 pip install --upgrade urllib3 cloudinary

# Step 4: Virtual Environment
virtualenv venv
source venv/bin/activate

# Step 5: Check Dependencies
python3.9 pip list | grep urllib3
python3.9 pip list | grep cloudinary

# Step 6: Search Online
echo "Please search online for specific solutions to your problem."

echo "All steps completed successfully."
exit 0
