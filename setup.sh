clear

echo "Creating virtual environment..."
python3 -m venv .venv --clear
source .venv/bin/activate

echo "Installing requirements..."
pip install -U -r "requirements.txt"